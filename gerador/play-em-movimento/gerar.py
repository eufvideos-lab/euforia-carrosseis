#!/usr/bin/env python3
"""Gera os 5 modelos de carrossel da proposta "Play em movimento" (1080x1350).
Uso: python3 gerar.py  -> escreve modelo-*.html nesta pasta; depois: node foto.js
Para um carrossel novo, copie o bloco do modelo e troque só os textos."""
import os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
# Archivo variável: usa a cópia ao lado deste arquivo, senão a da pasta do projeto
ARCHIVO = next((p for p in (os.path.join(AQUI, "Archivo.ttf"), os.path.join(AQUI, "..", "container", "Archivo.ttf"), "/mnt/project-files/dossie/thumb-materiais/Archivo.ttf") if os.path.exists(p)), "Archivo.ttf")
SYM = "M15,0L79.28,0A8,8 0 0 1 83.77,1.38L106.08,16.5A7.39,7.39 0 0 1 101.94,30L15,30A15,15 0 0 1 15,0Z M15,46L125.41,46A8,8 0 0 1 129.9,47.38L140.23,54.38A8,8 0 0 1 140.23,67.62L129.9,74.62A8,8 0 0 1 125.41,76L15,76A15,15 0 0 1 15,46Z M15,92L101.94,92A7.39,7.39 0 0 1 106.08,105.5L83.77,120.62A8,8 0 0 1 79.28,122L15,122A15,15 0 0 1 15,92Z"
# só a barra do meio (a que tem a ponta de play): vira risco, cursor e marcador
BAR = "M15,0L125.41,0A8,8 0 0 1 129.9,1.38L140.23,8.38A8,8 0 0 1 140.23,21.62L129.9,28.62A8,8 0 0 1 125.41,30L15,30A15,15 0 0 1 15,0Z"

def sym(cor, w, extra=""):
    return f'<svg class="sym" style="width:{w}px;{extra}" viewBox="0 0 146 122"><path fill="{cor}" d="{SYM}"/></svg>'

def bar(cor, w, h=None, extra=""):
    # barra esticável: preserveAspectRatio none permite alongar sem mudar a altura
    hh = f"height:{h}px;" if h else ""
    return f'<svg class="bar" style="width:{w}px;{hh}{extra}" viewBox="0 0 146 30" preserveAspectRatio="none"><path fill="{cor}" d="{BAR}"/></svg>'

def logo(nome, h=46):
    s = open(os.path.join(AQUI, f"horizontal-{nome}.svg")).read()
    return s.replace("<svg ", f'<svg class="logo" style="height:{h}px" ', 1)

CSS = f"""
@font-face{{font-family:Archivo;src:url(file://{ARCHIVO});font-weight:100 900;font-stretch:62% 125%}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#333;display:flex;gap:24px;padding:24px;width:max-content}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Inter,sans-serif;flex:none;
  --preto:#050505;--grafite:#141312;--fumaca:#26221F;--off:#F2EFEA;--areia:#DDD6CB;--lar:#FF6518;--brasa:#C2410C}}
.x{{font-family:Archivo;font-weight:800;font-stretch:125%;text-transform:uppercase;line-height:.94;letter-spacing:-.012em}}
.c{{font-family:Archivo;font-weight:800;font-stretch:62%;text-transform:uppercase;line-height:.84;letter-spacing:-.005em}}
.lab{{font-family:Archivo;font-weight:700;font-stretch:100%;text-transform:uppercase;letter-spacing:.16em;font-size:22px;line-height:1.2}}
.t{{font-size:38px;line-height:1.32;font-weight:500}}
.abs{{position:absolute}} svg{{display:block}} b{{font-weight:800}}
.top{{position:absolute;left:80px;right:80px;top:72px;display:flex;justify-content:space-between;align-items:center}}
.lar{{color:#FF6518}}
/* CTA comum */
.box{{border:3px solid currentColor;border-radius:18px;padding:30px 40px 34px;display:flex;flex-direction:column;gap:6px}}
"""

def page(nome, slides):
    html = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>' + "".join(slides)
    open(os.path.join(AQUI, f"{nome}.html"), "w").write(html)

