# -*- coding: utf-8 -*-
"""Referências do kit (Vancouver). Reaproveita as da aula e acrescenta as verificadas em 11/10/2026."""
import os as _os
KIT = _os.path.dirname(_os.path.abspath(__file__))
import sys
from refs_aula import REFS as TALK

REF = dict(TALK)
REF.update({
 'in373': "Brasil. Agência Nacional de Vigilância Sanitária. Instrução Normativa nº 373, de 5 de junho de 2025. Altera a Instrução Normativa nº 28, de 26 de julho de 2018, que estabelece as listas de constituintes, de limites de uso, de alegações e de rotulagem complementar dos suplementos alimentares. Diário Oficial da União. 2025 jun 9; Seção 1.",
 'rdc243': "Brasil. Agência Nacional de Vigilância Sanitária. Resolução da Diretoria Colegiada RDC nº 243, de 26 de julho de 2018. Dispõe sobre os requisitos sanitários dos suplementos alimentares. Diário Oficial da União. 2018 jul 27; Seção 1. Texto compilado disponível em: https://anvisalegis.datalegis.net",
 'rdc843': "Brasil. Agência Nacional de Vigilância Sanitária. Resolução da Diretoria Colegiada RDC nº 843, de 22 de fevereiro de 2024. Dispõe sobre a regularização de alimentos e embalagens sob competência do Sistema Nacional de Vigilância Sanitária (SNVS). Texto compilado disponível em: https://anvisalegis.datalegis.net",
 'anvisa26': "Agência Nacional de Vigilância Sanitária. Anvisa alerta e orienta sobre o prazo de adequação às regras de regularização de alimentos [Internet]. Brasília: Anvisa; 2026 [citado 2026 out 11]. Disponível em: https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2026/anvisa-alerta-e-orienta-sobre-o-prazo-de-adequacao-as-regras-de-regularizacao-de-alimentos",
 'abcd': "Autoridade Brasileira de Controle de Dopagem. Perguntas frequentes [Internet]. Brasília: ABCD; [citado 2026 out 11]. Disponível em: https://www.gov.br/abcd/pt-br/acesso-a-informacao/perguntas-frequentes",
 'abcdmanip': "Autoridade Brasileira de Controle de Dopagem. O risco no consumo de produtos manipulados [Internet]. Brasília: ABCD; [citado 2026 out 11]. Disponível em: https://www.gov.br/abcd/pt-br/composicao/gestao-de-resultados/analise-de-material-suspeito/o-risco-no-consumo-de-produtos-manipulados.pdf",
 'mountjoy23': "Mountjoy M, Ackerman KE, Bailey DM, Burke LM, Constantini N, Hackney AC, et al. 2023 International Olympic Committee's (IOC) consensus statement on Relative Energy Deficiency in Sport (REDs). Br J Sports Med. 2023;57(17):1073-97. doi:10.1136/bjsports-2023-106994",
 'stellingwerff23': "Stellingwerff T, Mountjoy M, McCluskey WT, Ackerman KE, Verhagen E, Heikura IA. Review of the scientific rationale, development and validation of the International Olympic Committee Relative Energy Deficiency in Sport Clinical Assessment Tool: V.2 (IOC REDs CAT2), by a subgroup of the IOC consensus on REDs. Br J Sports Med. 2023;57(17):1109-18. doi:10.1136/bjsports-2023-106914",
 'aap11': "American Academy of Pediatrics Committee on Nutrition; Council on Sports Medicine and Fitness. Sports drinks and energy drinks for children and adolescents: are they appropriate? Pediatrics. 2011;127(6):1182-9. doi:10.1542/peds.2011-0965",
 'healthcanada': "Health Canada. Caffeine in foods [Internet]. Ottawa: Government of Canada; 2025 [citado 2026 out 11]. Disponível em: https://www.canada.ca/en/health-canada/services/food-nutrition/food-safety/food-additives/caffeine-foods.html",
 'paruthi16': "Paruthi S, Brooks LJ, D'Ambrosio C, Hall WA, Kotagal S, Lloyd RM, et al. Recommended amount of sleep for pediatric populations: a consensus statement of the American Academy of Sleep Medicine. J Clin Sleep Med. 2016;12(6):785-6. doi:10.5664/jcsm.5866",
 'antonio21': "Antonio J, Candow DG, Forbes SC, Gualano B, Jagim AR, Kreider RB, et al. Common questions and misconceptions about creatine supplementation: what does the scientific evidence really show? J Int Soc Sports Nutr. 2021;18(1):13. doi:10.1186/s12970-021-00412-w",
 'vandermerwe09': "van der Merwe J, Brooks NE, Myburgh KH. Three weeks of creatine monohydrate supplementation affects dihydrotestosterone to testosterone ratio in college-aged rugby players. Clin J Sport Med. 2009;19(5):399-404. doi:10.1097/JSM.0b013e3181b8b52f",
 'nieschlag15': "Nieschlag E, Vorona E. Mechanisms in endocrinology: medical consequences of doping with anabolic androgenic steroids: effects on reproductive functions. Eur J Endocrinol. 2015;173(2):R47-58. doi:10.1530/EJE-15-0080",
 'iomtable': "Institute of Medicine. Dietary Reference Intakes (DRIs): recommended dietary allowances and adequate intakes, total water and macronutrients [Internet]. Washington (DC): National Academies Press; [citado 2026 out 11]. Disponível em: https://www.ncbi.nlm.nih.gov/books/NBK56068/table/summarytables.t4/",
})
# fix: TBCA citation date

