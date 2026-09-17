from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pathlib import Path

ROOT = Path(r"F:\EMPATHOAI_OS")
ASSETS = ROOT / "references" / "brand-assets"
OUT = ROOT / "deliverables" / "dermam_academy_platform_proposal.pptx"
LOGO = ASSETS / "01_LOGO" / "MASTER" / "empathoai-master-logo-light-trans.png"

# Light external-document adaptation of EmpathoAI tokens.
ORANGE = RGBColor(0xFF, 0x44, 0x02)
INK = RGBColor(0x0A, 0x0A, 0x0B)
GRAPHITE = RGBColor(0x2D, 0x2D, 0x2F)
MUTED = RGBColor(0x66, 0x66, 0x68)
LINE = RGBColor(0xE5, 0xE5, 0xEA)
CANVAS = RGBColor(0xFF, 0xFF, 0xFF)
SOFT = RGBColor(0xF7, 0xF7, 0xF5)
PALE_ORANGE = RGBColor(0xFF, 0xF0, 0xEB)
GREEN = RGBColor(0x1C, 0x7C, 0x54)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]


def rect(slide, x, y, w, h, fill, line=None, radius=False):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(y), Inches(w), Inches(h)
    )
    shape.fill.solid(); shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = line if line else fill
    if radius:
        shape.adjustments[0] = 0.04
    return shape


def text(slide, value, x, y, w, h, size=18, color=INK, bold=False,
         font="IBM Plex Sans", align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.TOP,
         italic=False, tracking=None):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame; tf.clear(); tf.word_wrap = True
    tf.margin_left = Inches(0.02); tf.margin_right = Inches(0.02)
    tf.margin_top = Inches(0.01); tf.margin_bottom = Inches(0.01)
    tf.vertical_anchor = valign
    p = tf.paragraphs[0]; p.alignment = align
    run = p.add_run(); run.text = value
    f = run.font; f.name = font; f.size = Pt(size); f.bold = bold; f.italic = italic
    f.color.rgb = color
    if tracking is not None:
        f.kerning = Pt(tracking)
    return box


def bullet_list(slide, items, x, y, w, h, size=16, color=INK, gap=0.13):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame; tf.clear(); tf.word_wrap = True
    tf.margin_left = Inches(0.04); tf.margin_right = Inches(0.02)
    for idx, item in enumerate(items):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = item; p.level = 0; p.space_after = Pt(gap * 72)
        p.font.name = "IBM Plex Sans"; p.font.size = Pt(size); p.font.color.rgb = color
        p._p.get_or_add_pPr().insert(0, p._p.get_or_add_pPr()._new_buChar()) if False else None
        # Use a compact orange marker instead of PowerPoint bullets.
        p.text = "■  " + item
        p.runs[0].font.color.rgb = ORANGE
        if len(p.runs) > 1:
            p.runs[1].font.color.rgb = color
    return box


def logo(slide, x=0.62, y=0.32, w=1.52):
    if LOGO.exists():
        slide.shapes.add_picture(str(LOGO), Inches(x), Inches(y), width=Inches(w))
    else:
        rect(slide, x, y+0.04, 0.14, 0.14, ORANGE)
        text(slide, "EMPATHOAI", x+0.22, y, w, 0.22, size=13, bold=True, color=INK)


def header(slide, kicker, title, page):
    rect(slide, 0, 0, 13.333, 7.5, CANVAS)
    logo(slide)
    text(slide, kicker.upper(), 10.1, 0.39, 2.55, 0.22, size=8.5, bold=True, color=ORANGE, align=PP_ALIGN.RIGHT, tracking=1.2)
    text(slide, title, 0.72, 1.02, 11.9, 0.58, size=29, bold=True, color=INK)
    rect(slide, 0.72, 1.78, 11.9, 0.012, LINE)
    text(slide, f"DERMA.M ACADEMY  /  {page:02d}", 0.72, 7.08, 4.0, 0.18, size=7.5, bold=True, color=MUTED, tracking=0.6)
    text(slide, "HUMAN DEPTH. MACHINE LEVERAGE.", 9.35, 7.08, 3.28, 0.18, size=7.5, bold=True, color=MUTED, align=PP_ALIGN.RIGHT, tracking=0.45)