# ───────────────────────── MODELO 1 · PLAYER ─────────────────────────
def player_chrome(i, n, cap, prox):
    segs = ""
    for k in range(1, n + 1):
        cor = "#FF6518" if k <= i else "#26221F"
        segs += f'<div style="flex:1;height:12px;border-radius:6px;background:{cor}"></div>'
    # cursor: a barra com ponta de play, na posição do capítulo
    x = 80 + (920 * i / n) - 46
    return f"""
    <div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:#8a827a">Capítulo {i} de {n}</div></div>
    <div class="abs" style="left:80px;right:80px;bottom:150px;display:flex;gap:10px">{segs}</div>
    <div class="abs" style="left:{x}px;bottom:134px">{bar('#F2EFEA', 64, 44)}</div>
    <div class="abs" style="left:80px;right:80px;bottom:72px;display:flex;justify-content:space-between;align-items:baseline">
      <div class="lab" style="color:#F2EFEA">{cap}</div><div class="lab" style="color:#8a827a">{prox}</div></div>"""

def m_player():
    bg = "background:#141312;color:#F2EFEA"
    s1 = f"""<div class="slide" style="{bg}">
      <div class="abs" style="right:-190px;top:176px">{sym('#FF6518', 690)}</div>
      {player_chrome(1, 4, 'Abertura', 'A seguir: a gravação')}
      <div class="abs" style="left:80px;right:80px;bottom:250px">
        <div class="x" style="font-size:98px">Você grava<br>uma vez.</div>
        <div class="t" style="margin-top:28px;max-width:760px;color:#cfc8bf">E aparece em todo lugar. O caminho de um vídeo dentro do ecossistema digital.</div>
      </div></div>"""
    s2 = f"""<div class="slide" style="{bg}">
      {player_chrome(2, 4, 'A gravação', 'A seguir: a equipe')}
      <div class="abs c" style="left:70px;top:230px;font-size:430px;color:transparent;-webkit-text-stroke:4px #FF6518">01</div>
      <div class="abs" style="left:80px;right:80px;top:660px">
        <div class="x" style="font-size:98px">Você só<br><span class="lar">grava.</span></div>
        <div class="t" style="margin-top:36px;max-width:820px;color:#cfc8bf">Você chega com o que já sabe. A estratégia e o roteiro já vêm prontos da nossa equipe.</div>
      </div></div>"""
    trilhas = [("Estratégia", 300), ("Roteiro", 420), ("Produção", 540), ("Edição", 660), ("Publicação", 780), ("Relatório", 900)]
    tr = ""
    for k, (nome, w) in enumerate(trilhas):
        cor = "#FF6518" if k % 2 == 0 else "#F2EFEA"
        tr += f'<div style="position:relative;height:54px">{bar(cor, w, 54)}<div class="lab abs" style="left:26px;top:13px;color:#050505;font-size:23px">{nome}</div></div>'
    s3 = f"""<div class="slide" style="{bg}">
      {player_chrome(3, 4, 'A equipe', 'A seguir: o seu play')}
      <div class="abs" style="left:80px;right:80px;top:200px">
        <div class="x" style="font-size:98px">A equipe<br>faz o <span class="lar">resto.</span></div></div>
      <div class="abs" style="left:80px;top:500px;display:flex;flex-direction:column;gap:20px">{tr}</div>
      <div class="abs t" style="left:80px;right:80px;top:960px;color:#cfc8bf;max-width:840px">Seis frentes rodando ao mesmo tempo, enquanto você cuida do seu negócio.</div>
      </div>"""
    s4 = f"""<div class="slide" style="{bg}">
      {player_chrome(4, 4, 'O seu play', 'Fim')}
      <div class="abs" style="left:80px;right:80px;top:200px">
        <div class="x" style="font-size:76px">Agende um <span class="lar"><span style="white-space:nowrap">Raio-X</span> gratuito</span> com os nossos consultores.</div>
        <div class="box" style="margin-top:56px;color:#FF6518"><div class="lab" style="color:#F2EFEA">Comente</div><div class="x" style="font-size:120px">Roteiro</div></div>
        <div class="t" style="margin-top:36px;font-size:32px;color:#cfc8bf">A gente te manda o link no direct. <b style="color:#F2EFEA">Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>
      </div></div>"""
    page("modelo-1-player", [s1, s2, s3, s4])

