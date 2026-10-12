# -*- coding: utf-8 -*-
"""Gera as ferramentas interativas (01 a 04) e a página do kit, em duas versões:
   site/  -> para publicar como artefato (index sem doctype)
   zip/Kit-Comida-Primeiro/ -> versão offline (index com doctype)"""
import os as _os
KIT = _os.path.dirname(_os.path.abspath(__file__))
import json, os, sys, shutil, glob, html
sys.path.insert(0, KIT)
from tbca import FOODS, COMBOS, combo_totals, fmt

FONTS_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
              '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&display=swap">')

CSS = r"""
/* Kit Comida Primeiro na tela: ficha clínica, número do item em serifa, cor por público */
:root{--bg:#f6f7fa;--surface:#fff;--ink:#1d2130;--muted:#596074;--rule:#dde1ea;--head:#1f2552;
--blue:#224f9d;--amber:#a86400;--green:#457011;--indigo:#3b3f8f;--red:#a3341f;
--t-blue:#eaf0f9;--t-amber:#fcf2de;--t-green:#edf4e1;--t-indigo:#ecedf7;--t-red:#fbebe7;--track:#e8ebf2;
--serif:"Source Serif 4",Georgia,"Times New Roman",serif;--sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
--acc:var(--indigo);--tint:var(--t-indigo)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#11131a;--surface:#191c26;--ink:#e6e8ef;--muted:#a2a8b9;--rule:#2b3040;--head:#dfe3ff;
--blue:#8fb0ef;--amber:#efb55a;--green:#a6d07a;--indigo:#b4b7ff;--red:#f19a86;--t-blue:#1c2640;--t-amber:#2d2312;--t-green:#1e2917;--t-indigo:#22233c;--t-red:#33201b;--track:#2a2f3e;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#11131a;--surface:#191c26;--ink:#e6e8ef;--muted:#a2a8b9;--rule:#2b3040;--head:#dfe3ff;
--blue:#8fb0ef;--amber:#efb55a;--green:#a6d07a;--indigo:#b4b7ff;--red:#f19a86;--t-blue:#1c2640;--t-amber:#2d2312;--t-green:#1e2917;--t-indigo:#22233c;--t-red:#33201b;--track:#2a2f3e;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.55;font-variant-numeric:tabular-nums}
.wrap{max-width:1040px;margin:0 auto;padding-inline:20px;padding-block:28px 56px}
a{color:var(--blue)}
.ped{--acc:var(--blue);--tint:var(--t-blue)}.fam{--acc:var(--amber);--tint:var(--t-amber)}.eq{--acc:var(--green);--tint:var(--t-green)}.app{--acc:var(--indigo);--tint:var(--t-indigo)}
.bar-top{display:flex;justify-content:space-between;align-items:baseline;gap:12px;border-bottom:2px solid var(--acc);padding-bottom:8px;margin-bottom:22px;flex-wrap:wrap}
.brand{font-family:var(--serif);font-weight:600;font-size:18px;color:var(--head);text-decoration:none}
.brand span{color:var(--amber)}
.tag{font-size:12px;text-transform:uppercase;letter-spacing:.1em;font-weight:600;color:var(--acc)}
.tb{display:grid;grid-template-columns:auto 1fr;gap:6px 18px;align-items:start;margin-bottom:18px}
.tb .num{font-family:var(--serif);font-weight:600;font-size:52px;line-height:.9;color:var(--acc);padding-right:16px;border-right:1px solid var(--rule)}
h1{font-family:var(--serif);font-weight:600;font-size:clamp(26px,4vw,36px);line-height:1.1;color:var(--head);margin:0 0 8px;text-wrap:balance}
h2{font-family:var(--serif);font-weight:600;font-size:22px;color:var(--head);margin:0 0 10px;line-height:1.2}
h3{font-family:var(--serif);font-weight:600;font-size:18px;color:var(--head);margin:0 0 6px;line-height:1.25}
.lede{color:var(--muted);font-size:17px;margin:0;max-width:62ch}
.k{display:block;font-family:var(--sans);font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:var(--acc);font-weight:600;margin-bottom:4px}
.card{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:18px}
.tint{background:var(--tint);border-radius:10px;padding:16px 18px}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:16px}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:14px}
.grid2>*,.grid3>*{min-width:0}
.stack{display:flex;flex-direction:column;gap:14px}
label{font-size:14px;font-weight:600;color:var(--head);display:block;margin-bottom:6px}
input[type=number],select{font:inherit;font-size:18px;padding:10px 12px;border:1px solid var(--rule);border-radius:8px;background:var(--surface);color:var(--ink);width:100%}
input:focus-visible,select:focus-visible,button:focus-visible,a:focus-visible{outline:3px solid var(--acc);outline-offset:2px}
button{font:inherit;cursor:pointer}
.btn{background:var(--acc);color:var(--surface);border:0;border-radius:8px;padding:10px 16px;font-weight:600;font-size:15px}
.btn.ghost{background:transparent;color:var(--acc);border:1.5px solid var(--acc)}
.btn:disabled{opacity:.45;cursor:default}
.tile .v{font-family:var(--serif);font-weight:600;font-size:34px;line-height:1;color:var(--acc)}
.tile .v small{font-size:16px;font-weight:600;margin-left:4px}
.tile .d{font-size:14px;color:var(--muted);margin-top:6px}
.meter{position:relative;height:14px;background:var(--track);border-radius:7px;overflow:visible;margin:14px 0 26px}
.meter i{position:absolute;left:0;top:0;bottom:0;border-radius:7px;background:var(--acc);transition:width .25s}
.meter .goal{position:absolute;top:-6px;bottom:-6px;border-left:2px dashed var(--head)}
.meter .goal span{position:absolute;top:22px;transform:translateX(-50%);font-size:12px;color:var(--muted);white-space:nowrap}
.meter .zero{position:absolute;left:0;top:22px;font-size:12px;color:var(--muted)}
.foods{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,250px),1fr));gap:8px}
.food{display:grid;grid-template-columns:1fr auto;gap:2px 10px;align-items:center;border:1px solid var(--rule);border-radius:8px;padding:8px 10px;background:var(--surface)}
.food .n{font-weight:600;font-size:15px}
.food .m{font-size:12.5px;color:var(--muted);grid-column:1}
.food .p{font-size:13px;color:var(--acc);font-weight:600}
.qty{display:flex;align-items:center;gap:6px;grid-row:1/3;grid-column:2}
.qty button{width:32px;height:32px;border-radius:50%;border:1.5px solid var(--acc);background:transparent;color:var(--acc);font-weight:700;font-size:18px;line-height:1}
.qty b{min-width:18px;text-align:center}
.food.on{border-color:var(--acc);background:var(--tint)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{border:1.5px solid var(--acc);color:var(--acc);background:transparent;border-radius:999px;padding:6px 12px;font-size:14px;font-weight:600}
.chip[aria-pressed="true"]{background:var(--acc);color:var(--surface)}
.status{display:inline-block;border-radius:999px;padding:4px 12px;font-weight:600;font-size:14px}
.status.ok{background:var(--t-green);color:var(--green)}.status.warn{background:var(--t-amber);color:var(--amber)}.status.bad{background:var(--t-red);color:var(--red)}
.src{font-size:13px;color:var(--muted);border-top:1px solid var(--rule);padding-top:12px;margin-top:28px}
.src ol{padding-left:20px;margin:6px 0 0}
.src li{overflow-wrap:anywhere}
sup.r{font-size:.62em;color:var(--acc);font-weight:600;line-height:0}
.back{font-size:14px;font-weight:600;color:var(--acc);text-decoration:none;background:none;border:0;padding:0}
.big{font-family:var(--serif);font-size:24px;line-height:1.35;color:var(--head)}
.q-opts{display:flex;gap:12px;flex-wrap:wrap}
.q-opts .btn{font-size:17px;padding:12px 22px}
.btn.choice{background:var(--surface);color:var(--head);border:1.5px solid var(--acc);min-width:140px}
.btn.choice:hover{background:var(--tint)}
.fb{border-radius:10px;padding:14px 16px;margin-top:14px}
.fb.ok{background:var(--t-green)}.fb.no{background:var(--t-red)}
.fb b{display:block;font-family:var(--serif);font-size:19px;margin-bottom:4px}
.fb.ok b{color:var(--green)}.fb.no b{color:var(--red)}
.progress{display:flex;gap:4px;margin:6px 0 16px}
.progress i{flex:1;height:6px;border-radius:3px;background:var(--track)}
.progress i.done{background:var(--acc)}
.progress i.cur{background:var(--head)}
.step{border-left:3px solid var(--acc);padding-left:14px}
.opt{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-bottom:1px solid var(--rule);font-size:15px}
.opt input{width:20px;height:20px;margin-top:2px;accent-color:var(--acc);flex:none}
.summary{white-space:pre-wrap;font-family:ui-monospace,"SFMono-Regular",Menlo,monospace;font-size:13.5px;line-height:1.55;background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:14px;overflow-x:auto}
.note{font-size:14px;color:var(--muted)}
table.mini{width:100%;border-collapse:collapse;font-size:15px}
table.mini td{padding:7px 0;border-bottom:1px solid var(--rule)}
table.mini td:last-child{text-align:right;font-weight:600;color:var(--acc)}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

def page(title, body, aud='app', standalone=True, extra_head=''):
    head = f'<title>{html.escape(title)}</title>{FONTS_LINK}<style>{CSS}</style>{extra_head}'
    if standalone:
        return ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                f'{head}</head><body class="{aud}">{body}</body></html>')
    return f'{head}<div class="{aud}">{body}</div>'

TOP = lambda aud, n: (f'<div class="bar-top"><a class="brand" href="../index.html" onclick="if(history.length>1){{history.back();return false}}">Kit <span>Comida Primeiro</span></a>'
                      f'<span class="tag">Ferramenta · {n:02d} de 20</span></div>')
SRC = lambda items: '<div class="src"><b>Fontes</b><ol>' + ''.join(f'<li>{html.escape(t)}</li>' for t in items) + '</ol></div>'
FOOTNOTE = ('<p class="note" style="margin-top:18px">Kit Comida Primeiro · material de apoio da aula “Creatina e Whey Protein: modismo inadequado”, '
            '42º Congresso Brasileiro de Pediatria, 2026. Getúlio Bernardo Morato Filho, Escola Superior de Ciências da Saúde, Brasília, DF. '
            'Orientação geral, que não substitui a avaliação individual.</p>')

# ------------------------------------------------------------------ 01 calculadora de proteína
foods_js = json.dumps([{'k': k, 'n': v[0], 'm': v[1], 'p': v[3], 'kc': v[4]} for k, v in FOODS.items()], ensure_ascii=False)
combos_js = json.dumps([{'n': n, 'parts': parts, 'note': note} for n, parts, note in COMBOS], ensure_ascii=False)
T01 = TOP('app', 1) + """
<div class="tb"><div class="num">01</div><div><h1>Calculadora de proteína do jovem atleta</h1>
<p class="lede">Informe o peso, a idade e o número de refeições. A meta do atleta, de cerca de 1,5&nbsp;g/kg/dia, é dividida pelas refeições; depois, monte o lanche pós-treino com alimentos brasileiros e compare com a meta.</p></div></div>
<div class="grid3" style="margin-bottom:18px">
 <div><label for="peso">Peso (kg)</label><input id="peso" type="number" min="25" max="120" step="0.5" value="60"></div>
 <div><label for="idade">Idade</label><select id="idade"><option value="10">10 anos</option><option value="11">11 anos</option><option value="12">12 anos</option><option value="13">13 anos</option><option value="14">14 anos</option><option value="15" selected>15 anos</option><option value="16">16 anos</option><option value="17">17 anos</option><option value="18">18 anos</option></select></div>
 <div><label for="ref">Refeições por dia</label><select id="ref"><option>4</option><option selected>5</option><option>6</option></select></div>
