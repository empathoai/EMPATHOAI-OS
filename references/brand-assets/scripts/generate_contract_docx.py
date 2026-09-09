#!/usr/bin/env python3
"""
EmpathoAI Contract Template Generator — DOCX Output
Generates a professional .docx contract using python-docx with EmpathoAI sovereign branding.
Tokens sourced from: F:\OS-EmpathoAI\EMPATHOAI_BRAND_ASSETS\05_TOKENS\tokens.json
"""

import os
from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

# ─── EmpathoAI Sovereign Tokens ───
TOKENS = {
    "canvas": RGBColor(0x0A, 0x0A, 0x0B),        # Obsidian Dark
    "surface_deep": RGBColor(0x14, 0x14, 0x16),  # Deep Surface
    "surface_mid": RGBColor(0x1E, 0x1E, 0x22),   # Mid Surface
    "hairline": RGBColor(0x2D, 0x2D, 0x2F),      # Technical Hairline
    "ivory": RGBColor(0xF5, 0xF5, 0xF5),         # Technical Ivory
    "muted": RGBColor(0x8E, 0x8E, 0x93),         # Muted Telemetry
    "orange": RGBColor(0xFF, 0x44, 0x02),        # Electric Signal Orange
    "ivory_dark": RGBColor(0xC7, 0xC7, 0xCC),    # Body text
}

FONTS = {
    "editorial": "IBM Plex Sans",
    "mono": "IBM Plex Mono",
}

# ─── Helpers ───
def set_cell_shading(cell, color_hex):
    """Set background color on a table cell."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_border(cell, **kwargs):
    """Set cell borders: top, bottom, left, right with (sz, val, color)."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}></w:tcBorders>')
    for edge, (sz, val, color) in kwargs.items():
        element = parse_xml(
            f'<w:{edge} {nsdecls("w")} w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        )
        tcBorders.append(element)
    tcPr.append(tcBorders)

def add_styled_run(paragraph, text, font_name=None, size=None, bold=False, color=None, italic=False, letter_spacing=None):
    run = paragraph.add_run(text)
    if font_name:
        run.font.name = font_name
        r = run._element
        rFonts = r.find(qn('w:rFonts'))
        if rFonts is not None:
            rFonts.set(qn('w:ascii'), font_name)
            rFonts.set(qn('w:hAnsi'), font_name)
            rFonts.set(qn('w:cs'), font_name)
    if size:
        run.font.size = Pt(size)
    if bold:
        run.font.bold = True
    if color:
        run.font.color.rgb = color
    if italic:
        run.font.italic = True
    if letter_spacing:
        # letter spacing in twips (1/20 pt)
        run._element.get_or_add_rPr().append(
            parse_xml(f'<w:spacing {nsdecls("w")} w:val="{int(letter_spacing * 20)}"/>')
        )
    return run

def set_paragraph_spacing(paragraph, space_before=0, space_after=0, line_spacing=1.15):
    pf = paragraph.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = Pt(line_spacing * 12)  # approximate

def hex_color(rgb):
    return f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"

ORANGE_HEX = hex_color((0xFF, 0x44, 0x02))
HAIRLINE_HEX = hex_color((0x2D, 0x2D, 0x2F))
SURFACE_DEEP_HEX = hex_color((0x14, 0x14, 0x16))
CANVAS_HEX = hex_color((0x0A, 0x0A, 0x0B))
IVORY_HEX = hex_color((0xF5, 0xF5, 0xF5))
MUTED_HEX = hex_color((0x8E, 0x8E, 0x93))

# ─── Document Setup ───
doc = Document()

# Page setup - A4
for section in doc.sections:
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)

# Default style
style = doc.styles['Normal']
font = style.font
font.name = FONTS["editorial"]
font.size = Pt(11)
font.color.rgb = TOKENS["ivory_dark"]
pf = style.paragraph_format
pf.space_after = Pt(6)
pf.line_spacing = Pt(16)

# ─── Color note: Since docx doesn't support dark mode backgrounds well for printing,
#     we'll use light backgrounds with EmpathoAI accent colors for professional output ───
#     The HTML version is the true dark-mode sovereign version.

# ═══════════════════════════════════════════
# PAGE 1: COVER
# ═══════════════════════════════════════════

# Add spacing to push content down
for _ in range(4):
    p = doc.add_paragraph()
    set_paragraph_spacing(p, 0, 0)
    p.paragraph_format.line_spacing = Pt(12)