# ───────────────────────── MODELO 2 · MANCHETE ─────────────────────────
def manchete_chrome(i, n, pe):
    return f"""
    <div class="abs" style="left:80px;right:80px;top:64px;height:8px;background:#050505"></div>
    <div class="abs" style="left:80px;right:80px;top:96px;display:flex;justify-content:space-between;align-items:center">{logo('cor-fundo-claro', 42)}<div class="lab" style="font-size:20px">Caderno de negócios</div></div>
    <div class="abs" style="left:80px;right:80px;top:162px;height:2px;background:#050505"></div>
    <div class="abs" style="left:80px;right:80px;bottom:112px;height:2px;background:#050505"></div>
    <div class="abs" style="left:80px;right:80px;bottom:64px;display:flex;justify-content:space-between;align-items:center">
      <div class="lab" style="font-size:20px">{pe}</div><div class="lab" style="font-size:20px">Página {i} de {n}</div></div>"""

def m_manchete():
    bg = "background:#F2EFEA;color:#050505"
    s1 = f"""<div class="slide" style="{bg}">{manchete_chrome(1, 4, 'Continua na página 2')}
      <div class="abs" style="left:80px;right:80px;top:214px">
        <span class="lab" style="background:#FF6518;padding:10px 16px 8px;display:inline-block">Análise</span>
        <div class="c" style="font-size:222px;margin-top:34px">O anúncio<br>parou.<br><span style="color:#C2410C">E agora?</span></div>
        <div class="t" style="margin-top:44px;font-size:42px;max-width:860px;font-weight:600">Quando o anúncio para, o conteúdo continua trabalhando.</div>
      </div></div>"""
    bases = [("Conteúdo", "Um ativo que continua sendo achado, assistido e compartilhado."),
             ("Estratégia", "Cada peça com uma função. Comprador, não curioso."),
             ("Relacionamento", "Audiência vira conversa. Conversa vira cliente.")]
    rows = ""
    for k, (a, b) in enumerate(bases):
        rows += f"""<div style="display:grid;grid-template-columns:150px 1fr;gap:10px;padding:34px 0;border-top:2px solid #050505;align-items:start">
          <div class="c" style="font-size:150px;color:#FF6518;line-height:.8">{k+1}</div>
          <div><div class="x" style="font-size:50px">{a}</div><div class="t" style="margin-top:14px;font-size:34px;color:#3a3531">{b}</div></div></div>"""
    s2 = f"""<div class="slide" style="{bg}">{manchete_chrome(2, 4, 'Continua na página 3')}
      <div class="abs" style="left:80px;right:80px;top:214px">
        <div class="lab" style="color:#C2410C">A nossa leitura</div>
        <div class="x" style="font-size:66px;margin-top:20px">Resultado se constrói em três bases</div>
        <div style="margin-top:44px;border-bottom:2px solid #050505">{rows}</div>
      </div></div>"""
    s3 = f"""<div class="slide" style="{bg}">{manchete_chrome(3, 4, 'Continua na página 4')}
      <div class="abs" style="left:80px;right:80px;top:230px">
        <div class="c" style="font-size:128px;line-height:.92">O anúncio acelera o que já funciona.</div>
        <div class="c" style="font-size:128px;line-height:1.02;margin-top:30px"><span style="background:#FF6518;box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:6px 14px 0;margin-left:-14px">A gente constrói o que funciona.</span></div>
        <div class="t" style="margin-top:56px;font-size:36px;max-width:820px;color:#3a3531">Não somos contra o anúncio. Ele é complemento e bônus, nunca a base.</div>
      </div></div>"""
    s4 = f"""<div class="slide" style="{bg}">{manchete_chrome(4, 4, '@euforiagrupo')}
      <div class="abs" style="left:80px;right:80px;top:214px">
        <div class="lab" style="color:#C2410C">Serviço</div>
        <div class="x" style="font-size:74px;margin-top:20px">Agende um <span style="white-space:nowrap">Raio-X</span> gratuito com os nossos consultores.</div>
        <div class="box" style="margin-top:54px;background:#050505;border-color:#050505;color:#FF6518"><div class="lab" style="color:#F2EFEA">Comente</div><div class="x" style="font-size:150px">Base</div></div>
        <div class="t" style="margin-top:36px;font-size:32px;color:#3a3531">A gente te manda o link no direct. <b style="color:#050505">Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>
      </div></div>"""
    page("modelo-2-manchete", [s1, s2, s3, s4])

