"""Prototipo del blog per sezioni, versione 7 (decisioni di Alessio, 2-3 novembre 2026).
Uso: python3 genmock7.py <cartella-di-uscita>     Niente va online."""
import re, sys, pathlib, runpy
HERE = pathlib.Path(__file__).resolve().parent
SITE = HERE.parents[2] / 'site'
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
SEZ = runpy.run_path(str(HERE / 'sezioni.py'))['SEZIONI']
ic = runpy.run_path(str(HERE / 'icone7.py')); ill = ic['ill7']; ICON_CSS = ic['ICONE7_CSS']

src = (SITE / 'blog/index.html').read_text()
HEADER = re.search(r'<header class="site-header">.*?</header>', src, re.S).group(0)
FOOTER = re.search(r'<footer class="site-footer">.*?</footer>', src, re.S).group(0)
items = []
for m in re.finditer(r'<a href="/blog/([^"]+)\.html">\s*<p class="post-meta"><time datetime="([^"]+)">([^<]+)</time><span class="sep">[^<]*</span>(\d+) min</p>\s*<h2 class="post-title">([^<]+)</h2>\s*<p class="post-excerpt">([^<]+)</p>', src):
    slug, iso, date, mins, title, exc = m.groups()
    items.append(dict(slug=slug, iso=iso, date=date, min=mins, title=title, exc=exc))
by = {i['slug']: i for i in items}
for s in SEZ:
    s['posts'] = sorted([by[a] for a in s['articoli']], key=lambda p: p['iso'], reverse=True)
assert sum(len(s['posts']) for s in SEZ) == len(items), 'ogni articolo deve stare in una sezione'
sez_of = {a: s for s in SEZ for a in s['articoli']}
def href(s): return f'sezione-{s["slug"]}.html'          # online: /blog/<slug>/
def anchor(n): return re.sub(r'[^a-z]+', '-', n.lower().replace('à','a')).strip('-')

SMALL = {
 'prevenzione': '<path d="M12 2.8l7.2 3v5.4c0 4.6-3.1 8.2-7.2 10-4.1-1.8-7.2-5.4-7.2-10V5.8z"/><path d="M12 15.6s-3.2-1.9-3.2-4.2a1.7 1.7 0 0 1 3.2-.8 1.7 1.7 0 0 1 3.2.8c0 2.3-3.2 4.2-3.2 4.2z"/>',
 'corpo': '<path d="M12 2.5c.8 3 4.6 4.8 4.6 9.6a4.6 4.6 0 0 1-9.2 0c0-2.4 1.2-3.8 2.4-4.8-.2 2.3.9 3.6 2.1 3.6 0-3.2-1.3-5.6.1-8.4z"/><path d="M4 21.2c2.6-1.4 5.2-1.4 8 0s5.4 1.4 8 0"/>',
 'comunicazione': '<path d="M4 4.5h9.5a2 2 0 0 1 2 2V11a2 2 0 0 1-2 2H8.6L5.5 16v-3H4a2 2 0 0 1-2-2V6.5a2 2 0 0 1 2-2z"/><path d="M17.8 8.5H20a2 2 0 0 1 2 2V15a2 2 0 0 1-2 2h-1.5v3l-3.1-3h-3.9a2 2 0 0 1-2-2v-.4"/>',
 'difficolta': '<path d="M3 20.5c0-3.8 2.3-6.6 6-7.3 2.3-.5 3.9.6 5.6 0 3.2-1 6.2 1.3 6.2 5 0 1.4-.8 2.3-2.1 2.3z"/><path d="M11.8 13.3c0-2.5.4-4.9 1.2-7.1"/><path d="M12.2 8.8c-2.4.1-4-1.4-4.4-3.5 2.3-.1 4 1.3 4.4 3.5zM12.8 6.9c1.4-2 3.6-2.7 5.5-1.9-.8 1.9-3.2 2.8-5.5 1.9z"/>',
 'maschera': '<path d="M12 9.2C10 7.6 6.4 7 3.6 8 2.6 8.4 1.8 9 1.4 9.8c.5 2.8 2.3 5.2 5 5.8 2.1.4 3.8-.8 4.8-2 .3-.4.5-.5.8-.5s.5.1.8.5c1 1.2 2.7 2.4 4.8 2 2.7-.6 4.5-3 5-5.8-.4-.8-1.2-1.4-2.2-1.8C17.6 7 14 7.6 12 9.2z"/><path d="M4.8 11.2c1.2-1.4 3.4-1.5 4.9.1-1.2 1.3-3.4 1.4-4.9-.1zM19.2 11.2c-1.2-1.4-3.4-1.5-4.9.1 1.2 1.3 3.4 1.4 4.9-.1z"/><path d="M21.6 12.4c.5 3.4.7 6.8.8 10.4"/>',
 'approfondimenti': '<path d="M12 18.8C9.8 17.2 6 16.9 3 17.4V6c3-.6 6.8-.2 9 1.3zM12 18.8c2.2-1.6 6-1.9 9-1.4V6c-3-.6-6.8-.2-9 1.3z"/><path d="M16.9 5.7v4.4l1-.8 1 .8V5.5"/>',
}
def small(k): return f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{SMALL[k]}</svg>'

