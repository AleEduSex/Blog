"""Anteprima completa del sito con tutte le modifiche proposte (niente va online).
Copia site/ in <uscita>, poi applica: blog per sezioni, pagine delle sezioni, articoli con sezione e
«Fai una domanda», percorsi con i prezzi nella landing, privacy aggiornata, sitemap.
Con --prova aggiunge la striscia «Versione di prova», noindex ovunque e robots che blocca tutto.
Uso: python3 anteprima.py <uscita> [--prova]"""
import re, sys, shutil, pathlib, runpy, tempfile, subprocess
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]; SITE = ROOT / 'site'; NT = HERE.parent
OUT = pathlib.Path(sys.argv[1]).resolve(); PROVA = '--prova' in sys.argv
assert OUT != SITE.resolve(), 'mai scrivere dentro site/'
shutil.rmtree(OUT, ignore_errors=True); shutil.copytree(SITE, OUT)
SEZ = runpy.run_path(str(HERE / 'sezioni.py'))['SEZIONI']
URL = 'https://aleedusex.net'

# ── 1. pagine generate dal prototipo v7, con i link veri ──
tmp = pathlib.Path(tempfile.mkdtemp())
subprocess.run([sys.executable, str(HERE / 'genmock7.py'), str(tmp)], check=True, stdout=subprocess.DEVNULL)
def link(h):
    h = re.sub(r'href="sezione-([a-z-]+)\.html', r'href="/blog/\1/', h)
    return h.replace('href="blog.html"', 'href="/blog/"')
def parti(gen):
    g = (tmp / gen).read_text()
    return re.search(r'<style>(.*?)</style>', g, re.S).group(1), link(re.search(r'<main id="contenuto">(.*?)</main>', g, re.S).group(1))
def head(h, title, desc, path):
    h = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', h)
    h = re.sub(r'(<meta name="description" content=")[^"]*', rf'\g<1>{desc}', h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*', rf'\g<1>{URL}{path}', h)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*', rf'\g<1>{URL}{path}', h)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*', rf'\g<1>{title}', h)
    return re.sub(r'(<meta property="og:description" content=")[^"]*', rf'\g<1>{desc}', h)
base = (SITE / 'blog/index.html').read_text()
def pagina(gen, title, desc, path):
    css, main = parti(gen)
    h = head(base, title, desc, path).replace('</head>', f'<style>{css}</style>\n</head>')
    return re.sub(r'<main>.*?</main>', lambda m: f'<main id="contenuto">{main}</main>', h, flags=re.S)
desc_blog = re.search(r'<meta name="description" content="([^"]*)', base).group(1)
(OUT / 'blog/index.html').write_text(pagina('blog.html', 'Blog di sessuologia — Alessio Cottonaro, consulente a Torino', desc_blog, '/blog/'))
for s in SEZ:
    d = OUT / 'blog' / s['slug']; d.mkdir()
    (d / 'index.html').write_text(pagina(f'sezione-{s["slug"]}.html', s['titolo_pagina'], s['descrizione'], f'/blog/{s["slug"]}/'))

