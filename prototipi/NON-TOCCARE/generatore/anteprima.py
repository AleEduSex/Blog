"""Anteprima completa del sito con tutte le modifiche proposte (niente va online).
Versione 2 (4 novembre 2026), dopo il vocale di Alessio: blog sobrio e ordinato (niente scotch),
indice delle sezioni a righe, logo nuovo in testata, blog nella home, percorsi ordinati con i video,
regalo dei 15 minuti più visibile, «Fai una domanda».
Uso: python3 anteprima.py <uscita> [--prova] [--media <cartella con v1.mp4…v5.mp4>]
--prova: striscia «Versione di prova», noindex ovunque, robots che blocca tutto."""
import re, sys, shutil, pathlib, runpy
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]; SITE = ROOT / 'site'; NT = HERE.parent; PERC = NT / 'percorsi'
args = sys.argv[1:]; OUT = pathlib.Path(args[0]).resolve(); PROVA = '--prova' in args
MEDIA = pathlib.Path(args[args.index('--media') + 1]) if '--media' in args else None
assert OUT != SITE.resolve(), 'mai scrivere dentro site/'
shutil.rmtree(OUT, ignore_errors=True); shutil.copytree(SITE, OUT)
SEZ = runpy.run_path(str(HERE / 'sezioni.py'))['SEZIONI']
ic = runpy.run_path(str(HERE / 'icone7.py')); ill = ic['ill7']; ICON_CSS = ic['ICONE7_CSS']
URL = 'https://aleedusex.net'
def rd(p): return (OUT / p).read_text()
def wr(p, s): (OUT / p).write_text(s)

small = dict(re.findall(r"'(\w+)': '(<path[^']*)'", (HERE / 'genmock7.py').read_text()))
def ico(k, cls='ico'): return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{small[k]}</svg>'
def n_art(s): n = len(s['articoli']); return f'{n} articol{"o" if n == 1 else "i"}'

idx = (SITE / 'blog/index.html').read_text()
LI = {}
for m in re.finditer(r'<li class="post-item[^"]*">\s*<a href="/blog/([^"]+)\.html">.*?</li>', idx, re.S): LI[m.group(1)] = m.group(0)
titoli = {k: re.search(r'<h2 class="post-title">([^<]+)', v).group(1) for k, v in LI.items()}
date = {k: re.search(r'datetime="([^"]+)"', v).group(1) for k, v in LI.items()}
sez_of = {a: s for s in SEZ for a in s['articoli']}
assert set(sez_of) == set(LI), 'ogni articolo deve stare in una sezione'

# ── 0. logo nuovo in testata (stesso file ovunque) ──
shutil.copy(PERC / 'logo-testata.png', OUT / 'img/logo-aleedusex.png')
IMG = '<img src="/img/logo-aleedusex.png" alt="AleEduSex" width="487" height="108">'

# ── 1. CSS del blog: sezioni, articoli, domanda, regalo ──
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* ── Logo in testata ── */
.wordmark img { height: 24px; width: auto; }
@media (min-width: 768px) { .wordmark img { height: 28px; } }

