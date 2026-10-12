# -*- coding: utf-8 -*-
"""Versão editável (.docx) da carta ao treinador e à escola (item 18)."""
import os as _os
KIT = _os.path.dirname(_os.path.abspath(__file__))
import re, sys
sys.path.insert(0, KIT)
from refs import REF
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

NAVY = RGBColor(0x1F, 0x25, 0x52); ACC = RGBColor(0x4A, 0x76, 0x13); MUT = RGBColor(0x5A, 0x60, 0x72)
doc = Document()
for s in doc.sections:
    s.top_margin = s.bottom_margin = Cm(2.2); s.left_margin = s.right_margin = Cm(2.4)
st = doc.styles['Normal']; st.font.name = 'Georgia'; st.font.size = Pt(11)
st.paragraph_format.space_after = Pt(6); st.paragraph_format.line_spacing = 1.25

order = []
def cite(keys):
    ns = []
    for k in keys.split(','):
        if k not in order: order.append(k)
        ns.append(order.index(k) + 1)
    return ','.join(str(n) for n in sorted(ns))

def para(text, bold_lead=None, align=None, size=None, color=None, space_after=None):
    p = doc.add_paragraph()
    if align: p.alignment = align
    if space_after is not None: p.paragraph_format.space_after = Pt(space_after)
    if bold_lead:
        r = p.add_run(bold_lead + ' '); r.bold = True; r.font.color.rgb = NAVY
    # campos [..] em verde, chamadas ^[..] sobrescritas
    for tok in re.split(r'(\[[^\]]+\]|\^\{[a-z0-9_,]+\})', text):
        if not tok: continue
        if tok.startswith('^{'):
            r = p.add_run(cite(tok[2:-1])); r.font.superscript = True; r.font.size = Pt(8); r.font.color.rgb = ACC
        elif tok.startswith('['):
            r = p.add_run(tok); r.font.color.rgb = ACC
        else:
            r = p.add_run(tok)
        if size: r.font.size = Pt(size)
        if color and not tok.startswith('[') and not tok.startswith('^{'): r.font.color.rgb = color
    return p

para('[Cidade], [data]', align=WD_ALIGN_PARAGRAPH.RIGHT)
para('[Nome do serviço ou consultório]', align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=14)
para('Prezado(a) [nome do treinador ou da coordenação],')
para('Acompanho [nome do atleta], de [idade] anos, que treina [modalidade] com vocês. Com a concordância dele e da família, escrevo para combinar cinco cuidados que fazem diferença na saúde e no rendimento de atletas em crescimento.')
items = [
 ('1. Comida primeiro.', 'A necessidade de proteína do adolescente que treina gira em torno de 1,5 g por quilo por dia e pode ser atendida com a alimentação^{desbrow}. Especialistas em futebol de base recomendam a mesma abordagem para os jogadores juniores^{collins}.'),
 ('2. Suplementos fora da rotina da equipe.', 'Peço que não indiquem nem distribuam suplementos. No Brasil, a creatina não é autorizada em suplementos para menores de 19 anos^{in28,in373}, e já se encontraram substâncias proibidas não declaradas em produtos vendidos como suplementos^{geyer}. Com controle antidopagem, o atleta responde por qualquer substância encontrada, mesmo sem intenção^{abcd}.'),
 ('3. Sem comentários sobre peso e corpo.', 'Comentários sobre peso ou aparência podem precipitar ou perpetuar transtornos alimentares em atletas^{desbrow}. O Comitê Olímpico Internacional recomenda avaliar composição corporal em menores de 18 anos apenas com finalidade médica^{mountjoy23}.'),
 ('4. Água à vontade e pausas para beber.', 'O jovem atleta pode esquecer de beber se ninguém lembrar e continuar se exercitando para acompanhar os colegas^{desbrow}. A água deve estar sempre disponível^{aap11}.'),
 ('5. Avisem a família se notarem', 'perda de peso, refeições puladas, fraturas por estresse ou outras lesões que se repetem, mudança de humor, mudança rápida do corpo ou uso de produtos para ganhar músculo ou emagrecer^{labotz,mountjoy23}.'),
]
for lead, txt in items:
    p = para(txt, bold_lead=lead); p.paragraph_format.left_indent = Cm(0.6)
para('Num programa conduzido dentro das próprias equipes, atletas do ensino médio do sexo feminino passaram a iniciar menos o uso de remédios para emagrecer e de substâncias para melhorar o desempenho^{elliot}.')
para('Fico à disposição para conversar.')
para('Atenciosamente,', space_after=28)
para('[Nome do pediatra]')
para('Conselho Regional de Medicina (CRM) [número e estado] · [telefone ou e-mail profissional]')
h = doc.add_paragraph(); h.paragraph_format.space_before = Pt(18); h.paragraph_format.page_break_before = True
r = h.add_run('Fontes'); r.bold = True; r.font.size = Pt(9); r.font.color.rgb = ACC
for i, k in enumerate(order, 1):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(f'{i}. {REF[k]}'); r.font.size = Pt(8); r.font.color.rgb = MUT
f = doc.sections[0].footer.paragraphs[0]
r = f.add_run('Modelo do Kit Comida Primeiro. Aula “Creatina e Whey Protein: modismo inadequado”, 42º Congresso Brasileiro de Pediatria, 2026. Getúlio Bernardo Morato Filho, Escola Superior de Ciências da Saúde, Brasília, DF.')
r.font.size = Pt(7); r.font.color.rgb = MUT
import datetime
cp = doc.core_properties
cp.title = 'Carta ao treinador e à escola'; cp.author = 'Getúlio Bernardo Morato Filho'; cp.last_modified_by = 'Getúlio Bernardo Morato Filho'
cp.comments = ''; cp.subject = 'Kit Comida Primeiro'; cp.keywords = ''; cp.category = ''
cp.created = cp.modified = datetime.datetime(2026, 10, 12, 9, 0, 0); cp.revision = 1
doc.save(KIT + '/out/18-carta-ao-treinador-e-a-escola.docx')
print('ok', len(order), 'refs')
