#!/usr/bin/env python3
"""Semana 16 a 22/11/2026 nos modelos Play em Movimento.
Uso: python3 semana_2026-11-16.py  -> grava carrosseis/<pasta>/slides.html; depois render_post.js."""
import os, sys, glob
AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
sys.path.insert(0, AQUI)
antes = set(glob.glob(os.path.join(AQUI, "modelo-*.html")))
import gerar as g   # os imports rodam os exemplos; os HTML gerados são apagados abaixo
import gerar2 as g2
from gerar import sym, bar, logo, player_chrome
from gerar2 import P, G, F, O, A, L, B, C, RX, lista, cantos
for f in set(glob.glob(os.path.join(AQUI, "modelo-*.html"))) - antes:
    os.remove(f)

def cta(palavra, tema="preto", topo="", top=210, rodape=""):
    h = g2.cta(palavra, tema, topo, top)
    if rodape:
        sub = "#3a3531" if tema in ("off",) else ("#050505" if tema == "laranja" else "#cfc8bf")
        h = h[:h.rfind("</div></div>")] + f'<div class="lab" style="margin-top:40px;color:{sub}">{rodape}</div></div></div>'
    return h

def salvar(pasta, slides):
    d = os.path.join(REPO, "carrosseis", pasta)
    os.makedirs(d, exist_ok=True)
    html = f'<!doctype html><meta charset="utf-8"><style>{g.CSS}</style>' + "".join(slides)
    open(os.path.join(d, "slides.html"), "w").write(html)

# ───────── SEG 16/11 · carrossel · PLAYER · Shorts em temporadas ─────────
def seg_player():
    bg = "background:#141312;color:#F2EFEA"; n = 7
    caps = ["Abertura", "A novidade", "Em sequência", "O motivo", "Para quem ensina", "O caminho", "O seu play"]
    def ch(i): return player_chrome(i, n, f"Episódio {i}", "Fim" if i == n else f"A seguir: {caps[i].lower()}")
    def corpo(i, html): return f'<div class="slide" style="{bg}">{ch(i)}{html}</div>'
    s1 = corpo(1, f"""<div class="abs" style="right:-190px;top:176px">{sym('#FF6518', 690)}</div>
      <div class="lab abs" style="left:80px;top:200px;background:#FF6518;color:#050505;padding:10px 16px 8px">Notícia</div>
      <div class="abs" style="left:80px;right:80px;bottom:250px">
        <div class="x" style="font-size:104px">O YouTube<br>virou série.</div>
        <div class="t" style="margin-top:28px;max-width:800px;color:#cfc8bf">Os Shorts agora podem ser organizados em temporadas e episódios.</div></div>""")
    s2 = corpo(2, f"""<div class="abs c" style="left:70px;top:200px;font-size:400px;color:transparent;-webkit-text-stroke:4px #FF6518">01</div>
      <div class="abs" style="left:80px;right:80px;top:600px">
        <div class="x" style="font-size:80px">Temporadas e <span class="lar">episódios.</span></div>
        <div class="t" style="margin-top:30px;max-width:860px;color:#cfc8bf">O recurso Shorts Series, anunciado no Made on YouTube, junta vídeos curtos numa série, com capa própria e ordem de exibição. Está sendo liberado aos poucos para canais do Programa de Parcerias.</div></div>""")
    s3 = corpo(3, f"""<div class="abs c" style="left:70px;top:200px;font-size:400px;color:transparent;-webkit-text-stroke:4px #FF6518">02</div>
      <div class="abs" style="left:80px;right:80px;top:600px">
        <div class="x" style="font-size:80px">Assistiu um, <span class="lar">vê o próximo.</span></div>
        <div class="t" style="margin-top:30px;max-width:860px;color:#cfc8bf">Quem encontra um episódio no feed ganha um botão para assistir a série inteira, na ordem.</div></div>""")
    s4 = corpo(4, f"""<div class="abs" style="left:76px;right:60px;top:210px">
        <div class="lab" style="color:#8a827a">Por que o YouTube fez isso</div>
        <div class="c" style="font-size:330px;color:#FF6518;white-space:nowrap;margin-top:20px">+6,5<span style="font-size:.42em;color:#F2EFEA;margin-left:14px">bi</span></div>
        <div class="x" style="font-size:52px;margin-top:30px;max-width:900px">de views em séries curtas no 1º semestre de 2026</div>
        <div class="t" style="margin-top:22px;font-size:32px;color:#cfc8bf;max-width:860px">Gente assistindo episódio atrás de episódio. Números divulgados pelo YouTube.</div></div>""")
    s5 = corpo(5, f"""<div class="abs" style="left:80px;right:80px;top:210px">
        <div class="x" style="font-size:92px">O seu conhecimento já é uma <span class="lar">série.</span></div>
        <div class="t" style="margin-top:40px;max-width:880px;color:#cfc8bf">As 10 dúvidas que você mais responde viram 10 episódios.</div>
        <div class="t" style="margin-top:24px;max-width:880px;font-weight:800">Quem assiste o primeiro chega no último já confiando em você.</div></div>""")
    trilhas = [("Vídeo longo", 300), ("Episódios curtos", 460), ("Instagram", 560), ("LinkedIn", 660), ("Busca", 760)]
    tr = "".join(f'<div style="position:relative;height:54px">{bar("#FF6518" if k % 2 == 0 else "#F2EFEA", w, 54)}<div class="lab abs" style="left:26px;top:13px;color:#050505;font-size:23px">{nome}</div></div>' for k, (nome, w) in enumerate(trilhas))
    s6 = corpo(6, f"""<div class="abs" style="left:80px;right:80px;top:200px"><div class="x" style="font-size:84px">Grava uma vez.<br><span class="lar">Aparece em todo lugar.</span></div></div>
      <div class="abs" style="left:80px;top:600px;display:flex;flex-direction:column;gap:20px">{tr}</div>
      <div class="abs t" style="left:80px;right:80px;top:990px;color:#cfc8bf;max-width:860px">É assim que funciona um ecossistema digital.</div>""")
    s7 = cta("Serie", "grafite", player_chrome(7, n, "Episódio 7", "Fim"), 200, "Salve e mande pra quem explica muito bem o que faz")
    salvar("2026-11-16_shorts-series", [s1, s2, s3, s4, s5, s6, s7])