/* ── Sezioni del blog ── */
.ico { width: 22px; height: 22px; flex: none; color: var(--burgundy); }
.sez-index { padding-top: 56px; padding-bottom: 8px; }
.sez-index h2, .list-h { font-family: var(--display); font-size: 32px; line-height: 1.05; letter-spacing: -0.02em; }
.sez-list { list-style: none; margin: 20px 0 0; padding: 0; border-top: 1px solid var(--line); }
.sez-list li { border-bottom: 1px solid var(--line-soft); }
.sez-list a { display: grid; grid-template-columns: 26px 1fr auto; align-items: center; gap: 16px; padding: 16px 0; min-height: 64px; }
.sez-list .ico { width: 26px; height: 26px; }
.sez-list .n { font-family: var(--display); font-size: 22px; line-height: 1.12; letter-spacing: -0.015em; transition: color 180ms ease; }
.sez-list .c { font-size: 15px; font-style: italic; color: rgba(26, 26, 26, 0.65); white-space: nowrap; }
.sez-list .ar { display: inline-block; margin-left: 6px; color: var(--burgundy); transition: transform 220ms ease; }
.sez-list a:hover .n { color: var(--burgundy); }
.sez-list a:hover .ar { transform: translateX(4px); }
.list-h { padding-top: 64px; padding-bottom: 4px; }
.post-meta .sez { display: block; margin-top: 6px; font-size: 15px; letter-spacing: 0; text-transform: none; font-style: italic; color: var(--burgundy); white-space: normal; }
@media (min-width: 768px) {
  .sez-index { padding-top: 88px; padding-bottom: 16px; }
  .sez-index h2, .list-h { font-size: 40px; }
  .sez-list a { grid-template-columns: 30px 1fr auto; gap: 24px; padding: 20px 0; }
  .sez-list .ico { width: 30px; height: 30px; }
  .sez-list .n { font-size: 30px; }
  .list-h { padding-top: 96px; }
}
/* pagina di una sezione */
.sez-hero .crumb { padding: 0 0 20px; }
.sez-hero .head { display: grid; gap: 24px; align-items: center; }
.sez-hero h1 { font-size: 46px; line-height: 1; }
.sez-hero .ill { width: 96px; height: 96px; }
@media (min-width: 768px) {
  .sez-hero .head { grid-template-columns: 1fr 180px; gap: 56px; }
  .sez-hero h1 { font-size: 72px; }
  .sez-hero .ill { width: 180px; height: 180px; }
}
.part-h { font-family: var(--display); font-size: 28px; line-height: 1.05; padding-top: 56px; }
.soon { padding-top: 32px; font-size: 17px; font-style: italic; color: rgba(26, 26, 26, 0.75); }
.soon a { color: var(--burgundy); text-decoration: underline; text-underline-offset: 4px; }
.about { padding-top: 24px; padding-bottom: 8px; }
.about h2 { font-family: var(--display); font-size: 32px; line-height: 1.05; margin-bottom: 8px; }
.about p { margin-top: 16px; font-size: 18px; line-height: 1.7; }
.sez-page .cta-box { margin-top: 64px; }
.sez-index.altre { padding-bottom: 96px; }

/* ── Articoli ── */
.prose a { overflow-wrap: anywhere; }
.crumb .tchip { display: inline-flex; gap: 6px; align-items: center; color: var(--burgundy); border: 1px solid var(--line-soft); border-radius: 999px; padding: 4px 12px 4px 8px; margin-left: 2px; }
.crumb .tchip .ico { width: 18px; height: 18px; }
.more { margin-top: 64px; padding-top: 32px; border-top: 1px solid var(--line); }
.more h2 { font-family: var(--display); font-size: 26px; line-height: 1.1; }
.more h2 a { color: var(--burgundy); text-decoration: underline; text-underline-offset: 5px; text-decoration-color: var(--line); }
.more ul { list-style: none; margin: 16px 0 0; padding: 0; }
.more li a { display: block; padding: 12px 0; border-top: 1px solid var(--line-soft); font-size: 18px; line-height: 1.4; }
.more li a:hover { color: var(--burgundy); }

/* ── Regalo dei 15 minuti, più visibile ── */
.cta-box .gift { display: inline-flex; align-items: center; gap: 8px; margin-top: 24px; padding: 12px 18px; min-height: 44px; border: 1px solid rgba(240, 231, 213, 0.45); border-radius: 2px; font-size: 16px; }
.cta-box .gift:hover { border-color: var(--cream); background: rgba(240, 231, 213, 0.08); }

