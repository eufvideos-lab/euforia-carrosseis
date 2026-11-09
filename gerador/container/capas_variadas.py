#!/usr/bin/env python3
"""Capas com modelos variados (marca Play). Uso: python3 capas_variadas.py <modelo> <saida.png> '<json de textos>'"""
import sys, json, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import render_local as R
from playwright.sync_api import sync_playwright

ARCH = R.b64(pathlib.Path(__file__).parent / "Archivo.ttf")
D = re.search(r'd="([^"]+)"', R.ICON).group(1)
O, K, OFF, W = "#FF6518", "#050505", "#F2EFEA", "#FFFFFF"

BASE = f"""@font-face{{font-family:'A';font-weight:100 900;font-stretch:62% 125%;src:url(data:font/ttf;base64,{ARCH}) format('truetype')}}
*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;overflow:hidden}}
.cv{{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:Inter}}
.T{{font-family:'A';font-weight:900;text-transform:uppercase;line-height:.9;letter-spacing:-.01em}}
.w{{font-stretch:125%}} .c{{font-stretch:68%}} .n{{font-stretch:100%}}
.o{{color:{O}}} .tag{{display:inline-block;font:800 26px Inter;letter-spacing:.18em;text-transform:uppercase;padding:12px 20px;border-radius:8px}}
"""

def sym(color, style, outline=False):
    p = f'fill="none" stroke="{color}" stroke-width="2"' if outline else f'fill="{color}"'
    return f'<svg viewBox="0 0 150 122" style="position:absolute;{style}"><path {p} d="{D}"/></svg>'

def lock(color_txt, style, size=34, sym_c=None):
    return (f'<div style="position:absolute;display:flex;align-items:center;gap:14px;{style}">'
            f'<svg viewBox="0 0 150 122" style="width:{int(size*1.6)}px"><path fill="{sym_c or O}" d="{D}"/></svg>'
            f'<div class="T w" style="font-size:{size}px;line-height:.92;color:{color_txt}">Grupo<br>Euforia</div></div>')

def logo_branco(style="left:76px;top:70px;width:260px"):
    return f'<img src="{R.LOGO_BRANCA}" style="position:absolute;{style}">'

M = {}

# 1. Busca: barra do Google em fundo off-white
M["busca"] = lambda t: f"""<div class="cv" style="background:{OFF};color:{K}">{lock(K,'left:76px;top:70px')}
<span class="tag" style="position:absolute;left:76px;top:250px;background:{K};color:{OFF}">{t['tag']}</span>
<div style="position:absolute;left:76px;right:76px;top:340px;background:#fff;border-radius:999px;box-shadow:0 10px 40px rgba(0,0,0,.12);padding:34px 44px;display:flex;align-items:center;gap:26px">
<svg width="44" height="44" viewBox="0 0 24 24"><circle cx="10" cy="10" r="7" fill="none" stroke="#848484" stroke-width="2.4"/><path d="M15 15l6 6" stroke="#848484" stroke-width="2.4" stroke-linecap="round"/></svg>
<span style="font:500 40px Inter;color:#262626">{t['busca']}</span><span style="width:3px;height:46px;background:{O};margin-left:-14px"></span></div>
<div style="position:absolute;left:76px;right:76px;top:500px;display:flex;gap:18px">{''.join(f'<span style="font:600 26px Inter;padding:12px 22px;border:2px solid #d8d3cb;border-radius:999px;color:#3a3a3a">{x}</span>' for x in t['abas'])}</div>
<h1 class="T w" style="position:absolute;left:76px;right:76px;top:680px;font-size:96px">{t['titulo']}</h1>
<p style="position:absolute;left:76px;right:76px;bottom:90px;font:500 36px/1.3 Inter;color:#3a3a3a">{t['sub']}</p></div>"""

# 2. Laranja chapado, tipografia gigante preta
M["laranja"] = lambda t: f"""<div class="cv" style="background:{O};color:{K}">
<h1 class="T w" style="position:absolute;left:70px;right:60px;top:150px;font-size:150px;line-height:.88">{t['titulo']}</h1>
<p style="position:absolute;left:76px;right:76px;bottom:200px;font:600 40px/1.3 Inter">{t['sub']}</p>
{lock(K,'left:76px;bottom:76px',sym_c=K)}</div>"""

# 3. Riscado: palavra riscada e a virada em laranja
M["riscado"] = lambda t: f"""<div class="cv" style="background:{K};color:{W}">{logo_branco()}
<span class="tag" style="position:absolute;left:76px;top:240px;background:{O};color:{K}">{t['tag']}</span>
<div style="position:absolute;left:70px;right:60px;top:340px">
{''.join(f'<div class="T w" style="font-size:110px;color:#5a5a5a;position:relative;display:inline-block;margin-bottom:34px">{x}<span style="position:absolute;left:-10px;right:-10px;top:46%;height:14px;background:{O}"></span></div><br>' for x in t['riscadas'])}
{''.join(f'<div class="T w o" style="font-size:118px;margin-top:10px">{x}</div>' for x in t['viradas'])}</div>
<p style="position:absolute;left:76px;right:76px;bottom:96px;font:600 38px/1.3 Inter;color:#d8d3cb">{t['sub']}</p></div>"""