SHORT = {
 'iom': 'Institute of Medicine. Dietary Reference Intakes, 2005', 'iomtable': 'Institute of Medicine. Tabela das DRIs',
 'desbrow': 'Desbrow B. Sports Med. 2021;51(Suppl 1):3-12', 'steffl': 'Steffl M et al. Nutrients. 2019;11(6):1305',
 'tbca': 'Tabela Brasileira de Composição de Alimentos (TBCA), versão 7.3, 2025', 'paruthi16': 'Paruthi S et al. J Clin Sleep Med. 2016;12(6):785-6',
 'healthcanada': 'Health Canada. Caffeine in foods, 2025', 'in28': 'Anvisa. Instrução Normativa nº 28/2018',
 'in373': 'Anvisa. Instrução Normativa nº 373/2025', 'geyer': 'Geyer H et al. Int J Sports Med. 2004;25(2):124-9',
 'tucker': 'Tucker J et al. JAMA Netw Open. 2018;1(6):e183337', 'nagata22': 'Nagata JM et al. Prev Med Rep. 2022;27:101778',
 'aap11': 'American Academy of Pediatrics. Pediatrics. 2011;127(6):1182-9', 'nagata26': 'Nagata JM et al. Lancet Child Adolesc Health. 2026;10(2):122-34',
 'eisenberg': 'Eisenberg ME et al. Pediatrics. 2012;130(6):1019-26', 'almeida': 'Almeida CC et al. J Diet Suppl. 2016;13(3):313-23',
 'collins': 'Collins J et al. Br J Sports Med. 2021;55(8):416', 'maughan': 'Maughan RJ et al. Br J Sports Med. 2018;52(7):439-55',
 'labotz': 'LaBotz M et al. Pediatrics. 2016;138(1):e20161300', 'antonio21': 'Antonio J et al. J Int Soc Sports Nutr. 2021;18(1):13',
 'mountjoy23': 'Mountjoy M et al. Br J Sports Med. 2023;57(17):1073-97', 'morton': 'Morton RW et al. Br J Sports Med. 2018;52(6):376-84',
 'jagim': 'Jagim AR, Kerksick CM. Nutrients. 2021;13(2):664', 'bergeron': 'Bergeron MF et al. Br J Sports Med. 2024;58(17):946-65',
 'pense': 'IBGE. PeNSE 2015', 'close': 'Close GL et al. Int J Sport Nutr Exerc Metab. 2022;32(5):371-86',
}

REF.update({
 'abcdlista': "Autoridade Brasileira de Controle de Dopagem. Substâncias e métodos proibidos: Lista Proibida 2026 [Internet]. Brasília: ABCD; 2026 [citado 2026 out 11]. Disponível em: https://www.gov.br/abcd/pt-br/composicao/atletas/substancias-e-metodos-proibidos",
 'informed': "LGC Group. Informed Sport [Internet]. [citado 2026 out 11]. Disponível em: https://sport.wetestyoutrust.com/",
 'nsf': "NSF International. NSF Certified for Sport [Internet]. [citado 2026 out 11]. Disponível em: https://www.nsfsport.com/",
 'koelner': "Kölner Liste [Internet]. [citado 2026 out 11]. Disponível em: https://www.koelnerliste.com/",
})
SHORT.update({'abcd': 'Autoridade Brasileira de Controle de Dopagem. Perguntas frequentes', 'rdc243': 'Anvisa. RDC nº 243/2018',
 'aap11': 'American Academy of Pediatrics. Pediatrics. 2011;127(6):1182-9'})

REF.update({
 'torstveit23': "Torstveit MK, Ackerman KE, Constantini N, Holtzman B, Koehler K, Mountjoy ML, et al. Primary, secondary and tertiary prevention of Relative Energy Deficiency in Sport (REDs): a narrative review by a subgroup of the IOC consensus on REDs. Br J Sports Med. 2023;57(17):1119-26. doi:10.1136/bjsports-2023-106932",
 'stellingwerff23': "Stellingwerff T, Mountjoy M, McCluskey WT, Ackerman KE, Verhagen E, Heikura IA. Review of the scientific rationale, development and validation of the International Olympic Committee Relative Energy Deficiency in Sport Clinical Assessment Tool: V.2 (IOC REDs CAT2)-by a subgroup of the IOC consensus on REDs. Br J Sports Med. 2023;57(17):1109-18. doi:10.1136/bjsports-2023-106914",
})

