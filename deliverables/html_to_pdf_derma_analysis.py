from html.parser import HTMLParser
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame
from xml.sax.saxutils import escape

SRC = Path(__file__).with_name('dermam_academy_ghl_vs_hotmart_analysis_v2.html')
OUT = Path(__file__).with_name('dermam_academy_ghl_vs_hotmart_analysis.pdf')

class SlideParser(HTMLParser):
    wanted = {'h1','h2','h3','p','li'}
    def __init__(self):
        super().__init__(); self.slides=[]; self.current=None; self.stack=[]; self.parts=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs); cls=attrs.get('class','')
        if tag=='section' and 'slide' in cls.split():
            self.current={'items':[],'cover':'cover' in cls}; self.slides.append(self.current)
        if self.current is not None and (tag in self.wanted or any(x in cls.split() for x in ['callout','big-verdict','small-note','metric','node','step','price','matrix'])):
            self.stack.append((tag,cls)); self.parts=[]
    def handle_endtag(self, tag):
        if not self.current or not self.stack: return
        open_tag, cls=self.stack[-1]
        if open_tag==tag:
            text=' '.join(''.join(self.parts).split())
            if text and text not in [x[1] for x in self.current['items']]:
                kind='title' if tag in ('h1','h2') else ('subtitle' if tag=='h3' else 'body')
                self.current['items'].append((kind,text,cls))
            self.stack.pop(); self.parts=[]
    def handle_data(self, data):
        if self.stack: self.parts.append(data)

html=SRC.read_text(encoding='utf-8')
parser=SlideParser(); parser.feed(html)
slides=parser.slides

W,H=13.333*inch,7.5*inch
ORANGE=colors.HexColor('#ff4402'); INK=colors.HexColor('#101113'); MUTED=colors.HexColor('#62656b'); SOFT=colors.HexColor('#f5f5f2'); PALE=colors.HexColor('#fff0eb'); LINE=colors.HexColor('#dedfdf'); GREEN=colors.HexColor('#157347')
styles=getSampleStyleSheet()
body=ParagraphStyle('body',parent=styles['BodyText'],fontName='Helvetica',fontSize=11.4,leading=14.2,textColor=MUTED,spaceAfter=7)
small=ParagraphStyle('small',parent=body,fontSize=8.5,leading=10.5)
card=ParagraphStyle('card',parent=body,fontSize=10.2,leading=12.3)
head=ParagraphStyle('head',parent=styles['Heading2'],fontName='Helvetica-Bold',fontSize=18,leading=20,textColor=INK,spaceAfter=8)


def draw_para(c, text, x, y, width, style=body):
    p=Paragraph(escape(text).replace('[','&#91;').replace(']','&#93;'), style)
    w,h=p.wrap(width, H)
    p.drawOn(c,x,y-h)
    return h

def draw_box(c, text, x, y, width, height, fill=SOFT, border=LINE, accent=ORANGE, style=card):
    c.setFillColor(fill); c.setStrokeColor(border); c.rect(x,y-height,width,height,fill=1,stroke=1)
    c.setFillColor(accent); c.rect(x,y-height,width,5,fill=1,stroke=0)
    draw_para(c,text,x+14,y-14,width-28,style)

def render_slide(c, slide, num):
    c.setFillColor(colors.white); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(ORANGE); c.rect(0,0,10,H,fill=1,stroke=0)
    items=slide['items']
    titles=[t for k,t,cl in items if k=='title']
    title=titles[0] if titles else 'GHL vs Hotmart'
    if slide['cover']:
        c.setFillColor(PALE); c.rect(W*.61,0,W*.39,H,fill=1,stroke=0)
        c.setFillColor(ORANGE); c.setFont('Helvetica-Bold',10); c.drawString(58,H-48,'ANÁLISIS DE DECISIÓN · ESTADOS UNIDOS')
        c.setFillColor(INK); c.setFont('Helvetica-Bold',32); c.drawString(58,H-180,'GHL vs Hotmart')
        c.drawString(58,H-220,'para cursos online')
        c.setFillColor(MUTED); c.setFont('Helvetica',14); c.drawString(60,H-285,'Viabilidad, economía, funnels, cursos y diferenciación.')
        c.drawString(60,H-307,'Restricción decisiva: Square es obligatorio para Derma.M.')
        c.setFillColor(INK); c.rect(W-305,H-385,240,240,fill=1,stroke=0)
        c.setFillColor(colors.white); c.setFont('Helvetica-Bold',24); c.drawCentredString(W-185,H-215,'GHL')
        c.setFillColor(ORANGE); c.drawCentredString(W-185,H-257,'VS')
        c.setFillColor(colors.white); c.drawCentredString(W-185,H-299,'HOTMART')
        c.setFillColor(INK); c.setFont('Helvetica-Bold',9); c.drawString(60,35,'EmpathoAI · HUMAN DEPTH. MACHINE LEVERAGE.')
        c.setFillColor(MUTED); c.drawRightString(W-55,35,'10 septiembre 2026')
        c.showPage(); return
    c.setFillColor(ORANGE); c.setFont('Helvetica-Bold',9); c.drawRightString(W-58,H-38,f'{num:02d} / DERMA.M ACADEMY')
    c.setFillColor(INK); c.setFont('Helvetica-Bold',25); c.drawString(58,H-82,title[:110])
    c.setStrokeColor(LINE); c.setLineWidth(1.2); c.line(58,H-104,W-58,H-104)
    content=[(k,t,cl) for k,t,cl in items if k!='title']
    # Cover the content as readable blocks in two columns.
    left=58; top=H-132; colw=(W-140)/2; gap=24
    left_items=content[::2]; right_items=content[1::2]
    for x,arr in [(left,left_items),(left+colw+gap,right_items)]:
        y=top
        for kind,text,cls in arr:
            if y<70: break
            if 'big-verdict' in cls or 'callout' in cls:
                h=min(106,max(48,18+len(text)*0.38)); draw_box(c,text,x,y,colw,h,fill=PALE,accent=ORANGE,style=card); y-=h+14
            elif kind=='subtitle' or 'metric' in cls or 'node' in cls or 'step' in cls or 'price' in cls:
                h=min(92,max(42,18+len(text)*0.25)); draw_box(c,text,x,y,colw,h,fill=SOFT,accent=ORANGE,style=card); y-=h+12
            else:
                h=draw_para(c,text,x,y,colw,body); y-=h+8
    c.setFillColor(MUTED); c.setFont('Helvetica-Bold',8); c.drawString(58,28,'EMPATHOAI'); c.drawRightString(W-58,28,f'{num} / {len(slides)}')
    c.showPage()

c=canvas.Canvas(str(OUT),pagesize=(W,H))
c.setTitle('GHL vs Hotmart — Análisis comparativo para cursos online')
c.setAuthor('EmpathoAI')
for i,slide in enumerate(slides,1): render_slide(c,slide,i)
c.save()
print(f'created={OUT} pages={len(slides)} bytes={OUT.stat().st_size}')
