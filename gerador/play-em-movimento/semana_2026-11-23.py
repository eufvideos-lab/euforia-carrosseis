#!/usr/bin/env python3
"""Semana 23 a 29/11/2026 nos modelos Play em Movimento.
Uso: python3 semana_2026-11-23.py  -> grava carrosseis/<pasta>/slides.html; depois render_post.js."""
import os, sys, glob
AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
sys.path.insert(0, AQUI)
antes = set(glob.glob(os.path.join(AQUI, "modelo-*.html")))
import gerar as g   # os imports rodam os exemplos; os HTML gerados são apagados abaixo
import gerar2 as g2
from gerar import sym, bar, logo, manchete_chrome, claquete
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

# ───────── SEG 23/11 · carrossel · MANCHETE · Instagram 90 minutos ─────────
def seg_manchete():
    n = 7; bg = "background:#F2EFEA;color:#050505"
    def sl(i, html, pe=None):
        return f'<div class="slide" style="{bg}">{manchete_chrome(i, n, pe or f"Continua na página {i+1}")}{html}</div>'
    s1 = sl(1, f"""<div class="abs" style="left:80px;right:80px;top:214px">
        <span class="lab" style="background:#FF6518;padding:10px 16px 8px;display:inline-block">Notícia</span>
        <div class="c" style="font-size:196px;margin-top:34px">O Instagram<br>agora tem<br><span style="color:#C2410C">90 minutos.</span></div>
        <div class="t" style="margin-top:44px;font-size:42px;max-width:880px;font-weight:600">O teste de vídeos longos do Instagram começou pelo Brasil.</div>
      </div>""")
    itens = [("Features", "Vídeos horizontais de até 90 minutos dentro do Instagram."),
             ("Onde", "O teste começou no Brasil e está chegando a um grupo pequeno de criadores nos EUA."),
             ("Clips as Reels", "Até 8 Reels curtos ligados ao vídeo longo, levando quem assiste até ele.")]
    rows = ""
    for k, (a, b) in enumerate(itens):
        rows += f"""<div style="display:grid;grid-template-columns:150px 1fr;gap:10px;padding:30px 0;border-top:2px solid #050505;align-items:start">
          <div class="c" style="font-size:150px;color:#FF6518;line-height:.8">{k+1}</div>
          <div><div class="x" style="font-size:50px">{a}</div><div class="t" style="margin-top:14px;font-size:34px;color:#3a3531">{b}</div></div></div>"""
    s2 = sl(2, f"""<div class="abs" style="left:80px;right:80px;top:214px">
        <div class="lab" style="color:#C2410C">O que foi anunciado</div>
        <div class="x" style="font-size:62px;margin-top:20px">Dois testes, anunciados em 26 de outubro</div>
        <div style="margin-top:40px;border-bottom:2px solid #050505">{rows}</div></div>""")
    s3 = sl(3, f"""<div class="abs" style="left:80px;right:80px;top:230px">
        <div class="c" style="font-size:300px;color:#FF6518;line-height:.7">“</div>
        <div class="c" style="font-size:120px;line-height:.92;margin-top:-20px">Por muito tempo, fui contra vídeo longo no Instagram.</div>
        <div class="lab" style="margin-top:50px">Adam Mosseri, chefe do Instagram</div>
        <div class="t" style="margin-top:20px;font-size:34px;color:#3a3531;max-width:860px">Agora o próprio Instagram está abrindo espaço para ele.</div></div>""")
    s4 = sl(4, f"""<div class="abs" style="left:80px;right:80px;top:214px">
        <div class="lab" style="color:#C2410C">A nossa leitura</div>
        <div class="x" style="font-size:84px;margin-top:24px">O vídeo longo voltou ao <span style="color:#C2410C">centro.</span></div>
        <div class="t" style="margin-top:40px;font-size:40px;max-width:880px">O YouTube já vivia disso. Agora o Instagram também quer que as pessoas fiquem mais tempo assistindo quem elas confiam.</div>
        <div class="t" style="margin-top:30px;font-size:40px;max-width:880px;font-weight:800">Quem explica bem o que faz sai na frente.</div></div>""")
    pts = [("Vídeo longo", "É onde a confiança nasce. A pessoa passa minutos com você antes de falar com você."),
           ("Cortes", "Levam gente nova até o vídeo longo, em todas as redes."),
           ("Constância", "Um vídeo por semana, sem falhar, vale mais que um mês de posts soltos.")]
    rows2 = ""
    for k, (a, b) in enumerate(pts):
        rows2 += f"""<div style="display:grid;grid-template-columns:150px 1fr;gap:10px;padding:30px 0;border-top:2px solid #050505;align-items:start">
          <div class="c" style="font-size:150px;color:#FF6518;line-height:.8">{k+1}</div>
          <div><div class="x" style="font-size:50px">{a}</div><div class="t" style="margin-top:14px;font-size:34px;color:#3a3531">{b}</div></div></div>"""
    s5 = sl(5, f"""<div class="abs" style="left:80px;right:80px;top:214px">
        <div class="lab" style="color:#C2410C">Para quem ensina o que sabe</div>
        <div class="x" style="font-size:62px;margin-top:20px">O que isso muda no seu negócio</div>
        <div style="margin-top:40px;border-bottom:2px solid #050505">{rows2}</div></div>""")
    s6 = sl(6, f"""<div class="abs" style="left:80px;right:80px;top:250px">
        <div class="c" style="font-size:150px;line-height:.92">Grava uma vez.</div>
        <div class="c" style="font-size:150px;line-height:1.02;margin-top:30px"><span style="background:#FF6518;box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:6px 14px 0;margin-left:-14px">Aparece em todo lugar.</span></div>
        <div class="t" style="margin-top:56px;font-size:38px;max-width:860px;color:#3a3531">É assim que funciona um ecossistema digital: um vídeo vira vários formatos, em todas as redes.</div></div>""")
    s7 = f"""<div class="slide" style="{bg}">{manchete_chrome(7, n, 'Fontes: Variety e The Next Web')}
      <div class="abs" style="left:80px;right:80px;top:214px">
        <div class="lab" style="color:#C2410C">Serviço</div>
        <div class="x" style="font-size:74px;margin-top:20px">Agende um {RX} gratuito com a nossa equipe.</div>
        <div class="box" style="margin-top:54px;background:#050505;border-color:#050505;color:#FF6518"><div class="lab" style="color:#F2EFEA">Comente</div><div class="x" style="font-size:150px">Longo</div></div>
        <div class="t" style="margin-top:36px;font-size:32px;color:#3a3531">A gente te manda o link no direct. <b style="color:#050505">Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>
      </div></div>"""
    salvar("2026-11-23_instagram-90-minutos", [s1, s2, s3, s4, s5, s6, s7])