# ── 2. articoli: sezione nel percorso, In breve in alto, «Fai una domanda», altri della sezione ──
small = {}
for k, v in re.findall(r"'(\w+)': '(<path[^']*)'", (HERE / 'genmock7.py').read_text()): small[k] = v
def ico(k): return f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{small[k]}</svg>'
idx = (SITE / 'blog/index.html').read_text()
titoli = dict(re.findall(r'<a href="/blog/([^"]+)\.html">\s*<p class="post-meta"><time datetime="[^"]+">[^<]+</time><span class="sep">[^<]*</span>\d+ min</p>\s*<h2 class="post-title">([^<]+)</h2>', idx))
date = dict(re.findall(r'<a href="/blog/([^"]+)\.html">\s*<p class="post-meta"><time datetime="([^"]+)"', idx))
DOMANDA = '''<section class="domanda" aria-labelledby="domanda-titolo">
      <h2 id="domanda-titolo">Hai una domanda su questo tema?</h2>
      <p>Scrivila qui, anche senza nome. Non serve la parola giusta. Arriva solo a me e non viene pubblicata: se può servire anche ad altre persone, diventa un articolo, senza niente che ti renda riconoscibile.</p>
      <form name="domanda" method="POST" action="/domanda-inviata.html" data-netlify="true" netlify-honeypot="bot-field">
        <input type="hidden" name="form-name" value="domanda">
        <input type="hidden" name="articolo" value="{slug}">
        <p class="hp"><label>Non compilare questo campo: <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
        <label class="lbl-f" for="domanda-testo">La tua domanda</label>
        <textarea id="domanda-testo" name="domanda" rows="5" maxlength="2000" required></textarea>
        <p class="nota">Non scrivere nome, email o dettagli che ti rendono riconoscibile: così non posso risponderti in privato. Se vuoi una risposta solo per te, scrivimi su WhatsApp.</p>
        <label class="ok"><input type="checkbox" name="privacy" value="si" required><span>Ho letto l’<a href="/legale.html#privacy">informativa privacy</a>.</span></label>
        <button class="btn-burgundy" type="submit">Invia la domanda <span class="arr" aria-hidden="true">→</span></button>
      </form>
    </section>

'''
sez_of = {a: s for s in SEZ for a in s['articoli']}
for f in sorted((OUT / 'blog').glob('*.html')):
    slug = f.stem
    if slug not in sez_of: continue
    s = sez_of[slug]; a = f.read_text()
    old = '<p class="crumb"><a href="/blog/">Blog</a> <span aria-hidden="true">/</span></p>'
    assert old in a, slug
    a = a.replace(old, f'<p class="crumb"><a href="/blog/">Blog</a> <span aria-hidden="true">/</span> <a class="tchip" href="/blog/{s["slug"]}/">{ico(s["icona"])}{s["nome"]}</a></p>')
    ib = re.search(r'\n\s*<aside class="in-breve".*?</aside>', a, re.S)
    if ib:
        a = a.replace(ib.group(0), '')
        a = a.replace('<div class="prose">', ib.group(0).strip().replace('class="in-breve"', 'class="in-breve pz"') + '\n    <div class="prose">', 1)
    a = a.replace('<section class="cta-box"', DOMANDA.replace('{slug}', slug) + '    <section class="cta-box"', 1)
    altri = sorted([x for x in s['articoli'] if x != slug], key=lambda x: date[x], reverse=True)[:4]
    box = (f'<p class="lbl">Altri articoli in {s["nome"]}</p><ul>' + ''.join(f'<li><a href="/blog/{x}.html">{titoli[x]}</a></li>' for x in altri) + '</ul>') if altri \
          else f'<p class="lbl">Questo articolo fa parte di {s["nome"]}</p>'
    old = '<a class="back-link" href="/blog/">← Tutti gli articoli</a>'
    assert old in a, slug
    a = a.replace(old, f'<section class="more pz">{box}<a href="/blog/{s["slug"]}/">Tutta la sezione {s["nome"]}</a></section>\n    {old}')
    f.write_text(a)
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* ── Sezioni del blog (anteprima) ── */
:root { --tape: rgba(214, 196, 163, 0.55); }
.pz { position: relative; background: var(--paper); border-radius: 3px; box-shadow: 0 10px 24px -16px rgba(60,30,20,.35), 0 2px 5px -3px rgba(60,30,20,.25); }
.pz::before { content: ""; position: absolute; top: -11px; left: 50%; width: 86px; height: 24px; transform: translateX(-50%) rotate(-2deg); background: var(--tape); }
.lbl { font-size: 14px; font-style: italic; color: rgba(26,26,26,.7); }
.prose a { overflow-wrap: anywhere; }
.crumb .tchip { display: inline-flex; gap: 6px; align-items: center; background: var(--paper); color: var(--burgundy); border: 1px solid var(--line-soft); border-radius: 999px; padding: 4px 12px 4px 8px; margin-left: 2px; }
.crumb .tchip .ico { width: 18px; height: 18px; color: var(--burgundy); }
.in-breve.pz { border: 0; margin: 8px 0 40px; padding: 28px 26px 22px; }
.in-breve.pz .eyebrow { letter-spacing: 0; text-transform: none; font-size: 15px; font-style: italic; }
.more { margin-top: 56px; padding: 26px 24px 18px; }
.more ul { list-style: none; margin: 10px 0 12px; padding: 0; }
.more li a { display: block; padding: 10px 0; border-top: 1px solid var(--line-soft); font-size: 18px; }
.more > a { font-style: italic; color: var(--burgundy); display: inline-block; padding: 8px 0; }
/* «Fai una domanda» */
.domanda { margin: 56px 0 40px; padding-top: 32px; border-top: 1px solid var(--line); }
.domanda h2 { font-family: var(--display); font-weight: 400; font-size: 30px; line-height: 1.05; letter-spacing: -.02em; }
.domanda > p { margin-top: 12px; font-size: 18px; line-height: 1.6; max-width: 36em; }
.domanda form { display: grid; gap: 12px; margin-top: 20px; max-width: 36em; }
.domanda .hp { position: absolute; left: -9999px; }
.domanda .lbl-f { font-size: 15px; font-style: italic; color: rgba(26,26,26,.75); }
.domanda textarea { width: 100%; font: inherit; font-size: 17px; line-height: 1.5; padding: 14px 16px; background: var(--paper); color: inherit; border: 1px solid var(--line); border-radius: 4px; resize: vertical; }
.domanda textarea:focus-visible, .domanda input:focus-visible { outline: 2px solid var(--burgundy); outline-offset: 2px; }
.domanda .nota { font-size: 15px; line-height: 1.5; color: rgba(26,26,26,.7); }
.domanda .ok { display: flex; gap: 10px; align-items: flex-start; font-size: 15px; line-height: 1.5; min-height: 44px; padding-top: 4px; }
.domanda .ok input { width: 20px; height: 20px; margin-top: 1px; accent-color: var(--burgundy); flex: none; }
.domanda .ok a { color: var(--burgundy); text-decoration: underline; text-underline-offset: 3px; }
.domanda button { justify-self: start; border: 0; cursor: pointer; font: inherit; font-size: 16px; padding: 14px 22px; min-height: 44px; }
''')

# ── 3. pagina «domanda inviata» (dalla 404, stessa testata e footer) ──
p404 = (SITE / '404.html').read_text()
grazie = re.sub(r'<title>.*?</title>', '<title>Domanda inviata — aleedusex</title>', p404)
grazie = re.sub(r'<main>.*?</main>', lambda m: '''<main>
  <section class="wrap" style="padding:96px 0 120px;max-width:40em">
    <h1 style="font-family:var(--display);font-weight:400;font-size:clamp(44px,8vw,72px);line-height:1;letter-spacing:-.03em">Domanda <span class="stamp">arrivata.</span></h1>
    <p style="margin-top:24px;font-size:19px;line-height:1.6">Grazie. La leggo io, e solo io. Se può servire anche ad altre persone, la risposta diventa un articolo, senza niente che ti renda riconoscibile.</p>
    <p style="margin-top:16px;font-size:19px;line-height:1.6">Se invece vuoi parlarne a tu per tu, <a href="/#contatti" style="color:var(--burgundy);text-decoration:underline;text-underline-offset:4px">scrivimi</a>.</p>
    <p style="margin-top:32px"><a class="back-link" href="/blog/">← Torna al blog</a></p>
  </section>
