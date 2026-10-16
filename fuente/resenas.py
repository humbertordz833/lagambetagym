# Reseñas reales (Google y TikTok), texto tal cual las escribieron.
# Para agregar una: sumala a REVIEWS y corré:  python3 fuente/resenas.py && python3 fuente/construir.py
REVIEWS=[
 ("@fer_eriii","FE","https://www.tiktok.com/@fer_eriii","Review en video · TikTok",
  "Un gimnasio que parece Estados Unidos estando en Presidente Franco."),
 ("Verónica Chávez","VC",None,"4 opiniones · Hace 5 meses",
  "Excelente atención, especialmente del instructor de piso. Ambiente ideal para entrenar, buena música. Buenísimas máquinas."),
 ("Jared Loucks","JL","https://www.google.com/maps/contrib/111355369501496619096/reviews?hl=es-419","Local Guide · 103 opiniones · Hace un año",
  "De todos los gimnasios a los que he ido en Paraguay, este es el que tiene más espacio y el equipo más limpio. ¡Además, el personal es muy amable, lo cual es un plus!"),
 ("Mario Varela","MV","https://www.google.com/maps/contrib/118235385375068926434/reviews?hl=es-419","Local Guide · 195 opiniones · Hace un año",
  "Que lugar señores espectacular una locura pregunten por el profe pichi varela el mejor 👏🏼"),
 ("Celso Vargas Viana","CV","https://www.google.com/maps/contrib/112795244041428118048/reviews?hl=es-419","Local Guide · 67 opiniones · Hace un año",
  "Si busca un buen lugar para realizar actividades físicas es la mejor opción en Pdte. Franco con profesionales de excelencia para acompañarte en las metas que tienes en subir de peso o adelgazar te invito a visitar!!!"),
 ("Alejandra","A","https://www.google.com/maps/contrib/117386878606092218717/reviews?hl=es-419","Local Guide · 10 opiniones · Hace 2 años",
  "Este lugar consta de un buen servicio al cliente que vaya allí, es un lugar bastante agradable en mi opinión.."),
 ("Geber Escobar Da Silva","GE","https://www.google.com/maps/contrib/100314023641661846927/reviews?hl=es-419","Local Guide · 8 opiniones · Hace 3 años",
  "Excelente servicio y atención a los clientes, de verdad lo mejor de lo mejor."),
 ("Osmar Moreira","OM","https://www.google.com/maps/contrib/101579361604645130054/reviews?hl=es-419","Local Guide · 6 opiniones · Hace 4 años",
  "Excelente 👌"),
 ("Rony Melgarejo","RM","https://www.google.com/maps/contrib/118318559880940795131/reviews?hl=es-419","Local Guide · 20 opiniones · Hace 4 años",
  "Espectacular"),
 ("Karina Cabañas","KC","https://www.google.com/maps/contrib/107409532578664380337/reviews?hl=es-419","1 opinión · Hace un año",
  None, 5),
]
import html
def card(n,ini,url,meta,text,stars=None):
    name=f'<a href="{url}" target="_blank" rel="noopener">{html.escape(n)}</a>' if url else html.escape(n)
    if text:
        body=f'<blockquote>{html.escape(text)}</blockquote>'
    else:
        body=(f'<div class="only-stars"><span class="stars" style="--r:{stars}" aria-label="{stars} de 5 estrellas"><i></i><i></i></span>'
              f'<span>Calificó con {stars} estrellas</span></div>')
    cls=' stars-only' if not text else ''
    return f'''        <figure class="review{cls}" data-tilt data-max="6">
          {body}
          <figcaption>
            <span class="avatar" aria-hidden="true"><span>{ini}</span></span>
            <span class="who"><b>{name}</b><span>{meta}</span></span>
          </figcaption>
        </figure>
'''
import os
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'plantilla.html')
s=open(p).read()
a=s.index('        <div class="review-list">'); b=s.index('        </div>\n      </div>\n',a)
s=s[:a]+'        <div class="review-list">\n'+''.join(card(*r) for r in REVIEWS)+s[b:]
css='.review.stars-only::before{content:none}\n.only-stars{display:flex;flex-direction:column;gap:10px}\n.only-stars .stars{width:138px;height:24px}\n.only-stars .stars i{background-size:27.6px 24px}\n.only-stars>span:last-child{color:var(--mute);font-family:var(--f-label);font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:.85rem}\n'
if '.review.stars-only' not in s:
    s=s.replace('/* Contacto */',css+'\n/* Contacto */',1)
old='.review-list{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:20px;perspective:1300px}'
if old in s:
    s=s.replace(old,'.review-list{columns:3 280px;column-gap:20px}\n.review-list .review{break-inside:avoid;margin-bottom:20px}')
open(p,'w').write(s)
print(s.count('class="review"'),'reseñas')
