#!/usr/bin/env python3
"""Modelos 16 a 25: personalidades, livros, insight, memes e ensaio (capa + miolo + CTA).
Usa os helpers do gerar.py e do gerar2.py. Depois: SAIDA=/pasta node foto.js
Fotos de personalidades ficam em fotos/ (ver fotos/CREDITOS.txt): só em post sobre a própria pessoa, com crédito."""
import os
import gerar2 as g2
from gerar import sym, bar, logo, page, AQUI
from gerar2 import cta, lista, P, G, F, O, A, L, B, C

def foto(nome, estilo):
    return f'<img src="file://{os.path.join(AQUI, "fotos", nome)}" style="display:block;object-fit:cover;filter:grayscale(1) contrast(1.12);{estilo}">'

def credito(t, cor=C, pos="right:22px;bottom:150px"):
    return f'<div class="abs" style="{pos};writing-mode:vertical-rl;font-size:17px;color:{cor};letter-spacing:.04em">Foto: {t}</div>'

def topo(lg, rot, cor=C):
    return f'<div class="top">{logo(lg)}<div class="lab" style="color:{cor}">{rot}</div></div>'

BARRAS = f"repeating-linear-gradient(90deg,{P} 0 6px,transparent 6px 10px,{P} 10px 20px,transparent 20px 26px,{P} 26px 30px,transparent 30px 40px)"

# ───────── 16 · REVISTA (personalidade + frase) ─────────
def m16():
    s1 = f"""<div class="slide" style="background:{P};color:{O}">
      <div class="abs" style="left:0;right:0;top:250px;bottom:0">{foto('adibe-estudio.jpg', 'width:100%;height:100%;object-position:50% 12%')}</div>
      <div class="abs c" style="left:0;right:0;top:26px;text-align:center;font-size:330px;color:{L};line-height:.8">Euforia</div>
      <div class="abs" style="left:60px;right:60px;top:292px;display:flex;justify-content:space-between"><div class="lab" style="background:{P};padding:8px 12px 6px">Edição · Grandes nomes</div><div class="lab" style="background:{L};color:{P};padding:8px 12px 6px">Negócios</div></div>
      <div class="abs" style="left:0;right:0;bottom:0;background:{P};padding:44px 60px 56px">
        <div class="x" style="font-size:64px">“O brasileiro gosta de comprar de quem <span class="lar">bota cara.</span>”</div>
        <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:22px"><div style="font-size:30px;color:#cfc8bf;font-weight:600">João Adibe Marques, presidente da Cimed, à Forbes</div><div style="width:150px;height:54px;background:{O};padding:6px"><div style="height:100%;background:{BARRAS}"></div></div></div>
      </div>
      {credito('doisamaisfarma.com.br', '#cfc8bf', 'right:20px;top:360px')}</div>"""
    fatos = ["Mostra a agenda, a fábrica e o dia a dia da empresa", "Nas redes, ganhou o apelido de Tio João", "Chama a Cimed de “a empresa farmacêutica mais digital do planeta”"]
    s2 = f"""<div class="slide" style="background:{P};color:{O}">{topo('cor-fundo-escuro', 'Matéria de capa · 2 / 3')}
      <div class="abs" style="left:80px;right:80px;top:200px"><div class="c" style="font-size:160px">Podia ficar nos bastidores. <span class="lar">Escolheu aparecer.</span></div>
      <div style="margin-top:40px">{lista(fatos, L, O, F, 40, 26)}</div>
      <div style="font-size:24px;color:{C};margin-top:26px">Fontes: Forbes Brasil, Bloomberg Línea e InvestNews.</div></div></div>"""
    page("modelo-16-revista", [s1, s2, cta("Cara", "preto")])