/* ── «Fai una domanda» ── */
.domanda { margin: 56px 0 40px; padding-top: 32px; border-top: 1px solid var(--line); }
.domanda h2 { font-family: var(--display); font-size: 30px; line-height: 1.05; letter-spacing: -.02em; }
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

GIFT_OLD = 'Hai solo una domanda? I primi 15 minuti te li regalo io'
GIFT_NEW = 'Hai solo una domanda? 15 minuti al telefono, te li regalo io'

def sez_rows(lista, cur=None):
    return ''.join(f'<li><a href="/blog/{s["slug"]}/"{" aria-current=page" if s is cur else ""}>{ico(s["icona"])}<span class="n">{s["nome"]}</span>'
                   f'<span class="c">{n_art(s)}<span class="ar" aria-hidden="true">→</span></span></a></li>' for s in lista)
def con_sez(slug, li, lead=True):
    s = sez_of[slug]
    li = li.replace('min</p>', f'min<span class="sez">{s["nome"]}</span></p>', 1)
    return li if lead else li.replace(' post-item--lead', '')

# ── 2. /blog/: il blog di oggi + indice delle sezioni + sezione in ogni articolo ──
b = idx
b = b.replace('<section id="articoli" class="wrap" aria-label="Articoli">',
  f'''<section class="wrap sez-index" aria-labelledby="sezioni-h">
    <h2 id="sezioni-h">Le sezioni</h2>
    <ol class="sez-list">{sez_rows(SEZ)}</ol>
  </section>

  <section id="articoli" class="wrap" aria-labelledby="tutti-h">
    <h2 class="list-h" id="tutti-h">Tutti gli articoli</h2>''')
for slug, li in LI.items(): b = b.replace(li, con_sez(slug, li))
wr('blog/index.html', b)

# ── 3. pagine delle sezioni: /blog/<sezione>/ ──
def head(h, title, desc, path):
    h = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', h)
    h = re.sub(r'(<meta name="description" content=")[^"]*', rf'\g<1>{desc}', h)
    for k in ('<link rel="canonical" href="', '<meta property="og:url" content="'):
        h = re.sub('(' + re.escape(k) + ')[^"]*', rf'\g<1>{URL}{path}', h)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*', rf'\g<1>{title}', h)
    return re.sub(r'(<meta property="og:description" content=")[^"]*', rf'\g<1>{desc}', h)
art0 = rd('blog/sesso-vanilla-cosa-significa.html')
CTA = re.search(r'<section class="cta-box".*?</section>', art0, re.S).group(0)
base = rd('blog/index.html')
for i, s in enumerate(SEZ):
    posts = sorted(s['articoli'], key=lambda a: date[a], reverse=True)
    def lista(arts): return '<ol class="post-list">' + ''.join(con_sez(a, LI[a], lead=False).replace(f'<span class="sez">{s["nome"]}</span>', '') for a in arts) + '</ol>'
    if s.get('parti'):
        piene = [p for p in s['parti'] if p['articoli']]; vuote = [p['nome'] for p in s['parti'] if not p['articoli']]
        corpo = ''.join(f'<h2 class="part-h">{p["nome"]}</h2>{lista(p["articoli"])}' for p in piene)
        if vuote: corpo += f'<p class="soon">In arrivo: {" e ".join(vuote)}. <a href="/#contatti">Scrivimi cosa vorresti leggere</a>.</p>'
    else:
        corpo = f'<h2 class="list-h">Gli articoli</h2>{lista(posts)}'
    nomi = [q['nome'] + '.' for q in s.get('parti', [])]
    def gr(t):
        for n in nomi:
            if t.startswith(n): return f'<strong>{n}</strong>' + t[len(n):]
        return t
    main = f'''<main id="contenuto" class="sez-page">
  <section class="blog-hero sez-hero">
    <div class="wrap">
      <p class="crumb"><a href="/blog/">Blog</a> <span aria-hidden="true">/</span></p>
      <div class="head"><div><h1>{s["h1"]}</h1><p class="intro">{s["intro"][0]}</p></div>{ill(s["icona"])}</div>
    </div>
  </section>
  <section class="wrap" aria-label="Articoli della sezione">{corpo}</section>
  <div class="wrap-narrow">
    <section class="about" aria-labelledby="about-h"><h2 id="about-h">Su questa sezione</h2>{"".join(f"<p>{gr(p)}</p>" for p in s["intro"][1:])}</section>
    {CTA}
  </div>
  <section class="wrap sez-index altre" aria-labelledby="altre-h"><h2 id="altre-h">Le altre sezioni</h2><ol class="sez-list">{sez_rows([o for o in SEZ if o is not s])}</ol></section>
</main>'''
    h = head(base, s['titolo_pagina'], s['descrizione'], f'/blog/{s["slug"]}/').replace('</head>', f'<style>:root{{--fg:var(--burgundy);--bg:var(--paper);--muted:rgba(26,26,26,.7)}}{ICON_CSS}</style>\n</head>')
    h = h.replace('<a href="/blog/" aria-current="page">Blog</a>', '<a href="/blog/">Blog</a>')
    h = re.sub(r'<main>.*?</main>', lambda m: main, h, flags=re.S)
    (OUT / 'blog' / s['slug']).mkdir(); wr(f'blog/{s["slug"]}/index.html', h)

