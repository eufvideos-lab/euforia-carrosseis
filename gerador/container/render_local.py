#!/usr/bin/env python3
"""Gerador de carrossel Grupo Euforia v2 (estilo notícia/editorial, preto + laranja).

Uso: python3 render2.py roteiro.json pasta_saida/

Roteiro: {"slides":[...], "legenda": "..."}
Slide "capa": foto (png recortado), selo, titulo_linhas [[texto, destaque?]...], subtitulo, credito
Slide "conteudo": tema ("claro"|"escuro"), blocos [...], barra (texto do rodapé), credito
Slide "cta": titulo, texto, palavra, rodape
Blocos: titulo, texto, chips, stats, citacao, comparativo, gigante, numerados, foto, fonte, espaco
Marcação no texto: **negrito**, ==tarja laranja==, *laranja*, __sublinhado laranja__
"""
import json, sys, html, base64, pathlib, re
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path("/home/user/euforia-carrosseis/gerador")
FONTS = ROOT / "node_modules/@fontsource"
MARCA = ROOT / "assets/marca"

def b64(path):
    return base64.b64encode(pathlib.Path(path).read_bytes()).decode()

def ff(family, path, weight):
    return f"@font-face{{font-family:'{family}';font-weight:{weight};src:url(data:font/woff2;base64,{b64(path)}) format('woff2');}}"

FONT_CSS = "@font-face{font-family:'Barlow Condensed';font-weight:100 900;font-stretch:62% 125%;src:url(data:font/ttf;base64,"+b64(pathlib.Path(__file__).parent/"Archivo.ttf")+") format('truetype');}*{font-stretch:68% !important}"

def img_uri(path):
    ext = pathlib.Path(path).suffix.lower().strip(".")
    mime = "image/png" if ext == "png" else "image/jpeg"
    return f"data:{mime};base64,{b64(path)}"

LOGO_BRANCA = img_uri(MARCA / "logo_branca.png")