# Logo row
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
add_styled_run(p, "■", FONTS["mono"], 28, True, TOKENS["orange"])
add_styled_run(p, " ", size=28)
add_styled_run(p, "EMPATHOAI", FONTS["editorial"], 28, True, TOKENS["ivory"], letter_spacing=0.14)

# Confidential badge
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
add_styled_run(p, "CONFIDENTIAL", FONTS["mono"], 9, True, TOKENS["orange"], letter_spacing=0.1)
p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
add_styled_run(p2, "SOVEREIGN BRAND ASSET SYSTEM v1.2", FONTS["mono"], 9, False, TOKENS["muted"], letter_spacing=0.05)

doc.add_paragraph()  # spacer

# Title
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
add_styled_run(p, "Master Services Agreement", FONTS["editorial"], 36, True, TOKENS["ivory"], letter_spacing=-0.02)
p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.LEFT
add_styled_run(p2, "& Statement of Work", FONTS["editorial"], 36, True, TOKENS["ivory"], letter_spacing=-0.02)

doc.add_paragraph()

# Subtitle
p = doc.add_paragraph()
add_styled_run(p, "Strategic Growth & Revenue Infrastructure Engagement", FONTS["editorial"], 16, False, TOKENS["muted"])

doc.add_paragraph()

# Doctrine quote
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(1.5)
add_styled_run(p, '"Human depth. Machine leverage. Precision over volume."', FONTS["editorial"], 14, False, TOKENS["muted"], italic=True)

doc.add_paragraph()
doc.add_paragraph()

# Details table
table = doc.add_table(rows=5, cols=2)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.style = 'Table Grid'

details = [
    ("PROJECT TITLE", "[Project.Title]"),
    ("AGREEMENT DATE", "[Effective.Date]"),
    ("TOTAL PROJECT FEE", "[Project.Fee]"),
    ("TIMELINE", "[Start.Date] → [EstimatedCompletionDate]"),
    ("SCOPE SUMMARY", "[High-level description — e.g., \"Precision Diagnostic & PGS Specification for revenue architecture redesign\"]"),
]

for i, (label, value) in enumerate(details):
    cell_l = table.cell(i, 0)
    cell_r = table.cell(i, 1)
    
    # Label cell
    p = cell_l.paragraphs[0]
    add_styled_run(p, label, FONTS["editorial"], 10, True, TOKENS["muted"], letter_spacing=0.02)
    set_paragraph_spacing(p, 0, 0)
    set_cell_shading(cell_l, SURFACE_DEEP_HEX)
    
    # Value cell
    p = cell_r.paragraphs[0]
    if i == 4:
        add_styled_run(p, value, FONTS["editorial"], 10, False, TOKENS["ivory_dark"])
    else:
        add_styled_run(p, value, FONTS["mono"], 10, False, TOKENS["muted"])
    set_paragraph_spacing(p, 0, 0)
    set_cell_shading(cell_r, SURFACE_DEEP_HEX)
    
    # Borders
    for cell in [cell_l, cell_r]:
        set_cell_border(cell, 
            top=(4, "single", HAIRLINE_HEX),
            bottom=(4, "single", HAIRLINE_HEX),
            left=(4, "single", HAIRLINE_HEX),
            right=(4, "single", HAIRLINE_HEX),
        )

# Set column widths
for row in table.rows:
    row.cells[0].width = Cm(5.5)
    row.cells[1].width = Cm(12.5)

doc.add_page_break()

# ═══════════════════════════════════════════
# PAGE 2: PARTIES & OVERVIEW
# ═══════════════════════════════════════════

# Section header
p = doc.add_paragraph()
add_styled_run(p, "■", FONTS["mono"], 14, True, TOKENS["orange"])
add_styled_run(p, " 01  PARTIES & AGREEMENT STRUCTURE", FONTS["editorial"], 18, True, TOKENS["ivory"], letter_spacing=-0.01)
p.paragraph_format.space_before = Pt(0)
p.paragraph_format.space_after = Pt(12)
# Add bottom border via XML
pPr = p._p.get_or_add_pPr()
pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="1" w:color="{HAIRLINE_HEX}"/></w:pBdr>')
pPr.append(pBdr)

# Intro
p = doc.add_paragraph()
add_styled_run(p, "This Agreement consists of two parts:", FONTS["editorial"], 11, False, TOKENS["ivory_dark"])

items = [
    ("Part 1 – Statement of Work (SOW):", "Defines the specific project scope, deliverables, milestones, functionality requirements, timeline, payment terms, and post-deployment support."),
    ("Part 2 – Master Services Agreement (MSA):", "Establishes the general legal terms governing all projects between the Parties, including intellectual property, confidentiality, liability limits, indemnification, and dispute resolution."),
]