# ───────── 17 · FIGURINHA (personalidade + trajetória) ─────────
def m17():
    def stat(a, b):
        return f'<div style="display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:13px 0;border-top:3px solid {P}"><span class="lab" style="font-size:19px">{a}</span><span class="c" style="font-size:50px;text-align:right">{b}</span></div>'
    s1 = f"""<div class="slide" style="background:{L};color:{P}">
      <div class="abs" style="left:120px;top:70px;width:840px;height:1130px;background:{O};border:10px solid {P};border-radius:44px;transform:rotate(-3deg);padding:34px 40px 0;box-shadow:22px 22px 0 {P}">
        <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab">Coleção · Grandes nomes</div><div class="c" style="font-size:64px;background:{P};color:{L};padding:10px 18px 2px;border-radius:14px">Rara</div></div>
        <div style="margin-top:22px;height:520px;border-radius:24px;overflow:hidden;border:6px solid {P};position:relative">{foto('alfredo-retrato.jpg', 'width:100%;height:100%;object-position:50% 14%')}
          <div class="abs" style="left:0;bottom:0;background:{L};padding:12px 22px 4px;border-radius:0 20px 0 0;border-top:6px solid {P};border-right:6px solid {P}"><div class="c" style="font-size:96px">Alfredo Soares</div></div></div>
        <div style="margin-top:20px;border-bottom:3px solid {P}">{stat('Fundou', 'Xtech Commerce')}{stat('Vendeu para', 'VTEX, em 2017')}{stat('Cofundou', 'G4 Educação')}{stat('Escreveu', '4 best-sellers')}</div>
        <div style="font-size:17px;margin-top:10px;color:#5c5650">Foto: g4business.com</div>
      </div>
      <div class="abs" style="left:80px;right:80px;bottom:56px;display:flex;justify-content:space-between;align-items:center">{logo('mono-preto')}<div style="display:flex;align-items:center;gap:18px"><div class="lab">Vire a figurinha</div>{bar(P, 110, 30)}</div></div></div>"""
    s2 = f"""<div class="slide" style="background:{L};color:{P}">
      <div class="abs" style="left:70px;top:80px;width:940px;height:1190px;background:{O};border:10px solid {P};border-radius:44px;padding:54px 54px 0;box-shadow:18px 18px 0 {P}">
        <div class="lab" style="color:{B}">Verso · 2 / 3 · A jogada dele</div>
        <div class="x" style="font-size:74px;margin-top:26px">“Sempre terá oportunidade para quem é <span style="color:{B}">lembrado.</span>”</div>
        <div style="border-top:4px solid {P};margin-top:40px;padding-top:34px;font-size:42px;line-height:1.3;font-weight:600">E como ser lembrado? Aparecendo.</div>
        <div class="c" style="font-size:150px;margin-top:20px;line-height:.9">Livro. Vídeo.<br>Palco. Podcast.</div>
        <div style="font-size:36px;font-weight:500;margin-top:30px;color:#3a3531">Quem some da cabeça do cliente some da agenda dele.</div>
        <div style="font-size:22px;color:#5c5650;margin-top:26px">Fontes: SBT News, VTEX e G4 Educação.</div>
      </div></div>"""
    page("modelo-17-figurinha", [s1, s2, cta("Lembrado", "laranja")])

