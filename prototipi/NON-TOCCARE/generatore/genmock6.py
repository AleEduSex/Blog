"""Prototipo del blog per temi (versione 6). Genera pagine di prova, niente va online.
Uso: python3 genmock6.py <cartella-di-uscita>"""
import re, sys, pathlib
HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
SITE = HERE.resolve().parents[2] / 'site'   # la cartella site/ del repository
exec((HERE/'icons5.py').read_text())

src = (SITE/'blog/index.html').read_text()
HEADER = re.search(r'<header class="site-header">.*?</header>', src, re.S).group(0)
FOOTER = re.search(r'<footer class="site-footer">.*?</footer>', src, re.S).group(0)
items = []
for m in re.finditer(r'<a href="/blog/([^"]+)\.html">\s*<p class="post-meta"><time datetime="([^"]+)">([^<]+)</time><span class="sep">[^<]*</span>(\d+) min</p>\s*<h2 class="post-title">([^<]+)</h2>\s*<p class="post-excerpt">([^<]+)</p>', src):
    slug, iso, date, mins, title, exc = m.groups()
    items.append(dict(slug=slug, iso=iso, date=date, min=mins, title=title, exc=exc))
by = {i['slug']: i for i in items}

# Icone piccole (24px) per indice e elenco
SMALL = {
 'protezione': '<path d="M12 2.8l7.2 3v5.4c0 4.6-3.1 8.2-7.2 10-4.1-1.8-7.2-5.4-7.2-10V5.8z"/><path d="M12 15.6s-3.2-1.9-3.2-4.2a1.7 1.7 0 0 1 3.2-.8 1.7 1.7 0 0 1 3.2.8c0 2.3-3.2 4.2-3.2 4.2z"/>',
 'piacere': '<path d="M12 2.5c.8 3 4.6 4.8 4.6 9.6a4.6 4.6 0 0 1-9.2 0c0-2.4 1.2-3.8 2.4-4.8-.2 2.3.9 3.6 2.1 3.6 0-3.2-1.3-5.6.1-8.4z"/><path d="M4 21.2c2.6-1.4 5.2-1.4 8 0s5.4 1.4 8 0"/>',
 'desiderio': '<path d="M12 9.2C10 7.6 6.4 7 3.6 8 2.6 8.4 1.8 9 1.4 9.8c.5 2.8 2.3 5.2 5 5.8 2.1.4 3.8-.8 4.8-2 .3-.4.5-.5.8-.5s.5.1.8.5c1 1.2 2.7 2.4 4.8 2 2.7-.6 4.5-3 5-5.8-.4-.8-1.2-1.4-2.2-1.8C17.6 7 14 7.6 12 9.2z"/><path d="M4.8 11.2c1.2-1.4 3.4-1.5 4.9.1-1.2 1.3-3.4 1.4-4.9-.1zM19.2 11.2c-1.2-1.4-3.4-1.5-4.9.1 1.2 1.3 3.4 1.4 4.9-.1z"/><path d="M21.6 12.4c.5 3.4.7 6.8.8 10.4"/>',
 'coppia': '<path d="M4 4.5h9.5a2 2 0 0 1 2 2V11a2 2 0 0 1-2 2H8.6L5.5 16v-3H4a2 2 0 0 1-2-2V6.5a2 2 0 0 1 2-2z"/><path d="M17.8 8.5H20a2 2 0 0 1 2 2V15a2 2 0 0 1-2 2h-1.5v3l-3.1-3h-3.9a2 2 0 0 1-2-2v-.4"/>',
 'difficolta': '<path d="M6 11h12a2 2 0 0 1 2 2v7a2.5 2.5 0 0 1-2.5 2.5h-11A2.5 2.5 0 0 1 4 20v-7a2 2 0 0 1 2-2z"/><path d="M7.6 11V7.4a4.4 4.4 0 0 1 8.3-2"/><path d="M12 15.2v2.6"/><circle cx="12" cy="15" r=".9"/>',
}
def small(k): return f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{SMALL[k]}</svg>'