for title, desc in items:
    p = doc.add_paragraph(style='List Bullet')
    p.clear()
    add_styled_run(p, title + " ", FONTS["editorial"], 11, True, TOKENS["ivory"])
    add_styled_run(p, desc, FONTS["editorial"], 11, False, TOKENS["ivory_dark"])

p = doc.add_paragraph()
add_styled_run(p, "This SOW is subject to the Master Services Agreement (\"MSA\") attached below. In case of conflict, this SOW shall control.", FONTS["editorial"], 11, False, TOKENS["ivory_dark"])

doc.add_paragraph()

# THE PARTIES
p = doc.add_paragraph()
add_styled_run(p, "■", FONTS["mono"], 12, True, TOKENS["orange"])
add_styled_run(p, " 1.1  THE PARTIES", FONTS["editorial"], 14, True, TOKENS["ivory"])

# Parties table
table = doc.add_table(rows=2, cols=2)
table.alignment = WD_TABLE_ALIGNMENT.CENTER

parties = [
    ("CLIENT", [
        ("Name:", "[Buyer.FirstName] [Buyer.LastName]"),
        ("Company:", "[Buyer.Company]"),
        ("Address:", "[Buyer.Address]"),
    ]),
    ("FREELANCER / CONSULTANT", [
        ("Name/Business:", "[Seller.Company]"),
        ("Address:", "[Seller.Address]"),
    ]),
]

for col_idx, (title, fields) in enumerate(parties):
    cell = table.cell(0, col_idx)
    p = cell.paragraphs[0]
    add_styled_run(p, title, FONTS["editorial"], 10, True, TOKENS["muted"], letter_spacing=0.02)
    set_cell_shading(cell, SURFACE_DEEP_HEX)
    set_paragraph_spacing(p, 6, 6)
    
    cell = table.cell(1, col_idx)
    for j, (label, value) in enumerate(fields):
        if j == 0:
            p = cell.paragraphs[0]
        else:
            p = cell.add_paragraph()
        add_styled_run(p, label + " ", FONTS["editorial"], 10, True, TOKENS["ivory"])
        add_styled_run(p, value, FONTS["mono"], 10, False, TOKENS["muted"])
        set_paragraph_spacing(p, 2, 2)
    set_cell_shading(cell, SURFACE_DEEP_HEX)

for row in table.rows:
    for cell in row.cells:
        set_cell_border(cell,
            top=(4, "single", HAIRLINE_HEX),
            bottom=(4, "single", HAIRLINE_HEX),
            left=(4, "single", HAIRLINE_HEX),
            right=(4, "single", HAIRLINE_HEX),
        )
    row.cells[0].width = Cm(9)
    row.cells[1].width = Cm(9)

doc.add_paragraph()

# KEY PROJECT DETAILS
p = doc.add_paragraph()
add_styled_run(p, "■", FONTS["mono"], 12, True, TOKENS["orange"])
add_styled_run(p, " 1.2  KEY PROJECT DETAILS", FONTS["editorial"], 14, True, TOKENS["ivory"])

key_details = [
    ("SCOPE OF WORK", "[High-level description — e.g., \"Build and deploy AI automation system integrating with Client's CRM and scheduling tool\"]"),
    ("TOTAL PROJECT FEE", "[Project.Fee]"),
    ("PAYMENT SCHEDULE", "[Deposit %, milestone amounts, due dates]"),
    ("PROJECT TIMELINE", "[Start.Date] to [EstimatedCompletionDate]"),
    ("WARRANTY / SUPPORT", "[e.g., \"30 days warranty support; ongoing maintenance at [Ongoing.monthly.maintenance]\"]"),
]

table = doc.add_table(rows=len(key_details), cols=2)
table.alignment = WD_TABLE_ALIGNMENT.CENTER

for i, (label, value) in enumerate(key_details):
    cell_l = table.cell(i, 0)
    cell_r = table.cell(i, 1)
    
    p = cell_l.paragraphs[0]
    add_styled_run(p, label, FONTS["editorial"], 10, True, TOKENS["muted"], letter_spacing=0.02)
    set_cell_shading(cell_l, SURFACE_DEEP_HEX)
    
    p = cell_r.paragraphs[0]
    add_styled_run(p, value, FONTS["mono"], 10, False, TOKENS["muted"])
    set_cell_shading(cell_r, SURFACE_DEEP_HEX)
    
    for cell in [cell_l, cell_r]:
        set_cell_border(cell,
            top=(4, "single", HAIRLINE_HEX),
            bottom=(4, "single", HAIRLINE_HEX),
            left=(4, "single", HAIRLINE_HEX),
            right=(4, "single", HAIRLINE_HEX),
        )