# ───────── TER 17/11 · post único · PARE ─────────
def ter_pare():
    oct_ = "clip-path:polygon(29.3% 0,70.7% 0,100% 29.3%,100% 70.7%,70.7% 100%,29.3% 100%,0 70.7%,0 29.3%)"
    s1 = f"""<div class="slide" style="background:{P};color:{O}">
      <div class="abs" style="left:110px;top:70px;width:860px;height:860px;background:{O};{oct_}"></div>
      <div class="abs" style="left:134px;top:94px;width:812px;height:812px;background:{L};{oct_};display:grid;place-items:center">
        <div class="c" style="font-size:400px;color:{P};margin-top:24px">Pare</div></div>
      <div class="abs" style="left:80px;right:80px;bottom:84px"><div class="x" style="font-size:78px">de depender de <span class="lar">indicação.</span></div>
      <div class="t" style="margin-top:22px;font-size:34px;color:#cfc8bf">Indicação é ótima. Só não pode ser o único caminho.</div></div></div>"""
    s1 = s1.replace("bottom:84px\"><div class=\"x\" style=\"font-size:78px\">", "bottom:70px\"><div class=\"x\" style=\"font-size:72px\">")
    salvar("2026-11-17_pare-indicacao", [s1])

# ───────── QUA 18/11 · carrossel · RAIO-X · Simon Sinek ─────────
def qua_raiox():
    n = 7
    def topo(i, t): return f'{cantos(O)}<div class="abs lab" style="left:110px;top:104px;color:{L}">{t}</div><div class="abs lab" style="right:110px;top:104px;color:{C}">{i} / {n}</div>'
    def sl(i, t, html): return f'<div class="slide" style="background:{G};color:{O}">{topo(i, t)}{html}</div>'
    def nota(t, pos): return f'<div class="abs lab" style="{pos};background:{L};color:{P};padding:10px 14px 8px;font-size:19px">{t}</div>'
    video = f"""<div class="abs" style="left:190px;right:190px;top:190px;height:400px;border-radius:22px;background:{F};display:grid;place-items:center">
        <div style="width:150px;height:150px;border-radius:50%;background:{L};display:grid;place-items:center"><div style="width:0;height:0;border-left:52px solid {P};border-top:32px solid transparent;border-bottom:32px solid transparent;margin-left:14px"></div></div>
        <div class="abs lab" style="right:20px;bottom:18px;background:rgba(0,0,0,.7);padding:8px 12px 6px">18:35</div></div>"""
    s1 = sl(1, "Raio-X · analisando", f"""{video}
      <div class="abs" style="left:60px;right:60px;top:660px;height:8px;background:{L}"></div>
      {nota('Uma câmera', 'left:110px;top:620px')}{nota('Um flip chart', 'right:110px;top:700px')}{nota('Uma ideia clara', 'left:380px;top:620px')}
      <div class="abs" style="left:110px;right:110px;bottom:120px"><div class="c" style="font-size:150px">Raio-X de um vídeo de <span class="lar">18 minutos</span></div>
      <div class="t" style="margin-top:24px;color:#cfc8bf">A história de Simon Sinek →</div></div>""")
    s2 = sl(2, "Raio-X · o vídeo", f"""<div class="abs" style="left:110px;right:110px;top:220px">
        <div class="c" style="font-size:200px;color:{L}">Setembro de 2009.</div>
        <div class="x" style="font-size:62px;margin-top:40px">Um palco pequeno, um flip chart e uma ideia.</div>
        <div class="t" style="margin-top:34px;color:#cfc8bf">Simon Sinek falou 18 minutos no TEDxPuget Sound sobre por que algumas empresas inspiram as pessoas e outras não.</div></div>""")
    circ = "".join(f'<div class="abs" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px;border-radius:50%;border:5px solid {L if k == 0 else O};display:grid;place-items:center"></div>' for k, (x, y, d) in enumerate([(370, 300, 340), (300, 230, 480), (230, 160, 620)]))
    s3 = sl(3, "Raio-X · a ideia", f"""<div class="abs" style="left:0;right:0;top:120px;height:720px">{circ}
        <div class="abs c" style="left:0;right:0;top:430px;text-align:center;font-size:76px;color:{L}">Por quê</div>
        <div class="abs c" style="left:0;right:0;top:262px;text-align:center;font-size:50px">Como</div>
        <div class="abs c" style="left:0;right:0;top:190px;text-align:center;font-size:44px;color:{C}">O quê</div></div>
      <div class="abs" style="left:110px;right:110px;bottom:130px"><div class="x" style="font-size:58px">As pessoas não compram o que você faz. <span class="lar">Compram por que você faz.</span></div>
      <div class="t" style="margin-top:20px;font-size:32px;color:#cfc8bf">O Círculo Dourado, de dentro para fora.</div></div>""")
    s4 = sl(4, "Raio-X · o alcance", f"""<div class="abs" style="left:106px;right:90px;top:220px">
        <div class="c" style="font-size:400px;color:{L};white-space:nowrap">+64<span style="font-size:.42em;color:{O};margin-left:14px">mi</span></div>
        <div class="x" style="font-size:56px;margin-top:34px">de visualizações só no site do TED</div>
        <div class="t" style="margin-top:22px;font-size:34px;color:#cfc8bf">Um dos vídeos mais assistidos da história do TED. Sem contar o YouTube.</div>
        <div class="lab" style="margin-top:30px;font-size:18px;color:{C}">Fonte: ted.com</div></div>""")
    itens = ["O livro Comece pelo Porquê", "Convites para palestrar pelo mundo", "Um nome que virou referência em liderança"]
    s5 = sl(5, "Raio-X · o que veio depois", f"""<div class="abs" style="left:110px;right:110px;top:220px"><div class="x" style="font-size:70px">Um vídeo que <span class="lar">abriu portas</span></div>
      <div style="margin-top:40px">{lista(itens, L, O, F, 46, 36)}</div></div>""")
    s6 = sl(6, "Raio-X · a lição", f"""<div class="abs" style="left:110px;right:110px;top:220px">
        <div class="c" style="font-size:112px;line-height:.9">Ele não tinha o maior currículo da sala.</div>
        <div class="c" style="font-size:112px;line-height:.9;margin-top:30px;color:{L}">Tinha a explicação mais clara. Gravada.</div>
        <div class="t" style="margin-top:44px;color:#cfc8bf">O que você explica bem, gravado uma vez, continua trabalhando por anos.</div></div>""")
    s7 = cta("Porque", "grafite", cantos(O) + f'<div class="abs lab" style="left:110px;top:104px;color:{L}">Raio-X · a sua vez</div><div class="abs lab" style="right:110px;top:104px;color:{C}">7 / 7</div>', 230, "Salve e mande pra quem tem muito a ensinar").replace("left:80px;right:80px;top:230px", "left:110px;right:110px;top:230px")
    salvar("2026-11-18_simon-sinek", [s1, s2, s3, s4, s5, s6, s7])