def mix(a, b, t):
    a = [int(a[i:i+2], 16) for i in (1, 3, 5)]; b = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return '#' + ''.join(f'{round(x*(1-t)+y*t):02X}' for x, y in zip(a, b))
CREAM, BURG = '#F0E7D5', '#7A1E2B'
def warm(p, t=.38): return mix(mix(p, CREAM, t), BURG, .035)   # pastello scaldato verso crema e bordeaux

SEZ = [
 ('protezione-e-salute','protezione','Protezione e salute','#CFDDC9','#3F5A3A',
  'Quando c’è un dubbio serve un’informazione chiara, non una predica.',
  'Un preservativo che si rompe, un test da fare, una pillola da prendere in fretta: sono momenti in cui serve un’informazione chiara, non una predica. Qui trovi le cose pratiche: come si usano i preservativi, quali test esistono e dove farli, cosa sono PEP e PrEP. Per le terapie il riferimento resta il medico o il consultorio; qui trovi da dove partire, con calma.',
  ['preservativo-rotto-cosa-fare','infezioni-sessualmente-trasmissibili-test','pep-e-prep-hiv'],
  ['come-mettere-il-preservativo','lubrificante-e-preservativo','preservativo-chi-deve-saperlo-mettere','preservativo-interno','preservativo-rotto-cosa-fare','pillola-del-giorno-dopo','pep-e-prep-hiv','infezioni-sessualmente-trasmissibili-test']),
 ('piacere-e-corpo','piacere','Piacere e corpo','#F4CDB9','#8A3F22',
  'Il corpo non è una prova da superare.',
  'Il corpo non è una prova da superare. Qui parlo di orgasmo, masturbazione, sex toys e sesso anale per come sono davvero: cose normali, che si possono conoscere meglio. Niente classifiche e niente prestazioni da raggiungere, solo informazioni per ascoltarti con più curiosità.',
  ['orgasmo-cos-e-cosa-succede-nel-corpo','masturbazione-e-normale-quando-preoccuparsi','sex-toys-in-sicurezza'],
  ['orgasmo-cos-e-cosa-succede-nel-corpo','masturbazione-e-normale-quando-preoccuparsi','sesso-anale-in-sicurezza','sex-toys-in-sicurezza','come-scegliere-un-lubrificante-intimo']),
 ('desiderio-e-fantasie','desiderio','Desiderio e fantasie','#D3C2E0','#6B3A5E',
  'Quello che immagini non dice chi sei: dice cosa ti accende.',
  'Quello che immagini non dice chi sei: dice cosa ti accende. Fantasie, kink, sesso vanilla. In questa sezione provo a dare un nome alle cose, senza giudizio, e a spiegare come parlarne e sperimentare in modo sicuro e consensuale.',
  ['fantasie-sessuali-e-immaginario-erotico','kink-cos-e-come-sperimentare','sesso-vanilla-cosa-significa'],
  ['fantasie-sessuali-e-immaginario-erotico','kink-cos-e-come-sperimentare','sesso-vanilla-cosa-significa']),
 ('coppia-e-consenso','coppia','Coppia e consenso','#EEC6CC','#7A1E2B',
  'Chiedere, dire di no, capirsi. Anche questo è sesso.',
  'Il sesso è anche linguaggio. Chiedere quello che vuoi, dire di no, capire cosa vuol dire consenso: sono cose che si imparano, e che a volte fanno paura. Qui trovi da dove cominciare, anche quando le parole sembrano mancare.',
  ['come-parlare-di-sesso-con-il-partner','consenso-sessuale-cosa-vuol-dire-e-cosa-no','stealthing-preservativo-tolto-di-nascosto'],
  ['come-parlare-di-sesso-con-il-partner','consenso-sessuale-cosa-vuol-dire-e-cosa-no','stealthing-preservativo-tolto-di-nascosto']),
 ('difficolta-e-blocchi','difficolta','Difficoltà e blocchi','#C9D7E0','#35495A',
  'Succede a molte persone, e c’è sempre un punto da cui cominciare.',
  'L’ansia che blocca, l’erezione che se ne va, l’orgasmo che non arriva. Succede a tantissime persone, e quasi mai vuol dire che qualcosa si è rotto. Qui spiego perché succede e cosa si può fare; quando serve, ti dico anche a chi rivolgerti.',
  ['ansia-da-prestazione-sessuale','perdita-di-erezione-durante-il-rapporto','orgasmo-che-non-arriva-cause-e-cosa-fare'],
  ['ansia-da-prestazione-sessuale','perdita-di-erezione-durante-il-rapporto','orgasmo-che-non-arriva-cause-e-cosa-fare']),
]
sez = [dict(id=a, ico=b, name=c, bg=warm(d, .22 if b=='difficolta' else .2 if b=='desiderio' else .32 if b=='protezione' else .38), fg=e, tag=f, intro=g, picks=[by[x] for x in h],
            posts=sorted([by[x] for x in l], key=lambda p: p['iso'], reverse=True)) for a,b,c,d,e,f,g,h,l in SEZ]