COMMON = ICON_CSS + '''
:root{--fg:var(--burgundy);--bg:var(--paper);--muted:rgba(26,26,26,.7);--tape:rgba(214,196,163,.55)}
html,body{overflow-x:clip}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
h1,h2,h3{text-wrap:balance} p{text-wrap:pretty}
.ico{width:22px;height:22px;flex:none;color:var(--burgundy)}
.lbl{font-size:14px;font-style:italic;color:var(--muted)}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@keyframes fade7{from{opacity:0;translate:0 8px}to{opacity:1;translate:0 0}}
@media (prefers-reduced-motion:no-preference){.in{animation:fade7 380ms cubic-bezier(.2,.7,.2,1) var(--td,0ms) both}}
/* pizzino: foglietto di carta con nastro adesivo */
.pz{position:relative;background:var(--paper);border-radius:3px;box-shadow:0 1px 0 rgba(255,255,255,.6) inset,0 10px 24px -16px rgba(60,30,20,.35),0 2px 5px -3px rgba(60,30,20,.25)}
.pz::before{content:"";position:absolute;top:-11px;left:50%;width:86px;height:24px;transform:translateX(-50%) rotate(-2deg);background:var(--tape);border-left:1px dashed rgba(122,30,43,.10);border-right:1px dashed rgba(122,30,43,.10);pointer-events:none}
.pz.alt::before{transform:translateX(-50%) rotate(3deg);left:38%}
.c1::before{width:104px;left:30%;transform:translateX(-50%) rotate(-4deg)}.c3::before{width:72px;left:64%}.c4::before{width:92px;left:24%;transform:translateX(-50%) rotate(5deg)}.c5::before{width:80px;left:70%;transform:translateX(-50%) rotate(-3deg)}.invite::before{width:110px;left:12%}.close::before{width:76px;left:84%}
'''
def page(title, desc, body, css):
    return f'''<!DOCTYPE html><html lang="it"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title>
<meta name="description" content="{desc}"><meta name="robots" content="noindex">
<link rel="stylesheet" href="/fonts/fonts.css"><link rel="stylesheet" href="/blog/blog.css">
<style>{COMMON}{css}</style></head><body>
<a class="skip" href="#contenuto">Vai al contenuto</a>
{HEADER}
<main id="contenuto">{body}</main>
{FOOTER}</body></html>'''

