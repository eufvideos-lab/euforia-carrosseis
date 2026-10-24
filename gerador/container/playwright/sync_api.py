import subprocess, tempfile, pathlib, json, os
SHOT = pathlib.Path(__file__).parent.parent / "shot.js"
class Page:
    def __init__(s): s.html=""
    def set_content(s, h): s.html=h
    def evaluate(s,*a): pass
    def wait_for_timeout(s,*a): pass
    def screenshot(s, path, clip=None):
        f=tempfile.NamedTemporaryFile("w",suffix=".html",delete=False,encoding="utf-8"); f.write(s.html); f.close()
        subprocess.run(["node",str(SHOT),f.name,path],check=True); os.unlink(f.name)
class Br:
    def new_page(s,**k): return Page()
    def close(s): pass
class Ch:
    def launch(s,**k): return Br()
class PW:
    chromium=Ch()
    def __enter__(s): return s
    def __exit__(s,*a): pass
def sync_playwright(): return PW()
