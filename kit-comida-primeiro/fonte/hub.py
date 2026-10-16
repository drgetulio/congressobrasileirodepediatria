# -*- coding: utf-8 -*-
"""Monta a página do kit (artefato e versão offline), as miniaturas e os pacotes ZIP."""
import os as _os
KIT = _os.path.dirname(_os.path.abspath(__file__))
import os, shutil, subprocess, zipfile, glob, html, sys, json
from PIL import Image
sys.path.insert(0, KIT)

SITE = KIT + '/site'
OFF = KIT + '/zip/Kit-Comida-Primeiro'
PDF = KIT + '/out/pdf'

def pages(p):
    out = subprocess.run(['pdfinfo', p], capture_output=True, text=True).stdout
    return int([l for l in out.splitlines() if l.startswith('Pages')][0].split()[-1])

# n, título, público, descrição, formato, arquivos
ITEMS = [
 (1, 'Calculadora de proteína', 'app', 'Meta do dia e de cada refeição pelo peso, pela idade e pelo número de refeições, com um montador de lanche pós-treino em medidas caseiras da tabela brasileira.', 'Ferramenta interativa', {'tool': '01-calculadora-de-proteina.html'}),
 (2, 'Água no treino', 'app', 'Volume por hora e a cada 15 minutos, e o teste da balança que mostra se o plano funcionou.', 'Ferramenta e PDF A4', {'tool': '02-agua-no-treino.html', 'pdf': '02-agua-no-treino.pdf'}),
 (3, 'Conduta passo a passo', 'app', 'Seis passos para o adolescente que pediu ou já usa suplemento, com resumo pronto para o prontuário.', 'Ferramenta e PDF A4', {'tool': '03-conduta-passo-a-passo.html', 'pdf': '03-conduta-passo-a-passo.pdf'}),
 (4, 'Verdade ou mito', 'app', 'Doze afirmações para o adolescente responder na sala de espera, cada uma com explicação e fonte.', 'Ferramenta interativa', {'tool': '04-verdade-ou-mito.html'}),
 (5, 'Cartão de bolso', 'ped', 'Os números da consulta em tamanho A6: proteína, água, sono, cafeína e os sinais que pedem conversa.', 'PDF A6', {'pdf': '05-cartao-de-bolso.pdf'}),
 (6, 'Roteiro de entrevista e registro', 'ped', 'Perguntas sobre suplementos, substâncias e imagem corporal, com modelo de registro no prontuário.', 'PDF A4', {'pdf': '06-roteiro-de-entrevista-e-registro.pdf'}),
 (7, 'Mapa dos suplementos', 'ped', 'Proteína, creatina, cafeína, bebidas esportivas, vitaminas e minerais: o que se sabe em adultos e na adolescência, a norma e a conduta.', 'PDF A4', {'pdf': '07-mapa-dos-suplementos.pdf'}),
 (8, 'Rótulo, regularização e doping', 'ped', 'O que conferir no pote segundo a Agência Nacional de Vigilância Sanitária, o que já se encontrou dentro dos potes e as regras antidopagem.', 'PDF A4', {'pdf': '08-rotulo-regularizacao-e-doping.pdf'}),
 (9, 'Creatina: o que os pais perguntam', 'ped', 'Respostas curtas às dúvidas mais comuns, cada uma marcada pelo grau de certeza da evidência.', 'PDF A4', {'pdf': '09-creatina-o-que-os-pais-perguntam.pdf'}),
 (10, 'Deficiência energética relativa no esporte', 'ped', 'O problema oposto ao do suplemento: definição do Comitê Olímpico Internacional, sinais, rastreio e prevenção.', 'PDF A4', {'pdf': '10-deficiencia-energetica-reds.pdf'}),
 (11, 'Energéticos, cafeína e pré-treino', 'ped', 'Teto de cafeína por peso, limite legal brasileiro das bebidas e uma tabela para somar todas as fontes do dia.', 'PDF A4', {'pdf': '11-energeticos-cafeina-e-pre-treino.pdf'}),
 (12, 'Folheto para os pais', 'fam', 'Cinco motivos para a resposta costumar ser não, ideias de lanche e perguntas para levar à consulta.', 'PDF A4, frente e verso', {'pdf': '12-folheto-para-os-pais.pdf'}),
 (13, 'Folheto para o adolescente', 'fam', 'Treino, comida, sono e água em linguagem direta, com a conta de proteína de um dia comum.', 'PDF A4, frente e verso', {'pdf': '13-folheto-para-o-adolescente.pdf'}),
 (14, 'Receituário de comida de verdade', 'fam', 'Prescrição em A5 com lanches pós-treino e metas por peso; no verso, a proteína dos alimentos em medidas de casa.', 'PDF A5, frente e verso', {'pdf': '14-receituario-de-comida-de-verdade.pdf'}),
 (15, 'Cardápio de lanches pós-treino', 'fam', 'Quinze lanches e refeições com comida brasileira, cada um com proteína, energia e a meta que cobre.', 'PDF A4', {'pdf': '15-cardapio-de-lanches-pos-treino.pdf'}),
 (16, 'Pôster para a sala de espera', 'fam', 'Treino, comida e sono em tamanho A3, com espaço para o carimbo do serviço.', 'PDF A3', {'pdf': '16-poster-para-a-sala-de-espera.pdf'}),
 (17, 'Carrossel para redes sociais', 'fam', 'Cinco cartões de 1080 × 1350 com legenda e fontes, e uma versão editável para incluir nome e registros profissionais antes de publicar.', 'PNG, legenda e versão editável', {'zip': '17-carrossel.zip', 'edit': '17-carrossel-editavel.html'}),
 (18, 'Carta ao treinador e à escola', 'eq', 'Modelo para adaptar e enviar com a concordância do adolescente e da família.', 'PDF A4 e Word', {'pdf': '18-carta-ao-treinador-e-a-escola.pdf', 'docx': '18-carta-ao-treinador-e-a-escola.docx'}),
 (19, 'Casos clínicos para discussão', 'eq', 'Quatro casos fictícios com perguntas, discussão comentada e roteiro para sessões de 30 minutos.', 'PDF A4', {'pdf': '19-casos-clinicos-para-discussao.pdf'}),
 (20, 'Bibliografia comentada', 'eq', 'Catorze leituras comentadas e a lista completa das referências do kit, com os links de cada artigo.', 'PDF A4', {'pdf': '20-bibliografia-comentada.pdf'}),
]
GROUPS = [('app', 'Ferramentas', 'Para usar na tela, durante a consulta ou na sala de espera.'),
          ('ped', 'Para o pediatra', 'Material de consulta rápida, para ter à mão no consultório.'),
          ('fam', 'Para as famílias', 'Para entregar, afixar ou publicar, em linguagem leiga.'),
          ('eq', 'Para a equipe e o ensino', 'Para escrever ao treinador, discutir casos e ir às fontes.')]