# ───────── TER 24/11 · post único · NOTIFICAÇÃO ─────────
def ter_notificacao():
    def notif(titulo, txt, quando, op=1, esc=1):
        return f"""<div style="background:{F};border-radius:34px;padding:30px 34px;display:grid;grid-template-columns:84px 1fr;gap:24px;align-items:center;opacity:{op};transform:scale({esc});transform-origin:top center">
          <div style="width:84px;height:84px;border-radius:22px;background:{L};display:grid;place-items:center">{bar(P, 50, 20)}</div>
          <div><div style="display:flex;justify-content:space-between;font-size:26px;color:{C};font-weight:600"><span>{titulo}</span><span>{quando}</span></div>
          <div style="font-size:35px;font-weight:600;line-height:1.25;margin-top:6px;color:{O}">{txt}</div></div></div>"""
    s1 = f"""<div class="slide" style="background:{G};color:{O}">
      <div class="abs lab" style="left:0;right:0;top:84px;text-align:center;color:{C}">Tela ilustrativa</div>
      <div class="abs c" style="left:0;right:0;top:120px;text-align:center;font-size:330px">09:41</div>
      <div class="abs" style="left:70px;right:70px;top:450px;display:flex;flex-direction:column;gap:18px">
        {notif('Mensagem nova', 'Assisti o seu vídeo inteiro. Quero agendar.', 'agora')}
        {notif('Mensagem nova', 'Te achei pesquisando no Google. Atende online?', '4 min', .75, .95)}
        {notif('Mensagem nova', 'Um amigo me mandou o seu vídeo.', '12 min', .4, .9)}
      </div>
      <div class="abs" style="left:80px;right:80px;bottom:84px"><div class="x" style="font-size:92px">E se o cliente chegasse <span class="lar">assim?</span></div></div></div>"""
    salvar("2026-11-24_notificacao-cliente", [s1])

