// Carrosséis do manual (seção Instagram). Usa os helpers globais do manual: hd, ft, box, ghost, lockH, sy, O, K, W.
var BR='#C2410C', OFF='#F2EFEA';
function sym(c,st){ return box(st,'<svg viewBox="0 0 150 122">'+sy(c)+'</svg>'); }
function symUp(c,st){ return box(st,'<svg viewBox="0 0 122 150"><g transform="translate(0,150) rotate(-90)">'+sy(c)+'</g></svg>'); }
function H(txt,top,size,extra){ return '<h2 class="T" style="position:absolute;left:76px;right:76px;top:'+top+'px;font-size:'+size+'px;'+(extra||'')+'">'+txt+'</h2>'; }
function P(txt,top,extra){ return '<p class="tx" style="position:absolute;left:76px;right:76px;top:'+top+'px;'+(extra||'')+'">'+txt+'</p>'; }
function list(items,top,dark){ return '<div style="position:absolute;left:76px;right:76px;top:'+top+'px;display:grid;gap:0">'+items.map(function(r,i){
  return '<div style="display:flex;align-items:center;gap:30px;border-top:2px solid '+(dark?'#d8d3cb':'#262626')+';padding:26px 0"><span class="T" style="font-size:44px;color:'+(dark?BR:'#FF6518')+';min-width:70px">'+(i+1<10?'0':'')+(i+1)+'</span><span style="font-size:38px;line-height:1.25;color:'+(dark?'#050505':'#fff')+';font-weight:600">'+r[0]+(r[1]?'<br><span style="font-weight:400;font-size:30px;color:'+(dark?'#3a3a3a':'#B8B8B8')+'">'+r[1]+'</span>':'')+'</span></div>';}).join('')+'</div>'; }
function nums(top,dark){ return '<div style="position:absolute;left:76px;right:76px;top:'+top+'px;display:grid;gap:0">'+
  [['+380','ecossistemas digitais construídos'],['+R$ 18,2 mi','que ajudamos nossos clientes a faturar'],['+2,1 bi','de visualizações geradas']].map(function(r){return '<div style="display:flex;align-items:baseline;gap:28px;border-top:2px solid '+(dark?'#d8d3cb':'#262626')+';padding:20px 0"><span class="T" style="font-size:54px;white-space:nowrap;color:'+(dark?BR:'#FF6518')+';min-width:430px">'+r[0]+'</span><span style="font-size:30px;line-height:1.25;color:'+(dark?'#3a3a3a':'#B8B8B8')+'">'+r[1]+'</span></div>';}).join('')+'</div>'; }
function ctaW(n,t,word){ return '<div class="cv">'+hd(n,t)+
  '<h2 class="T" style="position:absolute;left:76px;right:76px;top:180px;font-size:58px;font-stretch:112%;line-height:.98">Agende um <span class="o" style="white-space:nowrap">Raio-X</span> <span class="o">gratuito</span> com os nossos consultores.</h2>'+
  '<p class="tx" style="position:absolute;left:76px;right:76px;top:500px;font-size:36px">Apenas 15 minutos pra mudar o rumo do seu negócio.</p>'+
  '<div style="position:absolute;left:76px;right:76px;top:600px;border:3px solid #FF6518;border-radius:28px;padding:44px 0;text-align:center"><div style="font-size:26px;letter-spacing:.2em;color:#B8B8B8;font-weight:600">COMENTE</div><div class="T o" style="font-size:'+(word.length>7?150:190)+'px;line-height:1;margin-top:10px">'+word+'</div></div>'+
  '<p class="tx" style="position:absolute;left:76px;right:76px;top:960px;font-size:30px">Comente a palavra acima e a gente te manda o link no direct.<br><br><b>Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</p>'+
  '<div style="position:absolute;left:76px;bottom:64px;width:300px">'+lockH(O,W)+'</div></div>'; }