</div>
<div class="grid3" id="tiles"></div>
<p class="note" id="ctx" style="margin-top:12px"></p>
<div class="card" style="margin-top:22px">
 <h2><span class="k">Monte o lanche pós-treino</span>Meta por refeição: <span id="goalTxt"></span></h2>
 <div class="meter" id="meter"><i id="fill"></i><span class="zero">0 g</span><span class="goal" id="goal"><span id="goalLbl"></span></span></div>
 <p class="big" id="sumTxt" style="font-size:22px"></p>
 <div class="chips" id="combos" style="margin:12px 0 16px" aria-label="Lanches prontos"></div>
 <div class="foods" id="foods"></div>
 <p class="note" style="margin-top:12px">Valores de proteína e energia por medida caseira da Tabela Brasileira de Composição de Alimentos, versão 7.3.</p>
</div>
""" + SRC(['Institute of Medicine. Dietary reference intakes for energy, carbohydrate, fiber, fat, fatty acids, cholesterol, protein, and amino acids. Washington (DC): National Academies Press; 2005. doi:10.17226/10490',
          'Desbrow B. Youth athlete development and nutrition. Sports Med. 2021;51(Suppl 1):3-12. doi:10.1007/s40279-021-01534-6',
          'Steffl M, Kinkorova I, Kokstejn J, Petr M. Macronutrient intake in soccer players: a meta-analysis. Nutrients. 2019;11(6):1305. doi:10.3390/nu11061305',
          'Collins J, Maughan RJ, Gleeson M, et al. UEFA expert group statement on nutrition in elite football. Br J Sports Med. 2021;55(8):416. doi:10.1136/bjsports-2019-101961',
          'Tabela Brasileira de Composição de Alimentos (TBCA). Universidade de São Paulo (USP). Food Research Center (FoRC). Versão 7.3. São Paulo; 2025. Disponível em: http://www.fcf.usp.br/tbca']) + FOOTNOTE + """
