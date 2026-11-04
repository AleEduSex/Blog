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
    return f'''<details class="video mt-5">
              <summary class="list-none [&::-webkit-details-marker]:hidden cursor-pointer inline-flex items-center gap-2.5 min-h-[44px] font-body text-[16px] text-brand-burgundy" aria-label="Guarda il video: {titolo}, {durata}">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><circle cx="12" cy="12" r="10.5"/><path d="M10 8.2v7.6l6-3.8z" fill="currentColor" stroke="none"/></svg>
                <span class="underline underline-offset-4 decoration-brand-burgundy/35">Guarda il video</span> <span class="text-brand-ink/80 text-[15px]">{durata}</span>
              </summary>
              <video class="mt-4 w-full max-w-[260px] aspect-[9/16] bg-brand-ink/10" controls preload="none" playsinline poster="/video/{n}.jpg" aria-label="Video: {titolo}"><source src="/video/{n}.mp4" type="video/mp4"></video>
            </details>'''
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
# diagramma di oggi, senza ombra né rotazione
diag = re.search(r'(<svg class="pm-map pm-map-h".*?</svg>\s*<svg class="pm-map pm-map-v".*?</svg>)', land, re.S).group(1)
diag = re.sub(r'\s*<defs>.*?</defs>', '', diag, flags=re.S).replace(' filter="url(#pm-shadow-h)"', '').replace(' filter="url(#pm-shadow-v)"', '')
DIAG = f'<div class="diag-card reveal">{diag}</div>'
# blog: i nomi delle sezioni grandi, come un indice
ultimo = max(LI, key=lambda a: date[a])
nomi = ''.join(f'''
          <li><a href="/blog/{s["slug"]}/" class="group flex items-baseline justify-between gap-6 py-3 md:py-4"><span class="font-display text-brand-ink text-[28px] md:text-[40px] xl:text-[48px] leading-[1.05] tracking-tighter2 group-hover:text-brand-burgundy transition-colors">{s["nome"]}</span><span class="font-body text-[15px] text-brand-ink/80 whitespace-nowrap">{n_art(s)} <span class="inline-block transition-transform group-hover:translate-x-1" aria-hidden="true">→</span></span></a></li>''' for s in SEZ)
BLOG = f'''<!-- ═══════ Dal blog: i nomi delle sezioni come indice ═══════ -->
<section id="dal-blog" class="bg-brand-paper">
  <div class="max-w-[1280px] mx-auto px-6 md:px-10 py-20 md:py-36">
    <div class="grid lg:grid-cols-12 gap-10 md:gap-16">
      <div class="lg:col-span-4">
        <h2 class="font-display text-brand-ink text-[34px] md:text-[48px] leading-[1.02] tracking-tighter2 reveal">Se preferisci leggere prima.</h2>
        <p class="mt-6 font-body text-brand-ink text-[18px] leading-[1.6] reveal" data-delay="1">Nel blog rispondo alle domande che si fanno a bassa voce, un tema alla volta.</p>
        <p class="mt-8 font-body text-[16px] text-brand-ink/80 reveal" data-delay="1">Ultimo articolo:<br><a href="/blog/{ultimo}.html" class="font-display text-brand-ink text-[22px] leading-[1.25] underline underline-offset-4 decoration-brand-burgundy/35 hover:text-brand-burgundy">{titoli[ultimo]}</a></p>
        <a href="/blog/" class="btn-burgundy mt-10 reveal" data-delay="2">Vai al blog <span class="arr" aria-hidden="true">→</span></a>
      </div>
      <ol class="lg:col-span-8 reveal" data-delay="1">{nomi}
      </ol>
    </div>
  </div>
</section>'''
# percorsi: come un listino, raggruppati
P = [
 ('Da solo o in coppia', [
  ('al-cuore-del-problema', 'Al cuore del problema', '450&nbsp;€', 'Cinque incontri per capire dove si è bloccato qualcosa e cosa fare, con il metodo DEOPIARCA della Scuola di sessuologia di Torino.', '5 incontri da 60 minuti, ogni due settimane. Il prezzo è per tutto il percorso.', '58 s')]),
 ('In piccolo gruppo', [
  ('dialogo-positivo-sul-desiderio', 'Dialogo positivo sul desiderio', '240&nbsp;€', 'Per coppie con desideri diversi, che non riescono più a parlarne senza ferirsi.', '3 incontri da 90 minuti, gruppi di 4 coppie. 240 € a coppia, 300 € se partecipi senza partner.', '1 min 56'),
  ('laboratorio-del-piacere-consapevole', 'Laboratorio del piacere consapevole', '400&nbsp;€', 'Per coppie: corpo, desiderio, comunicazione, sex toys. Niente nudità né pratiche esplicite.', '4 incontri da 90 minuti, al massimo 3 coppie. Prezzo a coppia.', '2 min 16'),
  ('parliamo-di-sessualita-ai-figli', 'Parliamo di sessualità ai figli', '280&nbsp;€', 'Per genitori con figli tra 4 e 18 anni: come rispondere alle domande, età per età.', '4 incontri da 90 minuti, al massimo 8 persone.', '1 min 46')]),
]
gruppi = ''.join(f'''
        <div class="gruppo">
          <h3 class="font-body font-semibold text-[17px] text-brand-ink">{g}</h3>
          <ul class="mt-2">{"".join(f"""
            <li class="voce pt-7">
              <div class="riga"><span class="font-display text-brand-ink text-[26px] md:text-[30px] leading-[1.12] tracking-tightish">{nome}</span><span class="val">{prezzo}</span></div>
              <p class="mt-2 font-body text-[17px] leading-[1.6] text-brand-ink max-w-[38em]">{desc}</p>
              {video(slug, durata, nome)}
              <p class="mt-3 font-body text-[16px] leading-[1.55] text-brand-ink/80 max-w-[38em]">{meta}</p>
            </li>""" for slug, nome, prezzo, desc, meta, durata in voci)}
          </ul>
        </div>''' for g, voci in P)