# ───────────────────────── MODELO 3 · MITO × FATO ─────────────────────────
def m_mito():
    def par(i, n, mito, fato, apoio):
        return f"""<div class="slide" style="background:#050505;color:#F2EFEA">
          <div class="abs" style="left:0;right:0;top:0;height:560px;padding:72px 80px 0">
            <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab" style="color:#8a827a">Mito {i:02d}</div><div class="lab" style="color:#8a827a">{i+1} / {n}</div></div>
            <div style="position:relative;margin-top:60px;display:inline-block">
              <div class="x" style="font-size:78px;color:#6f6861">{mito}</div>
              <div class="abs" style="left:-24px;right:-40px;top:50%;margin-top:-22px;transform:rotate(-7deg)">{bar('#FF6518', '100%', 44, 'width:100%')}</div>
            </div>
          </div>
          <div class="abs" style="left:0;right:0;top:560px;bottom:0;background:#FF6518;color:#050505;padding:64px 80px 0">
            <div class="c abs" style="right:60px;top:-92px;font-size:190px;color:#050505;background:#FF6518;padding:22px 26px 0;border-radius:14px 14px 0 0;line-height:.8">Fato</div>
            <div class="x" style="font-size:80px;margin-top:70px">{fato}</div>
            <div class="t" style="margin-top:34px;font-size:36px;font-weight:600;max-width:860px">{apoio}</div>
            <div class="abs" style="left:80px;bottom:72px">{logo('mono-preto', 42)}</div>
          </div></div>"""
    s1 = f"""<div class="slide" style="background:#050505;color:#F2EFEA">
      <div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:#8a827a">1 / 4</div></div>
      <div class="abs" style="left:80px;top:200px">
        <div style="position:relative;display:inline-block"><div class="c" style="font-size:440px;color:#3a3531">Mito</div>
          <div class="abs" style="left:-40px;right:-110px;top:50%;margin-top:-34px">{bar('#FF6518', '100%', 68, 'width:100%')}</div></div>
        <div class="c" style="font-size:440px;color:#FF6518;margin-top:6px">Fato</div>
      </div>
      <div class="abs x" style="left:80px;right:80px;bottom:80px;font-size:50px">Dois mitos que seguram quem já é referência no offline</div>
      </div>"""
    s2 = par(1, 4, "“Preciso<br>virar<br>youtuber.”", "Você continua sendo o especialista.", "Você só grava. Nossa equipe faz estratégia, roteiro, produção, edição, publicação e relatório.")
    s3 = par(2, 4, "“Sem anúncio<br>não tem<br>resultado.”", "Nós não dependemos de tráfego pago.", "Anúncio é complemento, não a base. Resultado construído com conteúdo, estratégia e relacionamento.")
    s4 = f"""<div class="slide" style="background:#FF6518;color:#050505">
      <div class="top">{logo('mono-preto')}<div class="lab">4 / 4</div></div>
      <div class="abs" style="left:80px;right:80px;top:210px">
        <div class="x" style="font-size:78px">Agende um <span style="white-space:nowrap">Raio-X</span> gratuito com os nossos consultores.</div>
        <div class="box" style="margin-top:54px;background:#050505;border-color:#050505;color:#FF6518"><div class="lab" style="color:#F2EFEA">Comente</div><div class="x" style="font-size:150px">Fato</div></div>
        <div class="t" style="margin-top:36px;font-size:32px;font-weight:600">A gente te manda o link no direct. <b>Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>
      </div></div>"""
    page("modelo-3-mito-fato", [s1, s2, s3, s4])