for row in table.rows:
    row.cells[0].width = Cm(5)
    row.cells[1].width = Cm(13)

doc.add_page_break()

# ═══════════════════════════════════════════
# PAGE 3: SOW - SCOPE & DELIVERABLES
# ═══════════════════════════════════════════

p = doc.add_paragraph()
add_styled_run(p, "■", FONTS["mono"], 14, True, TOKENS["orange"])
add_styled_run(p, " 02  PART 1: STATEMENT OF WORK", FONTS["editorial"], 18, True, TOKENS["ivory"], letter_spacing=-0.01)
p.paragraph_format.space_before = Pt(0)
p.paragraph_format.space_after = Pt(12)
pPr = p._p.get_or_add_pPr()
pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="1" w:color="{HAIRLINE_HEX}"/></w:pBdr>')
pPr.append(pBdr)

# 2.1 Scope & Deliverables
p = doc.add_paragraph()
add_styled_run(p, "2.1", FONTS["mono"], 11, True, TOKENS["orange"])
add_styled_run(p, "  PROJECT SCOPE & DELIVERABLES", FONTS["editorial"], 13, True, TOKENS["ivory"])

p = doc.add_paragraph()
add_styled_run(p, "Freelancer agrees to perform the following Services:", FONTS["editorial"], 11, False, TOKENS["ivory_dark"])

p = doc.add_paragraph()
add_styled_run(p, "[Project.Scope]", FONTS["mono"], 11, False, TOKENS["muted"])
p.paragraph_format.left_indent = Cm(1)

p = doc.add_paragraph()
add_styled_run(p, "Deliverables:", FONTS["editorial"], 11, True, TOKENS["ivory"])

p = doc.add_paragraph()
add_styled_run(p, "[Project.Deliverables]", FONTS["mono"], 11, False, TOKENS["muted"])
p.paragraph_format.left_indent = Cm(1)

doc.add_paragraph()

# 2.2 Functionality Requirements
p = doc.add_paragraph()
add_styled_run(p, "2.2", FONTS["mono"], 11, True, TOKENS["orange"])
add_styled_run(p, "  FUNCTIONALITY REQUIREMENTS", FONTS["editorial"], 13, True, TOKENS["ivory"])

p = doc.add_paragraph()
add_styled_run(p, "Deliverables shall, at a minimum, perform the following functionality:", FONTS["editorial"], 11, False, TOKENS["ivory_dark"])

for placeholder in ["[Functionality.System.Must.Have]", "[Functionality.To.Meet.Acceptance]"]:
    p = doc.add_paragraph()
    add_styled_run(p, placeholder, FONTS["mono"], 11, False, TOKENS["muted"])
    p.paragraph_format.left_indent = Cm(1)

doc.add_paragraph()

# 2.3 Acceptance Testing
p = doc.add_paragraph()
add_styled_run(p, "2.3", FONTS["mono"], 11, True, TOKENS["orange"])
add_styled_run(p, "  ACCEPTANCE TESTING", FONTS["editorial"], 13, True, TOKENS["ivory"])

p = doc.add_paragraph()
add_styled_run(p, "Upon delivery of each milestone, Client shall have ", FONTS["editorial"], 11, False, TOKENS["ivory_dark"])
add_styled_run(p, "5–10 business days", FONTS["editorial"], 11, True, TOKENS["ivory"])
add_styled_run(p, " to test and confirm whether the deliverables meet the functionality requirements.", FONTS["editorial"], 11, False, TOKENS["ivory_dark"])

p = doc.add_paragraph()
add_styled_run(p, "If Client does not provide written notice of nonconformity within this period, the deliverables shall be deemed accepted.", FONTS["editorial"], 11, False, TOKENS["ivory_dark"])

p = doc.add_paragraph()
add_styled_run(p, "Any notice of nonconformity must specify the deficiency in writing. Freelancer shall promptly correct and resubmit for acceptance.", FONTS["editorial"], 11, False, TOKENS["ivory_dark"])

doc.add_paragraph()

# 2.4 Timeline & Milestones
p = doc.add_paragraph()
add_styled_run(p, "2.4", FONTS["mono"], 11, True, TOKENS["orange"])
add_styled_run(p, "  TIMELINE & MILESTONES", FONTS["editorial"], 13, True, TOKENS["ivory"])