<script>
const FOODS=__FOODS__, COMBOS=__COMBOS__;
const $=id=>document.getElementById(id);
const f1=x=>(Math.round(x*10+1e-7)/10).toLocaleString('pt-BR',{minimumFractionDigits:1,maximumFractionDigits:1});
const f0=x=>Math.round(x).toLocaleString('pt-BR');
let qty={leite:1,pao:1,minas:1};
function peso(){const v=parseFloat($('peso').value);return isFinite(v)&&v>=25&&v<=120?v:null}
function render(){
 const w=peso(), age=+$('idade').value, n=+$('ref').value;
 if(!w){$('tiles').innerHTML='<p class="note">Informe um peso entre 25 e 120 kg.</p>';return}
 const rda = age>=14 ? `<span class="v">${f0(0.85*w)}<small>g/dia</small></span><div class="d">Recomendação geral de 14 a 18 anos: 0,85&nbsp;g/kg/dia<sup class="r">1</sup></div>`
                     : `<span class="v">${f0(0.95*w)}<small>g/dia</small></span><div class="d">Recomendação geral de 9 a 13 anos: 0,95&nbsp;g/kg/dia<sup class="r">1</sup></div>`;
 const teen=age>=13, day=(teen?1.5:0.95)*w, meal=day/n;
 const ath = teen ? `<span class="v">${f0(day)}<small>g/dia</small></span><div class="d">Adolescente atleta, de 13 a 18 anos: cerca de 1,5&nbsp;g/kg/dia, que cobre crescimento e recuperação<sup class="r">2</sup></div>`
                  : `<span class="v">${f0(day)}<small>g/dia</small></span><div class="d">De 10 a 12 anos, a revisão não fixa meta própria para atletas: use 0,95&nbsp;g/kg/dia como piso e avalie a dieta<sup class="r">1,2</sup></div>`;
 $('tiles').innerHTML=`<div class="card tile">${rda}</div>
  <div class="card tile">${ath}</div>
  <div class="card tile"><span class="v">${f0(meal)}<small>g</small></span><div class="d">Por refeição: ${f0(day)}&nbsp;g divididos em ${n} refeições${n===5&&teen?', ou cerca de 0,3&nbsp;g/kg em cada uma, como propõe a revisão':''}<sup class="r">2</sup>.</div></div>`;
 $('ctx').innerHTML=`Para comparar: numa meta-análise com 647 jovens futebolistas de clubes de elite e subelite, o consumo médio foi de 1,9&nbsp;g/kg/dia, o que daria ${f0(1.9*w)}&nbsp;g para este peso<sup class="r">3</sup>. Especialistas em futebol de base consideram adequado até 1,6&nbsp;g/kg/dia para juniores, alcançável com a dieta<sup class="r">4</sup>.`;
 $('goalTxt').textContent=f1(meal)+' g';
 const tot=Object.entries(qty).reduce((s,[k,q])=>s+q*FOODS.find(f=>f.k===k).p,0);
 const kc=Object.entries(qty).reduce((s,[k,q])=>s+q*FOODS.find(f=>f.k===k).kc,0);
 const max=Math.max(meal*1.6,tot*1.05,10);
 $('fill').style.width=Math.min(100,tot/max*100)+'%';
 $('goal').style.left=(meal/max*100)+'%'; $('goalLbl').textContent='meta '+f1(meal)+' g';
 const diff=tot-meal;
 $('sumTxt').innerHTML = tot===0 ? 'Escolha alimentos abaixo ou um lanche pronto.' :
   `${f1(tot)} g de proteína, ${f0(kc)} kcal. ` + (diff>=0 ? (diff<=meal*0.1 ? '<span class="status ok">Na meta</span>' : `<span class="status ok">Passa ${f1(diff)} g da meta</span>`) : (-diff<=meal*0.1 ? `<span class="status warn">Perto da meta: faltam ${f1(-diff)} g</span>` : `<span class="status warn">Faltam ${f1(-diff)} g</span>`));
 $('foods').innerHTML=FOODS.map(f=>{const q=qty[f.k]||0;return `<div class="food${q?' on':''}"><span class="n">${f.n}</span><span class="m">${f.m} · <span class="p">${f1(f.p)} g</span></span>
  <span class="qty"><button aria-label="Tirar ${f.n}" data-k="${f.k}" data-d="-1">−</button><b>${q}</b><button aria-label="Pôr ${f.n}" data-k="${f.k}" data-d="1">+</button></span></div>`}).join('');
}
function combos(){
 $('combos').innerHTML=COMBOS.map((c,i)=>`<button class="chip" data-c="${i}" aria-pressed="false">${c.n}</button>`).join('')+'<button class="chip" data-c="clear" aria-pressed="false">Limpar</button>';
}
document.addEventListener('click',e=>{
 const b=e.target.closest('button'); if(!b) return;
 if(b.dataset.k){const k=b.dataset.k;qty[k]=Math.max(0,(qty[k]||0)+(+b.dataset.d));if(!qty[k])delete qty[k];render()}
 if(b.dataset.c){ if(b.dataset.c==='clear'){qty={}} else {qty={};for(const [k,q] of COMBOS[+b.dataset.c].parts) qty[k]=(qty[k]||0)+q}
   document.querySelectorAll('#combos .chip').forEach(x=>x.setAttribute('aria-pressed',x===b&&b.dataset.c!=='clear'?'true':'false')); render()}
});
['peso','idade','ref'].forEach(id=>$(id).addEventListener('input',render));
combos(); render();
document.querySelector('#combos .chip').setAttribute('aria-pressed','true');
</script>"""
T01 = T01.replace('__FOODS__', foods_js).replace('__COMBOS__', combos_js)

# ------------------------------------------------------------------ 02 hidratação
T02 = TOP('app', 2) + """
<div class="tb"><div class="num">02</div><div><h1>Água no treino</h1>
<p class="lede">Quanto beber durante o treino e como saber, pela balança, se o plano funcionou. Ponto de partida para um plano individual, revisto ao longo da puberdade.</p></div></div>
<div class="grid2">
<div class="card stack"><h2><span class="k">Plano para o treino</span>Quanto oferecer</h2>
 <div class="grid2"><div><label for="w">Peso (kg)</label><input id="w" type="number" min="25" max="120" step="0.5" value="60"></div>
 <div><label for="min">Duração do treino (min)</label><input id="min" type="number" min="15" max="300" step="5" value="90"></div></div>
 <div class="grid3" id="plan"></div>
 <p class="note">Cerca de 13&nbsp;mL/kg por hora de exercício costumam bastar para evitar déficit importante no atleta em desenvolvimento<sup class="r">1</sup>. Água é a bebida principal<sup class="r">2</sup>. Volumes arredondados para múltiplos de 5&nbsp;mL, como na versão impressa.</p>
