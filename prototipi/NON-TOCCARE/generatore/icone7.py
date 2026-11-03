"""Icone v7 (sezioni di Alessio): entrata una volta sola (disegno), vita solo su .live:hover / .live:focus-within.
Regola: un elemento = al massimo un'animazione. Entrata sugli elementi esterni, movimento continuo su <g class="lp-…"> interni.
Solo transform/opacity nei movimenti continui (niente stroke-dashoffset infinito)."""

ILL7 = {
'prevenzione': '''
<path class="dr d1" pathLength="1" d="M32 6 52 13v16c0 13-8.5 23-20 29-11.5-6-20-16-20-29V13z"/>
<path class="f f1 dash" d="M32 11.5 47 17v12.5c0 10-6.2 17.9-15 22.9-8.8-5-15-12.9-15-22.9V17z"/>
<g class="lp-beat"><path class="dr d2 fillsoft" pathLength="1" d="M32 41s-9-5.5-9-11.7c0-3.1 2.4-5.3 5.1-5.3 1.8 0 3.2 1 3.9 2.4.7-1.4 2.1-2.4 3.9-2.4 2.7 0 5.1 2.2 5.1 5.3C41 35.5 32 41 32 41z"/></g>
''',
'corpo': '''
<g class="lp-wave a"><path class="dr d1" pathLength="1" d="M13 51.5c3-2 6-2 9.5 0s6.5 2 9.5 0 6-2 9.5 0 6.5 2 9.5 0"/></g>
<g class="lp-wave b"><path class="dr d1" pathLength="1" d="M19.4 57c2.6-1.8 5.4-1.8 8.4 0s5.4 1.8 8.4 0 5.4-1.8 8.4 0"/></g>
<g class="lp-fla"><path class="dr d2 fillsoft" pathLength="1" d="M32 46c-8.5 0-14-6-14-13.5 0-6 3.2-10.1 6.4-13.1-.2 4 1.4 6.8 4 7.8-1-7.6 2-15.6 8-21.8-.8 6 2.2 10.4 5.6 14.8 2.6 3.4 4 7.4 4 12.3C46 40 40.5 46 32 46z"/></g>
<g class="lp-flb"><path class="dr d3" pathLength="1" d="M32 46c-5 0-8.2-3.6-8.2-8.2 0-4.2 2.6-6.8 5.2-9.2.4 3 2 4.8 4.2 5-.6-4.6 1.4-9 4.6-12 .2 4.4 2.4 7 2.4 12.2 0 7.2-3.6 12.2-8.2 12.2z"/></g>
<g class="lp-core"><path class="pop p1 fillcore" d="M32 46c-2.6 0-4.2-2-4.2-4.4 0-2.6 1.8-4.2 3.6-5.8.2 2 1.6 3 2.8 3.2 1.2 1 2 2 2 3 0 2.4-1.8 4-4.2 4z"/></g>
<g class="f f3"><g class="lp-spark a"><circle class="dotf" cx="41" cy="5" r="1.1"/></g><g class="lp-spark b"><circle class="dotf" cx="26" cy="8" r=".9"/></g><g class="lp-spark c"><circle class="dotf" cx="55" cy="22" r=".8"/></g><g class="lp-spark d"><circle class="dotf" cx="9" cy="24" r=".8"/></g></g>
''',

'comunicazione': '''
<path class="dr d1 fillsoft" pathLength="1" d="M10 9h26a5 5 0 0 1 5 5v14a5 5 0 0 1-5 5H21l-8 7v-7h-3a5 5 0 0 1-5-5V14a5 5 0 0 1 5-5z"/>
<g class="f f2"><g class="lp-type a"><circle class="dotf" cx="15" cy="21" r="1.9"/></g><g class="lp-type b"><circle class="dotf" cx="23" cy="21" r="1.9"/></g><g class="lp-type c"><circle class="dotf" cx="31" cy="21" r="1.9"/></g></g>
<g class="reply"><g class="lp-reply"><path class="bgfill" d="M28 29h26a5 5 0 0 1 5 5v12a5 5 0 0 1-5 5h-3v7l-8-7H28a5 5 0 0 1-5-5V34a5 5 0 0 1 5-5z"/>
<text x="41" y="45.5" class="si">sì</text></g></g>
''',
'difficolta': '''
<path class="f f1 dash" d="M3 58.5h58"/>
<path class="dr d1 fillsoft" pathLength="1" d="M8 54.5c0-10 6-17.5 16-19.5 6-1.2 10.5 1.5 15 0 8.5-2.8 16.5 3.6 16.5 13.5 0 3.5-2 6-5.5 6z"/>
<path class="dr d2" pathLength="1" d="M31.5 35.4l2.3 6.2-3.4 4.6 2.2 8.2"/>
<path class="dr d3" pathLength="1" d="M31.5 35.4c0-6.6 1-13 3.2-19"/>
<g class="g-leaf l"><g class="lp-leaf l"><path class="fillleaf" d="M32.6 23.5c-6.4.2-10.6-3.8-11.6-9.4 6-.2 10.6 3.4 11.6 9.4z"/></g></g>
<g class="g-leaf r"><g class="lp-leaf r"><path class="fillleaf" d="M34 18.5c3.6-5.4 9.6-7.2 14.6-5.2-2.2 5.2-8.6 7.6-14.6 5.2z"/></g></g>
''',
'approfondimenti': '''
<path class="dr d1 fillsoft" pathLength="1" d="M32 50C26 46 16 45 8 46.5V16c8-1.5 18-.5 24 3.5z"/>
<path class="dr d1 fillsoft" pathLength="1" d="M32 50c6-4 16-5 24-3.5V16c-8-1.5-18-.5-24 3.5z"/>
<path class="dr d2" pathLength="1" d="M8 46.5V50c8-1.5 18-1 24 3 6-4 16-4.5 24-3v-3.5"/>
<g class="f f2"><path d="M13 24c5-.8 10-.3 14 1.6M13 30c5-.8 10-.3 14 1.6M13 36c5-.8 10-.3 14 1.6M37 25.6c4-1.9 9-2.4 14-1.6M37 31.6c4-1.9 9-2.4 14-1.6"/></g>
<g class="pop p1"><path class="fillfg" d="M45 15.3V27l2.6-2.2 2.6 2.2V14.9z"/></g>
<g class="lp-page"><path class="bgfill" d="M32 19.5c6-4 16-5 24-3.5v30.5c-8-1.5-18-.5-24 3.5z"/></g>
''',

}

