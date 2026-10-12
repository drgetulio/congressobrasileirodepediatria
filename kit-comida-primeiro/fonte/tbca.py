# -*- coding: utf-8 -*-
"""Alimentos da TBCA 7.3 (2025), conferidos em 11/10/2026: (nome curto, medida caseira, g ou mL, proteína g, kcal, código)."""
FOODS = {
 'leite':      ('Leite integral', 'copo americano duplo (240 mL)', 240, 7.66, 149, 'BRC0043G'),
 'leited':     ('Leite desnatado', 'copo americano duplo (240 mL)', 240, 7.49, 87, 'BRC0036G'),
 'pao':        ('Pão francês', '1 unidade (50 g)', 50, 4.91, 149, 'BRC0002A'),
 'paoint':     ('Pão de forma integral', '1 fatia (25 g)', 25, 2.64, 62, 'BRC0155A'),
 'minas':      ('Queijo minas frescal', '1 fatia média (30 g)', 30, 4.76, 72, 'BRC0052G'),
 'mussarela':  ('Queijo muçarela', '1 fatia (20 g)', 20, 4.77, 64, 'BRC0059G'),
 'ricota':     ('Ricota', '1 fatia (30 g)', 30, 3.78, 41, 'BRC0051G'),
 'requeijao':  ('Requeijão', '1 colher de sopa cheia (30 g)', 30, 2.97, 84, 'BRC0066G'),
 'iogurte':    ('Iogurte natural', '1 pote (170 g)', 170, 6.75, 106, 'BRC0021G'),
 'ovo':        ('Ovo cozido', '1 unidade (50 g)', 50, 5.20, 62, 'BRC0010J'),
 'frango':     ('Peito de frango grelhado', '1 filé médio (110 g)', 110, 35.3, 165, 'BRC0114F'),
 'patinho':    ('Patinho grelhado', '1 porção média (100 g)', 100, 36.0, 211, 'BRC0045F'),
 'moida':      ('Carne moída refogada', '1 colher de servir cheia (60 g)', 60, 15.7, 129, 'BRC0244F'),
 'sardinha':   ('Sardinha em molho de tomate', '1 lata (125 g)', 125, 31.0, 264, 'BRC0071E'),
 'feijao':     ('Feijão carioca cozido', '1 concha cheia (140 g)', 140, 6.68, 99, 'BRC0001T'),
 'arroz':      ('Arroz branco cozido', '1 escumadeira cheia (85 g)', 85, 2.02, 111, 'BRC0018A'),
 'lentilha':   ('Lentilha cozida', '1 concha cheia (85 g)', 85, 6.21, 83, 'BRC0018T'),
 'grao':       ('Grão-de-bico cozido', '1 concha cheia (120 g)', 120, 9.04, 138, 'BRC0017T'),
 'amendoim':   ('Amendoim torrado', '1 colher de sopa cheia (19 g)', 19, 5.23, 118, 'BRC0021T'),
 'soja':       ('Bebida de soja', 'copo americano duplo (240 mL)', 240, 6.55, 100, 'BRC0043T'),
 'tofu':       ('Tofu', '1 colher de sopa cheia (30 g)', 30, 1.97, 20, 'BRC0056T'),
 'aveia':      ('Aveia em flocos finos', '1 colher de sopa cheia (15 g)', 15, 2.34, 56, 'BRC0024A'),
 'banana':     ('Banana prata', '1 unidade (40 g)', 40, 0.44, 42, 'BRC0011C'),
 'tapioca':    ('Tapioca sem recheio', '1 unidade (60 g)', 60, 0.21, 173, 'BRC0906B'),
}

def item(key, qty=1):
    n, m, g, p, k, c = FOODS[key]
    return dict(key=key, name=n, measure=m, qty=qty, prot=p * qty, kcal=k * qty, code=c)

# combinações de lanche e refeição (quantidade de medidas caseiras)
COMBOS = [
 ('Clássico de padaria', [('leite', 1), ('pao', 1), ('minas', 1)], 'O lanche da aula'),
 ('Pão com ovo', [('pao', 1), ('ovo', 2)], ''),
 ('Pão francês com muçarela', [('pao', 1), ('mussarela', 2)], ''),
 ('Vitamina de banana com aveia', [('leite', 1), ('aveia', 2), ('banana', 2)], 'Bom quando o apetite está baixo'),
 ('Iogurte com aveia e banana', [('iogurte', 1), ('aveia', 2), ('banana', 2)], ''),
 ('Tapioca com ovo e queijo', [('tapioca', 1), ('ovo', 2), ('minas', 1)], ''),
 ('Sanduíche integral de ricota', [('paoint', 2), ('ricota', 2)], ''),
 ('Pão integral com amendoim e bebida de soja', [('paoint', 2), ('amendoim', 1), ('soja', 1)], 'Sem ingredientes de origem animal'),
 ('Grão-de-bico com pão', [('grao', 1), ('pao', 1)], 'Sem ingredientes de origem animal'),
 ('Leite desnatado com pão e requeijão', [('leited', 1), ('pao', 1), ('requeijao', 1)], ''),
 ('Leite, pão francês e dois ovos', [('leite', 1), ('pao', 1), ('ovo', 2)], 'Para quem pesa 70 kg ou mais'),
 ('Leite e pão francês com muçarela', [('leite', 1), ('pao', 1), ('mussarela', 2)], 'Para quem pesa 70 kg ou mais'),
 ('Grão-de-bico em dobro com pão', [('grao', 2), ('pao', 1)], 'Sem ingredientes de origem animal'),
 ('Prato do almoço: arroz, feijão e frango', [('arroz', 2), ('feijao', 1), ('frango', 1)], 'Refeição completa depois do treino da manhã'),
 ('Prato vegetariano: arroz, feijão e ovos', [('arroz', 2), ('feijao', 1), ('ovo', 2)], ''),
]

def combo_totals(parts):
    its = [item(k, q) for k, q in parts]
    return its, sum(i['prot'] for i in its), sum(i['kcal'] for i in its)

def fmt(x, nd=1):
    """Arredonda meio para cima (13,95 vira 14,0), como na conta feita à mão."""
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(1).scaleb(-nd)
    s = str(Decimal(repr(round(x, 6))).quantize(q, rounding=ROUND_HALF_UP))
    return s.replace('.', ',')

if __name__ == '__main__':
    for name, parts, note in COMBOS:
        its, p, k = combo_totals(parts)
        print(f"{name:45s} {p:6.2f} g  {k:5.0f} kcal")