milestones = [
    ("1", "[milestoneone]", "[milestoneoneduedate]", "[milestoneonepaymentpercent]"),
    ("2", "[milestonetwo]", "[milestonetwoduedate]", "[milestonetwopaymentpercent]"),
    ("3", "[milestonethree]", "[milestonethreeduedate]", "[milestonethreepaymentpercent]"),
    ("4", "[milestonefour]", "[milestonefourduedate]", "[milestonefourpaymentpercent]"),
]

table = doc.add_table(rows=len(milestones)+1, cols=4)
table.alignment = WD_TABLE_ALIGNMENT.CENTER

# Header
headers = ["#", "MILESTONE DESCRIPTION", "DUE DATE", "PAYMENT %"]
for i, h in enumerate(headers):
    cell = table.cell(0, i)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 0 else WD_ALIGN_PARAGRAPH.LEFT
    add_styled_run(p, h, FONTS["editorial"], 9, True, TOKENS["muted"], letter_spacing=0.05)
    set_cell_shading(cell, SURFACE_DEEP_HEX)
    set_cell_border(cell,
        top=(4, "single", HAIRLINE_HEX),
        bottom=(4, "single", HAIRLINE_HEX),
        left=(4, "single", HAIRLINE_HEX),
        right=(4, "single", HAIRLINE_HEX),
    )

# Rows
for row_idx, (num, desc, date, pct) in enumerate(milestones, 1):
    for col_idx, val in enumerate([num, desc, date, pct]):
        cell = table.cell(row_idx, col_idx)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
        if col_idx == 0:
            add_styled_run(p, val, FONTS["mono"], 10, True, TOKENS["orange"])
        elif col_idx == 3:
            add_styled_run(p, val, FONTS["mono"], 10, False, TOKENS["orange"])
        else:
            add_styled_run(p, val, FONTS["mono"], 10, False, TOKENS["muted"])
        set_cell_shading(cell, CANVAS_HEX)
        set_cell_border(cell,
            top=(4, "single", HAIRLINE_HEX),
            bottom=(4, "single", HAIRLINE_HEX),
            left=(4, "single", HAIRLINE_HEX),
            right=(4, "single", HAIRLINE_HEX),
        )

# Column widths
widths = [Cm(1.2), Cm(9), Cm(4), Cm(3)]
for row in table.rows:
    for i, w in enumerate(widths):
        row.cells[i].width = w

p = doc.add_paragraph()
add_styled_run(p, "Note: Additional milestones may be added by mutual written agreement via Change Order.", FONTS["editorial"], 10, False, TOKENS["muted"], italic=True)

doc.add_page_break()

# ═══════════════════════════════════════════
# PAGE 4: RESPONSIBILITIES & PAYMENT
# ═══════════════════════════════════════════

p = doc.add_paragraph()
add_styled_run(p, "■", FONTS["mono"], 14, True, TOKENS["orange"])
add_styled_run(p, " 03  RESPONSIBILITIES & PAYMENT TERMS", FONTS["editorial"], 18, True, TOKENS["ivory"], letter_spacing=-0.01)
p.paragraph_format.space_before = Pt(0)
p.paragraph_format.space_after = Pt(12)
pPr = p._p.get_or_add_pPr()
pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="1" w:color="{HAIRLINE_HEX}"/></w:pBdr>')
pPr.append(pBdr)

# 3.1 Client Responsibilities
p = doc.add_paragraph()
add_styled_run(p, "3.1", FONTS["mono"], 11, True, TOKENS["orange"])
add_styled_run(p, "  CLIENT RESPONSIBILITIES", FONTS["editorial"], 13, True, TOKENS["ivory"])

client_resp = [
    "Provide all requested access, data, API keys, and materials in a timely manner.",
    "Designate a single point of contact for coordination.",
    "Review and approve deliverables promptly.",
    "Ensure all materials provided are lawful and non-infringing.",
    "Cooperate reasonably to avoid delays.",
]

for item in client_resp:
    p = doc.add_paragraph(style='List Bullet')
    p.clear()
    add_styled_run(p, item, FONTS["editorial"], 11, False, TOKENS["ivory_dark"])
    p.paragraph_format.left_indent = Cm(1)

doc.add_paragraph()

# 3.2 Freelancer Responsibilities
p = doc.add_paragraph()
add_styled_run(p, "3.2", FONTS["mono"], 11, True, TOKENS["orange"])
add_styled_run(p, "  FREELANCER RESPONSIBILITIES", FONTS["editorial"], 13, True, TOKENS["ivory"])