# ══════════ /blog/ ══════════
cssH = '''
.hero7{padding:56px 0 24px}
.hero7 h1{font-family:var(--display);font-size:48px;line-height:.98;letter-spacing:-.035em;max-width:15ch}
.hero7 .intro{margin-top:22px;max-width:34em;font-size:19px;line-height:1.6;color:rgba(26,26,26,.85)}
.board{display:grid;gap:30px;padding:44px 0 32px}
.card{padding:26px 22px 18px;display:flex;flex-direction:column;gap:10px;transition:transform 350ms var(--ease),box-shadow 350ms var(--ease)}
.card:has(.lk:focus-visible){outline:2px solid var(--burgundy);outline-offset:4px}
.card .ill{width:76px;height:76px;margin:-4px 0 0 -6px}
.card h2{font-family:var(--display);font-size:32px;line-height:1;letter-spacing:-.025em}
.card h2 a{outline:none}
.card h2 a::after{content:"";position:absolute;inset:0}
.card .tag{font-size:17px;line-height:1.5;font-style:italic;color:rgba(26,26,26,.82)}
.card ul{list-style:none;margin:6px 0 0;padding:0;position:relative;z-index:1}
.card li a{display:block;padding:11px 0;border-top:1px solid var(--line-soft);font-size:15.5px;line-height:1.4}
.card li a:hover{color:var(--burgundy);text-decoration:underline;text-underline-offset:3px}
.card .parts{display:flex;flex-wrap:wrap;gap:6px;position:relative;z-index:1;margin-top:4px}
.card .parts a{font-size:14px;padding:10px 12px;border-radius:999px;background:var(--cream);color:var(--burgundy);line-height:1.2}
.card .parts a:hover{text-decoration:underline;text-underline-offset:3px}
.card .all{position:relative;z-index:1;align-self:flex-start;margin-top:auto;padding:12px 0 6px;font-style:italic;color:var(--burgundy);text-decoration:underline;text-underline-offset:4px;text-decoration-color:var(--line)}
.card .all:focus-visible{outline:2px solid var(--burgundy);outline-offset:2px}
.invite{background:var(--burgundy);color:var(--cream);padding:30px 26px;display:grid;gap:18px;margin:16px 0 56px}
.invite::before{background:rgba(240,231,213,.35)}
.invite p{font-family:var(--display);font-size:23px;line-height:1.1;letter-spacing:-.02em;max-width:30ch}
.invite .btn-cream{justify-self:start}
.chron h2{font-family:var(--display);font-size:32px;line-height:1;letter-spacing:-.02em}
.chron .intro2{margin-top:8px;color:var(--muted);font-style:italic}
.chron ol{list-style:none;margin:20px 0 96px;padding:0;border-top:1px solid var(--line)}
.chron li a{display:grid;gap:4px;padding:14px 0;border-bottom:1px solid var(--line-soft)}
.chron .t{font-size:18px;line-height:1.35;transition:color .2s}
.chron a:hover .t{color:var(--burgundy)}
.chron .m{display:flex;gap:8px;align-items:center;font-size:14px;color:var(--muted)}
.chron .m .ico{width:18px;height:18px}
@media(max-width:767px){.card ul{display:none}.card{gap:6px}.card .ill{width:60px;height:60px}}
@media(min-width:768px){
 .hero7{padding:96px 0 40px}.hero7 h1{font-size:84px}.hero7 .intro{font-size:21px}
 .board{display:flex;flex-wrap:wrap;justify-content:center;align-items:flex-start;gap:40px 28px;padding:64px 0 40px}
 .card{width:calc(50% - 14px);transform:rotate(var(--r,0deg)) translateY(var(--y,0px))}
 .card:hover{transform:rotate(0) translateY(-4px)}
 .c1{width:calc(58% - 14px)}.c2{width:calc(42% - 14px);--y:36px}.c3{width:calc(34% - 19px)}.c4{width:calc(31% - 19px);--y:24px}.c5{width:calc(35% - 19px);--y:-8px}
 .c1 .ill{width:120px;height:120px}.c1 h2{font-size:52px}
 .invite{grid-template-columns:1fr auto;align-items:center;padding:36px 44px;transform:rotate(-.6deg)}.invite p{font-size:36px}
 .chron li a{grid-template-columns:150px 1fr 290px;align-items:baseline;gap:24px}
 .chron .m.th{justify-content:flex-end}
}
'''
R = [-1.4, 1.6, -1.0, 1.8, -1.6]
def card(s, k):
    if s.get('parti'):
        inner = '<div class="parts">' + ''.join(f'<a href="{href(s)}#{anchor(p["nome"])}">{p["nome"]}</a>' for p in s['parti']) + '</div>' + \
                '<ul>' + ''.join(f'<li><a href="/blog/{by[a]["slug"]}.html">{by[a]["title"]}</a></li>' for a in s['vetrina']) + '</ul>'
    else:
        inner = '<ul>' + ''.join(f'<li><a href="/blog/{by[a]["slug"]}.html">{by[a]["title"]}</a></li>' for a in s['vetrina']) + '</ul>'
    return f'''<article class="card pz{" alt" if k%2 else ""} c{k+1} live in" style="--r:{R[k]}deg;--td:{40+k*60}ms;--d:{200+k*150}ms">
{ill(s["icona"])}<h2><a class="lk" href="{href(s)}">{s["nome"]}</a></h2><p class="tag">{s["frase"]}</p>{inner}
<a class="all" href="{href(s)}">Tutti gli articoli della sezione</a></article>'''
chron = ''.join(f'''<li><a href="/blog/{p["slug"]}.html"><span class="m"><time datetime="{p["iso"]}">{p["date"]}</time></span><span class="t">{p["title"]}</span>
<span class="m th">{small(sez_of[p["slug"]]["icona"])}{sez_of[p["slug"]]["nome"]}</span></a></li>''' for p in items)
bodyH = f'''<section class="hero7"><div class="wrap">
<h1>Sessualità, senza giri di <span class="stamp">parole.</span></h1>
<p class="intro">Le domande che si fanno a bassa voce, con risposte scritte in chiaro. Gli articoli sono divisi in cinque sezioni: parti da quella che ti riguarda, oppure leggili dal più recente.</p></div></section>
<div class="wrap">
<section class="board" aria-label="Sezioni">{"".join(card(s,k) for k,s in enumerate(SEZ))}</section>
<aside class="invite pz"><p>Non c’è un livello minimo di disagio per meritarsi un’ora di chiarezza.</p><a class="btn-cream" href="/#contatti">Scrivimi</a></aside>
<section class="chron" aria-labelledby="tutti"><h2 id="tutti">Tutti gli articoli</h2><p class="intro2">Dal più recente.</p><ol>{chron}</ol></section>
</div>'''
(OUT/'blog.html').write_text(page('Blog di sessuologia, per sezioni — Alessio Cottonaro',
    'Corpo e piacere, prevenzione, comunicazione e consenso, difficoltà, approfondimenti: gli articoli di Alessio Cottonaro, consulente in sessuologia a Torino.', bodyH, cssH))

