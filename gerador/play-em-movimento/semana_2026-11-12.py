#!/usr/bin/env python3
"""Posts de 12 a 15/11/2026 refeitos nos modelos Play em Movimento (pedido do Henrique em 12/11).
Uso: python3 semana_2026-11-12.py  -> grava slides.html em cada carrosseis/<pasta>/; depois render_post.js."""
import os, sys, glob
AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
sys.path.insert(0, AQUI)
antes = set(glob.glob(os.path.join(AQUI, "modelo-*.html")))
import gerar as g  # o import roda os exemplos 1 a 5; apagamos os HTML gerados abaixo
from gerar import bar, logo, manchete_chrome
for f in set(glob.glob(os.path.join(AQUI, "modelo-*.html"))) - antes:
    os.remove(f)

P, G, F, O, A, L, B, C = "#050505", "#141312", "#26221F", "#F2EFEA", "#DDD6CB", "#FF6518", "#C2410C", "#8a827a"
RX = '<span style="white-space:nowrap">Raio-X</span>'

def salvar(pasta, slides):
    html = f'<!doctype html><meta charset="utf-8"><style>{g.CSS}</style>' + "".join(slides)
    open(os.path.join(REPO, "carrosseis", pasta, "slides.html"), "w").write(html)

def cta_txt(fg, sub, ac):
    return f"""<div class="x" style="font-size:76px">Agende um <span style="color:{ac}">{RX} gratuito</span> com a nossa equipe.</div>"""

def apos(fg, sub):
    return f"""<div class="t" style="margin-top:36px;font-size:32px;color:{sub}">A gente te manda o link no direct. <b style="color:{fg}">Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>"""

# ───────── QUI 12/11 · post único · PLACAR ─────────
def placar_2bi():
    dados = [("+380", "ecossistemas digitais"), ("+R$ 18,2 mi", "ajudamos clientes a faturar"), ("+2,1 bi", "de visualizações")]
    cels = ""
    for k, (v, l) in enumerate(dados):
        st = "background:#FF6518;color:#050505;border-color:#FF6518" if k == 2 else "color:#8a827a;border-color:#3a3531"
        cels += f'<div style="flex:1;border:3px solid;border-radius:14px;padding:18px 20px 16px;{st}"><div class="c" style="font-size:58px">{v}</div><div style="font-size:19px;font-weight:600;margin-top:8px;line-height:1.2">{l}</div></div>'
    s1 = f"""<div class="slide" style="background:#050505;color:#F2EFEA">
      <div class="top">{logo('cor-fundo-escuro')}<div class="lab" style="color:#8a827a">Placar</div></div>
      <div class="abs" style="left:80px;right:80px;bottom:72px;display:flex;gap:14px">{cels}</div>
      <div class="abs" style="left:76px;right:60px;top:190px">
        <div class="c" style="font-size:455px;color:#FF6518;white-space:nowrap">+2,1<span style="font-size:.42em;color:#F2EFEA;margin-left:14px">bi</span></div>
        <div class="x" style="font-size:56px;margin-top:34px;max-width:900px">de vezes alguém parou pra assistir</div>
        <div class="t" style="margin-top:22px;font-size:34px;color:#cfc8bf;max-width:860px">Visualizações geradas para especialistas que ensinam o que sabem. Movimento medido, gente certa chegando.</div>
      </div></div>"""
    salvar("2026-11-12_2-bilhoes", [s1])

