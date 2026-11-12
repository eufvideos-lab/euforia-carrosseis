#!/usr/bin/env python3
"""Modelos 6 a 15 (capa + miolo + CTA). Usa os helpers do gerar.py. Depois: node foto.js"""
import gerar as g
from gerar import sym, bar, logo, page

P, G, F, O, A, L, B, C = "#050505", "#141312", "#26221F", "#F2EFEA", "#DDD6CB", "#FF6518", "#C2410C", "#8a827a"
RX = '<span style="white-space:nowrap">Raio-X</span>'

def cta(palavra, tema="preto", topo="", top=210):
    bg, fg, ac, sub = {"preto": (P, O, L, "#cfc8bf"), "grafite": (G, O, L, "#cfc8bf"), "off": (O, P, B, "#3a3531"), "laranja": (L, P, P, P)}[tema]
    lg = {"preto": "cor-fundo-escuro", "grafite": "cor-fundo-escuro", "off": "cor-fundo-claro", "laranja": "mono-preto"}[tema]
    box = f"background:{P};border-color:{P};color:{L}" if tema in ("off", "laranja") else f"color:{L}"
    tam = 150 if len(palavra) <= 5 else (120 if len(palavra) <= 7 else 96)
    return f"""<div class="slide" style="background:{bg};color:{fg}">{topo or f'<div class="top">{logo(lg)}<div class="lab" style="opacity:.6">3 / 3</div></div>'}
      <div class="abs" style="left:80px;right:80px;top:{top}px">
        <div class="x" style="font-size:76px">Agende um <span style="color:{ac}">{RX} gratuito</span> com os nossos consultores.</div>
        <div class="box" style="margin-top:54px;{box}"><div class="lab" style="color:{O}">Comente</div><div class="x" style="font-size:{tam}px">{palavra}</div></div>
        <div class="t" style="margin-top:36px;font-size:32px;color:{sub}">A gente te manda o link no direct. <b style="color:{fg}">Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>
      </div></div>"""

def lista(itens, cor_n=L, cor_t=O, borda=F, tam=44, pad=30):
    h = ""
    for k, t in enumerate(itens):
        h += f'<div style="display:grid;grid-template-columns:96px 1fr;align-items:center;padding:{pad}px 0;border-top:3px solid {borda}"><div class="c" style="font-size:110px;color:{cor_n};line-height:.8">{k+1}</div><div style="font-size:{tam}px;font-weight:600;line-height:1.2;color:{cor_t}">{t}</div></div>'
    return f'<div style="border-bottom:3px solid {borda}">{h}</div>'

# ───────── 6 · NOTIFICAÇÃO ─────────
def m06():
    def notif(titulo, txt, quando, op=1, esc=1):
        return f"""<div style="background:{F};border-radius:34px;padding:30px 34px;display:grid;grid-template-columns:84px 1fr;gap:24px;align-items:center;opacity:{op};transform:scale({esc});transform-origin:top center">
          <div style="width:84px;height:84px;border-radius:22px;background:{L};display:grid;place-items:center">{bar(P, 50, 20)}</div>
          <div><div style="display:flex;justify-content:space-between;font-size:26px;color:{C};font-weight:600"><span>{titulo}</span><span>{quando}</span></div>
          <div style="font-size:35px;font-weight:600;line-height:1.25;margin-top:6px;color:{O}">{txt}</div></div></div>"""
    s1 = f"""<div class="slide" style="background:{G};color:{O}">
      <div class="abs lab" style="left:0;right:0;top:84px;text-align:center;color:{C}">Tela ilustrativa</div>
      <div class="abs c" style="left:0;right:0;top:120px;text-align:center;font-size:330px">09:41</div>
      <div class="abs" style="left:70px;right:70px;top:450px;display:flex;flex-direction:column;gap:18px">
        {notif('Mensagem nova', 'Oi! Vi o seu vídeo. Você atende online?', 'agora')}
        {notif('Mensagem nova', 'Achei você no YouTube. Podemos conversar?', '2 min', .75, .95)}
        {notif('Mensagem nova', 'Te encontrei pesquisando no Google.', '9 min', .4, .9)}
      </div>
      <div class="abs" style="left:80px;right:80px;bottom:84px"><div class="x" style="font-size:92px">E se o cliente chegasse <span class="lar">assim?</span></div></div></div>"""
    partes = ["A base de conteúdo", "A distribuição", "A busca", "O caminho até você"]
    cards = "".join(f'<div style="background:{F};border-radius:26px;padding:26px 30px;display:flex;gap:22px;align-items:center">{bar(L, 56, 22)}<div style="font-size:40px;font-weight:700">{p}</div></div>' for p in partes)
    s2 = f"""<div class="slide" style="background:{G};color:{O}"><div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:{C}">2 / 3</div></div>
      <div class="abs" style="left:80px;right:80px;top:200px"><div class="x" style="font-size:80px">Quem te procura precisa te <span class="lar">encontrar.</span></div>
      <div class="t" style="margin-top:30px;color:#cfc8bf">Um ecossistema digital funciona como um sistema, e não como posts soltos:</div>
      <div style="display:flex;flex-direction:column;gap:14px;margin-top:36px">{cards}</div></div></div>"""
    page("modelo-06-notificacao", [s1, s2, cta("Mensagem", "grafite")])