freelancer_resp = [
    "Perform Services consistent with industry standards and with reasonable skill and care.",
    "Remain responsible for the performance of any subcontractors used.",
    "Provide regular progress updates.",
]

for item in freelancer_resp:
    p = doc.add_paragraph(style='List Bullet')
    p.clear()
    add_styled_run(p, item, FONTS["editorial"], 11, False, TOKENS["ivory_dark"])
    p.paragraph_format.left_indent = Cm(1)

doc.add_paragraph()

# 3.3 Payment Terms
p = doc.add_paragraph()
add_styled_run(p, "3.3", FONTS["mono"], 11, True, TOKENS["orange"])
add_styled_run(p, "  PAYMENT TERMS", FONTS["editorial"], 13, True, TOKENS["ivory"])

payment_terms = [
    ("TOTAL FEE", "[Project.Fee]"),
    ("PAYMENT STRUCTURE", "[Milestone-based / upfront deposit + final payment]"),
    ("PAYMENT TERMS", "Net [X] days from invoice date"),
    ("LATE PAYMENT", "Freelancer may suspend work if payments are late beyond agreed terms."),
]

table = doc.add_table(rows=len(payment_terms), cols=2)
table.alignment = WD_TABLE_ALIGNMENT.CENTER

for i, (label, value) in enumerate(payment_terms):
    cell_l = table.cell(i, 0)
    cell_r = table.cell(i, 1)
    
    p = cell_l.paragraphs[0]
    add_styled_run(p, label, FONTS["editorial"], 10, True, TOKENS["muted"], letter_spacing=0.02)
    set_cell_shading(cell_l, SURFACE_DEEP_HEX)
    
    p = cell_r.paragraphs[0]
    add_styled_run(p, value, FONTS["mono"], 10, False, TOKENS["muted"])
    set_cell_shading(cell_r, SURFACE_DEEP_HEX)
    
    for cell in [cell_l, cell_r]:
        set_cell_border(cell,
            top=(4, "single", HAIRLINE_HEX),
            bottom=(4, "single", HAIRLINE_HEX),
            left=(4, "single", HAIRLINE_HEX),
            right=(4, "single", HAIRLINE_HEX),
        )

for row in table.rows:
    row.cells[0].width = Cm(5)
    row.cells[1].width = Cm(13)

doc.add_paragraph()

# 3.4 Post-Deployment Support
p = doc.add_paragraph()
add_styled_run(p, "3.4", FONTS["mono"], 11, True, TOKENS["orange"])
add_styled_run(p, "  POST-DEPLOYMENT SUPPORT & MAINTENANCE", FONTS["editorial"], 13, True, TOKENS["ivory"])

support_terms = [
    ("WARRANTY PERIOD", "[30/60/90] days post-deployment"),
    ("WARRANTY SCOPE", "Fix defects preventing the system from meeting functionality requirements, at no cost. Minor adjustments that do not materially alter scope included."),
    ("ONGOING MAINTENANCE (OPTIONAL)", "Available at Freelancer's then-current rates ([Ongoing.monthly.maintenance])"),
]

table = doc.add_table(rows=len(support_terms), cols=2)
table.alignment = WD_TABLE_ALIGNMENT.CENTER

for i, (label, value) in enumerate(support_terms):
    cell_l = table.cell(i, 0)
    cell_r = table.cell(i, 1)
    
    p = cell_l.paragraphs[0]
    add_styled_run(p, label, FONTS["editorial"], 10, True, TOKENS["muted"], letter_spacing=0.02)
    set_cell_shading(cell_l, SURFACE_DEEP_HEX)
    
    p = cell_r.paragraphs[0]
    add_styled_run(p, value, FONTS["editorial"], 10, False, TOKENS["ivory_dark"])
    set_cell_shading(cell_r, SURFACE_DEEP_HEX)
    
    for cell in [cell_l, cell_r]:
        set_cell_border(cell,
            top=(4, "single", HAIRLINE_HEX),
            bottom=(4, "single", HAIRLINE_HEX),
            left=(4, "single", HAIRLINE_HEX),
            right=(4, "single", HAIRLINE_HEX),
        )

for row in table.rows:
    row.cells[0].width = Cm(5)
    row.cells[1].width = Cm(13)

doc.add_page_break()

# ═══════════════════════════════════════════
# PAGE 5: MSA PART 1
# ═══════════════════════════════════════════

