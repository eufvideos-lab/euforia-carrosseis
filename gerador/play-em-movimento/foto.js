// Fotografa cada .slide dos modelo-*.html em PNG e JPG (1080x1350) e monta a folha de contato.
let chromium; try { ({ chromium } = require('playwright')); } catch (e) { ({ chromium } = require('/opt/node-tools/node_modules/playwright')); }
const fs = require('fs'), path = require('path');
(async () => {
  const aqui = __dirname, saida = process.env.SAIDA || path.join(aqui, 'saida');
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 4600, height: 1420 }, deviceScaleFactor: 1 });
  for (const f of fs.readdirSync(aqui).filter(f => /^modelo-.*\.html$/.test(f)).sort()) {
    const nome = f.replace('.html', ''), dir = path.join(saida, nome);
    fs.mkdirSync(dir, { recursive: true });
    await p.goto('file://' + path.join(aqui, f)); await p.evaluate(() => document.fonts.ready);
    const els = await p.$$('.slide');
    for (let i = 0; i < els.length; i++) {
      const n = String(i + 1).padStart(2, '0');
      await els[i].screenshot({ path: path.join(dir, `slide_${n}.png`) });
      await els[i].screenshot({ path: path.join(dir, `slide_${n}.jpg`), type: 'jpeg', quality: 92 });
    }
    await p.screenshot({ path: path.join(saida, nome + '-visao-geral.jpg'), type: 'jpeg', quality: 85, fullPage: true });
    console.log(nome, els.length);
  }
  await b.close();
})();