assert sum(len(s['posts']) for s in sez) == len(items)
theme_of = {p['slug']: s for s in sez for p in s['posts']}
def href(s): return f'sezione-{s["id"]}.html'   # online diventerà /blog/{id}/

TOKENS = ':root{' + ''.join(f'--t-{s["ico"]}-bg:{s["bg"]};--t-{s["ico"]}-fg:{s["fg"]};' for s in sez) + '}\n' + \
         ''.join(f'.t-{s["ico"]}{{--bg:var(--t-{s["ico"]}-bg);--fg:var(--t-{s["ico"]}-fg)}}\n' for s in sez)

COMMON = TOKENS + ILL5_CSS + '''
html,body{overflow-x:clip}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
h1,h2,h3{text-wrap:balance} p{text-wrap:pretty}
.ico{width:22px;height:22px;flex:none;color:var(--fg)}
.lbl{font-size:14px;font-style:italic;color:var(--muted)}
:root{--muted:rgba(26,26,26,.7)}
@keyframes rise5{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:no-preference){.in{animation:rise5 380ms cubic-bezier(.2,.7,.2,1) var(--td,0ms) both}}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.draft{margin-top:14px;font-size:13px;font-style:italic;color:var(--muted);border-left:2px dashed var(--line);padding-left:10px}
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

# ══════════ HUB ══════════
cssH = '''
.hero5{padding:56px 0 32px}
.hero5 h1{font-family:var(--display);font-size:48px;line-height:.98;letter-spacing:-.035em;max-width:15ch}
.hero5 .intro{margin-top:22px;max-width:34em;font-size:19px;line-height:1.6;color:rgba(26,26,26,.85)}
.latest{border-block:1px solid var(--line);padding:18px 0;display:grid;gap:12px}
.latest h2{font-family:var(--body);font-weight:400}.latest ol{list-style:none;margin:0;padding:0;display:grid;gap:4px}
.latest a{display:grid;gap:2px;padding:8px 0}
.latest .t{font-family:var(--display);font-size:21px;line-height:1.15;transition:color .2s}
.latest a:hover .t{color:var(--burgundy)}
.themes{display:grid;gap:16px;padding:40px 0 24px}
.theme{position:relative;background:var(--bg);border:0;border-radius:14px;padding:22px 22px 18px;display:flex;flex-direction:column;gap:10px;transition:transform 300ms var(--ease),border-color 300ms}
.theme:hover{transform:translateY(-2px)}
.theme:active,.next:active{transform:translateY(-1px)}.theme:has(.lk:focus-visible){outline:2px solid var(--burgundy);outline-offset:3px}
.theme .all-t{position:relative;z-index:1;align-self:flex-start;margin-top:auto;padding:10px 0 2px;font-style:italic;color:var(--fg);text-decoration:underline;text-underline-offset:4px;text-decoration-color:color-mix(in srgb,var(--fg) 40%,transparent)}
.theme .all-t:focus-visible{outline:2px solid var(--burgundy);outline-offset:2px}
.theme .ill{width:92px;height:92px;margin:-2px 0 2px -6px}
.theme h2{font-family:var(--display);font-size:34px;line-height:1;letter-spacing:-.025em}
.theme h2 a{outline:none}
.theme h2 a::after{content:"";position:absolute;inset:0;border-radius:14px}
.theme .tag{font-size:17px;line-height:1.5;color:rgba(26,26,26,.82)}.th-protezione .tag{margin-top:10px}
.theme .lbl{margin-top:6px}
.theme ul{list-style:none;margin:8px 0 0;padding:0;position:relative;z-index:1}
.theme li a{display:block;padding:10px 0;border-top:1px solid color-mix(in srgb,var(--fg) 22%,transparent);font-size:15.5px;line-height:1.4;transition:color .2s}
.theme li a:hover{color:var(--fg);text-decoration:underline;text-underline-offset:3px}
.invite{background:var(--burgundy);color:var(--cream);border-radius:14px;padding:32px 26px;display:grid;gap:20px;margin:8px 0 56px;position:relative;overflow:hidden;isolation:isolate}
.invite p{font-family:var(--display);font-size:28px;line-height:1.1;letter-spacing:-.02em;max-width:30ch}
.invite .btn-cream{justify-self:start}
.chron h2{font-family:var(--display);font-size:32px;line-height:1;letter-spacing:-.02em}
.chron .intro2{margin-top:8px;color:var(--muted);font-style:italic}
.chron ol{list-style:none;margin:20px 0 96px;padding:0;border-top:1px solid var(--line)}
.chron li a{display:grid;grid-template-columns:1fr;gap:4px;padding:14px 0;border-bottom:1px solid var(--line-soft)}
.chron .t{font-size:18px;line-height:1.35;transition:color .2s}
.chron a:hover .t{color:var(--burgundy)}
.chron .m{display:flex;gap:8px;align-items:center;font-size:14px;color:var(--muted)}
.chron .m .ico{width:18px;height:18px}
@media(max-width:767px){
 .theme ul{display:none}.theme .ill{width:68px;height:68px}.th-protezione .ill{width:68px;height:68px}
 .theme{padding:18px 20px 14px;gap:6px}.theme h2,.th-protezione h2{font-size:30px}.theme .all-t{margin-top:4px}
}
@media(min-width:768px){
 .hero5{padding:96px 0 48px}.hero5 h1{font-size:84px}.hero5 .intro{font-size:21px}
 .latest{grid-template-columns:200px 1fr;align-items:start}.latest h2{font-family:var(--body);font-weight:400}.latest ol{grid-template-columns:repeat(3,1fr);gap:32px}
 .themes{grid-template-columns:repeat(6,1fr);grid-template-areas:"a a a a b b" "c c d d e e";gap:20px;padding:56px 0 28px}
 .th-protezione{grid-area:a}.th-piacere{grid-area:b}.th-desiderio{grid-area:c}.th-coppia{grid-area:d}.th-difficolta{grid-area:e}
 .th-protezione{display:grid;grid-template-columns:1fr 1fr;column-gap:32px;align-content:start}
 .th-protezione .ill{width:150px;height:150px}.th-protezione h2{font-size:56px}
 .th-protezione .col2{grid-column:2;grid-row:1/span 4;align-self:center;display:flex;flex-direction:column}
 .invite{grid-template-columns:1fr auto;align-items:center;padding:40px 44px}.invite p{font-size:40px}
 .chron li a{grid-template-columns:150px 1fr 220px;align-items:baseline;gap:24px}
 .chron .m.th{justify-content:flex-end}
}
'''
def theme_tile(s, k):
    picks = ''.join(f'<li><a href="/blog/{p["slug"]}.html">{p["title"]}</a></li>' for p in s['picks'])
    inner = f'''<ul>{picks}</ul><a class="all-t" href="{href(s)}">Tutti gli articoli del tema</a>'''
    if s['ico'] == 'protezione':
        return f'''<article class="theme th-{s["ico"]} t-{s["ico"]} live in" style="--td:{40+k*50}ms;--d:{200+k*150}ms">
