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
.sez-hero h1 { font-size: clamp(34px, 11vw, 46px); line-height: 1; }
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
# 6b. HOME v3 (restyle dopo la revisione del 4/11: Impeccable distill + Taste «split stage»)
GIFT_URL = 'https://wa.me/393273003855?text=Ciao%20Alessio%2C%20vorrei%20fissare%20la%20telefonata%20gratuita%20di%2015%20minuti.'
EMAIL_ENT = re.search(r'href="mailto:([^"]+)"', land).group(1)
def video(n, durata, titolo):
    # si apre grande, su fondo scuro (script in fondo alla pagina); senza JavaScript apre il file del video
    return f'''<a class="apri-video mt-5 inline-flex items-center gap-2.5 min-h-[44px] font-body text-[16px] text-brand-burgundy" href="/video/{n}.mp4" data-poster="/video/{n}.jpg" data-titolo="{titolo}">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><circle cx="12" cy="12" r="10.5"/><path d="M10 8.2v7.6l6-3.8z" fill="currentColor" stroke="none"/></svg>
              <span class="underline underline-offset-4 decoration-brand-burgundy/35">Guarda il video</span> <span class="text-brand-ink/80 text-[15px]">{durata}</span>
            </a>'''
PIU = '<svg class="piu shrink-0 mt-2 text-brand-burgundy" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><line x1="12" y1="5" x2="12" y2="19"/></svg>'
FRASI = [
 ('Non desidero più il mio partner, e non capisco perché.', 'Il desiderio cambia nel tempo, e quasi mai per colpa di qualcuno. Si può capire cosa si è spento e da dove ripartire.', '/blog/difficolta-e-blocchi/', 'Difficoltà e blocchi'),
 ('Ho paura di non essere all’altezza.', 'Capita a tante persone, a ogni età. Non è un difetto: è un circolo che si può interrompere.', '/blog/ansia-da-prestazione-sessuale.html', 'Ansia da prestazione'),
 ('Ho perso il piacere e non so quando è successo.', 'A volte il piacere si spegne piano, senza un motivo chiaro. Ripartire dal corpo aiuta a ritrovarlo.', '/blog/corpo-piacere-e-fantasie/', 'Corpo, piacere e fantasie'),
 ('Con il mio partner abbiamo smesso di parlarne.', 'Il silenzio si sedimenta e le parole diventano più difficili. Si può ricominciare da piccole frasi vere.', '/blog/come-parlare-di-sesso-con-il-partner.html', 'Come parlare di sesso con il partner'),
 ('Non mi ritrovo più, nelle relazioni o nella mia sessualità.', 'Non serve avere già le risposte. Si parte da quello che senti adesso, senza etichette.', '#contatti', 'Scrivimi'),
]
frasi = ''.join(f'''
        <li><details class="frase">
          <summary class="list-none [&::-webkit-details-marker]:hidden cursor-pointer flex items-start justify-between gap-6 py-4 min-h-[44px]"><span class="testo font-display text-brand-ink text-[22px] md:text-[26px] leading-[1.22] tracking-tightish">«{f}»</span>{PIU}</summary>
          <div class="pb-6 font-body text-[17px] leading-[1.6] text-brand-ink max-w-[34em]">{d} <a href="{u}" class="text-brand-burgundy underline underline-offset-4 decoration-brand-burgundy/35">{"Leggi: " if u != "#contatti" else ""}{t} →</a></div>
        </details></li>''' for f, d, u, t in FRASI)
# diagramma di oggi, senza ombra; sotto il timbro il nome AleEduSex
diag = re.search(r'(<svg class="pm-map pm-map-h".*?</svg>\s*<svg class="pm-map pm-map-v".*?</svg>)', land, re.S).group(1)
diag = re.sub(r'\s*<defs>.*?</defs>', '', diag, flags=re.S).replace(' filter="url(#pm-shadow-h)"', '').replace(' filter="url(#pm-shadow-v)"', '')
assert diag.count('— Alessio') == 2; diag = diag.replace('— Alessio', 'AleEduSex')
DIAG = f'<div class="diag-card reveal">{diag}</div>'
# blog in home v8 (Taste «index with preview»): le frasi degli ultimi articoli grandi, la copertina a fianco cambia con la riga
def dati(slug):
    a = (SITE / f'blog/{slug}.html').read_text()
    fr = re.search(r'<p class="frase">([^<]+)</p>', a); cv = re.search(r'<figure class="cover">\s*<img src="/blog/img/([^"]+)"', a)
    return (fr.group(1).strip() if fr else ''), (cv.group(1) if cv else None)
ultimi = sorted(LI, key=lambda a: date[a], reverse=True)[:4]
def riga(slug):
    fr, cv = dati(slug)
    img = f'<img src="/blog/img/mini/{cv}" alt="" width="1040" height="650" loading="lazy" decoding="async">' if cv else ''
    return f'''
        <li><a href="/blog/{slug}.html">{img}<span class="f">{fr}</span><span class="t">{titoli[slug]} <span class="ar" aria-hidden="true">→</span></span></a></li>'''
sez_home = ''.join(f'<li><a href="/blog/{s["slug"]}/">{ico(s["icona"], "ico-s")}<span>{s["nome"]}</span></a></li>' for s in SEZ)
BLOG = f'''<!-- ═══════ Dal blog: le frasi degli ultimi articoli, con la copertina a fianco ═══════ -->
<section id="dal-blog" class="bg-brand-ink text-brand-cream">
  <div class="max-w-[1280px] mx-auto px-6 md:px-10 py-20 md:py-32">
    <div class="grid lg:grid-cols-12 gap-8 lg:gap-16 items-end">
      <h2 class="lg:col-span-7 font-display text-brand-cream text-[44px] sm:text-[56px] lg:text-[72px] leading-[0.98] tracking-tighter2 reveal">Se preferisci <span class="italic">leggere prima.</span></h2>
      <div class="lg:col-span-5 reveal" data-delay="1">
        <p class="font-body text-brand-cream text-[18px] leading-[1.6]">Nel blog ogni articolo parte da una frase vera: quella che di solito non si dice a nessuno. Scegli la tua.</p>
        <a href="/blog/" class="btn-cream-on-burgundy mt-8">Vai al blog <span aria-hidden="true">→</span></a>
      </div>
    </div>
    <ul class="vetrina mt-14 md:mt-20 reveal" data-delay="1">{"".join(riga(x) for x in ultimi)}
    </ul>
    <nav class="sez-home mt-14 md:mt-20 reveal" aria-labelledby="sez-home-h">
      <h3 id="sez-home-h">Oppure parti da una sezione</h3>
      <ul>{sez_home}</ul>
    </nav>
  </div>
</section>'''
PREZZO_SINGOLO = 100   # incontro singolo da 60 minuti: DA CONFERMARE con Alessio (serve per mostrare il risparmio)
# percorsi: prima scegli per chi (da solo, in coppia, in gruppo), poi vedi solo quelli adatti; funziona anche senza JavaScript
P = [
 ('al-cuore-del-problema', 'Al cuore del problema', '450&nbsp;€', 'solo coppia', 'Cinque incontri per capire dove si è bloccato qualcosa e cosa fare, con il metodo DEOPIARCA della Scuola di sessuologia di Torino.', 'Da solo o in coppia. 5 incontri da 60 minuti, ogni due settimane. Il prezzo è per tutto il percorso.', '58 s'),
 ('dialogo-positivo-sul-desiderio', 'Dialogo positivo sul desiderio', '240&nbsp;€', 'coppia gruppo solo', 'Per coppie con desideri diversi, che non riescono più a parlarne senza ferirsi.', 'In piccolo gruppo: 3 incontri da 90 minuti, gruppi di 4 coppie. 240 € a coppia, 300 € se partecipi senza partner.', '1 min 56'),
 ('laboratorio-del-piacere-consapevole', 'Laboratorio del piacere consapevole', '400&nbsp;€', 'coppia gruppo', 'Per coppie: corpo, desiderio, comunicazione, sex toys. Niente nudità né pratiche esplicite.', 'In piccolo gruppo: 4 incontri da 90 minuti, al massimo 3 coppie. Prezzo a coppia.', '2 min 16'),
 ('parliamo-di-sessualita-ai-figli', 'Parliamo di sessualità ai figli', '280&nbsp;€', 'gruppo', 'Per genitori con figli tra 4 e 18 anni: come rispondere alle domande, età per età.', 'In piccolo gruppo: 4 incontri da 90 minuti, al massimo 8 persone.', '1 min 46'),
]
def risparmio(slug, prezzo):
    tot = int(re.sub(r'\D', '', prezzo))
    if slug == 'al-cuore-del-problema':
        singoli = 5 * PREZZO_SINGOLO
        if singoli > tot:
            return (f'<span class="barrato" aria-label="invece di {singoli} euro con 5 incontri singoli"><s>{singoli}&nbsp;€</s></span><span class="val">{prezzo}</span>'
                    f'<span class="risparmi">Risparmi {singoli - tot}&nbsp;€</span>')
    n = {'dialogo-positivo-sul-desiderio': 3, 'laboratorio-del-piacere-consapevole': 4, 'parliamo-di-sessualita-ai-figli': 4}.get(slug)
    extra = f'<span class="a-incontro">{round(tot / n)}&nbsp;€ a incontro da 90 minuti</span>' if n else ''
    return f'<span class="val">{prezzo}</span>{extra}'
voci = ''.join(f'''
          <li class="voce pt-8 pb-2" data-per="{per}">
            <div class="riga"><span class="font-display text-brand-ink text-[26px] md:text-[30px] leading-[1.12] tracking-tightish">{nome}</span><span class="prezzi">{risparmio(slug, prezzo)}</span></div>
            <p class="mt-2 font-body text-[17px] leading-[1.6] text-brand-ink max-w-[38em]">{desc}</p>
            {video(slug, durata, nome)}
            <p class="mt-3 font-body text-[16px] leading-[1.55] text-brand-ink/80 max-w-[38em]">{meta}</p>
          </li>''' for slug, nome, prezzo, per, desc, meta, durata in P)
scelte = ''.join(f'<input type="radio" name="per" id="per-{k}" value="{k}"{" checked" if k == "tutti" else ""}><label for="per-{k}">{t}</label>' for k, t in [('tutti', 'Tutti'), ('solo', 'Da solo'), ('coppia', 'In coppia'), ('gruppo', 'In gruppo')])
PERCORSI = f'''<!-- ═══════ I percorsi: prima scegli per chi ═══════ -->
<section id="percorsi" class="bg-brand-cream">
  <div class="max-w-[1280px] mx-auto px-6 md:px-10 py-20 md:py-36">
    <div class="grid lg:grid-cols-12 gap-10 md:gap-16">
      <div class="lg:col-span-4">
        <h2 class="font-display text-brand-ink text-[44px] md:text-[56px] lg:text-[64px] leading-[0.98] tracking-tighter2 reveal">I percorsi, <span class="italic text-brand-burgundy">se servono.</span></h2>
        <p class="mt-6 font-body text-brand-ink text-[18px] leading-[1.6] reveal" data-delay="1">Te li propongo dopo la prima consulenza, solo se hanno senso per te. Ognuno ha un obiettivo chiaro e un numero di incontri definito. Si prenotano come la prima consulenza.</p>
        <a href="#contatti" class="btn-burgundy mt-10 reveal" data-delay="2">Scrivimi per un percorso <span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="lg:col-span-8 reveal" data-delay="1">
        <fieldset class="per">
          <legend class="font-body font-semibold text-[17px] text-brand-ink mb-3">Per chi è?</legend>
          {scelte}
          <ul class="voci">{voci}
          </ul>
          <p class="nota-singolo mt-6 font-body text-[15px] text-brand-ink/80">Un incontro singolo costa {PREZZO_SINGOLO}&nbsp;€ <span class="text-brand-burgundy">[prezzo d’esempio, da confermare con Alessio]</span>.</p>
        </fieldset>
      </div>
    </div>
  </div>
</section>'''
VIDEO_PRIMA = video('prima-consulenza', '44 s', 'come funziona la prima consulenza')
# FAQ come prima (fisarmonica numerata, titolo di prima), con le 5 risposte nuove
faq_old = re.search(r'<section id="faq".*?</section>', (SITE / 'index.html').read_text(), re.S).group(0)
lis = re.findall(r'<li>\s*<details.*?</li>', faq_old, re.S); modello_li = lis[1]
QA = [
 ('Non so se è abbastanza grave da scriverti.', 'Non c’è un livello minimo di disagio per meritarsi un’ora di chiarezza. Se ci pensi da mesi, è già un buon motivo.'),
 ('Il problema è del mio partner, posso venire senza?', 'Sì, succede spesso. Partiamo da quello che dipende da te. Se serve coinvolgere l’altra persona, lo decidiamo insieme.'),
 ('Online funziona come in presenza?', 'Per molte persone sì. Ci vediamo in videochiamata e l’ora è tutta tua. A volte parlarne da casa propria aiuta.'),
 ('Quanto costa, in tutto?', 'La prima consulenza costa 60 €. Se poi serve un percorso, costo e numero di incontri li trovi qui sopra e li decidiamo prima di iniziare. Nessuna sorpresa.'),
 ('Quello che dico resta tra noi?', 'Sì. Non uso storie, frasi o situazioni riconoscibili delle persone che seguo, né sul sito né sui social.'),
]
nuovi = []
for k, (q, r) in enumerate(QA, 1):
    li = modello_li
    li = re.sub(r'(<span class="num-eyebrow[^>]*>)\d+(</span>)', rf'\g<1>{k:02d}\g<2>', li, count=1)
    li = re.sub(r'(<span class="qmark">«</span>).*?(<span class="qmark">»</span>)', lambda m: f'{m.group(1)} {q} {m.group(2)}', li, count=1, flags=re.S)
    li = re.sub(r'(<div class="faq-answer[^>]*>).*?(</div>)', lambda m: f'{m.group(1)}\n                {r}\n              {m.group(2)}', li, count=1, flags=re.S)
    if k == 1: li = li.replace('<details class="reveal">', '<details class="reveal" open>', 1)
    nuovi.append(li)