def thumbs():
    os.makedirs(SITE + '/thumbs', exist_ok=True)
    tmp = KIT + '/out/tmpthumb'; os.makedirs(tmp, exist_ok=True)
    for n, t, aud, d, fmt, fs in ITEMS:
        out = f'{SITE}/thumbs/{n:02d}.jpg'
        if 'pdf' in fs:
            base = f'{tmp}/{n:02d}'
            subprocess.run(['pdftoppm', '-png', '-r', '60', '-f', '1', '-l', '1', '-singlefile', f'{PDF}/{fs["pdf"]}', base], check=True)
            im = Image.open(base + '.png').convert('RGB')
        elif 'tool' in fs:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as pw:
                br = pw.chromium.launch(); pg = br.new_page(viewport={'width': 1000, 'height': 1414})
                pg.goto(f'file://{SITE}/ferramentas/{fs["tool"]}'); pg.wait_for_timeout(500)
                pg.screenshot(path=f'{tmp}/{n:02d}.png'); br.close()
            im = Image.open(f'{tmp}/{n:02d}.png').convert('RGB')
        else:
            im = Image.open(f'{KIT}/carrossel/17-carrossel-1.png').convert('RGB')
        w = 420; im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        im.save(out, quality=84, optimize=True)

def assemble():
    for root in (SITE, OFF):
        for sub in ('materiais', 'carrossel'):
            os.makedirs(f'{root}/{sub}', exist_ok=True)
        for f in glob.glob(PDF + '/*.pdf'):
            shutil.copy(f, f'{root}/materiais/')
        for f in glob.glob(KIT + '/carrossel/17-*'):
            shutil.copy(f, f'{root}/carrossel/')
    for d in (SITE + '/downloads', OFF + '/downloads'):
        if os.path.isdir(d): shutil.rmtree(d)
    for f in glob.glob(SITE + '/materiais/*.docx'):
        os.remove(f)
    shutil.copy(KIT + '/out/18-carta-ao-treinador-e-a-escola.docx', OFF + '/materiais/')
    shutil.copytree(SITE + '/thumbs', OFF + '/thumbs', dirs_exist_ok=True)
    os.makedirs(SITE + '/data', exist_ok=True)
    import base64, json
    json.dump({'name': '18-carta-ao-treinador-e-a-escola.docx',
               'b64': base64.b64encode(open(KIT + '/out/18-carta-ao-treinador-e-a-escola.docx', 'rb').read()).decode()},
              open(SITE + '/data/carta-docx.json', 'w'))