# ───────── SEX 13/11 · carrossel · MANCHETE ─────────
def manchete_ia():
    bg = "background:#F2EFEA;color:#050505"
    n = 7
    def pg(i, corpo, pe=None):
        return f'<div class="slide" style="{bg}">{manchete_chrome(i, n, pe or f"Continua na página {i+1}")}<div class="abs" style="left:80px;right:80px;top:214px">{corpo}</div></div>'
    s1 = pg(1, f"""<span class="lab" style="background:#FF6518;padding:10px 16px 8px;display:inline-block">Análise</span>
        <div class="c" style="font-size:178px;margin-top:34px">Seu cliente perguntou pro ChatGPT.<br><span style="color:#C2410C">Ele citou você?</span></div>
        <div class="t" style="margin-top:44px;font-size:42px;max-width:860px;font-weight:600">A busca está mudando de lugar.</div>""")
    s2 = pg(2, f"""<div class="lab" style="color:#C2410C">A mudança</div>
        <div class="c" style="font-size:150px;margin-top:26px">Antes:<br>10 links<br>no Google.</div>
        <div class="t" style="margin-top:44px;font-size:40px;color:#3a3531">Agora muita gente pergunta direto pro ChatGPT ou pro Gemini: “quem é bom nesse assunto na minha cidade?”</div>
        <div class="t" style="margin-top:28px;font-size:40px;font-weight:800">E recebe uma resposta pronta, com poucos nomes.</div>""")
    s3 = pg(3, f"""<div class="lab" style="color:#C2410C">A previsão</div>
        <div class="c" style="font-size:400px;color:#FF6518;margin-top:20px;line-height:.8">−25%</div>
        <div class="x" style="font-size:54px;margin-top:40px">no volume da busca tradicional até 2026</div>
        <div class="t" style="margin-top:30px;font-size:34px;color:#3a3531">A previsão do Gartner é de 2024 e foi contestada por parte do mercado. <b style="color:#050505">Mas a direção é clara: a resposta está saindo da lista de links.</b></div>
        <div class="lab" style="margin-top:34px;font-size:18px;color:#8a827a">Fonte: Gartner (fev/2024) e Search Engine Land</div>""")
    itens = [("Vídeo", "Você explicando o assunto, com a sua voz."), ("Site", "Texto que responde as dúvidas de quem procura."), ("Perfil", "Completo e atualizado em cada rede."), ("Citações", "Gente falando de você e do seu trabalho.")]
    rows = "".join(f"""<div style="display:grid;grid-template-columns:120px 1fr;gap:10px;padding:26px 0;border-top:2px solid #050505;align-items:start">
          <div class="c" style="font-size:120px;color:#FF6518;line-height:.8">{k+1}</div>
          <div><div class="x" style="font-size:44px">{a}</div><div class="t" style="margin-top:10px;font-size:32px;color:#3a3531">{b}</div></div></div>""" for k, (a, b) in enumerate(itens))
    s4 = pg(4, f"""<div class="lab" style="color:#C2410C">O que pesa</div>
        <div class="x" style="font-size:60px;margin-top:20px">Quem aparece tem conteúdo público e consistente</div>
        <div style="margin-top:34px;border-bottom:2px solid #050505">{rows}</div>""")
    s5 = pg(5, f"""<div class="lab" style="color:#C2410C">Bastidor</div>
        <div class="c" style="font-size:136px;line-height:.92;margin-top:24px">A gente fez isso na nossa própria casa.</div>
        <div class="c" style="font-size:96px;line-height:1.06;margin-top:34px"><span style="background:#FF6518;box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:6px 14px 0;margin-left:-14px">Site novo. Blog toda semana. Cada rede organizada.</span></div>
        <div class="t" style="margin-top:50px;font-size:36px;max-width:840px;color:#3a3531">Pouca gente no mercado cuida disso junto com o vídeo.</div>""")
    s6 = pg(6, f"""<div class="lab" style="color:#C2410C">Faça o teste</div>
        <div class="c" style="font-size:150px;line-height:.92;margin-top:30px">Pergunte pro ChatGPT quem é referência no seu assunto.</div>
        <div class="c" style="font-size:132px;line-height:1;margin-top:50px;white-space:nowrap"><span style="background:#FF6518;padding:6px 16px 0;margin-left:-16px">Você apareceu?</span></div>""")
    s7 = pg(7, f"""<div class="lab" style="color:#C2410C">Serviço</div>
        <div class="x" style="font-size:74px;margin-top:20px">Agende um {RX} gratuito com a nossa equipe.</div>
        <div class="box" style="margin-top:54px;background:#050505;border-color:#050505;color:#FF6518"><div class="lab" style="color:#F2EFEA">Comente</div><div class="x" style="font-size:150px">Busca</div></div>
        <div class="t" style="margin-top:36px;font-size:32px;color:#3a3531">A gente te manda o link no direct. <b style="color:#050505">Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>
        <div class="lab" style="margin-top:40px;color:#3a3531">Salve e faça o teste com o seu nome</div>""", "@euforiagrupo")
    salvar("2026-11-13_google-ias", [s1, s2, s3, s4, s5, s6, s7])

# ───────── SÁB 14/11 · post único · REC ─────────
def cantos(cor, m=60, t=90, e=8, topo=60, base=60):
    c = lambda pos: f'<div class="abs" style="{pos};width:{t}px;height:{t}px"></div>'
    est = f"border-color:{cor};border-style:solid;border-width:0"
    return (f'<div class="abs" style="left:{m}px;top:{topo}px;width:{t}px;height:{t}px;{est};border-left-width:{e}px;border-top-width:{e}px"></div>'
            f'<div class="abs" style="right:{m}px;top:{topo}px;width:{t}px;height:{t}px;{est};border-right-width:{e}px;border-top-width:{e}px"></div>'
            f'<div class="abs" style="left:{m}px;bottom:{base}px;width:{t}px;height:{t}px;{est};border-left-width:{e}px;border-bottom-width:{e}px"></div>'
            f'<div class="abs" style="right:{m}px;bottom:{base}px;width:{t}px;height:{t}px;{est};border-right-width:{e}px;border-bottom-width:{e}px"></div>')