p = doc.add_paragraph()
add_styled_run(p, "■", FONTS["mono"], 14, True, TOKENS["orange"])
add_styled_run(p, " 04  PART 2: MASTER SERVICES AGREEMENT", FONTS["editorial"], 18, True, TOKENS["ivory"], letter_spacing=-0.01)
p.paragraph_format.space_before = Pt(0)
p.paragraph_format.space_after = Pt(12)
pPr = p._p.get_or_add_pPr()
pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="1" w:color="{HAIRLINE_HEX}"/></w:pBdr>')
pPr.append(pBdr)

p = doc.add_paragraph()
add_styled_run(p, "This MSA governs all services performed by Freelancer for Client across all current and future SOWs.", FONTS["editorial"], 11, False, TOKENS["ivory_dark"])

doc.add_paragraph()

msa_clauses_1 = [
    ("4.1", "TERM AND TERMINATION", [
        "This Agreement begins on the Effective Date and continues until terminated.",
        "Either party may terminate with 30 days written notice.",
        "Either party may terminate immediately for material breach, subject to a 10-day cure period.",
        "Upon termination, Client shall pay for all Services performed and deliverables accepted to date.",
    ]),
    ("4.2", "INTELLECTUAL PROPERTY", [
        "All pre-existing IP of Freelancer remains Freelancer's property.",
        "Upon full payment, deliverables created under this SOW transfer to Client.",
        "Freelancer retains the right to use non-confidential learnings, know-how, and methodologies developed during the engagement.",
    ]),
    ("4.3", "CONFIDENTIALITY", [
        "Both parties agree to protect and not disclose each other's confidential information except as required to perform this Agreement.",
        "Confidentiality obligations survive termination for 3 years.",
    ]),
    ("4.4", "CLIENT MATERIALS & COMPLIANCE", [
        "Client represents that any materials, data, or access it provides are lawful and do not infringe third-party rights.",
        "Client shall indemnify Freelancer against claims arising from Client-provided materials.",
    ]),
]

for num, title, items in msa_clauses_1:
    p = doc.add_paragraph()
    add_styled_run(p, num, FONTS["mono"], 11, True, TOKENS["orange"])
    add_styled_run(p, f"  {title}", FONTS["editorial"], 13, True, TOKENS["ivory"])
    
    for item in items:
        p = doc.add_paragraph(style='List Bullet')
        p.clear()
        add_styled_run(p, item, FONTS["editorial"], 11, False, TOKENS["ivory_dark"])
        p.paragraph_format.left_indent = Cm(1)
    
    doc.add_paragraph()

doc.add_page_break()

# ═══════════════════════════════════════════
# PAGE 6: MSA PART 2
# ═══════════════════════════════════════════

msa_clauses_2 = [
    ("4.5", "INDEPENDENT CONTRACTOR", [
        "Freelancer is an independent contractor, not an employee. Client shall not control how Freelancer performs the Services.",
        "No employment, partnership, or joint venture is created by this Agreement.",
    ]),
    ("4.6", "LIABILITY LIMITS", [
        "Freelancer's liability is capped at the total fees paid under the applicable SOW.",
        "Freelancer is not liable for indirect, incidental, or consequential damages (including lost profits, data loss, or business interruption).",
    ]),
    ("4.7", "INDEMNIFICATION", [
        "Client shall indemnify Freelancer against claims arising from Client's use of the deliverables, misuse, or violation of law.",
        "Freelancer shall indemnify Client against claims that Freelancer's work infringes third-party IP, provided Client used deliverables as intended.",
    ]),
    ("4.8", "NON-SOLICITATION", [
        "During the term and for 12 months thereafter, neither party shall solicit or hire the other's employees or contractors without written consent.",
    ]),
    ("4.9", "DISPUTE RESOLUTION", [
        "Parties shall first attempt to resolve disputes through good faith negotiation.",
        "If unresolved, disputes shall proceed to [mediation/arbitration] in [Jurisdiction].",
        "Governing law: [State/Country].",
    ]),
    ("4.10", "GENERAL PROVISIONS", [
        "This Agreement constitutes the entire agreement between the parties.",
        "Amendments must be in writing and signed by both parties.",
        "Notices shall be sent to the addresses listed on the cover page.",
        "Neither party may assign without the other's consent, except to successors.",
        "If any provision is found unenforceable, the remainder remains in effect.",
    ]),
]

for num, title, items in msa_clauses_2:
    p = doc.add_paragraph()
    add_styled_run(p, num, FONTS["mono"], 11, True, TOKENS["orange"])
    add_styled_run(p, f"  {title}", FONTS["editorial"], 13, True, TOKENS["ivory"])
    
    for item in items:
        p = doc.add_paragraph(style='List Bullet')
        p.clear()
        add_styled_run(p, item, FONTS["editorial"], 11, False, TOKENS["ivory_dark"])
        p.paragraph_format.left_indent = Cm(1)
    
    doc.add_paragraph()

