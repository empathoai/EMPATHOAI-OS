from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Image, HRFlowable
)
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dermam_academy_ghl_vs_hotmart_a4_report.pdf'
LOGO = ROOT.parent / 'references' / 'brand-assets' / '01_LOGO' / 'MASTER' / 'empathoai-master-logo-light-trans.png'

ORANGE = HexColor('#FF4402')
INK = HexColor('#0A0A0B')
MUTED = HexColor('#555558')
LIGHT = HexColor('#F8F8FA')
PALE = HexColor('#FFF8F5')
LINE = HexColor('#E5E5EA')
GREEN = HexColor('#157347')
AMBER = HexColor('#9A6700')
RED = HexColor('#B42318')
BLUE = HexColor('#205EA8')

# Prefer the repository's brand fonts when present; fall back safely.
font_dir = ROOT.parent / 'references' / 'brand-assets'
font_candidates = list(font_dir.rglob('IBMPlexSans-Regular.ttf')) + list(font_dir.rglob('IBM-Plex-Sans-Regular.ttf'))
if font_candidates:
    pdfmetrics.registerFont(TTFont('IBMPlexSans', str(font_candidates[0])))
    FONT = 'IBMPlexSans'
else:
    FONT = 'Helvetica'

styles = getSampleStyleSheet()
styles.add(ParagraphStyle('CoverEyebrow', fontName='Helvetica-Bold', fontSize=9, leading=11, textColor=ORANGE, tracking=1.3, spaceAfter=10))
styles.add(ParagraphStyle('CoverTitle', fontName='Helvetica-Bold', fontSize=27, leading=30, textColor=INK, spaceAfter=10))
styles.add(ParagraphStyle('CoverSub', fontName='Helvetica', fontSize=11.5, leading=16, textColor=MUTED, spaceAfter=16))
styles.add(ParagraphStyle('H1x', fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=INK, spaceBefore=5, spaceAfter=8, keepWithNext=True))
styles.add(ParagraphStyle('H2x', fontName='Helvetica-Bold', fontSize=11.5, leading=14, textColor=ORANGE, spaceBefore=10, spaceAfter=4, keepWithNext=True))
styles.add(ParagraphStyle('Bodyx', fontName='Helvetica', fontSize=9.2, leading=13.1, textColor=INK, spaceAfter=7))
styles.add(ParagraphStyle('Smallx', fontName='Helvetica', fontSize=7.6, leading=10, textColor=MUTED, spaceAfter=4))
styles.add(ParagraphStyle('Calloutx', fontName='Helvetica-Bold', fontSize=10.2, leading=14, textColor=INK, leftIndent=0, spaceAfter=0))
styles.add(ParagraphStyle('TableHead', fontName='Helvetica-Bold', fontSize=7.5, leading=9, textColor=colors.white))
styles.add(ParagraphStyle('TableCell', fontName='Helvetica', fontSize=7.6, leading=9.4, textColor=INK))
styles.add(ParagraphStyle('TableCellBold', fontName='Helvetica-Bold', fontSize=7.6, leading=9.4, textColor=INK))
styles.add(ParagraphStyle('Source', fontName='Helvetica', fontSize=7.2, leading=9.2, textColor=INK, spaceAfter=4))
styles.add(ParagraphStyle('TOC', fontName='Helvetica', fontSize=9, leading=13, textColor=INK, leftIndent=10, spaceAfter=3))


def P(text, style='Bodyx'):
    return Paragraph(text, styles[style])

def bullet(text):
    return Paragraph(f'• {text}', styles['Bodyx'])

def callout(text, label='DECISIÓN'):
    t = Table([[P(f'<b>{label}</b><br/>{text}', 'Calloutx')]], colWidths=[174*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),PALE), ('BOX',(0,0),(-1,-1),0.6,LINE),
        ('LINEBEFORE',(0,0),(0,-1),4,ORANGE), ('LEFTPADDING',(0,0),(-1,-1),11),
        ('RIGHTPADDING',(0,0),(-1,-1),11), ('TOPPADDING',(0,0),(-1,-1),9),
        ('BOTTOMPADDING',(0,0),(-1,-1),9),
    ]))
    return t