# ───────── 18 · DOSSIÊ (personalidade + curiosidades) ─────────
def m18():
    def campo(a, b):
        return f'<div style="display:grid;grid-template-columns:140px 1fr;align-items:baseline;padding:16px 0;border-bottom:3px dotted {P}"><span class="lab" style="font-size:20px">{a}</span><span class="c" style="font-size:44px;white-space:nowrap">{b}</span></div>'
    pasta = f'<div class="abs" style="left:50px;top:120px;width:520px;height:90px;background:{A};border-radius:26px 26px 0 0"></div><div class="abs" style="left:50px;right:50px;top:190px;bottom:60px;background:{A};border-radius:0 30px 30px 30px"></div>'
    s1 = f"""<div class="slide" style="background:{G};color:{P}">{pasta}
      <div class="abs lab" style="left:86px;top:146px;font-size:24px">Arquivo · Grandes nomes</div>
      <div class="abs" style="left:100px;top:250px;width:880px;height:900px;background:{O};transform:rotate(-2deg);padding:50px 50px 0">
        <div class="c" style="font-size:150px">Dossiê</div>
        <div style="width:500px;margin-top:20px">{campo('Nome', 'João Adibe Marques')}{campo('Cargo', 'Presidente da Cimed')}{campo('Codinome', 'Tio João')}{campo('Arma', 'Botar a cara')}</div>
      </div>
      <div class="abs" style="right:80px;top:300px;width:320px;height:420px;background:{O};padding:16px 16px 60px;transform:rotate(5deg);box-shadow:10px 10px 0 {P}">{foto('adibe-caixas.jpg', 'width:100%;height:100%;object-position:60% 20%')}<div style="font-size:16px;margin-top:10px;color:#5c5650">Foto: exame.com</div></div>
      <div class="abs" style="right:210px;top:262px;width:44px;height:120px;border:9px solid {P};border-radius:22px;transform:rotate(12deg)"></div>
      <div class="abs c" style="right:100px;top:860px;font-size:76px;color:{L};border:9px solid {L};border-radius:18px;padding:16px 24px 4px;transform:rotate(-9deg)">3 curiosidades</div>
      <div class="abs x" style="left:120px;right:120px;bottom:120px;font-size:70px;transform:rotate(-2deg)">O que o Tio João entendeu antes</div></div>"""
    cur = ["Podia ficar nos bastidores. Escolheu aparecer e virou o rosto da marca.", "Chama a Cimed de “a empresa farmacêutica mais digital do planeta”.", "No 1º trimestre de 2026, a Cimed faturou R$ 1 bilhão, alta de 20%, segundo o InvestNews."]
    s2 = f"""<div class="slide" style="background:{G};color:{P}">{pasta}
      <div class="abs lab" style="left:86px;top:146px;font-size:24px">Arquivo · 2 / 3</div>
      <div class="abs" style="left:90px;top:240px;width:900px;height:1000px;background:{O};padding:54px 54px 0">
        <div class="c" style="font-size:120px">3 curiosidades</div>
        <div style="margin-top:20px">{lista(cur, B, P, P, 39, 26)}</div>
        <div style="font-size:22px;color:#5c5650;margin-top:24px">Fontes: Forbes Brasil, Bloomberg Línea e InvestNews.</div>
      </div></div>"""
    page("modelo-18-dossie", [s1, s2, cta("Dossiê", "grafite")])

# ───────── 19 · ASPAS (frase de personalidade) ─────────
def m19():
    s1 = f"""<div class="slide" style="background:{O};color:{P}">
      <div class="abs" style="left:40px;top:-150px;font-family:Archivo;font-weight:800;font-stretch:125%;font-size:900px;line-height:1;color:{L}">“</div>
      <div class="abs lab" style="right:80px;top:84px;opacity:.6">1 / 3</div>
      <div class="abs" style="left:80px;right:80px;top:400px"><div class="c" style="font-size:156px;line-height:1">Sempre terá oportunidade para quem é <span style="background:{P};color:{L};padding:10px 16px 0;margin-left:-16px">lembrado.</span></div></div>
      <div class="abs" style="left:80px;right:80px;bottom:76px;display:flex;align-items:center;gap:26px">
        <div style="width:150px;height:150px;border-radius:50%;overflow:hidden;border:6px solid {P};flex:none">{foto('alfredo-rosto.jpg', 'width:100%;height:100%')}</div>
        <div style="flex:1"><div class="x" style="font-size:44px">Alfredo Soares</div><div style="font-size:28px;font-weight:600;color:#3a3531;margin-top:6px">cofundador do G4 Educação, ao SBT News</div><div style="font-size:17px;color:#5c5650;margin-top:6px">Foto: dmtpalestras.com.br</div></div>
        {bar(L, 110, 30)}</div></div>"""
    pal = "".join(f'<div style="display:flex;align-items:center;gap:26px;margin-top:14px">{bar(L if k % 2 == 0 else O, 150 + k * 90, 56)}<div class="c" style="font-size:120px">{t}</div></div>' for k, t in enumerate(["Livro", "Vídeo", "Palco", "Podcast"]))
    s2 = f"""<div class="slide" style="background:{P};color:{O}">{topo('cor-fundo-escuro', '2 / 3')}
      <div class="abs" style="left:80px;right:80px;top:200px"><div class="x" style="font-size:84px">E como ser <span class="lar">lembrado?</span></div>
      <div class="t" style="margin-top:24px;color:#cfc8bf">Aparecendo.</div><div style="margin-top:26px">{pal}</div>
      <div class="t" style="margin-top:44px;color:#cfc8bf;font-size:36px">Quem some da cabeça do cliente some da agenda dele.</div></div></div>"""
    page("modelo-19-aspas", [s1, s2, cta("Frase", "off")])

