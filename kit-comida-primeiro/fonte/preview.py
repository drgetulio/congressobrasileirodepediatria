import os as _os
KIT = _os.path.dirname(_os.path.abspath(__file__))
import sys, glob, os, subprocess
from PIL import Image
# uso: python3 preview.py saida.png 06 07 ...  (gera folha com todas as páginas dos PDFs)
out = sys.argv[1]; pre = sys.argv[2:]
pdfs = sorted(f for f in glob.glob(KIT + '/out/pdf/*.pdf') if any(os.path.basename(f).startswith(p) for p in pre))
ims = []
tmp = KIT + '/out/tmpprev'; os.makedirs(tmp, exist_ok=True)
for f in pdfs:
    base = os.path.join(tmp, os.path.basename(f)[:-4])
    for g in glob.glob(base + '-*.png'): os.remove(g)
    subprocess.run(['pdftoppm', '-png', '-r', '55', f, base], check=True)
    ims += [Image.open(g) for g in sorted(glob.glob(base + '-*.png'))]
cols = int(sys.argv[0] and 4)
h = max(i.height for i in ims); w = max(i.width for i in ims)
cols = min(cols, len(ims)); rows = (len(ims) + cols - 1) // cols
sheet = Image.new('RGB', (cols * (w + 10), rows * (h + 10)), '#777')
for k, im in enumerate(ims):
    sheet.paste(im, ((k % cols) * (w + 10), (k // cols) * (h + 10)))
sheet.save(out)
print(out, len(ims), 'páginas')