# ══════════ SEZIONI ══════════
cssS = '''
.sec-hero{padding:24px 0 8px}
.sec-hero .box{padding:22px 22px 26px;display:grid;gap:6px;margin-top:18px}
.sec-hero .crumb{padding-top:0;font-size:15px}
.sec-hero .crumb a{display:inline-block;padding:10px 0;border:0;color:var(--burgundy);text-decoration:underline;text-underline-offset:4px;text-decoration-color:var(--line)}
.sec-hero .ill{width:72px;height:72px;margin:2px 0 0 -6px}
.sec-hero h1{font-family:var(--display);font-size:46px;line-height:.95;letter-spacing:-.035em}
.sec-hero .lead{margin-top:12px;font-size:19px;line-height:1.6;max-width:36em;color:rgba(26,26,26,.86)}
.book{display:grid;padding:24px 0}
.toc-side{display:none}
.toc-mob{display:flex;flex-wrap:wrap;gap:6px;padding:0 0 64px}
.toc-mob a{display:inline-flex;gap:6px;align-items:center;border-radius:999px;min-height:44px;padding:8px 12px 8px 8px;font-size:14px;background:var(--paper)}
.idx{list-style:none;margin:0;padding:0}
.idx li{position:relative;display:grid;gap:4px;padding:18px 0;border-bottom:1px solid var(--line-soft)}
.idx .row{display:flex;align-items:baseline;gap:12px}
.idx a.t{font-size:20px;line-height:1.35;transition:color .2s}
.idx a.t::after{content:"";position:absolute;inset:0}
.idx a.t:focus-visible{outline:none}.idx li:has(a.t:focus-visible){outline:2px solid var(--burgundy);outline-offset:4px;border-radius:4px}
.idx li:hover a.t{color:var(--burgundy)}
.idx .dots{flex:1;border-bottom:1px dotted var(--line);transform:translateY(-5px);min-width:24px}
.idx .m{font-size:14px;color:var(--muted);white-space:nowrap;font-style:italic}
.idx .x{font-size:16px;line-height:1.55;font-style:italic;color:rgba(26,26,26,.7);max-width:40em}
.part{margin-top:36px}.part:first-child{margin-top:0}
.part h2{font-family:var(--display);font-size:30px;line-height:1}
.part .pd{margin-top:6px;color:var(--muted);font-style:italic}
.part{scroll-margin-top:110px}
.soon{margin-top:44px;padding:24px 24px 16px;display:grid;gap:4px;max-width:30em}
.soon-t{font-family:var(--display);font-size:26px;line-height:1.1}
.soon a{justify-self:start;padding:10px 0;font-style:italic;color:var(--burgundy);text-decoration:underline;text-underline-offset:4px;text-decoration-color:var(--line)}
.about{margin-top:48px;max-width:38em}
.about h2{font-family:var(--display);font-size:30px;line-height:1;margin-bottom:14px}
.about p{font-size:18px;line-height:1.7;margin-top:14px}
.close{background:var(--burgundy);color:var(--cream);padding:26px 24px;margin:48px 0 28px;display:grid;gap:16px}
.close::before{background:rgba(240,231,213,.35)}
.close p{font-family:var(--display);font-size:22px;line-height:1.1;max-width:30ch}
.close .btn-cream{justify-self:start}
.next{display:flex;align-items:center;justify-content:space-between;gap:16px;margin:0 0 40px;padding:20px 22px;transition:transform .3s var(--ease)}
.next:hover{transform:translateY(-3px)}
.next:focus-visible{outline:2px solid var(--burgundy);outline-offset:3px}
.next b{display:block;font-weight:400;font-family:var(--display);font-size:30px;line-height:1;margin-top:6px}
.next .ill{width:72px;height:72px;flex:none}
@media(min-width:900px){
 .toc-mob{display:none}
 .sec-hero{padding-top:40px}.sec-hero .box{grid-template-columns:1fr 250px;column-gap:48px;padding:36px 40px 40px;transform:rotate(-.5deg)}
 .sec-hero .box>*{grid-column:1}.sec-hero .ill{grid-column:2;grid-row:1/6;width:240px;height:240px;margin:-24px -12px 0 0;justify-self:end;align-self:start}
 .sec-hero h1{font-size:80px}
 .book{grid-template-columns:270px 1fr;gap:64px;padding-top:40px}
 .toc-side{display:block;position:sticky;top:110px;align-self:start}
 .toc-side ol{list-style:none;margin:12px 0 0;padding:0}
 .toc-side a{display:flex;gap:12px;align-items:center;padding:10px;border-radius:10px;margin-left:-10px;transition:background .2s}
 .toc-side a:hover{background:var(--paper)}
 .toc-side a[aria-current]{background:var(--paper);color:var(--burgundy)}
 .toc-side .all{display:inline-block;margin-top:14px;padding:10px 0;font-style:italic;color:var(--burgundy)}
 .idx a.t{font-size:22px}
 .close{grid-template-columns:1fr auto;align-items:center;padding:30px 36px;transform:rotate(.5deg)}.close p{font-size:26px}
 .next{margin-bottom:96px;transform:rotate(-.6deg)}.next:hover{transform:rotate(0) translateY(-3px)}
}
'''
def lis(posts):
    return ''.join(f'''<li><span class="row"><a class="t" href="/blog/{p["slug"]}.html">{p["title"]}</a><span class="dots" aria-hidden="true"></span><span class="m">{p["min"]} min</span></span>
<span class="x">{p["exc"]}</span><span class="lbl"><time datetime="{p["iso"]}">{p["date"]}</time></span></li>''' for p in posts)
for i, s in enumerate(SEZ):
    nx = SEZ[(i+1) % len(SEZ)]
    side = '<nav class="toc-side" aria-label="Sezioni del blog"><p class="lbl">Sezioni del blog</p><ol>' + ''.join(
        f'<li><a href="{href(o)}"{" aria-current=page" if o is s else ""}>{small(o["icona"])}{o["nome"]}</a></li>' for o in SEZ) + \
        '</ol><a class="all" href="blog.html">Tutti gli articoli</a></nav>'
    mob = '<nav class="toc-mob" aria-label="Altre sezioni"><p class="lbl" style="width:100%">Altre sezioni</p>' + ''.join(
        f'<a href="{href(o)}"{" aria-current=page" if o is s else ""}>{small(o["icona"])}{o["nome"]}</a>' for o in SEZ) + '</nav>'
    if s.get('parti'):
        piene = [p for p in s['parti'] if p['articoli']]; vuote = [p for p in s['parti'] if not p['articoli']]
        lista = ''.join(f'''<section class="part" id="{anchor(p["nome"])}"><h2>{p["nome"]}</h2><ol class="idx">{lis([by[a] for a in p["articoli"]])}</ol></section>''' for p in piene)
        if vuote:
            lista += ''.join(f'<span id="{anchor(p["nome"])}"></span>' for p in vuote) + \
                f'''<aside class="soon pz alt"><p class="lbl">In arrivo</p><p class="soon-t">{" e ".join(p["nome"] for p in vuote)}</p>
<a href="/#contatti">Scrivimi cosa vorresti leggere</a></aside>'''
    else:
        lista = f'<h2 class="sr">Articoli</h2><ol class="idx">{lis(s["posts"])}</ol>'
    nomi_parti = [q['nome'] + '.' for q in s.get('parti', [])]
    def grassetto(t):
        for n in nomi_parti:
            if t.startswith(n): return f'<strong>{n}</strong>' + t[len(n):]
        return t
    resto = ''.join(f'<p>{grassetto(p)}</p>' for p in s['intro'][1:])
    body = f'''<section class="sec-hero"><div class="wrap">
<div class="box pz live" style="--d:100ms"><p class="crumb"><a href="blog.html">Blog</a> <span aria-hidden="true">/</span> <span aria-current="page">{s["nome"]}</span></p>{ill(s["icona"])}
<h1>{s["h1"]}</h1><p class="lead">{s["intro"][0]}</p></div></div></section>
<div class="wrap"><div class="book">{side}<div>{lista}
<section class="about" aria-labelledby="about"><h2 id="about">Su questa sezione</h2>{resto}</section>
<aside class="close pz"><p>Non serve la parola giusta. Scrivimi come viene.</p><a class="btn-cream" href="/#contatti">Scrivimi</a></aside>
<a class="next pz alt live" href="{href(nx)}" style="--d:400ms"><span><span class="lbl">Prossima sezione</span><b>{nx["nome"]}</b></span>{ill(nx["icona"])}</a>{mob}</div></div></div>'''
    (OUT/f'sezione-{s["slug"]}.html').write_text(page(s['titolo_pagina'], s['descrizione'], body, cssS))

