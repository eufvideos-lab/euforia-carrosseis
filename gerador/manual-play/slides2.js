// Carrosséis "História de empresário" com foto (PH = mapa de fotos em data URL, injetado pelo render)
var BR='#C2410C', OFF='#F2EFEA';
function sym(c,st){ return box(st,'<svg viewBox="0 0 150 122">'+sy(c)+'</svg>'); }
function H(txt,top,size,extra){ return '<h2 class="T" style="position:absolute;left:76px;right:76px;top:'+top+'px;font-size:'+size+'px;'+(extra||'')+'">'+txt+'</h2>'; }
function P(txt,top,extra){ return '<p class="tx" style="position:absolute;left:76px;right:76px;top:'+top+'px;'+(extra||'')+'">'+txt+'</p>'; }
function photo(src,pos,h){ return '<div style="position:absolute;left:0;right:0;top:0;height:'+(h||1350)+'px;background:url('+src+') '+(pos||'center')+'/cover no-repeat"></div><div style="position:absolute;left:0;right:0;top:0;height:'+(h||1350)+'px;background:linear-gradient(180deg,rgba(5,5,5,.15) 0%,rgba(5,5,5,0) 30%,rgba(5,5,5,.75) 62%,#050505 86%)"></div>'; }
function credit(t,bottom){ return '<div style="position:absolute;right:76px;bottom:'+(bottom||150)+'px;font-size:20px;color:#848484;letter-spacing:.04em">Foto: '+t+'</div>'; }
function eyebrow(t,top,c){ return '<div style="position:absolute;left:76px;top:'+top+'px;font-size:26px;letter-spacing:.2em;font-weight:600;color:'+(c||'#FF6518')+';text-transform:uppercase">'+t+'</div>'; }
function quote(n,t,q,who,bg){ var dk=bg==='#FF6518'; return '<div class="cv" style="background:'+bg+';color:'+(dk?'#050505':'#fff')+'">'+hd(n,t,dk?1:0)+
  '<div class="T" style="position:absolute;left:60px;top:150px;font-size:300px;line-height:1;color:'+(dk?'#050505':'#FF6518')+'">“</div>'+
  H(q,430,92,'color:'+(dk?'#050505':'#fff'))+
  '<p class="tx" style="position:absolute;left:76px;right:76px;top:1040px;font-size:32px;color:'+(dk?'#050505':'#B8B8B8')+'">'+who+'</p>'+ft('Por que isso importa?',dk?1:0)+'</div>'; }
function ctaW(n,t,word){ return '<div class="cv">'+hd(n,t)+
  '<h2 class="T" style="position:absolute;left:76px;right:76px;top:180px;font-size:58px;font-stretch:112%;line-height:.98">Agende um <span class="o" style="white-space:nowrap">Raio-X</span> <span class="o">gratuito</span> com os nossos consultores.</h2>'+
  '<p class="tx" style="position:absolute;left:76px;right:76px;top:500px;font-size:36px">Apenas 15 minutos pra mudar o rumo do seu negócio.</p>'+
  '<div style="position:absolute;left:76px;right:76px;top:600px;border:3px solid #FF6518;border-radius:28px;padding:44px 0;text-align:center"><div style="font-size:26px;letter-spacing:.2em;color:#B8B8B8;font-weight:600">COMENTE</div><div class="T o" style="font-size:150px;line-height:1;margin-top:10px">'+word+'</div></div>'+
  '<p class="tx" style="position:absolute;left:76px;right:76px;top:960px;font-size:30px">Comente a palavra acima e a gente te manda o link no direct.<br><br><b>Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</p>'+
  '<div style="position:absolute;left:76px;bottom:64px;width:300px">'+lockH(O,W)+'</div></div>'; }