REF.update({
 'who2020': "Bull FC, Al-Ansari SS, Biddle S, Borodulin K, Buman MP, Cardon G, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. Br J Sports Med. 2020;54(24):1451-62. doi:10.1136/bjsports-2020-102955",
 'melin14': "Melin A, Tornberg AB, Skouby S, Faber J, Ritz C, Sjödin A, et al. The LEAF questionnaire: a screening tool for the identification of female athletes at risk for the female athlete triad. Br J Sports Med. 2014;48(7):540-5. doi:10.1136/bjsports-2013-093240",
 'cem': "Conselho Federal de Medicina. Código de Ética Médica: Resolução CFM nº 2.217, de 27 de setembro de 2018, modificada pelas Resoluções CFM nº 2.222/2018 e 2.226/2019. Brasília: CFM; 2019. Disponível em: https://portal.cfm.org.br/images/PDF/cem2019.pdf",
 'cfm2336': "Conselho Federal de Medicina. Resolução CFM nº 2.336, de 13 de julho de 2023. Dispõe sobre publicidade e propaganda médicas. Diário Oficial da União. 2023 set 13; Seção 1:312.",
 'sbp22': "Sociedade Brasileira de Pediatria, Departamento Científico de Nutrologia. Consumo de bebidas energéticas por crianças e adolescentes. Documento Científico nº 10. Rio de Janeiro: SBP; 2022 [citado 2026 out 12]. Disponível em: https://www.sbp.com.br/fileadmin/user_upload/23377c-DC-Consumo_BebEnergeticas_crc_e_adl.pdf",
 'anvisa25': "Brasil. Agência Nacional de Vigilância Sanitária. Creatinas: Anvisa divulga resultados de análise em suplementos [Internet]. Brasília: Anvisa; 2025 [citado 2026 out 11]. Disponível em: https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2025/creatinas-anvisa-divulga-resultados-de-analise-em-suplementos",
 'anvisa26': "Brasil. Agência Nacional de Vigilância Sanitária. Anvisa alerta e orienta sobre o prazo de adequação às regras de regularização de alimentos [Internet]. Brasília: Anvisa; 2026 [citado 2026 out 11]. Disponível em: https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2026/anvisa-alerta-e-orienta-sobre-o-prazo-de-adequacao-as-regras-de-regularizacao-de-alimentos",
 'abcd': "Brasil. Autoridade Brasileira de Controle de Dopagem. Perguntas frequentes [Internet]. Brasília: ABCD; [citado 2026 out 11]. Disponível em: https://www.gov.br/abcd/pt-br/acesso-a-informacao/perguntas-frequentes",
 'abcdmanip': "Brasil. Autoridade Brasileira de Controle de Dopagem. O risco no consumo de produtos manipulados [Internet]. Brasília: ABCD; [citado 2026 out 11]. Disponível em: https://www.gov.br/abcd/pt-br/composicao/gestao-de-resultados/analise-de-material-suspeito/o-risco-no-consumo-de-produtos-manipulados.pdf",
 'abcdlista': "Brasil. Autoridade Brasileira de Controle de Dopagem. Substâncias e métodos proibidos: Lista Proibida 2026 [Internet]. Brasília: ABCD; 2026 [citado 2026 out 11]. Disponível em: https://www.gov.br/abcd/pt-br/composicao/atletas/substancias-e-metodos-proibidos",
})
SHORT.update({
 'who2020': 'Bull FC et al. Br J Sports Med. 2020;54(24):1451-62 (Organização Mundial da Saúde)', 'sbp22': 'Sociedade Brasileira de Pediatria. Documento Científico nº 10, 2022',
 'souza': 'Souza AM et al. Rev Saude Publica. 2016;50 Suppl 1:5s (ERICA)', 'barretto': 'Barretto JR et al. J Pediatr (Rio J). 2024;100 Suppl 1:S31-9',
 'lanhers': 'Lanhers C et al. Sports Med. 2017;47(1):163-73', 'paruthi16': 'Paruthi S et al. J Clin Sleep Med. 2016;12(6):785-6',
 'tsiaras': 'Tsiaras A et al. J Ren Nutr. 2026', 'verduci': 'Verduci E et al. J Pediatr Gastroenterol Nutr. 2025;81(5):1318-45',
})
REF['simpson19'] = "Simpson AJ, Horne S, Sharp P, Sharps R, Kippelen P. Effect of creatine supplementation on the airways of youth elite soccer players. Med Sci Sports Exerc. 2019;51(8):1582-90. doi:10.1249/MSS.0000000000001979"
SHORT['simpson19'] = 'Simpson AJ et al. Med Sci Sports Exerc. 2019;51(8):1582-90'
REF['rdc719'] = "Brasil. Agência Nacional de Vigilância Sanitária. Resolução da Diretoria Colegiada RDC nº 719, de 1º de julho de 2022. Dispõe sobre os requisitos sanitários das misturas para o preparo de alimentos e dos alimentos prontos para o consumo. Diário Oficial da União. 2022 jul 6; Seção 1."
SHORT['rdc719'] = 'Anvisa. RDC nº 719/2022'