var CARS={
// 1 · GRAVA UMA VEZ (capa off-white do manual)
'grava-uma-vez':[
 function(){ return '<div class="cv" style="background:'+OFF+';color:#050505">'+hd(1,7,1)+H('Grava<br>uma vez.',300,120)+H('Aparece<br>em todo<br>lugar.',620,96,'color:'+BR)+sym(O,'right:76px;bottom:76px;width:140px')+'</div>'; },
 function(){ return '<div class="cv">'+hd(2,7)+H('Você não<br>precisa postar<br>todo <span class="o">dia.</span>',210,100)+P('Precisa de <b>um dia bem gravado</b> e de um time que transforma esse dia em semanas de conteúdo.',720)+ghost()+ft('Como funciona')+'</div>'; },
 function(){ return '<div class="cv">'+hd(3,7)+H('Um dia de<br><span class="o">gravação</span> vira:',190,92)+list([['Vídeos longos no YouTube','onde o cliente decide'],['Cortes curtos','Shorts, Reels e TikTok'],['Carrosséis e posts','Instagram e LinkedIn'],['Material de venda','pro seu time usar na conversa']],520)+ft('E depois?')+'</div>'; },
 function(){ return '<div class="cv" style="background:#FF6518;color:#050505">'+hd(4,7,1)+H('Gravar.<br>Distribuir.<br>Faturar.',230,124,'color:#050505')+'<p class="tx" style="position:absolute;left:76px;right:76px;top:760px;color:#050505">Você aparece uma vez na frente da câmera. <b style="color:#050505">A gente cuida do resto</b>, todo mês, em todas as redes.</p>'+ft('Quem chega, chega diferente',1)+'</div>'; },
 function(){ return '<div class="cv">'+hd(5,7)+H('O cliente<br>chega <span class="o">pronto.</span>',210,110)+P('Ele já te assistiu, já entendeu como você trabalha e <b>já confia em você</b> antes da primeira conversa.',600)+P('Menos explicação. Menos objeção. Mais fechamento.',960,'font-size:36px;color:#fff;font-weight:600')+ft('Funciona mesmo?')+'</div>'; },
 function(){ return '<div class="cv" style="background:'+OFF+';color:#050505">'+hd(6,7,1)+box('left:76px;top:200px;width:700px',lockH(O,K))+'<p class="tx" style="position:absolute;left:76px;right:76px;top:440px;color:#3a3a3a">É o que a gente chama de <b style="color:#050505">ecossistema digital</b>. E já construímos muitos.</p>'+nums(700,1)+ft('Quer o seu?',1)+'</div>'; },
 function(){ return ctaW(7,7,'APARECER'); }
],
// 2 · PARE DE POSTAR POR POSTAR (capa laranja do manual)
'pare-de-postar':[
 function(){ return '<div class="cv" style="background:#FF6518;color:#050505">'+hd(1,7,1)+H('Pare de<br>postar<br>por<br>postar.',330,118)+box('left:76px;bottom:80px;width:300px',lockH(K,K))+'</div>'; },
 function(){ return '<div class="cv">'+hd(2,7)+H('Post todo dia.<br>Direct <span class="o">vazio.</span>',210,96)+
   '<div style="position:absolute;left:76px;right:76px;top:560px;background:#141414;border:2px solid #262626;border-radius:28px;padding:48px;display:flex;gap:30px;align-items:center"><div style="width:84px;height:84px;border-radius:50%;background:#2e2e2e;flex:none"></div><div style="font:700 40px Inter;color:#fff;line-height:1.25">Nenhuma mensagem nova<br><span style="font-weight:500;font-size:32px;color:#848484">há 12 dias</span></div></div>'+
   P('Se isso parece familiar, o problema não é falta de esforço.',900)+ft('É falta de direção')+'</div>'; },
 function(){ return '<div class="cv">'+hd(3,7)+H('3 sinais de<br>que você posta<br>por <span class="o">postar</span>',190,84)+list([['Você posta pra cumprir tabela','e não pra levar alguém a um próximo passo'],['Quem curte é colega de profissão','não é quem te contrata'],['Ninguém pergunta preço','porque nada no post leva até você']],600)+ft('Então o que fazer?')+'</div>'; },
 function(){ return '<div class="cv" style="background:'+OFF+';color:#050505">'+hd(4,7,1)+H('Antes de gravar,<br>responda <span style="color:'+BR+'">3 coisas:</span>',200,72,'color:#050505')+list([['Pra quem é?','o cliente que você quer atender'],['Que problema resolve?','a dor que faz ele te procurar'],['Qual o próximo passo?','o que ele faz depois de assistir']],560,1)+ft('E depois?',1)+'</div>'; },
 function(){ return '<div class="cv">'+hd(5,7)+H('Menos post.<br>Mais <span class="o">ecossistema.</span>',210,100)+P('Um vídeo longo bem pensado alimenta o mês inteiro: cortes, carrosséis e posts que <b>levam todos pro mesmo lugar</b>. Você.',620)+ghost()+ft('E se eu for bom no que faço?')+'</div>'; },
 function(){ return '<div class="cv" style="background:#FF6518;color:#050505">'+hd(6,7,1)+H('Você é bom.<br>Mas ninguém<br>sabe.',230,100,'color:#050505')+'<p class="tx" style="position:absolute;left:76px;right:76px;top:900px;color:#050505">O que falta não é talento. <b style="color:#050505">É a internet saber disso.</b></p>'+ft('Bora resolver?',1)+'</div>'; },
 function(){ return ctaW(7,7,'OBJETIVO'); }
],
// 3 · PRA CIMA SEMPRE (capa preta do manual)
'pra-cima-sempre':[
 function(){ return '<div class="cv">'+hd(1,6)+symUp(O,'left:300px;top:170px;width:480px')+H('Pra cima<br><span class="o">sempre.</span>',820,132)+P('Tudo na marca aponta pra frente. Igual o seu negócio deveria.',1100,'font-size:34px')+ft('Desliza')+'</div>'; },
 function(){ return '<div class="cv">'+hd(2,6)+H('Tem muito<br>profissional<br>sério que<br><span class="o">ninguém<br>conhece.</span>',190,104)+ghost()+ft('A gente existe por isso')+'</div>'; },
 function(){ return '<div class="cv" style="background:#FF6518;color:#050505">'+hd(3,6,1)+sym(K,'left:76px;top:190px;width:520px')+H('A gente aperta<br>o play nessa<br>história.',720,96,'color:#050505')+ft('Como?',1)+'</div>'; },
 function(){ return '<div class="cv">'+hd(4,6)+H('Pra cima não<br>é slogan.<br>É <span class="o">método.</span>',190,100)+list([['Gravar','um dia bem planejado'],['Distribuir','em todas as redes, todo mês'],['Medir','o que trouxe cliente de verdade'],['Melhorar','e gravar de novo, melhor']],640)+ft('Pra quem é isso?')+'</div>'; },
 function(){ return '<div class="cv" style="background:'+OFF+';color:#050505">'+hd(5,6,1)+H('Consultores.<br>Mentores.<br>Terapeutas.<br>Advogados.<br>Palestrantes.',200,92,'color:#050505')+'<p class="tx" style="position:absolute;left:76px;right:76px;top:820px;color:#3a3a3a">Quem já é referência no offline e quer <b style="color:#050505">ser visto, lembrado e escolhido</b> na internet.</p>'+ft('Bora pra cima?',1)+'</div>'; },
 function(){ return ctaW(6,6,'SEMPRE'); }
],
// 4 · GRUPO EUFORIA · MESMO NOME, MESMO TIME (capa off-white do manual)
'mesmo-time':[
 function(){ return '<div class="cv" style="background:'+OFF+';color:#050505">'+hd(1,6,1)+box('left:76px;top:200px;width:928px',lockH(O,K))+'<p class="tx" style="position:absolute;left:76px;right:76px;top:480px;color:#3a3a3a">Mesmo nome, mesmo time, <b style="color:#050505">mesma obsessão</b>: fazer profissional sério ser visto na internet.</p>'+nums(760,1)+ft('Desliza',1)+'</div>'; },
 function(){ return '<div class="cv">'+hd(2,6)+H('O que<br><span class="o">mudou?</span>',200,120)+P('A marca. O símbolo virou um play e as frentes do grupo cresceram.',540)+H('O que<br>não mudou?',800,80,'color:#848484')+P('<b>O time, o método e o cuidado com cada cliente.</b>',1010)+ft('E o que tem de novo?')+'</div>'; },
 function(){ return '<div class="cv">'+hd(3,6)+H('Um grupo de<br><span class="o">soluções.</span>',200,88)+list([['Mídia','canais e ecossistemas próprios'],['Tecnologia','sistemas próprios que rodam o grupo'],['Produção de alto padrão','gravação que valoriza quem aparece'],['Negócios','marcas que querem anunciar onde o público está']],520)+ft('E pra você?')+'</div>'; },
 function(){ return '<div class="cv" style="background:#FF6518;color:#050505">'+hd(4,6,1)+H('O mesmo<br>time que<br>já construiu<br>+380<br>ecossistemas.',200,112,'color:#050505')+ft('Agora com mais força',1)+'</div>'; },
 function(){ return '<div class="cv">'+hd(5,6)+H('Construindo<br>negócios sólidos<br>para profissionais<br><span class="o">sérios.</span>',220,76)+P('Se o mercado muda, a gente muda junto. <b>Pra cima, sempre.</b>',860)+ghost()+ft('Vamos conversar?')+'</div>'; },
 function(){ return ctaW(6,6,'TIME'); }
]
};