var CARS={
'adibe-cimed':[
 function(){ return '<div class="cv">'+photo(PH.adibe1,'center 20%')+hd(1,7)+eyebrow('História de empresário',760)+H('O dono da<br>Cimed virou<br>o rosto da <span class="o">marca.</span>',820,96)+credit('exame.com',150)+ft('Desliza')+'</div>'; },
 function(){ return '<div class="cv">'+hd(2,7)+H('Ele podia<br>ficar nos<br><span class="o">bastidores.</span>',200,110)+P('João Adibe Marques é o presidente da Cimed, uma das maiores farmacêuticas do país. Mesmo assim, decidiu <b>sair de trás da mesa e aparecer</b>.',680)+P('Nas redes, ganhou até apelido: <b>Tio João</b>.',1000,'font-size:36px')+ghost()+ft('E o que ele diz?')+'</div>'; },
 function(){ return quote(3,7,'O brasileiro gosta de comprar de quem bota cara.','João Adibe, à Forbes (maio de 2026)','#FF6518'); },
 function(){ return '<div class="cv">'+hd(4,7)+H('Agenda,<br>fábrica e<br><span class="o">bastidor.</span>',200,110)+P('Ele mostra a rotina, os produtos sendo feitos e o dia a dia da empresa. <b>A família inteira entrou no jogo.</b>',660)+P('Ele mesmo chama a Cimed de <b>“a empresa farmacêutica mais digital do planeta”</b>.',920)+ft('E deu resultado?')+'</div>'; },
 function(){ return '<div class="cv">'+photo(PH.adibe2,'center 15%')+hd(5,7)+eyebrow('Resultado',700)+H('R$ 1 bilhão<br>em <span class="o">3 meses.</span>',760,104)+P('Faturamento da Cimed no 1º trimestre de 2026, alta de 20% sobre o ano anterior (InvestNews).',1010,'font-size:32px')+credit('marciatravessoni.com.br',150)+ft('E o que você leva disso?')+'</div>'; },
 function(){ return '<div class="cv" style="background:'+OFF+';color:#050505">'+hd(6,7,1)+H('Você não<br>precisa ser<br>dono de uma<br><span style="color:'+BR+'">farmacêutica.</span>',200,96,'color:#050505')+'<p class="tx" style="position:absolute;left:76px;right:76px;top:780px;color:#3a3a3a">Precisa <b style="color:#050505">botar a cara</b>. Quem é referência no offline e aparece na internet vira a escolha óbvia de quem procura.</p>'+ft('Bora aparecer?',1)+'</div>'; },
 function(){ return ctaW(7,7,'CARA'); }
],
'alfredo-soares':[
 function(){ return '<div class="cv">'+photo(PH.alfredo1,'center 18%')+hd(1,7)+eyebrow('História de empresário',760)+H('Quem é<br>lembrado<br>sempre tem<br><span class="o">oportunidade.</span>',820,88)+credit('g4business.com',150)+ft('Desliza')+'</div>'; },
 function(){ return '<div class="cv">'+hd(2,7)+H('Alfredo<br><span class="o">Soares.</span>',200,120)+P('Fundou a <b>Xtech Commerce</b>. Em três anos, a plataforma transacionou <b>R$ 547 milhões</b> em vendas e foi comprada pela <b>VTEX</b> em 2017.',560)+ghost()+ft('E depois?')+'</div>'; },
 function(){ return '<div class="cv">'+hd(3,7)+H('Não parou<br><span class="o">por aí.</span>',200,110)+
   '<div style="position:absolute;left:76px;right:76px;top:540px;display:grid;gap:0">'+[['Sócio da VTEX',''],['Cofundador do G4 Educação','com Tallis Gomes e Bruno Nardon'],['4 livros best-sellers','como o Bora Vender'],['Canal no YouTube e palestras','conteúdo e palco']].map(function(r,i){return '<div style="display:flex;align-items:center;gap:30px;border-top:2px solid #262626;padding:26px 0"><span class="T" style="font-size:44px;color:#FF6518;min-width:70px">0'+(i+1)+'</span><span style="font-size:38px;line-height:1.25;color:#fff;font-weight:600">'+r[0]+(r[1]?'<br><span style="font-weight:400;font-size:30px;color:#B8B8B8">'+r[1]+'</span>':'')+'</span></div>';}).join('')+'</div>'+ft('E o segredo?')+'</div>'; },
 function(){ return quote(4,7,'Sempre terá oportunidade para quem é lembrado.','Alfredo Soares, ao SBT News','#050505'); },
 function(){ return '<div class="cv">'+photo(PH.alfredo2,'center 20%')+hd(5,7)+H('E como ser<br><span class="o">lembrado?</span>',760,88)+P('<b>Aparecendo.</b> Livro, vídeo, palco, podcast. Quem some da cabeça do cliente some da agenda dele.',980,'font-size:34px')+credit('infomoney.com.br',150)+ft('E pra você?')+'</div>'; },
 function(){ return '<div class="cv" style="background:#FF6518;color:#050505">'+hd(6,7,1)+H('Seu cliente<br>só te contrata<br>se lembrar<br>de você.',200,100,'color:#050505')+'<p class="tx" style="position:absolute;left:76px;right:76px;top:800px;color:#050505">E ele precisa lembrar <b style="color:#050505">na hora em que precisa</b>. Conteúdo frequente é o que te coloca nessa hora.</p>'+ft('Bora ser lembrado?',1)+'</div>'; },
 function(){ return ctaW(7,7,'LEMBRADO'); }
]
};