</div>
<div class="card stack"><h2><span class="k">Teste da balança</span>O plano funcionou?</h2>
 <div class="grid2"><div><label for="pre">Peso antes (kg)</label><input id="pre" type="number" step="0.1" value="60"></div>
 <div><label for="pos">Peso depois (kg)</label><input id="pos" type="number" step="0.1" value="59.1"></div></div>
 <div id="res"></div>
 <p class="note">Pese com pouca roupa, antes e depois, sem suor e com a bexiga vazia no início. A meta é perder no máximo 2% do peso e não ganhar peso<sup class="r">1</sup>.</p>
</div>
</div>
<div class="tint" style="margin-top:18px"><h3>Por que lembrar o adolescente de beber</h3>
<p style="margin:0">Adolescentes treinados podem perder mais de 4% do peso em campo, com taxas de suor de até 2,16&nbsp;L por hora. O jovem atleta pode não reconhecer os sinais de estresse pelo calor, esquecer de beber se ninguém lembrar e continuar se exercitando para acompanhar os colegas<sup class="r">1</sup>. No calor, em treino intenso ou longo e com uniforme pesado, as medidas que reduzem a carga de calor devem ser adotadas de forma antecipada<sup class="r">1</sup>. A bebida esportiva fica para atividades intensas e prolongadas<sup class="r">2</sup>.</p></div>
""" + SRC(['Desbrow B. Youth athlete development and nutrition. Sports Med. 2021;51(Suppl 1):3-12. doi:10.1007/s40279-021-01534-6',
          'American Academy of Pediatrics Committee on Nutrition; Council on Sports Medicine and Fitness. Sports drinks and energy drinks for children and adolescents: are they appropriate? Pediatrics. 2011;127(6):1182-9. doi:10.1542/peds.2011-0965']) + FOOTNOTE + """