# 4. Número gigante sangrando
M["numero"] = lambda t: f"""<div class="cv" style="background:{OFF};color:{K}">{lock(K,'left:76px;top:70px')}
<div class="T c o" style="position:absolute;left:40px;top:200px;font-size:430px;line-height:.8;letter-spacing:-.03em;white-space:nowrap">{t['numero']}</div>
<h1 class="T w" style="position:absolute;left:76px;right:76px;top:700px;font-size:104px">{t['titulo']}</h1>
<div style="position:absolute;left:76px;right:76px;bottom:90px;border-top:3px solid {K};padding-top:28px;font:600 34px/1.35 Inter;color:#3a3a3a">{t['sub']}</div></div>"""

# 5. Conversa: balões de chat
M["chat"] = lambda t: f"""<div class="cv" style="background:#111;color:{W}">{logo_branco()}
<div style="position:absolute;right:76px;top:230px;max-width:780px;background:{O};color:{K};font:600 40px/1.3 Inter;padding:34px 40px;border-radius:40px 40px 8px 40px">{t['pergunta']}</div>
<div style="position:absolute;left:76px;top:470px;width:820px;background:#232323;border-radius:40px 40px 40px 8px;padding:36px 40px;font:500 34px/1.5 Inter;color:#d8d3cb">{t['resposta']}
{''.join(f'<div style="display:flex;gap:16px;align-items:center;margin-top:16px"><span style="color:{O};font-weight:800">{i+1}.</span><span style="display:inline-block;height:26px;width:{w}px;background:#4a4a4a;border-radius:13px;filter:blur(1px)"></span></div>' for i,w in enumerate([380,300,340]))}</div>
<h1 class="T w" style="position:absolute;left:76px;right:76px;bottom:200px;font-size:112px">{t['titulo']}</h1>
<p style="position:absolute;left:76px;right:76px;bottom:96px;font:600 36px Inter;color:#B8B8B8">{t['sub']}</p></div>"""

# 6. Card de vídeo (feed corporativo genérico)
M["video"] = lambda t: f"""<div class="cv" style="background:{K};color:{W}">{logo_branco()}
<span class="tag" style="position:absolute;left:76px;top:220px;background:{W};color:{K}">{t['tag']}</span>
<h1 class="T w" style="position:absolute;left:76px;right:76px;top:310px;font-size:100px">{t['titulo']}</h1>
<div style="position:absolute;left:76px;right:76px;top:690px;height:440px;border-radius:30px;background:#1c1c1c;border:2px solid #2e2e2e;overflow:hidden">
<div style="display:flex;align-items:center;gap:20px;padding:28px 32px"><span style="width:64px;height:64px;border-radius:50%;background:#3a3a3a"></span><span><span style="display:block;width:260px;height:20px;background:#4a4a4a;border-radius:10px"></span><span style="display:block;width:170px;height:16px;background:#333;border-radius:8px;margin-top:12px"></span></span></div>
<div style="position:absolute;left:32px;right:32px;top:120px;bottom:32px;border-radius:20px;background:#2a2a2a;display:flex;align-items:center;justify-content:center">
<div style="width:150px;height:150px;border-radius:50%;background:{O};display:flex;align-items:center;justify-content:center"><div style="width:0;height:0;border-left:52px solid {K};border-top:32px solid transparent;border-bottom:32px solid transparent;margin-left:14px"></div></div>
<span style="position:absolute;right:20px;bottom:18px;font:700 26px Inter;background:rgba(0,0,0,.7);padding:6px 14px;border-radius:8px">{t['duracao']}</span></div></div>
<p style="position:absolute;left:76px;right:76px;bottom:70px;font:600 34px Inter;color:#B8B8B8">{t['sub']}</p></div>"""

# 7. Livro: capa de livro em pé sobre laranja + frase
M["livro"] = lambda t: f"""<div class="cv" style="background:{O};color:{K}">{lock(K,'left:76px;top:70px',sym_c=K)}
<div style="position:absolute;right:90px;top:230px;width:420px;height:600px;background:{K};border-radius:6px 16px 16px 6px;box-shadow:24px 28px 0 rgba(0,0,0,.18);transform:rotate(4deg);padding:50px 40px;color:{OFF}">
<div style="position:absolute;left:0;top:0;bottom:0;width:22px;background:#1e1e1e;border-radius:6px 0 0 6px"></div>
<div class="T n" style="font-size:56px;line-height:.98">{t['livro']}</div><div style="width:80px;height:8px;background:{O};margin:34px 0"></div>
<div style="font:600 30px Inter;color:#B8B8B8">{t['autor']}</div></div>
<span class="tag" style="position:absolute;left:76px;top:250px;background:{K};color:{O}">{t['tag']}</span>
<div class="T" style="position:absolute;left:66px;top:300px;font-size:300px;line-height:1;font-family:Georgia,serif;color:{K}">“</div>
<h1 class="T w" style="position:absolute;left:76px;right:76px;top:900px;font-size:104px">{t['titulo']}</h1>
<p style="position:absolute;left:76px;right:76px;bottom:80px;font:600 34px Inter">{t['sub']}</p></div>"""

def render(modelo, saida, t):
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1350})
        pg.set_content(f"<!doctype html><html><head><meta charset='utf-8'><style>{BASE}</style></head><body>{M[modelo](t)}</body></html>")
        pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(200)
        pg.screenshot(path=saida, clip={"x":0,"y":0,"width":1080,"height":1350}); b.close()
    from PIL import Image
    Image.open(saida).convert("RGB").save(str(pathlib.Path(saida).with_suffix(".jpg")), "JPEG", quality=92)

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2], json.loads(sys.argv[3]))
