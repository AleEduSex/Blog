"""Icone v5: entrata una volta sola (disegno), vita solo su .live:hover / .live:focus-within.
Regola: un elemento = al massimo un'animazione. Entrata sugli elementi esterni, movimento continuo su <g class="lp-…"> interni.
Solo transform/opacity nei movimenti continui (niente stroke-dashoffset infinito)."""

ILL5 = {
'protezione': '''
<path class="dr d1" pathLength="1" d="M32 6 52 13v16c0 13-8.5 23-20 29-11.5-6-20-16-20-29V13z"/>
<path class="f f1 dash" d="M32 11.5 47 17v12.5c0 10-6.2 17.9-15 22.9-8.8-5-15-12.9-15-22.9V17z"/>
<g class="lp-beat"><path class="dr d2 fillsoft" pathLength="1" d="M32 41s-9-5.5-9-11.7c0-3.1 2.4-5.3 5.1-5.3 1.8 0 3.2 1 3.9 2.4.7-1.4 2.1-2.4 3.9-2.4 2.7 0 5.1 2.2 5.1 5.3C41 35.5 32 41 32 41z"/></g>
''',
'piacere': '''
<g class="lp-wave a"><path class="dr d1" pathLength="1" d="M13 51.5c3-2 6-2 9.5 0s6.5 2 9.5 0 6-2 9.5 0 6.5 2 9.5 0"/></g>
<g class="lp-wave b"><path class="dr d1" pathLength="1" d="M19.4 57c2.6-1.8 5.4-1.8 8.4 0s5.4 1.8 8.4 0 5.4-1.8 8.4 0"/></g>
<g class="lp-fla"><path class="dr d2 fillsoft" pathLength="1" d="M32 46c-8.5 0-14-6-14-13.5 0-6 3.2-10.1 6.4-13.1-.2 4 1.4 6.8 4 7.8-1-7.6 2-15.6 8-21.8-.8 6 2.2 10.4 5.6 14.8 2.6 3.4 4 7.4 4 12.3C46 40 40.5 46 32 46z"/></g>
<g class="lp-flb"><path class="dr d3" pathLength="1" d="M32 46c-5 0-8.2-3.6-8.2-8.2 0-4.2 2.6-6.8 5.2-9.2.4 3 2 4.8 4.2 5-.6-4.6 1.4-9 4.6-12 .2 4.4 2.4 7 2.4 12.2 0 7.2-3.6 12.2-8.2 12.2z"/></g>
<g class="lp-core"><path class="pop p1 fillcore" d="M32 46c-2.6 0-4.2-2-4.2-4.4 0-2.6 1.8-4.2 3.6-5.8.2 2 1.6 3 2.8 3.2 1.2 1 2 2 2 3 0 2.4-1.8 4-4.2 4z"/></g>
<g class="f f3"><g class="lp-spark a"><circle class="dotf" cx="41" cy="5" r="1.1"/></g><g class="lp-spark b"><circle class="dotf" cx="26" cy="8" r=".9"/></g><g class="lp-spark c"><circle class="dotf" cx="55" cy="22" r=".8"/></g><g class="lp-spark d"><circle class="dotf" cx="9" cy="24" r=".8"/></g></g>
''',
'desiderio': '''
<g class="lp-tilt">
 <g class="f f4"><g class="lp-plume">
  <path class="fillsoft" d="M50.6 19.2c-1.8-7.4.4-13.8 6.4-17.2 1.8 6.6-.2 13-6.4 17.2z"/>
  <path d="M50.6 19.2C52.4 13.4 54.4 7.6 57 2"/>
  <path class="fillsoft" d="M47.4 19.4c-2.8-5-2.4-9.8.8-13.4 1.6 4.4 1.2 9-.8 13.4z"/>
  <path d="M53.4 12.6l2.6-1.2M52.2 16.2l2.8-.6M54.6 8.6l2-1.6"/>
 </g></g>
 <path class="dr d1 fillsoft" pathLength="1" d="M32 22.5C27 18.5 18 17 10.5 19.5 7.5 20.5 5.2 22 4 24.2c1.4 7.3 6.2 13.8 13.5 15.4 5.5 1.2 10.1-2 12.7-5.2.8-1 1.3-1.4 1.8-1.4s1 .4 1.8 1.4c2.6 3.2 7.2 6.4 12.7 5.2 7.3-1.6 12.1-8.1 13.5-15.4-1.2-2.2-3.5-3.7-6.5-4.7C46 17 37 18.5 32 22.5z"/>
 <path class="f f1 dash" d="M9 23.2c6.4-2.4 14.6-1.6 20.6 2.4M55 23.2c-6.4-2.4-14.6-1.6-20.6 2.4"/>
 <path class="dr d2 bgfill" pathLength="1" d="M12.5 28.6c3.1-3.6 9.1-4 13.1.4-3.2 3.4-9.2 3.8-13.1-.4z"/>
 <path class="dr d2 bgfill" pathLength="1" d="M51.5 28.6c-3.1-3.6-9.1-4-13.1.4 3.2 3.4 9.2 3.8 13.1-.4z"/>
 <g class="f f2">PEARLS</g>
 <g class="pop p1"><g class="lp-gem"><path class="fillfg" d="M32 16.2l2.1 3.3-2.1 3.3-2.1-3.3z"/></g></g>
 <path class="dr d3" pathLength="1" d="M57.6 31.4c1.2 8.6 1.8 17.6 2 27.6"/>
 <g class="lp-ribbon"><path class="dr d4" pathLength="1" d="M58.8 45.2c-2-2.4-4.6-2.2-4.6-.3s2.6 2.2 4.6.3zM58.8 45.2c2-2.4 4.4-2.2 4.4-.3s-2.4 2.2-4.4.3z"/><path class="dr d4" pathLength="1" d="M58.4 45.6l-2.2 5.4M59.2 45.6l2 5.6"/></g>
</g>
''',
'coppia': '''
<path class="dr d1 fillsoft" pathLength="1" d="M10 9h26a5 5 0 0 1 5 5v14a5 5 0 0 1-5 5H21l-8 7v-7h-3a5 5 0 0 1-5-5V14a5 5 0 0 1 5-5z"/>
<g class="f f2"><g class="lp-type a"><circle class="dotf" cx="15" cy="21" r="1.9"/></g><g class="lp-type b"><circle class="dotf" cx="23" cy="21" r="1.9"/></g><g class="lp-type c"><circle class="dotf" cx="31" cy="21" r="1.9"/></g></g>
<g class="reply"><g class="lp-reply"><path class="bgfill" d="M28 29h26a5 5 0 0 1 5 5v12a5 5 0 0 1-5 5h-3v7l-8-7H28a5 5 0 0 1-5-5V34a5 5 0 0 1 5-5z"/>
<text x="41" y="45.5" class="si">sì</text></g></g>
''',
'difficolta': '''
<g class="l-sh"><g class="lp-sh">
 <path class="dr d2" pathLength="1" d="M17.5 30V19.5a12.5 12.5 0 0 1 25 0V30"/>
 <path class="dr d2" pathLength="1" d="M22 30V19.5a8 8 0 0 1 16 0V30"/>
</g></g>
<path class="dr d1 fillsoft" pathLength="1" d="M15 30h30a4.5 4.5 0 0 1 4.5 4.5V53a6 6 0 0 1-6 6h-27a6 6 0 0 1-6-6V34.5A4.5 4.5 0 0 1 15 30z"/>
<path class="f f1" d="M11 36h38" style="opacity:.45"/>
<g class="lp-glow"><circle cx="30" cy="45" r="5.5" class="glow"/></g>
<g class="f f2"><circle class="dotf" cx="15" cy="54.4" r=".9"/><circle class="dotf" cx="45" cy="54.4" r=".9"/></g>
<g class="pop p1"><circle class="dotf" cx="30" cy="43.4" r="3.2"/><path class="fillfg" d="M28.5 45.4h3l.7 5.4h-4.4z"/></g>
<g class="l-key"><g class="lp-key">
 <circle cx="57" cy="34.6" r="4.4" class="bgfill"/><circle cx="57" cy="34.6" r="1.4"/>
 <path d="M54.6 39.6h4.8M57 39.6V56M57 49.4h-3.2v2.4h1.6v1.8H57"/>
</g></g>
''',
}
_pearls = [(13.4,35.4),(18,37.4),(22.8,36.8),(41.2,36.8),(46,37.4),(50.6,35.4)]
ILL5['desiderio'] = ILL5['desiderio'].replace('PEARLS', ''.join(
    f'<g class="lp-shine s{i+1}"><circle class="dotf" cx="{x}" cy="{y}" r=".95"/></g>' for i,(x,y) in enumerate(_pearls)))