# ───────── 7 · RECIBO ─────────
def m07():
    zig = ",".join(f"{x}% {100 if k % 2 else 97.6}%" for k, x in enumerate([100 - i * 4 for i in range(26)]))
    papel = f"background:{O};color:{P};clip-path:polygon(0 0,100% 0,{zig})"
    def lin(a, b, forte=False):
        fs = 64 if forte else 44
        return f'<div class="c" style="display:flex;align-items:baseline;gap:12px;font-size:{fs}px;line-height:1.1;margin-top:{26 if forte else 16}px"><span>{a}</span><span style="flex:1;border-bottom:4px dotted {P};transform:translateY(-8px)"></span><span>{b}</span></div>'
    s1 = f"""<div class="slide" style="background:{L};color:{P}">
      <div class="abs" style="left:150px;right:150px;top:70px;height:1010px;padding:56px 56px 0;{papel};transform:rotate(-2.5deg)">
        <div class="c" style="font-size:86px;text-align:center">Cupom do mês</div>
        <div class="lab" style="text-align:center;margin-top:10px;font-size:20px">Perfil ativo · todo santo dia</div>
        <div style="border-top:4px dashed {P};margin:30px 0 14px"></div>
        {lin('30x post', 'feito')}{lin('Foto do escritório', 'feito')}{lin('Frase motivacional', 'feito')}{lin('Dica rápida', 'feito')}{lin('Data comemorativa', 'feito')}
        <div style="border-top:4px dashed {P};margin:34px 0 0"></div>
        {lin('Clientes novos', '?', True)}
        <div style="margin-top:36px;height:70px;background:repeating-linear-gradient(90deg,{P} 0 6px,transparent 6px 10px,{P} 10px 20px,transparent 20px 26px,{P} 26px 30px,transparent 30px 40px)"></div>
        <div class="lab" style="text-align:center;margin-top:14px;font-size:18px">Volte sempre</div>
      </div>
      <div class="abs x" style="left:80px;right:80px;bottom:80px;font-size:76px">A conta de postar por postar</div></div>"""
    itens = ["Comece pelo cliente, não pelo calendário", "Tenha uma base que acumula", "Use o Instagram para distribuir", "Deixe claro o próximo passo", "Meça o que importa"]
    s2 = f"""<div class="slide" style="background:{L};color:{P}">
      <div class="abs" style="left:70px;right:70px;top:70px;height:1210px;padding:60px 60px 0;{papel}">
        <div class="lab" style="color:{B}">2 / 3 · A conta certa</div>
        <div class="x" style="font-size:70px;margin-top:18px">O que fazer em vez disso</div>
        <div style="margin-top:34px">{lista(itens, B, P, P, 42, 24)}</div>
      </div></div>"""
    page("modelo-07-recibo", [s1, s2, cta("Conta", "laranja")])