# ───────────────────────── MODELO 4 · ROTEIRO ─────────────────────────
def claquete(c1, c2, cena, tomada, fg):
    listras = f"repeating-linear-gradient(115deg,{c1} 0 70px,{c2} 70px 140px)"
    cel = f"border-right:3px solid {fg};padding:16px 22px 14px"
    return f"""<div class="abs" style="left:0;right:0;top:0;height:112px;background:{listras}"></div>
    <div class="abs" style="left:0;right:0;top:112px;display:grid;grid-template-columns:1.6fr 1fr 1fr;border-bottom:3px solid {fg};border-top:3px solid {fg};color:{fg}">
      <div style="{cel};padding-left:80px"><div class="lab" style="font-size:16px;opacity:.7">Produção</div><div class="c" style="font-size:52px;margin-top:6px">Grupo Euforia</div></div>
      <div style="{cel}"><div class="lab" style="font-size:16px;opacity:.7">Cena</div><div class="c" style="font-size:52px;margin-top:6px">{cena}</div></div>
      <div style="{cel};border-right:0"><div class="lab" style="font-size:16px;opacity:.7">Slide</div><div class="c" style="font-size:52px;margin-top:6px">{tomada}</div></div>
    </div>"""

def m_roteiro():
    def cena(n, titulo, quem, texto, voce=False):
        cor = "#FF6518" if voce else "#050505"; tx = "#050505" if voce else "#F2EFEA"
        return f"""<div style="padding:58px 0 60px;border-bottom:3px solid #050505">
          <div style="display:flex;justify-content:space-between;align-items:center;gap:20px">
            <div class="c" style="font-size:88px">Cena {n:02d} · {titulo}</div>
            <div class="lab" style="background:{cor};color:{tx};padding:10px 16px 8px;font-size:19px;white-space:nowrap;flex:none">{quem}</div></div>
          <div class="t" style="margin-top:26px;font-size:43px;color:#2a2622;max-width:880px">{texto}</div></div>"""
    s1 = f"""<div class="slide" style="background:#FF6518;color:#050505">{claquete('#050505', '#F2EFEA', 'Abertura', '1 de 4', '#050505')}
      <div class="abs" style="left:80px;right:80px;top:330px">
        <div class="lab">Quem faz o quê, cena por cena</div>
        <div class="x" style="font-size:96px;margin-top:30px">O roteiro<br>de um<br>ecossistema<br>digital</div>
      </div>
      <div class="abs" style="left:80px;right:80px;bottom:76px;display:flex;justify-content:space-between;align-items:center">{logo('mono-preto')}<div style="display:flex;align-items:center;gap:18px"><div class="lab">Arraste</div>{bar('#050505', 110, 30)}</div></div>
      </div>"""
    s2 = f"""<div class="slide" style="background:#F2EFEA;color:#050505">{claquete('#050505', '#FF6518', '01 e 02', '2 de 4', '#050505')}
      <div class="abs" style="left:80px;right:80px;top:270px">
        {cena(1, 'Estratégia e roteiro', 'Nossa equipe', 'Cada peça nasce com uma função: atrair quem ainda não conhece, convencer quem está em dúvida e levar para a conversa.')}
        {cena(2, 'Gravação', 'Você', 'Você grava com o roteiro na mão. É a única cena em que você entra.', True)}
      </div>
      <div class="abs lab" style="left:80px;bottom:76px;color:#8a827a">Corta para: edição</div></div>"""
    s3 = f"""<div class="slide" style="background:#F2EFEA;color:#050505">{claquete('#050505', '#FF6518', '03 e 04', '3 de 4', '#050505')}
      <div class="abs" style="left:80px;right:80px;top:270px">
        {cena(3, 'Produção e edição', 'Nossa equipe', 'Um vídeo vira vários formatos. Grava uma vez, aparece em todo lugar.')}
        {cena(4, 'Publicação e relatório', 'Nossa equipe', 'No ar nas redes, com o movimento medido todo mês: views, inscritos, conversas e leads.')}
      </div>
      <div class="abs lab" style="left:80px;bottom:76px;color:#8a827a">Corta para: a sua cena</div></div>"""
    s4 = f"""<div class="slide" style="background:#050505;color:#F2EFEA">{claquete('#FF6518', '#050505', 'A sua', '4 de 4', '#F2EFEA')}
      <div class="abs" style="left:80px;right:80px;top:320px">
        <div class="x" style="font-size:76px">Agende um <span class="lar"><span style="white-space:nowrap">Raio-X</span> gratuito</span> com os nossos consultores.</div>
        <div class="box" style="margin-top:54px;color:#FF6518"><div class="lab" style="color:#F2EFEA">Comente</div><div class="x" style="font-size:150px">Cena</div></div>
        <div class="t" style="margin-top:36px;font-size:32px;color:#cfc8bf">A gente te manda o link no direct. <b style="color:#F2EFEA">Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>
      </div></div>"""
    page("modelo-4-roteiro", [s1, s2, s3, s4])

