# Equipo de La Gambeta Gym. name=None → "Nombre a confirmar"; photo=None → silueta.
# Cuando el dueño apruebe: completar name y photo (nombre del archivo en fuente/fotos/local sin .jpg)
# y correr:  python3 fuente/equipo.py && python3 fuente/construir.py
TEAM=[
 dict(area='atencion',     role='Encargado/a',               name=None, photo=None, color='#a855f7',
      text='Coordina el día a día del gym y está para resolver cualquier consulta.', tags=['Coordinación']),
 dict(area='atencion',     role='Recepción',                 name=None, photo=None, color='#a855f7',
      text='Te recibe, gestiona tu inscripción y tus pagos, y te informa de planes y horarios.', tags=['Inscripciones','Pagos']),
 dict(area='instructores', role='Instructor/a de sala',      name=None, photo=None, color='#3ee68a',
      text='Te guía en las máquinas, corrige tu técnica y te ayuda a armar tu rutina.', tags=['Musculación']),
 dict(area='instructores', role='Instructor/a de funcional', name=None, photo=None, color='#3ee68a',
      text='Dirige los entrenamientos funcionales en grupo.', tags=['Funcional']),
 dict(area='instructores', role='Instructor/a de GAP y spinning', name=None, photo=None, color='#3ee68a',
      text='Lleva las clases de GAP y spinning con música y ritmo.', tags=['GAP','Spinning']),
 dict(area='servicios',    role='Mantenimiento',             name=None, photo=None, color='#5b8cff',
      text='Cuida que cada máquina esté en condiciones y funcionando bien.', tags=['Equipos']),
 dict(area='servicios',    role='Limpieza',                  name=None, photo=None, color='#5b8cff',
      text='Mantiene la sala, los sanitarios y los equipos limpios para que entrenes cómodo.', tags=['Higiene']),
 dict(area='servicios',    role='Cafetería',                 name=None, photo=None, color='#ffc83d',
      text='Prepara tapiocas, jugos naturales y comidas fit en La Gambeta Café.', tags=['La Gambeta Café']),
]
import html
SIL='<svg class="sil" viewBox="0 0 120 150" aria-hidden="true"><circle cx="60" cy="52" r="26" fill="currentColor"/><path d="M14 150c0-30 20-52 46-52s46 22 46 52z" fill="currentColor"/></svg>'
def card(m):
    pend=m['name'] is None
    name='Nombre a confirmar' if pend else html.escape(m['name'])
    photo=(f'<img data-img="{m["photo"]}" alt="{name}">' if m['photo'] else SIL)
    chip='<span class="pending">Foto y nombre por confirmar</span>' if pend or not m['photo'] else ''
    tags=''.join(f'<span>{html.escape(t)}</span>' for t in m['tags'])
    return f'''        <article class="member{' is-pending' if pend else ''}" data-area="{m['area']}" data-tilt data-max="7" style="--c:{m['color']}">
          <div class="m-photo">{photo}{chip}</div>
          <div class="m-body">
            <span class="m-role">{html.escape(m['role'])}</span>
            <h3 class="m-name">{name}</h3>
            <p>{html.escape(m['text'])}</p>
            <div class="m-tags">{tags}</div>
          </div>
        </article>
'''
import os
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'plantilla.html')
s=open(p).read()
body=''.join(card(m) for m in TEAM)
if '<section id="equipo">' in s:
    a=s.index('      <div class="team-grid" id="teamGrid">\n')+len('      <div class="team-grid" id="teamGrid">\n'); b=s.index('      </div>\n    </div>\n  </section>',a)
    s=s[:a]+body+s[b:]