<script>
const $=id=>document.getElementById(id);
const nf=(x,d=0)=>x.toLocaleString('pt-BR',{minimumFractionDigits:d,maximumFractionDigits:d});
function r5(x){return Math.round(x/5)*5}
function plan(){const w=parseFloat($('w').value),m=parseFloat($('min').value);
 if(!(w>=25&&w<=120&&m>=15&&m<=300)){$('plan').innerHTML='<p class="note">Informe peso entre 25 e 120 kg e duração entre 15 e 300 minutos.</p>';return}
 const h=13*w, tot=h*m/60;
 $('plan').innerHTML=`<div class="tile"><span class="v">${nf(r5(tot))}<small>mL</small></span><div class="d">no treino todo</div></div>
 <div class="tile"><span class="v">${nf(r5(h))}<small>mL</small></span><div class="d">por hora</div></div>
 <div class="tile"><span class="v">${nf(r5(h/4))}<small>mL</small></span><div class="d">a cada 15 minutos</div></div>`;}
function test(){const a=parseFloat($('pre').value),b=parseFloat($('pos').value);
 if(!(a>0&&b>0)){$('res').innerHTML='';return}
 const pct=(a-b)/a*100, lim=a*0.02;
 let s;
 if(pct<0) s=`<span class="status warn">Ganhou ${nf(b-a,1)} kg</span><p>Bebeu além do necessário. Reduza o volume no próximo treino<sup class="r">1</sup>.</p>`;
 else if(pct<=2) s=`<span class="status ok">Perdeu ${nf(pct,1)}% do peso</span><p>Dentro da meta de até 2% (${nf(lim,1)} kg para este peso)<sup class="r">1</sup>.</p>`;
 else s=`<span class="status bad">Perdeu ${nf(pct,1)}% do peso</span><p>Acima de 2% (${nf(lim,1)} kg). Aumente a ingestão no próximo treino e reavalie, sobretudo no calor<sup class="r">1</sup>.</p>`;
 $('res').innerHTML=s;}
['w','min'].forEach(i=>$(i).addEventListener('input',plan));['pre','pos'].forEach(i=>$(i).addEventListener('input',test));
plan();test();
</script>"""

# ------------------------------------------------------------------ 03 conduta
T03 = TOP('app', 3) + """
<div class="tb"><div class="num">03</div><div><h1>Conduta passo a passo</h1>
<p class="lede">Para o adolescente que pediu ou já usa suplemento. Marque o que encontrou na consulta; o resumo da conduta, com as fontes, se monta ao lado e pode ser copiado para o prontuário. A tela abre com o caso da aula como exemplo.</p></div></div>
<div class="grid2">
<div class="stack">
 <p class="note" style="margin:0">O passo 1 (perguntar antes de opinar) e o passo 6 (comida primeiro e retorno marcado) entram sempre no resumo, como na versão impressa.</p>
 <div class="card step" style="--acc:var(--red)"><h3>Passo 2. Algum sinal que muda a prioridade?</h3>
  <label class="opt"><input type="checkbox" data-g="al" value="reds">Restrição alimentar, perda de peso ou alteração menstrual</label>
  <label class="opt"><input type="checkbox" data-g="al" value="dism">Sofrimento com a aparência, rotina rígida de treino e dieta</label>
  <label class="opt"><input type="checkbox" data-g="al" value="aas">Acne intensa, ginecomastia, mudança rápida do corpo ou do humor</label></div>
 <div class="card step"><h3>Passo 3. O que ele já usa?</h3>
  <label class="opt"><input type="checkbox" data-g="uso" value="creatina" checked>Creatina</label>
  <label class="opt"><input type="checkbox" data-g="uso" value="proteina" checked>Proteína em pó (whey ou outra)</label>
  <label class="opt"><input type="checkbox" data-g="uso" value="estimulante">Energético, pré-treino ou cafeína em pó</label>
  <label class="opt"><input type="checkbox" data-g="uso" value="risco">Produto sem procedência, comprado pela internet ou com promessa hormonal</label>
  <label class="opt"><input type="checkbox" data-g="uso" value="nada">Ainda não usa; só pediu (desmarca os demais)</label></div>
 <div class="card step"><h3>Passo 4. Há indicação clínica?</h3>
  <label class="opt"><input type="radio" name="ind" value="nao" checked>Não</label>
  <label class="opt"><input type="radio" name="ind" value="restr">Dieta restritiva que não alcança a meta, como em alguns vegetarianos</label>
  <label class="opt"><input type="radio" name="ind" value="doenca">Doença com indicação estabelecida</label></div>
 <div class="card step" style="--acc:var(--amber)"><h3>Passo 5. Há comida suficiente em casa?</h3>
  <label class="opt"><input type="checkbox" data-g="soc" value="acesso">Pouco acesso a comida (insegurança alimentar)</label></div>