# ───────── 8 · PARE ─────────
def m08():
    oct_ = "clip-path:polygon(29.3% 0,70.7% 0,100% 29.3%,100% 70.7%,70.7% 100%,29.3% 100%,0 70.7%,0 29.3%)"
    s1 = f"""<div class="slide" style="background:{P};color:{O}">
      <div class="abs" style="left:110px;top:70px;width:860px;height:860px;background:{O};{oct_}"></div>
      <div class="abs" style="left:134px;top:94px;width:812px;height:812px;background:{L};{oct_};display:grid;place-items:center">
        <div class="c" style="font-size:400px;color:{P};margin-top:24px">Pare</div></div>
      <div class="abs" style="left:80px;right:80px;bottom:84px"><div class="x" style="font-size:78px">de depender de <span class="lar">indicação.</span></div></div></div>"""
    def placa(t):
        return f'<div style="background:{O};color:{P};border-radius:22px;padding:8px"><div style="border:5px solid {P};border-radius:16px;padding:26px 30px;display:flex;justify-content:space-between;align-items:center"><div class="c" style="font-size:96px">{t}</div>{bar(L, 170, 56)}</div></div>'
    s2 = f"""<div class="slide" style="background:{P};color:{O}"><div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:{C}">2 / 3</div></div>
      <div class="abs" style="left:80px;right:80px;top:200px"><div class="x" style="font-size:74px">Indicação é ótima. Só não pode ser o <span class="lar">único caminho.</span></div>
      <div style="display:flex;flex-direction:column;gap:22px;margin-top:50px">{placa('Ser encontrado')}{placa('Ser assistido')}{placa('Ser procurado')}</div></div></div>"""
    page("modelo-08-pare", [s1, s2, cta("Caminho", "preto")])

# ───────── 9 · INGRESSO ─────────
def m09():
    furo = f"radial-gradient(circle at 0 50%,transparent 34px,#000 35px) left/51% 100% no-repeat,radial-gradient(circle at 100% 50%,transparent 34px,#000 35px) right/51% 100% no-repeat"
    s1 = f"""<div class="slide" style="background:{P};color:{O}">
      <div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:{C}">1 / 3</div></div>
      <div class="abs x" style="left:80px;right:80px;top:190px;font-size:118px">Entrada<br><span class="lar">franca.</span></div>
      <div class="abs" style="left:-30px;top:520px;width:1140px;height:500px;transform:rotate(-7deg);display:grid;grid-template-columns:1fr 290px;-webkit-mask:{furo};mask:{furo}">
        <div style="background:{O};color:{P};padding:50px 50px 0 90px;border-right:6px dashed {P}">
          <div class="lab" style="font-size:24px">Vale uma sessão</div>
          <div class="c" style="font-size:230px;margin-top:8px">Raio-X</div>
          <div style="display:flex;gap:40px;margin-top:22px"><div><div class="lab" style="font-size:16px;opacity:.6">Entrada</div><div class="c" style="font-size:56px">Gratuita</div></div><div><div class="lab" style="font-size:16px;opacity:.6">Com</div><div class="c" style="font-size:56px">Nossos consultores</div></div></div>
        </div>
        <div style="background:{L};color:{P};padding:50px 70px 0 36px"><div class="lab" style="font-size:20px">Admite</div><div class="c" style="font-size:260px;line-height:.8;margin-top:10px">1</div>
          <div style="margin-top:26px;height:96px;background:repeating-linear-gradient(90deg,{P} 0 6px,transparent 6px 10px,{P} 10px 20px,transparent 20px 26px,{P} 26px 30px,transparent 30px 40px)"></div></div>
      </div>
      <div class="abs t" style="left:80px;right:80px;bottom:84px;color:#cfc8bf">Uma conversa para olhar o seu digital de perto.</div></div>"""
    def campo(a, b):
        return f'<div style="padding:34px 0;border-top:3px solid {F}"><div class="lab" style="color:{L}">{a}</div><div class="x" style="font-size:54px;margin-top:12px">{b}</div></div>'
    s2 = f"""<div class="slide" style="background:{P};color:{O}"><div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:{C}">2 / 3</div></div>
      <div class="abs" style="left:80px;right:80px;top:200px"><div class="c" style="font-size:150px">Programa da sessão</div>
      <div style="margin-top:40px;border-bottom:3px solid {F}">{campo('Para quem', 'Profissionais com resultado no offline')}{campo('Com quem', 'Os nossos consultores')}{campo('Quanto custa', 'Nada. É gratuito.')}</div></div></div>"""
    page("modelo-09-ingresso", [s1, s2, cta("Ingresso", "preto")])