# ───────── QUI 19/11 · post único · INGRESSO ─────────
def qui_ingresso():
    furo = f"radial-gradient(circle at 0 50%,transparent 34px,#000 35px) left/51% 100% no-repeat,radial-gradient(circle at 100% 50%,transparent 34px,#000 35px) right/51% 100% no-repeat"
    s1 = f"""<div class="slide" style="background:{P};color:{O}">
      <div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:{C}">Convite</div></div>
      <div class="abs x" style="left:80px;right:80px;top:190px;font-size:118px">Entrada<br><span class="lar">franca.</span></div>
      <div class="abs" style="left:-30px;top:520px;width:1140px;height:500px;transform:rotate(-7deg);display:grid;grid-template-columns:1fr 290px;-webkit-mask:{furo};mask:{furo}">
        <div style="background:{O};color:{P};padding:50px 50px 0 90px;border-right:6px dashed {P}">
          <div class="lab" style="font-size:24px">Vale uma sessão</div>
          <div class="c" style="font-size:230px;margin-top:8px">Raio-X</div>
          <div style="display:flex;gap:40px;margin-top:22px"><div><div class="lab" style="font-size:16px;opacity:.6">Entrada</div><div class="c" style="font-size:56px">Gratuita</div></div><div><div class="lab" style="font-size:16px;opacity:.6">Com</div><div class="c" style="font-size:56px">Nossa equipe</div></div></div>
        </div>
        <div style="background:{L};color:{P};padding:50px 70px 0 36px"><div class="lab" style="font-size:20px">Admite</div><div class="c" style="font-size:260px;line-height:.8;margin-top:10px">1</div>
          <div style="margin-top:26px;height:96px;background:repeating-linear-gradient(90deg,{P} 0 6px,transparent 6px 10px,{P} 10px 20px,transparent 20px 26px,{P} 26px 30px,transparent 30px 40px)"></div></div>
      </div>
      <div class="abs t" style="left:80px;right:80px;bottom:84px;color:#cfc8bf">Uma conversa para olhar o seu digital de perto. <b style="color:{O}">Comente INGRESSO.</b></div></div>"""
    salvar("2026-11-19_ingresso-raiox", [s1])