</div>
<div class="stack" style="position:sticky;top:12px;align-self:start">
 <div class="card"><h2><span class="k">Resumo da conduta</span>O que fazer</h2><ol id="out" style="padding-left:20px;margin:0"></ol></div>
 <div class="card"><h3>Texto para o prontuário</h3><div class="summary" id="rec"></div>
 <div style="display:flex;gap:10px;margin-top:10px;flex-wrap:wrap"><button class="btn" id="copy">Copiar texto</button><button class="btn ghost" id="clear">Limpar marcações</button></div>
 <p class="note" id="copied" aria-live="polite"></p></div>
</div></div>
""" + SRC(['Eisenberg ME, Wall M, Neumark-Sztainer D. Muscle-enhancing behaviors among adolescent girls and boys. Pediatrics. 2012;130(6):1019-26.',
 'Brasil. Agência Nacional de Vigilância Sanitária. Instrução Normativa nº 28/2018 e Instrução Normativa nº 373/2025.',
 'Desbrow B. Youth athlete development and nutrition. Sports Med. 2021;51(Suppl 1):3-12.',
 'Steffl M et al. Macronutrient intake in soccer players: a meta-analysis. Nutrients. 2019;11(6):1305.',
 'American Academy of Pediatrics. Sports drinks and energy drinks for children and adolescents: are they appropriate? Pediatrics. 2011;127(6):1182-9.',
 'Tucker J et al. Unapproved pharmaceutical ingredients included in dietary supplements associated with US Food and Drug Administration warnings. JAMA Netw Open. 2018;1(6):e183337.',
 'LaBotz M, Griesemer BA; Council on Sports Medicine and Fitness. Use of performance-enhancing substances. Pediatrics. 2016;138(1):e20161300.',
 'Barretto JR, Gouveia MADC, Alves C. Use of dietary supplements by children and adolescents. J Pediatr (Rio J). 2024;100 Suppl 1:S31-9.',
 'Hargreaves D et al. Strategies and interventions for healthy adolescent growth, nutrition, and development. Lancet. 2022;399(10320):198-210.',
 'Maughan RJ et al. IOC consensus statement: dietary supplements and the high-performance athlete. Br J Sports Med. 2018;52(7):439-55.',
 'Mountjoy M et al. 2023 International Olympic Committee consensus statement on Relative Energy Deficiency in Sport (REDs). Br J Sports Med. 2023;57(17):1073-97.',
 'Nagata JM et al. Muscle dysmorphia in adolescents and young adults. Lancet Child Adolesc Health. 2026;10(2):122-34.',
 'Paruthi S et al. Recommended amount of sleep for pediatric populations. J Clin Sleep Med. 2016;12(6):785-6.',
 'Sociedade Brasileira de Pediatria, Departamento Científico de Nutrologia. Consumo de bebidas energéticas por crianças e adolescentes. Documento Científico nº 10. Rio de Janeiro: SBP; 2022.',
 'Health Canada. Caffeine in foods [Internet]. Ottawa: Government of Canada; 2025.']) + FOOTNOTE + """
<script>
const $=id=>document.getElementById(id);
const S=n=>`<sup class="r">${n}</sup>`;
function sel(g){return [...document.querySelectorAll(`input[data-g="${g}"]:checked`)].map(x=>x.value)}
function build(){
 const uso=sel('uso'), al=sel('al'), soc=sel('soc'), ind=document.querySelector('input[name=ind]:checked').value;
 const L=[], R=[];
 L.push('Perguntar sem julgamento o que usa, para quê, quanto, onde comprou e quem indicou; conversar também a sós'+S(1)+'.');
 if(al.includes('reds')){L.push('Restrição, perda de peso ou alteração menstrual: avaliar deficiência energética relativa no esporte'+S(11)+'.');R.push('Sinais de baixa disponibilidade energética: avaliação dirigida.')}
 if(al.includes('dism')){L.push('Sofrimento com a aparência ou rotina rígida: rastrear dismorfia muscular e encaminhar à saúde mental quando indicado'+S(12)+'.');R.push('Rastreio de dismorfia muscular indicado.')}
 if(al.includes('aas')){L.push('Acne intensa, ginecomastia ou mudança rápida do corpo ou do humor: considerar uso de esteroides anabolizantes'+S(7)+'.');R.push('Sinais sugestivos de esteroides anabolizantes: avaliação clínica e laboratorial dirigida.')}
 if(uso.includes('creatina')){L.push('Combinar a suspensão da creatina: não é autorizada em suplementos de 0 a 18 anos'+S(2)+'.');R.push('Combinada a suspensão da creatina (não autorizada em suplementos antes dos 19 anos).')}
 if(uso.includes('proteina')){L.push('Calcular a proteína da dieta antes de decidir: a necessidade gira em torno de 1,5 g/kg/dia'+S(3)+'; numa meta-análise com 647 jovens futebolistas de clubes de elite e subelite, o consumo médio foi de 1,9 g/kg/dia'+S(4)+'.');R.push('Proteína em pó: estimada a ingestão da dieta; orientado plano alimentar.')}
 if(uso.includes('estimulante')){L.push('Desaconselhar energético e pré-treino: não são apropriados para crianças e adolescentes'+S('5,14')+'; somar a cafeína de todas as fontes do dia, com teto de 2,5 mg/kg/dia'+S(15)+'.');R.push('Orientado suspender energético ou pré-treino.')}
 if(uso.includes('risco')){L.push('Investigar esteroides e outras substâncias: entre 92 produtos de ganho muscular já sob alerta oficial nos Estados Unidos, 82 continham esteroides ou similares'+S(6)+'.');R.push('Produto sem procedência ou com promessa hormonal: investigação dirigida.')}
 if(ind==='restr'){L.push('Dieta restritiva abaixo da meta: avaliação nutricional completa; o suplemento pode ter lugar, com acompanhamento'+S('8,10')+'.');R.push('Indicação possível: dieta restritiva abaixo da meta; avaliação nutricional.')}
 if(soc.includes('acesso')){L.push('Pouco acesso a comida: acionar o serviço social e a escola; rede de proteção social e alimentação escolar antes de qualquer produto'+S(9)+'.');R.push('Insegurança alimentar: acionados serviço social e escola.')}
 if(ind==='doenca'){L.push('Doença com indicação estabelecida: prescrição médica e seguimento especializado.');R.push('Indicação clínica estabelecida: prescrição e seguimento especializado.')}
 L.push('Comida primeiro: cerca de 0,3 g/kg de proteína em cada uma de 5 refeições, lanche pós-treino de comida, água no treino e sono de 8 a 10 horas de 13 a 18 anos (9 a 12 horas de 6 a 12 anos)'+S('3,13')+'.');
 R.push('Orientação: comida primeiro, lanche pós-treino, hidratação e sono adequado à idade.');
 L.push('Registrar no prontuário e marcar retorno com a família; com a concordância do adolescente, incluir o treinador no plano.');
 $('out').innerHTML=L.map(x=>`<li style="margin-bottom:8px">${x}</li>`).join('');
 const usoTxt = uso.filter(u=>u!=='nada').map(u=>({creatina:'creatina',proteina:'proteína em pó',estimulante:'energético/pré-treino',risco:'produto sem procedência'}[u])).join(', ')||'nenhum (apenas pedido)';
 $('rec').textContent=`AVALIAÇÃO DE SUPLEMENTOS (adolescente que pratica esporte)\\nEm uso: ${usoTxt}.\\n`+R.map(x=>'- '+x).join('\\n')+'\\nRetorno combinado com a família.';
}
document.addEventListener('change',e=>{const t=e.target;
 if(t.dataset&&t.dataset.g==='uso'&&t.checked){
  if(t.value==='nada'){document.querySelectorAll('input[data-g="uso"]').forEach(x=>{if(x!==t)x.checked=false})}
  else{const n=document.querySelector('input[data-g="uso"][value="nada"]');if(n)n.checked=false}}
 build()});
