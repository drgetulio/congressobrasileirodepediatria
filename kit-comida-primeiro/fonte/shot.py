import sys
from playwright.sync_api import sync_playwright
# uso: python3 shot.py arquivo.html saida.png largura [dark]
f, out, w = sys.argv[1], sys.argv[2], int(sys.argv[3]); dark = len(sys.argv) > 4
with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={'width': w, 'height': 900}, color_scheme='dark' if dark else 'light')
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
    pg.goto('file://' + f); pg.wait_for_timeout(400)
    sw = pg.evaluate('document.documentElement.scrollWidth')
    pg.screenshot(path=out, full_page=True)
    print('scrollWidth', sw, 'viewport', w, 'erros', [e for e in errs if 'fonts.g' not in e][:5])
    br.close()