# ───────── QUA 25/11 · carrossel · PLACAR · Gary Vaynerchuk ─────────
def qua_placar():
    n = 7
    dados = [("14 anos", "o primeiro emprego"), ("2006", "o vídeo diário"), ("US$ 60 mi", "vendas por ano")]
    def chrome(ativo, i):
        cels = ""
        for k, (v, l) in enumerate(dados):
            on = k == ativo
            st = "background:#FF6518;color:#050505;border-color:#FF6518" if on else "color:#8a827a;border-color:#3a3531"
            cels += f'<div style="flex:1;border:3px solid;border-radius:14px;padding:18px 20px 16px;{st}"><div class="c" style="font-size:54px;white-space:nowrap">{v}</div><div style="font-size:19px;font-weight:600;margin-top:8px;line-height:1.2">{l}</div></div>'
        return f"""<div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:#8a827a">História de empresário · {i} / {n}</div></div>
        <div class="abs" style="left:80px;right:80px;bottom:72px;display:flex;gap:14px">{cels}</div>"""
    def sl(ativo, i, html): return f'<div class="slide" style="background:#050505;color:#F2EFEA">{chrome(ativo, i)}{html}</div>'
    def num(ativo, i, pre, grande, pos, linha, apoio, tam=455):
        pre_h = f'<div class="c" style="font-size:130px;color:#F2EFEA;margin-bottom:-6px">{pre}</div>' if pre else ""
        pos_h = f'<span style="font-size:.42em;color:#F2EFEA;margin-left:14px">{pos}</span>' if pos else ""
        return sl(ativo, i, f"""<div class="abs" style="left:76px;right:60px;top:190px">{pre_h}
            <div class="c" style="font-size:{tam}px;color:#FF6518;white-space:nowrap">{grande}{pos_h}</div>
            <div class="x" style="font-size:54px;margin-top:34px;max-width:900px">{linha}</div>
            <div class="t" style="margin-top:22px;font-size:34px;color:#cfc8bf;max-width:860px">{apoio}</div></div>""")
    s1 = sl(-1, 1, f"""<div class="abs" style="left:80px;right:80px;top:200px">
        <div class="lab" style="background:#FF6518;color:#050505;padding:10px 16px 8px;display:inline-block">Gary Vaynerchuk</div>
        <div class="c" style="font-size:250px;margin-top:40px">Um vídeo<br>por dia.</div>
        <div class="x" style="font-size:72px;margin-top:20px;color:#FF6518">Cinco anos seguidos.</div>
        <div class="t" style="margin-top:30px;color:#cfc8bf;max-width:860px">E a loja de vinhos da família que foi junto.</div></div>""")
    s2 = num(0, 2, "Aos", "14", "anos", "Ensacando gelo na loja do pai", "Por US$ 2 a hora, segundo a biografia oficial dele. O negócio da família vendia vinhos e bebidas em Nova Jersey.")
    s3 = num(-1, 3, "", "1996", "", "A loja vira Wine Library e passa a vender pela internet", "Uma das primeiras lojas de bebidas a vender online nos Estados Unidos.", 400)
    s4 = num(1, 4, "", "2006", "", "Começa o Wine Library TV, no YouTube", "Um programa diário sobre vinho. Ele gravou um episódio quase todo dia, por cinco anos.", 400)
    s5 = num(2, 5, "De US$ 4 para", "60", "mi", "Em vendas por ano", "Na gestão dele, segundo a própria biografia. A venda online e o vídeo diário fizeram parte dessa virada.")
    s6 = sl(-1, 6, f"""<div class="abs" style="left:80px;right:80px;top:210px">
        <div class="lab" style="color:#8a827a">A lição</div>
        <div class="x" style="font-size:86px;margin-top:24px">Ele não esperou o estúdio perfeito. <span class="lar">Apareceu todo dia.</span></div>
        <div class="t" style="margin-top:40px;color:#cfc8bf;max-width:880px">Quem assiste você explicando o que sabe chega na primeira conversa já confiando.</div></div>""")
    s7 = cta("Video", "preto", chrome(-1, 7), 200, "Fonte: biografia oficial em garyvaynerchuk.com")
    salvar("2026-11-25_gary-vaynerchuk", [s1, s2, s3, s4, s5, s6, s7])