def table(data, widths, header=True, font_size=None):
    wrapped=[]
    for r, row in enumerate(data):
        out=[]
        for cell in row:
            if isinstance(cell, Paragraph): out.append(cell)
            else: out.append(P(str(cell), 'TableHead' if header and r==0 else 'TableCell'))
        wrapped.append(out)
    t=Table(wrapped, colWidths=widths, repeatRows=1 if header else 0, hAlign='LEFT')
    commands=[('GRID',(0,0),(-1,-1),0.35,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]
    if header: commands += [('BACKGROUND',(0,0),(-1,0),INK),('TEXTCOLOR',(0,0),(-1,0),colors.white)]
    for r in range(1 if header else 0,len(data)):
        if r%2==0: commands.append(('BACKGROUND',(0,r),(-1,r),LIGHT))
    t.setStyle(TableStyle(commands)); return t

def link(label, url):
    return f'<link href="{url}" color="{BLUE}"><u>{escape(label)}</u></link>'

sources = [
    ('HighLevel Pricing', 'https://www.gohighlevel.com/pricing', 'Consultada 2026-09-10. Pricing, Starter, subcuentas y funciones.'),
    ('HighLevel Square Payment Processor', 'https://help.gohighlevel.com/support/solutions/articles/155000003314-how-to-connect-and-use-square-payment-processor-in-highlevel', 'Consultada 2026-09-10. Conexión y usos documentados de Square.'),
    ('HighLevel Payment Providers by Product Area', 'https://help.gohighlevel.com/support/solutions/articles/155000006075-supported-payment-providers-methods-by-product-area-what-works-where-', 'Consultada 2026-09-10. Matriz de compatibilidad por área.'),
    ('HighLevel Launch a Course', 'https://help.gohighlevel.com/support/solutions/articles/155000005072-getting-started-launch-a-course', 'Consultada 2026-09-10. Creación y lanzamiento de cursos.'),
    ('HighLevel Assessments / Quizzes', 'https://help.gohighlevel.com/support/solutions/articles/48001224429-how-to-create-assessments-quizzes-for-membership-courses', 'Consultada 2026-09-10. Evaluaciones, passing grade, intentos y resultados.'),
    ('HighLevel Facebook Conversion API', 'https://help.gohighlevel.com/support/solutions/articles/48001236281-how-to-set-up-a-funnel-event-pixel-for-facebook-conversion-api-', 'Consultada 2026-09-10. Pixel y CAPI para funnels.'),
    ('HighLevel AI Product Pricing', 'https://help.gohighlevel.com/support/solutions/articles/155000006652-ai-product-pricing', 'Consultada 2026-09-10. Precios y modalidades de AI. Puede cambiar.'),
    ('Hotmart Pricing', 'https://hotmart.com/en/pricing', 'Consultada 2026-09-10. Sin mensualidad base según la página consultada.'),
    ('Hotmart Payment Methods', 'https://help.hotmart.com/en/article/25648853025037/what-payment-methods-are-available-for-purchasing-on-hotmart-', 'Consultada 2026-09-10. Métodos publicados. Square no apareció en la fuente revisada.'),
    ('Hotmart Club Members Area', 'https://help.hotmart.com/en/article/20060658355085/hotmart-club-everything-you-need-to-know-about-hotmart-s-members-area', 'Consultada 2026-09-10. Área de miembros, cursos, comunidades y progreso.'),
    ('Hotmart Webhooks', 'https://developers.hotmart.com/docs/en/1.0.0/webhook/using-webhook/', 'Consultada 2026-09-10. Eventos de compra, reembolso y recurrencia.'),
    ('Hotmart Fees', 'https://help.hotmart.com/en/article/208298448/what-are-the-fees-charged-by-hotmart-', 'Consultada 2026-09-10. Fórmula de tarifas consultada; confirmar caso final.'),
    ('Hotmart Facebook features', 'https://help.hotmart.com/en/article/43410346545165/how-to-integrate-facebook-features-into-my-hotmart-pages-', 'Consultada 2026-09-10. Pixel, CAPI y páginas de Hotmart.'),
]

class NumberedDocTemplate(SimpleDocTemplate):
    pass

def page_header_footer(canvas, doc):
    canvas.saveState()
    w,h=A4
    if doc.page > 1:
        canvas.setStrokeColor(ORANGE); canvas.setLineWidth(1.2); canvas.line(15*mm,h-18*mm,195*mm,h-18*mm)
        canvas.setFillColor(MUTED); canvas.setFont('Helvetica-Bold',7.5); canvas.drawString(15*mm,h-14*mm,'EMPATHOAI  /  STRATEGIC GROWTH & REVENUE INFRASTRUCTURE')
        canvas.setFillColor(ORANGE); canvas.drawRightString(195*mm,h-14*mm,'DERMA.M ACADEMY')
    canvas.setStrokeColor(LINE); canvas.setLineWidth(.6); canvas.line(15*mm,13*mm,195*mm,13*mm)
    canvas.setFillColor(MUTED); canvas.setFont('Helvetica',7.2); canvas.drawString(15*mm,8.5*mm,'Documento confidencial · Preparado por EmpathoAI · Consulta de fuentes: 10 septiembre 2026')
    canvas.drawRightString(195*mm,8.5*mm,str(doc.page))
    canvas.restoreState()

story=[]
# Cover
if LOGO.exists():
    logo=Image(str(LOGO), width=42*mm, height=10*mm)
    story.append(logo)
story += [Spacer(1,18*mm), P('ANÁLISIS COMPARATIVO · ESTADOS UNIDOS','CoverEyebrow'), P('GHL vs Hotmart<br/>para cursos online','CoverTitle'), P('Viabilidad técnica, economía, funnels, cursos, membresías y oportunidades de diferenciación para una academia online con Square como pasarela obligatoria.','CoverSub'), Spacer(1,8*mm), callout('Para Derma.M, la recomendación operativa es reemplazar WordPress con una nueva academia en GHL, alojada en la cuenta o subcuenta propiedad de Derma.M y conectada a su Square. Hotmart queda como alternativa si se acepta utilizar su checkout y sistema de pagos.', 'CONCLUSIÓN EJECUTIVA'), Spacer(1,22*mm), P('<b>Cliente:</b> Derma.M Academy · West Palm Beach, Florida<br/><b>Documento:</b> Informe de decisión de plataforma<br/><b>Fecha:</b> 10 de septiembre de 2026<br/><b>Preparado por:</b> EmpathoAI Strategic Growth & Revenue Infrastructure','Smallx'), PageBreak()]

# Executive summary
story += [P('1. Resumen ejecutivo','H1x'), P('Hotmart y GHL no son equivalentes. Hotmart está optimizado para vender y entregar infoproductos. GHL está optimizado para operar el ciclo completo de adquisición, conversión, pago, relación y seguimiento.', 'Bodyx'), callout('Square es una restricción de arquitectura, no una preferencia. La documentación pública revisada confirma GHL + Square para áreas relevantes de pagos, cursos y membresías. No se encontró confirmación oficial de Hotmart + Square.','HALLAZGO CENTRAL'), Spacer(1,8), table([
    ['Decisión', 'Recomendación'],
    ['Plataforma para Derma.M bajo Square', 'GHL + Square'],
    ['Propiedad de producción', 'Cuenta/subcuenta, dominio, Square, billing y activos bajo Derma.M'],
    ['Estado actual', 'POC validada preliminarmente; todavía no producción'],
    ['Hotmart', 'Alternativa si se acepta el sistema de pagos de Hotmart'],
    ['WordPress existente', 'Reemplazo completo; no es la base de la nueva academia'],
], [52*mm,122*mm]), P('La conclusión no significa que Hotmart sea inferior. Significa que su fortaleza comercial depende de aceptar su checkout y su infraestructura de pagos, mientras que Derma.M necesita conservar Square.', 'Bodyx'), PageBreak()]

# Scope and criteria
story += [P('2. Alcance y criterios de decisión','H1x'), P('Este informe está limitado a disponibilidad, jurisdicción, precios e integraciones aplicables a creadores y negocios que operan en Estados Unidos. Las páginas sin fecha editorial verificable se identifican por su fecha de consulta.', 'Bodyx'), table([
    ['Criterio', 'Pregunta de decisión'],
    ['Cursos de video', '¿Qué tan fácil es estructurar, entregar y seguir un curso lineal?'],
    ['Membresías', '¿Cómo se manejan pagos recurrentes, comunidades y retención?'],
    ['Evaluación', '¿Permite quizzes, aprobación, certificados y evidencia de competencia?'],
    ['Square', '¿Puede Derma.M conservar su procesador obligatorio?'],
    ['Funnel', '¿Puede conectarse Meta → landing → CRM → checkout → alumno?'],
    ['Economía', '¿Qué costos son fijos, variables y dependientes del volumen?'],
    ['Control', '¿Quién posee los datos, dominio, pagos y activos?'],
], [43*mm,131*mm]), P('Supuestos de análisis', 'H2x'), bullet('El sitio WordPress actual se reemplaza completamente.'), bullet('La POC de GHL es evidencia preliminar, no una implementación productiva.'), bullet('Square es el método de pago obligatorio para Derma.M.'), bullet('Los precios, tarifas y capacidades pueden cambiar; deben reconfirmarse antes de firmar o lanzar.'), PageBreak()]

# Platform comparison
story += [P('3. Qué resuelve cada plataforma','H1x'), table([
    ['Área', 'GHL / GoHighLevel', 'Hotmart'],
    ['Posicionamiento', 'Sistema operativo comercial para CRM, funnels, pagos, cursos y automatizaciones.', 'Ecosistema de venta y entrega de productos digitales.'],
    ['Curso', 'Courses, módulos, lecciones, videos, archivos y ofertas.', 'Hotmart Club, área de miembros, video, materiales y progreso.'],
    ['Membresía', 'Membresías y comunidades conectadas al CRM.', 'Suscripciones, comunidades, bundles y productos adicionales.'],
    ['CRM', 'Nativo y central para leads, compradores y alumnos.', 'Menos central; suele requerir integraciones o webhooks.'],
    ['Afiliados', 'No es su ventaja principal.', 'Una de sus fortalezas comerciales.'],
    ['Checkout', 'Con proveedor conectado, incluido Square.', 'Checkout propio de Hotmart.'],
    ['Control de relación', 'Alto: workflows, emails, WhatsApp, pipelines y tareas.', 'Alto dentro del ecosistema Hotmart; menor control sobre el procesador.'],
], [34*mm,70*mm,70*mm]), Spacer(1,8), callout('Hotmart reduce el trabajo técnico de lanzar un infoproducto. GHL requiere más arquitectura, pero permite diseñar la operación completa alrededor de la relación con el alumno.','LECTURA ESTRATÉGICA'), PageBreak()]

# Course types
story += [P('4. Casos de uso prioritarios','H1x'), P('4.1 Cursos de video estructurados','H2x'), table([
    ['Aspecto', 'GHL', 'Hotmart'],
    ['Organización', 'Módulos, lecciones, archivos y ofertas.', 'Área de miembros especializada con módulos, lecciones y materiales.'],
    ['Progresión', 'Controles de experiencia y progresión; validar configuración final.', 'Progreso y experiencia de miembro dentro de Hotmart Club.'],
    ['Automatización', 'Muy fuerte: onboarding, segmentación, WhatsApp y workflows.', 'Disponible, más centrada en venta y entrega.'],
    ['Resultado', 'Adecuado y más conectado a operación.', 'Más maduro como producto de cursos digitales listo para usar.'],
], [36*mm,69*mm,69*mm]), P('4.2 Membresías y comunidades','H2x'), P('Hotmart destaca cuando la membresía depende de checkout propio, afiliados, bundles y alcance internacional. GHL destaca cuando la retención depende de CRM, comunicación, pagos fallidos, reactivación, ventas de servicios y seguimiento individual.', 'Bodyx'), P('4.3 Certificaciones y evaluaciones','H2x'), P('GHL documenta assessments/quizzes con preguntas, passing grade, pass/fail, intentos, resultados y workflows. Hotmart puede entregar certificados y gestionar progreso, pero no se verificó que cubra por sí solo proctoring, rúbricas complejas, bancos de exámenes o auditoría regulatoria.', 'Bodyx'), callout('Una certificación de finalización no equivale automáticamente a una certificación profesional rigurosa. Para una academia seria conviene agregar reglas académicas, evidencia práctica, certificado verificable y auditoría de resultados.','LÍMITE DECLARADO'), PageBreak()]

# Square and funnel
story += [P('5. Square y funnel completo','H1x'), P('5.1 GHL + Square','H2x'), table([
    ['Componente', 'Evaluación'],
    ['Conexión Square', 'Documentada oficialmente por HighLevel.'],
    ['Courses / Communities', 'La matriz de proveedores de HighLevel marca Square como compatible en áreas relevantes.'],
    ['Pagos únicos', 'Documentados para order forms, forms, payment links, invoices y cursos.'],
    ['Pagos recurrentes', 'Posibles, pero deben probarse con una cuenta real y el caso exacto.'],
    ['SaaS / rebilling de HighLevel', 'Restricción documentada; no confundir con cobrar los propios cursos de Derma.M.'],
], [50*mm,124*mm]), P('5.2 Hotmart + Square','H2x'), P('La documentación pública revisada de Hotmart publica tarjetas, PayPal, Apple Pay, Google Pay, Venmo, Klarna y otros métodos según país. Square no apareció en la documentación de métodos consultada y no se encontró una guía oficial para conectar una cuenta Square externa.', 'Bodyx'), callout('Hotmart Webhooks pueden enviar a GHL eventos de compra, reembolso o recurrencia. Eso sincroniza información después de la transacción; no convierte Square en el procesador de Hotmart.','NO CONFUNDIR INTEGRACIÓN CON PASARELA'), P('5.3 Arquitectura recomendada para Derma.M','H2x'), P('<b>Meta Ads → Landing GHL → CRM → Oferta → Square → Courses/Memberships → Onboarding → WhatsApp/Email → Progreso → Certificación → Recompra</b>', 'Bodyx'), PageBreak()]

# Economics
story += [P('6. Economía, costos y márgenes','H1x'), table([
    ['Elemento', 'GHL', 'Hotmart'],
    ['Costo base publicado', '$97/mes Starter.', 'Sin mensualidad base anunciada en la página consultada.'],
    ['Costo variable', 'Square, email, SMS, llamadas, WhatsApp, AI y terceros según uso.', 'Tarifa por transacción; posible video, afiliados, impuestos y reembolsos.'],
    ['Procesador', 'Square de Derma.M.', 'Sistema de pagos de Hotmart.'],
    ['Economía con volumen', 'Costo fijo más favorable cuando el volumen se estabiliza, pero requiere implementación.', 'Entrada barata para probar; comisión crece con cada venta.'],
], [42*mm,66*mm,66*mm]), P('Ejemplo orientativo con curso de $399', 'H2x'), table([
    ['Concepto', 'Referencia'],
    ['9.9% sobre $399', '$39.50'],
    ['Tarifa fija', '$0.50'],
    ['Video Player, si aplica', '$1.49'],
    ['Costo estimado Hotmart', '$41.49'],
    ['Ingreso antes de otros costos', '$357.51'],
], [85*mm,89*mm]), P('Este cálculo utiliza la fórmula consultada en la fuente de tarifas y no debe tratarse como cotización universal. Hay que confirmar país, moneda, tipo de producto, afiliados, impuestos, reembolsos, reproductor y condiciones vigentes.', 'Smallx'), callout('El punto de equilibrio puramente matemático frente a $97/mes es aproximadamente 2.34 ventas de $399 bajo ese ejemplo. No es una comparación completa: GHL añade consumos variables y Hotmart puede aportar afiliados, checkout y distribución.','INTERPRETACIÓN ECONÓMICA'), PageBreak()]

# UX/support/ownership
story += [P('7. Experiencia, soporte y propiedad','H1x'), table([
    ['Dimensión', 'GHL', 'Hotmart'],
    ['Creador', 'Más potente, pero con curva de aprendizaje mayor.', 'Más directo para crear y vender un producto digital.'],
    ['Alumno', 'Experiencia branded conectada a CRM; depende de configuración.', 'Área de miembros más especializada y lista para cursos.'],
    ['Soporte', 'Help Center, comunidad y documentación técnica.', 'Help Center, documentación de cursos, pagos, afiliados y webhooks.'],
    ['Calidad objetiva de soporte', 'No verificada comparativamente con evidencia suficiente.', 'No verificada comparativamente con evidencia suficiente.'],
    ['Propiedad recomendada', 'Cuenta, dominio, Square, billing y activos bajo Derma.M.', 'Cuenta y activos de Hotmart bajo el titular real del negocio.'],
], [42*mm,66*mm,66*mm]), P('Modelo administrado por EmpathoAI', 'H2x'), P('Si EmpathoAI aloja la academia en infraestructura propia, no debe presentarse como “GHL gratis”. El cliente estaría pagando una modalidad administrada que incluye infraestructura, configuración, soporte y posibles consumos variables. Deben definirse límites, propiedad de datos, acceso, exportación y plan de salida.', 'Bodyx'), PageBreak()]

# Integrated alternative and differentiation
story += [P('8. Viabilidad de una solución integrada','H1x'), P('Es técnicamente viable construir una solución integrada sin desarrollar otro Hotmart o GHL desde cero. La ruta sensata es utilizar GHL como núcleo operativo, Square como procesador, una capa académica especializada cuando sea necesario y reporting unificado.', 'Bodyx'), table([
    ['Capa', 'Función recomendada'],
    ['Adquisición', 'Meta Ads, Pixel/CAPI, landing y tracking.'],
    ['Conversión', 'GHL funnel y checkout con Square.'],
    ['Entrega', 'GHL Courses/Memberships y video.'],
    ['Relación', 'CRM, workflows, email, WhatsApp y tareas humanas.'],
    ['Evaluación', 'Assessments, reglas de aprobación y certificado verificable.'],
    ['Datos', 'Exportación, ownership del dominio, contactos y activos.'],
    ['Reporting', 'Anuncio → lead → compra → progreso → certificación → recompra.'],
], [42*mm,132*mm]), P('Oportunidades de diferenciación', 'H2x'), bullet('Solución Square-first para negocios que no quieren cambiar de pasarela.'), bullet('Certificaciones con ID verificable, rúbricas, evidencia práctica y auditoría.'), bullet('Automatización de abandono, reactivación, pagos fallidos y riesgo de deserción.'), bullet('Analítica de rendimiento comercial y académico en un mismo reporte.'), bullet('Migración limpia desde WordPress cargado de plugins.'), bullet('Verticales profesionales: estética, belleza, compliance y formación especializada.'), PageBreak()]

# Recommendation and acceptance
story += [P('9. Recomendación de implementación para Derma.M','H1x'), P('La nueva academia debe vivir en una cuenta o subcuenta de GHL propiedad de Derma.M. La POC de Alex es una prueba de dirección, no una autorización para asumir que producción está terminada.', 'Bodyx'), table([
    ['Fase', 'Resultado exigible'],
    ['1. Ownership', 'Cuenta, dominio, Square, billing, usuarios administradores y activos bajo Derma.M.'],
    ['2. Arquitectura', 'Productos, ofertas, precios, acceso, tags, pipelines y workflows documentados.'],
    ['3. Pago único', 'Compra real con Square, acceso automático y confirmación en CRM.'],
    ['4. Fallos', 'Pago rechazado, abandono, reintento, email/WhatsApp y tratamiento del acceso.'],
    ['5. Reembolso', 'Reembolso real y verificación de acceso, notificaciones y registro.'],
    ['6. Recurrencia', 'Renovación, cancelación, tarjeta fallida y revocación.'],
    ['7. Evaluación', 'Quiz, aprobación, reintento, certificado y workflow posterior.'],
    ['8. Salida', 'Exportación de contactos, contenidos, dominios, datos y documentación.'],
], [38*mm,136*mm]), callout('No lanzar hasta que el flujo completo funcione con datos y pagos reales dentro de la cuenta de Derma.M.','CRITERIO DE PRODUCCIÓN'), PageBreak()]

# Source ledger
story += [P('10. Registro de fuentes y límites','H1x'), P('Las fuentes siguientes fueron consultadas el 10 de septiembre de 2026. Cuando una página no muestra fecha editorial verificable, se reporta la fecha de consulta y no una fecha de publicación inventada.', 'Bodyx')]
for i,(name,url,note) in enumerate(sources,1):
    story.append(P(f'<b>[{i}] {escape(name)}</b> · {link(url,url)}<br/>{escape(note)}','Source'))
story += [Spacer(1,8), P('Límites de verificación', 'H2x'), bullet('No se encontró confirmación oficial pública de Hotmart como pasarela Square externa.'), bullet('No se verificó proctoring, rúbricas complejas ni acreditación regulatoria nativa en ninguna plataforma.'), bullet('Los precios de AI, WhatsApp, email, SMS y servicios externos dependen de configuración y consumo.'), bullet('La calidad comparativa del soporte no se afirmó sin una muestra metodológicamente comparable.'), bullet('La recomendación es específica para el requisito actual de Square y no una clasificación universal de plataformas.'), Spacer(1,10), P('<b>Documento preparado por EmpathoAI Strategic Growth & Revenue Infrastructure.</b><br/>Human depth. Machine leverage. Precision over volume.', 'Smallx')]

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=15*mm, leftMargin=15*mm, topMargin=24*mm, bottomMargin=18*mm, title='GHL vs Hotmart — Análisis comparativo para Derma.M Academy', author='EmpathoAI')
doc.build(story, onFirstPage=page_header_footer, onLaterPages=page_header_footer)
print(f'created={OUT} bytes={OUT.stat().st_size}')
