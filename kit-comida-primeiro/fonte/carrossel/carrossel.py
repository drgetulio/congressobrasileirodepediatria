# -*- coding: utf-8 -*-
"""Carrossel para redes sociais (item 17): 5 PNGs 1080x1350, legenda e versão editável em HTML."""
import os as _os
KIT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import base64, sys
sys.path.insert(0, KIT)
from playwright.sync_api import sync_playwright

FD = _os.path.join(_os.path.dirname(KIT), 'node_modules', '@fontsource')
def emb(family, folder, weight):
    b = base64.b64encode(open(f'{FD}/{folder}/files/{folder}-latin-{weight}-normal.woff2', 'rb').read()).decode()
    return f"@font-face{{font-family:'{family}';src:url(data:font/woff2;base64,{b}) format('woff2');font-weight:{weight};font-style:normal;font-display:block}}\n"
FONTS = emb('Source Serif 4', 'source-serif-4', 600) + emb('Source Serif 4', 'source-serif-4', 400) + \
        emb('IBM Plex Sans', 'ibm-plex-sans', 400) + emb('IBM Plex Sans', 'ibm-plex-sans', 600)

SLIDE_CSS = """
.s{width:1080px;height:1350px;position:relative;overflow:hidden;display:flex;flex-direction:column;padding:92px 92px 76px;font-family:'IBM Plex Sans',sans-serif;color:#262a36;background:#fff}
.s *{margin:0;padding:0;box-sizing:border-box}
.s.navy{background:#252a5a;color:#fff}
.s::before{content:'';position:absolute;left:0;right:0;top:0;height:16px;background:#eaaa0e}
.s.amber{background:#fdf3dc}
.s .top{display:flex;justify-content:space-between;font-size:30px;letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:#9a6700}
.s.navy .top{color:#eaaa0e}
.s .top span:last-child{color:#6b7080;letter-spacing:.06em}
.s.navy .top span:last-child{color:#aab0d6}
.s h1{font-family:'Source Serif 4',serif;font-weight:600;font-size:112px;line-height:1.04;letter-spacing:-.01em;margin-top:280px}
.s .big{font-family:'Source Serif 4',serif;font-weight:600;font-size:250px;line-height:.9;color:#b97a00;margin-top:110px;font-variant-numeric:lining-nums}
.s .big small{font-size:110px}
.s p.t{font-size:54px;line-height:1.3;margin-top:46px;color:#252a5a;max-width:900px}
.s p.t b{font-weight:600}
.s p.k{font-size:44px;line-height:1.35;margin-top:40px;color:#4a5078;max-width:880px}
.s.navy p.k{color:#d4d8f2}
.s sup{font-size:30px;color:#9a6700;font-weight:600;position:relative;top:-.95em;vertical-align:baseline;line-height:0;margin-left:4px}
.s .foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-size:30px;color:#6b7080;gap:24px}
.s.navy .foot{color:#aab0d6}
.s .list{margin-top:56px;display:flex;flex-direction:column;gap:28px}
.s .list div{font-family:'Source Serif 4',serif;font-size:68px;font-weight:600;color:#252a5a;display:flex;gap:28px;align-items:baseline}
.s .list div i{font-style:normal;color:#9a6700;font-family:'IBM Plex Sans',sans-serif;font-size:42px;font-weight:600;width:60px;flex:none}
.s .list small{display:block;font-family:'IBM Plex Sans',sans-serif;font-size:34px;line-height:1.3;font-weight:400;color:#4a5078;margin-top:10px}
.s .ident{margin-top:40px;border-top:3px solid #eaaa0e;padding-top:24px;font-size:32px;line-height:1.4;color:#252a5a}
.s .ident b{font-weight:600}
.s .handle{font-size:34px;color:#9a6700;font-weight:600}
.s [contenteditable]{outline:none}
.s .ph{background:rgba(234,170,14,.18);border-radius:8px;padding:0 8px}
"""