doc.add_page_break()

# ═══════════════════════════════════════════
# PAGE 7: SIGNATURES
# ═══════════════════════════════════════════

p = doc.add_paragraph()
add_styled_run(p, "■", FONTS["mono"], 14, True, TOKENS["orange"])
add_styled_run(p, " 05  EXECUTION", FONTS["editorial"], 18, True, TOKENS["ivory"], letter_spacing=-0.01)
p.paragraph_format.space_before = Pt(0)
p.paragraph_format.space_after = Pt(12)
pPr = p._p.get_or_add_pPr()
pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="1" w:color="{HAIRLINE_HEX}"/></w:pBdr>')
pPr.append(pBdr)

p = doc.add_paragraph()
add_styled_run(p, "By signing below, both parties acknowledge they have read, understood, and agreed to the terms outlined in this Agreement, consisting of the Cover Page, the Statement of Work (Part 1), and the Master Services Agreement (Part 2).", FONTS["editorial"], 11, False, TOKENS["ivory_dark"])

doc.add_paragraph()
doc.add_paragraph()

# Signature table
table = doc.add_table(rows=1, cols=2)
table.alignment = WD_TABLE_ALIGNMENT.CENTER

for col_idx, party in enumerate(["FREELANCER / CONSULTANT", "CLIENT"]):
    cell = table.cell(0, col_idx)
    
    # Party label
    p = cell.paragraphs[0]
    add_styled_run(p, party, FONTS["editorial"], 10, True, TOKENS["muted"], letter_spacing=0.02)
    set_paragraph_spacing(p, 0, 4)
    
    # Fields
    fields = [
        ("Name:", "[Seller.FirstName] [Seller.LastName]" if col_idx == 0 else "[Buyer.FirstName] [Buyer.LastName]"),
        ("Title:", "[Seller.Title]" if col_idx == 0 else "[Buyer.Title]"),
        ("Company:", "[Seller.Company]" if col_idx == 0 else "[Buyer.Company]"),
    ]
    for label, value in fields:
        p = cell.add_paragraph()
        add_styled_run(p, label + " ", FONTS["editorial"], 10, True, TOKENS["ivory"])
        add_styled_run(p, value, FONTS["mono"], 10, False, TOKENS["muted"])
        set_paragraph_spacing(p, 1, 1)
    
    # Signature line
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(24)
    add_styled_run(p, "Signature: ________________________________________", FONTS["mono"], 10, False, TOKENS["muted"])
    
    p = cell.add_paragraph()
    add_styled_run(p, "Date: ________________________________________", FONTS["mono"], 10, False, TOKENS["muted"])
    
    set_cell_shading(cell, SURFACE_DEEP_HEX)
    set_cell_border(cell,
        top=(4, "single", HAIRLINE_HEX),
        bottom=(4, "single", HAIRLINE_HEX),
        left=(4, "single", HAIRLINE_HEX),
        right=(4, "single", HAIRLINE_HEX),
    )

table.cell(0, 0).width = Cm(9)
table.cell(0, 1).width = Cm(9)

doc.add_paragraph()
doc.add_paragraph()

# Document control
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
# Add top border
pPr = p._p.get_or_add_pPr()
pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="1" w:color="{ORANGE_HEX}"/></w:pBdr>')
pPr.append(pBdr)
add_styled_run(p, "DOCUMENT CONTROL", FONTS["editorial"], 9, True, TOKENS["orange"], letter_spacing=0.08)

p = doc.add_paragraph()
add_styled_run(p, "EMPATHOAI MSA/SOW TEMPLATE v1.0 // SOVEREIGN BRAND SYSTEM", FONTS["mono"], 8, False, TOKENS["muted"], letter_spacing=0.06)

p = doc.add_paragraph()
add_styled_run(p, "Generated from F:\\OS-EmpathoAI\\EMPATHOAI_BRAND_ASSETS\\05_TOKENS\\tokens.json", FONTS["mono"], 8, False, TOKENS["muted"], letter_spacing=0.06)

# ─── Save ───
output_path = r"F:\OS-EmpathoAI\EMPATHOAI_BRAND_ASSETS\04_TEMPLATES\EMPATHOAI_CONTRACT_TEMPLATE.docx"
doc.save(output_path)
print(f"✅ Contract DOCX generated: {output_path}")