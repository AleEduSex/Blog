// Inserisce la prova «Percorsi» dopo il passo 3 di #funziona e fotografa desktop e mobile.
const { chromium } = require('playwright'); const fs = require('fs');
const CSS = fs.readFileSync(__dirname + '/tw.css', 'utf8');
const SNIP = fs.readFileSync(process.argv[2], 'utf8'); const OUT = process.argv[3];
(async () => {
  const b = await chromium.launch();
  for (const [w, h, tag] of [[1280, 800, 'desktop'], [390, 760, 'mobile']]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    await p.route('https://cdn.tailwindcss.com/**', r => r.fulfill({ contentType: 'application/javascript',
      body: `window.tailwind={};(function(){var s=document.createElement('style');s.textContent=${JSON.stringify(CSS)};document.head.appendChild(s)})();` }));
    await p.goto('http://localhost:8768/', { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
    const H = await p.evaluate(() => document.body.scrollHeight);
    for (let y = 0; y < H; y += 500) { await p.evaluate(v => window.scrollTo(0, v), y); await p.waitForTimeout(100); }
    await p.evaluate(s => { const ol = document.querySelector('#funziona ol'); ol.insertAdjacentHTML('afterend', s); for (const e of document.querySelectorAll('body *')) { const ps = getComputedStyle(e).position; if (ps === 'fixed' || ps === 'sticky') e.style.display = 'none'; } }, SNIP);
    await p.waitForTimeout(500);
    const el = await p.$('#percorsi-prova');
    await el.evaluate(e => e.scrollIntoView({ block: 'start' }));
    await p.evaluate(() => window.scrollBy(0, -260)); await p.waitForTimeout(600);
    await el.screenshot({ path: `${OUT}/percorsi-${tag}-solo.png` });
    // contesto: dal passo 3 alla fine del blocco
    const bb = await p.evaluate(() => { const a = document.querySelector('#funziona ol').getBoundingClientRect(), z = document.querySelector('#percorsi-prova').getBoundingClientRect();
      return { y: a.bottom - 520 + scrollY, h: z.bottom - a.bottom + 560 }; });
    await p.screenshot({ path: `${OUT}/percorsi-${tag}.png`, fullPage: true, clip: { x: 0, y: bb.y, width: w, height: bb.h } });
    const ov = await p.evaluate(() => document.documentElement.scrollWidth > innerWidth);
    console.log(tag, 'overflow:', ov);
    await p.close();
  }
  await b.close();
})();