# ───────── 20 · ESTANTE (resumo de livro) ─────────
def m20():
    def lomb(w, cor, borda="", ml=0, txt=""):
        b = f"border:4px solid {borda};" if borda else ""
        dentro = txt or f'<div style="height:16px;border-radius:8px;width:44%;background:{F if cor != F else "#3a3531"}"></div>'
        return f'<div style="width:{w}px;height:112px;background:{cor};{b}border-radius:10px;margin-left:{ml}px;display:flex;align-items:center;padding:0 34px;gap:20px">{dentro}</div>'
    destaque = f'<div class="c" style="font-size:54px;color:{P};white-space:nowrap">Building a StoryBrand</div><div style="flex:1"></div><div class="lab" style="color:{P};font-size:19px;white-space:nowrap">Donald Miller</div>'
    pilha = lomb(700, F, "", 40) + lomb(780, A, "", 0) + lomb(800, L, "", 100, destaque) + lomb(740, O, "", 30) + lomb(820, G, "#3a3531", 70)
    s1 = f"""<div class="slide" style="background:{P};color:{O}">{topo('cor-fundo-escuro', 'Resumo de livro · 1 / 3')}
      <div class="abs" style="left:80px;right:80px;top:190px"><div class="x" style="font-size:112px">O livro em<br><span class="lar">3 ideias</span></div></div>
      <div class="abs" style="left:60px;top:540px;display:flex;flex-direction:column;gap:12px">{pilha}</div>
      <div class="abs" style="left:60px;right:60px;top:1168px;height:10px;background:{F};border-radius:5px"></div>
      <div class="abs t" style="left:80px;right:80px;bottom:70px;font-size:34px;color:#cfc8bf">Para quem não tem tempo de ler, mas precisa aplicar.</div></div>"""
    ideias = ["O herói da história é o cliente, não a marca", "A marca é o guia: mostra o plano e chama para a ação", "Se a mensagem confunde, o cliente vai embora"]
    s2 = f"""<div class="slide" style="background:{P};color:{O}">{topo('cor-fundo-escuro', 'Resumo de livro · 2 / 3')}
      <div class="abs" style="left:80px;right:80px;top:200px"><div style="display:inline-block">{lomb(860, L, "", 0, destaque)}</div>
      <div style="margin-top:44px">{lista(ideias, L, O, F, 46, 36)}</div>
      <div class="t" style="margin-top:36px;color:#cfc8bf;font-size:34px">Vale para o seu vídeo, o seu post e a sua página.</div></div></div>"""
    page("modelo-20-estante", [s1, s2, cta("Livro", "preto")])