else:
    sec=f'''  <section id="equipo">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <p class="eyebrow">Nuestro equipo</p>
          <h2>Las personas<br>detrás del gym</h2>
          <p class="lead">Desde que entrás hasta que terminás tu rutina, hay un equipo atento a que entrenes cómodo y seguro.</p>
        </div>
        <div class="team-filter" role="tablist" aria-label="Filtrar equipo por área">
          <button type="button" role="tab" aria-selected="true" data-f="all">Todos</button>
          <button type="button" role="tab" aria-selected="false" data-f="instructores">Instructores</button>
          <button type="button" role="tab" aria-selected="false" data-f="atencion">Atención</button>
          <button type="button" role="tab" aria-selected="false" data-f="servicios">Servicios</button>
        </div>
      </div>
      <div class="team-grid" id="teamGrid">
{body}      </div>
    </div>
  </section>

'''
    i=s.index('  <section id="cafe">'); s=s[:i]+sec+s[i:]
    css='''/* Nuestro equipo */
#equipo{border-top:1px solid var(--line)}
.team-filter{display:flex;flex-wrap:wrap;gap:8px}
.team-filter button{font-family:var(--f-label);font-weight:700;text-transform:uppercase;letter-spacing:.1em;font-size:.92rem;background:transparent;color:var(--mute);border:1px solid var(--line);border-radius:999px;padding:9px 18px;cursor:pointer;transition:background .25s,color .25s,border-color .25s}
.team-filter button:hover{border-color:var(--violet);color:var(--chalk)}
.team-filter button[aria-selected="true"]{background:var(--chalk);color:var(--ink);border-color:var(--chalk)}
.team-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,250px),1fr));gap:20px;perspective:1300px}
.member{position:relative;display:flex;flex-direction:column;border-radius:18px;overflow:hidden;border:1px solid var(--line);background:linear-gradient(170deg,var(--panel),var(--ink))}
.member:not([hidden]){animation:pop-in .55s var(--ease) both}
@keyframes pop-in{from{transform:perspective(900px) rotateX(-12deg) translateY(18px) scale(.97)}to{transform:none}}
.m-photo{position:relative;aspect-ratio:4/4.2;overflow:hidden;display:grid;place-items:end center;background:radial-gradient(90% 70% at 50% 100%,color-mix(in srgb,var(--c) 30%,transparent),transparent 70%),linear-gradient(180deg,#14121c,#0c0b12)}
.m-photo::after{content:"";position:absolute;inset:auto 0 0;height:3px;background:linear-gradient(90deg,transparent,var(--c),transparent);opacity:.8}
.m-photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .6s var(--ease)}
.member:hover .m-photo img{transform:scale(1.05)}
.m-photo .sil{width:62%;height:auto;color:color-mix(in srgb,var(--c) 22%,#2a2638);transform:translateY(6%);transition:transform .6s var(--ease)}
.member:hover .m-photo .sil{transform:translateY(2%) scale(1.03)}
.pending{position:absolute;top:12px;left:12px;font-family:var(--f-label);font-weight:700;letter-spacing:.1em;text-transform:uppercase;font-size:.7rem;padding:5px 9px;border-radius:6px;color:var(--mute);background:color-mix(in srgb,var(--ink) 70%,transparent);border:1px dashed color-mix(in srgb,var(--c) 50%,var(--line))}
.m-body{display:flex;flex-direction:column;gap:6px;padding:18px 20px 22px}
.m-role{font-family:var(--f-label);font-weight:700;text-transform:uppercase;letter-spacing:.14em;font-size:.8rem;color:var(--c)}
.m-name{font-family:var(--f-display);font-weight:800;font-size:1.7rem;line-height:1;text-transform:uppercase;transform:translateZ(22px)}
.is-pending .m-name{color:var(--mute);font-weight:700}
.m-body p{margin:.2rem 0 0;color:var(--mute);font-size:.95rem}
.m-tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.m-tags span{font-family:var(--f-label);font-weight:600;letter-spacing:.06em;font-size:.78rem;text-transform:uppercase;padding:4px 9px;border-radius:999px;border:1px solid color-mix(in srgb,var(--c) 40%,var(--line));color:var(--chalk)}

/* Cafetería: horario, carrusel 3D y fotos en el menú */'''
    assert s.count('/* Cafetería: horario, carrusel 3D y fotos en el menú */')==1
    s=s.replace('/* Cafetería: horario, carrusel 3D y fotos en el menú */',css)
    js='''  /* ---------- Filtro del equipo ---------- */
  var tf=document.querySelectorAll('.team-filter button');
  tf.forEach(function(btn){btn.addEventListener('click',function(){
    tf.forEach(function(x){x.setAttribute('aria-selected',x===btn?'true':'false')});
    var f=btn.dataset.f;
    document.querySelectorAll('#teamGrid .member').forEach(function(m){m.hidden=!(f==='all'||m.dataset.area===f)});
    if(typeof measureRise==='function') setTimeout(measureRise,50);
  })});

  /* ---------- Inclinación 3D en tarjetas ---------- */'''
    assert s.count('  /* ---------- Inclinación 3D en tarjetas ---------- */')==1
    s=s.replace('  /* ---------- Inclinación 3D en tarjetas ---------- */',js)
    assert s.count('<a href="#cafe">Cafetería</a>')==1
    s=s.replace('<a href="#cafe">Cafetería</a>','<a href="#equipo">Equipo</a>\n      <a href="#cafe">Cafetería</a>')
    s=s.replace("addRise('.more-reviews');","addRise('.more-reviews');addRise('.member',.04);addRise('.team-filter');")
open(p,'w').write(s); print('equipo ok:',len(TEAM),'puestos')