# ── 4. articoli: sezione nel percorso, «Fai una domanda», altri della sezione, regalo ──
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
for slug in LI:
    s = sez_of[slug]; a = rd(f'blog/{slug}.html')
    old = '<p class="crumb"><a href="/blog/">Blog</a> <span aria-hidden="true">/</span></p>'; assert old in a, slug
    a = a.replace(old, f'<p class="crumb"><a href="/blog/">Blog</a> <span aria-hidden="true">/</span> <a class="tchip" href="/blog/{s["slug"]}/">{ico(s["icona"])}{s["nome"]}</a></p>')
    a = a.replace('<section class="cta-box"', DOMANDA.replace('{slug}', slug) + '    <section class="cta-box"', 1)
    altri = sorted([x for x in s['articoli'] if x != slug], key=lambda x: date[x], reverse=True)[:4]
    if altri:
        more = f'<section class="more" aria-labelledby="more-h"><h2 id="more-h">Altri articoli in <a href="/blog/{s["slug"]}/">{s["nome"]}</a></h2><ul>' + \
               ''.join(f'<li><a href="/blog/{x}.html">{titoli[x]}</a></li>' for x in altri) + '</ul></section>'
    else:
        more = f'<section class="more"><h2>Fa parte di <a href="/blog/{s["slug"]}/">{s["nome"]}</a></h2></section>'
    old = '<a class="back-link" href="/blog/">← Tutti gli articoli</a>'; assert old in a, slug
    a = a.replace(old, f'{more}\n    {old}')
    wr(f'blog/{slug}.html', a)
for f in list(OUT.rglob('*.html')):
    h = f.read_text()
    if GIFT_OLD in h: f.write_text(h.replace(GIFT_OLD, GIFT_NEW))

# ── 5. pagina «domanda inviata» ──
grazie = re.sub(r'<title>.*?</title>', '<title>Domanda inviata — aleedusex</title>', rd('404.html'))
grazie = re.sub(r'<main>.*?</main>', lambda m: '''<main>
  <section class="wrap" style="padding:96px 0 120px;max-width:40em">
    <h1 style="font-family:var(--display);font-weight:400;font-size:clamp(44px,8vw,72px);line-height:1;letter-spacing:-.03em">Domanda <span class="stamp">arrivata.</span></h1>
    <p style="margin-top:24px;font-size:19px;line-height:1.6">Grazie. La leggo io, e solo io. Se può servire anche ad altre persone, la risposta diventa un articolo, senza niente che ti renda riconoscibile.</p>
    <p style="margin-top:16px;font-size:19px;line-height:1.6">Se invece vuoi parlarne a tu per tu, <a href="/#contatti" style="color:var(--burgundy);text-decoration:underline;text-underline-offset:4px">scrivimi</a>.</p>
    <p style="margin-top:32px"><a class="back-link" href="/blog/">← Torna al blog</a></p>
  </section>
</main>''', grazie, flags=re.S)
wr('domanda-inviata.html', grazie)