# ───────── 21 · MARCA-TEXTO (a frase que vale o livro) ─────────
def m21():
    def linhas(n, ws):
        return "".join(f'<div style="height:18px;border-radius:9px;background:{A};width:{ws[k % len(ws)]}%;margin-top:26px"></div>' for k in range(n))
    cab = f'<div class="abs" style="left:90px;right:90px;top:80px;display:flex;justify-content:space-between;border-bottom:3px solid {P};padding-bottom:16px"><div class="lab" style="font-size:19px">Building a StoryBrand · Donald Miller</div><div class="lab" style="font-size:19px">'
    fita = f'<div class="abs" style="right:250px;top:0;width:76px;height:210px;background:{L};clip-path:polygon(0 0,100% 0,100% 100%,50% 82%,0 100%)"></div>'
    s1 = f"""<div class="slide" style="background:{O};color:{P}">{cab}1 / 3</div></div>{fita}
      <div class="abs" style="left:90px;right:90px;top:170px">{linhas(5, [100, 96, 100, 92, 58])}
        <div style="margin:54px 0 28px;font-size:104px;font-weight:800;line-height:1.16;letter-spacing:-.02em"><span style="background:{L};box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:2px 14px;margin-left:-14px">O herói não é você. É o seu cliente.</span></div>
        {linhas(6, [100, 94, 100, 97, 100, 40])}</div>
      <div class="abs" style="left:90px;right:90px;bottom:70px;display:flex;justify-content:space-between;align-items:center"><div class="x" style="font-size:38px">A frase que vale o livro</div>{bar(P, 110, 30)}</div></div>"""
    s2 = f"""<div class="slide" style="background:{O};color:{P}">{cab}2 / 3</div></div>{fita}
      <div class="abs" style="left:90px;right:90px;top:220px"><div class="x" style="font-size:66px">O que isso muda no seu conteúdo</div>
        <div style="margin-top:50px"><div class="lab" style="color:#5c5650">Em vez de</div>
          <div style="position:relative;display:inline-block;margin-top:14px"><div style="font-size:56px;font-weight:700;line-height:1.2;color:#8a827a">“Nossa empresa tem 20 anos de mercado.”</div><div class="abs" style="left:-10px;right:-10px;top:50%;margin-top:-10px;transform:rotate(-2deg)">{bar(P, '100%', 18, 'width:100%')}</div></div></div>
        <div style="margin-top:60px"><div class="lab" style="color:{B}">Experimente</div>
          <div style="font-size:64px;font-weight:800;line-height:1.2;margin-top:14px"><span style="background:{L};box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:2px 12px;margin-left:-12px">“Você tem 20 anos de mercado e quase ninguém te encontra?”</span></div></div>
        <div style="font-size:34px;font-weight:500;margin-top:50px;color:#3a3531">A primeira frase fala de você. A segunda fala de quem está lendo.</div></div></div>"""
    page("modelo-21-marca-texto", [s1, s2, cta("Herói", "off")])

# ───────── 22 · HOLOFOTE (insight) ─────────
def m22():
    s1 = f"""<div class="slide" style="background:{P};color:{O}">{topo('cor-fundo-escuro', 'Insight · 1 / 3')}
      <div class="abs" style="left:-60px;top:170px;width:1200px;height:1200px;border-radius:50%;background:{L}"></div>
      <div class="abs" style="left:110px;right:110px;top:430px;color:{P};text-align:center"><div class="lab" style="font-size:26px">Anota essa</div>
        <div class="x" style="font-size:98px;margin-top:30px">Confiança não nasce em 15 segundos de anúncio.</div></div>
      <div class="abs" style="left:0;right:0;bottom:90px;display:flex;justify-content:center">{bar(P, 130, 36)}</div></div>"""
    elos = ["Audiência", "Conversa", "Cliente", "Indicação"]
    cad = ""
    for k, e in enumerate(elos):
        cad += f'<div style="display:flex;align-items:center;gap:24px"><div style="width:{470 + k * 110}px;height:150px;border-radius:75px;background:{L if k == 3 else F};color:{P if k == 3 else O};display:flex;align-items:center;padding:8px 44px 0"><span class="c" style="font-size:96px">{e}</span></div>{"" if k == 3 else "<span class=lab style=color:" + C + ">vira</span>"}</div>'
    s2 = f"""<div class="slide" style="background:{P};color:{O}">{topo('cor-fundo-escuro', 'Insight · 2 / 3')}
      <div class="abs" style="left:80px;right:80px;top:200px"><div class="x" style="font-size:80px">Ela nasce de <span class="lar">gente que conversa com gente.</span></div>
      <div style="display:flex;flex-direction:column;gap:18px;margin-top:50px">{cad}</div></div></div>"""
    page("modelo-22-holofote", [s1, s2, cta("Insight", "preto")])