$('clear').addEventListener('click',()=>{document.querySelectorAll('input[type=checkbox]').forEach(x=>x.checked=false);document.querySelector('input[name=ind][value=nao]').checked=true;build()});
$('copy').addEventListener('click',async()=>{const t=$('rec').textContent;try{await navigator.clipboard.writeText(t);$('copied').textContent='Texto copiado.'}catch(e){const r=document.createRange();r.selectNodeContents($('rec'));const s=getSelection();s.removeAllRanges();s.addRange(r);$('copied').textContent='Texto selecionado; use Ctrl+C ou o menu para copiar.'}});
build();
</script>"""

# ------------------------------------------------------------------ 04 quiz
QUIZ = [
 ('Adolescente que treina precisa de whey para ganhar músculo.', False, 'Na maioria das vezes, a comida dá conta: a necessidade gira em torno de 1,5 g de proteína por quilo por dia, e especialistas do futebol de base dizem que a proteína extra se alcança com a dieta, sem suplementos.', 'Desbrow, Sports Med 2021; Collins et al., Br J Sports Med 2021'),
 ('Um lanche com um copo de leite, um pão francês e uma fatia de queijo minas tem cerca de 17 g de proteína.', True, 'Somam 17,3 g pela Tabela Brasileira de Composição de Alimentos. Para quem pesa 60 kg, a meta de um lanche é de cerca de 18 g.', 'Tabela Brasileira de Composição de Alimentos, versão 7.3, 2025; Desbrow, Sports Med 2021'),
 ('Creatina é um tipo de anabolizante.', False, 'A creatina é um nutriente que vem da carne e do peixe e também é produzido pelo corpo. Anabolizantes são fármacos com outra estrutura química e outra classificação legal.', 'Maughan et al., Br J Sports Med 2018; Antonio et al., J Int Soc Sports Nutr 2021'),
 ('No Brasil, suplemento de creatina pode ser indicado para menores de 19 anos.', False, 'A Agência Nacional de Vigilância Sanitária (Anvisa) não autoriza creatina em suplementos para nenhuma faixa de 0 a 18 anos. A regra foi mantida em 2025.', 'Agência Nacional de Vigilância Sanitária, Instrução Normativa nº 28/2018 e Instrução Normativa nº 373/2025'),
 ('Todo suplemento tem exatamente o que diz o rótulo.', False, 'Sete de dez marcas brasileiras de whey analisadas tinham menos proteína que o rótulo, e já se encontrou anabolizante não declarado em suplementos.', 'Almeida et al., J Diet Suppl 2016; Geyer et al., Int J Sports Med 2004'),
 ('Adolescentes de 13 a 18 anos precisam de 8 a 10 horas de sono por noite.', True, 'É a recomendação da Academia Americana de Medicina do Sono. Dormir pouco aumenta o risco de acidentes e lesões.', 'Paruthi et al., J Clin Sleep Med 2016'),
 ('Tomar energético antes do treino é uma boa ideia na adolescência.', False, 'A Sociedade Brasileira de Pediatria considera os energéticos não apropriados para crianças e adolescentes, e a Academia Americana de Pediatria afirma que os estimulantes dessas bebidas não têm lugar na dieta dessa idade.', 'Sociedade Brasileira de Pediatria, Documento Científico nº 10, 2022; American Academy of Pediatrics, Pediatrics 2011'),
 ('Na maioria dos treinos, a melhor bebida é a água.', True, 'A água é a principal fonte de hidratação de crianças e adolescentes. A bebida esportiva fica para atividades intensas e prolongadas.', 'American Academy of Pediatrics, Pediatrics 2011'),
 ('No começo do uso, a creatina faz o corpo reter água.', True, 'Na fase de ataque, o peso costuma subir de 1 a 3 kg, sobretudo de água.', 'Antonio et al., J Int Soc Sports Nutr 2021'),
 ('Quem usa proteína em pó na adolescência tem mais chance de começar, depois, a usar esteroides ou outras substâncias para ganhar músculo.', True, 'Uma coorte que acompanhou 1.535 jovens encontrou essa associação, com risco 2,09 vezes maior nos rapazes. Associação não prova causa, mas vale a conversa.', 'Nagata et al., Prev Med Rep 2022'),
 ('Pular refeições para “secar” melhora o desempenho.', False, 'Pouca energia para muito treino pode atrasar a puberdade, prejudicar o osso, alterar os ciclos menstruais e aumentar o risco de lesão.', 'Desbrow, Sports Med 2021; Mountjoy et al., Br J Sports Med 2023'),
 ('Quanto mais proteína, mais músculo.', False, 'Em adultos que treinam musculação, acima de 1,6 g por quilo por dia não houve ganho adicional de massa magra.', 'Morton et al., Br J Sports Med 2018'),
]
quiz_js = json.dumps([{'q': q, 'a': a, 'e': e, 's': s} for q, a, e, s in QUIZ], ensure_ascii=False)
T04 = TOP('app', 4) + """
<div class="tb"><div class="num">04</div><div><h1>Verdade ou mito?</h1>
<p class="lede">Doze afirmações sobre treino, comida e suplementos, para o adolescente responder na sala de espera ou junto com o pediatra.</p></div></div>
<div class="card" id="quiz" style="max-width:760px">
 <div class="progress" id="prog" aria-hidden="true"></div>
 <p class="tag" id="count" style="margin:0 0 8px"></p>
 <p class="big" id="q" style="margin:0 0 18px"></p>
 <div class="q-opts" id="opts"><button class="btn choice" data-a="1">Verdade</button><button class="btn choice" data-a="0">Mito</button></div>
 <div id="fb" aria-live="polite"></div>
 <div style="margin-top:16px;display:flex;gap:10px;flex-wrap:wrap"><button class="btn" id="next" hidden>Próxima</button><button class="btn ghost" id="again" hidden>Jogar de novo</button></div>