</main>''', grazie, flags=re.S)
(OUT / 'domanda-inviata.html').write_text(grazie)

# ── 4. landing: percorsi con i prezzi dopo il passo 3 di «Come funziona» ──
perc = re.sub(r'<!--.*?-->\s*', '', (NT / 'percorsi/sezione-percorsi.html').read_text(), flags=re.S)
perc = perc.replace('<p style="margin-top:8px;font-size:15px;font-style:italic;color:rgba(26,26,26,.7)">Disdette e rimborsi: come funzionano (pagina «Note legali»).</p>',
                    '<p style="margin-top:8px;font-size:15px;font-style:italic;color:rgba(26,26,26,.7)">Disdette e rimborsi: <a href="/legale.html#disdette" style="color:inherit;text-decoration:underline;text-underline-offset:3px">come funzionano</a>.</p>')
land = (OUT / 'index.html').read_text()
i = land.index('id="funziona"'); j = land.index('</ol>', i) + len('</ol>')
(OUT / 'index.html').write_text(land[:j] + '\n' + perc + land[j:])

# ── 5. pagina legale: modulo domande e disdette (testi da far approvare ad Alessio) ──
leg = (OUT / 'legale.html').read_text()
old = 'Il sito non ha moduli, non usa strumenti di statistica'
assert old in leg
leg = leg.replace(old, 'Il sito non usa strumenti di statistica')
dati = re.search(r'(<p>I dati trattati durante una consulenza.*?</p>)', leg, re.S).group(1)
leg = leg.replace(dati, '''<p><strong>Domande dal blog.</strong> Il modulo «Fai una domanda» in fondo agli articoli raccoglie solo il testo che scrivi e la pagina da cui scrivi. Non chiede nome né email: ti chiedo di non inserire dati che ti rendono riconoscibile. Le domande sono conservate dal servizio di hosting (Netlify) e arrivano a me per email; le uso per scrivere articoli, senza dati di chi le ha fatte, e le cancello entro [periodo da decidere]. Base giuridica: il consenso che dai spuntando la casella (art. 6, par. 1, lett. a GDPR).</p>
        ''' + dati)
note = re.search(r'(<h2>Note legali</h2>.*?</section>)', leg, re.S).group(1)
leg = leg.replace(note, note.replace('</section>', '''</section>

      <section id="disdette">
        <h2>Disdette e rimborsi</h2>
        <p>[Testo da scrivere con Alessio: entro quando si può spostare o disdire un incontro, cosa succede se si salta, come funziona il rimborso dei percorsi.]</p>
      </section>''', 1))
(OUT / 'legale.html').write_text(leg)

# ── 6. sitemap ──
sm = (OUT / 'sitemap.xml').read_text()
sm = sm.replace(f'<url><loc>{URL}/blog/</loc></url>', f'<url><loc>{URL}/blog/</loc></url>\n' + '\n'.join(f'  <url><loc>{URL}/blog/{s["slug"]}/</loc></url>' for s in SEZ), 1)
(OUT / 'sitemap.xml').write_text(sm)

# ── 7. solo per la prova: striscia, noindex, robots ──
if PROVA:
    STRISCIA = '<div style="background:#1A1A1A;color:#F0E7D5;font:15px/1.4 Georgia,serif;text-align:center;padding:9px 16px;position:relative;z-index:100">Versione di prova · il sito vero non è cambiato</div>'
    for f in OUT.rglob('*.html'):
        h = f.read_text()
        if 'noindex' not in h: h = h.replace('<head>', '<head>\n<meta name="robots" content="noindex">', 1)
        h = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + '\n' + STRISCIA, h, count=1)
        f.write_text(h)
    (OUT / 'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('ok', OUT)