# ── 6. landing ──
land = rd('index.html')
# 6a. logo
old = '<a href="#top" class="font-display text-brand-burgundy text-[22px] md:text-[26px] leading-none tracking-tightish lowercase">aleedusex</a>'; assert old in land
land = land.replace(old, '<a href="#top" class="block"><img src="/img/logo-aleedusex.png" alt="AleEduSex" width="487" height="108" class="h-[24px] md:h-[28px] w-auto"></a>')
# 6b. regalo più visibile nell'hero (era grigio 14px)
land = land.replace('class="alt-link mt-4 inline-flex items-center gap-1.5 text-[14px] italic text-brand-ink/60 hover:text-brand-burgundy transition-colors"',
                    'class="alt-link mt-5 inline-flex items-center gap-1.5 text-[16px] md:text-[17px] italic text-brand-burgundy underline underline-offset-4 decoration-brand-burgundy/30 hover:decoration-brand-burgundy transition-colors"', 1)
# 6c. regalo nel passo 1, come primo passo possibile
old = '<p class="font-body italic text-brand-burgundy/80 text-[16px]">— Non c\'è una segreteria. Non ci sono moduli infiniti.</p>'; assert old in land
land = land.replace(old, old + '''
          <a href="https://wa.me/393273003855" target="_blank" rel="noreferrer" class="group mt-8 flex flex-col sm:flex-row sm:items-center gap-3 sm:gap-6 max-w-2xl border border-brand-burgundy/35 px-6 py-5 hover:border-brand-burgundy transition-colors">
            <span class="font-display text-brand-burgundy text-[40px] leading-none whitespace-nowrap">15 min</span>
            <span class="font-body text-brand-ink/85 text-[17px] leading-[1.5]"><strong class="font-semibold">In regalo, al telefono.</strong> Se hai solo una domanda, o vuoi capire se ha senso iniziare. Scrivimi e ci sentiamo. <span class="text-brand-burgundy inline-block transition-transform group-hover:translate-x-1" aria-hidden="true">→</span></span>
          </a>''')
# 6d. video della prima consulenza nel passo 2
def video(n, durata, label='Guarda il video'):
    return f'''<details class="mt-5 group/v">
              <summary class="list-none [&::-webkit-details-marker]:hidden cursor-pointer inline-flex items-center gap-2.5 min-h-[44px] text-[16px] italic text-brand-burgundy">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><circle cx="12" cy="12" r="10.5"/><path d="M10 8.2v7.6l6-3.8z" fill="currentColor" stroke="none"/></svg>
                <span class="underline underline-offset-4 decoration-brand-burgundy/30">{label}</span><span class="not-italic text-brand-ink/55 text-[14px]">{durata}</span>
              </summary>
              <video class="mt-4 w-full max-w-[280px] aspect-[9/16] bg-brand-ink/10 rounded-[2px]" controls preload="none" playsinline poster="/video/{n}.jpg"><source src="/video/{n}.mp4" type="video/mp4"></video>
            </details>'''