PERCORSI = f'''<!-- ═══════ I percorsi: come un listino ═══════ -->
<section id="percorsi" class="bg-brand-cream">
  <div class="max-w-[1280px] mx-auto px-6 md:px-10 py-20 md:py-36">
    <div class="grid lg:grid-cols-12 gap-10 md:gap-16">
      <div class="lg:col-span-4">
        <h2 class="font-display text-brand-ink text-[34px] md:text-[48px] leading-[1.02] tracking-tighter2 reveal">I percorsi.</h2>
        <p class="mt-6 font-body text-brand-ink text-[18px] leading-[1.6] reveal" data-delay="1">Te li propongo dopo la prima consulenza, solo se hanno senso per te. Ognuno ha un obiettivo chiaro e un numero di incontri definito. Si prenotano come la prima consulenza.</p>
        <a href="#contatti" class="btn-burgundy mt-10 reveal" data-delay="2">Scrivimi per un percorso <span class="arr" aria-hidden="true">→</span></a>
      </div>
      <div class="lg:col-span-8 space-y-16 reveal" data-delay="1">{gruppi}
      </div>
    </div>
  </div>
</section>'''
VIDEO_PRIMA = video('prima-consulenza', '44 s', 'come funziona la prima consulenza')
corpo = (PERC.parent / 'generatore' / 'home-v3.html').read_text()
for k, v in {'{{FRASI}}': frasi, '{{BLOG}}': BLOG, '{{PERCORSI}}': PERCORSI, '{{DIAGRAMMA}}': DIAG, '{{VIDEO_PRIMA}}': VIDEO_PRIMA, '{{GIFT_URL}}': GIFT_URL, '{{EMAIL_ENT}}': EMAIL_ENT}.items():
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
  .gift:hover .arrow { transform: translateX(4px); }
  .diag-card { background: transparent !important; box-shadow: none !important; border: 0 !important; padding: 0 !important; transform: none !important; }
  .diag-card .pm-ink { stroke-dashoffset: 0 !important; animation: none !important; }
  .diag-card .pm-stamp, .diag-card .pm-fade, .diag-card .pm-dot { opacity: 1 !important; transform: none !important; animation: none !important; }
  .diag-card .pm-ripple { display: none; }
  @media (prefers-reduced-motion: reduce) { .split-foto .foto { transition: none; } .diag-card .pm-stamp { opacity: 1; transform: none; } }
</style>
'''
land = land.replace('</head>', CSS_V3 + '</head>', 1)
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
k = land.rindex('</body>'); land = land[:k] + FOTO_JS + land[k:]
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
