"""Arma la página publicada (public/index.html) a partir de fuente/plantilla.html y las fotos.

Uso, desde la raíz del repositorio:
    python3 fuente/construir.py

Las fotos de fuente/fotos/local y fuente/fotos/cafeteria se convierten a WebP y se
incrustan en el HTML, así la página es un solo archivo. En la plantilla, cada foto se
usa por su nombre de archivo sin extensión (por ejemplo IMG['hero'] o data-img="hero").
Requiere Python 3 con Pillow (pip install pillow).
"""
import base64, io, json, os
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = lambda *p: os.path.join(RAIZ, *p)

plantilla = open(F('fuente', 'plantilla.html'), encoding='utf-8').read()
imgs, dims = {}, {}
for carpeta in ['local', 'cafeteria']:
    d = F('fuente', 'fotos', carpeta)
    for f in sorted(os.listdir(d)):
        if not f.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        k = os.path.splitext(f)[0]
        assert k not in imgs, f'Nombre de foto repetido: {k}'
        im = Image.open(os.path.join(d, f)); dims[k] = list(im.size)
        if f.lower().endswith('.png'):
            data, mime = open(os.path.join(d, f), 'rb').read(), 'image/png'
        else:
            b = io.BytesIO(); im.convert('RGB').save(b, 'WEBP', quality=72, method=6); data, mime = b.getvalue(), 'image/webp'
        imgs[k] = f'data:{mime};base64,' + base64.b64encode(data).decode()

cuerpo = plantilla.replace('<!--IMG-->', '<script>window.GYM_IMG=' + json.dumps(imgs) + ';window.GYM_DIM=' + json.dumps(dims) + ';</script>')
assert '<!--IMG-->' not in cuerpo

def png_uri(path, size):
    im = Image.open(path).convert('RGBA').resize((size, size), Image.LANCZOS); b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()

logo = F('fuente', 'fotos', 'local', 'logo.png')
URL = 'https://lagambetagym.netlify.app/'
desc = 'La Gambeta Gym en Presidente Franco: musculación, GAP, spinning y funcional. Horarios, planes, cafetería, opiniones y contacto.'
head = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f'<meta name="description" content="{desc}">\n<meta name="theme-color" content="#08070c">\n'
        f'<link rel="icon" type="image/png" href="{png_uri(logo, 64)}">\n'
        f'<link rel="apple-touch-icon" href="{png_uri(logo, 180)}">\n'
        '<meta property="og:type" content="website">\n<meta property="og:site_name" content="La Gambeta Gym">\n'
        '<meta property="og:title" content="La Gambeta Gym · Presidente Franco">\n'
        f'<meta property="og:description" content="{desc}">\n'
        f'<link rel="canonical" href="{URL}">\n<meta property="og:url" content="{URL}">\n'
        f'<meta property="og:image" content="{URL}og-image.jpg">\n'
        '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
        '<meta property="og:locale" content="es_PY">\n<meta name="twitter:card" content="summary_large_image">\n')
i = cuerpo.index('</style>') + len('</style>')
salida = head + cuerpo[:i] + '\n</head>\n<body style="margin:0">\n' + cuerpo[i:] + '\n</body>\n</html>\n'
os.makedirs(F('public'), exist_ok=True)
open(F('public', 'index.html'), 'w', encoding='utf-8').write(salida)
print(f'{len(imgs)} fotos · public/index.html {os.path.getsize(F("public", "index.html")) / 1e6:.2f} MB')