def ill7(key, cls=''):
    return f'<svg class="ill ill-{key} {cls}" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ILL7[key]}</svg>'


LIVE = '.live:is(:hover,:focus-visible,:has(.lk:focus-visible))'

ICONE7_CSS = f'''
.ill{{color:var(--fg);overflow:visible}}
.ill *{{transform-box:fill-box;transform-origin:center}}
.ill .dash{{stroke-dasharray:2 3;opacity:.55}}
.ill .dotf,.ill .fillfg{{fill:currentColor;stroke:none}}
.ill .fillsoft{{fill:color-mix(in srgb,var(--fg) 12%,transparent)}}
.ill .fillcore{{fill:color-mix(in srgb,var(--fg) 45%,transparent);stroke:none}}
.ill .bgfill{{fill:var(--bg);stroke:currentColor}}
.ill .si{{font-family:var(--display);font-style:italic;font-size:15px;fill:currentColor;stroke:none;text-anchor:middle}}
.ill .fillleaf{{fill:color-mix(in srgb,var(--fg) 22%,transparent);stroke:currentColor}}
.ill-approfondimenti .lp-page{{opacity:0;transform-origin:0% 50%}}
.ill-difficolta .g-leaf.l,.ill-difficolta .lp-leaf.l{{transform-origin:100% 100%}}
.ill-difficolta .g-leaf.r,.ill-difficolta .lp-leaf.r{{transform-origin:0% 100%}}
@keyframes ill-grow{{from{{transform:scale(0)}}to{{transform:scale(1)}}}}
@keyframes lp-leaf{{0%,100%{{transform:rotate(0)}}50%{{transform:rotate(var(--sw))}}}}
@keyframes lp-page{{0%{{opacity:0;transform:scaleX(1)}}12%{{opacity:1;transform:scaleX(1)}}50%{{transform:scaleX(0)}}86%{{opacity:1;transform:scaleX(-1)}}100%{{opacity:0;transform:scaleX(-1)}}}}
.ill .glow{{fill:color-mix(in srgb,var(--fg) 22%,transparent);stroke:none;opacity:0}}
.ill .dr{{stroke-dasharray:1;stroke-dashoffset:0}}

@keyframes ill-draw{{from{{stroke-dashoffset:1;stroke-opacity:0}}7%{{stroke-opacity:1}}to{{stroke-dashoffset:0;stroke-opacity:1}}}}
@keyframes ill-fillin{{from{{fill-opacity:0}}to{{fill-opacity:1}}}}
@keyframes ill-fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes ill-pop{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes ill-reply{{0%{{opacity:0;transform:translate(4px,8px) scale(.7)}}70%{{opacity:1;transform:translate(0,-1px) scale(1.03)}}100%{{opacity:1;transform:none}}}}
/* vita (solo al passaggio): partono tutte dalla posa di riposo e ci tornano */
@keyframes lp-beat{{0%,46%,100%{{transform:scale(1)}}8%{{transform:scale(1.14)}}16%{{transform:scale(.98)}}24%{{transform:scale(1.09)}}34%{{transform:scale(1)}}}}
@keyframes lp-tw{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:.3;transform:scale(.55)}}}}
@keyframes lp-fla{{0%,100%{{transform:none}}30%{{transform:scaleY(1.045) skewX(-1.8deg)}}60%{{transform:scaleY(.975) skewX(1.4deg)}}82%{{transform:scaleY(1.02) skewX(-.5deg)}}}}
@keyframes lp-flb{{0%,100%{{transform:none}}35%{{transform:scaleY(.95) skewX(2.2deg)}}70%{{transform:scaleY(1.06) skewX(-1.6deg)}}}}
@keyframes lp-core{{0%,100%{{transform:scale(1);opacity:1}}50%{{transform:scale(1.12);opacity:.8}}}}
@keyframes lp-halo{{0%,100%{{transform:rotate(0)}}50%{{transform:rotate(7deg)}}}}
@keyframes lp-wave{{0%,100%{{transform:translateX(0)}}50%{{transform:translateX(-2.5px)}}}}
@keyframes lp-spark{{0%{{opacity:1;transform:translateY(0)}}70%{{opacity:0;transform:translateY(-12px)}}71%{{opacity:0;transform:translateY(4px)}}100%{{opacity:1;transform:translateY(0)}}}}
@keyframes lp-type{{0%,60%,100%{{transform:translateY(0)}}30%{{transform:translateY(-3.5px)}}}}
@keyframes lp-reply{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.03)}}}}

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
 .ill-difficolta .g-leaf.l{{animation:ill-grow 700ms var(--ease) calc(var(--d,0ms) + 1900ms) both}}
 .ill-difficolta .g-leaf.r{{animation:ill-grow 700ms var(--ease) calc(var(--d,0ms) + 2100ms) both}}
 .ill-comunicazione .reply{{transform-origin:75% 100%;animation:ill-reply 800ms var(--ease) calc(var(--d,0ms) + 2500ms) both}}

 /* vita: solo con il puntatore sopra o il fuoco dentro il contenitore .live */
 {LIVE} .lp-leaf.l{{--sw:-7deg;animation:lp-leaf 3.2s ease-in-out infinite}}
 {LIVE} .lp-leaf.r{{--sw:7deg;animation:lp-leaf 3.2s ease-in-out .4s infinite}}
 {LIVE} .lp-page{{animation:lp-page 3.6s cubic-bezier(.45,0,.3,1) infinite}}
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
 {LIVE} .lp-type{{animation:lp-type 1.2s ease-in-out infinite}}
 {LIVE} .lp-type.b{{animation-delay:.15s}} {LIVE} .lp-type.c{{animation-delay:.3s}}
 {LIVE} .lp-reply{{transform-origin:75% 100%;animation:lp-reply 3s ease-in-out infinite}}
}}
'''
