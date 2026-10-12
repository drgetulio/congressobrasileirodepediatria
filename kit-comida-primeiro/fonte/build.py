# -*- coding: utf-8 -*-
"""Monta os materiais impressos do Kit Comida Primeiro: src/*.html -> out/pdf/*.pdf (+ html intermediário).
Uso: python3 build.py [prefixos...]   ex.: python3 build.py 05 06"""
import os as _os
KIT = _os.path.dirname(_os.path.abspath(__file__))
import json, re, sys, os, glob, html
sys.path.insert(0, KIT)
from refs import REF, SHORT

FD = _os.path.join(_os.path.dirname(KIT), 'node_modules', '@fontsource')
AUD = {'ped': ('Para o pediatra', 'aud-ped'), 'fam': ('Para as famílias', 'aud-fam'),
       'eq': ('Para a equipe e o ensino', 'aud-eq'), 'app': ('Ferramenta', 'aud-app')}

def ff(family, folder, weight, style='normal'):
    return (f"@font-face{{font-family:'{family}';src:url('file://{FD}/{folder}/files/{folder}-latin-{weight}-{style}.woff2') format('woff2');"
            f"font-weight:{weight};font-style:{style};}}\n"
            f"@font-face{{font-family:'{family}';src:url('file://{FD}/{folder}/files/{folder}-latin-ext-{weight}-{style}.woff2') format('woff2');"
            f"font-weight:{weight};font-style:{style};unicode-range:U+0100-024F,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF;}}\n")

FONTS = ''.join([ff('Source Serif 4', 'source-serif-4', w, s) for w, s in [(400, 'normal'), (400, 'italic'), (600, 'normal'), (600, 'italic'), (700, 'normal')]] +
                [ff('IBM Plex Sans', 'ibm-plex-sans', w, s) for w, s in [(400, 'normal'), (400, 'italic'), (500, 'normal'), (600, 'normal'), (600, 'italic'), (700, 'normal')]] +
                [ff('IBM Plex Mono', 'ibm-plex-mono', w, 'normal') for w in (400, 500)])
CSS = open(KIT + '/base.css').read()

ATTR_LONG = ('Material de apoio da aula “Creatina e Whey Protein: modismo inadequado”, 42º Congresso Brasileiro de Pediatria, '
             'Belo Horizonte, outubro de 2026. Getúlio Bernardo Morato Filho, Escola Superior de Ciências da Saúde, Brasília, DF.')
ATTR_FAM = 'Orientação geral, que não substitui a consulta. Kit Comida Primeiro, Getúlio Bernardo Morato Filho, Escola Superior de Ciências da Saúde, Brasília, DF.'
ATTR_SHORT = 'Aula “Creatina e Whey Protein: modismo inadequado”, 42º Congresso Brasileiro de Pediatria, 2026.'

SUP = re.compile(r'\[\[ref:([a-z0-9_,]+)\]\]')
SIZES = {'A4': ('210mm', '297mm'), 'A5': ('148mm', '210mm'), 'A6': ('105mm', '148mm'), 'A3': ('297mm', '420mm')}

def link_ref(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'doi:(\S+?)(\.?)(\s|$)', lambda m: f'doi:<a href="https://doi.org/{m.group(1)}">{m.group(1)}</a>{m.group(2)}{m.group(3)}', t)
    t = re.sub(r'(Disponível em: )(https?://\S+)', lambda m: f'{m.group(1)}<a href="{m.group(2)}">{m.group(2)}</a>', t)
    return t

