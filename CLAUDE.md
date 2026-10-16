# La Gambeta Gym — página web

Proyecto del Lic. Humberto Rodríguez: página web para La Gambeta Gym (Presidente Franco, Paraguay),
presentada al dueño como propuesta comercial. Respondé siempre en español rioplatense/paraguayo (voseo).

## Dónde está todo
- Página publicada: https://lagambetagym.netlify.app (Netlify, proyecto "lagambetagym").
- Netlify publica automáticamente cada push a la rama `main` de este repositorio, solo la carpeta `public/`.
- `fuente/plantilla.html` es la página editable: HTML + CSS + JS en un solo archivo. Las fotos se cargan
  por nombre (`data-img="hero"`, `IMG['hero']`).
- `fuente/fotos/local/` y `fuente/fotos/cafeteria/` son las fotos que usa la página (ya recortadas).
- `fuente/originales/` son fotos originales en mejor calidad, por si hay que recortar de nuevo.
- `fuente/construir.py` arma `public/index.html` (fotos incrustadas en WebP, un solo archivo).
- `fuente/equipo.py` regenera la sección del equipo y `fuente/resenas.py` la de opiniones, a partir de sus listas de datos.
- `propuesta/propuesta.html` + `propuesta/capturas/` generan la propuesta en PDF (A4, 7 páginas).
- `entregables/` contiene la propuesta en PDF y el video instructivo con voz y subtítulos (.mp4 y .srt).

## Cómo hacer un cambio
1. Editar `fuente/plantilla.html` (o los datos en `fuente/equipo.py` / `fuente/resenas.py` y correrlos).
2. `python3 fuente/construir.py`
3. Revisar la página en computadora y en celular (320, 400 y 1440 px de ancho): sin scroll horizontal, sin errores, todas las fotos cargan.
4. Commit y push a `main`. En ~1 minuto Netlify publica el cambio.

## Datos del gym (confirmados)
- WhatsApp 0993 429 849 (wa.me/595993429849) · Instagram @lagambetagym · tienda @lagambetastore
- Dirección: Pdte. Franco 100219, Paraguay · Google Maps: https://www.google.com/maps?cid=15297809469216503233
- Google: 4,8 estrellas, 108 opiniones.
- Horario: lunes a viernes 05:00–23:00, sábados 09:00–18:00, domingos cerrado.
- Cafetería: 06:00–09:00 y 15:00–21:30.
- Planes de musculación: diario Gs. 40.000, semanal 100.000, quincenal 150.000, mensual 200.000,
  trimestral 500.000, semestral 900.000, anual 1.700.000. Funcional mensual 150.000; funcional + musculación 200.000.
  Tarifa preferencial para universitarios, colegiales y horario especial (consultar).
- Clases: GAP (glúteos, abdomen, piernas), spinning, funcional.
- Sala de Poses: espejo de cuerpo entero, focos, cuadros de Arnold Schwarzenegger, Ronnie Coleman y Chris Bumstead.

## Pendiente de confirmar con el dueño
- Nombres y fotos del equipo (las tarjetas dicen "Nombre a confirmar"). Las reseñas mencionan al "profe Pichi Varela".
- Precios del sándwich proteico, la hamburguesa fit y el waffle (hoy dicen "Consultar").
- Días y horarios de GAP, spinning y funcional, y si spinning tiene precio aparte.
- Si la cafetería abre los sábados. Estacionamiento, formas de pago y clase de prueba (para preguntas frecuentes).

## Decisiones ya tomadas
- Estilo: negro con violeta y verde neón, logo LG con anillo de colores, animaciones 3D fluidas.
- Se quitó el recorrido virtual hasta tener fotos 360° reales; está ofrecido como opcional (Gs. 800.000) en la propuesta.
- Se quitó la sección "Todo lo que vas a encontrar" (fotos del video de @fer_eriii); se mantiene su reseña en Opiniones.
- La transición entre portada y la sección siguiente debe ser discreta (franja fina), no cintas grandes.
- Precio propuesto: Gs. 3.500.000 pago único (50% al aprobar, 50% al publicar). Opcionales: dominio ~Gs. 100.000/año,
  mantenimiento Gs. 250.000/mes, recorrido 360° Gs. 800.000, sección tienda Gs. 600.000, grilla de clases Gs. 300.000.