FAQ = re.sub(r'(<ul class="border-y[^>]*>).*(</ul>)', lambda m: m.group(1) + '\n          ' + '\n          '.join(nuovi) + '\n        ' + m.group(2), faq_old, count=1, flags=re.S)
FAQ = FAQ.replace('<section id="faq" class="bg-brand-cream">', '<section id="faq" class="bg-brand-paper">')
assert FAQ.count('<details') == 5
FAQ = FAQ.replace('Sono le frasi che mi ripetono in privato, prima di prenotare.', 'Sono le cose che sento più spesso, prima di una prima consulenza.')
assert 'cose che sento più spesso' in FAQ
assert 'text-[44px] sm:text-[56px] md:text-[72px]' in FAQ
FAQ = FAQ.replace('text-[44px] sm:text-[56px] md:text-[72px]', 'text-[44px] sm:text-[56px] md:text-[44px] lg:text-[60px]', 1)
corpo = (PERC.parent / 'generatore' / 'home-v3.html').read_text()
for k, v in {'{{FRASI}}': frasi, '{{BLOG}}': BLOG, '{{PERCORSI}}': PERCORSI, '{{DIAGRAMMA}}': DIAG, '{{VIDEO_PRIMA}}': VIDEO_PRIMA, '{{GIFT_URL}}': GIFT_URL, '{{EMAIL_ENT}}': EMAIL_ENT, '{{FAQ}}': FAQ}.items():
    assert k in corpo, k; corpo = corpo.replace(k, v)
assert '{{' not in corpo
i = land.index('<!-- ═════════════════════════ HERO'); j = land.index('<!-- ═════════════════════════ 9 · FOOTER')
land = land[:i] + corpo + '\n\n' + land[j:]
# navigazione: via «Manifesto», dentro «Percorsi»
land = re.sub(r'\s*<li><a href="#manifesto"[^>]*>Manifesto</a></li>', '', land)
land = re.sub(r'(<li><a href="#funziona"(\s*class="[^"]*")>Come funziona</a></li>)', r'\1\n      <li><a href="#percorsi"\2>Percorsi</a></li>', land)
assert land.count('href="#percorsi"') >= 3, land.count('href="#percorsi"')
# stile della v3 e foto che cambiano con la sezione
CSS_V3 = '''<style>
  /* Home v3 */
  .split-foto .foto { opacity: 0; transition: opacity 1.6s cubic-bezier(.4,0,.2,1); }
  .split-foto .foto.is-on { opacity: 1; }
  @media (max-width: 767px) { .split-foto { aspect-ratio: 4 / 5; max-height: 78svh; } }
  .frase summary:hover .testo, .frase summary:focus-visible .testo { color: #7A1E2B; }
  .frase .piu { transition: transform .3s cubic-bezier(.16,1,.3,1); }
  .frase[open] .piu { transform: rotate(45deg); }
  .riga { display: flex; justify-content: space-between; align-items: baseline; gap: 24px; }
  .riga .val { font-family: 'DM Serif Display', Georgia, serif; font-size: 26px; line-height: 1; color: #1A1A1A; white-space: nowrap; font-variant-numeric: tabular-nums; }
  @media (min-width: 768px) { .riga .val { font-size: 30px; } }
  .faq-p { break-inside: avoid; margin-bottom: 24px; }
  .contatti-righe a { display: flex; justify-content: space-between; align-items: baseline; gap: 24px; padding: 26px 24px; font-family: 'DM Serif Display', Georgia, serif; font-size: clamp(28px, 4.4vw, 60px); line-height: 1.05; letter-spacing: -0.02em; color: #F0E7D5; transition: background .25s ease; }
  @media (min-width: 768px) { .contatti-righe a { padding: 30px max(40px, calc((100vw - 1280px) / 2 + 40px)); } }
  .contatti-righe li:nth-child(odd) a { background: #5C1520; }
  .contatti-righe a:hover, .contatti-righe a:focus-visible { background: #4A1019; }
  .contatti-righe .v { font-size: clamp(18px, .55em, 34px); white-space: nowrap; }
  .gift .arrow { transition: transform .2s ease; }
  .bg-brand-burgundy ::selection, .bg-brand-ink ::selection, .bg-brand-burgundy-deep ::selection { background: rgba(240,231,213,.28); color: #F0E7D5; }
  .diag-card .pm-t-st-sig { text-transform: none; letter-spacing: .02em; }
  @keyframes assestaHome { from { scale: 1.08; opacity: .5; } to { scale: 1; opacity: 1; } }
  @media (prefers-reduced-motion: no-preference) { @supports (animation-timeline: view()) { img.assesta { animation: assestaHome linear both; animation-timeline: view(); animation-range: entry 0% cover 35%; } } }
  .gift:hover .arrow { transform: translateX(4px); }
  .diag-card { background: transparent !important; box-shadow: none !important; border: 0 !important; padding: 0 !important; transform: none !important; }
  /* v8: blog in home, indice con anteprima */
  .vetrina { position: relative; list-style: none; margin-left: 0; padding: 0; }
  .vetrina a { display: block; padding: 16px 0; color: #F0E7D5; }
  .vetrina .f { display: block; font-family: 'DM Serif Display', Georgia, serif; font-size: clamp(24px, 3vw, 40px); line-height: 1.15; letter-spacing: -0.015em; text-wrap: balance; transition: opacity .3s ease; }
  .vetrina .t { display: block; margin-top: 6px; font-size: 16px; line-height: 1.45; color: rgba(240,231,213,.82); }
  .vetrina .ar { display: inline-block; transition: transform .3s cubic-bezier(.16,1,.3,1); }
  .vetrina a:hover .ar, .vetrina a:focus-visible .ar { transform: translateX(5px); }
  .vetrina img { display: none; }
  .vetrina li:first-child img { display: block; width: 100%; height: auto; aspect-ratio: 16 / 10; object-fit: cover; margin-bottom: 20px; }
  @media (min-width: 1024px) {
    .vetrina { padding-right: 46%; min-height: 560px; }
    .vetrina img, .vetrina li:first-child img { display: block; position: absolute; right: 0; top: 0; width: 40%; height: auto; aspect-ratio: 4 / 5; object-fit: cover; margin: 0; opacity: 0; transition: opacity .4s ease; }
    .vetrina .f { opacity: .5; }
    .vetrina li:hover img, .vetrina li:focus-within img, .vetrina li:hover .f, .vetrina li:focus-within .f { opacity: 1; }
    .vetrina:not(:has(li:hover)):not(:has(li:focus-within)) li:first-child img, .vetrina:not(:has(li:hover)):not(:has(li:focus-within)) li:first-child .f { opacity: 1; }
  }
  .sez-home h3 { font-family: 'Source Serif 4', Georgia, serif; font-size: 17px; font-weight: 600; color: #F0E7D5; }
  .sez-home ul { list-style: none; margin: 12px 0 0; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 24px; }
  @media (min-width: 1024px) { .sez-home ul { grid-template-columns: repeat(5, minmax(0, 1fr)); } }
  .sez-home a { display: flex; gap: 10px; align-items: flex-start; padding: 12px 0; min-height: 44px; color: #F0E7D5; font-family: 'DM Serif Display', Georgia, serif; font-size: 19px; line-height: 1.2; }
  .sez-home a:hover span, .sez-home a:focus-visible span { text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 5px; }
  .ico-s { width: 22px; height: 22px; flex: none; margin-top: 1px; color: #F0E7D5; }
  @media (prefers-reduced-motion: reduce) { .vetrina img, .vetrina .f, .vetrina .ar { transition: none; } }
  /* v4: percorsi, scegli per chi */
  .per { border: 0; padding: 0; margin: 0; display: flex; flex-wrap: wrap; gap: 8px; }
  .per legend { width: 100%; }
  .per input { position: absolute; opacity: 0; pointer-events: none; }
  .per label { cursor: pointer; display: inline-flex; align-items: center; min-height: 44px; padding: 10px 20px; border-radius: 2px; background: #F8F1E0; color: #1A1A1A; font-size: 16px; transition: background .2s ease, color .2s ease; }
  .per label:hover { background: #EADFC9; }
  .per input:checked + label { background: #7A1E2B; color: #F0E7D5; }
  .per input:focus-visible + label { outline: 2px solid #7A1E2B; outline-offset: 3px; }
  .per .voci { flex-basis: 100%; margin-top: 8px; }
  #per-solo:checked ~ .voci .voce:not([data-per~="solo"]),
  #per-coppia:checked ~ .voci .voce:not([data-per~="coppia"]),
  #per-gruppo:checked ~ .voci .voce:not([data-per~="gruppo"]) { display: none; }
  /* v4.1: prezzi con il risparmio */
  .prezzi { display: flex; flex-direction: column; align-items: flex-end; gap: 4px; text-align: right; }
  .prezzi .barrato { font-family: 'Source Serif 4', Georgia, serif; font-size: 17px; color: rgba(26,26,26,.7); }
  .prezzi .risparmi { display: inline-block; margin-top: 4px; padding: 4px 10px; background: #7A1E2B; color: #F0E7D5; font-size: 14px; font-weight: 600; white-space: nowrap; }
  .prezzi .a-incontro { font-size: 14px; color: rgba(26,26,26,.78); white-space: nowrap; }
  @media (max-width: 640px) { .voce .riga { flex-direction: column; gap: 6px; } .voce .prezzi { align-items: flex-start; text-align: left; } }
  /* v4: video grande su fondo scuro */
  .vbox { position: fixed; inset: 0; z-index: 10000; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 14px; background: rgba(26,26,26,.94); padding: 56px 16px 24px; }
  .vbox[hidden] { display: none; }
  .vbox-in { position: relative; margin: 0; height: min(82svh, 150vw); aspect-ratio: 9 / 16; max-width: 92vw; background: #000; }
  .vbox-in video { width: 100%; height: 100%; object-fit: cover; display: block; cursor: pointer; }
  .vbox-play { position: absolute; inset: 0; margin: auto; width: 76px; height: 76px; border-radius: 50%; border: 0; background: rgba(240,231,213,.92); color: #7A1E2B; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: opacity .2s ease; }
  .vbox.suona .vbox-play { opacity: 0; pointer-events: none; }
  .vbox-barra { position: absolute; left: 0; right: 0; bottom: 0; height: 18px; cursor: pointer; display: flex; align-items: flex-end; }
  .vbox-barra::before { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 4px; background: rgba(240,231,213,.3); }
  .vbox-barra span { position: relative; height: 4px; width: 0; background: #F0E7D5; }
  .vbox-tit { color: #F0E7D5; font-family: 'DM Serif Display', Georgia, serif; font-size: 20px; text-align: center; max-width: 92vw; }
  .vbox-chiudi { position: absolute; top: 12px; right: 12px; width: 48px; height: 48px; border: 0; background: transparent; color: #F0E7D5; cursor: pointer; display: flex; align-items: center; justify-content: center; }
  .vbox button:focus-visible { outline: 2px solid #F0E7D5; outline-offset: 3px; }
  @media (prefers-reduced-motion: reduce) { .split-foto .foto { transition: none; } .diag-card .pm-stamp { opacity: 1; transform: none; } }
</style>
'''
land = land.replace('</head>', CSS_V3 + '</head>', 1)
for a_, b_ in [("var navLinks = document.querySelectorAll('header nav a[href^=\"#\"]');", "var navLinks = document.querySelectorAll('header nav a.nav-desktop-link[href^=\"#\"]');"),
               ("var active = document.querySelector('header nav a[href=\"#' + e.target.id + '\"]');", "var active = document.querySelector('header nav a.nav-desktop-link[href=\"#' + e.target.id + '\"]');")]:
    assert a_ in land, a_; land = land.replace(a_, b_, 1)
# menu completo solo da 1024px: sotto, il menu a panino (a 768 le voci andavano a capo)
for a_, b_ in [('<ul class="hidden md:flex items-center gap-9', '<ul class="hidden lg:flex items-center gap-9'),
               ('class="md:hidden inline-flex flex-col justify-center gap-[5px]', 'class="lg:hidden inline-flex flex-col justify-center gap-[5px]'),
               ('class="md:hidden fixed inset-0 z-[9998]', 'class="lg:hidden fixed inset-0 z-[9998]')]:
    assert a_ in land, a_; land = land.replace(a_, b_, 1)