# ───────── 10 · ECO ─────────
def m10():
    linhas = ""
    for k, cor in enumerate([A, "#b0a89c", "#6f6861"]):
        linhas += f'<div class="c" style="font-size:236px;color:transparent;-webkit-text-stroke:3px {cor};line-height:.88">Invisível</div>'
    s1 = f"""<div class="slide" style="background:{O};color:{P}">
      <div class="top">{logo('cor-fundo-claro')}<div class="lab" style="opacity:.6">1 / 3</div></div>
      <div class="abs" style="left:76px;top:190px">{linhas}
        <div style="position:relative;display:inline-block"><div class="c" style="font-size:236px;line-height:.88">Invisível</div>
        <div class="abs" style="left:-34px;top:36%;width:236px;transform:rotate(-8deg)">{bar(L, 236, 52)}</div></div>
      </div>
      <div class="abs" style="left:80px;right:80px;bottom:80px;font-size:44px;font-weight:700;line-height:1.2">20 anos de mercado.<br>E na internet, quem te encontra?</div></div>"""
    itens = ["Entenda como o seu cliente procura o que você vende", "Escolha uma base, não cinco redes ao mesmo tempo", "Grave com roteiro, não no improviso", "Deixe o resto com quem faz isso todo dia", "Meça o movimento, não só as curtidas"]
    s2 = f"""<div class="slide" style="background:{P};color:{O}"><div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:{C}">2 / 3</div></div>
      <div class="abs" style="left:80px;right:80px;top:190px"><div class="c" style="font-size:170px">De <span style="color:transparent;-webkit-text-stroke:3px {C}">in</span><span class="lar">visível</span></div>
      <div class="x" style="font-size:44px;margin-top:10px">Por onde começar</div>
      <div style="margin-top:30px">{lista(itens, L, O, F, 38, 20)}</div></div></div>"""
    page("modelo-10-eco", [s1, s2, cta("Visível", "off")])

# ───────── 11 · DICIONÁRIO ─────────
def m11():
    aba = lambda t: f'<div class="abs c" style="right:0;top:250px;width:92px;height:150px;background:{L};color:{P};border-radius:18px 0 0 18px;font-size:110px;display:grid;place-items:center;padding-top:14px">{t}</div>'
    verb = "font-family:Archivo;font-weight:800;font-stretch:100%;letter-spacing:-.02em;line-height:.92"
    s1 = f"""<div class="slide" style="background:{O};color:{P}">{aba('E')}
      <div class="top">{logo('cor-fundo-claro')}<div class="lab" style="opacity:.6;margin-right:60px">Dicionário · 1 / 3</div></div>
      <div class="abs" style="left:80px;right:110px;top:230px">
        <div style="{verb};font-size:176px">e·cos·sis·<br>te·ma<br>di·gi·tal</div>
        <div style="font-size:34px;font-style:italic;color:{B};margin-top:26px;font-weight:600">substantivo masculino</div>
        <div style="border-top:4px solid {P};margin-top:30px;padding-top:30px;display:grid;grid-template-columns:60px 1fr;gap:14px 8px;font-size:48px;line-height:1.25;font-weight:500">
          <b>1.</b><div>Presença na internet que funciona como um sistema, e não como posts soltos.</div>
          <b>2.</b><div><b>Grava uma vez, aparece em todo lugar.</b></div></div>
        <div style="margin-top:44px;font-size:42px;font-weight:600;display:flex;align-items:center;gap:14px"><span style="font-style:italic;color:{B}">Não confundir com</span>
          <span style="position:relative;font-weight:800">canal<span class="abs" style="left:-10px;right:-10px;top:50%;margin-top:-2px">{bar(L, '100%', 9, 'width:100%')}</span></span></div>
      </div></div>"""
    partes = [("a base de conteúdo", "normalmente, vídeos no YouTube"), ("a distribuição", "o conteúdo vai para as outras redes"), ("a busca", "para ser achado por quem pesquisa"), ("o caminho até você", "o próximo passo fica claro"), ("a leitura dos resultados", "o movimento é medido")]
    ent = "".join(f'<div style="padding:34px 0;border-top:3px solid {P}"><span style="{verb};font-size:64px">{a}</span><div style="font-size:37px;color:#3a3531;margin-top:8px;font-style:italic">{b}</div></div>' for a, b in partes)
    s2 = f"""<div class="slide" style="background:{O};color:{P}">{aba('E')}
      <div class="top">{logo('cor-fundo-claro')}<div class="lab" style="opacity:.6;margin-right:60px">Dicionário · 2 / 3</div></div>
      <div class="abs" style="left:80px;right:130px;top:210px"><div class="lab" style="color:{B}">Ver também</div><div class="x" style="font-size:66px;margin-top:16px">As cinco partes</div>
      <div style="margin-top:30px;border-bottom:3px solid {P}">{ent}</div></div></div>"""
    page("modelo-11-dicionario", [s1, s2, cta("Verbete", "off")])

