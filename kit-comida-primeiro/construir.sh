#!/usr/bin/env bash
# Reconstrói todos os materiais do kit e atualiza a pasta docs/ (site publicado).
# Requisitos: Python 3.10 ou mais recente, Node.js (para as fontes tipográficas) e poppler-utils (pdftoppm, pdfinfo).
set -euo pipefail
cd "$(dirname "$0")"
[ -d node_modules ] || npm ci
cd fonte
python3 gen_src.py          # itens 14 e 15, calculados a partir da TBCA
python3 build.py            # PDFs dos itens 02, 03, 05 a 16 e 18 a 20
python3 gen_docx.py         # carta ao treinador em Word
python3 web.py              # ferramentas interativas 01 a 04
python3 carrossel/carrossel.py
python3 hub.py              # página do kit, miniaturas e pacote offline
cd ..
rm -rf docs && mkdir docs
cp -r fonte/zip/Kit-Comida-Primeiro/. docs/
touch docs/.nojekyll
echo "Pronto: docs/ atualizada e pacote em fonte/out/Kit-Comida-Primeiro.zip"