# ───────── SEX 20/11 · carrossel · MITO × FATO ─────────
def sex_mito():
    n = 7
    def par(i, mito, fato, apoio):
        return f"""<div class="slide" style="background:#050505;color:#F2EFEA">
          <div class="abs" style="left:0;right:0;top:0;height:560px;padding:72px 80px 0">
            <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab" style="color:#8a827a">Mito {i:02d}</div><div class="lab" style="color:#8a827a">{i+1} / {n}</div></div>
            <div style="position:relative;margin-top:60px;display:inline-block">
              <div class="x" style="font-size:74px;color:#6f6861">{mito}</div>
              <div class="abs" style="left:-24px;right:-40px;top:50%;margin-top:-12px;transform:rotate(-4deg)">{bar('#FF6518', '100%', 24, 'width:100%')}</div>
            </div></div>
          <div class="abs" style="left:0;right:0;top:560px;bottom:0;background:#FF6518;color:#050505;padding:64px 80px 0">
            <div class="c abs" style="right:60px;top:-92px;font-size:190px;color:#050505;background:#FF6518;padding:22px 26px 0;border-radius:14px 14px 0 0;line-height:.8">Fato</div>
            <div class="x" style="font-size:72px;margin-top:70px">{fato}</div>
            <div class="t" style="margin-top:30px;font-size:35px;font-weight:600;max-width:880px">{apoio}</div>
            <div class="abs" style="left:80px;bottom:72px">{logo('mono-preto', 42)}</div>
          </div></div>"""
    s1 = f"""<div class="slide" style="background:#050505;color:#F2EFEA">
      <div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:#8a827a">1 / {n}</div></div>
      <div class="abs" style="left:80px;top:200px">
        <div style="position:relative;display:inline-block"><div class="c" style="font-size:440px;color:#3a3531">Mito</div>
          <div class="abs" style="left:-40px;right:-110px;top:50%;margin-top:-34px">{bar('#FF6518', '100%', 68, 'width:100%')}</div></div>
        <div class="c" style="font-size:440px;color:#FF6518;margin-top:6px">Fato</div></div>
      <div class="abs x" style="left:80px;right:80px;bottom:80px;font-size:50px">Quatro mitos sobre aparecer na internet</div></div>"""
    s2 = par(1, "“Quem é bom<br>não precisa<br>aparecer.”", "Quem não aparece não é encontrado.", "O cliente pesquisa antes de contratar. Se não te acha, acha outro.")
    s3 = par(2, "“Vídeo é coisa<br>de influenciador.”", "Vídeo é onde o cliente te conhece.", "Quem te assiste explicando chega na primeira conversa já sabendo como você pensa.")
    s4 = par(3, "“Preciso postar<br>todo dia.”", "Precisa de uma base que acumula.", "Um vídeo bom continua sendo achado meses depois. Post solto some do feed em poucas horas.")
    s5 = par(4, "“Sem anúncio<br>não tem<br>resultado.”", "Anúncio é complemento, não a base.", "Resultado se constrói com conteúdo, estratégia e relacionamento. O anúncio acelera o que já funciona.")
    s6 = f"""<div class="slide" style="background:#050505;color:#F2EFEA">
      <div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:#8a827a">6 / {n}</div></div>
      <div class="abs" style="left:80px;right:80px;top:230px">
        <div class="c" style="font-size:150px;line-height:.92">A indicação continua.</div>
        <div class="c" style="font-size:150px;line-height:.92;margin-top:30px;color:#FF6518">Só deixa de ser o único caminho.</div>
        <div class="t" style="margin-top:50px;color:#cfc8bf;max-width:860px">Quem já é referência no offline tem o mais difícil: o conhecimento. Falta ser encontrado.</div></div></div>"""
    s7 = cta("Fato", "laranja", f'<div class="top">{logo("mono-preto")}<div class="lab">7 / {n}</div></div>', 210, "Salve e mande pra quem ainda acredita no mito 1")
    salvar("2026-11-20_mitos-aparecer", [s1, s2, s3, s4, s5, s6, s7])

