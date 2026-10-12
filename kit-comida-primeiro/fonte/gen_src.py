# -*- coding: utf-8 -*-
"""Gera src/14 (receituário) e src/15 (cardápio) a partir dos dados da TBCA."""
import os as _os
KIT = _os.path.dirname(_os.path.abspath(__file__))
import sys
sys.path.insert(0, KIT)
from tbca import FOODS, COMBOS, combo_totals, fmt

def qtxt(k, q):
    n, m, g, p, kc, c = FOODS[k]
    if q == 1:
        return n, m
    # medida no plural, simples
    mm = m
    for a, b in [('1 unidade', f'{q} unidades'), ('1 fatia média', f'{q} fatias médias'), ('1 fatia', f'{q} fatias'),
                 ('1 colher de sopa cheia', f'{q} colheres de sopa cheias'), ('1 escumadeira cheia', f'{q} escumadeiras cheias'),
                 ('1 concha cheia', f'{q} conchas cheias')]:
        if mm.startswith(a):
            g2 = g * q
            mm = b + f' ({g2:g} g)'.replace('.', ',')
            break
    return n, mm

# ---------- 15: cardápio
cards = []
for name, parts, note in COMBOS:
    its, p, k = combo_totals(parts)
    lis = ''.join(f'<li><span>{qtxt(i["key"], i["qty"])[0]}</span><span>{fmt(i["prot"])} g</span></li>' for i in its)
    meas = '; '.join(qtxt(i['key'], i['qty'])[1] for i in its)
    cover = int(p / 0.3)
    cover_txt = 'Atinge a meta de todos os pesos da tabela' if cover >= 70 else f'Cobre a meta de quem pesa até {cover} kg' 
    tag = f'<span class="tag">{note}</span>' if note else ''
    pct = min(p, 25) / 25 * 100
    marks = ''.join(f'<span class="tgt" style="left:{v/25*100:.1f}%"></span>' for v in (12, 15, 18, 21))
    cards.append(f'''<div class="dish">{tag}<h3>{name}</h3><ul>{lis}</ul>
<p class="meas">{meas}</p>
<div class="bar"><i style="width:{pct:.1f}%"></i>{marks}</div>
<div class="tot"><b>{fmt(p)} g</b><span>{k:.0f} kcal</span></div>
<p class="cover">{cover_txt}</p></div>''')

head15 = '''<!--{"n":15,"slug":"cardapio-de-lanches-pos-treino","title":"Cardápio de lanches pós-treino","aud":"fam","size":"A4","short":true}-->
<section class="page">
<div class="tb"><div class="num">15</div><div>
<h1>Cardápio de lanches pós-treino com comida brasileira</h1>
<p class="lede">A meta de cada lanche ou refeição depois do treino é de cerca de 0,3&nbsp;g de proteína por quilo de peso[[ref:desbrow]]. Proteína e energia calculadas com a Tabela Brasileira de Composição de Alimentos[[ref:tbca]].</p>
</div></div>
<div class="targets">
<div><span>40 kg</span><b>12 g</b></div><div><span>50 kg</span><b>15 g</b></div><div><span>60 kg</span><b>18 g</b></div><div><span>70 kg</span><b>21 g</b></div>
</div>
<p class="small">Na barra de cada lanche, a escala vai de 0 a 25&nbsp;g, e os traços marcam as metas de 12, 15, 18 e 21&nbsp;g. Acima de 70&nbsp;kg, a meta passa de 21&nbsp;g: escolha as opções marcadas para esse peso, os pratos de almoço ou some um copo de leite (7,7&nbsp;g) a qualquer lanche.</p>
<div class="menu">''' + ''.join(cards[:6]) + '''</div>

</section>
<section class="page">
<div class="menu">''' + ''.join(cards[6:12]) + '''</div>
<div class="box fam"><span class="lbl">Leite e queijo também levam cálcio</span>
<p>No Estudo de Riscos Cardiovasculares em Adolescentes (ERICA), com 71.791 adolescentes brasileiros de 12 a 17 anos, a ingestão de cálcio foi inadequada em 95% a 99% deles, conforme sexo e idade; o baixo consumo de laticínios ajuda a explicar o achado[[ref:souza]]. Lanches com leite, iogurte ou queijo ajudam nas duas frentes.</p></div>
</section>
<section class="page">
<div class="menu">''' + ''.join(cards[12:]) + '''</div>
<div class="cols-2">
<div class="box fam"><span class="lbl">Como usar</span>
<ul><li>Escolha o lanche pela meta do peso e pelo que há em casa; varie ao longo da semana.</li>
<li>Coma logo depois do treino; proteína e carboidrato distribuídos ao longo do dia sustentam a recuperação[[ref:desbrow]].</li>
<li>Para treinos longos, some uma fruta ou mais pão: o carboidrato repõe o combustível gasto[[ref:desbrow]].</li>
<li>Quem treina de manhã pode usar o almoço como refeição pós-treino.</li></ul></div>
<div class="box line"><span class="lbl">Sobre os números</span>
<p>Cada valor corresponde à medida caseira da tabela; quantidades dobradas foram multiplicadas. O ovo cozido da tabela usada tem 10,4&nbsp;g de proteína por 100&nbsp;g; outras tabelas brasileiras trazem valores mais altos, o que deixa conservadoras as contas com ovo. Nos lanches sem ingredientes de origem animal, confira com o pediatra a vitamina B12 e o ferro[[ref:verduci,desbrow]].</p>
<p class="small" style="margin-top:1.4mm">Códigos na tabela: ''' + ', '.join(f'{v[0].lower()} {v[5]}' for v in FOODS.values() if any(v[5]==FOODS[k][5] for _, parts, _ in COMBOS for k, _ in parts)) + '''.</p></div>
</div>
[[sources]]
</section>
'''
open(KIT + '/src/15-cardapio-lanches.html', 'w').write(head15)