def rec_linkedin():
    grade = f'<div class="abs" style="left:33.33%;top:60px;bottom:60px;width:2px;background:{F}"></div><div class="abs" style="left:66.66%;top:60px;bottom:60px;width:2px;background:{F}"></div><div class="abs" style="top:33.33%;left:60px;right:60px;height:2px;background:{F}"></div><div class="abs" style="top:66.66%;left:60px;right:60px;height:2px;background:{F}"></div>'
    bat = f'<div style="width:74px;height:34px;border:4px solid {O};border-radius:8px;padding:4px;position:relative"><div style="height:100%;width:70%;background:{O};border-radius:2px"></div><div class="abs" style="right:-10px;top:8px;width:6px;height:10px;background:{O};border-radius:0 3px 3px 0"></div></div>'
    s1 = f"""<div class="slide" style="background:{P};color:{O}">{grade}{cantos(O)}
      <div class="abs" style="left:110px;top:100px;display:flex;align-items:center;gap:16px"><div style="width:30px;height:30px;border-radius:50%;background:{L}"></div><div class="c" style="font-size:56px;color:{L}">Rec</div><div class="c" style="font-size:56px;margin-left:14px">00:00:00</div></div>
      <div class="abs" style="right:110px;top:108px;display:flex;align-items:center;gap:20px"><div class="lab" style="color:{C}">Notícia</div>{bat}</div>
      <div class="abs" style="left:110px;right:110px;top:250px;background:{P};padding:0 0 10px"><div class="x" style="font-size:96px">O LinkedIn quer pagar por <span class="lar">vídeo.</span></div></div>
      <div class="abs" style="left:110px;right:110px;bottom:220px;background:{P};font-size:40px;font-weight:700;line-height:1.25">A rede testa anúncios antes dos vídeos de criadores, com divisão da receita.<br><span style="color:#cfc8bf;font-weight:500">E o vídeo é o formato que mais cresce por lá.</span></div>
      <div class="abs" style="left:110px;right:110px;bottom:104px;display:flex;justify-content:space-between;align-items:center"><div class="lab" style="background:{O};color:{P};padding:10px 14px 8px">Em teste</div><div class="lab" style="color:{C};font-size:18px">Fontes: Net Influencer e Inc.</div></div></div>"""
    salvar("2026-11-14_linkedin-video", [s1])