land = land.replace('<div class="text-[10px] tracking-[0.28em] uppercase text-brand-cream/60 mb-5">', '<div class="font-body text-[15px] text-brand-cream/80 mb-4">')
land = land.replace('<div class="tracking-[0.18em] uppercase">© 2026 · aleedusex</div>', '<div>© 2026 · aleedusex</div>')
land = land.replace('max-w-3xl pb-16 md:pb-20 border-b border-brand-cream/15', 'max-w-3xl pb-16 md:pb-20').replace('pt-6 border-t border-brand-cream/12 flex', 'pt-6 flex')
FOTO_JS = """
<script>
  // Home v3: la foto ferma cambia piano piano con la sezione che stai leggendo.
  (function () {
    var foto = document.querySelectorAll('.split-foto .foto');
    if (!foto.length || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (voci) {
      voci.forEach(function (v) {
        if (!v.isIntersecting) return;
        var k = v.target.getAttribute('data-foto-per');
        foto.forEach(function (f) { f.classList.toggle('is-on', f.getAttribute('data-foto') === k); });
      });
    }, { rootMargin: '-45% 0px -45% 0px' });
    document.querySelectorAll('[data-foto-per]').forEach(function (s) { io.observe(s); });
  })();
</script>
"""
VBOX_JS = '<script>\n  // Video dei percorsi: si apre grande su fondo scuro, si tocca per fermare o ripartire, Esc o la X per chiudere.\n  (function () {\n    var link = document.querySelectorAll(\'a.apri-video\'); if (!link.length) return;\n    var box = document.createElement(\'div\'); box.className = \'vbox\'; box.hidden = true;\n    box.setAttribute(\'role\', \'dialog\'); box.setAttribute(\'aria-modal\', \'true\'); box.setAttribute(\'aria-label\', \'Video\');\n    box.innerHTML = \'<button type="button" class="vbox-chiudi" aria-label="Chiudi il video"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><line x1="5" y1="5" x2="19" y2="19"/><line x1="19" y1="5" x2="5" y2="19"/></svg></button>\' +\n      \'<figure class="vbox-in"><video playsinline preload="none"></video><button type="button" class="vbox-play" aria-label="Riproduci"><svg width="28" height="28" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg></button><div class="vbox-barra" aria-hidden="true"><span></span></div></figure>\' +\n      \'<p class="vbox-tit"></p>\';\n    document.body.appendChild(box);\n    var v = box.querySelector(\'video\'), play = box.querySelector(\'.vbox-play\'), chiudi = box.querySelector(\'.vbox-chiudi\'), barra = box.querySelector(\'.vbox-barra\'), riemp = barra.querySelector(\'span\'), tit = box.querySelector(\'.vbox-tit\'), da = null;\n    function apri(a) { da = a; v.src = a.getAttribute(\'href\'); v.poster = a.getAttribute(\'data-poster\') || \'\'; tit.textContent = a.getAttribute(\'data-titolo\') || \'\';\n      box.hidden = false; document.body.style.overflow = \'hidden\'; chiudi.focus(); var p = v.play(); if (p && p.catch) p.catch(function () {}); }\n    function chiudiBox() { v.pause(); v.removeAttribute(\'src\'); v.load(); box.hidden = true; document.body.style.overflow = \'\'; box.classList.remove(\'suona\'); if (da) da.focus(); }\n    function alterna() { if (v.paused) v.play(); else v.pause(); }\n    link.forEach(function (a) { a.addEventListener(\'click\', function (e) { e.preventDefault(); apri(a); }); });\n    v.addEventListener(\'click\', alterna); play.addEventListener(\'click\', alterna);\n    v.addEventListener(\'play\', function () { box.classList.add(\'suona\'); play.setAttribute(\'aria-label\', \'Pausa\'); });\n    v.addEventListener(\'pause\', function () { box.classList.remove(\'suona\'); play.setAttribute(\'aria-label\', \'Riproduci\'); });\n    v.addEventListener(\'timeupdate\', function () { if (v.duration) riemp.style.width = (v.currentTime / v.duration * 100) + \'%\'; });\n    barra.addEventListener(\'click\', function (e) { var r = barra.getBoundingClientRect(); if (v.duration) v.currentTime = (e.clientX - r.left) / r.width * v.duration; });\n    chiudi.addEventListener(\'click\', chiudiBox);\n    box.addEventListener(\'click\', function (e) { if (e.target === box) chiudiBox(); });\n    document.addEventListener(\'keydown\', function (e) { if (box.hidden) return; if (e.key === \'Escape\') chiudiBox(); if (e.key === \' \' && document.activeElement !== play) { e.preventDefault(); alterna(); } });\n  })();\n</script>\n'
k = land.rindex('</body>'); land = land[:k] + FOTO_JS + VBOX_JS + land[k:]
# menu da telefono: da chiuso è inattivo (niente tab sui link nascosti), all'apertura il focus va su «Chiudi»
for a_, b_ in [
  ('transform: translateX(100%); transition: transform 320ms cubic-bezier(.2,.7,.2,1);"\n  aria-hidden="true"',
   'transform: translateX(100%); transition: transform 320ms cubic-bezier(.2,.7,.2,1); visibility: hidden;"\n  aria-hidden="true" inert'),
  ("      menu.style.transform = 'translateX(0)';", "      menu.removeAttribute('inert'); menu.style.visibility = 'visible';\n      menu.style.transform = 'translateX(0)';\n      setTimeout(function () { closeBtn.focus(); }, 50);"),
  ("      menu.style.transform = 'translateX(100%)';", "      menu.style.transform = 'translateX(100%)';\n      menu.setAttribute('inert', '');\n      setTimeout(function () { if (!isOpen) menu.style.visibility = 'hidden'; }, 330);\n      toggle.focus();")]:
    assert a_ in land, a_[:50]; land = land.replace(a_, b_, 1)
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


# ── 10. correzioni della revisione del 4 novembre (blocco A: senza decisioni) ──
def sost(path, a, b):
    h = rd(path); assert a in h, (path, a[:60]); wr(path, h.replace(a, b))
# A1. niente più «nessun modulo» dove il modulo c'è
sost('legale.html', 'non ha moduli e non traccia nessuno', 'non traccia nessuno')
# A2. niente segnaposto online: disdette nascoste finché Alessio non manda il testo; conservazione 12 mesi (da confermare)
h = rd('legale.html'); h = re.sub(r'\n\n      <section id="disdette">.*?</section>', '', h, flags=re.S); wr('legale.html', h)
h = rd('index.html'); h = re.sub(r'\s*<a href="/legale.html#disdette"[^>]*>[^<]*</a>', '', h); wr('index.html', h)
# A8. privacy del modulo: dati tecnici di Netlify, conservazione, consenso esplicito
sost('legale.html', 'raccoglie solo il testo che scrivi e la pagina da cui scrivi. Non chiede nome né email',
     'raccoglie il testo che scrivi e la pagina da cui scrivi; il servizio di hosting registra anche dati tecnici come indirizzo IP e browser, per bloccare lo spam. Non chiede nome né email')
sost('legale.html', 'le cancello entro [periodo da decidere]', 'le cancello, insieme alle email, entro 12 mesi')
sost('legale.html', 'Base giuridica: il consenso che dai spuntando la casella (art. 6, par. 1, lett. a GDPR).',
     'Base giuridica: il consenso esplicito che dai spuntando la casella (art. 6, par. 1, lett. a e art. 9, par. 2, lett. a GDPR), che puoi revocare scrivendomi.')
for slug in LI:
    p = f'blog/{slug}.html'
    sost(p, '<span>Ho letto l’<a href="/legale.html#privacy">informativa privacy</a>.</span>',
         '<span>Acconsento al trattamento di quello che scrivo, come spiegato nell’<a href="/legale.html#privacy">informativa privacy</a>.</span>')
    sost(p, 'Non scrivere nome, email o dettagli che ti rendono riconoscibile: così non posso risponderti in privato. Se vuoi una risposta solo per te, scrivimi su WhatsApp.',
         'Non scrivere nome, email o dettagli che ti rendono riconoscibile. Le domande arrivano senza mittente, quindi non posso risponderti in privato: se vuoi una risposta solo per te, scrivimi su WhatsApp.')
    sost(p, '<p class="hp">', '<p class="hp" aria-hidden="true">')
# A3. Foucault: titoli in corsivo vero, frase con soggetto
p = 'blog/foucault-storia-della-sessualita.html'; h = rd(p)
h = re.sub(r'\*([^*<\n\s][^*<\n]{1,90}?)\*', r'<em>\1</em>', h)
h = h.replace('Io non sono un confessore e non ti giudico. Serve a capire', 'Io non sono un confessore e non ti giudico. Parlarne serve a capire')
assert '*La volontà' not in h; wr(p, h)
# A4 e A6. focus visibile sui fondi bordeaux del blog; telefoni stretti senza scorrimento laterale
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('\n/* Focus visibile sui fondi scuri */\n'
            '.cta-box a:focus-visible, .cta-box button:focus-visible, .site-footer a:focus-visible { outline-color: var(--cream); }\n'
            '/* Telefoni stretti: il conteggio della sezione va sotto il nome */\n'
            '@media (max-width: 359px) { .sez-list a { grid-template-columns: 22px 1fr; } .sez-list .c { grid-column: 2; white-space: normal; } }\n')
# A5 e A4 (home): video in pausa alla chiusura e uno solo alla volta; focus crema sul bordeaux
VIDEO_JS = ('\n<script>\n  // Video dei percorsi: si fermano quando si chiude la scheda e ne suona uno alla volta.\n'
            "  document.querySelectorAll('details video').forEach(function (v) {\n"
            "    v.closest('details').addEventListener('toggle', function (e) { if (!e.target.open) v.pause(); });\n"
            "    v.addEventListener('play', function () {\n"
            "      document.querySelectorAll('details video').forEach(function (o) { if (o !== v) o.pause(); });\n"
            '    });\n  });\n</script>\n')
FOCUS_CSS = '<style>.bg-brand-burgundy :focus-visible, .bg-brand-burgundy-deep :focus-visible { outline-color: #F0E7D5 !important; --tw-ring-color: #F0E7D5; }</style>\n'
h = rd('index.html'); h = h.replace('</head>', FOCUS_CSS + '</head>', 1)
i = h.rindex('</body>'); h = h[:i] + VIDEO_JS + h[i:]; wr('index.html', h)
# A7. il link «salta al contenuto» nelle pagine sezione
for sz in SEZ:
    sost(f'blog/{sz["slug"]}/index.html', '<section class="wrap" aria-label="Articoli della sezione">', '<section id="articoli" class="wrap" aria-label="Articoli della sezione">')
# A9. virgolette dritte nel testo visibile → « » (non tocca attributi, script e stili)
def virgolette(h):
    parti = re.split(r'(<script.*?</script>|<style.*?</style>|<[^>]+>)', h, flags=re.S)
    return ''.join(x if (x.startswith('<') or '"' not in x) else re.sub(r'"([^"\n]{1,200})"', r'«\1»', x) for x in parti)
for f in OUT.rglob('*.html'):
    if f.name.startswith('_'): continue
    h = f.read_text(); n = virgolette(h)
    if n != h: f.write_text(n)


# ── 11. v3: blog e articoli più calmi (revisione del 4/11, punti B5, B6, B9, B3) ──
GIFT_URL3 = 'https://wa.me/393273003855?text=Ciao%20Alessio%2C%20vorrei%20fissare%20la%20telefonata%20gratuita%20di%2015%20minuti.'
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* v3: niente timbro, testo semplice */
.stamp { background: none !important; color: inherit !important; padding: 0 !important; box-shadow: none !important; transform: none !important; animation: none !important; font-style: normal !important; border-radius: 0 !important; display: inline !important; }
/* v3: «In breve» subito sotto il sommario */
.article-head + .in-breve, .in-breve.su { margin: 8px 0 48px; }
/* v3: la domanda anonima si apre a richiesta */
.domanda { margin: 32px 0 56px; padding-top: 28px; }
.domanda summary { list-style: none; cursor: pointer; display: flex; justify-content: space-between; align-items: center; gap: 16px; min-height: 44px; }
.domanda summary::-webkit-details-marker { display: none; }
.domanda summary::after { content: "+"; font-family: var(--display); font-size: 32px; line-height: 1; color: var(--burgundy); transition: transform 300ms cubic-bezier(.16,1,.3,1); }
.domanda[open] summary::after { transform: rotate(45deg); }
.domanda summary:hover h2, .domanda summary:focus-visible h2 { color: var(--burgundy); }
.domanda h2 { font-size: 26px; }
.cta-box::before { display: none !important; }
/* v3: niente ombre a riposo, niente maiuscoletto spaziato: scrittura normale come nella home */
.cta-box { box-shadow: none !important; }
.post-meta, .article-head .post-meta { text-transform: none; letter-spacing: 0; font-size: 15px; }
.in-breve .eyebrow, .site-footer .label, .cta-box .eyebrow { text-transform: none; letter-spacing: 0; font-size: 15px; }
.site-footer .legal .copy { text-transform: none; letter-spacing: 0; }
''')
for f in OUT.rglob('*.html'):
    if f.name.startswith('_'): continue
    h = f.read_text(); o = h
    # 15 minuti: una formula sola e WhatsApp con il messaggio già scritto
    h = h.replace('Hai solo una domanda? Una telefonata di 15 minuti, gratis', 'Hai solo una domanda? Una telefonata di 15 minuti, gratis')
    h = h.replace('Hai solo una domanda? 15 minuti al telefono, te li regalo io', 'Hai solo una domanda? Una telefonata di 15 minuti, gratis')
    h = h.replace('i primi 15 minuti te li regalo io', 'ci sentiamo 15 minuti al telefono, gratis')
    h = h.replace('<a class="gift" href="https://wa.me/393273003855"', f'<a class="gift" href="{GIFT_URL3}"')
    # niente etichette sopra i titoli
    h = h.replace('<p class="eyebrow">Cominciamo da qui</p>', '').replace('<p class="eyebrow">Blog</p>', '')
    h = h.replace('<h2 id="cta-titolo">Ne vuoi <span style="font-style:italic">parlare?</span></h2>', '<h2 id="cta-titolo">Ne vuoi parlare?</h2>')
    if h != o: f.write_text(h)
for slug in LI:
    p = f'blog/{slug}.html'; a = rd(p)
    # «In breve» in alto, prima del testo
    ib = re.search(r'\n\s*<aside class="in-breve".*?</aside>', a, re.S)
    if ib:
        a = a.replace(ib.group(0), '')
        a = a.replace('<div class="prose">', ib.group(0).strip().replace('class="in-breve"', 'class="in-breve su"') + '\n    <div class="prose">', 1)
    # un solo blocco finale: consulenza, poi la domanda anonima chiusa
    dm = re.search(r'<section class="domanda".*?</section>\n\n', a, re.S); assert dm, slug
    a = a.replace(dm.group(0), '')
    d = dm.group(0).strip()
    d = d.replace('<section class="domanda" aria-labelledby="domanda-titolo">\n      <h2 id="domanda-titolo">Hai una domanda su questo tema?</h2>',
                  '<details class="domanda">\n      <summary><h2 id="domanda-titolo">Preferisci fare una domanda anonima?</h2></summary>')
    assert d.startswith('<details'), slug
    d = d[:d.rindex('</section>')] + '</details>'
    i = a.index('<section class="cta-box"'); j = a.index('</section>', i) + len('</section>')
    a = a[:j] + '\n\n    ' + d + a[j:]
    wr(p, a)
# Approfondimenti: fuori da Google finché ha pochi articoli, niente «In arrivo»
p = 'blog/approfondimenti-e-attualita/index.html'; h = rd(p)
h = re.sub(r'<p class="soon">.*?</p>', '', h, flags=re.S)
h = h.replace('<head>', '<head>\n<meta name="robots" content="noindex, follow">', 1); wr(p, h)
sm = rd('sitemap.xml'); sm = re.sub(r'\n\s*<url><loc>[^<]*/blog/approfondimenti-e-attualita/</loc></url>', '', sm); wr('sitemap.xml', sm)
# home: il menu a panino accanto a «Scrivimi», non in mezzo
h = rd('index.html'); a_ = 'class="lg:hidden inline-flex flex-col justify-center gap-[5px]'; assert a_ in h
wr('index.html', h.replace(a_, 'class="lg:hidden ml-auto mr-4 inline-flex flex-col justify-center gap-[5px]', 1))


# ── 12. v3.1: blog più ricco (Impeccable «bolder» + Taste: immagini vere, la frase del lettore) ──
from PIL import Image
(OUT / 'blog/img/mini').mkdir(exist_ok=True)
FRASE, COVER = {}, {}
for slug in LI:
    a = (SITE / f'blog/{slug}.html').read_text()
    m = re.search(r'<p class="frase">([^<]+)</p>', a); FRASE[slug] = m.group(1).strip() if m else ''
    c = re.search(r'<figure class="cover">\s*<img src="/blog/img/([^"]+)" alt="([^"]*)"', a)
    if c:
        COVER[slug] = (c.group(1), c.group(2))
        im = Image.open(SITE / 'blog/img' / c.group(1)).convert('RGB'); im.thumbnail((1040, 650), Image.LANCZOS)
        im.save(OUT / 'blog/img/mini' / c.group(1), quality=80, optimize=True, progressive=True)
def ricco(h):
    def un(m):
        li = m.group(0); slug = re.search(r'<a href="/blog/([^"]+)\.html">', li).group(1)
        lead = 'post-item--lead' in li
        if slug in COVER:
            f, alt = COVER[slug]; src = f'/blog/img/{f}' if lead else f'/blog/img/mini/{f}'
            w, hh = (1600, 1000) if lead else Image.open(OUT / 'blog/img/mini' / f).size
            li = li.replace(f'<a href="/blog/{slug}.html">', f'<a href="/blog/{slug}.html">\n          <img class="post-cover" src="{src}" alt="" width="{w}" height="{hh}" loading="{"eager" if lead else "lazy"}" decoding="async">', 1)
        if FRASE.get(slug):
            li = li.replace('<h2 class="post-title">', f'<p class="post-frase">{FRASE[slug]}</p>\n          <h2 class="post-title">', 1)
        return li
    return re.sub(r'<li class="post-item[^"]*">.*?</li>', un, h, flags=re.S)
for p in ['blog/index.html'] + [f'blog/{s["slug"]}/index.html' for s in SEZ]:
    wr(p, ricco(rd(p)))
# /blog/: le sezioni salgono accanto al titolo (riempiono il vuoto a destra)
h = rd('blog/index.html')
sez = re.search(r'\s*<section class="wrap sez-index" aria-labelledby="sezioni-h">.*?</section>', h, re.S).group(0)
h = h.replace(sez, '')
hero = re.search(r'<section class="blog-hero">\s*<div class="wrap">(.*?)</div>\s*</section>', h, re.S)
nuovo = ('<section class="blog-hero blog-hero-v31">\n    <div class="wrap hero-grid">\n      <div class="hero-testo">' + hero.group(1) +
         '</div>\n      <nav class="hero-sez" aria-labelledby="sezioni-h">\n        <h2 id="sezioni-h">Le sezioni</h2>\n        ' +
         re.search(r'<ol class="sez-list">.*?</ol>', sez, re.S).group(0) + '\n      </nav>\n    </div>\n  </section>')
h = h.replace(hero.group(0), nuovo); wr('blog/index.html', h)
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* ── v3.1: blog più ricco ── */
.blog-hero-v31 .hero-grid { display: grid; gap: 48px; }
.hero-sez h2 { font-family: var(--display); font-size: 24px; line-height: 1.1; }
.hero-sez .sez-list { margin-top: 12px; }
.hero-sez .sez-list .n { font-size: 22px; }
@media (min-width: 1024px) {
  .blog-hero-v31 .hero-grid { grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); gap: 80px; align-items: end; }
}
.post-cover { width: 100%; height: auto; aspect-ratio: 16 / 10; object-fit: cover; background: var(--paper); margin-bottom: 20px; transition: transform 500ms cubic-bezier(.16,1,.3,1); }
.post-item > a { overflow: hidden; }
/* cornice: passe-partout color carta (stacco di tono, niente bordi né ombre) */
.post-cover { box-sizing: border-box; padding: 12px; background: var(--paper); }
.post-item--lead .post-cover { padding: 20px; }
@media (min-width: 768px) { .post-cover { padding: 14px; } .post-item--lead .post-cover { padding: 32px; } }
.post-item > a:hover .post-cover { transform: scale(1.02); }
.post-frase { font-family: var(--display); font-size: 21px; line-height: 1.35; color: var(--burgundy); margin: 10px 0 8px; max-width: 30em; }
.post-item--lead .post-frase { font-size: 26px; }
@media (min-width: 768px) {
  .post-item > a { grid-template-columns: 300px 1fr; column-gap: 48px; }
  .post-item > a .post-cover { grid-column: 1; grid-row: 1 / span 6; margin-bottom: 0; align-self: start; }
  .post-item > a > .post-meta { grid-column: 2; padding-top: 0; }
  .post-item--lead > a { grid-template-columns: 1fr; }
  .post-item--lead > a .post-cover { grid-row: auto; margin-bottom: 28px; aspect-ratio: 16 / 9; }
  .post-item--lead > a > * { grid-column: 1 !important; }
}
''')