# ───────── 12 · CHECKLIST ─────────
def m12():
    sinais = ["Os meses ficaram imprevisíveis", "Quem chega já chega comparando preço", "Tem gente que some depois de pesquisar o seu nome", "Concorrentes mais novos aparecem na sua frente", "A sensação de que o crescimento travou"]
    def caixa(on=False, t=62):
        dentro = f'<div class="abs" style="left:8px;top:{t*0.28}px;transform:rotate(-38deg)">{bar(L, t*1.25, t*0.4)}</div>' if on else ""
        return f'<div style="width:{t}px;height:{t}px;border:6px solid {P};border-radius:12px;position:relative;flex:none">{dentro}</div>'
    falsas = "".join(f'<div style="display:flex;gap:26px;align-items:center;margin-top:24px">{caixa(k == 0, 70)}<div style="height:30px;border-radius:15px;background:{A if k else P};width:{w}px"></div></div>' for k, w in enumerate([470, 400, 520, 360, 440]))
    clip = f'<div class="abs" style="left:50%;top:-46px;margin-left:-150px;width:300px;height:110px;background:{P};border-radius:22px"></div><div class="abs" style="left:50%;top:-70px;margin-left:-50px;width:100px;height:70px;border:16px solid {P};border-bottom:0;border-radius:40px 40px 0 0"></div>'
    s1 = f"""<div class="slide" style="background:{L};color:{P}">
      <div class="abs" style="left:110px;top:130px;width:860px;height:1040px;background:{O};border-radius:26px;transform:rotate(3deg);padding:104px 70px 0">{clip}
        <div class="c" style="font-size:126px">5 sinais de que a indicação está diminuindo</div>{falsas}</div>
      <div class="abs" style="left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;align-items:center">{logo('mono-preto')}<div style="display:flex;align-items:center;gap:18px"><div class="lab">Confira os seus</div>{bar(P, 110, 30)}</div></div></div>"""
    linhas = "".join(f'<div style="display:flex;gap:26px;align-items:center;padding:28px 0;border-top:3px solid {A}">{caixa(True)}<div style="font-size:42px;font-weight:700;line-height:1.2">{s}</div></div>' for s in sinais)
    s2 = f"""<div class="slide" style="background:{L};color:{P}">
      <div class="abs" style="left:60px;top:110px;width:960px;height:1180px;background:{O};border-radius:26px;padding:100px 60px 0">{clip}
        <div class="lab" style="color:{B}">2 / 3 · Marque os que são seus</div>{'<div style="margin-top:22px;border-bottom:3px solid ' + A + '">' + linhas + '</div>'}
        <div style="font-size:34px;font-weight:600;margin-top:30px;color:#3a3531">Marcou algum? O problema pode não ser o seu trabalho.</div></div></div>"""
    page("modelo-12-checklist", [s1, s2, cta("Sinais", "laranja")])