old = '<li>60&nbsp;€</li>\n          </ul>'; assert old in land
land = land.replace(old, old + '\n          ' + video('prima-consulenza', '44 s', 'Come funziona, in un video'), 1)
# 6e. percorsi a righe, nello stile di «Come funziona»
P = [
 ('al-cuore-del-problema', 'Al cuore del problema', 'Cinque incontri per capire dove ti sei bloccato e cosa fare, con il metodo DEOPIARCA della Scuola di sessuologia di Torino.',
  ['Da solo o in coppia', '5 incontri da 60 minuti', 'Ogni due settimane'], '450&nbsp;€', 'tutto il percorso', '58 s'),
 ('dialogo-positivo-sul-desiderio', 'Dialogo positivo sul desiderio', 'Per coppie con desideri diversi, che non riescono più a parlarne senza ferirsi.',
  ['Coppie, in piccolo gruppo', '3 incontri da 90 minuti', 'Gruppi di 4 coppie'], '240&nbsp;€', 'a coppia · 300&nbsp;€ se vieni da solo', '1 min 56'),
 ('laboratorio-del-piacere-consapevole', 'Laboratorio del piacere consapevole', 'Corpo, desiderio, comunicazione, sex toys. Niente nudità né pratiche esplicite.',
  ['Coppie, in piccolo gruppo', '4 incontri da 90 minuti', 'Massimo 3 coppie'], '400&nbsp;€', 'a coppia', '2 min 16'),
 ('parliamo-di-sessualita-ai-figli', 'Parliamo di sessualità ai figli', 'Per genitori con figli tra 4 e 18 anni: come rispondere alle domande, età per età.',
  ['Genitori, in piccolo gruppo', '4 incontri da 90 minuti', 'Massimo 8 persone'], '280&nbsp;€', '', '1 min 46'),
]
righe = ''.join(f'''
        <li class="grid md:grid-cols-12 gap-x-10 gap-y-4 py-10 md:py-12 border-b border-brand-line/30">
          <div class="md:col-span-6">
            <h4 class="font-display text-brand-ink text-[30px] md:text-[38px] leading-[1.02] tracking-tighter2">{nome}</h4>
            <p class="mt-4 font-body text-brand-ink/80 text-[17px] md:text-[18px] leading-[1.6] max-w-xl">{desc}</p>
            {video(slug, durata)}
          </div>
          <ul class="md:col-span-3 md:pt-3 font-body text-brand-ink/75 text-[16px] leading-[1.9]">{"".join(f"<li>{m}</li>" for m in meta)}</ul>
          <div class="md:col-span-3 md:pt-2 md:text-right">
            <p class="font-display italic text-brand-burgundy text-[36px] md:text-[44px] leading-none">{prezzo}</p>
            {f'<p class="mt-2 font-body italic text-brand-ink/60 text-[15px]">{sotto}</p>' if sotto else ''}
          </div>
        </li>''' for slug, nome, desc, meta, prezzo, sotto, durata in P)
PERCORSI = f'''

    <!-- Percorsi (prova): dopo la prima consulenza, se serve -->
    <div id="percorsi" class="mt-24 md:mt-36 pt-16 md:pt-24 border-t border-brand-line/40">
      <div class="grid md:grid-cols-12 gap-8 md:gap-16 mb-10 md:mb-14">
        <h3 class="md:col-span-6 font-display text-brand-ink text-[40px] sm:text-[52px] md:text-[64px] leading-[0.98] tracking-tighter2 reveal">
          I percorsi, <span class="italic text-brand-burgundy">se servono.</span>
        </h3>
        <p class="md:col-span-5 md:col-start-8 self-end font-body text-brand-ink/80 text-[18px] md:text-[19px] leading-[1.6] reveal" data-delay="1">
          Te li propongo dopo la prima consulenza, solo se hanno senso per te. Ognuno ha un obiettivo chiaro e un numero di incontri definito. Si prenotano come la prima consulenza: mi scrivi e ne parliamo.
        </p>
      </div>
      <ul class="border-t border-brand-line/50">{righe}
      </ul>
      <div class="mt-10 flex flex-col sm:flex-row sm:items-center gap-5 sm:gap-8">
        <a href="#contatti" class="btn-burgundy self-start">Scrivimi per un percorso <span class="arr" aria-hidden="true">→</span></a>
        <a href="/legale.html#disdette" class="font-body italic text-brand-ink/70 text-[15px] underline underline-offset-4 decoration-brand-line hover:text-brand-burgundy">Disdette e rimborsi: come funzionano</a>
      </div>
    </div>'''
