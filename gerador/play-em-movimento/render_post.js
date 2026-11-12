// Fotografa os slides de UM post: lê carrosseis/<pasta>/slides.html e grava slide_XX (ou post_01) .png/.jpg na mesma pasta.
// Uso: node render_post.js <pasta_do_post> [post]   ("post" = post único: o slide sai como post_01)
let chromium; try { ({ chromium } = require('playwright')); } catch (e) { ({ chromium } = require('/opt/node-tools/node_modules/playwright')); }
const path = require('path');
(async () => {
  const [dir, modo] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1400 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve(dir, 'slides.html'));
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  const els = await p.$$('.slide');
  for (let i = 0; i < els.length; i++) {
    const n = (modo === 'post' ? 'post_' : 'slide_') + String(i + 1).padStart(2, '0');
    await els[i].screenshot({ path: path.join(dir, n + '.png') });
    await els[i].screenshot({ path: path.join(dir, n + '.jpg'), type: 'jpeg', quality: 92 });
  }
  console.log(dir, els.length);
  await b.close();
})();