ICON = """<svg class="icone" viewBox="0 0 100 140" xmlns="http://www.w3.org/2000/svg"><defs>
<linearGradient id="ig" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFB072"/><stop offset="1" stop-color="#FF5A00"/></linearGradient></defs>
<rect x="0" y="4" width="100" height="30" rx="15" fill="url(#ig)"/><rect x="0" y="55" width="100" height="30" rx="15" fill="url(#ig)"/><rect x="0" y="106" width="100" height="30" rx="15" fill="url(#ig)"/></svg>"""

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
.claro{background:#F4F2EE;color:#141414}
.escuro{background:#0A0A0A;color:#fff}
.escuro::before{content:"";position:absolute;inset:0;background:
 radial-gradient(70% 45% at 100% 0%,rgba(255,90,0,.28),transparent 70%),
 radial-gradient(80% 40% at 0% 105%,rgba(255,60,0,.22),transparent 70%)}
.grain{position:absolute;inset:0;pointer-events:none;opacity:.10;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.icone{position:absolute;top:64px;left:80px;width:40px;height:auto}
.num{position:absolute;top:70px;right:80px;font:600 24px 'Inter';opacity:.45}
.corpo{position:absolute;left:80px;right:80px;top:170px;bottom:190px;display:flex;flex-direction:column;justify-content:center;gap:34px}
.corpo.topo{justify-content:flex-start}
/* texto */
.t{font:800 56px/1.12 'Inter';letter-spacing:-.02em}
.t.m{font-size:48px}
.p{font:400 34px/1.45 'Inter';opacity:.92}
.p.pequeno{font-size:29px}
b{font-weight:800}
.tarja{background:linear-gradient(90deg,#FF7A1A,#FF4D00);color:#fff;padding:.02em .22em .06em;border-radius:.18em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.lj{color:#FF5A00}
.escuro .lj{color:#FF8A3D}
.sub{text-decoration:underline;text-decoration-color:#FF5A00;text-decoration-thickness:5px;text-underline-offset:8px}
/* chips */
.chips{display:flex;flex-wrap:wrap;gap:16px}
.chip{display:flex;align-items:center;gap:14px;background:#fff;border-radius:16px;padding:18px 26px;font:700 30px 'Inter';box-shadow:0 6px 24px rgba(0,0,0,.08)}
.escuro .chip{background:#1A1A1A;box-shadow:none;border:1px solid #2A2A2A}
.chip i{width:14px;height:14px;border-radius:50%;background:linear-gradient(135deg,#FFB072,#FF4D00);display:block}
/* stats */
.stats{display:grid;gap:18px}
.stat{display:flex;align-items:center;gap:26px;background:#fff;border-radius:22px;padding:24px 30px;box-shadow:0 8px 30px rgba(0,0,0,.08)}
.escuro .stat{background:#161616;box-shadow:none;border:1px solid #262626}
.stat .v{font:800 64px/1 'Barlow Condensed';background:linear-gradient(180deg,#FF9A4A,#FF4D00);-webkit-background-clip:text;background-clip:text;color:transparent;min-width:260px}
.stat .l{font:500 28px/1.3 'Inter'}
/* citação */
.cit{position:relative;padding-left:40px;border-left:8px solid #FF5A00}
.cit .q{font:800 60px/1.1 'Inter';letter-spacing:-.02em}
.cit .a{margin-top:22px;font:500 28px 'Inter';opacity:.7}
/* comparativo */
.comp{display:grid;gap:22px}
.linha{background:#fff;border-radius:24px;padding:30px 34px;box-shadow:0 8px 30px rgba(0,0,0,.08)}
.escuro .linha{background:#161616;border:1px solid #262626;box-shadow:none}
.linha .n{font:800 34px 'Inter';margin-bottom:18px}
.linha .n small{font:500 24px 'Inter';opacity:.6;margin-left:10px}
.barras{display:grid;grid-template-columns:200px 1fr;gap:12px 20px;align-items:center;font:600 26px 'Inter'}
.bar{height:44px;border-radius:12px;display:flex;align-items:center;padding:0 18px;font:800 28px 'Inter';color:#fff;white-space:nowrap}
.bar.fat{background:#2B2B2B}
.claro .bar.fat{background:#3A3A3A}
.bar.neg{background:#D7261E}
.bar.pos{background:linear-gradient(90deg,#FF7A1A,#FF4D00)}
/* gigante */
.gig{font:800 150px/.9 'Barlow Condensed';text-transform:uppercase;letter-spacing:-.01em}
.gig.m{font-size:122px}
.gig .g2{display:inline-block;background:linear-gradient(90deg,#FF7A1A,#FF4D00);color:#fff;padding:0 .12em .02em;border-radius:14px;margin-top:10px}
/* numerados */
.nums{display:grid;gap:22px}
.it{display:grid;grid-template-columns:78px 1fr;gap:24px;align-items:start}
.it .k{width:78px;height:78px;border-radius:20px;background:linear-gradient(135deg,#FF8A3D,#FF4D00);color:#fff;font:800 46px/78px 'Barlow Condensed';text-align:center}
.it .h{font:800 38px/1.2 'Inter'}
.it .d{font:400 31px/1.4 'Inter';opacity:.85;margin-top:6px}
.rot{font:800 24px 'Inter';letter-spacing:.14em;text-transform:uppercase;color:#FF5A00}
.escuro .rot{color:#FF8A3D}
.fonte{font:500 22px 'Inter';opacity:.5}
/* foto lateral */
.foto{position:absolute;right:-40px;bottom:0;height:78%;filter:drop-shadow(0 0 60px rgba(255,80,0,.25))}
.foto.fade{-webkit-mask-image:linear-gradient(180deg,#000 70%,transparent 100%);mask-image:linear-gradient(180deg,#000 70%,transparent 100%)}
/* barra inferior */
.barra{position:absolute;left:50%;transform:translateX(-50%);bottom:64px;min-width:700px;max-width:960px;white-space:nowrap;display:flex;align-items:center;justify-content:center;gap:18px;padding:22px 30px 22px 40px;border-radius:20px;background:linear-gradient(90deg,#FF7A1A,#FF4D00);color:#fff;font:700 29px/1.25 'Inter';box-shadow:0 12px 34px rgba(255,77,0,.35)}
.barra .seta{flex:none;width:46px;height:46px;border-radius:50%;background:#fff;color:#FF4D00;display:grid;place-items:center;font:900 28px/1 'Inter'}
.credito{position:absolute;right:26px;top:50%;transform:rotate(-90deg) translateX(50%);transform-origin:right top;font:500 16px 'Inter';opacity:.5;white-space:nowrap}
/* capa */
.capa{background:#0A0A0A;color:#fff}
.capa .halo{position:absolute;left:50%;top:40%;width:1200px;height:1200px;transform:translate(-50%,-50%);background:radial-gradient(circle,rgba(255,100,0,.55) 0%,rgba(255,70,0,.18) 35%,transparent 62%)}
.capa .pessoa{position:absolute;left:50%;transform:translateX(-50%);bottom:220px;width:780px;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 14%,#000 86%,transparent 100%),linear-gradient(180deg,#000 70%,transparent 99%);-webkit-mask-composite:source-in;mask-image:linear-gradient(90deg,transparent 0,#000 14%,#000 86%,transparent 100%),linear-gradient(180deg,#000 70%,transparent 99%);mask-composite:intersect}
.capa .base{position:absolute;left:0;right:0;bottom:0;height:700px;background:linear-gradient(180deg,transparent,#0A0A0A 42%)}
.capa .topo{position:absolute;left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(10,10,10,.85),transparent)}
.capa .logo{position:absolute;top:58px;left:50%;transform:translateX(-50%);width:210px}
.capa .txt{position:absolute;left:70px;right:70px;bottom:90px;text-align:center}
.selo{display:inline-block;background:#fff;color:#FF4D00;font:800 38px/1 'Barlow Condensed';letter-spacing:.04em;text-transform:uppercase;padding:12px 22px 10px;border-radius:10px;transform:rotate(-2deg)}
.hl{font:800 142px/.9 'Barlow Condensed';text-transform:uppercase;margin-top:22px;letter-spacing:-.005em}
.hl span{display:inline-block}
.hl .d{background:linear-gradient(90deg,#FF7A1A,#FF4D00);padding:0 .14em .02em;border-radius:14px;margin-top:10px}
.capa .st{margin-top:28px;font:600 36px/1.3 'Inter'}
/* cta */
.cta .logo{position:absolute;top:64px;left:50%;transform:translateX(-50%);width:230px}
.cta .corpo{text-align:center;align-items:center}
.cta .t.m{font-size:58px}
.cta .p{font-size:36px}
.palavra{display:inline-block;font:800 120px/1 'Barlow Condensed';letter-spacing:.03em;background:linear-gradient(90deg,#FF7A1A,#FF4D00);color:#fff;padding:14px 40px 10px;border-radius:22px;box-shadow:0 16px 50px rgba(255,77,0,.4)}
.rod{position:absolute;bottom:70px;left:0;right:0;text-align:center;font:500 26px 'Inter';opacity:.6}

/* ===== institucional ===== */
.hl.menor{font-size:112px}
.capa .fundo{position:absolute;inset:0;background-size:cover;background-position:center;filter:saturate(.9) brightness(.8)}
.capa.comfundo .halo{opacity:.55}
.capa.comfundo .base{height:820px;background:linear-gradient(180deg,transparent,rgba(10,10,10,.92) 38%,#0A0A0A 60%)}
.full{position:absolute;inset:0;background-size:cover;background-position:center;filter:brightness(.75)}
.fullgrad{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.55) 0%,rgba(10,10,10,0) 25%,rgba(10,10,10,.2) 45%,rgba(10,10,10,.92) 70%,#0A0A0A 100%)}
.fototxt{position:absolute;left:80px;right:80px;bottom:190px;display:flex;flex-direction:column;gap:26px;color:#fff}
.nums4{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.n4{background:#fff;border-radius:26px;padding:34px 30px;box-shadow:0 8px 30px rgba(0,0,0,.08)}
.escuro .n4{background:#161616;border:1px solid #262626;box-shadow:none}
.n4 .v{font:800 96px/1 'Barlow Condensed';background:linear-gradient(180deg,#FF9A4A,#FF4D00);-webkit-background-clip:text;background-clip:text;color:transparent}
.n4 .l{margin-top:12px;font:600 28px/1.3 'Inter'}
.canais{display:grid;gap:22px}
.canal{display:flex;align-items:center;gap:34px;background:#fff;border-radius:30px;padding:34px 36px;box-shadow:0 8px 30px rgba(0,0,0,.08)}
.escuro .canal{background:#161616;border:1px solid #262626;box-shadow:none}
.canal img{width:190px;height:190px;border-radius:50%;object-fit:cover;flex:none;box-shadow:0 0 0 6px #fff,0 0 0 10px #FF6A1A}
.escuro .canal img{box-shadow:0 0 0 6px #161616,0 0 0 10px #FF6A1A}
.canal .cn{font:800 44px/1.12 'Inter'}
.canal .ch{margin-top:10px;font:500 30px 'Inter';opacity:.6}
.canal .yt{margin-left:auto;flex:none;width:64px;height:46px;border-radius:12px;background:#FF0000;position:relative}
.canal .yt::after{content:"";position:absolute;left:25px;top:13px;border-left:18px solid #fff;border-top:10px solid transparent;border-bottom:10px solid transparent}
.valor .vn{font:800 230px/.8 'Barlow Condensed';background:linear-gradient(180deg,#FFB072,#FF4D00);-webkit-background-clip:text;background-clip:text;color:transparent}
.valor .vt{font:800 34px 'Inter';letter-spacing:.12em;text-transform:uppercase;margin-top:26px;color:#FF5A00}
.escuro .valor .vt{color:#FF8A3D}
.valor .vf{font:800 88px/1.02 'Barlow Condensed';text-transform:uppercase;margin-top:18px}
.valor .vd{font:400 34px/1.45 'Inter';opacity:.9;margin-top:26px}
.imagem{width:100%;border-radius:28px;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.25)}
.imagem img{display:block;width:100%;height:100%;object-fit:cover}
.galeria{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:330px 330px;gap:18px}
.galeria div{border-radius:24px;overflow:hidden}
.galeria div:first-child{grid-row:span 2}
.galeria img{width:100%;height:100%;object-fit:cover;display:block}

/* ===== v3: cabeçalho, progresso e blocos novos ===== */
.prog{position:absolute;top:34px;left:80px;right:80px;display:flex;gap:8px}
.prog i{flex:1;height:6px;border-radius:3px;background:currentColor;opacity:.13}
.prog i.on{opacity:1;background:linear-gradient(90deg,#FF8A3D,#FF4D00)}
.cat{position:absolute;top:72px;left:138px;font:800 21px 'Inter';letter-spacing:.16em;text-transform:uppercase;opacity:.55}
.claro .pontos{position:absolute;inset:0;background-image:radial-gradient(rgba(20,20,20,.07) 1.6px,transparent 1.8px);background-size:34px 34px;-webkit-mask-image:linear-gradient(180deg,transparent 0,#000 30%,#000 70%,transparent 100%);mask-image:linear-gradient(180deg,transparent 0,#000 30%,#000 70%,transparent 100%)}
.mc{font:800 98px/.95 'Barlow Condensed';text-transform:uppercase;letter-spacing:-.005em}
.mc.m{font-size:82px}
.mc .tarja{border-radius:12px;padding:0 .12em}
/* linha do tempo */
.tl{position:relative;display:grid;gap:26px;padding-left:64px}
.tl::before{content:"";position:absolute;left:18px;top:14px;bottom:14px;width:4px;border-radius:2px;background:linear-gradient(180deg,#FFB072,#FF4D00)}
.tl .e{position:relative}
.tl .e::before{content:"";position:absolute;left:-58px;top:8px;width:28px;height:28px;border-radius:50%;background:#F4F2EE;border:6px solid #FF5A00;box-sizing:border-box}
.escuro .tl .e::before{background:#0A0A0A}
.tl .e.ult::before{background:#FF5A00;box-shadow:0 0 0 8px rgba(255,90,0,.2)}
.tl .ano{font:800 30px 'Barlow Condensed';letter-spacing:.06em;color:#FF5A00;text-transform:uppercase}
.escuro .tl .ano{color:#FF8A3D}
.tl .h{font:800 38px/1.18 'Inter';margin-top:2px}
.tl .d{font:400 29px/1.38 'Inter';opacity:.8;margin-top:4px}
/* funil */
.funil{display:grid;gap:14px;justify-items:center}
.fd{display:flex;align-items:center;justify-content:space-between;gap:24px;border-radius:22px;padding:26px 36px;color:#fff;box-shadow:0 10px 30px rgba(255,77,0,.18)}
.fd .fl{font:800 34px/1.15 'Inter'}
.fd .fl small{display:block;font:500 24px/1.3 'Inter';opacity:.85;margin-top:4px}
.fd .fv{font:800 58px/1 'Barlow Condensed';white-space:nowrap;text-align:right}
.fd .fv small{display:block;font:600 20px 'Inter';opacity:.85;margin-top:4px;letter-spacing:.02em}
/* número herói */
.heroi .hn{font:800 210px/.85 'Barlow Condensed';letter-spacing:-.01em;background:linear-gradient(180deg,#FFB072,#FF4D00);-webkit-background-clip:text;background-clip:text;color:transparent}
.heroi .hl2{font:800 40px/1.2 'Inter';margin-top:18px}
/* destaque (cartão) */
.dq{background:#111;color:#fff;border-radius:26px;padding:34px 38px;border-left:10px solid #FF5A00;font:500 32px/1.42 'Inter'}
.escuro .dq{background:#1A1A1A}
.dq b{color:#FF8A3D}
/* capa tipográfica */
.capa.numero .aneis{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);width:1500px;height:1500px;border-radius:50%;background:repeating-radial-gradient(circle,rgba(255,110,30,.16) 0 2px,transparent 2px 70px);-webkit-mask-image:radial-gradient(circle,#000 20%,transparent 62%);mask-image:radial-gradient(circle,#000 20%,transparent 62%)}
.capa.numero .halo{top:44%}
.capa.numero .txt{bottom:auto;top:50%;transform:translateY(-46%)}
.capa .gnum{font:800 300px/.82 'Barlow Condensed';letter-spacing:-.02em;background:linear-gradient(180deg,#FFFFFF 0%,#FFD2B0 45%,#FF6A1A 100%);-webkit-background-clip:text;background-clip:text;color:transparent;margin-top:30px;filter:drop-shadow(0 18px 50px rgba(255,80,0,.35))}
.capa .gnum2{font:800 96px/.95 'Barlow Condensed';text-transform:uppercase;margin-top:6px}
.capa .gnum2 .d{background:linear-gradient(90deg,#FF7A1A,#FF4D00);padding:0 .14em .02em;border-radius:12px}
.capa .arrasta{position:absolute;bottom:62px;left:0;right:0;text-align:center;font:700 24px 'Inter';letter-spacing:.2em;text-transform:uppercase;opacity:.55}
/* cta comentário */
.coment{display:inline-flex;align-items:center;gap:22px;background:#fff;color:#141414;border-radius:999px;padding:18px 40px 18px 18px;box-shadow:0 18px 50px rgba(255,77,0,.35)}
.coment .av{width:78px;height:78px;border-radius:50%;background:linear-gradient(135deg,#FFB072,#FF4D00);flex:none}
.coment .cw{font:800 76px/1 'Barlow Condensed';letter-spacing:.04em;color:#FF4D00}
.coment .cur{width:5px;height:64px;background:#FF4D00;border-radius:3px}
"""

def rich(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"==(.+?)==", r'<span class="tarja">\1</span>', t)
    t = re.sub(r"__(.+?)__", r'<span class="sub">\1</span>', t)
    t = re.sub(r"\*(.+?)\*", r'<span class="lj">\1</span>', t)
    return t.replace("\n", "<br>")

def bloco(b):
    k = b["tipo"]
    if k == "titulo":
        return f'<div class="t {b.get("tam","")}">{rich(b["texto"])}</div>'
    if k == "texto":
        return "".join(f'<div class="p {b.get("tam","")}">{rich(x)}</div>' for x in b["texto"].split("\n\n"))
    if k == "rotulo":
        return f'<div class="rot">{rich(b["texto"])}</div>'
    if k == "chips":
        return '<div class="chips">' + "".join(f'<div class="chip"><i></i>{rich(c)}</div>' for c in b["itens"]) + "</div>"
    if k == "stats":
        return '<div class="stats">' + "".join(f'<div class="stat"><div class="v">{rich(v)}</div><div class="l">{rich(l)}</div></div>' for v, l in b["itens"]) + "</div>"
    if k == "citacao":
        return f'<div class="cit"><div class="q">{rich(b["texto"])}</div><div class="a">{rich(b["autor"])}</div></div>'
    if k == "comparativo":
        out = '<div class="comp">'
        for L in b["linhas"]:
            mx = max(x["valor"] for L2 in b["linhas"] for x in L2["barras"])
            out += f'<div class="linha"><div class="n">{rich(L["nome"])}<small>{rich(L.get("detalhe",""))}</small></div><div class="barras">'
            for x in L["barras"]:
                w = max(30, 100 * x["valor"] / mx)
                out += f'<div>{rich(x["rotulo"])}</div><div><div class="bar {x["cor"]}" style="width:{w:.0f}%">{rich(x["texto"])}</div></div>'
            out += "</div></div>"
        return out + "</div>"
    if k == "gigante":
        return f'<div class="gig {b.get("tam","")}">{rich(b["linha1"])}<br><span class="g2">{rich(b["linha2"])}</span></div>'
    if k == "numerados":
        return '<div class="nums">' + "".join(
            f'<div class="it"><div class="k">{i}</div><div><div class="h">{rich(h)}</div><div class="d">{rich(d)}</div></div></div>'
            for i, (h, d) in enumerate(b["itens"], b.get("inicio", 1))) + "</div>"
    if k == "fonte":
        return f'<div class="fonte">{rich(b["texto"])}</div>'
    if k == "numeros":
        return '<div class="nums4">' + "".join(f'<div class="n4"><div class="v">{rich(v)}</div><div class="l">{rich(l)}</div></div>' for v, l in b["itens"]) + "</div>"
    if k == "canais":
        return '<div class="canais">' + "".join(
            f'<div class="canal"><img src="{img_uri(ROOT / c["foto"])}"><div><div class="cn">{rich(c["nome"])}</div><div class="ch">{rich(c.get("handle",""))}</div></div><i class="yt"></i></div>'
            for c in b["itens"]) + "</div>"
    if k == "valor":
        return f'<div class="valor"><div class="vn">{html.escape(b["numero"])}</div><div class="vt">{rich(b["titulo"])}</div><div class="vf">{rich(b["frase"])}</div><div class="vd">{rich(b.get("texto",""))}</div></div>'
    if k == "imagem":
        return f'<div class="imagem" style="height:{b.get("altura",520)}px"><img src="{img_uri(ROOT / b["foto"])}" style="object-position:{b.get("posicao","center")}"></div>'
    if k == "galeria":
        return '<div class="galeria">' + "".join(f'<div><img src="{img_uri(ROOT / f)}"></div>' for f in b["fotos"]) + "</div>"
    if k == "manchete":
        return f'<div class="mc {b.get("tam","")}">{rich(b["texto"])}</div>'
    if k == "linha_tempo":
        its=b["itens"];out='<div class="tl">'
        for j,(a,h,d) in enumerate(its):
            out+=f'<div class="e{" ult" if j==len(its)-1 else ""}"><div class="ano">{rich(a)}</div><div class="h">{rich(h)}</div>'+(f'<div class="d">{rich(d)}</div>' if d else '')+'</div>'
        return out+'</div>'
    if k == "funil":
        its=b["itens"];n=len(its);out='<div class="funil">'
        for j,(l,sl,v,sv) in enumerate(its):
            w=100-j*(34/max(1,n-1)); op=0.72+0.28*j/max(1,n-1)
            out+=f'<div class="fd" style="width:{w:.0f}%;background:linear-gradient(90deg,rgba(255,122,26,{op:.2f}),rgba(255,77,0,{op:.2f}))"><div class="fl">{rich(l)}<small>{rich(sl)}</small></div><div class="fv">{rich(v)}<small>{rich(sv)}</small></div></div>'
        return out+'</div>'
    if k == "heroi":
        return f'<div class="heroi"><div class="hn">{html.escape(b["numero"])}</div><div class="hl2">{rich(b["texto"])}</div></div>'
    if k == "destaque":
        return f'<div class="dq">{rich(b["texto"])}</div>'
    if k == "espaco":
        return f'<div style="height:{b.get("px",20)}px"></div>'
    raise ValueError(k)

def cabecalho(i, n, cat):
    prog = '<div class="prog">' + "".join(f'<i class="{"on" if j<=i else ""}"></i>' for j in range(1, n+1)) + '</div>'
    return prog + (f'<div class="cat">{html.escape(cat)}</div>' if cat else "")

def slide(s, i, n, cat=""):
    tipo = s["tipo"]
    if tipo == "capa_numero":
        return f'''<div class="s capa numero"><div class="aneis"></div><div class="halo"></div><div class="topo"></div><img class="logo" src="{LOGO_BRANCA}">
<div class="txt"><span class="selo">{rich(s["selo"])}</span><div class="gnum">{html.escape(s["numero"])}</div><div class="gnum2">{"".join(f'<span class="{"d" if d else ""}">{rich(t)}</span><br>' for t, d in s["linhas"])}</div><div class="st">{rich(s["subtitulo"])}</div></div>
<div class="arrasta">Arrasta pro lado →</div><div class="grain"></div></div>'''
    cred = f'<div class="credito">{html.escape(s["credito"])}</div>' if s.get("credito") else ""
    if tipo == "capa":
        linhas = "".join(
            f'<span class="{"d" if dest else ""}">{rich(txt)}</span><br>' for txt, dest in s["titulo_linhas"])
        if s.get("fundo"):
            topo = f'<div class="fundo" style="background-image:url({img_uri(ROOT / s["fundo"])});background-position:{s.get("posicao","center")}"></div>'
            cls = "s capa comfundo"
        else:
            topo = f'<div class="halo"></div><img class="pessoa" src="{img_uri(s["foto"])}" style="{s.get("foto_estilo","")}">'
            cls = "s capa"
        tam = "menor" if s.get("titulo_menor") else ""
        return f'''<div class="{cls}">{topo}
<div class="base"></div><div class="topo"></div><img class="logo" src="{LOGO_BRANCA}">
<div class="txt"><span class="selo">{rich(s["selo"])}</span><div class="hl {tam}">{linhas}</div><div class="st">{rich(s["subtitulo"])}</div></div>{cred}<div class="grain"></div></div>'''
    if tipo == "cta":
        palavra = (f'<div class="coment"><i class="av"></i><span class="cw">{html.escape(s["palavra"])}</span><i class="cur"></i></div>' if s.get("estilo") == "comentario"
                   else f'<span class="palavra">{html.escape(s["palavra"])}</span>')
        return f'''<div class="s escuro cta"><img class="logo" src="{LOGO_BRANCA}"><div class="corpo">
<div class="t m">{rich(s["titulo"])}</div><div class="p">{rich(s["texto"])}</div><div>{palavra}</div>
<div class="p pequeno">{rich(s.get("apos",""))}</div></div><div class="rod">{rich(s.get("rodape",""))}</div><div class="grain"></div></div>'''
    if tipo == "foto":
        corpo = "".join(bloco(b) for b in s["blocos"])
        barra = f'<div class="barra">{rich(s["barra"])}<span class="seta">→</span></div>' if s.get("barra") else ""
        return f'''<div class="s escuro"><div class="full" style="background-image:url({img_uri(ROOT / s["fundo"])});background-position:{s.get("posicao","center")}"></div><div class="fullgrad"></div>{ICON}<div class="num">{i}/{n}</div>
<div class="fototxt">{corpo}</div>{barra}<div class="grain"></div></div>'''
    tema = s.get("tema", "claro")
    foto = ""
    if s.get("foto"):
        foto = f'<img class="foto fade" src="{img_uri(s["foto"])}" style="{s.get("foto_estilo","")}">'
    corpo = "".join(bloco(b) for b in s["blocos"])
    barra = f'<div class="barra">{rich(s["barra"])}<span class="seta">→</span></div>' if s.get("barra") else ""
    alinh = "topo" if s.get("alinhar") == "topo" else ""
    estilo = s.get("corpo_estilo", "")
    cab = cabecalho(i, n, cat) if cat else ""
    pontos = '<div class="pontos"></div>' if (cat and tema == "claro") else ""
    return f'''<div class="s {tema}">{pontos}{foto}{ICON}{cab}<div class="num">{i}/{n}</div>
<div class="corpo {alinh}" style="{estilo}">{corpo}</div>{barra}{cred}<div class="grain"></div></div>'''

def render(roteiro, saida):
    data = json.loads(pathlib.Path(roteiro).read_text(encoding="utf-8"))
    base = pathlib.Path(roteiro).parent
    out = pathlib.Path(saida); out.mkdir(parents=True, exist_ok=True)
    slides = data["slides"]
    for s in slides:
        if s.get("foto") and not pathlib.Path(s["foto"]).is_absolute():
            s["foto"] = str((ROOT / s["foto"]).resolve())
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 1080, "height": 1350})
        for i, s in enumerate(slides, 1):
            pg.set_content(f"<!doctype html><html><head><meta charset='utf-8'><style>{FONT_CSS}{CSS}</style></head><body>{slide(s, i, len(slides), data.get('categoria',''))}</body></html>")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            f = out / f"slide_{i:02d}.png"
            pg.screenshot(path=str(f), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            from PIL import Image
            Image.open(f).convert("RGB").save(f.with_suffix(".jpg"), "JPEG", quality=92)  # API do Instagram só aceita JPEG
            print(f)
        br.close()
    if data.get("legenda"):
        (out / "legenda.txt").write_text(data["legenda"], encoding="utf-8")

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])