def manifest():
    """Arquivos do ZIP montado no navegador: [origem no artefato, caminho dentro do ZIP]."""
    kit = []
    for root, _, files in os.walk(OFF):
        for f in sorted(files):
            rel = os.path.relpath(os.path.join(root, f), OFF)
            if rel.endswith('.docx'):
                src = 'b64:data/carta-docx.json'
            elif rel in ('index.html', 'LEIA-ME.txt'):
                src = 'offline/' + rel
            else:
                src = rel
            kit.append([src, 'Kit-Comida-Primeiro/' + rel])
    car = [[f'carrossel/{os.path.basename(f)}', f'17-carrossel/{os.path.basename(f)}'] for f in sorted(glob.glob(KIT + '/carrossel/17-*'))]
    return {'kit': kit, 'carrossel': car}

LEIA = """Kit Comida Primeiro
Material de apoio da aula "Creatina e Whey Protein: modismo inadequado", 42º Congresso Brasileiro de Pediatria, Belo Horizonte, outubro de 2026.
Getúlio Bernardo Morato Filho, professor da Escola Superior de Ciências da Saúde (ESCS) e do Centro Universitário de Brasília (UniCEUB), supervisor do Programa de Residência Médica do Hospital Materno-Infantil de Brasília (HMIB), Brasília, Distrito Federal.
Instagram: @drgetulio (https://www.instagram.com/drgetulio/).

Como abrir
Abra o arquivo index.html em qualquer navegador. Ele leva às quatro ferramentas (pasta ferramentas), aos materiais em PDF e Word (pasta materiais) e ao carrossel (carrossel/index.html).
As ferramentas funcionam sem internet; com internet, usam as fontes tipográficas do kit.

Antes de publicar o carrossel
Preencha nome, CRM e RQE no último cartão, pela versão editável (carrossel/17-carrossel-editavel.html). A Resolução CFM nº 2.336/2023 pede essa identificação na publicidade médica e também na página principal do perfil.

Uso educacional livre, com citação da fonte. Orientação geral, que não substitui a avaliação individual. Revisado em outubro de 2026.
"""