# ───────── DOM 15/11 · carrossel · DICIONÁRIO ─────────
def dicionario_storybrand():
    n = 7
    verb = "font-family:Archivo;font-weight:800;font-stretch:100%;letter-spacing:-.02em;line-height:.92"
    aba = lambda t: f'<div class="abs c" style="right:0;top:250px;width:92px;height:150px;background:{L};color:{P};border-radius:18px 0 0 18px;font-size:110px;display:grid;place-items:center;padding-top:14px">{t}</div>'
    def topo(i):
        return f'<div class="top">{logo("cor-fundo-claro")}<div class="lab" style="opacity:.6;margin-right:60px">Dicionário · {i} / {n}</div></div>'
    def risca(p):
        return f'<span style="position:relative;font-weight:800">{p}<span class="abs" style="left:-10px;right:-10px;top:50%;margin-top:-2px">{bar(L, "100%", 9, "width:100%")}</span></span>'
    def verbete(i, letra, palavra, classe, defs, extra="", tam=176):
        dd = "".join(f'<b>{k+1}.</b><div>{d}</div>' for k, d in enumerate(defs))
        return f"""<div class="slide" style="background:{O};color:{P}">{aba(letra)}{topo(i)}
      <div class="abs" style="left:80px;right:110px;top:270px">
        <div style="{verb};font-size:{tam}px">{palavra}</div>
        <div style="font-size:40px;font-style:italic;color:{B};margin-top:30px;font-weight:600">{classe}</div>
        <div style="border-top:4px solid {P};margin-top:30px;padding-top:30px;display:grid;grid-template-columns:60px 1fr;gap:18px 8px;font-size:54px;line-height:1.22;font-weight:500">{dd}</div>
        {extra}</div></div>"""
    s1 = verbete(1, "H", "he·rói", "substantivo masculino",
                 ["Quem vive o problema e precisa vencê-lo.", "<b>Na história da sua marca: o seu cliente.</b>"],
                 f'<div style="margin-top:44px;font-size:42px;font-weight:600;display:flex;align-items:center;gap:14px"><span style="font-style:italic;color:{B}">Não confundir com</span>{risca("você")}</div>'
                 f'<div class="lab" style="margin-top:110px;font-size:26px;color:#3a3531">A ideia de StoryBrand, de Donald Miller →</div>', 270)
    s2 = verbete(2, "S", "Story·<br>Brand", "livro de Donald Miller, 2017",
                 ["Método para explicar o que você faz sem confundir o cliente.", "<b>A ideia central cabe numa frase.</b>"], tam=220)
    s3 = verbete(3, "G", "gui·a", "substantivo masculino",
                 ["Quem já conhece o caminho e mostra a saída.", "<b>Na história da sua marca: você.</b>"],
                 f'<div style="margin-top:50px;font-size:40px;font-weight:600;font-style:italic;color:{B}">O cliente é o herói. Você é o guia.</div>', 270)
    s4 = f"""<div class="slide" style="background:{O};color:{P}">{aba('E')}{topo(4)}
      <div class="abs" style="left:80px;right:130px;top:220px"><div class="lab" style="color:{B}">Uso incorreto</div>
        <div class="x" style="font-size:84px;margin-top:22px">Falar de si em vez de falar do problema dele</div>
        <div style="border-left:8px solid {L};margin-top:44px;padding:8px 0 8px 36px;font-size:54px;font-style:italic;font-weight:600;line-height:1.3">“Tenho 15 anos de experiência, sou pós-graduado...”</div>
        <div style="margin-top:60px;font-size:54px;font-weight:500;line-height:1.3">O cliente lê e pensa: <b>e eu?</b></div>
        <div style="margin-top:30px;font-size:46px;color:#3a3531;line-height:1.3">Ele quer saber se você entende o problema dele e como sair dali.</div></div></div>"""
    partes = [("nomeia o problema", "mostra que entende o que o cliente vive"), ("mostra o caminho", "um plano simples, em poucos passos"), ("chama pra ação", "diz exatamente qual é o próximo passo")]
    ent = "".join(f'<div style="padding:40px 0;border-top:3px solid {P}"><span style="{verb};font-size:72px">{a}</span><div style="font-size:38px;color:#3a3531;margin-top:10px;font-style:italic">{b}</div></div>' for a, b in partes)
    s5 = f"""<div class="slide" style="background:{O};color:{P}">{aba('G')}{topo(5)}
      <div class="abs" style="left:80px;right:130px;top:220px"><div class="lab" style="color:{B}">Ver também</div><div class="x" style="font-size:66px;margin-top:16px">O que o guia faz</div>
      <div style="margin-top:34px;border-bottom:3px solid {P}">{ent}</div></div></div>"""
    s6 = f"""<div class="slide" style="background:{O};color:{P}">{aba('V')}{topo(6)}
      <div class="abs" style="left:80px;right:130px;top:220px"><div class="lab" style="color:{B}">Exemplo de uso · no vídeo</div>
        <div style="{verb};font-size:118px;margin-top:30px">Todo bom vídeo começa pela <span style="color:{L}">dúvida do cliente.</span></div>
        <div style="border-top:4px solid {P};margin-top:50px;padding-top:34px;font-size:42px;line-height:1.3;font-weight:500">Quando você responde o que ele pergunta, ele se vê na história.<br><br><b>E quem se vê na história procura o guia.</b></div></div></div>"""
    s7 = f"""<div class="slide" style="background:{O};color:{P}"><div class="top">{logo('cor-fundo-claro')}<div class="lab" style="opacity:.6">{n} / {n}</div></div>
      <div class="abs" style="left:80px;right:80px;top:210px">
        <div class="x" style="font-size:76px">Agende um <span style="color:{B}">{RX} gratuito</span> com a nossa equipe.</div>
        <div class="box" style="margin-top:54px;background:{P};border-color:{P};color:{L}"><div class="lab" style="color:{O}">Comente</div><div class="x" style="font-size:150px">Heroi</div></div>
        <div class="t" style="margin-top:36px;font-size:32px;color:#3a3531">A gente te manda o link no direct. <b style="color:{P}">Exclusivo para profissionais com resultado no offline</b> que precisam escalar no digital.</div>
        <div class="lab" style="margin-top:40px;color:#3a3531">Salve e mande pra quem só fala do próprio currículo</div></div></div>"""
    salvar("2026-11-15_storybrand", [s1, s2, s3, s4, s5, s6, s7])

if __name__ == "__main__":
    for f in (placar_2bi, manchete_ia, rec_linkedin, dicionario_storybrand):
        f()
    print("ok")