# ───────── QUI 26/11 · post único · ECO ─────────
def qui_eco():
    linhas = ""
    for cor in [A, "#b0a89c", "#6f6861"]:
        linhas += f'<div class="c" style="font-size:236px;color:transparent;-webkit-text-stroke:3px {cor};line-height:.88">Invisível</div>'
    s1 = f"""<div class="slide" style="background:{O};color:{P}">
      <div class="top">{logo('cor-fundo-claro')}<div class="lab" style="opacity:.6">Grupo Euforia</div></div>
      <div class="abs" style="left:76px;top:190px">{linhas}
        <div style="position:relative;display:inline-block"><div class="c" style="font-size:236px;line-height:.88">Invisível</div>
        <div class="abs" style="left:-34px;top:36%;width:236px;transform:rotate(-8deg)">{bar(L, 236, 52)}</div></div>
      </div>
      <div class="abs" style="left:80px;right:80px;bottom:80px;font-size:44px;font-weight:700;line-height:1.2">Referência no offline.<br>E na internet, quem te encontra?</div></div>"""
    salvar("2026-11-26_invisivel", [s1])

# ───────── SEX 27/11 · carrossel · CHECKLIST · 6 sinais ─────────
def sex_checklist():
    n = 6
    def caixa(on=False, t=62):
        dentro = f'<div class="abs" style="left:8px;top:{t*0.28}px;transform:rotate(-38deg)">{bar(L, t*1.25, t*0.4)}</div>' if on else ""
        return f'<div style="width:{t}px;height:{t}px;border:6px solid {P};border-radius:12px;position:relative;flex:none">{dentro}</div>'
    clip = f'<div class="abs" style="left:50%;top:-46px;margin-left:-150px;width:300px;height:110px;background:{P};border-radius:22px"></div><div class="abs" style="left:50%;top:-70px;margin-left:-50px;width:100px;height:70px;border:16px solid {P};border-bottom:0;border-radius:40px 40px 0 0"></div>'
    falsas = "".join(f'<div style="display:flex;gap:26px;align-items:center;margin-top:24px">{caixa(k == 0, 70)}<div style="height:30px;border-radius:15px;background:{A if k else P};width:{w}px"></div></div>' for k, w in enumerate([470, 400, 520, 360, 440]))
    s1 = f"""<div class="slide" style="background:{L};color:{P}">
      <div class="abs" style="left:110px;top:130px;width:860px;height:1040px;background:{O};border-radius:26px;transform:rotate(3deg);padding:104px 70px 0">{clip}
        <div class="c" style="font-size:104px;line-height:.92">6 sinais de que o seu digital está te custando clientes</div>{falsas}</div>
      <div class="abs" style="left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;align-items:center">{logo('mono-preto')}<div style="display:flex;align-items:center;gap:18px"><div class="lab">Confira os seus</div>{bar(P, 110, 30)}</div></div></div>"""
    def prancheta(i, titulo, html, rodape=""):
        rod = f'<div style="font-size:42px;font-weight:700;margin-top:44px;color:#3a3531">{rodape}</div>' if rodape else ""
        return f"""<div class="slide" style="background:{L};color:{P}">
          <div class="abs" style="left:60px;top:110px;width:960px;height:1180px;background:{O};border-radius:26px;padding:100px 60px 0">{clip}
            <div class="lab" style="color:{B}">{i} / {n} · {titulo}</div>{html}{rod}</div></div>"""
    def checks(sinais, ini):
        linhas = "".join(f'<div style="display:flex;gap:26px;align-items:center;padding:56px 0;border-top:3px solid {A}">{caixa(True, 76)}<div><div class="lab" style="color:{C};font-size:22px">Sinal {ini+k}</div><div style="font-size:54px;font-weight:700;line-height:1.2;margin-top:6px">{s}</div></div></div>' for k, s in enumerate(sinais))
        return f'<div style="margin-top:22px;border-bottom:3px solid {A}">{linhas}</div>'
    s2 = prancheta(2, "Marque os que são seus", checks(["Quem pesquisa o seu nome encontra pouco ou nada", "O seu último vídeo tem mais de um mês", "Os clientes novos chegam quase só por indicação"], 1))
    s3 = prancheta(3, "Continue marcando", checks(["Você explica a mesma coisa em toda primeira conversa", "O seu perfil mostra o que você faz, mas não como você pensa", "Quem chega já chega comparando preço"], 4))
    s4 = prancheta(4, "O que eles têm em comum", f"""<div class="c" style="font-size:150px;line-height:.96;margin-top:40px">O cliente decide <span style="color:{B}">antes</span> de falar com você.</div>
        <div style="font-size:44px;font-weight:600;line-height:1.3;margin-top:40px;color:#3a3531">Se ele não te encontra, ou encontra pouco, a decisão vai para outro. Mesmo que o seu trabalho seja melhor.</div>""")
    s5 = prancheta(5, "Por onde começar", f'<div style="margin-top:30px">{lista(["Responda em vídeo as perguntas que você mais ouve", "Escolha uma base e seja constante nela", "Distribua os cortes onde o seu cliente está"], B, P, A, 54, 56)}</div>',
                   "Marcou dois ou mais? Vale olhar isso de perto.")
    s6 = cta("Sinais", "laranja", f'<div class="top">{logo("mono-preto")}<div class="lab" style="opacity:.7">6 / 6</div></div>', 210, "Salve e mande pra quem precisa conferir")
    salvar("2026-11-27_seis-sinais", [s1, s2, s3, s4, s5, s6])