i = land.index('id="funziona"'); j = land.index('</ol>', i) + len('</ol>')
land = land[:j] + PERCORSI + land[j:]
# 6f. il blog nella home, dopo «Di cosa possiamo parlare»
righe_b = ''.join(f'''
          <li class="border-b border-brand-line/25"><a href="/blog/{s["slug"]}/" class="group grid grid-cols-[26px_1fr_auto] md:grid-cols-[30px_1fr_auto] items-center gap-4 md:gap-6 py-4 md:py-5 min-h-[64px]">
            {ico(s["icona"], "w-[26px] h-[26px] md:w-[30px] md:h-[30px] text-brand-burgundy")}
            <span class="font-display text-brand-ink text-[21px] md:text-[27px] leading-[1.12] tracking-tightish group-hover:text-brand-burgundy transition-colors">{s["nome"]}</span>
            <span class="font-body italic text-brand-ink/60 text-[15px] whitespace-nowrap">{n_art(s)} <span class="text-brand-burgundy inline-block transition-transform group-hover:translate-x-1" aria-hidden="true">→</span></span>
          </a></li>''' for s in SEZ)
ultimo = max(LI, key=lambda a: date[a])
BLOG = f'''

<!-- ═════════════════════════ IL BLOG (prova) ═════════════════════════ -->
<section id="dal-blog" class="bg-brand-paper border-y border-brand-line/30">
  <div class="max-w-[1280px] mx-auto px-6 md:px-10 py-20 md:py-28">
    <div class="grid md:grid-cols-12 gap-12 md:gap-16">
      <div class="md:col-span-5 reveal">
        <h2 class="font-display text-brand-ink text-[42px] sm:text-[56px] md:text-[64px] leading-[0.98] tracking-tighter2">
          Se preferisci <span class="italic text-brand-burgundy">leggere prima.</span>
        </h2>
        <p class="mt-6 font-body text-brand-ink/80 text-[18px] md:text-[19px] leading-[1.6] max-w-md">
          Nel blog rispondo alle domande che si fanno a bassa voce, con risposte scritte in chiaro. Un tema alla volta, diviso in cinque sezioni.
        </p>
        <p class="mt-8 font-body text-[16px] text-brand-ink/70">Ultimo articolo:<br><a href="/blog/{ultimo}.html" class="font-display text-brand-ink text-[22px] leading-[1.2] hover:text-brand-burgundy underline underline-offset-4 decoration-brand-line">{titoli[ultimo]}</a></p>
        <a href="/blog/" class="btn-burgundy mt-10">Vai al blog <span class="arr" aria-hidden="true">→</span></a>
      </div>
      <ol class="md:col-span-7 border-t border-brand-line/50 reveal" data-delay="1">{righe_b}
      </ol>
    </div>
  </div>
</section>
'''
k = land.index('<section id="perche-me"'); k = land.rfind('\n', 0, land.rfind('<!--', 0, k))
land = land[:k] + BLOG + land[k:]
# 6g. contatti: il regalo accanto al prezzo, con lo stesso timbro
old = '''<div class="price-stamp text-center">'''; assert land.count(old) == 1
land = land.replace('<div class="md:col-span-4 flex justify-start md:justify-end reveal" data-delay="1">\n        ' + old,
  '''<div class="md:col-span-4 grid grid-cols-2 md:grid-cols-1 gap-4 md:justify-items-end reveal" data-delay="1">
        <div class="price-stamp text-center w-full md:w-[220px]">
          <div class="text-[10px] tracking-[0.32em] uppercase opacity-80 mb-1">Prima di tutto</div>
          <div class="text-[56px] md:text-[68px] leading-none">15′</div>
          <div class="text-[10px] tracking-[0.32em] uppercase opacity-80 mt-2">in regalo</div>
        </div>
        ''' + old.replace('text-center', 'text-center w-full md:w-[220px]'))