<div>{ill5(s["ico"])}<h2><a class="lk" href="{href(s)}">{s["name"]}</a></h2><p class="tag">{s["tag"]}</p></div><div class="col2">{inner}</div></article>'''
    return f'''<article class="theme th-{s["ico"]} t-{s["ico"]} live in" style="--td:{40+k*50}ms;--d:{200+k*150}ms">
{ill5(s["ico"])}<h2><a class="lk" href="{href(s)}">{s["name"]}</a></h2><p class="tag">{s["tag"]}</p>{inner}</article>'''

latest = ''.join(f'<li><a href="/blog/{p["slug"]}.html"><span class="lbl">{p["date"]}</span><span class="t">{p["title"]}</span></a></li>' for p in items[:3])
chron = ''.join(f'''<li><a href="/blog/{p["slug"]}.html"><span class="m"><time datetime="{p["iso"]}">{p["date"]}</time></span><span class="t">{p["title"]}</span>
<span class="m th t-{theme_of[p["slug"]]["ico"]}">{small(theme_of[p["slug"]]["ico"])}{theme_of[p["slug"]]["name"]}</span></a></li>''' for p in items)
bodyH = f'''<section class="hero5"><div class="wrap">
<h1>Sessualità, senza giri di <span class="stamp">parole.</span></h1>
<p class="intro">Le domande che si fanno a bassa voce, con risposte scritte in chiaro. Gli articoli sono divisi in cinque temi: parti da quello che ti riguarda, oppure leggili dal più recente.</p></div></section>
<div class="wrap">
<section class="themes" aria-label="Temi">{"".join(theme_tile(s,k) for k,s in enumerate(sez))}</section>
<aside class="invite"><p>Non c’è un livello minimo di disagio per meritarsi un’ora di chiarezza.</p><a class="btn-cream" href="/#contatti">Scrivimi</a></aside>
<section class="chron" aria-labelledby="tutti"><h2 id="tutti">Tutti gli articoli</h2><p class="intro2">Dal più recente.</p><ol>{chron}</ol></section>
</div>'''
(OUT/'blog.html').write_text(page('Blog di sessuologia, per temi — Alessio Cottonaro',
    'Desiderio, piacere, protezione, coppia e difficoltà: gli articoli di Alessio Cottonaro, consulente in sessuologia a Torino, divisi in cinque temi.', bodyH, cssH))

# ══════════ SEZIONE ══════════
cssS = '''
.sec-hero{background:var(--bg)}
.sec-hero .wrap{padding-top:20px;padding-bottom:32px;display:grid;gap:6px}
.sec-hero .crumb{padding-top:0;font-size:15px}
.sec-hero .crumb a{display:inline-block;padding:10px 0;border:0;color:var(--fg);text-decoration:underline;text-underline-offset:4px;text-decoration-color:color-mix(in srgb,var(--fg) 45%,transparent)}
.sec-hero .ill{width:72px;height:72px;margin:4px 0 0 -6px}
.sec-hero h1{font-family:var(--display);font-size:48px;line-height:.95;letter-spacing:-.035em}
.sec-hero .lead{margin-top:14px;font-size:19px;line-height:1.6;max-width:36em;color:rgba(26,26,26,.86)}
.book{display:grid;padding-bottom:24px}
.toc-side{display:none}
.toc-mob{display:flex;flex-wrap:wrap;gap:6px;padding:0 0 64px}
.toc-mob a{display:inline-flex;gap:6px;align-items:center;border-radius:999px;min-height:44px;padding:8px 12px 8px 8px;font-size:14px;background:color-mix(in srgb,var(--bg) 60%,transparent)}
.toc-mob a[aria-current]{background:var(--bg);box-shadow:inset 0 0 0 1px var(--fg)}
.idx{list-style:none;margin:0;padding:12px 0 0}
.idx li{position:relative;display:grid;gap:4px;padding:18px 0;border-bottom:1px solid var(--line-soft)}
.idx a.t::after{content:"";position:absolute;inset:0}
.idx a.t:focus-visible{outline:none}.idx li:has(a.t:focus-visible){outline:2px solid var(--burgundy);outline-offset:4px;border-radius:4px}
.idx .row{display:flex;align-items:baseline;gap:12px}
.idx .t{font-size:20px;line-height:1.35;transition:color .2s}
.idx .dots{flex:1;border-bottom:1px dotted color-mix(in srgb,var(--fg) 60%,transparent);transform:translateY(-5px);min-width:24px}
.idx .m{font-size:14px;color:var(--muted);white-space:nowrap;font-style:italic}
.idx .x{font-size:16px;line-height:1.55;font-style:italic;color:rgba(26,26,26,.7);max-width:40em}
.idx li:hover a.t{color:var(--fg)}
.close{background:var(--burgundy);color:var(--cream);border-radius:14px;padding:28px 26px;margin:48px 0 20px;display:grid;gap:18px}
.close p{font-family:var(--display);font-size:26px;line-height:1.1;max-width:30ch}
.close .btn-cream{justify-self:start}
.next{display:flex;align-items:center;justify-content:space-between;gap:16px;margin:0 0 40px;background:var(--bg);border:0;border-radius:14px;padding:18px 22px;transition:transform .3s var(--ease),border-color .3s}
.next:hover{transform:translateY(-3px);border-color:color-mix(in srgb,var(--fg) 55%,transparent)}
.next:focus-visible{outline:2px solid var(--burgundy);outline-offset:3px}
.next b{display:block;font-weight:400;font-family:var(--display);font-size:32px;line-height:1;margin-top:6px}
.next .ill{width:76px;height:76px;flex:none}
@media(min-width:900px){
 .toc-mob{display:none}
 .sec-hero .wrap{grid-template-columns:1fr 240px;column-gap:48px;padding-top:44px;padding-bottom:60px}
 .sec-hero .wrap>*{grid-column:1}.sec-hero .ill{grid-column:2;grid-row:1/6;width:230px;height:230px;margin:0;justify-self:end;align-self:center}
 .sec-hero h1{font-size:84px}
 .book{grid-template-columns:250px 1fr;gap:64px}.next{margin-bottom:96px}
 .toc-side{display:block;position:sticky;top:110px;align-self:start;padding-top:36px}
 .toc-side ol{list-style:none;margin:12px 0 0;padding:0}
 .toc-side a{display:flex;gap:12px;align-items:center;padding:10px;border-radius:10px;margin-left:-10px;transition:background .2s}
 .toc-side a:hover{background:color-mix(in srgb,var(--bg) 60%,transparent)}
 .toc-side a[aria-current]{background:var(--bg)}
 .toc-side .all{display:inline-block;margin-top:14px;padding:8px 0;font-style:italic;color:var(--burgundy)}
 .idx .t{font-size:22px}
 .close{grid-template-columns:1fr auto;align-items:center;padding:32px 36px}
}
'''
for i, s in enumerate(sez):
    nx = sez[(i+1) % len(sez)]
    side = '<nav class="toc-side" aria-label="Temi del blog"><p class="lbl">Temi del blog</p><ol>' + ''.join(
        f'<li><a href="{href(o)}" class="t-{o["ico"]}"{" aria-current=page" if o is s else ""}>{small(o["ico"])}{o["name"]}</a></li>' for o in sez) + \
        '</ol><a class="all" href="blog.html">Tutti gli articoli</a></nav>'
    mob = '<nav class="toc-mob" aria-label="Altri temi"><p class="lbl" style="width:100%">Altri temi</p>' + ''.join(
        f'<a href="{href(o)}" class="t-{o["ico"]}"{" aria-current=page" if o is s else ""}>{small(o["ico"])}{o["name"]}</a>' for o in sez) + '</nav>'
    lis = ''.join(f'''<li><span class="row"><a class="t" href="/blog/{p["slug"]}.html">{p["title"]}</a><span class="dots" aria-hidden="true"></span><span class="m">{p["min"]} min</span></span>