</div>
<p class="src">As fontes de cada resposta aparecem logo abaixo da explicação. Referências completas no item 20 do kit.</p>""" + FOOTNOTE + """
<script>
const Q=__QUIZ__; const $=id=>document.getElementById(id);
let i=0, score=0, answered=false;
function show(){answered=false;$('fb').innerHTML='';$('next').hidden=true;$('again').hidden=true;$('opts').hidden=false;
 if(i>=Q.length){$('q').innerHTML=`Você acertou ${score} de ${Q.length}.`;$('count').textContent='Resultado';$('opts').hidden=true;
  $('fb').innerHTML=`<div class="fb ok"><b>${score>=10?'Você entende do assunto.':score>=7?'Bom resultado.':'Vale conversar com o pediatra.'}</b>Músculo se constrói com treino, comida e sono. Dúvidas sobre suplementos? Converse com o seu pediatra.</div>`;$('again').hidden=false;prog();return}
 $('count').textContent=`Afirmação ${i+1} de ${Q.length}`;$('q').textContent=Q[i].q;prog()}
function prog(){$('prog').innerHTML=Q.map((_,k)=>`<i class="${k<i?'done':k===i?'cur':''}"></i>`).join('')}
$('opts').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||answered)return;answered=true;
 const ans=b.dataset.a==='1', ok=ans===Q[i].a; if(ok)score++;
 $('fb').innerHTML=`<div class="fb ${ok?'ok':'no'}"><b>${ok?'Acertou.':'Não foi desta vez.'} ${Q[i].a?'É verdade.':'É mito.'}</b>${Q[i].e}<p class="note" style="margin:8px 0 0">Fonte: ${Q[i].s}</p></div>`;
 $('opts').hidden=true;$('next').hidden=false;$('next').focus()});
$('next').addEventListener('click',()=>{i++;show()});
$('again').addEventListener('click',()=>{i=0;score=0;show()});
show();
</script>"""
T04 = T04.replace('__QUIZ__', quiz_js)

TOOLS = [('01-calculadora-de-proteina.html', 'Calculadora de proteína', T01), ('02-agua-no-treino.html', 'Água no treino', T02),
         ('03-conduta-passo-a-passo.html', 'Conduta passo a passo', T03), ('04-verdade-ou-mito.html', 'Verdade ou mito', T04)]

if __name__ == '__main__':
    for d in ('site/ferramentas', 'zip/Kit-Comida-Primeiro/ferramentas'):
        os.makedirs(f'{KIT}/{d}', exist_ok=True)
    for fn, title, body in TOOLS:
        doc = page(title + ' · Kit Comida Primeiro', '<main class="wrap">' + body + '</main>', 'app', True)
        for d in ('site/ferramentas', 'zip/Kit-Comida-Primeiro/ferramentas'):
            open(f'{KIT}/{d}/{fn}', 'w').write(doc)
    print('ferramentas ok')