def slides(editable=False):
    ce = ' contenteditable="true" spellcheck="false"' if editable else ''
    ph = lambda txt, key: f'<span class="ph" data-f="{key}"{ce}>{txt}</span>'
    return [
    ('navy', f'<div class="top"><span>Comida primeiro</span><span>1/5</span></div><h1>Seu filho precisa de whey ou creatina para o esporte?</h1><p class="k">Arraste para ver o que os estudos mostram.</p><div class="foot"><span>Fontes na legenda</span><span>Kit Comida Primeiro</span></div>'),
    ('', '<div class="top"><span>Proteína</span><span>2/5</span></div><div class="big">1,9 <small>g/kg</small></div><p class="t">de proteína por dia foi o consumo médio de 647 jovens jogadores de clubes de futebol de elite e subelite, numa revisão de estudos<sup>1</sup>.</p><p class="k">A necessidade de quem treina gira em torno de 1,5&nbsp;g/kg<sup>2</sup>. Na maioria das vezes, a comida já dá conta.</p><div class="foot"><span>Fontes na legenda</span><span>Kit Comida Primeiro</span></div>'),
    ('', '<div class="top"><span>Lanche</span><span>3/5</span></div><div class="big">17 <small>g</small></div><p class="t">de proteína em um lanche de padaria: <b>um copo de leite, um pão francês e uma fatia de queijo minas</b><sup>3</sup>.</p><p class="k">Depois do treino, a meta é de cerca de 0,3&nbsp;g por quilo de peso: 18&nbsp;g para quem pesa 60&nbsp;kg<sup>2</sup>.</p><div class="foot"><span>Fontes na legenda</span><span>Kit Comida Primeiro</span></div>'),
    ('', '<div class="top"><span>A regra no Brasil</span><span>4/5</span></div><div class="big">19 <small>anos</small></div><p class="t">é a idade mínima para creatina em suplementos. Para crianças e adolescentes, a Agência Nacional de Vigilância Sanitária (Anvisa) não autoriza<sup>4</sup>.</p><p class="k">Energético também não é apropriado nessa idade<sup>5</sup>.</p><div class="foot"><span>Fontes na legenda</span><span>Kit Comida Primeiro</span></div>'),
    ('amber', '<div class="top"><span>O que funciona</span><span>5/5</span></div><div class="list"><div><i>1</i>Treino orientado</div><div><i>2</i>Comida de verdade</div><div><i>3</i><span>Sono suficiente<sup>6</sup><small>8 a 10 horas de 13 a 18 anos; 9 a 12 horas de 6 a 12 anos</small></span></div></div>'
              '<p class="t" style="margin-top:56px">Dúvidas? <b>Converse com o pediatra.</b></p>'
              f'<div class="ident"><b>{ph("[Nome completo]", "nome")}</b> · MÉDICO · CRM {ph("[número/UF]", "crm")}<br>Pediatria · RQE {ph("[número]", "rqe")}</div>'
              f'<div class="foot"><span class="handle">{ph("@seu.perfil", "perfil")}</span><span>Fontes na legenda</span></div>'),
    ]

def doc(editable=False):
    secs = ''.join(f'<section class="s {c}">{b}</section>' for c, b in slides(editable))
    return '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>' + FONTS + '*{box-sizing:border-box}body{margin:0;background:#ccc}' + SLIDE_CSS + '</style></head><body>' + secs + '</body></html>'

open(KIT + '/carrossel/carrossel.html', 'w').write(doc())
with sync_playwright() as pw:
    br = pw.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file://' + KIT + '/carrossel/carrossel.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
    over = pg.evaluate("""() => [...document.querySelectorAll('section.s')].map((s,i)=>({i:i+1,over:s.scrollHeight-s.clientHeight}))""")
    print('transbordo', over)
    for i, el in enumerate(pg.query_selector_all('section.s'), 1):
        el.screenshot(path=f'{KIT}/carrossel/17-carrossel-{i}.png')
    br.close()