wr('index.html', land)
# video e copertine
(OUT / 'video').mkdir(exist_ok=True)
NOMI = {'v1': 'prima-consulenza', 'v2': 'al-cuore-del-problema', 'v3': 'dialogo-positivo-sul-desiderio', 'v4': 'laboratorio-del-piacere-consapevole', 'v5': 'parliamo-di-sessualita-ai-figli'}
for v, n in NOMI.items():
    shutil.copy(PERC / 'poster' / f'{v}.jpg', OUT / 'video' / f'{n}.jpg')
    if MEDIA and (MEDIA / f'{v}.mp4').exists(): shutil.copy(MEDIA / f'{v}.mp4', OUT / 'video' / f'{n}.mp4')
    else: print('ATTENZIONE: manca il video', v, '(passa --media)')

# ── 7. pagina legale: modulo domande e disdette (testi da far approvare ad Alessio) ──
leg = rd('legale.html')
old = 'Il sito non ha moduli, non usa strumenti di statistica'; assert old in leg
leg = leg.replace(old, 'Il sito non usa strumenti di statistica')
dati = re.search(r'(<p>I dati trattati durante una consulenza.*?</p>)', leg, re.S).group(1)
leg = leg.replace(dati, '''<p><strong>Domande dal blog.</strong> Il modulo «Fai una domanda» in fondo agli articoli raccoglie solo il testo che scrivi e la pagina da cui scrivi. Non chiede nome né email: ti chiedo di non inserire dati che ti rendono riconoscibile. Le domande sono conservate dal servizio di hosting (Netlify) e arrivano a me per email; le uso per scrivere articoli, senza dati di chi le ha fatte, e le cancello entro [periodo da decidere]. Base giuridica: il consenso che dai spuntando la casella (art. 6, par. 1, lett. a GDPR).</p>
        ''' + dati)
note = re.search(r'(<h2>Note legali</h2>.*?</section>)', leg, re.S).group(1)
leg = leg.replace(note, note.replace('</section>', '''</section>

      <section id="disdette">
        <h2>Disdette e rimborsi</h2>
        <p>[Testo in arrivo da Alessio: entro quando si può spostare o disdire un incontro, cosa succede se si salta, come funziona il rimborso dei percorsi.]</p>
      </section>''', 1))
wr('legale.html', leg)

# ── 8. sitemap ──
sm = rd('sitemap.xml')
sm = sm.replace(f'<url><loc>{URL}/blog/</loc></url>', f'<url><loc>{URL}/blog/</loc></url>\n' + '\n'.join(f'  <url><loc>{URL}/blog/{s["slug"]}/</loc></url>' for s in SEZ), 1)
wr('sitemap.xml', sm)

# logo in testata, su tutte le pagine (alla fine, dopo che le pagine sono state riscritte)
for f in OUT.rglob('*.html'):
    h = f.read_text()
    h = h.replace('<a class="wordmark" href="/">aleedusex</a>', f'<a class="wordmark" href="/">{IMG}</a>')
    f.write_text(h)

# ── 9. solo per la prova ──
if PROVA:
    STRISCIA = '<div style="background:#1A1A1A;color:#F0E7D5;font:15px/1.4 Georgia,serif;text-align:center;padding:9px 16px;position:relative;z-index:100">Versione di prova · il sito vero non è cambiato</div>'
    for f in OUT.rglob('*.html'):
        h = f.read_text()
        if 'noindex' not in h: h = h.replace('<head>', '<head>\n<meta name="robots" content="noindex">', 1)
        h = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + '\n' + STRISCIA, h, count=1)
        f.write_text(h)
    (OUT / 'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('ok', OUT)
