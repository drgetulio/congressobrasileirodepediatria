# Kit Comida Primeiro

Vinte materiais de apoio à aula **“Creatina e Whey Protein: modismo inadequado”**, apresentada no 42º Congresso Brasileiro de Pediatria (Belo Horizonte, outubro de 2026). O kit leva ao consultório o princípio da comida primeiro na orientação do adolescente que pratica esporte: ferramentas para a consulta, fichas de referência para o pediatra, materiais para as famílias e recursos para o ensino.

**Autor:** Getúlio Bernardo Morato Filho, professor da Escola Superior de Ciências da Saúde (ESCS) e do Centro Universitário de Brasília (UniCEUB), supervisor do Programa de Residência Médica do Hospital Materno-Infantil de Brasília (HMIB), Brasília, Distrito Federal, Brasil. Instagram: [@drgetulio](https://www.instagram.com/drgetulio/).

**Versão:** 1.0, revisada em outubro de 2026.

> Orientação geral, que não substitui a avaliação individual.

## O que há no kit

| Nº | Material | Público | Formato |
|---|---|---|---|
| 01 | [Calculadora de proteína](docs/ferramentas/01-calculadora-de-proteina.html) | Ferramenta | Página interativa |
| 02 | [Água no treino](docs/ferramentas/02-agua-no-treino.html) | Ferramenta | Página interativa e [PDF A4](docs/materiais/02-agua-no-treino.pdf) |
| 03 | [Conduta passo a passo](docs/ferramentas/03-conduta-passo-a-passo.html) | Ferramenta | Página interativa e [PDF A4](docs/materiais/03-conduta-passo-a-passo.pdf) |
| 04 | [Verdade ou mito](docs/ferramentas/04-verdade-ou-mito.html) | Ferramenta | Página interativa com 12 afirmações |
| 05 | [Cartão de bolso](docs/materiais/05-cartao-de-bolso.pdf) | Pediatra | PDF A6 |
| 06 | [Roteiro de entrevista e registro](docs/materiais/06-roteiro-de-entrevista-e-registro.pdf) | Pediatra | PDF A4 |
| 07 | [Mapa dos suplementos](docs/materiais/07-mapa-dos-suplementos.pdf) | Pediatra | PDF A4 |
| 08 | [Rótulo, regularização e doping](docs/materiais/08-rotulo-regularizacao-e-doping.pdf) | Pediatra | PDF A4 |
| 09 | [Creatina: o que os pais perguntam](docs/materiais/09-creatina-o-que-os-pais-perguntam.pdf) | Pediatra | PDF A4 |
| 10 | [Deficiência energética relativa no esporte](docs/materiais/10-deficiencia-energetica-reds.pdf) | Pediatra | PDF A4 |
| 11 | [Energéticos, cafeína e pré-treino](docs/materiais/11-energeticos-cafeina-e-pre-treino.pdf) | Pediatra | PDF A4 |
| 12 | [Folheto para os pais](docs/materiais/12-folheto-para-os-pais.pdf) | Famílias | PDF A4, frente e verso |
| 13 | [Folheto para o adolescente](docs/materiais/13-folheto-para-o-adolescente.pdf) | Famílias | PDF A4, frente e verso |
| 14 | [Receituário de comida de verdade](docs/materiais/14-receituario-de-comida-de-verdade.pdf) | Famílias | PDF A5, frente e verso |
| 15 | [Cardápio de lanches pós-treino](docs/materiais/15-cardapio-de-lanches-pos-treino.pdf) | Famílias | PDF A4 |
| 16 | [Pôster para a sala de espera](docs/materiais/16-poster-para-a-sala-de-espera.pdf) | Famílias | PDF A3 |
| 17 | [Carrossel para redes sociais](docs/carrossel/index.html) | Famílias | 5 imagens PNG, legenda e versão editável |
| 18 | [Carta ao treinador e à escola](docs/materiais/18-carta-ao-treinador-e-a-escola.pdf) | Equipe | PDF A4 e [Word](docs/materiais/18-carta-ao-treinador-e-a-escola.docx) |
| 19 | [Casos clínicos para discussão](docs/materiais/19-casos-clinicos-para-discussao.pdf) | Ensino | PDF A4 |
| 20 | [Bibliografia comentada](docs/materiais/20-bibliografia-comentada.pdf) | Ensino | PDF A4, com a lista completa de referências |

## Como usar

**Pelo navegador, sem instalar nada.** A pasta `docs/` contém o kit completo como site estático. Abra `docs/index.html` em qualquer navegador; as quatro ferramentas funcionam sem internet.

**Como página pública no GitHub Pages.** No repositório, abra *Settings*, depois *Pages*, escolha *Deploy from a branch*, a branch `main` e a pasta `/docs`. O endereço do site aparece na mesma tela após a primeira publicação.

**Antes de publicar o carrossel (item 17).** Preencha nome, CRM e RQE no último cartão pela versão editável (`docs/carrossel/17-carrossel-editavel.html`). A Resolução CFM nº 2.336/2023 exige essa identificação na publicidade médica e também na página principal do perfil.

## Como reconstruir os materiais

Os PDFs, as ferramentas, o carrossel e a página do kit são gerados a partir dos arquivos da pasta `fonte/`. Para alterar um texto ou um número, edite a fonte e reconstrua.

Requisitos: Python 3.10 ou mais recente, Node.js 18 ou mais recente e poppler-utils (`pdftoppm` e `pdfinfo`).

```bash
npm ci                                   # fontes tipográficas Source Serif 4, IBM Plex Sans e IBM Plex Mono
pip install -r requirements.txt
python -m playwright install chromium    # navegador usado para gerar PDFs e imagens
./construir.sh                           # reconstrói tudo e atualiza docs/
```

O script verifica se algum conteúdo transborda a página e informa o resultado item a item. O pacote para uso offline fica em `fonte/out/Kit-Comida-Primeiro.zip`.

### Onde está cada coisa

```
fonte/
  src/              textos dos materiais impressos, um arquivo HTML por item
  base.css          identidade visual dos impressos (tipografia, cores por público, tamanhos A3 a A6)
  build.py          gera os PDFs, numera as citações e monta as listas de fontes
  refs.py           referências do kit em estilo Vancouver, com as formas curtas
  refs_aula.py      referências herdadas da aula
  tbca.py           valores de proteína e energia por medida caseira (TBCA 7.3) e combinações de lanches
  gen_src.py        gera os itens 14 e 15 a partir de tbca.py
  gen_docx.py       gera a carta ao treinador em Word
  web.py            gera as ferramentas interativas 01 a 04
  carrossel/        gera os cartões, a legenda e a versão editável do item 17
  hub.py            gera a página do kit, as miniaturas e o pacote offline
  shot.py, preview.py  capturas de tela e folhas de conferência visual das páginas
docs/               site publicado (resultado da construção)
```

Nos textos de `fonte/src/`, `[[ref:chave]]` insere a chamada numerada da referência, `[[sources]]` insere a lista de fontes do item e `[[cite:chave]]` insere a referência completa. As chaves estão em `refs.py`.

## Fontes e verificação

Cada número do kit remete a uma fonte citada no próprio material. As referências foram conferidas nas publicações originais em outubro de 2026, e a lista completa, em ordem alfabética, está no item 20, que também justifica as dez referências com mais de dez anos.

Normas brasileiras conferidas em outubro de 2026:
- Agência Nacional de Vigilância Sanitária (Anvisa): RDC nº 243/2018, Instrução Normativa nº 28/2018, Instrução Normativa nº 373/2025, RDC nº 843/2024 e RDC nº 719/2022.
- Conselho Federal de Medicina (CFM): Código de Ética Médica (Resolução CFM nº 2.217/2018) e Resolução CFM nº 2.336/2023.

Os valores de alimentos vêm da Tabela Brasileira de Composição de Alimentos (TBCA), versão 7.3, Universidade de São Paulo, com os códigos de cada alimento registrados em `fonte/tbca.py` e no item 15. Os totais são arredondados com meio para cima, na primeira casa decimal.

## Como citar

Morato Filho GB. Kit Comida Primeiro: materiais de apoio da aula “Creatina e Whey Protein: modismo inadequado”. 42º Congresso Brasileiro de Pediatria; 2026 out; Belo Horizonte. Brasília: Escola Superior de Ciências da Saúde; 2026. Versão 1.0.

Os metadados de citação estão em [`CITATION.cff`](CITATION.cff).

## Termos de uso

Uso educacional livre, com citação da fonte. Detalhes em [`LICENCA.md`](LICENCA.md).