# ───────── SÁB 21/11 · post único · RECIBO ─────────
def sab_recibo():
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
    salvar("2026-11-21_cupom-postar", [s1])

# ───────── DOM 22/11 · carrossel · CALENDÁRIO · Hábitos Atômicos ─────────
def dom_calendario():
    n = 7
    def topo(i): return f'<div class="top">{logo("cor-fundo-escuro")}<div class="lab" style="color:{C}">{i} / {n}</div></div>'
    def sl(i, html): return f'<div class="slide" style="background:{P};color:{O}">{topo(i)}{html}</div>'
    cel = "".join(f'<div style="border:2px solid {F if d < 24 else L};border-radius:12px;height:136px;padding:10px 12px;position:relative;{"background:" + L + ";color:" + P if d >= 24 else ""}"><div class="c" style="font-size:40px;color:{P if d >= 24 else C}">{d:02d}</div><div class="lab" style="position:absolute;left:12px;bottom:12px;font-size:15px;color:{P if d >= 24 else "#5c5650"}">+1%</div></div>' for d in range(1, 31))
    s1 = sl(1, f"""<div class="abs x" style="left:80px;top:196px;font-size:62px">1% melhor por dia.</div>
      <div class="abs" style="left:80px;right:80px;top:320px;display:grid;grid-template-columns:repeat(6,1fr);gap:10px">{cel}</div>
      <div class="abs" style="left:-60px;right:-60px;top:590px;background:{L};color:{P};transform:rotate(-7deg);padding:26px 0 18px;text-align:center"><div class="c" style="font-size:200px">37x em um ano</div></div>
      <div class="abs t" style="left:80px;right:80px;bottom:76px;color:#cfc8bf;font-size:38px">A conta de Hábitos Atômicos, de James Clear →</div>""")
    s2 = sl(2, f"""<div class="abs" style="left:80px;right:80px;top:210px"><div class="lab" style="color:{L}">O livro</div>
        <div class="x" style="font-size:84px;margin-top:20px">Hábitos Atômicos, de <span class="lar">James Clear.</span></div>
        <div class="t" style="margin-top:36px;color:#cfc8bf">Lançado em 2018, passou de 20 milhões de exemplares vendidos, segundo a editora.</div>
        <div class="t" style="margin-top:26px;font-weight:800">A ideia central: pequenas melhorias, repetidas, se acumulam.</div></div>""")
    s3 = sl(3, f"""<div class="abs" style="left:76px;right:60px;top:210px"><div class="lab" style="color:{L}">A conta do livro</div>
        <div class="c" style="font-size:250px;color:{L};white-space:nowrap;margin-top:20px">1,01<sup style="font-size:.4em">365</sup></div>
        <div class="c" style="font-size:250px;white-space:nowrap">= 37,78</div>
        <div class="t" style="margin-top:34px;color:#cfc8bf;max-width:880px">Melhorar 1% por dia durante um ano deixa você cerca de 37 vezes melhor. Piorar 1% por dia leva quase a zero.</div></div>""")
    s4 = sl(4, f"""<div class="abs" style="left:80px;right:80px;top:220px"><div class="lab" style="color:{L}">O ponto</div>
        <div class="c" style="font-size:150px;line-height:.92;margin-top:30px">Você não sobe ao nível das suas metas.</div>
        <div class="c" style="font-size:150px;line-height:.92;margin-top:30px;color:{L}">Cai ao nível dos seus sistemas.</div>
        <div class="lab" style="margin-top:40px;color:{C}">James Clear, Hábitos Atômicos</div></div>""")
    itens = ["Um vídeo por semana, sem falhar", "Cada vídeo um pouco melhor que o anterior", "Os cortes distribuídos sempre", "Medir e ajustar todo mês"]
    s5 = sl(5, f"""<div class="abs" style="left:80px;right:80px;top:200px"><div class="x" style="font-size:70px">O sistema <span class="lar">no digital</span></div>
      <div style="margin-top:36px">{lista(itens, L, O, F, 42, 30)}</div></div>""")
    sem = "".join(f'<div style="height:52px;border-radius:8px;background:{L if k < 40 else F}"></div>' for k in range(52))
    s6 = sl(6, f"""<div class="abs" style="left:80px;right:80px;top:200px"><div class="lab" style="color:{L}">52 semanas</div>
        <div style="display:grid;grid-template-columns:repeat(13,1fr);gap:8px;margin-top:24px">{sem}</div>
        <div class="c" style="font-size:136px;line-height:.92;margin-top:60px">Constância com método vence <span class="lar">intensidade sem direção.</span></div></div>""")
    s7 = cta("Habito", "preto", f'<div class="top">{logo("cor-fundo-escuro")}<div class="lab" style="color:{C}">7 / {n}</div></div>', 210, "Salve e mande pra quem começa forte e para no mês 2")
    salvar("2026-11-22_habitos-atomicos", [s1, s2, s3, s4, s5, s6, s7])

if __name__ == "__main__":
    for f in (seg_player, ter_pare, qua_raiox, qui_ingresso, sex_mito, sab_recibo, dom_calendario):
        f()
    print("ok")