# ───────── SÁB 28/11 · post único · REC ─────────
def sab_rec():
    grade = f'<div class="abs" style="left:33.33%;top:60px;bottom:60px;width:2px;background:{F}"></div><div class="abs" style="left:66.66%;top:60px;bottom:60px;width:2px;background:{F}"></div><div class="abs" style="top:33.33%;left:60px;right:60px;height:2px;background:{F}"></div><div class="abs" style="top:66.66%;left:60px;right:60px;height:2px;background:{F}"></div>'
    bat = f'<div style="width:74px;height:34px;border:4px solid {O};border-radius:8px;padding:4px;position:relative"><div style="height:100%;width:70%;background:{O};border-radius:2px"></div><div class="abs" style="right:-10px;top:8px;width:6px;height:10px;background:{O};border-radius:0 3px 3px 0"></div></div>'
    s1 = f"""<div class="slide" style="background:{P};color:{O}">{grade}{cantos(O)}
      <div class="abs" style="left:110px;top:100px;display:flex;align-items:center;gap:16px"><div style="width:30px;height:30px;border-radius:50%;background:{L}"></div><div class="c" style="font-size:56px;color:{L}">Rec</div><div class="c" style="font-size:56px;margin-left:14px">00:00:00</div></div>
      <div class="abs" style="right:110px;top:108px">{bat}</div>
      <div class="abs" style="left:50%;top:50%;width:90px;height:90px;margin:-45px 0 0 -45px"><div class="abs" style="left:43px;top:0;bottom:0;width:4px;background:{O}"></div><div class="abs" style="top:43px;left:0;right:0;height:4px;background:{O}"></div></div>
      <div class="abs" style="left:110px;right:110px;top:250px"><div class="x" style="font-size:100px">Vergonha<br>de <span class="lar">câmera?</span></div></div>
      <div class="abs" style="left:110px;right:110px;bottom:230px;font-size:44px;font-weight:700;line-height:1.2">Você fala bem em reunião.<br>E trava quando a câmera liga.</div>
      <div class="abs" style="left:110px;right:110px;bottom:104px;display:flex;justify-content:space-between"><div class="lab" style="background:{O};color:{P};padding:10px 14px 8px">Roteiro: pronto</div><div class="lab" style="color:{C};padding:10px 0">Tomada 01</div></div></div>"""
    salvar("2026-11-28_vergonha-camera", [s1])