# ───────────────────────── MODELO 5 · PLACAR ─────────────────────────
def m_placar():
    dados = [("+380", "ecossistemas digitais"), ("+R$ 18,2 mi", "faturados pelos clientes"), ("+2,1 bi", "de visualizações")]
    def chrome(ativo, i):
        cels = ""
        for k, (v, l) in enumerate(dados):
            on = k == ativo
            st = "background:#FF6518;color:#050505;border-color:#FF6518" if on else "color:#8a827a;border-color:#3a3531"
            cels += f'<div style="flex:1;border:3px solid;border-radius:14px;padding:18px 20px 16px;{st}"><div class="c" style="font-size:58px">{v}</div><div style="font-size:19px;font-weight:600;margin-top:8px;line-height:1.2">{l}</div></div>'
        return f"""<div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:#8a827a">Placar · {i} / 4</div></div>
        <div class="abs" style="left:80px;right:80px;bottom:72px;display:flex;gap:14px">{cels}</div>"""
    def num(ativo, i, pre, grande, pos, linha, apoio):
        pre_h = f'<div class="c" style="font-size:150px;color:#F2EFEA;margin-bottom:-6px">{pre}</div>' if pre else ""
        tam = 455 if pos else 520
        pos_h = f'<span style="font-size:.42em;color:#F2EFEA;margin-left:14px">{pos}</span>' if pos else ""
        return f"""<div class="slide" style="background:#050505;color:#F2EFEA">{chrome(ativo, i)}
          <div class="abs" style="left:76px;right:60px;top:190px">{pre_h}
            <div class="c" style="font-size:{tam}px;color:#FF6518;white-space:nowrap">{grande}{pos_h}</div>
            <div class="x" style="font-size:56px;margin-top:34px;max-width:900px">{linha}</div>
            <div class="t" style="margin-top:22px;font-size:34px;color:#cfc8bf;max-width:860px">{apoio}</div>
          </div></div>"""
    s1 = num(0, 1, "", "+380", "", "Ecossistemas digitais criados", "Três números contam a história do Grupo Euforia. Este é o primeiro.")
    s2 = num(1, 2, "+R$", "18,2", "mi", "Que ajudamos nossos clientes a faturar", "O resultado é deles. A gente constrói o caminho.")
    s3 = num(2, 3, "", "+2,1", "bi", "De visualizações geradas", "Para quem ensina o que sabe.")
    s4 = f"""<div class="slide" style="background:#050505;color:#F2EFEA">{chrome(-1, 4)}
      <div class="abs" style="left:80px;right:80px;top:200px">
        <div class="x" style="font-size:76px">Agende um <span class="lar"><span style="white-space:nowrap">Raio-X</span> gratuito</span> com os nossos consultores.</div>
        <div class="box" style="margin-top:50px;color:#FF6518"><div class="lab" style="color:#F2EFEA">Comente</div><div class="x" style="font-size:130px">Placar</div></div>
        <div class="t" style="margin-top:32px;font-size:31px;color:#cfc8bf">A gente te manda o link no direct. <b style="color:#F2EFEA">Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>
      </div></div>"""
    page("modelo-5-placar", [s1, s2, s3, s4])

for f in (m_player, m_manchete, m_mito, m_roteiro, m_placar):
    f()
print("ok")