# ── 13. v3.2: le regole di Taste anche sul blog; immagini più d'impatto (grandi, a filo, nessuna cornice) ──
def meta_sotto(h):
    def un(m):
        li = m.group(0); mt = re.search(r'\s*<p class="post-meta">.*?</p>', li, re.S)
        if not mt: return li
        li = li.replace(mt.group(0), '', 1)
        return li.replace('</p>\n          <span class="read-more">', '</p>' + mt.group(0) + '\n          <span class="read-more">', 1) if '<span class="read-more">' in li else li
    return re.sub(r'<li class="post-item[^"]*">.*?</li>', un, h, flags=re.S)
for p in ['blog/index.html'] + [f'blog/{s["slug"]}/index.html' for s in SEZ]:
    wr(p, meta_sotto(rd(p)))
for slug in LI:
    p = f'blog/{slug}.html'; a = rd(p)
    # data e minuti dopo il sommario, non sopra il titolo
    head_ = re.search(r'<header class="article-head">.*?</header>', a, re.S).group(0); nh = head_
    mt = re.search(r'\s*<p class="post-meta">.*?</p>', nh, re.S)
    if mt:
        nh = nh.replace(mt.group(0), '', 1)
        nh = re.sub(r'(<p class="lede">.*?</p>)', lambda m: m.group(1) + mt.group(0), nh, count=1, flags=re.S)
    a = a.replace(head_, nh)
    # percorso semplice al posto della pillola
    a = re.sub(r'<a class="tchip" href="([^"]+)"><svg.*?</svg>([^<]+)</a>', r'<a href="\1">\2</a>', a, flags=re.S)
    wr(p, a)
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* ── v3.2: Taste anche sul blog ── */
html, body { overflow-x: clip; }
/* immagini: nessuna cornice, più grandi, a filo */
.post-cover { padding: 0 !important; background: none !important; }
.post-item > a:hover .post-cover { transform: none; }
@media (min-width: 768px) {
  .post-item > a { grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); column-gap: 56px; }
  .post-item > a .post-cover { aspect-ratio: 4 / 3; }
}
/* l'ultimo articolo: una colonna, copertina a tutta larghezza */
.post-item--lead > a { overflow: visible; grid-template-columns: 1fr !important; }
.post-item--lead > a > * { grid-column: 1 !important; grid-row: auto !important; }
.post-item--lead .post-cover { width: 100vw; max-width: none; margin-left: calc(50% - 50vw); aspect-ratio: auto !important; height: min(78svh, 56vw); object-fit: cover; margin-bottom: 40px; }
/* copertina dell'articolo a tutta larghezza */
.cover { width: 100vw; max-width: none; margin-left: calc(50% - 50vw); margin-bottom: 56px; }
.cover img { width: 100%; height: min(72svh, 56vw); object-fit: cover; border-radius: 0 !important; border: 0 !important; }
.cover figcaption { max-width: 760px; margin: 12px auto 0; padding: 0 24px; }
/* titoli entro due righe: misura larga, corpo più contenuto */
.post-title { max-width: none !important; font-size: 24px !important; }
@media (min-width: 768px) { .post-title { font-size: 28px !important; } }
.post-item--lead .post-title { font-size: clamp(30px, 4vw, 52px) !important; }
.article-head h1 { font-size: clamp(32px, 4.4vw, 46px) !important; max-width: none !important; }
/* data e minuti sotto il titolo */
.post-item .post-meta { margin-top: 14px; }
.article-head .post-meta { margin: 20px 0 0 !important; }
/* niente linee sottili: spazio e un passo di tono */
.post-item { border-bottom: 0 !important; }
.post-item > a { padding: 36px 0 !important; }
@media (min-width: 768px) { .post-item > a { padding: 52px 0 !important; } }
.sez-list, .sez-list li { border: 0 !important; }
.blog-hero { border-bottom: 0 !important; }
.blog-hero-v31 { background: var(--paper); }
.frase { border-bottom: 0 !important; padding-bottom: 0 !important; }
.in-breve { border: 0 !important; }
.more, .domanda { border-top: 0 !important; }
.more li a { border-top: 0 !important; padding: 8px 0; }
.site-footer .legal { font-size: 13px; }
/* movimento: la copertina si assesta entrando, il testo sale; solo CSS, nessun JavaScript */
@keyframes assesta { from { scale: 1.08; opacity: .5; } to { scale: 1; opacity: 1; } }
@keyframes sale { from { opacity: 0; translate: 0 24px; } to { opacity: 1; translate: 0 0; } }
@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .post-item:not(.post-item--lead) .post-cover { animation: assesta linear both; animation-timeline: view(); animation-range: entry 0% cover 30%; }
    .post-item:not(.post-item--lead) > a > :not(.post-cover) { animation: sale linear both; animation-timeline: view(); animation-range: entry 0% entry 60%; }
  }
}
''')

# ── 14. v3.3: correzioni della revisione v3 (agente) e ultimi punti di Taste sul blog ──
INDICE = ('<li><a href="/#chi-sono">Chi sono</a></li>\n          <li><a href="/#parliamone">Di cosa parliamo</a></li>\n          <li><a href="/#funziona">Come funziona</a></li>\n'
          '          <li><a href="/#percorsi">Percorsi</a></li>\n          <li><a href="/#faq">FAQ</a></li>\n          <li><a href="/blog/">Blog</a></li>')
for f in OUT.rglob('*.html'):
    if f.name == 'index.html' and f.parent == OUT: continue
    h = f.read_text(); o = h
    # footer: niente più «Manifesto», stesse voci e stesso ordine della testata della home
    h = re.sub(r'<li><a href="/#manifesto">Manifesto</a></li>\s*<li><a href="/#chi-sono">Chi sono</a></li>\s*<li><a href="/#funziona">Come funziona</a></li>\s*<li><a href="/#faq">FAQ</a></li>\s*<li><a href="/blog/">Blog</a></li>', INDICE, h)
    # testata del blog: Chi sono · Percorsi · Blog, nello stesso ordine della home
    h = re.sub(r'<li><a href="/blog/"( aria-current="page")?>Blog</a></li>\s*<li class="hide-sm"><a href="/#chi-sono">Chi sono</a></li>',
               lambda m: f'<li class="hide-sm"><a href="/#chi-sono">Chi sono</a></li>\n        <li class="hide-sm"><a href="/#percorsi">Percorsi</a></li>\n        <li><a href="/blog/"{m.group(1) or ""}>Blog</a></li>', h)
    if h != o: f.write_text(h)
assert '/#manifesto' not in ''.join(f.read_text() for f in OUT.rglob('*.html'))
# pagina legale: data e nome del modulo come sul sito
h = rd('legale.html')
h = h.replace('<time datetime="2026-09-23">23 settembre 2026</time>', '<time datetime="2026-11-04">4 novembre 2026</time>')
h = h.replace('Il modulo «Fai una domanda» in fondo agli articoli', 'Il modulo per le domande anonime in fondo agli articoli'); wr('legale.html', h)
# home: voce attiva giusta, titoli liberi dopo un'ancora, testata più piena sopra le parti scure, footer in ordine
h = rd('index.html')
for a_, b_ in [("{ threshold: 0.3, rootMargin: '-10% 0px -60% 0px' }", "{ threshold: 0, rootMargin: '-90px 0px -75% 0px' }"),
               ('sticky top-0 z-40 bg-brand-cream/85', 'sticky top-0 z-40 bg-brand-cream/95')]:
    assert a_ in h, a_; h = h.replace(a_, b_, 1)
h = re.sub(r'(<li><a href="#parliamone"[^>]*>Di cosa parliamo</a></li>)(\s*)(<li><a href="#chi-sono"[^>]*>Chi sono</a></li>)', r'\3\2\1', h)
h = h.replace('</head>', '<style>section[id], [id="percorsi"] { scroll-margin-top: 88px; }</style>\n</head>', 1)
wr('index.html', h)
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* niente linee: testata e note legali separate dallo spazio */
.site-header { border-bottom: 0 !important; }
.site-footer .legal { border-top: 0 !important; }
/* ── v3.3: titoli e frasi entro due-tre righe anche su tablet e telefono ── */
@media (min-width: 768px) and (max-width: 1023px) {
  .post-item > a { grid-template-columns: 1fr !important; }
  .post-item > a > * { grid-column: 1 !important; grid-row: auto !important; }
  .post-item > a .post-cover { margin-bottom: 24px; }
}
@media (max-width: 767px) {
  .frase { font-size: 24px !important; }
  .post-item--lead .post-frase { font-size: 22px; }
  .post-title { font-size: 22px !important; }
  .post-item--lead .post-title { font-size: 26px !important; }
}
''')