# ───────── 23 · EXPECTATIVA × REALIDADE (meme) ─────────
def m23():
    zig = ",".join(f"{x}% {100 if k % 2 else 95}%" for k, x in enumerate([100 - i * 5 for i in range(21)]))
    s1 = f"""<div class="slide" style="background:{P};color:{O}">
      <div class="abs" style="left:0;right:0;top:0;height:700px;background:{O};color:{P};clip-path:polygon(0 0,100% 0,{zig});padding:80px 80px 0">
        <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab" style="background:{P};color:{O};padding:10px 16px 8px;font-size:26px">Expectativa</div>{logo('cor-fundo-claro', 40)}</div>
        <div class="c" style="font-size:138px;margin-top:40px;line-height:.9">“Vou postar todo dia e a agenda vai lotar.”</div></div>
      <div class="abs" style="left:80px;right:80px;top:740px">
        <div class="lab" style="background:{L};color:{P};padding:10px 16px 8px;font-size:26px;display:inline-block">Realidade</div>
        <div style="background:{F};border-radius:30px;padding:34px 38px;margin-top:30px;display:flex;align-items:center;gap:30px">
          <div style="width:110px;height:110px;border-radius:50%;background:{L};display:grid;place-items:center;flex:none"><div class="c" style="font-size:86px;color:{P};margin-top:10px">3</div></div>
          <div><div class="x" style="font-size:60px">curtidas</div><div style="font-size:40px;font-weight:600;color:#cfc8bf;margin-top:10px">Sua mãe, seu sócio e você.</div></div></div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:44px"><div style="font-size:32px;color:{C};font-weight:600">Já passou por isso?</div>{bar(L, 110, 30)}</div></div></div>"""
    s2 = f"""<div class="slide" style="background:{P};color:{O}">{topo('cor-fundo-escuro', '2 / 3')}
      <div class="abs" style="left:80px;right:80px;top:210px"><div class="c" style="font-size:190px;line-height:.88">Não é falta de esforço. <span class="lar">É falta de caminho.</span></div>
      <div class="t" style="margin-top:44px;color:#cfc8bf;font-size:42px">Frequência sozinha não traz cliente. Conteúdo com função, sim: atrair, convencer e levar para a conversa.</div></div></div>"""
    page("modelo-23-expectativa", [s1, s2, cta("Realidade", "preto")])

# ───────── 24 · KIT (meme "starter pack") ─────────
def m24():
    def caixa(icone, leg, bg=O, fg=P, bd=P):
        return f'<div style="border:6px solid {bd};border-radius:26px;background:{bg};color:{fg};padding:26px;display:flex;flex-direction:column;justify-content:space-between;height:400px"><div style="flex:1;display:grid;place-items:center">{icone}</div><div class="c" style="font-size:62px;line-height:.9;text-align:center">{leg}</div></div>'
    cartao = f'<div style="width:270px;height:160px;border:6px solid {P};border-radius:14px;padding:22px;transform:rotate(-6deg);background:{O}"><div style="height:20px;width:60%;background:{P};border-radius:10px"></div><div style="height:12px;width:80%;background:{A};border-radius:6px;margin-top:22px"></div><div style="height:12px;width:50%;background:{A};border-radius:6px;margin-top:12px"></div></div>'
    boca = f'<div style="display:flex;align-items:center;gap:8px"><div style="width:110px;height:110px;border-radius:50%;border:6px solid {P}"></div>{bar(L, 90, 26)}<div style="width:110px;height:110px;border-radius:50%;background:{P}"></div></div>'
    post = f'<div style="width:190px;height:190px;border:6px solid {P};border-radius:18px;display:grid;place-items:center;position:relative"><div class="c" style="font-size:86px;color:{A};margin-top:10px">2022</div></div>'
    obra = f'<div style="width:290px;height:110px;border:6px solid {P};border-radius:12px;background:repeating-linear-gradient(115deg,{P} 0 30px,{L} 30px 60px)"></div>'
    s1 = f"""<div class="slide" style="background:{O};color:{P}">
      <div class="abs" style="left:70px;right:70px;top:66px;display:flex;justify-content:space-between;align-items:center">{logo('cor-fundo-claro', 40)}<div class="lab" style="opacity:.6">Meme · 1 / 3</div></div>
      <div class="abs" style="left:70px;right:70px;top:150px"><div class="c" style="font-size:120px;line-height:.88;white-space:nowrap">Kit do especialista<br><span style="color:{B}">invisível</span></div></div>
      <div class="abs" style="left:70px;right:70px;top:440px;display:grid;grid-template-columns:1fr 1fr;gap:20px">
        {caixa(cartao, 'Cartão de visita')}{caixa(boca, 'Indicação do cunhado')}{caixa(post, 'Último post')}{caixa(obra, 'Site em construção')}</div></div>"""
    def bloco(t):
        return f'<div style="border-radius:26px;background:{L};color:{P};padding:30px 34px;height:230px;display:flex;flex-direction:column;justify-content:space-between">{bar(P, 90, 26)}<div class="c" style="font-size:74px;line-height:.9">{t}</div></div>'
    s2 = f"""<div class="slide" style="background:{P};color:{O}">{topo('cor-fundo-escuro', '2 / 3')}
      <div class="abs" style="left:70px;right:70px;top:190px"><div class="c" style="font-size:150px;line-height:.86">Kit do especialista <span class="lar">encontrado</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:44px">{bloco('Base de conteúdo')}{bloco('Distribuição')}{bloco('Busca')}{bloco('Caminho até você')}</div>
      <div class="t" style="margin-top:40px;color:#cfc8bf;font-size:36px">Brincadeiras à parte: o primeiro kit não some. Ele só não basta mais.</div></div></div>"""
    page("modelo-24-kit", [s1, s2, cta("Kit", "off")])