def process(src):
    first, body = src.split('\n', 1)
    meta = json.loads(re.match(r'<!--(.*)-->', first.strip()).group(1))
    order = []
    def num(m):
        keys = m.group(1).split(',')
        ns = []
        for k in keys:
            if k not in REF:
                raise KeyError(f"referência desconhecida: {k} em {meta['slug']}")
            if k not in order:
                order.append(k)
            ns.append(order.index(k) + 1)
        return '<sup class="r">' + ','.join(str(n) for n in sorted(ns)) + '</sup>'
    body = SUP.sub(num, body)
    body = re.sub(r'\[\[cite:([a-z0-9_]+)\]\]', lambda m: link_ref(REF[m.group(1)]), body)
    if '[[allrefs' in body:
        keys = set()
        for f in glob.glob(KIT + '/src/*.html'):
            for m in re.finditer(r'\[\[(?:ref|cite):([a-z0-9_,]+)\]\]', open(f).read()):
                keys.update(m.group(1).split(','))
        def sk(k):
            s = REF[k]
            return re.sub(r'^(van der |van |de )', '', s, flags=re.I).lower()
        allk = sorted(keys, key=sk)
        half = (len(allk) + 1) // 2 - 3
        body = body.replace('[[allrefs]]', '<ol class="allrefs">' + ''.join(f'<li>{link_ref(REF[k])}</li>' for k in allk) + '</ol>')
        body = body.replace('[[allrefs:1]]', '<ol class="allrefs">' + ''.join(f'<li>{link_ref(REF[k])}</li>' for k in allk[:half]) + '</ol>')
        body = body.replace('[[allrefs:2]]', f'<ol class="allrefs" start="{half+1}">' + ''.join(f'<li>{link_ref(REF[k])}</li>' for k in allk[half:]) + '</ol>')
        meta['_nall'] = len(allk)
    srcs = ''
    if order:
        if meta.get('short'):
            srcs = ('<div class="sources"><span class="lbl">Fontes (referências completas no item 20)</span><ol>' +
                    ''.join(f'<li>{html.escape(SHORT[k])}</li>' for k in order) + '</ol></div>')
        else:
            cls = 'sources two' if len(order) >= 6 else 'sources'
            srcs = (f'<div class="{cls}"><span class="lbl">Fontes</span><ol>' +
                    ''.join(f'<li>{link_ref(REF[k])}</li>' for k in order) + '</ol></div>')
    body = body.replace('[[sources]]', srcs)
    return meta, body, order

def wrap(meta, body):
    aud_label, aud_cls = AUD[meta['aud']]
    size = meta.get('size', 'A4')
    pages = re.findall(r'<section class="page[^"]*">(.*?)</section>', body, flags=re.S)
    if not pages:
        raise ValueError('sem <section class="page">')
    attr = ATTR_FAM if meta['aud'] == 'fam' else ATTR_LONG
    if size == 'A6':
        attr = ATTR_SHORT
    out = []
    for i, p in enumerate(pages, 1):
        head = (f'<header class="kh"><div class="brand">Kit <span>Comida Primeiro</span></div>'
                f'<div class="meta"><b>{aud_label}</b><span>{meta["n"]:02d} de 20</span></div></header>')
        foot = (f'<footer class="kf"><div>{attr} Uso educacional livre, com citação da fonte.</div>'
                f'<div class="pg">Revisado em outubro de 2026 · {i}/{len(pages)}</div></footer>')
        if meta.get('bare'):
            head = foot = ''
        out.append(f'<section class="page">{head}<div class="content">{p}</div>{foot}</section>')
    w, h = SIZES[size]
    doc = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{html.escape(meta["title"])}</title>'
           f'<style>{FONTS}{CSS}@page{{size:{w} {h};margin:0}}</style></head>'
           f'<body class="{aud_cls} sz-{size}">' + ''.join(out) + '</body></html>')
    return doc

def build(prefixes=None):
    from playwright.sync_api import sync_playwright
    os.makedirs(KIT + '/out/html', exist_ok=True); os.makedirs(KIT + '/out/pdf', exist_ok=True)
    files = sorted(glob.glob(KIT + '/src/*.html'))
    if prefixes:
        files = [f for f in files if any(os.path.basename(f).startswith(p) for p in prefixes)]
    report = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        for f in files:
            meta, body, order = process(open(f).read())
            doc = wrap(meta, body)
            name = f"{meta['n']:02d}-{meta['slug']}"
            hp = f"{KIT}/out/html/{name}.html"
            open(hp, 'w').write(doc)
            pg.goto('file://' + hp)
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(150)
            over = pg.evaluate('''() => [...document.querySelectorAll('.page .content')].map((c,i) =>
                 ({i:i+1, over: c.scrollHeight - c.clientHeight, w: c.scrollWidth - c.clientWidth}))
                 .filter(x => x.over > 1 || x.w > 1)''')
            fams = pg.evaluate('''() => { const s = new Set(); document.querySelectorAll('*').forEach(e => s.add(getComputedStyle(e).fontFamily.split(',')[0])); return [...s]; }''')
            w, h = SIZES[meta.get('size', 'A4')]
            pg.pdf(path=f"{KIT}/out/pdf/{name}.pdf", width=w, height=h, print_background=True, prefer_css_page_size=True)
            report.append((name, len(order), over))
        br.close()
    for name, nref, over in report:
        print(f"{name:40s} refs={nref:2d} {'TRANSBORDA ' + str(over) if over else 'ok'}")

if __name__ == '__main__':
    build(sys.argv[1:] or None)