def ill5(key, cls=''):
    return f'<svg class="ill ill-{key} {cls}" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ILL5[key]}</svg>'

KEY_T = "translate(-27px,-11.6px) rotate(90deg) scale(-.58,.58)"      # chiave infilata e girata
SH_OPEN = "translateY(-6px) rotate(-26deg)"                             # arco aperto

LIVE = '.live:is(:hover,:focus-visible,:has(.lk:focus-visible))'

ILL5_CSS = f'''
.ill{{color:var(--fg);overflow:visible}}
.ill *{{transform-box:fill-box;transform-origin:center}}
.ill .dash{{stroke-dasharray:2 3;opacity:.55}}
.ill .dotf,.ill .fillfg{{fill:currentColor;stroke:none}}
.ill .fillsoft{{fill:color-mix(in srgb,var(--fg) 12%,transparent)}}
.ill .fillcore{{fill:color-mix(in srgb,var(--fg) 45%,transparent);stroke:none}}
.ill .bgfill{{fill:var(--bg);stroke:currentColor}}
.ill .si{{font-family:var(--display);font-style:italic;font-size:15px;fill:currentColor;stroke:none;text-anchor:middle}}
.ill .glow{{fill:color-mix(in srgb,var(--fg) 22%,transparent);stroke:none;opacity:0}}
.ill .dr{{stroke-dasharray:1;stroke-dashoffset:0}}
/* posa finale (anche per chi ha «riduci movimento»): lucchetto aperto, chiave infilata */
.ill-difficolta .l-sh{{transform-box:view-box;transform-origin:17.5px 30px;transform:{SH_OPEN}}}
.ill-difficolta .lp-sh{{transform-box:view-box;transform-origin:17.5px 30px}}
.ill-difficolta .l-key{{transform-origin:50% 100%;transform:{KEY_T}}}

@keyframes ill-draw{{from{{stroke-dashoffset:1;stroke-opacity:0}}7%{{stroke-opacity:1}}to{{stroke-dashoffset:0;stroke-opacity:1}}}}
@keyframes ill-fillin{{from{{fill-opacity:0}}to{{fill-opacity:1}}}}
@keyframes ill-fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes ill-pop{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes ill-reply{{0%{{opacity:0;transform:translate(4px,8px) scale(.7)}}70%{{opacity:1;transform:translate(0,-1px) scale(1.03)}}100%{{opacity:1;transform:none}}}}
@keyframes l-keyin{{0%{{transform:translate(0,0) rotate(0deg) scale(1,1)}}
 35%{{transform:translate(-8px,-11px) rotate(34deg) scale(.88,.88)}}
 68%{{transform:translate(-20px,-14px) rotate(72deg) scale(.72,.72)}}
 86%{{transform:translate(-27px,-11.6px) rotate(90deg) scale(.58,.58);animation-timing-function:cubic-bezier(.6,0,.4,1)}}
 100%{{transform:{KEY_T}}}}}
@keyframes l-shopen{{0%{{transform:none}}62%{{transform:translateY(-7.4px) rotate(-29deg)}}82%{{transform:translateY(-5.6px) rotate(-24.5deg)}}100%{{transform:{SH_OPEN}}}}}
@keyframes l-raysin{{0%{{opacity:0;transform:scale(.4)}}60%{{opacity:1;transform:scale(1.12)}}100%{{opacity:1;transform:none}}}}
/* vita (solo al passaggio): partono tutte dalla posa di riposo e ci tornano */
@keyframes lp-beat{{0%,46%,100%{{transform:scale(1)}}8%{{transform:scale(1.14)}}16%{{transform:scale(.98)}}24%{{transform:scale(1.09)}}34%{{transform:scale(1)}}}}
@keyframes lp-tw{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:.3;transform:scale(.55)}}}}
@keyframes lp-fla{{0%,100%{{transform:none}}30%{{transform:scaleY(1.045) skewX(-1.8deg)}}60%{{transform:scaleY(.975) skewX(1.4deg)}}82%{{transform:scaleY(1.02) skewX(-.5deg)}}}}
@keyframes lp-flb{{0%,100%{{transform:none}}35%{{transform:scaleY(.95) skewX(2.2deg)}}70%{{transform:scaleY(1.06) skewX(-1.6deg)}}}}
@keyframes lp-core{{0%,100%{{transform:scale(1);opacity:1}}50%{{transform:scale(1.12);opacity:.8}}}}
@keyframes lp-halo{{0%,100%{{transform:rotate(0)}}50%{{transform:rotate(7deg)}}}}
@keyframes lp-wave{{0%,100%{{transform:translateX(0)}}50%{{transform:translateX(-2.5px)}}}}
@keyframes lp-spark{{0%{{opacity:1;transform:translateY(0)}}70%{{opacity:0;transform:translateY(-12px)}}71%{{opacity:0;transform:translateY(4px)}}100%{{opacity:1;transform:translateY(0)}}}}
@keyframes lp-tilt{{0%,100%{{transform:rotate(0)}}25%{{transform:rotate(-2.5deg)}}75%{{transform:rotate(2deg)}}}}
@keyframes lp-plume{{0%,100%{{transform:rotate(0)}}50%{{transform:rotate(-8deg)}}}}
@keyframes lp-ribbon{{0%,100%{{transform:rotate(0)}}50%{{transform:rotate(10deg)}}}}
@keyframes lp-shine{{0%,22%,100%{{transform:scale(1)}}8%{{transform:scale(1.65)}}}}
@keyframes lp-gem{{0%,60%{{transform:scale(1) rotate(0)}}75%{{transform:scale(1.3) rotate(90deg)}}90%,100%{{transform:scale(1) rotate(180deg)}}}}
@keyframes lp-type{{0%,60%,100%{{transform:translateY(0)}}30%{{transform:translateY(-3.5px)}}}}
@keyframes lp-reply{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.03)}}}}
@keyframes lp-sh{{0%,12%{{transform:none}}34%{{transform:rotate(27deg) translateY(6.6px)}}44%,56%{{transform:rotate(26deg) translateY(6px)}}74%{{transform:rotate(-2deg) translateY(-.8px)}}84%,100%{{transform:none}}}}
@keyframes lp-key{{0%,30%,100%{{transform:scaleX(1)}}45%,70%{{transform:scaleX(-1)}}}}
@keyframes lp-glow{{0%,60%,100%{{opacity:0;transform:scale(.6)}}78%,90%{{opacity:.75;transform:scale(1.2)}}}}
@keyframes lp-rays{{0%,62%,100%{{opacity:1;transform:scale(1)}}40%,56%{{opacity:0;transform:scale(.7)}}74%{{opacity:1;transform:scale(1.15)}}}}

@media (prefers-reduced-motion:no-preference){{
 /* entrata: una volta sola, tutto finito entro ~4,5 s */
 .ill .d1{{animation:ill-draw 1300ms cubic-bezier(.42,0,.18,1) calc(var(--d,0ms) + 200ms) both}}
 .ill .d2{{animation:ill-draw 1000ms cubic-bezier(.42,0,.18,1) calc(var(--d,0ms) + 900ms) both}}
 .ill .d3{{animation:ill-draw 900ms cubic-bezier(.42,0,.18,1) calc(var(--d,0ms) + 1300ms) both}}
 .ill .d4{{animation:ill-draw 800ms cubic-bezier(.42,0,.18,1) calc(var(--d,0ms) + 1700ms) both}}
 .ill .dr.d1.fillsoft{{animation:ill-draw 1300ms cubic-bezier(.42,0,.18,1) calc(var(--d,0ms) + 200ms) both,ill-fillin 700ms ease calc(var(--d,0ms) + 1200ms) both}}
 .ill .dr.d2.fillsoft{{animation:ill-draw 1000ms cubic-bezier(.42,0,.18,1) calc(var(--d,0ms) + 900ms) both,ill-fillin 700ms ease calc(var(--d,0ms) + 1700ms) both}}
 .ill .f1{{animation:ill-fade 900ms ease calc(var(--d,0ms) + 1000ms) both}}
 .ill .f2{{animation:ill-fade 900ms ease calc(var(--d,0ms) + 1500ms) both}}
 .ill .f3{{animation:ill-fade 900ms ease calc(var(--d,0ms) + 1900ms) both}}
 .ill .f4{{animation:ill-fade 700ms ease calc(var(--d,0ms) + 1700ms) both}}
 .ill .p1{{animation:ill-pop 700ms var(--ease) calc(var(--d,0ms) + 1700ms) both}}
 .ill .p3{{animation:ill-pop 700ms var(--ease) calc(var(--d,0ms) + 2300ms) both}}
 .ill .p4{{animation:ill-pop 700ms var(--ease) calc(var(--d,0ms) + 3100ms) both}}
 .ill-coppia .reply{{transform-origin:75% 100%;animation:ill-reply 800ms var(--ease) calc(var(--d,0ms) + 2500ms) both}}
 .ill-difficolta .l-key{{animation:l-keyin 1700ms cubic-bezier(.45,0,.3,1) calc(var(--d,0ms) + 1500ms) both}}
 .ill-difficolta .l-sh{{animation:l-shopen 900ms cubic-bezier(.45,0,.3,1) calc(var(--d,0ms) + 3200ms) both}}
 .ill-difficolta .l-rays{{animation:l-raysin 600ms var(--ease) calc(var(--d,0ms) + 3500ms) both}}

 /* vita: solo con il puntatore sopra o il fuoco dentro il contenitore .live */
 {LIVE} .lp-beat{{animation:lp-beat 2.6s ease-in-out infinite}}
 {LIVE} .lp-tw.a{{animation:lp-tw 2.6s ease-in-out infinite}}
 {LIVE} .lp-tw.b{{animation:lp-tw 3.1s ease-in-out .4s infinite}}
 {LIVE} .lp-tw.c{{animation:lp-tw 2.2s ease-in-out .8s infinite}}
 {LIVE} .lp-fla{{transform-origin:50% 100%;animation:lp-fla 2.6s ease-in-out infinite}}
 {LIVE} .lp-flb{{transform-origin:50% 100%;animation:lp-flb 1.9s ease-in-out infinite}}
 {LIVE} .lp-core{{transform-origin:50% 100%;animation:lp-core 1.6s ease-in-out infinite}}
 {LIVE} .lp-halo{{animation:lp-halo 4s ease-in-out infinite}}
 {LIVE} .lp-wave.a{{animation:lp-wave 3.2s ease-in-out infinite}}
 {LIVE} .lp-wave.b{{animation:lp-wave 3.2s ease-in-out -1.6s infinite}}
 {LIVE} .lp-spark{{animation:lp-spark 2.4s ease-out infinite}}
 {LIVE} .lp-spark.b{{animation-delay:-.6s}} {LIVE} .lp-spark.c{{animation-delay:-1.2s}} {LIVE} .lp-spark.d{{animation-delay:-1.8s}}
 {LIVE} .lp-tilt{{transform-origin:90% 100%;animation:lp-tilt 5s ease-in-out infinite}}
 {LIVE} .lp-plume{{transform-origin:10% 100%;animation:lp-plume 3.4s ease-in-out infinite}}
 {LIVE} .lp-ribbon{{transform-origin:50% 0%;animation:lp-ribbon 2.8s ease-in-out infinite}}
 {LIVE} .lp-shine{{animation:lp-shine 3.2s ease-in-out infinite}}
 ''' + ''.join(f"{LIVE} .lp-shine.s{i+1}{{animation-delay:{i*0.16:.2f}s}} " for i in range(6)) + f'''
 {LIVE} .lp-gem{{animation:lp-gem 3.2s ease-in-out .9s infinite}}
 {LIVE} .lp-type{{animation:lp-type 1.2s ease-in-out infinite}}
 {LIVE} .lp-type.b{{animation-delay:.15s}} {LIVE} .lp-type.c{{animation-delay:.3s}}
 {LIVE} .lp-reply{{transform-origin:75% 100%;animation:lp-reply 3s ease-in-out infinite}}
 {LIVE} .lp-sh{{animation:lp-sh 3.4s cubic-bezier(.45,0,.3,1) infinite}}
 {LIVE} .lp-key{{animation:lp-key 3.4s cubic-bezier(.45,0,.3,1) infinite}}
 {LIVE} .lp-glow{{animation:lp-glow 3.4s cubic-bezier(.45,0,.3,1) infinite}}
 {LIVE} .lp-rays{{animation:lp-rays 3.4s cubic-bezier(.45,0,.3,1) infinite}}
}}
'''