# ───────── 25 · ENSAIO (reflexão) ─────────
def m25():
    tit = "font-family:Archivo;font-weight:700;font-stretch:100%;letter-spacing:-.025em;line-height:.98"
    def cab(n):
        return f'<div class="abs" style="left:110px;right:110px;top:90px;display:flex;justify-content:space-between;align-items:center"><div style="display:flex;align-items:center;gap:16px">{bar(L, 60, 18)}<div class="lab">Ensaio</div></div><div class="lab" style="opacity:.6">{n}</div></div><div class="abs" style="left:110px;right:110px;bottom:84px;display:flex;justify-content:space-between;align-items:center">{logo("cor-fundo-claro", 36)}<div style="font-size:24px;font-style:italic;color:#5c5650">leitura de um minuto</div></div>'
    s1 = f"""<div class="slide" style="background:{O};color:{P}">{cab('I')}
      <div class="abs" style="left:110px;right:110px;top:250px"><div style="{tit};font-size:150px">Sobre ser<br>encontrado</div>
        <div style="width:120px;height:6px;background:{P};margin:54px 0 44px"></div>
        <div style="font-size:46px;line-height:1.42;font-weight:500"><span class="x" style="float:left;font-size:176px;line-height:.78;color:{L};padding:10px 18px 0 0">D</span>urante anos, a indicação funcionou sozinha. Um cliente satisfeito falava com um amigo, o amigo ligava, e a agenda se enchia.</div></div></div>"""
    s2 = f"""<div class="slide" style="background:{O};color:{P}">{cab('II')}
      <div class="abs" style="left:110px;right:110px;top:230px">
        <div style="font-size:46px;line-height:1.42;font-weight:500">O trabalho continua bom. O que mudou foi o caminho. Antes de ligar, as pessoas pesquisam. E quem não aparece na pesquisa não entra na conversa.</div>
        <div style="border-left:10px solid {L};padding-left:36px;margin-top:64px"><div style="{tit};font-size:92px">Ser bom deixou de ser suficiente. É preciso ser encontrável.</div></div>
        <div style="font-size:40px;line-height:1.42;font-weight:500;margin-top:60px;color:#3a3531">A experiência de décadas não se perde. Ela só precisa estar onde o cliente procura.</div></div></div>"""
    page("modelo-25-ensaio", [s1, s2, cta("Ensaio", "off")])

for f in (m16, m17, m18, m19, m20, m21, m22, m23, m24, m25):
    f()
print("ok3")