def label(slide, value, x, y, w=1.6):
    rect(slide, x, y, w, 0.30, PALE_ORANGE)
    text(slide, value.upper(), x+0.10, y+0.06, w-0.20, 0.15, size=8, bold=True, color=ORANGE, tracking=0.6)


def card(slide, x, y, w, h, title, body, accent=ORANGE, fill=SOFT):
    rect(slide, x, y, w, h, fill, LINE, radius=False)
    rect(slide, x, y, 0.06, h, accent)
    text(slide, title, x+0.24, y+0.20, w-0.45, 0.30, size=15, bold=True, color=INK)
    text(slide, body, x+0.24, y+0.62, w-0.45, h-0.78, size=12.5, color=MUTED)

# 1 Cover
s = prs.slides.add_slide(blank)
rect(s, 0, 0, 13.333, 7.5, CANVAS)
rect(s, 0, 0, 0.13, 7.5, ORANGE)
logo(s, 0.72, 0.52, 1.95)
text(s, "PROPUESTA DE PLATAFORMA", 0.78, 2.00, 4.4, 0.25, size=11, bold=True, color=ORANGE, tracking=1.5)
text(s, "Una academia más simple\npara crecer con control", 0.72, 2.42, 8.8, 1.35, size=37, bold=True, color=INK)
text(s, "Reemplazo de la infraestructura WordPress actual\npor una experiencia educativa y comercial más estable.", 0.76, 4.12, 6.55, 0.72, size=18, color=MUTED)
rect(s, 8.7, 1.65, 3.2, 3.2, PALE_ORANGE)
rect(s, 9.15, 2.12, 2.25, 2.25, INK)
rect(s, 10.73, 3.70, 0.67, 0.67, ORANGE)
text(s, "DERMA.M\nACADEMY", 9.47, 2.62, 1.6, 0.8, size=19, bold=True, color=CANVAS, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
text(s, "Presentado por EmpathoAI", 0.76, 6.42, 3.8, 0.22, size=10, bold=True, color=GRAPHITE)
text(s, "Septiembre 2026", 0.76, 6.70, 2.2, 0.18, size=9, color=MUTED)

# 2 Why change
s = prs.slides.add_slide(blank); header(s, "01 / diagnóstico", "El problema no es el contenido. Es la base.", 2)
text(s, "La academia actual depende de WordPress y una acumulación de plugins. Eso aumenta la fricción, el mantenimiento y el riesgo operativo.", 0.74, 2.08, 11.1, 0.55, size=18, color=MUTED)
card(s, 0.74, 3.02, 3.75, 2.28, "Mantenimiento", "Actualizaciones, compatibilidad y errores consumen tiempo que debería ir a ventas y alumnos.", ORANGE)
card(s, 4.79, 3.02, 3.75, 2.28, "Experiencia", "El alumno encuentra una experiencia fragmentada entre registro, pago, acceso y soporte.", GRAPHITE)
card(s, 8.84, 3.02, 3.75, 2.28, "Control", "La operación queda atada a una estructura difícil de auditar, transferir y escalar.", GREEN)
label(s, "Principio", 0.74, 5.92, 1.12)
text(s, "No vamos a maquillar el sistema anterior. Vamos a reemplazarlo por una base más limpia.", 2.02, 5.92, 9.7, 0.32, size=16, bold=True, color=INK)

# 3 solution
s = prs.slides.add_slide(blank); header(s, "02 / solución", "Una sola experiencia para vender, enseñar y acompañar.", 3)
text(s, "La nueva academia se construye fuera del WordPress actual, con GHL como centro operativo y Square como procesador de pagos.", 0.74, 2.08, 11.0, 0.48, size=17, color=MUTED)
# flow
steps = [("01", "Sitio y funnel", "Presentación clara\ny conversión"), ("02", "Square", "Cobro con la\ncuenta existente"), ("03", "Courses", "Acceso y\ncontenido"), ("04", "CRM + WhatsApp", "Seguimiento\ny soporte")]
xs = [0.74, 3.86, 6.98, 10.10]
for i, (num, title, body) in enumerate(steps):
    rect(s, xs[i], 3.12, 2.42, 1.82, SOFT, LINE)
    rect(s, xs[i], 3.12, 2.42, 0.08, ORANGE if i == 0 else GRAPHITE)
    text(s, num, xs[i]+0.18, 3.38, 0.45, 0.25, size=10, bold=True, color=ORANGE)
    text(s, title, xs[i]+0.18, 3.78, 2.0, 0.30, size=15, bold=True, color=INK)
    text(s, body, xs[i]+0.18, 4.20, 2.0, 0.45, size=12, color=MUTED)
    if i < 3:
        text(s, "→", xs[i]+2.55, 3.80, 0.38, 0.34, size=24, bold=True, color=ORANGE, align=PP_ALIGN.CENTER)
label(s, "Resultado", 0.74, 5.70, 1.20)
text(s, "Menos piezas. Menos puntos de falla. Más claridad para Derma.M y para sus alumnos.", 2.10, 5.70, 9.9, 0.30, size=16, bold=True, color=INK)

# 4 What she gets
s = prs.slides.add_slide(blank); header(s, "03 / alcance", "Qué recibe Derma.M.", 4)
items = [
    ("Academia nueva", "Sitio, landing y experiencia de inscripción sin depender del WordPress actual."),
    ("Cursos y acceso", "Contenido organizado, registro de alumnos y acceso controlado."),
    ("Pagos con Square", "Se conserva la cuenta de pagos que Derma.M ya utiliza."),
    ("WhatsApp", "Canal de comunicación conectado al CRM para responder y dar seguimiento."),
    ("Automatizaciones", "Confirmación, onboarding, recordatorios y soporte básico."),
    ("Base transferible", "El dominio, contenido, datos y Square permanecen bajo control de Derma.M.")
]
for i, (t, b) in enumerate(items):
    x = 0.74 + (i % 2) * 6.05; y = 2.16 + (i // 2) * 1.34
    rect(s, x, y, 5.55, 1.04, CANVAS, LINE)
    rect(s, x, y, 0.06, 1.04, ORANGE if i % 2 == 0 else GRAPHITE)
    text(s, t, x+0.24, y+0.18, 4.95, 0.26, size=14, bold=True, color=INK)
    text(s, b, x+0.24, y+0.52, 5.0, 0.36, size=11.5, color=MUTED)

# 5 Option A
s = prs.slides.add_slide(blank); header(s, "04 / opción A", "Cuenta propia de Derma.M.", 5)
label(s, "Mayor autonomía", 0.74, 2.10, 1.65)
text(s, "La cuenta de GHL, el dominio, Square y los activos quedan directamente bajo Derma.M.", 0.74, 2.58, 7.0, 0.58, size=20, bold=True, color=INK)
rect(s, 8.65, 2.05, 3.85, 2.12, INK)
text(s, "$117", 8.98, 2.42, 2.6, 0.70, size=42, bold=True, color=CANVAS)
text(s, "/ mes de plataforma", 9.02, 3.27, 2.7, 0.24, size=12, color=RGBColor(0xC8,0xC8,0xC8))
rect(s, 8.98, 3.76, 2.8, 0.05, ORANGE)
text(s, "GHL $97  +  WhatsApp $20", 8.98, 3.90, 3.05, 0.22, size=10.5, bold=True, color=CANVAS)
bullet_list(s, ["Más control y menor dependencia de EmpathoAI.", "La cliente asume directamente el costo mensual.", "Recomendable si quiere administrar el sistema internamente."], 0.90, 3.62, 7.0, 1.45, size=15)
text(s, "No incluye tarifas de Square ni consumos variables de mensajería/IA.", 0.74, 5.95, 8.0, 0.25, size=11, italic=True, color=MUTED)

# 6 Option B
s = prs.slides.add_slide(blank); header(s, "05 / opción B", "Plataforma administrada por EmpathoAI.", 6)
label(s, "Menor entrada", 0.74, 2.10, 1.45)
text(s, "EmpathoAI aloja y administra la infraestructura. Derma.M paga solo los servicios variables acordados.", 0.74, 2.58, 7.15, 0.58, size=20, bold=True, color=INK)
rect(s, 8.65, 2.05, 3.85, 2.12, PALE_ORANGE)
text(s, "≈ $39", 8.98, 2.42, 2.8, 0.70, size=42, bold=True, color=INK)
text(s, "/ mes estimados", 9.02, 3.27, 2.7, 0.24, size=12, color=MUTED)
rect(s, 8.98, 3.76, 2.8, 0.05, ORANGE)
text(s, "GoGHL $29  +  IA estimada $10", 8.98, 3.90, 3.12, 0.22, size=10.5, bold=True, color=INK)
bullet_list(s, ["Menor costo visible para Derma.M.", "Implementación y operación centralizadas.", "EmpathoAI mantiene la responsabilidad técnica.", "El uso de IA es estimado, no un precio fijo garantizado."], 0.90, 3.62, 7.0, 1.75, size=15)
text(s, "La cuenta y los activos de Derma.M deben mantenerse identificables y transferibles.", 0.74, 5.95, 8.6, 0.25, size=11, italic=True, color=MUTED)

# 7 comparison
s = prs.slides.add_slide(blank); header(s, "06 / decisión", "Dos modelos. Una misma academia.", 7)
# table
x0, y0 = 0.74, 2.15
cols = [3.05, 3.55, 3.55]
headers = ["Criterio", "Cuenta propia", "Administrada por EmpathoAI"]
for j, h in enumerate(headers):
    x = x0 + sum(cols[:j]); fill = INK if j else GRAPHITE
    rect(s, x, y0, cols[j], 0.56, fill)
    text(s, h, x+0.16, y0+0.16, cols[j]-0.32, 0.22, size=11, bold=True, color=CANVAS)
rows = [
    ("Costo visible", "$117/mes", "≈ $39/mes estimados"),
    ("Control", "Directo de Derma.M", "Gestionado por EmpathoAI"),
    ("Responsabilidad técnica", "Derma.M / su equipo", "EmpathoAI"),
    ("Dependencia", "Menor", "Mayor, con acuerdo claro"),
    ("Recomendación", "Si quiere autonomía", "Si prioriza entrada baja")
]
for i, row in enumerate(rows):
    y = y0 + 0.56 + i*0.68
    for j, val in enumerate(row):
        x = x0 + sum(cols[:j]); fill = SOFT if i % 2 == 0 else CANVAS
        rect(s, x, y, cols[j], 0.68, fill, LINE)
        text(s, val, x+0.16, y+0.20, cols[j]-0.32, 0.24, size=12, bold=(j==0 or i==4), color=INK if j != 2 else GRAPHITE)
label(s, "Mi recomendación", 0.74, 6.28, 1.68)
text(s, "Presentar ambas. Recomendar la opción administrada para validar rápido y reducir fricción inicial, con una ruta de transferencia documentada.", 2.62, 6.28, 9.8, 0.28, size=14, bold=True, color=INK)

# 8 next steps
s = prs.slides.add_slide(blank); header(s, "07 / siguiente paso", "Validar antes de lanzar.", 8)
text(s, "La decisión no debe basarse solo en el precio. Primero hay que probar el flujo completo con las cuentas reales.", 0.74, 2.08, 11.0, 0.46, size=18, color=MUTED)
checks = ["Crear la nueva estructura en GHL.", "Conectar Square de Derma.M.", "Migrar y ordenar el contenido del curso.", "Probar compra, acceso, reembolso y revocación.", "Configurar WhatsApp y respuestas básicas.", "Definir propiedad, soporte y transferencia."]
for i, item in enumerate(checks):
    x = 0.86 + (i % 2)*6.05; y = 2.98 + (i//2)*0.86
    rect(s, x, y, 5.35, 0.58, CANVAS, LINE)
    rect(s, x+0.18, y+0.17, 0.24, 0.24, ORANGE)
    text(s, "✓", x+0.20, y+0.15, 0.20, 0.22, size=12, bold=True, color=CANVAS, align=PP_ALIGN.CENTER)
    text(s, item, x+0.60, y+0.16, 4.55, 0.22, size=13, color=INK)
rect(s, 0.74, 5.88, 11.85, 0.70, INK)
text(s, "Decisión solicitada", 1.03, 6.08, 1.7, 0.20, size=11, bold=True, color=ORANGE)
text(s, "Elegir el modelo de cuenta y autorizar la prueba de producción.", 2.83, 6.06, 8.95, 0.22, size=15, bold=True, color=CANVAS)

# Speaker notes as a final source note on the last slide.
text(s, "Costos mostrados: estimaciones de plataforma compartidas para esta propuesta. Square y consumos variables se facturan aparte.", 0.74, 6.72, 11.2, 0.18, size=8.5, color=MUTED, italic=True)

prs.save(OUT)
print(OUT)