# ───────── 13 · CALENDÁRIO ─────────
def m13():
    cel = ""
    for d in range(1, 31):
        cel += f'<div style="border:2px solid {F};border-radius:12px;height:136px;padding:10px 12px;position:relative"><div class="c" style="font-size:40px;color:{C}">{d:02d}</div><div class="lab" style="position:absolute;left:12px;bottom:12px;font-size:15px;color:#5c5650">postou</div><div class="abs" style="right:10px;top:16px">{bar("#3a3531", 34, 12)}</div></div>'
    s1 = f"""<div class="slide" style="background:{P};color:{O}">
      <div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:{C}">1 / 3</div></div>
      <div class="abs x" style="left:80px;top:196px;font-size:62px">30 dias postando.</div>
      <div class="abs" style="left:80px;right:80px;top:320px;display:grid;grid-template-columns:repeat(6,1fr);gap:10px">{cel}</div>
      <div class="abs" style="left:-60px;right:-60px;top:590px;background:{L};color:{P};transform:rotate(-7deg);padding:26px 0 18px;text-align:center"><div class="c" style="font-size:230px">E o cliente?</div></div>
      <div class="abs t" style="left:80px;right:80px;bottom:76px;color:#cfc8bf;font-size:40px">Frequência sozinha não traz cliente.</div></div>"""
    itens = ["O conteúdo é genérico", "Falta profundidade", "O post some do feed rapidamente", "O público é de curiosos, não de compradores", "Não existe próximo passo"]
    s2 = f"""<div class="slide" style="background:{P};color:{O}"><div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:{C}">2 / 3</div></div>
      <div class="abs" style="left:80px;right:80px;top:200px"><div class="x" style="font-size:70px">Por que postar todo dia <span class="lar">não basta</span></div>
      <div style="margin-top:36px">{lista(itens, L, O, F, 42, 24)}</div></div></div>"""
    page("modelo-13-calendario", [s1, s2, cta("Agenda", "preto")])

# ───────── 14 · RAIO-X ─────────
def cantos(cor, m=60, t=90, e=8, topo=60, base=60):
    q = lambda pos, b: f'<div class="abs" style="{pos};width:{t}px;height:{t}px;{b}"></div>'
    return (q(f"left:{m}px;top:{topo}px", f"border-left:{e}px solid {cor};border-top:{e}px solid {cor}") + q(f"right:{m}px;top:{topo}px", f"border-right:{e}px solid {cor};border-top:{e}px solid {cor}")
            + q(f"left:{m}px;bottom:{base}px", f"border-left:{e}px solid {cor};border-bottom:{e}px solid {cor}") + q(f"right:{m}px;bottom:{base}px", f"border-right:{e}px solid {cor};border-bottom:{e}px solid {cor}"))

def m14():
    thumbs = "".join(f'<div style="aspect-ratio:1.45;border-radius:14px;{"border:6px solid " + L if k == 4 else "background:" + F}"></div>' for k in range(6))
    def nota(t, pos):
        return f'<div class="abs lab" style="{pos};background:{L};color:{P};padding:10px 14px 8px;font-size:19px">{t}</div>'
    s1 = f"""<div class="slide" style="background:{G};color:{O}">{cantos(O)}
      <div class="abs lab" style="left:110px;top:104px;color:{L}">Raio-X · analisando</div><div class="abs lab" style="right:110px;top:104px;color:{C}">1 / 3</div>
      <div class="abs" style="left:190px;right:190px;top:190px">
        <div style="display:flex;gap:30px;align-items:center"><div style="width:150px;height:150px;border-radius:50%;background:{F};flex:none"></div>
          <div style="flex:1"><div style="height:30px;border-radius:15px;background:{F};width:70%"></div><div style="height:20px;border-radius:10px;background:{F};width:90%;margin-top:18px"></div><div style="height:20px;border-radius:10px;background:{F};width:50%;margin-top:12px"></div></div></div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px">{thumbs}</div></div>
      <div class="abs" style="left:60px;right:60px;top:530px;height:8px;background:{L}"></div>
      {nota('Como o cliente te procura', 'left:110px;top:372px')}{nota('O que ele encontra', 'right:110px;top:486px')}{nota('O próximo passo', 'left:300px;top:660px')}
      <div class="abs" style="left:110px;right:110px;bottom:120px"><div class="c" style="font-size:172px">Raio-X do seu <span class="lar">digital</span></div></div></div>"""
    perg = ["Como o seu cliente procura o que você vende?", "O que ele encontra quando pesquisa o seu nome?", "Qual é o próximo passo depois que ele te acha?"]
    s2 = f"""<div class="slide" style="background:{G};color:{O}">{cantos(O)}
      <div class="abs lab" style="left:110px;top:104px;color:{L}">Raio-X · resultado</div><div class="abs lab" style="right:110px;top:104px;color:{C}">2 / 3</div>
      <div class="abs" style="left:110px;right:110px;top:210px"><div class="x" style="font-size:66px">Três perguntas sobre o seu digital</div>
      <div style="margin-top:36px">{lista(perg, L, O, F, 46, 36)}</div></div></div>"""
    s3 = cta("Raio-X", "grafite", cantos(O) + f'<div class="abs lab" style="left:110px;top:104px;color:{L}">Raio-X · a sua vez</div><div class="abs lab" style="right:110px;top:104px;color:{C}">3 / 3</div>', 230).replace("left:80px;right:80px;top:230px", "left:110px;right:110px;top:230px")
    page("modelo-14-raio-x", [s1, s2, s3])

