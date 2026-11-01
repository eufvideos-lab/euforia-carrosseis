const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file:///mnt/project-files/rebranding/manual-euforia-play.html');await p.waitForTimeout(2000);
await p.addStyleTag({content:"@font-face{font-family:'Archivo';src:url(data:font/ttf;base64,"+fs.readFileSync('/mnt/project-files/dossie/thumb-materiais/Archivo.ttf').toString('base64')+") format('truetype');font-weight:100 900;font-stretch:62% 125%}.cv .T{line-height:.98 !important}"});
await p.addScriptTag({content:fs.readFileSync('slides.js','utf8')});
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
await p.evaluate(()=>{const s=document.createElement('div');s.id='stage';s.style.cssText='position:fixed;left:0;top:0;width:1080px;height:1350px;z-index:999999;background:#000';document.body.appendChild(s);window.scrollTo(0,0);});
const keys=await p.evaluate(()=>Object.keys(CARS));
for(const k of keys){fs.mkdirSync('out/'+k,{recursive:true});const n=await p.evaluate(k=>CARS[k].length,k);
 for(let i=0;i<n;i++){await p.evaluate(([k,i])=>{document.getElementById('stage').innerHTML=CARS[k][i]();
 document.querySelectorAll('#stage .T').forEach(function(el){ var cs=getComputedStyle(el); if(cs.position!=='absolute' && !el.closest('[style*="border:3px"]')) return; var w=el.clientWidth||el.parentElement.clientWidth; var g=0; while(el.scrollWidth>w+1 && g<60){ el.style.fontSize=(parseFloat(getComputedStyle(el).fontSize)*0.97)+'px'; g++; } });
},[k,i]);await p.waitForTimeout(150);
  const el=await p.$('#stage .cv');await el.screenshot({path:`out/${k}/slide_${String(i+1).padStart(2,'0')}.png`});}}
await b.close();})();