# ---------- versão editável
EDIT = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Carrossel editável · Kit Comida Primeiro</title>
<style>""" + FONTS + """
:root{--bg:#eef1f7;--ink:#262a36;--muted:#5d6386;--acc:#8f6200;--card:#fff;--rule:#d9dfec}
@media (prefers-color-scheme:dark){:root{--bg:#12152b;--ink:#e8ebf7;--muted:#a4aacb;--card:#1b1f3d;--rule:#2e3460;--acc:#f2c25a}}
*{box-sizing:border-box}
body{margin:0;border-top:6px solid #eaaa0e;background:var(--bg);color:var(--ink);font-family:'IBM Plex Sans',system-ui,sans-serif;line-height:1.5}
.wrap{max-width:1180px;margin:0 auto;padding:24px 16px 56px}
h1{font-family:'Source Serif 4',Georgia,serif;font-weight:600;font-size:30px;margin:0 0 6px}
p.lede{color:var(--muted);margin:0 0 18px;max-width:70ch}
.form{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:12px;background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:16px;margin-bottom:18px}
label{font-size:13px;font-weight:600;display:block;margin-bottom:4px}
input{font:inherit;font-size:16px;width:100%;padding:8px 10px;border:1px solid var(--rule);border-radius:8px;background:var(--card);color:var(--ink)}
.note{font-size:13.5px;color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));gap:18px}
.slot{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:10px}
.frame{width:100%;aspect-ratio:1080/1350;position:relative;overflow:hidden;border-radius:6px}
.frame .s{position:absolute;left:0;top:0;transform-origin:0 0}
.slot .row{display:flex;justify-content:space-between;align-items:center;margin-top:8px;gap:8px}
button{font:inherit;font-weight:600;font-size:14px;cursor:pointer;border-radius:8px;padding:8px 12px;border:1.5px solid var(--acc);background:transparent;color:var(--acc)}
button.main{background:var(--acc);color:var(--card)}
button:disabled{opacity:.45;cursor:default}
#stage{position:fixed;left:-20000px;top:0}
""" + SLIDE_CSS + """</style></head><body><div class="wrap">
<h1>Carrossel editável</h1>
<p class="lede">Preencha a identificação; ela aparece no último cartão. Os textos também podem ser corrigidos clicando direto sobre eles. Depois, baixe cada cartão em PNG (1080 × 1350) ou faça uma captura de tela.</p>
<div class="form">
<div><label for="f-nome">Nome completo</label><input id="f-nome" data-k="nome" placeholder="Nome como no registro"></div>
<div><label for="f-crm">CRM (número/UF)</label><input id="f-crm" data-k="crm" placeholder="000000/DF"></div>
<div><label for="f-rqe">RQE de Pediatria</label><input id="f-rqe" data-k="rqe" placeholder="00000"></div>
<div><label for="f-perfil">Perfil na rede</label><input id="f-perfil" data-k="perfil" placeholder="@seu.perfil"></div>
<p class="note" style="grid-column:1/-1;margin:0">A Resolução CFM nº 2.336/2023 pede, na publicidade médica, o nome do médico, a palavra MÉDICO e o número de inscrição no Conselho Regional de Medicina (CRM); ao divulgar a especialidade, o número do Registro de Qualificação de Especialista (RQE). A mesma identificação deve constar na página principal do perfil.</p>
</div>
<div class="grid" id="grid"></div>
<p class="note" id="msg" aria-live="polite" style="margin-top:14px"></p>
<p class="note">As fontes de cada número estão na legenda que acompanha o carrossel (arquivo 17-legenda-do-carrossel.txt). Kit Comida Primeiro, material de apoio da aula “Creatina e Whey Protein: modismo inadequado”, 42º Congresso Brasileiro de Pediatria, 2026.</p>
</div>
<div id="stage"></div>
<template id="tpl">__SLIDES__</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script>
const grid=document.getElementById('grid'), tpl=document.getElementById('tpl'), msg=document.getElementById('msg');
const slides=[...tpl.content.querySelectorAll('section.s')];
const frames=[];
slides.forEach((s,i)=>{const slot=document.createElement('div');slot.className='slot';
 const fr=document.createElement('div');fr.className='frame';const el=s.cloneNode(true);fr.appendChild(el);slot.appendChild(fr);
 const row=document.createElement('div');row.className='row';row.innerHTML=`<span class="note">Cartão ${i+1} de ${slides.length}</span><button class="main" data-i="${i}">Baixar PNG</button>`;slot.appendChild(row);
 grid.appendChild(slot);frames.push(el)});
function fit(){frames.forEach(el=>{const w=el.parentElement.clientWidth;el.style.transform=`scale(${w/1080})`})}
addEventListener('resize',fit);document.fonts.ready.then(fit);fit();
document.querySelectorAll('input[data-k]').forEach(inp=>inp.addEventListener('input',()=>{
 const v=inp.value.trim();document.querySelectorAll(`.frame [data-f="${inp.dataset.k}"]`).forEach(x=>{x.textContent=v||x.dataset.def;x.classList.toggle('ph',!v)})}));
document.querySelectorAll('.frame [data-f]').forEach(x=>x.dataset.def=x.textContent);
let dl=null;(async()=>{try{dl=await window.claude?.use?.('downloads')}catch(e){dl=null}})();
async function save(blob,name){
 if(dl){try{await dl.save({filename:name,data:blob});msg.textContent='Arquivo oferecido para download.';return}catch(e){if(e&&e.code==='declined'){msg.textContent='Download cancelado.';return}}}
 const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},1500);msg.textContent='Download iniciado.'}