# ── 15. v4 (vocale di Alessio del 4/11 sera): blog con i quadretti delle sezioni, immagini più contenute, AleEduSex, Gratis ──
h = rd('blog/index.html')
nav = re.search(r'<nav class="hero-sez" aria-labelledby="sezioni-h">.*?</nav>', h, re.S).group(0)
quad = ''.join(f'<li><a href="/blog/{s["slug"]}/">{ico(s["icona"])}<span><span class="n">{s["nome"]}</span><span class="c">{n_art(s)} <span aria-hidden="true">→</span></span></span></a></li>' for s in SEZ)
h = h.replace(nav, f'<nav class="quadretti" aria-labelledby="sezioni-h">\n        <h2 id="sezioni-h">Le sezioni</h2>\n        <ul>{quad}</ul>\n      </nav>')
wr('blog/index.html', h)
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* ── v4: le sezioni come quadretti sotto il titolo ── */
.blog-hero-v31 .hero-grid { grid-template-columns: 1fr !important; gap: 48px; }
.quadretti h2 { font-family: var(--display); font-size: 26px; line-height: 1.1; }
.quadretti ul { list-style: none; margin: 16px 0 0; padding: 0; display: grid; gap: 12px; grid-template-columns: repeat(2, minmax(0, 1fr)); }
@media (min-width: 768px) { .quadretti ul { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
@media (min-width: 1024px) { .quadretti ul { grid-template-columns: repeat(5, minmax(0, 1fr)); } }
.quadretti a { display: flex; flex-direction: column; justify-content: space-between; gap: 20px; height: 100%; min-height: 136px; padding: 20px; background: var(--cream); transition: background 200ms ease; }
.quadretti a:hover { background: #E8DCC4; }
.quadretti .ico { width: 30px; height: 30px; }
.quadretti .n { display: block; font-family: var(--display); font-size: 19px; line-height: 1.15; }
.quadretti .c { display: block; margin-top: 4px; font-size: 14px; font-style: italic; color: rgba(26,26,26,.75); }
.quadretti a:hover .n { color: var(--burgundy); }
/* ── v4: immagini più contenute ── */
.post-item--lead .post-cover { width: 100% !important; margin: 0 0 28px !important; height: auto !important; aspect-ratio: 16 / 10 !important; }
@media (min-width: 1024px) {
  .post-item--lead > a { grid-template-columns: minmax(0, 7fr) minmax(0, 5fr) !important; column-gap: 56px; align-items: center; }
  .post-item--lead > a > .post-cover { grid-column: 1 !important; grid-row: 1 / span 6 !important; margin: 0 !important; }
  .post-item--lead > a > :not(.post-cover) { grid-column: 2 !important; grid-row: auto !important; }
  .post-item:not(.post-item--lead) > a { grid-template-columns: minmax(0, 4fr) minmax(0, 8fr) !important; }
  .post-item--lead .post-title { font-size: clamp(30px, 2.8vw, 40px) !important; }
}
.site-footer .brand { text-transform: none; }
''')
for f in OUT.rglob('*.html'):
    hh = f.read_text(); o = hh
    hh = re.sub(r'class="([^"]*?) ?lowercase([^"]*)">aleedusex<', r'class="\1\2">AleEduSex<', hh)
    hh = hh.replace('>aleedusex<', '>AleEduSex<').replace('© 2026 · aleedusex', '© 2026 · AleEduSex')
    hh = hh.replace('Una telefonata di 15 minuti, gratis', 'Una telefonata di 15 minuti. Gratis')
    if hh != o: f.write_text(hh)

# ── 16. v5: testa del blog «Da dove parti?» (brainstorming del 5/11: muro delle frasi + ingresso dal problema) ──
DOVE = {  # una frase per sezione, nella voce di chi legge: DA FAR APPROVARE AD ALESSIO
 'corpo-piacere-e-fantasie': 'Voglio capire come funziona il mio piacere.',
 'prevenzione-e-salute': 'Ho avuto un rapporto a rischio. E adesso?',
 'comunicazione-relazioni-e-consenso': 'Non riesco a parlarne con chi ho accanto.',
 'difficolta-e-blocchi': 'Qualcosa si è inceppato e non so perché.',
 'approfondimenti-e-attualita': 'Voglio capire da dove arrivano certe idee sul sesso.',
}
h = rd('blog/index.html')
hero = re.search(r'<section class="blog-hero blog-hero-v31">.*?</section>', h, re.S).group(0)
testo = re.search(r'<div class="hero-testo">(.*?)</div>\s*<nav class="quadretti"', hero, re.S).group(1)
quad = re.search(r'<nav class="quadretti".*?</nav>', hero, re.S).group(0)
frasi_dove = ''.join(f'''
          <li><a href="/blog/{s["slug"]}/"><span class="f">«{DOVE[s["slug"]]}»</span><span class="s">{s["nome"]} <span aria-hidden="true">→</span></span></a></li>''' for s in SEZ)
nuovo = f'''<section class="blog-hero dove">
    <div class="wrap dove-grid">
      <div class="hero-testo">{testo}</div>
      <nav class="dove-parti" aria-labelledby="dove-h">
        <h2 id="dove-h">Da dove parti?</h2>
        <ul>{frasi_dove}
        </ul>
      </nav>
    </div>
  </section>

  <section class="wrap quadretti-sec" aria-label="Le sezioni del blog">
      {quad}
  </section>'''
h = h.replace(hero, nuovo); wr('blog/index.html', h)
# pagine sezione: stessa testa bordeaux, con la frase della sezione sopra il titolo
for s in SEZ:
    p = f'blog/{s["slug"]}/index.html'; hh = rd(p)
    hh = hh.replace('<section class="blog-hero sez-hero">', '<section class="blog-hero sez-hero dove">', 1)
    hh = hh.replace('<div class="head"><div><h1>', f'<div class="head"><div><p class="sez-frase">«{DOVE[s["slug"]]}»</p><h1>', 1)
    wr(p, hh)
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* ── v5: testa del blog su bordeaux, «Da dove parti?» ── */
.blog-hero.dove { background: var(--burgundy) !important; color: var(--cream); padding: 64px 0 72px; }
.dove h1, .dove h1 .stamp { color: var(--cream) !important; }
.dove .intro, .dove .lead { color: rgba(240, 231, 213, 0.92) !important; }
.dove .crumb, .dove .crumb a { color: var(--cream) !important; }
.dove .ill { --fg: var(--cream); --bg: var(--burgundy); color: var(--cream); }
.dove-grid { display: grid; gap: 48px; }
@media (min-width: 1024px) {
  .blog-hero.dove { padding: 104px 0 112px; }
  .dove-grid { grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr); gap: 80px; align-items: center; }
}
.dove-parti h2 { font-family: var(--body); font-size: 17px; font-weight: 600; color: var(--cream); }
.dove-parti ul { list-style: none; margin: 14px 0 0; padding: 0; }
.dove-parti a { display: block; padding: 10px 0; color: var(--cream); }
.dove-parti .f { display: block; font-family: var(--display); font-size: clamp(24px, 2.5vw, 34px); line-height: 1.15; letter-spacing: -0.01em; text-wrap: balance; }
.dove-parti li:nth-child(even) .f { font-size: clamp(21px, 2vw, 28px); padding-left: clamp(0px, 3vw, 48px); }
.dove-parti .s { display: block; margin-top: 4px; font-size: 15px; font-style: italic; color: rgba(240, 231, 213, 0.85); }
.dove-parti li:nth-child(even) .s { padding-left: clamp(0px, 3vw, 48px); }
.dove-parti a:hover .f, .dove-parti a:focus-visible .f { text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 6px; }
.dove a:focus-visible { outline-color: var(--cream); }
/* una frase alla volta si accende, piano (solo CSS) */
@keyframes accendi { 0% { opacity: .72; } 4%, 18% { opacity: 1; } 22%, 100% { opacity: .72; } }
@media (prefers-reduced-motion: no-preference) {
  .dove-parti .f { opacity: .72; animation: accendi 15s ease-in-out infinite; }
  .dove-parti li:nth-child(2) .f { animation-delay: 3s; } .dove-parti li:nth-child(3) .f { animation-delay: 6s; }
  .dove-parti li:nth-child(4) .f { animation-delay: 9s; } .dove-parti li:nth-child(5) .f { animation-delay: 12s; }
  .dove-parti ul:hover .f, .dove-parti ul:focus-within .f { animation-play-state: paused; }
  .dove-parti li:hover .f, .dove-parti li:focus-within .f { opacity: 1 !important; animation: none; }
}
/* selezione leggibile sulle parti scure; titolo con un filo di aria in più */
.dove ::selection, .cta-box ::selection, .site-footer ::selection { background: rgba(240, 231, 213, 0.28); color: var(--cream); }
.blog-hero.dove h1 { line-height: 1.06; }
/* le frasi di sezione, sopra il titolo */
.sez-frase { font-family: var(--display); font-style: italic; font-size: clamp(22px, 2.4vw, 30px); line-height: 1.2; color: var(--cream); margin-bottom: 14px; }
/* quadretti subito sotto il capitolo bordeaux */
.quadretti-sec { padding-top: 48px; padding-bottom: 8px; }
.quadretti-sec .quadretti a { background: var(--paper); }
.quadretti-sec .quadretti a:hover { background: #EADFC9; }
''')

# ── 17. v6 (messaggi di Alessio del 5/11): titoli di studio e albi; quadretti delle sezioni con il loro disegno ──
CRED = 'Master di I livello in Consulenza in Sessuologia, Università di Torino · Albo degli Educatori professionali (FNO TSRM e PSTRP) · Albo dei Consulenti in sessuologia FISS'
for slug in LI:
    p = f'blog/{slug}.html'; a = rd(p)
    a = re.sub(r'(<span class="role">[^<]*</span>)', rf'\1\n      <span class="cred">{CRED}</span>', a, count=1)
    wr(p, a)
h = rd('blog/index.html')
nav = re.search(r'<nav class="quadretti" aria-labelledby="sezioni-h">.*?</nav>', h, re.S).group(0)
carte = ''.join(f'''<li><a class="carta live" href="/blog/{s["slug"]}/" style="--d:{150 + k * 120}ms">{ill(s["icona"])}<span class="testo"><span class="n">{s["nome"]}</span><span class="c">{n_art(s)} <span class="ar" aria-hidden="true">→</span></span></span></a></li>''' for k, s in enumerate(SEZ))
h = h.replace(nav, f'<nav class="quadretti carte" aria-labelledby="sezioni-h">\n        <h2 id="sezioni-h">Le sezioni</h2>\n        <ul>{carte}</ul>\n      </nav>')
h = h.replace('</head>', f'<style>:root{{--fg:var(--burgundy);--bg:var(--paper);--muted:rgba(26,26,26,.7)}}{ICON_CSS}</style>\n</head>', 1)
wr('blog/index.html', h)
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* ── v6: credenziali nel riquadro autore ── */
.author-box .cred { display: block; margin-top: 6px; font-size: 14px; line-height: 1.5; color: rgba(26, 26, 26, 0.78); }
/* ── v6: quadretti delle sezioni con il loro disegno (Impeccable «delight»: il disegno prende vita) ── */
.carte ul { gap: 14px; }
.carte .carta { position: relative; display: flex; flex-direction: column; justify-content: space-between; gap: 18px; min-height: 236px; padding: 22px 22px 20px; background: var(--paper); color: var(--ink);
  --fg: var(--burgundy); --bg: var(--paper); transition: background 300ms cubic-bezier(.16,1,.3,1), color 300ms cubic-bezier(.16,1,.3,1), transform 300ms cubic-bezier(.16,1,.3,1); }
.carte .carta .ill { width: 84px; height: 84px; margin: -6px 0 0 -8px; }
.carte .carta .n { display: block; font-family: var(--display); font-size: 21px; line-height: 1.12; letter-spacing: -0.01em; }
.carte .carta .c { display: block; margin-top: 6px; font-size: 14px; font-style: italic; color: rgba(26, 26, 26, 0.75); transition: color 300ms ease; }
.carte .carta .ar { display: inline-block; transition: transform 300ms cubic-bezier(.16,1,.3,1); }
.quadretti-sec .carte .carta:hover, .quadretti-sec .carte .carta:focus-visible, .carte .carta:hover, .carte .carta:focus-visible { background: var(--burgundy); color: var(--cream); --fg: var(--cream); --bg: var(--burgundy); transform: translateY(-3px); }
.carte .carta:hover .c, .carte .carta:focus-visible .c { color: rgba(240, 231, 213, 0.88); }
.carte .carta:hover .ar, .carte .carta:focus-visible .ar { transform: translateX(4px); }
.carte .carta:hover .n { color: var(--cream); }
.carte .carta:focus-visible { outline: 2px solid var(--burgundy); outline-offset: 3px; }
@media (min-width: 1024px) { .carte .carta { min-height: 260px; } .carte .carta .ill { width: 96px; height: 96px; } }
@media (max-width: 767px) { .carte .carta { min-height: 196px; } .carte .carta .ill { width: 68px; height: 68px; } }
@media (prefers-reduced-motion: reduce) { .carte .carta { transition: none; } .carte .carta:hover { transform: none; } }
''')

# ── 18. v7: le «chicche» finali (Taste: ink fill, opening statement, scroll progress; Impeccable: un gesto per zona) ──
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* ── v7: quadretti da collezione: il disegno grande esce dall'angolo, la prima sezione è larga il doppio ── */
.carte ul { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; }
.carte li:first-child { grid-column: span 2; }
@media (min-width: 768px) { .carte ul { grid-template-columns: repeat(3, minmax(0, 1fr)) !important; } }
@media (min-width: 1024px) { .carte ul { grid-template-columns: repeat(6, minmax(0, 1fr)) !important; } }
.carte .carta { overflow: hidden; justify-content: flex-start; min-height: 230px !important; }
.carte .carta .testo { position: relative; z-index: 1; max-width: 12em; }
.carte .carta .ill { position: absolute; right: -26px; bottom: -30px; width: 150px !important; height: 150px !important; margin: 0 !important; transition: transform 500ms cubic-bezier(.16,1,.3,1); }
.carte li:first-child .carta .ill { width: 230px !important; height: 230px !important; right: -20px; bottom: -44px; }
.carte li:first-child .carta .n { font-size: 30px; }
.carte .carta:hover .ill, .carte .carta:focus-visible .ill { transform: translate(-6px, -6px) rotate(-3deg); }
@media (max-width: 767px) { .carte .carta { min-height: 190px !important; } .carte .carta .ill { width: 112px !important; height: 112px !important; right: -18px; bottom: -22px; } .carte li:first-child .carta .ill { width: 170px !important; height: 170px !important; } }
@media (prefers-reduced-motion: reduce) { .carte .carta .ill { transition: none; } .carte .carta:hover .ill { transform: none; } }

/* ── v7: ogni articolo si apre con la frase di chi legge, a pagina piena su bordeaux ── */
article.wrap-narrow > .crumb { margin: 0; padding: 28px 0 0; background: var(--burgundy); color: var(--cream); box-shadow: 0 0 0 100vmax var(--burgundy); clip-path: inset(0 -100vmax); }
article.wrap-narrow > .crumb a { color: var(--cream); border-color: rgba(240, 231, 213, 0.4); }
article.wrap-narrow > .crumb a:focus-visible { outline-color: var(--cream); }
.article-head .frase { display: flex; align-items: center; min-height: 46svh; margin: 0 0 56px !important; padding: 32px 0 72px !important; background: var(--burgundy); color: var(--cream) !important; box-shadow: 0 0 0 100vmax var(--burgundy); clip-path: inset(0 -100vmax);
  font-size: clamp(30px, 4.6vw, 54px) !important; line-height: 1.12; font-style: italic; text-wrap: balance; }
article.wrap-narrow > .crumb ::selection, .article-head .frase::selection { background: rgba(240, 231, 213, 0.28); color: var(--cream); }
article.wrap-narrow > .crumb { padding-bottom: 6px !important; }
article.wrap-narrow > .crumb + .article-head { padding-top: 0 !important; margin-top: 0 !important; border-top: 0 !important; }
@media (min-width: 1024px) { .carte .carta { min-height: 256px !important; } .carte li:not(:first-child) .carta .ill { width: 132px !important; height: 132px !important; } }
/* ── v7: il filo di lettura (solo CSS) ── */
@supports (animation-timeline: scroll()) { @media (prefers-reduced-motion: no-preference) {
  body:has(article.wrap-narrow)::before { content: ""; position: fixed; inset: 0 0 auto 0; height: 3px; z-index: 60; background: var(--burgundy-deep); transform-origin: 0 50%; transform: scaleX(0); animation: filo linear both; animation-timeline: scroll(root); }
  @keyframes filo { to { transform: scaleX(1); } }
} }
''')
# home: i tre principi si riempiono d'inchiostro mentre scorri
h = rd('index.html')
a_ = 'Niente da dimostrare. Niente da nascondere. Niente giri di parole.</p>'; assert a_ in h
h = h.replace(a_, '<span class="inchiostro">Niente da dimostrare. Niente da nascondere. Niente giri di parole.</span></p>', 1)
h = h.replace('</head>', '''<style>
  @supports (animation-timeline: view()) { @media (prefers-reduced-motion: no-preference) {
    .inchiostro { background: linear-gradient(90deg, #7A1E2B 50%, rgba(122,30,43,.22) 50%) 100% 0 / 200% 100% no-repeat; -webkit-background-clip: text; background-clip: text; color: transparent; animation: inchiostro linear both; animation-timeline: view(); animation-range: entry 60% cover 55%; }
    @keyframes inchiostro { to { background-position: 0 0; } }
  } }
</style>
</head>''', 1)
wr('index.html', h)

# ── 19. v9: revisione estetica (fondi alternati, illustrazioni su carta, blog a capitoli, niente vuoti) ──
# 1. home: chiaro e scuro alternati; il blog scende dopo i percorsi; la carta solo per i riquadri
h = rd('index.html')
blog_sec = re.search(r'<section id="dal-blog".*?</section>\n?', h, re.S).group(0)
h = h.replace(blog_sec, '', 1)
i = h.index('<section id="faq"'); h = h[:i] + blog_sec + '\n' + h[i:]
for a_, b_ in [('<section id="funziona" class="bg-brand-paper">', '<section id="funziona" class="bg-brand-cream">'),
               ('class="tragitto lg:col-span-7 bg-brand-cream', 'class="tragitto lg:col-span-7 bg-brand-paper'),
               ('<section id="faq" class="bg-brand-paper">', '<section id="faq" class="bg-brand-cream">')]:
    assert a_ in h, a_; h = h.replace(a_, b_, 1)
# 4. niente metà vuote: nei percorsi la colonna di sinistra resta ferma; il diagramma si stringe
i = h.index('<section id="percorsi"'); j = h.index('<div class="lg:col-span-4">', i)
h = h[:j] + '<div class="lg:col-span-4 lg:sticky lg:top-[120px] lg:self-start">' + h[j + len('<div class="lg:col-span-4">'):]
h = h.replace('</head>', '<style>#percorsi > div { padding-top: 0 !important; } .diag { max-width: 940px; margin-left: auto; margin-right: auto; padding-top: 28px !important; padding-bottom: 28px !important; }</style>\n</head>', 1)
wr('index.html', h)
# 3. blog a capitoli: l'ultimo articolo grande, poi gli altri divisi per sezione, due per riga
h = rd('blog/index.html')
ol = re.search(r'<ol class="post-list"[^>]*>.*?</ol>', h, re.S).group(0)
lis = re.findall(r'<li class="post-item[^"]*">.*?</li>', ol, re.S)
lead = [x for x in lis if 'post-item--lead' in x]; assert len(lead) == 1
def slug_di(li): return re.search(r'href="/blog/([^"]+)\.html"', li).group(1)
gruppi_h = ''
for s in SEZ:
    suoi = [x for x in lis if x is not lead[0] and sez_of[slug_di(x)] is s]
    if not suoi: continue
    gruppi_h += f'''
    <section class="gruppo" aria-labelledby="g-{s["slug"]}">
      <header><a href="/blog/{s["slug"]}/">{ico(s["icona"])}<h2 id="g-{s["slug"]}">{s["nome"]}</h2><span class="c">{n_art(s)} <span aria-hidden="true">→</span></span></a></header>
      <ol class="post-list due">{"".join(suoi)}</ol>
    </section>'''
h = h.replace(ol, f'<ol class="post-list">{lead[0]}</ol>{gruppi_h}')
h = h.replace('id="tutti-h">Tutti gli articoli</h2>', 'id="tutti-h">L’ultimo articolo</h2>')
wr('blog/index.html', h)
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* ── v9: illustrazioni e foto posate su un campo color carta, stesse proporzioni ── */
.post-cover { box-sizing: border-box; padding: 12px !important; background: var(--paper) !important; aspect-ratio: 16 / 10 !important; }
.post-item--lead .post-cover { padding: 20px !important; }
.cover { width: auto !important; margin-left: 0 !important; }
.cover img { box-sizing: border-box; height: auto !important; aspect-ratio: 16 / 10; padding: 14px; background: var(--paper); }
.cover figcaption { padding: 0 !important; }
/* ── v9: blog a capitoli ── */
.gruppo { padding-top: 72px; }
.gruppo header a { display: flex; align-items: center; flex-wrap: wrap; gap: 8px 14px; }
.gruppo header .ico { width: 34px; height: 34px; }
.gruppo h2 { font-family: var(--display); font-size: clamp(28px, 3.2vw, 40px); line-height: 1.05; letter-spacing: -0.02em; }
.gruppo header .c { font-size: 15px; font-style: italic; color: rgba(26,26,26,.75); }
.gruppo header a:hover h2 { color: var(--burgundy); }
.gruppo .post-meta .sez { display: none; }
.post-list.due { padding-bottom: 0 !important; }
.post-list.due .post-item > a { grid-template-columns: 1fr !important; padding: 28px 0 !important; }
.post-list.due .post-item > a > * { grid-column: 1 !important; grid-row: auto !important; }
.post-list.due .post-cover { margin-bottom: 18px !important; }
@media (min-width: 768px) { .post-list.due { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: 56px; } }
.gruppo:last-of-type { padding-bottom: 96px; }
''')
# ── 20. v10: le 6 mosse d'eccellenza (revisione 7: finitura, «», scala tipografica, primo schermo, numeri, ritmo del blog) ──
# Ordine: 6 (finitura) e 2 (virgolette) → 1 (scala) → 5 (primo schermo) → 3 (numeri) → 4 (blog). Poi gli errori (quadretti a 390, menu).
TOKENS = ('--t-hero: clamp(52px, 7.8vw, 120px); --t-h2: clamp(42px, 5.4vw, 80px); --t-h3: clamp(24px, 2.2vw, 28px); '
          '--t-lead: 21px; --t-body: 18px; --t-small: 15px; --t-micro: 13px; --ease: cubic-bezier(.2,.7,.2,1); --dur: 200ms; --dur-press: 120ms;')
FRECCIA = '<span class="freccia" aria-hidden="true">→</span>'

# 6a. stesso menu in tutte le pagine: le voci della home + Scrivimi; su telefono si apre con <details> (niente JavaScript nel blog)
VOCI = [('/#chi-sono', 'Chi sono'), ('/#parliamone', 'Di cosa parliamo'), ('/#funziona', 'Come funziona'), ('/#percorsi', 'Percorsi'), ('/#faq', 'FAQ'), ('/blog/', 'Blog')]
def nav_blog(blog_corrente):
    li = lambda cls: ''.join(f'\n        <li><a href="{u}"{" aria-current=\"page\"" if (u == "/blog/" and blog_corrente) else ""}>{t}</a></li>' for u, t in VOCI)
    return (f'<nav class="nav" aria-label="Principale">\n      <ul class="nav-full">{li("")}\n      </ul>\n'
            '      <details class="nav-m">\n        <summary aria-label="Menu"><span class="b"></span><span class="b"></span><span class="b"></span></summary>\n'
            f'        <ul>{li("")}\n        </ul>\n      </details>\n'
            '      <a class="btn-burgundy" href="/#contatti">Scrivimi <span class="arr" aria-hidden="true"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></span></a>\n'
            '    </nav>')
n_nav = 0
for f in OUT.rglob('*.html'):
    if f.parent == OUT and f.name == 'index.html': continue
    h = f.read_text()
    m = re.search(r'(<header class="site-header">.*?)(<nav class="nav" aria-label="Principale">.*?</nav>)(.*?</header>)', h, re.S)
    if not m: continue
    corrente = 'aria-current="page">Blog' in m.group(2)
    h = h.replace(m.group(0), m.group(1) + nav_blog(corrente) + m.group(3), 1); f.write_text(h); n_nav += 1
assert n_nav >= 20, n_nav

# 2a. FAQ: un solo stile di virgolette, attaccate al testo (niente « » staccate e chiare)
h = rd('index.html')
h, k = re.subn(r'<span class="qmark">«</span>\s*(.*?)\s*<span class="qmark">»</span>', r'«\1»', h, flags=re.S); assert k == 5, k
# 6b. via l'occhiello sopra le FAQ
h, k = re.subn(r'\s*<div class="[^"]*uppercase[^"]*">Pensieri ad alta voce</div>', '', h); assert k == 1, k
# 2b. la « gigante accanto a «Le frasi che non dici» (segno del sito, solo decorazione)
a_ = '<h2 id="parliamone-h"'; assert a_ in h
h = h.replace(a_, '<span class="ancora" aria-hidden="true">«</span>\n      ' + a_, 1)
# 1. una sola scala tipografica: le misure in px di Tailwind diventano 7 gradini (classi t-*)
def gradino(px, hero=False):
    if hero: return 't-hero'
    if px >= 40: return 't-h2'
    if px >= 22: return 't-h3'
    if px >= 19: return 't-lead'
    if px >= 16.5: return 't-body'
    if px >= 14: return 't-small'
    return 't-micro'
def scala(m):
    cls = m.group(1); px = [float(x) for x in re.findall(r'(?:^|\s)(?:[a-z]+:)?text-\[([0-9.]+)px\]', cls)]
    if not px: return m.group(0)
    hero = 'tracking-tighter2' in cls and max(px) >= 84 and 'xl:' in cls
    base = [float(x) for x in re.findall(r'(?:^|\s)text-\[([0-9.]+)px\]', cls)] or px
    g = gradino(max(px) if max(px) >= 40 else base[0], hero)
    cls = re.sub(r'\s*(?:[a-z]+:)?text-\[[0-9.]+px\]', '', cls).strip()
    return f'class="{g} {cls}"'
i = h.index('<body'); h = h[:i] + re.sub(r'class="([^"]*)"', scala, h[i:])
assert 'text-[72px]' not in h and 'text-[12.5px]' not in h and h.count('t-h2 ') >= 8 and 't-hero ' in h
# 5. su telefono: titolo, timbro e «Scrivimi» nel primo schermo, la foto subito dopo; la foto di «Chi sono» dopo la lettera
a_ = re.search(r'\n\s*<img src="img/alessio-cottonaro-in-consulenza.jpg" alt="" width="1199" height="1600" class="md:hidden[^"]*" loading="lazy">', h).group(0)
h = h.replace(a_, '', 1)
i = h.index('aria-label="Formazione e albi"'); j = h.index('</ul>', i) + 5
h = h[:j] + '\n      <img src="img/alessio-cottonaro-in-consulenza.jpg" alt="" width="1199" height="1600" class="md:hidden foto-m mt-12" loading="lazy">' + h[j:]
i = h.index('data-foto-per="hero"'); j = h.index('</section>', i)
h = h[:j] + '  <img src="img/alessio-cottonaro-ritratto-principale.jpg" alt="Alessio Cottonaro, consulente in sessuologia, seduto in una stanza chiara" width="1200" height="1600" class="md:hidden foto-m hero-foto-m mt-10">\n    ' + h[j:]
h = h.replace('<div class="md:order-1 px-6', '<div class="colonna-testo md:order-1 px-6', 1)
# 3. «Come funziona» in tre colonne con la cifra in alto; la fascia nera sotto, a tutta riga
fz = re.search(r'<section id="funziona".*?</section>', h, re.S).group(0)
desc = re.findall(r'<p class="t-body mt-2 font-body[^"]*">(.*?)</p>', fz, re.S); assert len(desc) == 3, len(desc)
vid = re.search(r'<a class="[^"]*apri-video.*?</a>', fz, re.S).group(0)
intro = re.search(r'<p class="[^"]*"[^>]*>(Tre passi.*?)</p>', fz, re.S).group(1)
def passo(cifra, quando, cosa, d, extra='', it=False):
    return f'''
      <li>
        <p class="cifra{" cifra--it" if it else ""}">{cifra}</p>
        <p class="quando t-small">{quando}</p>
        <h3 class="cosa t-h3">{cosa}</h3>
        <p class="t-body">{d}</p>{extra}
      </li>'''
FZ = f'''<section id="funziona" class="bg-brand-cream">
  <div class="max-w-[1280px] mx-auto px-6 md:px-10 py-20 md:py-32">
    <div class="testa-sez">
      <h2 class="t-h2 font-display text-brand-ink leading-[0.98] tracking-tighter2 reveal">Come <span class="italic text-brand-burgundy">funziona.</span></h2>
      <p class="t-body font-body text-brand-ink leading-[1.6] max-w-[30em] reveal" data-delay="1">{intro}</p>
    </div>
    <ol class="passi reveal" data-delay="2">{passo("Gratis", "Oggi", "Mi scrivi.", desc[0])}{passo("60&#8239;€", "La prima consulenza", "Un’ora insieme.", desc[1], chr(10) + "        " + vid)}{passo("su misura", "Dopo", "Decidiamo insieme.", desc[2], it=True)}
      <li class="fine t-body">Alla fine sai cosa stai guardando e da dove partire.</li>
    </ol>
  </div>
</section>'''
assert 'Alla fine sai cosa stai guardando' in fz
h = h.replace(fz, FZ, 1)
# 1b. titoli entro due righe: più misura a «Cosa faccio» e alle FAQ (titolo sopra, domande sotto a tutta riga)
for a_, b_ in [('<h2 class="t-h2 lg:col-span-4 font-display text-brand-cream', '<h2 class="t-h2 lg:col-span-5 font-display text-brand-cream'),
               ('<dl class="t-body lg:col-span-8 grid', '<dl class="t-body lg:col-span-7 grid'),
               ('<div class="grid md:grid-cols-12 gap-10 md:gap-16">\n      <div class="md:col-span-4">', '<div class="grid md:grid-cols-12 gap-10 md:gap-16">\n      <div class="md:col-span-12 testa-sez">'),
               ('tracking-tighter2 mb-8 reveal">\n          Quello che', 'tracking-tighter2 reveal">\n          Quello che'),
               ('<div class="md:col-span-8">\n        <ul class="border-y border-brand-line divide-y divide-brand-line">', '<div class="md:col-span-12 lg:col-start-3 lg:col-span-10">\n        <ul class="faq-lista">'),
               # 6. niente fili: la testata della home come quella del blog
               ('<header id="top" class="sticky top-0 z-40 bg-brand-cream/95 backdrop-blur-md border-b border-brand-line">', '<header id="top" class="sticky top-0 z-40 bg-brand-cream/95 backdrop-blur-md">')]:
    assert h.count(a_) == 1, a_[:60]; h = h.replace(a_, b_, 1)
# 3b. euro staccato da uno spazio fine che non va a capo
h = re.sub(r'(\d)&nbsp;€', '\\1&#8239;€', h)
# 6c. finitura unica, scala, virgolette appese, numeri: tutto in un foglio in fondo alla testa
CSS_V10 = '''<style>
  /* ── v10: un sistema solo ── */
  :root { ''' + TOKENS + ''' }
  html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
  .t-hero { font-size: var(--t-hero); } .t-h2 { font-size: var(--t-h2); } .t-h3 { font-size: var(--t-h3); }
  .t-lead { font-size: var(--t-lead); } .t-body { font-size: var(--t-body); } .t-small { font-size: var(--t-small); } .t-micro { font-size: var(--t-micro); }
  h1, h2, h3, dt { text-wrap: balance; } p, li, dd { text-wrap: pretty; }
  @media (max-width: 640px) { #main-content p, section p, dd { hyphens: auto; -webkit-hyphens: auto; } h1, h2, h3, .faq-question, .testo, #main-content [data-foto-per="hero"] p { hyphens: manual; -webkit-hyphens: manual; } }
  /* titolo della home: grande quanto la colonna permette */
  .colonna-testo { container-type: inline-size; }
  #titolo.t-hero { font-size: min(var(--t-hero), 14.8cqi); }
  /* le misure scritte nei fogli di stile, sugli stessi gradini */
  .vetrina .t, .per label, .prezzi .a-incontro, .prezzi .risparmi { font-size: var(--t-small) !important; }
  .prezzi .barrato { font-size: var(--t-body); }
  .sez-home a { font-size: var(--t-lead); }
  .sez-home h3 { font-size: var(--t-body) !important; }
  .vetrina .f { font-size: var(--t-h3) !important; line-height: 1.2 !important; }
  .contatti-righe a { font-size: calc(var(--t-h2) * .75) !important; }
  .contatti-righe .v { font-size: var(--t-h3) !important; }
  .btn-burgundy, .btn-cream-on-burgundy, .btn-outline-cream { font-size: var(--t-small); }
  .faq-lista > li + li { margin-top: 2px; }
  .faq-summary { padding-left: 12px; padding-right: 12px; }
  details[open] .faq-summary { padding-left: 12px; background-color: rgba(122,30,43,0.04); }
  .faq-answer { padding-left: 84px; }
  @media (max-width: 767px) { .faq-answer { padding-left: 12px; } }
  .faq-answer-text { font-size: var(--t-body); }
  /* schema «Tu → sessuologia»: niente maiuscoletto spaziato */
  .pm-t-cond, .pm-t-cond-v { text-transform: none !important; letter-spacing: 0 !important; font-style: italic; font-size: 18px; }
  .pm-t-st-small { text-transform: none !important; letter-spacing: 0 !important; font-size: 18px; font-style: italic; }
  /* 2. le «» sono il segno: la virgoletta d'apertura appesa fuori dal filo del testo */
  .frase .testo, .faq-question, .vetrina .f { text-indent: -.42em; }
  .ancora { display: block; font-family: 'DM Serif Display', Georgia, serif; font-size: clamp(150px, 16vw, 240px); line-height: .62; height: .62em; margin: -.12em 0 0 -.06em; color: #7A1E2B; user-select: none; pointer-events: none; }
  /* 6. un movimento solo: stessa curva e stessa durata per tutto ciò che si tocca */
  a:not(.reveal), button, summary, label, .arr, .arrow, .piu, .faq-plus, .v, .ar, .freccia { transition-duration: var(--dur) !important; transition-timing-function: var(--ease) !important; }
  .btn-burgundy:hover, .btn-cream-on-burgundy:hover, .btn-outline-cream:hover { transform: none; }
  .btn-burgundy:active, .btn-cream-on-burgundy:active, .btn-outline-cream:active, .per label:active { transform: scale(.97) !important; transition-duration: var(--dur-press) !important; }
  .contatti-righe .v { display: inline-block; transition-property: transform; }
  .contatti-righe a:hover .v, .contatti-righe a:focus-visible .v { transform: translateX(6px); }
  .vetrina a:hover .ar, .vetrina a:focus-visible .ar, .gift:hover .arrow { transform: translateX(6px); }
  .btn-burgundy:hover .arr { transform: translateX(4px); }
  header img[alt="AleEduSex"] { mix-blend-mode: darken; }
  @media (prefers-reduced-motion: reduce) {
    a:not(.reveal), button, summary, label, .arr, .arrow, .piu, .faq-plus, .v, .ar, .freccia { transition-duration: .01ms !important; }
    .contatti-righe a:hover .v, .vetrina a:hover .ar, .gift:hover .arrow, .btn-burgundy:hover .arr, .btn-burgundy:active { transform: none !important; }
  }
  /* 5. telefono: prima il titolo, poi la foto */
  .foto-m { width: 100%; aspect-ratio: 4 / 5; height: auto; object-fit: cover; object-position: 50% 30%; }
  .hero-foto-m { max-height: 60svh; }
  @media (max-width: 767px) {
    .foto-m { display: block; }
    .split-foto { display: none !important; }
    [data-foto-per="hero"] { padding-top: 40px !important; }
    #titolo .hero-line.mt-3 { margin-top: 8px; }
  }
  /* 3. i numeri protagonisti: «Come funziona» in tre colonne */
  .testa-sez { display: grid; gap: 24px; align-items: end; }
  @media (min-width: 1024px) { .testa-sez { grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); gap: 64px; } }
  .passi { list-style: none; margin: 48px 0 0; padding: clamp(28px, 4vw, 56px) clamp(24px, 4vw, 56px) 0; display: grid; gap: 80px clamp(24px, 4vw, 64px); background: #F8F1E0; }
  .passi .fine { margin-top: -32px !important; }
  @media (min-width: 900px) { .passi .fine { margin-top: 8px !important; } }
  @media (min-width: 900px) { .passi { grid-template-columns: repeat(3, minmax(0, 1fr)); margin-top: 72px; } }
  .passi .cifra { font-family: 'DM Serif Display', Georgia, serif; font-weight: 400; font-size: var(--t-h2); line-height: .95; letter-spacing: -0.02em; color: #1A1A1A; font-variant-numeric: lining-nums tabular-nums; white-space: nowrap; }
  .passi .cifra--it { font-style: italic; color: #7A1E2B; }
  .passi .quando { margin-top: 20px; font-weight: 600; color: #1A1A1A; }
  .passi .quando::after { content: "  →"; color: #7A1E2B; font-weight: 400; }
  .passi li:nth-child(3) .quando::after { content: none; }
  .passi .cosa { margin-top: 6px; font-family: 'DM Serif Display', Georgia, serif; line-height: 1.1; color: #1A1A1A; }
  .passi .cosa + p { margin-top: 10px; line-height: 1.6; color: #1A1A1A; max-width: 30em; }
  .passi .apri-video { margin-top: 12px; }
  .passi .fine { grid-column: 1 / -1; margin: 8px calc(-1 * clamp(24px, 4vw, 56px)) 0; padding: 22px clamp(24px, 4vw, 56px); background: #1A1A1A; color: #F0E7D5; line-height: 1.5; }
  /* 3b. percorsi: il prezzo grande, cifre in colonna, un solo filo a destra */
  .voce .riga .val { font-size: clamp(36px, 3.4vw, 44px) !important; line-height: 1; letter-spacing: -0.01em; font-variant-numeric: lining-nums tabular-nums; }
  .voce .riga { align-items: flex-start; }
  .voce .prezzi { display: grid; grid-template-columns: auto auto; justify-content: end; align-items: baseline; column-gap: 12px; row-gap: 4px; }
  .voce .prezzi .barrato { grid-column: 1; } .voce .prezzi .val { grid-column: 2; justify-self: end; }
  .voce .prezzi .risparmi, .voce .prezzi .a-incontro { grid-column: 1 / -1; justify-self: end; margin-top: 0; }
  @media (max-width: 640px) { .voce .prezzi { justify-content: start; } .voce .prezzi .val { grid-column: auto; justify-self: start; } .voce .prezzi .risparmi, .voce .prezzi .a-incontro { justify-self: start; } }
  .voce .riga > span:first-child { padding-top: 6px; }
  /* 4. stessa correzione di tono su tutte le foto delle copertine */
  .vetrina img { filter: saturate(.92) sepia(.05); }
</style>
'''
h = h.replace('</head>', CSS_V10 + '</head>', 1)
wr('index.html', h)

# 2c + 5b. articoli: la fascia bordeaux tiene frase, titolo e data; il sommario subito sotto; la « gigante a destra
for slug in LI:
    p = f'blog/{slug}.html'; a = rd(p)
    hd = re.search(r'<header class="article-head">(.*?)</header>', a, re.S)
    fr = re.search(r'\s*<p class="frase">.*?</p>', hd.group(1), re.S); h1 = re.search(r'\s*<h1>.*?</h1>', hd.group(1), re.S)
    le = re.search(r'\s*<p class="lede">.*?</p>', hd.group(1), re.S); mt = re.search(r'\s*<p class="post-meta">.*?</p>', hd.group(1), re.S)
    assert fr and h1 and le and mt, slug
    nuovo = f'\n      <div class="fascia">{fr.group(0)}{h1.group(0)}{mt.group(0)}\n      </div>{le.group(0)}\n    '
    a = a.replace(hd.group(0), f'<header class="article-head">{nuovo}</header>', 1); wr(p, a)

# 4. indice del blog e pagine di sezione: per ogni sezione un articolo grande, gli altri in elenco di frasi
def a_riga(li):
    li = li.replace('<li class="post-item">', '<li class="post-item post-item--riga">', 1)
    li = re.sub(r'\s*<img class="post-cover"[^>]*>', '', li)
    li = re.sub(r'\s*<p class="post-excerpt">.*?</p>', '', li, flags=re.S)
    li = re.sub(r'<span class="read-more">.*?</span></span>', FRECCIA, li, flags=re.S)
    return li
def ritmo(ol_html):
    lis = re.findall(r'<li class="post-item[^"]*">.*?</li>', ol_html, re.S)
    out = [lis[0].replace('<li class="post-item">', '<li class="post-item post-item--primo">', 1)] + [a_riga(x) for x in lis[1:]]
    return out
h = rd('blog/index.html')
for ol in re.findall(r'<ol class="post-list due">.*?</ol>', h, re.S):
    h = h.replace(ol, '<ol class="post-list ritmo">' + ''.join(ritmo(ol)) + '</ol>', 1)
assert h.count('class="post-item post-item--lead"') == 1 and 'post-list due' not in h
for slug in LI: assert f'href="/blog/{slug}.html"' in h, slug
wr('blog/index.html', h)
for s in SEZ:
    p = f'blog/{s["slug"]}/index.html'; hh = rd(p)
    for ol in re.findall(r'<ol class="post-list">.*?</ol>', hh, re.S):
        hh = hh.replace(ol, '<ol class="post-list ritmo">' + ''.join(ritmo(ol)) + '</ol>', 1)
    wr(p, hh)

with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('''
/* ══════ v10: le 6 mosse d'eccellenza ══════ */
:root { ''' + TOKENS + ''' }
html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
h1, h2, h3 { text-wrap: balance; } p, li { text-wrap: pretty; }
@media (max-width: 640px) { .prose p, .prose li, .post-excerpt, .about p, .intro, .lede { hyphens: auto; -webkit-hyphens: auto; } }

/* 6. lo stesso menu della home: sei voci e «Scrivimi»; su telefono si apre senza JavaScript */
.nav { gap: 12px; }
.nav-full { display: none !important; }
@media (min-width: 1024px) { .nav-full { display: flex !important; gap: 36px !important; } .nav-m { display: none; } .nav { gap: 36px; } }
.nav-m > summary { list-style: none; cursor: pointer; width: 44px; height: 44px; display: inline-flex; flex-direction: column; justify-content: center; align-items: center; gap: 5px; border-radius: 3px; }
.nav-m > summary::-webkit-details-marker { display: none; }
.nav-m .b { display: block; width: 20px; height: 1.5px; background: var(--ink); transition: transform var(--dur) var(--ease), opacity var(--dur) var(--ease); }
.nav-m[open] .b:nth-child(1) { transform: translateY(6.5px) rotate(45deg); }
.nav-m[open] .b:nth-child(2) { opacity: 0; }
.nav-m[open] .b:nth-child(3) { transform: translateY(-6.5px) rotate(-45deg); }
.nav-m > summary:focus-visible { outline: 2px solid var(--burgundy); outline-offset: 2px; }
.nav-m > ul { position: absolute; left: 0; right: 0; top: 100%; display: grid; gap: 4px; list-style: none; margin: 0; padding: 20px 24px 32px; background: var(--paper); }
.nav-m:not([open]) > ul { display: none; }
.nav-m > ul a { display: block; padding: 8px 0; font-family: var(--display); font-size: var(--t-h3); line-height: 1.15; color: var(--ink); }
.nav-m > ul a:hover, .nav-m > ul a[aria-current="page"] { color: var(--burgundy); }
.wordmark img { mix-blend-mode: darken; }

/* 6. un movimento solo */
a, button, summary, .ar, .arr, .freccia, .post-cover, .carta, .carta .ill { transition-duration: var(--dur) !important; transition-timing-function: var(--ease) !important; }
.btn-burgundy:active, .btn-cream:active, .btn-outline-cream:active, .domanda button:active { transform: scale(.97) !important; transition-duration: var(--dur-press) !important; }
.btn-burgundy:hover .arr { transform: translateX(4px); }
.read-more .ar, .freccia { display: inline-block; }
.post-item > a:hover .read-more .ar, .post-item > a:focus-visible .read-more .ar { transform: translateX(6px); }
@media (prefers-reduced-motion: reduce) {
  a, button, summary, .ar, .arr, .freccia, .post-cover, .carta, .carta .ill { transition-duration: .01ms !important; }
  .post-item > a:hover .read-more .ar, .post-item--riga > a:hover .freccia, .btn-burgundy:hover .arr, .btn-burgundy:active { transform: none !important; }
}

/* 1. la scala: sette gradini, uguali alla home */
body { font-size: var(--t-body); }
.blog-hero .hero-testo, .sez-hero .head > div { container-type: inline-size; }
.blog-hero h1 { font-size: min(var(--t-hero), 20cqi) !important; line-height: .98 !important; max-width: none !important; }
.sez-hero h1 { font-size: min(var(--t-h2), 13cqi) !important; line-height: 1 !important; }
.blog-hero .intro, .lede { font-size: var(--t-lead) !important; }
.list-h, .gruppo h2, .part-h { font-size: var(--t-h2) !important; line-height: 1 !important; letter-spacing: -0.03em; }
.about h2, .more h2, .domanda h2, .quadretti h2, .sez-index h2, .cta-box h2 { font-size: var(--t-h3) !important; line-height: 1.1 !important; }
.cta-box h2 { font-size: calc(var(--t-h2) * .62) !important; line-height: 1 !important; }
.post-title { font-size: var(--t-h3) !important; }
.post-item--lead .post-frase { font-size: var(--t-h3) !important; }
.post-item--lead .post-title { font-size: calc(var(--t-h2) * .5) !important; }
.btn-burgundy { font-size: var(--t-small); }
.site-footer .brand { font-size: var(--t-h3); }
.post-excerpt, .about p, .soon, .more li a { font-size: var(--t-body) !important; }
.post-meta, .post-meta .sez, .crumb, .gruppo header .c, .read-more, .author-box .role, .cta-box .price, .domanda .nota, .domanda .ok, .domanda .lbl-f, .site-footer ul, .site-footer .label { font-size: var(--t-small) !important; }
.site-footer .who, .site-footer .legal, .author-box .cred, figcaption, .disclaimer { font-size: var(--t-micro) !important; }
.prose { font-size: var(--t-body); }
@media (min-width: 768px) { .prose { font-size: 20px; } }
.prose h2 { font-size: calc(var(--t-h3) * 1.2); }
.prose blockquote { font-size: var(--t-h3); }
.carte .carta .n { font-size: var(--t-lead) !important; }
.carte li:first-child .carta .n { font-size: var(--t-h3) !important; }
.carte .carta .c { font-size: var(--t-small) !important; }
.dove-parti h2 { font-size: var(--t-small); }
.dove-parti .s, .sez-list .c { font-size: var(--t-small) !important; }
.sez-frase { font-size: var(--t-h3) !important; }

/* niente etichette in maiuscoletto spaziato */
.eyebrow { text-transform: none !important; letter-spacing: 0 !important; font-size: var(--t-small) !important; font-style: italic; }

/* 2. le «» sono il segno: virgoletta d'apertura appesa */
.dove-parti .f, .post-frase, .sez-frase, .article-head .frase { text-indent: -.42em; }

/* 5. articolo: la fascia bordeaux tiene frase, titolo e data; il sommario subito dopo */
.article-head .fascia { position: relative; margin-top: -1px; padding: 25px 0 44px; background: var(--burgundy); color: var(--cream); box-shadow: 0 0 0 100vmax var(--burgundy); clip-path: inset(0 -100vmax); }
.article-head .fascia .frase { display: block !important; min-height: 0 !important; margin: 0 !important; padding: 0 !important; box-shadow: none !important; clip-path: none !important; background: none !important;
  font-size: 30px !important; line-height: 1.15 !important; color: var(--cream) !important; font-style: italic; }
.article-head .fascia h1 { margin-top: 20px; color: var(--cream); font-size: 34px !important; line-height: 1.04 !important; }
.article-head .fascia .post-meta { margin: 18px 0 0 !important; color: rgba(240, 231, 213, .82); }
.article-head .fascia .post-meta .sep { color: rgba(240, 231, 213, .6); }
.article-head .fascia ::selection { background: rgba(240, 231, 213, 0.28); color: var(--cream); }
.article-head .lede { margin-top: 32px; }
@media (min-width: 768px) {
  .article-head .fascia { padding: 40px 0 64px; }
  .article-head .fascia .frase { font-size: 40px !important; }
  .article-head .fascia h1 { margin-top: 28px; font-size: min(var(--t-h2), 54px) !important; }
}
@media (min-width: 1180px) {
  .article-head .fascia::after { content: "«" / ""; position: absolute; left: calc(100% + clamp(40px, 6vw, 96px)); top: 50%; translate: 0 -50%;
    font-family: var(--display); font-size: clamp(200px, 22vw, 320px); line-height: .7; color: rgba(240, 231, 213, .2); pointer-events: none; }
}

/* 4. il ritmo dell'indice: per ogni sezione un articolo grande, gli altri in elenco di frasi */
.post-list.ritmo { display: block !important; padding-bottom: 0 !important; }
#articoli > .post-list:not(.ritmo) { padding-bottom: 0 !important; }
.post-list.ritmo .post-item--primo > a { overflow: visible !important; display: grid !important; grid-template-columns: 1fr !important; gap: 10px; padding: 32px 0 24px !important; }
.post-list.ritmo .post-item--primo > a > * { grid-column: 1 !important; grid-row: auto !important; }
.post-list.ritmo .post-item--primo .post-cover { margin: 0 0 14px !important; aspect-ratio: 16 / 10 !important; }
.post-list.ritmo .post-item--primo .post-frase { font-size: var(--t-h3); line-height: 1.25; margin: 0; }
.post-list.ritmo .post-item--primo .post-title { font-size: calc(var(--t-h2) * .5) !important; line-height: 1.08; }
@media (min-width: 1024px) {
  .post-list.ritmo .post-item--primo > a { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) !important; column-gap: 56px; align-items: center; padding: 40px 0 32px !important; }
  .post-list.ritmo .post-item--primo > a > .post-cover { grid-column: 1 !important; grid-row: 1 / span 6 !important; margin: 0 !important; }
  .post-list.ritmo .post-item--primo > a > :not(.post-cover) { grid-column: 2 !important; }
}
.post-list.ritmo .post-item--riga > a { display: grid !important; grid-template-columns: minmax(0, 1fr) auto !important; column-gap: 24px; row-gap: 6px; align-items: center;
  margin: 0 -16px; padding: 20px 16px !important; transition-property: background-color; }
.post-list.ritmo .post-item--riga > a > * { grid-column: 1 !important; grid-row: auto !important; animation: none !important; }
.post-list.ritmo .post-item--riga > a > .freccia { grid-column: 2 !important; grid-row: 1 / span 3 !important; font-size: var(--t-h3); color: var(--burgundy); transition-property: transform; }
.post-list.ritmo .post-item--riga > a:hover, .post-list.ritmo .post-item--riga > a:focus-visible { background: var(--paper); }
.post-list.ritmo .post-item--riga > a:hover .freccia, .post-list.ritmo .post-item--riga > a:focus-visible .freccia { transform: translateX(6px); }
.post-list.ritmo .post-item--riga .post-frase { margin: 0; font-size: var(--t-h3); line-height: 1.22; color: var(--ink); max-width: 34em; }
.post-list.ritmo .post-item--riga > a:hover .post-frase { color: var(--burgundy); }
.post-list.ritmo .post-item--riga .post-title { font-family: var(--body); font-size: var(--t-body) !important; line-height: 1.45; letter-spacing: 0; color: rgba(26, 26, 26, .82); }
.post-list.ritmo .post-item--riga > a:hover .post-title { color: rgba(26, 26, 26, .82); }
.post-list.ritmo .post-item--riga .post-meta { margin-top: 0 !important; }
.post-list.ritmo .post-item--riga .post-meta .sez { display: none; }
.post-list.ritmo .post-item--primo + .post-item--riga { margin-top: 8px; }
.gruppo { padding-top: clamp(64px, 8vw, 112px); }
.gruppo header .ico { width: clamp(30px, 3vw, 44px); height: clamp(30px, 3vw, 44px); }
/* stessa correzione di tono su tutte le copertine, finché non arrivano le illustrazioni nuove */
.post-cover, .cover img { filter: saturate(.92) sepia(.05); }

/* errore: a 390 px i quadretti delle sezioni non tagliano più i nomi lunghi */
@media (max-width: 520px) {
  .carte .carta { padding: 16px 14px !important; }
  .carte .carta .n { font-size: var(--t-body) !important; hyphens: auto; -webkit-hyphens: auto; overflow-wrap: break-word; }
  .carte li:first-child .carta .n { font-size: var(--t-h3) !important; }
  .carte .carta .testo { max-width: none; }
}
''')


# ── 21. v11: skill ux-animation-principles (tempi e variabili, target 44 px, barra Scrivimi su telefono, attesa del video) ──
TOKENS = ':root { --dur-fast: 150ms; --dur-base: 250ms; --dur-enter: 400ms; --ease-out: cubic-bezier(.22,1,.36,1); --ease-in: cubic-bezier(.55,0,1,.45); --stagger: 50ms; }'
with open(OUT / 'blog/blog.css', 'a') as c:
    c.write('\n/* ── v11: una sola famiglia di tempi (skill ux-animation-principles) ── */\n' + TOKENS + '''
.blog-hero h1, .article-head h1 { animation-duration: 450ms !important; animation-timing-function: var(--ease-out) !important; }
/* aree da 44 px per i link isolati (non quelli dentro il testo) */
.crumb a, .author-box a, .back-link, .site-footer ul a, .site-footer .legal a, .more > a { display: inline-flex; align-items: center; min-height: 44px; }
.site-footer ul { gap: 0 !important; }
.wordmark { display: inline-flex; align-items: center; min-height: 44px; }
''')
h = rd('index.html')
h = h.replace('</head>', '<style>' + TOKENS + '''
  .reveal { transition-duration: var(--dur-enter) !important; transition-timing-function: var(--ease-out) !important; }
  .reveal[data-delay="1"] { transition-delay: calc(var(--stagger) * 1) !important; }
  .reveal[data-delay="2"] { transition-delay: calc(var(--stagger) * 2) !important; }
  .reveal[data-delay="3"] { transition-delay: calc(var(--stagger) * 3) !important; }
  .hero-line { animation-duration: 450ms !important; animation-timing-function: var(--ease-out) !important; }
  .stamp-in, .block-stamp { animation-duration: 500ms !important; }
  footer a { display: inline-flex; align-items: center; min-height: 44px; }
  header a[href="#top"] { display: inline-flex !important; align-items: center; min-height: 44px; }
  footer ul { row-gap: 0 !important; }
  footer ul > li + li { margin-top: 0 !important; }
  /* barra «Scrivimi» in basso su telefono: compare dopo il primo schermo, sparisce sopra i contatti */
  .barra-cta { position: fixed; left: 12px; right: 12px; bottom: calc(12px + env(safe-area-inset-bottom)); z-index: 45; display: flex; align-items: center; justify-content: space-between; gap: 12px; min-height: 54px; padding: 0 20px; background: #7A1E2B; color: #F0E7D5; font-family: 'Source Serif 4', Georgia, serif; font-size: 16px; box-shadow: 0 10px 24px -12px rgba(26,26,26,.55); transform: translateY(160%); transition: transform var(--dur-base) var(--ease-in); }
  .barra-cta.vista { transform: translateY(0); transition-timing-function: var(--ease-out); }
  .barra-cta:active { transform: translateY(0) scale(.97); }
  .barra-cta small { font-size: 14px; color: rgba(240,231,213,.88); }
  .barra-cta:focus-visible { outline: 2px solid #F0E7D5; outline-offset: -5px; }
  @media (min-width: 1024px) { .barra-cta { display: none; } }
  @media (prefers-reduced-motion: reduce) { .barra-cta { transition: none; } }
  /* attesa del video: un anello che gira finché non parte */
  .vbox .attesa { position: absolute; inset: 0; margin: auto; width: 44px; height: 44px; border-radius: 50%; border: 3px solid rgba(240,231,213,.3); border-top-color: #F0E7D5; opacity: 0; pointer-events: none; transition: opacity var(--dur-fast) ease; animation: giro 800ms linear infinite; }
  .vbox.carica .attesa { opacity: 1; }
  .vbox.carica .vbox-play { opacity: 0; }
  @keyframes giro { to { transform: rotate(360deg); } }
</style>
</head>''', 1)
k = h.rindex('</body>')
h = h[:k] + '''<a class="barra-cta" href="#contatti" aria-hidden="true" tabindex="-1"><span>Scrivimi <small>· 15 minuti al telefono, Gratis</small></span><span aria-hidden="true">→</span></a>
<script>
  // Barra «Scrivimi» su telefono: visibile tra il primo schermo e i contatti.
  (function () {
    var barra = document.querySelector('.barra-cta'), hero = document.querySelector('[data-foto-per="hero"]'), cont = document.getElementById('contatti');
    if (!barra || !hero || !cont || !('IntersectionObserver' in window)) return;
    var fuoriHero = false, neiContatti = false;
    function agg() { var v = fuoriHero && !neiContatti; barra.classList.toggle('vista', v); barra.setAttribute('aria-hidden', v ? 'false' : 'true'); barra.tabIndex = v ? 0 : -1; }
    new IntersectionObserver(function (e) { fuoriHero = !e[0].isIntersecting; agg(); }).observe(hero);
    new IntersectionObserver(function (e) { neiContatti = e[0].isIntersecting; agg(); }, { rootMargin: '0px 0px -30% 0px' }).observe(cont);
  })();
  // Video: anello d'attesa finché il video non parte davvero.
  (function () {
    var box = document.querySelector('.vbox'); if (!box) return;
    var v = box.querySelector('video'), a = document.createElement('span'); a.className = 'attesa'; a.setAttribute('aria-hidden', 'true'); box.querySelector('.vbox-in').appendChild(a);
    ['loadstart', 'waiting'].forEach(function (t) { v.addEventListener(t, function () { box.classList.add('carica'); }); });
    ['playing', 'canplay', 'pause', 'error', 'emptied'].forEach(function (t) { v.addEventListener(t, function () { box.classList.remove('carica'); }); });
  })();
</script>
''' + h[k:]
wr('index.html', h)
# logo in testata, su tutte le pagine (alla fine, dopo che le pagine sono state riscritte)
for f in OUT.rglob('*.html'):
    h = f.read_text()
    h = re.sub(r'<a class="wordmark" href="/">(aleedusex|AleEduSex)</a>', f'<a class="wordmark" href="/">{IMG}</a>', h)
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