# ---------- 14: receituário (A5)
opts = [('Leite, pão francês e queijo minas', ['leite', 'pao', 'minas']), ('Pão francês com 2 ovos', ['pao', 'ovo', 'ovo']),
        ('Vitamina de leite com 2 bananas e 2 colheres de aveia', ['leite', 'banana', 'banana', 'aveia', 'aveia']), ('Iogurte natural com 2 colheres de aveia e 2 bananas', ['iogurte', 'aveia', 'aveia', 'banana', 'banana']),
        ('Bebida de soja, 2 fatias de pão integral e amendoim', ['soja', 'paoint', 'paoint', 'amendoim']), ('Leite, pão francês e 2 ovos (70 kg ou mais)', ['leite', 'pao', 'ovo', 'ovo'])]
lis = ''
for n, ks in opts:
    p = sum(FOODS[k][3] for k in ks)
    lis += f'<li><span>{n}</span><span>{fmt(p)} g</span></li>'
groups = [('Leite, queijos e ovos', ['leite', 'iogurte', 'minas', 'mussarela', 'ovo']),
          ('Carnes e peixes', ['frango', 'moida', 'sardinha']),
          ('Leguminosas e oleaginosas', ['feijao', 'lentilha', 'grao', 'soja', 'amendoim']),
          ('Pães e cereais', ['pao', 'paoint', 'aveia', 'arroz'])]
tab = ''
for g, ks in groups:
    tab += f'<h3 style="margin-top:1.6mm;color:var(--acc)">{g}</h3><div class="foodgrid sm">' + ''.join(f'<div><span>{FOODS[k][0]}<br><small class="muted">{FOODS[k][1]}</small></span><span>{fmt(FOODS[k][3])} g</span></div>' for k in ks) + '</div>'
rx = f'''<!--{{"n":14,"slug":"receituario-de-comida-de-verdade","title":"Receituário de comida de verdade","aud":"fam","size":"A5","short":true}}-->
<section class="page">
<div class="tb"><div class="num" style="font-size:24pt">14</div><div><h1 style="font-size:15pt">Receituário de comida de verdade</h1></div></div>
<div class="rx-fields"><div class="field"><span>Nome</span><div class="write"></div></div><div class="field"><span>Idade</span><div class="write"></div></div><div class="field"><span>Peso</span><div class="write"></div></div><div class="field"><span>Data</span><div class="write"></div></div></div>
<div class="rx"><p class="rx-title">Uso oral, nos dias de treino</p>
<ol>
<li><b>Lanche logo depois do treino.</b> Escolha um:
<ul class="ck" style="margin-top:1mm">{lis}</ul></li>
<li><b>Proteína em todas as refeições:</b> <span class="blank"></span> g por refeição, cerca de 5 vezes ao dia (0,3&nbsp;g × peso em kg)[[ref:desbrow]].</li>
<li><b>Água no treino:</b> <span class="blank"></span> mL por hora (13&nbsp;mL × peso em kg), com mais atenção no calor[[ref:desbrow]].</li>
<li><b>Sono:</b> 8 a 10 horas por noite de 13 a 18 anos; 9 a 12 horas de 6 a 12 anos[[ref:paruthi16]].</li>
<li><b>Energético e pré-treino:</b> não usar[[ref:sbp22,aap11]].</li>
</ol></div>
<div><p class="lbl" style="color:var(--muted)">Observações</p><div class="write"></div><div class="write"></div></div>
<div class="sig"><div>Retorno em</div><div>Assinatura, carimbo e registro no Conselho Regional de Medicina</div></div>
</section>
<section class="page">
<h2><span class="k">Verso</span>Proteína dos alimentos, em medidas de casa[[ref:tbca]]</h2>
<div>{tab}</div>
[[sources]]
</section>
'''
open(KIT + '/src/14-receituario.html', 'w').write(rx)
print('ok')