grid.addEventListener('click',async e=>{const b=e.target.closest('button[data-i]');if(!b)return;
 if(typeof html2canvas!=='function'){msg.textContent='O download em PNG precisa de conexão com a internet. Sem ela, use a captura de tela do cartão.';return}
 const i=+b.dataset.i;b.disabled=true;msg.textContent='Gerando a imagem...';
 const stage=document.getElementById('stage');stage.innerHTML='';const c=frames[i].cloneNode(true);c.style.transform='none';
 c.querySelectorAll('.ph').forEach(x=>x.classList.remove('ph'));stage.appendChild(c);
 try{await document.fonts.ready;const cv=await html2canvas(c,{width:1080,height:1350,scale:1,backgroundColor:null});
  cv.toBlob(async bl=>{await save(bl,`carrossel-${i+1}.png`);b.disabled=false},'image/png')}
 catch(err){msg.textContent='Não foi possível gerar a imagem; use a captura de tela.';b.disabled=false}
 finally{setTimeout(()=>stage.innerHTML='',500)}});
</script></body></html>"""
secs = ''.join(f'<section class="s {c}">{b}</section>' for c, b in slides(True))
open(KIT + '/carrossel/17-carrossel-editavel.html', 'w').write(EDIT.replace('__SLIDES__', secs))

cap = """Seu filho precisa de whey ou creatina para o esporte? Na maioria das vezes, não.

Numa revisão de estudos, 647 jovens jogadores de clubes de futebol de elite e subelite consumiam, em média, 1,9 g de proteína por quilo por dia (1), e a necessidade do adolescente que treina gira em torno de 1,5 g/kg (2). Um lanche de padaria, com um copo de leite, um pão francês e uma fatia de queijo minas, soma 17 g de proteína (3). No Brasil, a Agência Nacional de Vigilância Sanitária (Anvisa) não autoriza creatina em suplementos para menores de 19 anos (4), e energético não é apropriado para crianças e adolescentes (5). O que funciona: treino orientado, comida de verdade e sono suficiente, de 8 a 10 horas por noite entre 13 e 18 anos e de 9 a 12 horas entre 6 e 12 anos (6).

Dúvidas? Converse com o pediatra.

[Nome completo] · MÉDICO · CRM [número/UF] · Pediatria · RQE [número]

Fontes
1. Steffl M, Kinkorova I, Kokstejn J, Petr M. Macronutrient intake in soccer players: a meta-analysis. Nutrients. 2019;11(6):1305.
2. Desbrow B. Youth athlete development and nutrition. Sports Med. 2021;51(Suppl 1):3-12.
3. Tabela Brasileira de Composição de Alimentos (TBCA), versão 7.3. Universidade de São Paulo; 2025.
4. Agência Nacional de Vigilância Sanitária. Instrução Normativa nº 28/2018 e Instrução Normativa nº 373/2025.
5. Sociedade Brasileira de Pediatria, Departamento Científico de Nutrologia. Consumo de bebidas energéticas por crianças e adolescentes. Documento Científico nº 10; 2022.
6. Paruthi S et al. Recommended amount of sleep for pediatric populations. J Clin Sleep Med. 2016;12(6):785-6.

Antes de publicar: preencha nome, CRM e RQE no último cartão (arquivo 17-carrossel-editavel.html). A Resolução CFM nº 2.336/2023 pede essa identificação na publicidade médica e também na página principal do perfil.
"""
open(KIT + '/carrossel/17-legenda-do-carrossel.txt', 'w').write(cap)
print('ok')