# ───────── 15 · REC ─────────
def m15():
    def visor(tc, n):
        grade = f'<div class="abs" style="left:33.33%;top:60px;bottom:60px;width:2px;background:{F}"></div><div class="abs" style="left:66.66%;top:60px;bottom:60px;width:2px;background:{F}"></div><div class="abs" style="top:33.33%;left:60px;right:60px;height:2px;background:{F}"></div><div class="abs" style="top:66.66%;left:60px;right:60px;height:2px;background:{F}"></div>'
        bat = f'<div style="width:74px;height:34px;border:4px solid {O};border-radius:8px;padding:4px;position:relative"><div style="height:100%;width:70%;background:{O};border-radius:2px"></div><div class="abs" style="right:-10px;top:8px;width:6px;height:10px;background:{O};border-radius:0 3px 3px 0"></div></div>'
        return f"""{grade}{cantos(O)}
          <div class="abs" style="left:110px;top:100px;display:flex;align-items:center;gap:16px"><div style="width:30px;height:30px;border-radius:50%;background:{L}"></div><div class="c" style="font-size:56px;color:{L}">Rec</div><div class="c" style="font-size:56px;margin-left:14px">{tc}</div></div>
          <div class="abs" style="right:110px;top:108px;display:flex;align-items:center;gap:20px"><div class="lab" style="color:{C}">{n} / 3</div>{bat}</div>"""
    s1 = f"""<div class="slide" style="background:{P};color:{O}">{visor('00:00:00', 1)}
      <div class="abs" style="left:50%;top:50%;width:90px;height:90px;margin:-45px 0 0 -45px"><div class="abs" style="left:43px;top:0;bottom:0;width:4px;background:{O}"></div><div class="abs" style="top:43px;left:0;right:0;height:4px;background:{O}"></div></div>
      <div class="abs" style="left:110px;right:110px;top:250px"><div class="x" style="font-size:100px">Vergonha<br>de <span class="lar">câmera?</span></div></div>
      <div class="abs" style="left:110px;right:110px;bottom:230px;font-size:44px;font-weight:700;line-height:1.2">Você fala bem em reunião.<br>E trava quando a câmera liga.</div>
      <div class="abs" style="left:110px;right:110px;bottom:104px;display:flex;justify-content:space-between"><div class="lab" style="background:{O};color:{P};padding:10px 14px 8px">Roteiro: pronto</div><div class="lab" style="color:{C};padding:10px 0">Tomada 01</div></div></div>"""
    itens = ["Você sabe por onde começar", "Você sabe quando terminar", "Você fala do que conhece", "Errar deixa de ser um problema"]
    s2 = f"""<div class="slide" style="background:{P};color:{O}">{visor('00:00:12', 2)}
      <div class="abs" style="left:110px;right:110px;top:230px;background:{P}"><div class="x" style="font-size:66px">O que muda com o <span class="lar">roteiro pronto</span></div>
      <div style="margin-top:34px;background:{P}">{lista(itens, L, O, F, 46, 30)}</div></div>
      <div class="abs" style="left:110px;bottom:104px"><div class="lab" style="background:{O};color:{P};padding:10px 14px 8px">Tomada 02</div></div></div>"""
    s3 = cta("Gravar", "preto", cantos(O) + f'<div class="abs" style="left:110px;top:100px;display:flex;align-items:center;gap:16px"><div style="width:30px;height:30px;border-radius:50%;background:{L}"></div><div class="c" style="font-size:56px;color:{L}">Rec</div><div class="c" style="font-size:56px;margin-left:14px">00:00:24</div></div><div class="abs lab" style="right:110px;top:116px;color:{C}">3 / 3</div>', 250).replace("left:80px;right:80px;top:250px", "left:110px;right:110px;top:250px")
    page("modelo-15-rec", [s1, s2, s3])

for f in (m06, m07, m08, m09, m10, m11, m12, m13, m14, m15):
    f()
print("ok2")