<span class="x">{p["exc"]}</span><span class="lbl"><time datetime="{p["iso"]}">{p["date"]}</time></span></li>''' for p in s['posts'])
    body = f'''<section class="sec-hero t-{s["ico"]} live" style="--d:100ms"><div class="wrap">
<p class="crumb"><a href="blog.html">Blog</a> <span aria-hidden="true">/</span> <span aria-current="page">{s["name"]}</span></p>{ill5(s["ico"])}
<h1>{s["name"]}</h1><p class="lead">{s["intro"]}</p><p class="draft">Testo di prova: da rivedere con Alessio.</p></div></section>
<div class="wrap t-{s["ico"]}"><div class="book">{side}<div><h2 class="sr">Articoli</h2><ol class="idx">{lis}</ol>
<aside class="close"><p>Non serve la parola giusta. Scrivimi come viene.</p><a class="btn-cream" href="/#contatti">Scrivimi</a></aside>
<a class="next live t-{nx["ico"]}" href="{href(nx)}" style="--d:400ms"><span><span class="lbl">Prossimo tema</span><b>{nx["name"]}</b></span>{ill5(nx["ico"])}</a>{mob}</div></div></div>'''
    (OUT/f'sezione-{s["id"]}.html').write_text(page(f'{s["name"]}: articoli — Alessio Cottonaro', s['tag'], body, cssS))

# ══════════ TAVOLA ICONE ══════════
cssI = '''.sheet{display:grid;gap:18px;padding:40px 0 96px}.plate{background:var(--bg);border-radius:16px;padding:24px;display:grid;gap:12px;justify-items:center;text-align:center;border:1px solid color-mix(in srgb,var(--fg) 22%,transparent)}
.plate .ill{width:200px;height:200px}.plate h2{font-family:var(--display);font-size:28px;line-height:1}.plate .lbl{max-width:24em}
@media(min-width:768px){.sheet{grid-template-columns:repeat(3,1fr);gap:24px}}'''
plates = ''.join(f'<article class="plate live t-{s["ico"]}" tabindex="0" style="--d:{k*200}ms">{ill5(s["ico"])}<h2>{s["name"]}</h2><p class="lbl">Passa sopra o tocca per vederla muoversi.</p></article>' for k,s in enumerate(sez))
(OUT/'icone.html').write_text(page('Icone dei temi', 'Tavola delle icone dei cinque temi.', f'<div class="wrap"><h1 style="font-family:var(--display);font-size:56px;line-height:1;padding:64px 0 8px">Icone dei temi</h1><div class="sheet">{plates}</div></div>', cssI))

# ══════════ ARTICOLO (testa e coda) ══════════
art = (SITE/'blog/sesso-vanilla-cosa-significa.html').read_text()
s = theme_of['sesso-vanilla-cosa-significa']
art = art.replace('<p class="crumb"><a href="/blog/">Blog</a> <span aria-hidden="true">/</span></p>',
  f'<p class="crumb"><a href="blog.html">Blog</a> <span aria-hidden="true">/</span> <a class="tchip t-{s["ico"]}" href="{href(s)}">{s["name"]}</a></p>')
others = ''.join(f'<li><a href="/blog/{p["slug"]}.html">{p["title"]}</a></li>' for p in s['posts'] if p['slug']!='sesso-vanilla-cosa-significa')
art = art.replace('<a class="back-link" href="/blog/">← Tutti gli articoli</a>',
  f'''<section class="more t-{s["ico"]}"><p class="lbl">Altri articoli su {s["name"]}</p><ul>{others}</ul><a href="{href(s)}">Tutto il tema {s["name"]}</a></section>
    <a class="back-link" href="blog.html">← Tutti gli articoli</a>''')
art = art.replace('</head>', '''<style>.more{margin-top:56px;padding:22px 24px;border-radius:14px;background:var(--bg)}
.more ul{list-style:none;margin:10px 0 12px;padding:0}.more li a{display:block;padding:10px 0;border-top:1px solid color-mix(in srgb,var(--fg) 22%,transparent);font-size:18px}
.prose a{overflow-wrap:anywhere}
.crumb .tchip{display:inline-block;background:var(--bg);color:var(--fg);border:0;border-radius:999px;padding:4px 12px;margin-left:2px}
.more>a{font-style:italic;color:var(--fg);display:inline-block;padding:8px 0}.lbl{font-size:14px;font-style:italic;color:rgba(26,26,26,.7)}
'''+TOKENS+'''</style><meta name="robots" content="noindex"></head>''')
(OUT/'articolo-esempio.html').write_text(art)
print('ok', len(items), [len(s['posts']) for s in sez], [s['bg'] for s in sez])