# ══════════ TAVOLA ICONE ══════════
cssI = '''.sheet{display:grid;gap:32px;padding:24px 0 96px}.plate{padding:48px 24px 24px;display:grid;gap:12px;justify-items:center;text-align:center}
.plate .ill{width:200px;height:200px}.plate h2{font-family:var(--display);font-size:26px;line-height:1.05}
@media(min-width:768px){.sheet{grid-template-columns:repeat(3,1fr);gap:40px 28px}}'''
plates = ''.join(f'<article class="plate pz{" alt" if k%2 else ""} live" tabindex="0" style="--d:{k*200}ms">{ill(s["icona"])}<h2>{s["nome"]}</h2></article>' for k,s in enumerate(SEZ))
(OUT/'icone.html').write_text(page('Icone delle sezioni', 'Tavola delle icone delle cinque sezioni.', f'<div class="wrap"><h1 style="font-family:var(--display);font-size:56px;line-height:1;padding:64px 0 24px">Icone delle sezioni</h1><div class="sheet">{plates}</div></div>', cssI))

# ══════════ ARTICOLO (testa e coda) ══════════
for slug, nome in [('sesso-vanilla-cosa-significa', 'articolo-esempio.html'), ('foucault-storia-della-sessualita', 'articolo-approfondimenti.html')]:
    art = (SITE/f'blog/{slug}.html').read_text(); s = sez_of[slug]
    art = art.replace('<p class="crumb"><a href="/blog/">Blog</a> <span aria-hidden="true">/</span></p>',
      f'<p class="crumb"><a href="blog.html">Blog</a> <span aria-hidden="true">/</span> <a class="tchip" href="{href(s)}">{small(s["icona"])}{s["nome"]}</a></p>')
    ib = re.search(r'\n\s*<aside class="in-breve".*?</aside>', art, re.S)
    if ib:
        art = art.replace(ib.group(0), '')
        art = art.replace('<div class="prose">', ib.group(0).strip().replace('class="in-breve"', 'class="in-breve pz"') + '\n    <div class="prose">', 1)
    others = [p for p in s['posts'] if p['slug'] != slug]
    box = (f'<p class="lbl">Altri articoli in {s["nome"]}</p><ul>' + ''.join(f'<li><a href="/blog/{p["slug"]}.html">{p["title"]}</a></li>' for p in others) + '</ul>') if others \
          else f'<p class="lbl">Questo articolo fa parte di {s["nome"]}</p>'
    art = art.replace('<a class="back-link" href="/blog/">← Tutti gli articoli</a>',
      f'''<section class="more pz">{box}<a href="{href(s)}">Tutta la sezione {s["nome"]}</a></section>
    <a class="back-link" href="blog.html">← Tutti gli articoli</a>''')
    art = art.replace('</head>', '''<style>:root{--tape:rgba(214,196,163,.55)}
.pz{position:relative;background:var(--paper);border-radius:3px;box-shadow:0 10px 24px -16px rgba(60,30,20,.35),0 2px 5px -3px rgba(60,30,20,.25)}
.pz::before{content:"";position:absolute;top:-11px;left:50%;width:86px;height:24px;transform:translateX(-50%) rotate(-2deg);background:var(--tape)}
.more{margin-top:56px;padding:26px 24px 18px}
.more ul{list-style:none;margin:10px 0 12px;padding:0}.more li a{display:block;padding:10px 0;border-top:1px solid var(--line-soft);font-size:18px}
.more>a{font-style:italic;color:var(--burgundy);display:inline-block;padding:8px 0}.lbl{font-size:14px;font-style:italic;color:rgba(26,26,26,.7)}
.prose a{overflow-wrap:anywhere}
.crumb .tchip{display:inline-flex;gap:6px;align-items:center;background:var(--paper);color:var(--burgundy);border:1px solid var(--line-soft);border-radius:999px;padding:4px 12px 4px 8px;margin-left:2px}
.crumb .tchip .ico{width:18px;height:18px;color:var(--burgundy)}
.in-breve.pz{border:0;margin:8px 0 40px;padding:28px 26px 22px}.in-breve .eyebrow{letter-spacing:0;text-transform:none;font-size:15px;font-style:italic}
</style><meta name="robots" content="noindex"></head>''')
    (OUT/nome).write_text(art)
print('ok', len(items), [(s['nome'], len(s['posts'])) for s in SEZ])