# ───────── DOM 29/11 · carrossel · ROTEIRO · Mostre seu trabalho ─────────
def dom_roteiro():
    n = 5
    def cena(k, titulo, quem, texto, voce=False):
        cor = "#FF6518" if voce else "#050505"; tx = "#050505" if voce else "#F2EFEA"
        return f"""<div style="padding:50px 0 54px;border-bottom:3px solid #050505">
          <div style="display:flex;justify-content:space-between;align-items:center;gap:20px">
            <div class="c" style="font-size:84px">{titulo}</div>
            <div class="lab" style="background:{cor};color:{tx};padding:10px 16px 8px;font-size:19px;white-space:nowrap;flex:none">{quem}</div></div>
          <div class="t" style="margin-top:24px;font-size:40px;color:#2a2622;max-width:880px">{texto}</div></div>"""
    s1 = f"""<div class="slide" style="background:#FF6518;color:#050505">{claquete('#050505', '#F2EFEA', 'Livro', f'1 de {n}', '#050505')}
      <div class="abs" style="left:80px;right:80px;top:330px">
        <div class="lab">Austin Kleon · 2014</div>
        <div class="x" style="font-size:118px;margin-top:30px">Mostre<br>seu<br>trabalho!</div>
        <div class="t" style="margin-top:36px;font-size:40px;font-weight:600;max-width:900px">O livro tem 10 regras para ser encontrado. Separamos 4.</div>
      </div>
      <div class="abs" style="left:80px;right:80px;bottom:76px;display:flex;justify-content:space-between;align-items:center">{logo('mono-preto')}<div style="display:flex;align-items:center;gap:18px"><div class="lab">Arraste</div>{bar('#050505', 110, 30)}</div></div>
      </div>"""
    s2 = f"""<div class="slide" style="background:#F2EFEA;color:#050505">{claquete('#050505', '#FF6518', 'Regras', f'2 de {n}', '#050505')}
      <div class="abs" style="left:80px;right:80px;top:270px">
        {cena(1, 'Você não precisa ser um gênio', 'Regra 1', 'Ninguém espera perfeição. Quem mostra o caminho, com acertos e erros, gera mais confiança do que quem só mostra o resultado.')}
        {cena(3, 'Algo pequeno todo dia', 'Regra 3', 'Uma dica, um bastidor, uma dúvida respondida. O que você mostra com frequência vale mais que um portfólio parado.')}
      </div>
      <div class="abs lab" style="left:80px;bottom:76px;color:#8a827a">Corta para: mais duas regras</div></div>"""
    s3 = f"""<div class="slide" style="background:#F2EFEA;color:#050505">{claquete('#050505', '#FF6518', 'Regras', f'3 de {n}', '#050505')}
      <div class="abs" style="left:80px;right:80px;top:270px">
        {cena(6, 'Ensine o que você sabe', 'Regra 6', 'Ensinar não tira cliente. Mostra que você domina o assunto e faz a pessoa querer você do lado dela.')}
        {cena(10, 'Não pare', 'Regra 10', 'Quem continua aparecendo, mês após mês, é quem fica na memória quando a necessidade chega.')}
      </div>
      <div class="abs lab" style="left:80px;bottom:76px;color:#8a827a">Corta para: o seu negócio</div></div>"""
    s4 = f"""<div class="slide" style="background:#F2EFEA;color:#050505">{claquete('#050505', '#FF6518', 'Na prática', f'4 de {n}', '#050505')}
      <div class="abs" style="left:80px;right:80px;top:270px">
        {cena(0, 'Gravar', 'Você', 'Um vídeo por semana, com roteiro na mão, falando do que você já explica todo dia.', True)}
        {cena(0, 'Todo o resto', 'Nossa equipe', 'Edição, cortes, publicação em todas as redes e o relatório do mês.')}
      </div>
      <div class="abs lab" style="left:80px;bottom:76px;color:#8a827a">Corta para: a sua cena</div></div>"""
    s5 = f"""<div class="slide" style="background:#050505;color:#F2EFEA">{claquete('#FF6518', '#050505', 'A sua', f'5 de {n}', '#F2EFEA')}
      <div class="abs" style="left:80px;right:80px;top:320px">
        <div class="x" style="font-size:76px">Agende um <span class="lar">{RX} gratuito</span> com a nossa equipe.</div>
        <div class="box" style="margin-top:54px;color:#FF6518"><div class="lab" style="color:#F2EFEA">Comente</div><div class="x" style="font-size:130px">Mostre</div></div>
        <div class="t" style="margin-top:36px;font-size:32px;color:#cfc8bf">A gente te manda o link no direct. <b style="color:#F2EFEA">Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>
      </div></div>"""
    salvar("2026-11-29_mostre-seu-trabalho", [s1, s2, s3, s4, s5])

for f in (seg_manchete, ter_notificacao, qua_placar, qui_eco, sex_checklist, sab_rec, dom_roteiro):
    f()
print("ok")