CARROSSEL_INDEX = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Carrossel · Kit Comida Primeiro</title>
<style>
:root{--bg:#f6f8fc;--surface:#fff;--ink:#262a36;--muted:#5d6386;--rule:#d9dfec;--head:#252a5a;--acc:#8f6200}
@media (prefers-color-scheme:dark){:root{--bg:#12152b;--surface:#1b1f3d;--ink:#e8ebf7;--muted:#a4aacb;--rule:#2e3460;--head:#e3e6fa;--acc:#f2c25a;color-scheme:dark}}
*{box-sizing:border-box}body{margin:0;border-top:6px solid #eaaa0e;background:var(--bg);color:var(--ink);font-family:"IBM Plex Sans",system-ui,sans-serif;line-height:1.55}
.wrap{max-width:1120px;margin:0 auto;padding:28px 20px 56px}
h1{font-family:"Source Serif 4",Georgia,serif;color:var(--head);font-size:34px;margin:0 0 8px}
p{max-width:70ch}a{color:var(--acc);font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,200px),1fr));gap:14px;margin:20px 0}
.grid a{display:block;background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:8px;text-decoration:none}
.grid img{width:100%;height:auto;display:block;border-radius:6px}
.grid span{display:block;font-size:14px;margin-top:6px;color:var(--muted)}
</style></head><body><div class="wrap">
<p><a href="../index.html">Kit Comida Primeiro</a></p>
<h1>17 · Carrossel para redes sociais</h1>
<p>Cinco cartões de 1080 × 1350 pixels. Antes de publicar, preencha nome, CRM e RQE no último cartão pela <a href="17-carrossel-editavel.html">versão editável</a>; a Resolução CFM nº 2.336/2023 pede essa identificação na publicidade médica e na página principal do perfil. A legenda, com as fontes, está em <a href="17-legenda-do-carrossel.txt">17-legenda-do-carrossel.txt</a>.</p>
<div class="grid">
<a href="17-carrossel-1.png"><img src="17-carrossel-1.png" alt="Cartão 1 do carrossel"><span>Cartão 1</span></a>
<a href="17-carrossel-2.png"><img src="17-carrossel-2.png" alt="Cartão 2 do carrossel"><span>Cartão 2</span></a>
<a href="17-carrossel-3.png"><img src="17-carrossel-3.png" alt="Cartão 3 do carrossel"><span>Cartão 3</span></a>
<a href="17-carrossel-4.png"><img src="17-carrossel-4.png" alt="Cartão 4 do carrossel"><span>Cartão 4</span></a>
<a href="17-carrossel-5.png"><img src="17-carrossel-5.png" alt="Cartão 5 do carrossel"><span>Cartão 5</span></a>
</div></div></body></html>
"""

def page(offline):
    def btns(n, fs):
        b = []
        if 'tool' in fs:
            b.append(f'<a class="act primary" href="ferramentas/{fs["tool"]}">Abrir a ferramenta</a>')
        if 'edit' in fs:
            b.append(f'<a class="act primary" href="carrossel/{fs["edit"]}">Abrir a versão editável</a>')
        for key, label in (('pdf', 'PDF'), ('docx', 'Word'), ('zip', 'cartões e legenda')):
            if key not in fs:
                continue
            if offline:
                path = {'pdf': 'materiais/' + fs.get('pdf', ''), 'docx': 'materiais/' + fs.get('docx', ''), 'zip': 'carrossel/index.html'}[key]
                b.append(f'<a class="act" href="{path}">{label[0].upper() + label[1:]}</a>')
            elif key == 'pdf':
                path = 'materiais/' + fs['pdf']
                b.append(f'<button class="act dl" type="button" data-file="{path}" data-name="{fs[key]}">Baixar {label}</button>'
                         f'<a class="act fb" href="{path}" hidden>Abrir {label}</a>')
            elif key == 'docx':
                b.append(f'<button class="act dl" type="button" data-b64="data/carta-docx.json" data-name="{fs[key]}">Baixar {label}</button>')
            else:
                b.append(f'<button class="act dl" type="button" data-zip="carrossel" data-name="{fs[key]}">Baixar {label}</button>')
        return ''.join(b)
    cards = {}
    for n, t, aud, d, fmt, fs in ITEMS:
        pg_info = f' · {pages(PDF + "/" + fs["pdf"])} {"página" if pages(PDF + "/" + fs["pdf"]) == 1 else "páginas"}' if 'pdf' in fs else ''
        cards.setdefault(aud, []).append(f'''<article class="item {aud}" id="item-{n:02d}">
<div class="thumb"><img src="thumbs/{n:02d}.jpg" alt="Primeira página do item {n:02d}, {html.escape(t)}" loading="lazy" width="420" height="594"></div>
<div class="body"><div class="titlerow"><p class="num">{n:02d}</p><h3>{html.escape(t)}</h3></div><p class="desc">{html.escape(d)}</p>
<p class="fmt">{html.escape(fmt)}{pg_info}</p></div>
<div class="acts">{btns(n, fs)}</div></article>''')
    groups = ''.join(f'''<section class="group {aud}" aria-labelledby="g-{aud}"><header class="ghead"><h2 id="g-{aud}">{name}</h2><p>{sub}</p></header>
<div class="grid">{"".join(cards[aud])}</div></section>''' for aud, name, sub in GROUPS)
    zip_btn = ('<a class="big-dl" href="LEIA-ME.txt">Leia-me do kit</a>' if offline else
               '<button class="big-dl dl" type="button" data-zip="kit" data-name="Kit-Comida-Primeiro.zip">Baixar o kit completo <span>ZIP · __ZIPSIZE__</span></button><p class="fb" hidden>Nesta visualização, os arquivos abrem um a um pelos botões de cada item.</p>')
    body = f'''<title>Kit Comida Primeiro</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&display=swap">
<style>
/* Layout: capa de prontuário, atalhos de uso por momento da consulta e catálogo agrupado pela cor de público dos impressos */
:root{{--bg:#f6f8fc;--surface:#fff;--ink:#262a36;--muted:#5d6386;--rule:#d9dfec;--head:#252a5a;
--blue:#224f9d;--amber:#8f6200;--green:#4f6f0f;--indigo:#483c90;--t-blue:#e9f0fa;--t-amber:#fdf3dc;--t-green:#eef6dd;--t-indigo:#eeecf6;
--serif:"Source Serif 4",Georgia,"Times New Roman",serif;--sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--acc:var(--indigo);--tint:var(--t-indigo)}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#12152b;--surface:#1b1f3d;--ink:#e8ebf7;--muted:#a4aacb;--rule:#2e3460;--head:#e3e6fa;
--blue:#8fb0e3;--amber:#f2c25a;--green:#a9d25a;--indigo:#b9b0f0;--t-blue:#1e2750;--t-amber:#3a3220;--t-green:#243317;--t-indigo:#272350;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#12152b;--surface:#1b1f3d;--ink:#e8ebf7;--muted:#a4aacb;--rule:#2e3460;--head:#e3e6fa;
--blue:#8fb0e3;--amber:#f2c25a;--green:#a9d25a;--indigo:#b9b0f0;--t-blue:#1e2750;--t-amber:#3a3220;--t-green:#243317;--t-indigo:#272350;color-scheme:dark}}
*{{box-sizing:border-box}}
body{{margin:0;border-top:6px solid #eaaa0e;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.55}}
.wrap{{max-width:1120px;margin:0 auto;padding-inline:20px;padding-block:28px 64px;display:flex;flex-direction:column;gap:40px}}
.app{{--acc:var(--indigo);--tint:var(--t-indigo)}}.ped{{--acc:var(--blue);--tint:var(--t-blue)}}.fam{{--acc:var(--amber);--tint:var(--t-amber)}}.eq{{--acc:var(--green);--tint:var(--t-green)}}
.cover{{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);gap:28px;align-items:end;border-bottom:2px solid var(--head);padding-bottom:26px}}
.eyebrow{{font-size:13px;letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:var(--muted);margin:0 0 10px}}
h1{{font-family:var(--serif);font-weight:600;font-size:clamp(40px,6.4vw,72px);line-height:1;color:var(--head);margin:0;text-wrap:balance;letter-spacing:-.01em}}
h1 em{{font-style:normal;color:var(--amber)}}
@media (prefers-color-scheme:light){{h1 em{{color:#b97a00}}}}
.lede{{font-size:18px;color:var(--ink);margin:16px 0 0;max-width:60ch}}
.byline{{font-size:14px;color:var(--muted);margin:10px 0 0}}
.side{{display:flex;flex-direction:column;gap:12px}}
.big-dl{{display:flex;flex-direction:column;align-items:flex-start;gap:2px;width:100%;text-align:left;font:inherit;font-weight:600;font-size:19px;background:var(--head);color:var(--bg);border:0;border-radius:10px;padding:16px 20px;cursor:pointer;text-decoration:none}}
.big-dl span{{font-weight:400;font-size:14px;opacity:.85}}
.side p{{margin:0;font-size:14px;color:var(--muted)}}
.paths{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:12px}}
.path{{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:14px 16px}}
.path b{{display:block;font-family:var(--serif);font-size:18px;color:var(--head);margin-bottom:6px}}
.path a{{display:inline-block;font-variant-numeric:tabular-nums;font-weight:600;color:var(--acc);text-decoration:none;border:1.5px solid var(--acc);border-radius:999px;padding:1px 10px;margin:2px 4px 2px 0;font-size:14px}}
.path a.app{{--acc:var(--indigo)}}.path a.ped{{--acc:var(--blue)}}.path a.fam{{--acc:var(--amber)}}.path a.eq{{--acc:var(--green)}}
.group{{display:flex;flex-direction:column;gap:16px}}
.ghead{{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 16px;border-top:4px solid var(--acc);padding-top:12px}}
.ghead h2{{font-family:var(--serif);font-weight:600;font-size:28px;color:var(--head);margin:0}}
.ghead p{{margin:0;color:var(--muted)}}
.grid{{display:flex;flex-direction:column;gap:10px}}
.item{{display:grid;grid-template-columns:92px minmax(0,1fr) 210px;gap:18px;align-items:center;background:var(--surface);border:1px solid var(--rule);border-radius:12px;padding:12px 16px 12px 12px}}
.thumb{{background:var(--tint);border-radius:6px;padding:6px;align-self:start;aspect-ratio:210/297;display:flex;align-items:flex-start;justify-content:center;overflow:hidden;max-width:100%}}
.thumb img{{width:100%;height:auto;display:block;box-shadow:0 1px 4px rgba(20,24,40,.18)}}
.body{{display:flex;flex-direction:column;gap:4px;min-width:0}}
.titlerow{{display:flex;align-items:baseline;gap:12px}}
.num{{margin:0;font-family:var(--serif);font-weight:600;font-size:28px;line-height:1;color:var(--acc);font-variant-numeric:lining-nums tabular-nums;flex:none}}
.item h3{{font-family:var(--serif);font-weight:600;font-size:19px;line-height:1.2;color:var(--head);margin:0;text-wrap:balance}}
.desc{{margin:0;font-size:15.5px;max-width:68ch}}
.fmt{{margin:0;font-size:13px;color:var(--muted)}}
.acts{{display:flex;flex-direction:column;gap:8px}}
.acts .act{{text-align:center}}
.act{{font:inherit;font-size:14px;font-weight:600;color:var(--acc);background:transparent;border:1.5px solid var(--acc);border-radius:8px;padding:6px 12px;cursor:pointer;text-decoration:none}}
.act.primary{{background:var(--acc);color:var(--surface)}}
.act:disabled{{opacity:.5;cursor:default}}
a:focus-visible,button:focus-visible{{outline:3px solid var(--acc);outline-offset:2px}}
.status{{min-height:1.5em;margin:0;font-size:14px;color:var(--muted)}}
footer{{border-top:1px solid var(--rule);padding-top:16px;font-size:14px;color:var(--muted);display:flex;flex-direction:column;gap:6px}}
footer p{{margin:0;max-width:80ch}}
@media (max-width:760px){{.cover{{grid-template-columns:1fr}}.item{{grid-template-columns:76px minmax(0,1fr);align-items:start}}.acts{{grid-column:1/-1;flex-direction:row;flex-wrap:wrap}}.acts .act{{flex:1 1 auto}}}}
[hidden]{{display:none!important}}
@media (prefers-reduced-motion:reduce){{*{{transition:none!important}}}}
</style>
<div class="wrap">
<header class="cover">
<div><p class="eyebrow">42º Congresso Brasileiro de Pediatria · Belo Horizonte · outubro de 2026</p>
<h1>Kit <em>Comida</em> Primeiro</h1>
<p class="lede">Vinte materiais para levar a aula “Creatina e Whey Protein: modismo inadequado” ao consultório: ferramentas para a consulta, fichas de referência, materiais para as famílias e recursos para o ensino.</p>
<p class="byline">Getúlio Bernardo Morato Filho, professor da Escola Superior de Ciências da Saúde (ESCS) e do Centro Universitário de Brasília (UniCEUB), supervisor do Programa de Residência Médica do Hospital Materno-Infantil de Brasília (HMIB), Brasília, Distrito Federal. Instagram: <a href="https://www.instagram.com/drgetulio/" style="color:inherit;font-weight:600">@drgetulio</a>.</p></div>
<div class="side">{zip_btn}
<p>Todos os PDFs, a carta em Word, o carrossel e as ferramentas, que também funcionam sem internet.</p>
<p class="status" id="status" aria-live="polite"></p></div>
</header>
<section aria-labelledby="h-paths"><h2 id="h-paths" class="eyebrow" style="margin-bottom:12px">Por onde começar</h2>
<div class="paths">
<div class="path"><b>Na consulta</b><a class="app" href="#item-03">03</a><a class="ped" href="#item-05">05</a><a class="ped" href="#item-06">06</a><a class="app" href="#item-01">01</a></div>
<div class="path"><b>Para a família levar</b><a class="fam" href="#item-12">12</a><a class="fam" href="#item-13">13</a><a class="fam" href="#item-14">14</a><a class="fam" href="#item-15">15</a></div>
<div class="path"><b>Na sala de espera</b><a class="app" href="#item-04">04</a><a class="fam" href="#item-16">16</a></div>
<div class="path"><b>Para ensinar e estudar</b><a class="eq" href="#item-19">19</a><a class="eq" href="#item-20">20</a><a class="ped" href="#item-07">07</a></div>
</div></section>
{groups}
<footer>
<p>Orientação geral, que não substitui a avaliação individual. Uso educacional livre, com citação da fonte. As referências completas de todos os materiais estão no item 20.</p>
<p>Valores de alimentos da Tabela Brasileira de Composição de Alimentos, versão 7.3. Normas sanitárias e antidopagem conferidas em outubro de 2026.</p>
</footer>
</div>
'''
    if not offline:
        body += ('<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>\n<script>\nconst MANIFEST=' + json.dumps(manifest(), ensure_ascii=False) + ';\n' + '''
const st=document.getElementById('status');
async function getBlob(src){
 if(src.startsWith('b64:')){const j=await (await fetch(src.slice(4))).json();const bin=atob(j.b64);const u=new Uint8Array(bin.length);for(let i=0;i<bin.length;i++)u[i]=bin.charCodeAt(i);return new Blob([u])}
 const r=await fetch(src); if(!r.ok) throw new Error('fetch '+src); return await r.blob();
}
async function makeZip(key){
 if(typeof JSZip!=='function') throw {code:'nozip'};
 const z=new JSZip(); const list=MANIFEST[key];
 for(let i=0;i<list.length;i++){st.textContent='Montando o pacote: '+(i+1)+' de '+list.length+' arquivos...'; z.file(list[i][1], await getBlob(list[i][0]))}
 return await z.generateAsync({type:'blob',compression:'DEFLATE'});
}
(async()=>{
 let dl=null; try{ dl = await window.claude?.use?.('downloads'); }catch(e){ dl=null; }
 if(!dl){ document.querySelectorAll('.dl').forEach(b=>b.hidden=true); document.querySelectorAll('.fb').forEach(a=>a.hidden=false); return; }
 document.addEventListener('click', async e=>{
  const b=e.target.closest('button.dl'); if(!b) return;
  b.disabled=true; st.textContent='Preparando '+b.dataset.name+'...';
  try{
   const blob = b.dataset.zip ? await makeZip(b.dataset.zip) : await getBlob(b.dataset.b64 ? 'b64:'+b.dataset.b64 : b.dataset.file);
   await dl.save({filename:b.dataset.name, data:blob});
   st.textContent='Arquivo entregue: '+b.dataset.name+'.';
  }catch(err){
   const c=err&&err.code;
   st.textContent = c==='declined' ? 'Download cancelado.' : c==='rate_limited' ? 'Há um download aguardando confirmação. Tente de novo em instantes.' : c==='nozip' ? 'O pacote ZIP precisa de conexão com a internet. Baixe os arquivos um a um pelos botões de cada item.' : 'Não foi possível baixar agora. Tente novamente.';
  }finally{ b.disabled=false; }
 });
})();
</script>''')
        return body
    return ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            + body.split('<div class="wrap">')[0] + '</head><body><div class="wrap">' + body.split('<div class="wrap">', 1)[1] + '</body></html>')

if __name__ == '__main__':
    import json
    if '--no-thumbs' not in sys.argv:
        thumbs()
    assemble()
    open(OFF + '/index.html', 'w').write(page(True))
    open(OFF + '/carrossel/index.html', 'w').write(CARROSSEL_INDEX)
    open(SITE + '/carrossel/index.html', 'w').write(CARROSSEL_INDEX)
    open(OFF + '/LEIA-ME.txt', 'w').write(LEIA)
    os.makedirs(SITE + '/offline', exist_ok=True)
    shutil.copy(OFF + '/index.html', SITE + '/offline/index.html')
    shutil.copy(OFF + '/LEIA-ME.txt', SITE + '/offline/LEIA-ME.txt')
    zp = KIT + '/out/Kit-Comida-Primeiro.zip'
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(OFF):
            for f in sorted(files):
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, os.path.dirname(OFF)))
    size = os.path.getsize(zp) / 1024 / 1024
    open(SITE + '/index.html', 'w').write(page(False).replace('__ZIPSIZE__', f'{size:.1f} MB'.replace('.', ',')))
    print('ok', f'{size:.2f} MB')
