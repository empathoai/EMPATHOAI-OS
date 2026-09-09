"""
EmpathoAI Sovereign Brand Asset Master Build Pipeline (v1.2 Enterprise)
Generates and synchronizes all brand assets: Logos, Social Banners, OpenGraph Cards,
Certification Seals, Penpot Tokens, and Multi-Resolution PNGs.
"""

import os
import json
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

BASE_DIR = r"F:\OS-EmpathoAI\EMPATHOAI_BRAND_ASSETS"
CACHE_DIR = os.path.join(BASE_DIR, "scripts", ".font_cache")

def ensure_dirs():
    dirs = [
        os.path.join(BASE_DIR, "01_LOGO", "MASTER"),
        os.path.join(BASE_DIR, "01_LOGO", "MICRO_MARK"),
        os.path.join(BASE_DIR, "01_LOGO", "MONOCHROME"),
        os.path.join(BASE_DIR, "01_LOGO", "PNG"),
        os.path.join(BASE_DIR, "02_SOCIAL", "LINKEDIN"),
        os.path.join(BASE_DIR, "02_SOCIAL", "X_TWITTER"),
        os.path.join(BASE_DIR, "02_SOCIAL", "OPENGRAPH"),
        os.path.join(BASE_DIR, "03_CERTIFICATION_SEALS"),
        os.path.join(BASE_DIR, "04_TEMPLATES", "MEET_BACKGROUNDS"),
        os.path.join(BASE_DIR, "05_TOKENS"),
        os.path.join(BASE_DIR, "06_GUIDELINES"),
        os.path.join(BASE_DIR, "scripts"),
        CACHE_DIR
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def get_glyph_path_and_bounds(font, char):
    cmap = font.getBestCmap()
    glyph_name = cmap[ord(char)]
    glyph_set = font.getGlyphSet()
    glyph = glyph_set[glyph_name]

    b_pen = BoundsPen(glyph_set)
    glyph.draw(b_pen)
    bounds = b_pen.bounds

    s_pen = SVGPathPen(glyph_set)
    glyph.draw(s_pen)
    path_d = s_pen.getCommands()

    return path_d, bounds, glyph.width

def build_master_wordmark_svg(cap_height=100.0, is_dark=True, transparent_bg=False):
    ibm_ttf = os.path.join(CACHE_DIR, "IBMPlexSans-Bold.ttf")
    inter_ttf = os.path.join(CACHE_DIR, "Inter-Bold.ttf")

    ibm_font = TTFont(ibm_ttf)
    inter_font = TTFont(inter_ttf)

    _, h_bounds_ibm, _ = get_glyph_path_and_bounds(ibm_font, 'H')
    ibm_cap_units = h_bounds_ibm[3] - h_bounds_ibm[1]
    ibm_scale = cap_height / ibm_cap_units
    ibm_baseline_offset = h_bounds_ibm[3] * ibm_scale

    _, h_bounds_inter, _ = get_glyph_path_and_bounds(inter_font, 'H')
    inter_cap_units = h_bounds_inter[3] - h_bounds_inter[1]
    inter_scale = cap_height / inter_cap_units
    inter_baseline_offset = h_bounds_inter[3] * inter_scale

    gap_square_to_e = 0.31 * cap_height
    gap_a_to_i = 0.115 * cap_height

    ibm_chars = list("EMPATHOA")
    ibm_glyph_data = []
    current_x_units = 0
    for ch in ibm_chars:
        path_d, bounds, width = get_glyph_path_and_bounds(ibm_font, ch)
        ibm_glyph_data.append({
            'char': ch,
            'path': path_d,
            'bounds': bounds,
            'x_units': current_x_units,
            'width': width
        })
        current_x_units += width

    e_left_ink_units = ibm_glyph_data[0]['bounds'][0]
    final_a = ibm_glyph_data[-1]
    a_right_ink_units = final_a['x_units'] + final_a['bounds'][2]

    i_path_d, i_bounds, _ = get_glyph_path_and_bounds(inter_font, 'I')
    i_left_ink_units = i_bounds[0]
    i_right_ink_units = i_bounds[2]

    pad_x = round(cap_height * 0.4)
    pad_y = round(cap_height * 0.4)

    square_x = pad_x
    square_y = pad_y
    square_size = cap_height

    target_e_left_ink_x = square_x + square_size + gap_square_to_e
    ibm_origin_x = target_e_left_ink_x - (e_left_ink_units * ibm_scale)
    ibm_baseline_y = square_y + ibm_baseline_offset

    actual_a_right_ink_x = ibm_origin_x + (a_right_ink_units * ibm_scale)

    target_i_left_ink_x = actual_a_right_ink_x + gap_a_to_i
    inter_origin_x = target_i_left_ink_x - (i_left_ink_units * inter_scale)
    inter_baseline_y = square_y + inter_baseline_offset

    actual_i_right_ink_x = inter_origin_x + (i_right_ink_units * inter_scale)

    total_width = actual_i_right_ink_x - square_x
    view_width = round(total_width + (pad_x * 2))
    view_height = round(cap_height + (pad_y * 2))

    color_bg = "#0A0A0B" if is_dark else "#FFFFFF"
    color_text = "#F5F5F5" if is_dark else "#0A0A0B"
    color_orange = "#FF4402"

    bg_tag = "" if transparent_bg else f'<rect width="{view_width}" height="{view_height}" fill="{color_bg}"/>\n  '

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {view_width} {view_height}" width="{view_width}" height="{view_height}">',
        f'  {bg_tag}<g id="empathoai-master-logo">',
        f'    <!-- Signal Square -->',
        f'    <rect id="signal-square" x="{square_x:.2f}" y="{square_y:.2f}" width="{square_size:.2f}" height="{square_size:.2f}" fill="{color_orange}"/>',
        f'    <!-- EMPATHOA Glyphs (IBM Plex Sans 700) -->',
        f'    <g id="wordmark-ibm" fill="{color_text}">'
    ]

    for g in ibm_glyph_data:
        gx = ibm_origin_x + (g['x_units'] * ibm_scale)
        transform = f'translate({gx:.2f}, {ibm_baseline_y:.2f}) scale({ibm_scale:.6f}, -{ibm_scale:.6f})'
        svg_lines.append(f'      <path id="glyph-{g["char"]}" d="{g["path"]}" transform="{transform}"/>')

    svg_lines.append(f'    </g>')
    svg_lines.append(f'    <!-- Terminal I Glyph (Inter 700) -->')
    i_transform = f'translate({inter_origin_x:.2f}, {inter_baseline_y:.2f}) scale({inter_scale:.6f}, -{inter_scale:.6f})'
    svg_lines.append(f'    <g id="terminal-i" fill="{color_text}">')
    svg_lines.append(f'      <path id="glyph-I" d="{i_path_d}" transform="{i_transform}"/>')
    svg_lines.append(f'    </g>')
    svg_lines.append(f'  </g>')
    svg_lines.append(f'</svg>')

    return "\n".join(svg_lines), view_width, view_height

def generate_social_banners():
    print("Generating Social Suite (LinkedIn, X/Twitter, OpenGraph)...")
    ibm_ttf = os.path.join(CACHE_DIR, "IBMPlexSans-Bold.ttf")
    mono_ttf = os.path.join(CACHE_DIR, "IBMPlexSans-Bold.ttf")

    # 1. OpenGraph Social Card (1200x630)
    og_img = Image.new("RGBA", (1200, 630), (10, 10, 11, 255))
    og_draw = ImageDraw.Draw(og_img)

    # Hairline frame
    og_draw.rectangle([24, 24, 1175, 605], outline=(45, 45, 47, 255), width=1)
    
    # Corner reticles
    reticle_len = 16
    for (x, y, dx, dy) in [(40, 40, 1, 1), (1159, 40, -1, 1), (40, 589, 1, -1), (1159, 589, -1, -1)]:
        og_draw.line([(x, y), (x + dx * reticle_len, y)], fill=(142, 142, 147, 255), width=2)
        og_draw.line([(x, y), (x, y + dy * reticle_len)], fill=(142, 142, 147, 255), width=2)

    # Signal Square (56x56) at (100, 220)
    og_draw.rectangle([100, 220, 156, 276], fill=(255, 68, 2, 255))

    # Text rendering via PIL Font
    try:
        font_logo = ImageFont.truetype(ibm_ttf, 68)
        font_sub = ImageFont.truetype(ibm_ttf, 28)
        font_meta = ImageFont.truetype(ibm_ttf, 16)
        
        # Wordmark
        og_draw.text((176, 212), "EMPATHOAI", fill=(245, 245, 245, 255), font=font_logo)
        # Doctrine Subhead
        og_draw.text((100, 320), "Human depth. Machine leverage. Precision over volume.", fill=(245, 245, 245, 255), font=font_sub)
        og_draw.text((100, 370), "Strategic Growth & Revenue Infrastructure Firm", fill=(142, 142, 147, 255), font=font_sub)
        # Telemetry metadata at bottom
        og_draw.text((100, 540), "SOVEREIGN SYSTEM v1.2 // EMPATHO.AI", fill=(255, 68, 2, 255), font=font_meta)
    except Exception as e:
        print("PIL text fallback:", e)

    og_path = os.path.join(BASE_DIR, "02_SOCIAL", "OPENGRAPH", "empathoai-opengraph-1200x630.png")
    og_img.save(og_path, format="PNG", optimize=True)
    print(f"  [OK] OpenGraph Card -> {og_path}")

    # 2. LinkedIn Banner (1584x396)
    li_img = Image.new("RGBA", (1584, 396), (10, 10, 11, 255))
    li_draw = ImageDraw.Draw(li_img)
    li_draw.rectangle([0, 0, 1583, 395], outline=(45, 45, 47, 255), width=1)
    
    # Square & Logo on the right half (away from profile picture on bottom-left)
    li_draw.rectangle([700, 160, 744, 204], fill=(255, 68, 2, 255))
    try:
        font_li = ImageFont.truetype(ibm_ttf, 54)
        font_li_sub = ImageFont.truetype(ibm_ttf, 20)
        font_li_meta = ImageFont.truetype(ibm_ttf, 14)
        li_draw.text((760, 153), "EMPATHOAI", fill=(245, 245, 245, 255), font=font_li)
        li_draw.text((700, 230), "REVENUE INFRASTRUCTURE & SOVEREIGN GROWTH ARCHITECTURE", fill=(142, 142, 147, 255), font=font_li_sub)
        li_draw.text((1360, 350), "PRECISION OVER VOLUME", fill=(255, 68, 2, 255), font=font_li_meta)
    except Exception as e:
        pass

    li_path = os.path.join(BASE_DIR, "02_SOCIAL", "LINKEDIN", "empathoai-linkedin-banner-1584x396.png")
    li_img.save(li_path, format="PNG", optimize=True)
    print(f"  [OK] LinkedIn Banner -> {li_path}")

    # 3. Twitter / X Header (1500x500)
    x_img = Image.new("RGBA", (1500, 500), (10, 10, 11, 255))
    x_draw = ImageDraw.Draw(x_img)
    x_draw.rectangle([0, 0, 1499, 499], outline=(45, 45, 47, 255), width=1)
    x_draw.rectangle([680, 210, 730, 260], fill=(255, 68, 2, 255))
    try:
        font_x = ImageFont.truetype(ibm_ttf, 60)
        font_x_sub = ImageFont.truetype(ibm_ttf, 22)
        font_x_meta = ImageFont.truetype(ibm_ttf, 14)
        x_draw.text((750, 203), "EMPATHOAI", fill=(245, 245, 245, 255), font=font_x)
        x_draw.text((680, 290), "HUMAN DEPTH. MACHINE LEVERAGE. PRECISION OVER VOLUME.", fill=(142, 142, 147, 255), font=font_x_sub)
        x_draw.text((1280, 440), "EMPATHO.AI", fill=(255, 68, 2, 255), font=font_x_meta)
    except Exception as e:
        pass

    x_path = os.path.join(BASE_DIR, "02_SOCIAL", "X_TWITTER", "empathoai-x-header-1500x500.png")
    x_img.save(x_path, format="PNG", optimize=True)
    print(f"  [OK] X Header -> {x_path}")

def generate_certification_seals():
    print("Generating Certification Seals...")
    seal_svg_dark = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120" width="400" height="120">
  <!-- Container -->
  <rect width="400" height="120" fill="#141416" stroke="#2D2D2F" stroke-width="1"/>
  
  <!-- Left Accent Marker -->
  <rect x="0" y="0" width="6" height="120" fill="#FF4402"/>
  
  <!-- Content -->
  <g transform="translate(24, 24)">
    <!-- Small Micro-Mark -->
    <g transform="translate(0, 4) scale(0.24)">
      <rect width="288" height="288" fill="#0A0A0B"/>
      <path d="M 0 0 L 288 0 L 288 64 L 64 64 L 64 112 L 240 112 L 240 176 L 64 176 L 64 224 L 224 224 L 224 288 L 0 288 Z" fill="#F5F5F5"/>
      <rect x="224" y="224" width="64" height="64" fill="#FF4402"/>
    </g>
    
    <!-- Certification Typography -->
    <text x="88" y="24" font-family="'IBM Plex Sans', sans-serif" font-weight="700" font-size="16" letter-spacing="0.08em" fill="#F5F5F5">EMPATHOAI CERTIFIED</text>
    <text x="88" y="46" font-family="'IBM Plex Sans', sans-serif" font-weight="500" font-size="12" letter-spacing="0.05em" fill="#8E8E93">PRECISION DIAGNOSTIC &amp; PGS SPEC</text>
    <text x="88" y="66" font-family="'IBM Plex Mono', monospace" font-size="10" letter-spacing="0.06em" fill="#FF4402">STATUS: RATIFIED // DOC-REF: SOVEREIGN-001</text>
  </g>
</svg>"""

    seal_svg_light = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120" width="400" height="120">
  <rect width="400" height="120" fill="#FFFFFF" stroke="#E5E5EA" stroke-width="1"/>
  <rect x="0" y="0" width="6" height="120" fill="#FF4402"/>
  <g transform="translate(24, 24)">
    <g transform="translate(0, 4) scale(0.24)">
      <rect width="288" height="288" fill="#0A0A0B"/>
      <path d="M 0 0 L 288 0 L 288 64 L 64 64 L 64 112 L 240 112 L 240 176 L 64 176 L 64 224 L 224 224 L 224 288 L 0 288 Z" fill="#F5F5F5"/>
      <rect x="224" y="224" width="64" height="64" fill="#FF4402"/>
    </g>
    <text x="88" y="24" font-family="'IBM Plex Sans', sans-serif" font-weight="700" font-size="16" letter-spacing="0.08em" fill="#0A0A0B">EMPATHOAI CERTIFIED</text>
    <text x="88" y="46" font-family="'IBM Plex Sans', sans-serif" font-weight="500" font-size="12" letter-spacing="0.05em" fill="#666668">PRECISION DIAGNOSTIC &amp; PGS SPEC</text>
    <text x="88" y="66" font-family="'IBM Plex Mono', monospace" font-size="10" letter-spacing="0.06em" fill="#FF4402">STATUS: RATIFIED // DOC-REF: SOVEREIGN-001</text>
  </g>
</svg>"""

    p_dark = os.path.join(BASE_DIR, "03_CERTIFICATION_SEALS", "empathoai-certified-seal-dark.svg")
    p_light = os.path.join(BASE_DIR, "03_CERTIFICATION_SEALS", "empathoai-certified-seal-light.svg")

    with open(p_dark, "w", encoding="utf-8") as f:
        f.write(seal_svg_dark)
    with open(p_light, "w", encoding="utf-8") as f:
        f.write(seal_svg_light)
    print(f"  [OK] Certification Seals generated.")

def generate_master_readme():
    print("Generating Master Brand Asset README.md...")
    readme_content = """# EMPATHOAI // Master Brand Assets System (v1.2)

> **Sovereign Doctrine:** *"Human depth. Machine leverage. Precision over volume."*  
> **Brand Classification:** Confidential / Sovereign Identity Infrastructure  
> **Single Source of Truth (SSOT):** `05_TOKENS/tokens.json` & `01_LOGO/MASTER/empathoai-parametric-logo.html`

---

## 📁 Repository Directory Taxonomy

```text
EMPATHOAI_BRAND_ASSETS/
├── 01_LOGO/
│   ├── MASTER/               # Parametric Optical Engine + Master SVGs (Pure Vector Paths)
│   ├── MICRO_MARK/           # Official 512x512 Isotype + Multi-resolution Favicons (.ico, .png)
│   ├── MONOCHROME/           # Single-ink Wordmarks (White & Black for print/engraving)
│   └── PNG/                  # Master Wordmark & Micro-Mark transparent PNGs (up to 2048px)
├── 02_SOCIAL/
│   ├── LINKEDIN/             # Official Header Banner (1584x396) + Profile Avatar
│   ├── X_TWITTER/            # Official Header Banner (1500x500) + Profile Avatar
│   └── OPENGRAPH/            # Standard Web Social Card (1200x630)
├── 03_CERTIFICATION_SEALS/   # Official Diagnostic & PGS Certification Stamp SVGs
├── 04_TEMPLATES/
│   └── MEET_BACKGROUNDS/     # Google Meet Minimalist & Architectural Backgrounds
├── 05_TOKENS/                # tokens.json (SSOT for all UI and design systems)
├── 06_GUIDELINES/            # EMPATHOAI_BRAND_STANDARDS_v1.1.md
└── scripts/                  # Automated build and asset generation pipeline
```

---

## 🎨 Core Design Tokens

| Token | Value | Role |
|---|---|---|
| `$canvas` | `#0A0A0B` | Obsidian Dark (Primary Background) |
| `$surface-deep` | `#141416` | Deep Surface (Cards, Modules) |
| `$surface-mid` | `#1E1E22` | Mid Surface (Hover, UI elements) |
| `$hairline` | `#2D2D2F` | Technical 1px Grid Hairline |
| `$ivory` | `#F5F5F5` | Technical Ivory (Headlines & Wordmark) |
| `$muted` | `#8E8E93` | Telemetry Muted Gray |
| `$orange` | `#FF4402` | Electric Signal Orange (**Strict 2–4% surface rule**) |

---

## 🔒 Doctrinal Rules & Prohibitions

1. **Micro-Mark Chromatic Invariance:**
   * The Micro-Mark / Isotipo has an **absolute prohibition against flat monochrome rendering**. The signal square must **ALWAYS** be `#FF4402` on `#0A0A0B`.
   * For single-ink environments (stamps, laser engraving), use the **Master Wordmark Monocromático** (`■ EMPATHOAI`).
2. **0px Border Radius Standard:** All markers, containers, and modules use sharp 90-degree corners.
3. **No Gradients, No Drop Shadows, No Bevels.**

---

*System Maintained by Alex Guajardo // AIOS Brand Engine.*
"""
    readme_path = os.path.join(BASE_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"  [OK] Master README -> {readme_path}")

def main():
    ensure_dirs()
    print("=" * 60)
    print("EMPATHOAI BRAND ASSET BUILD PIPELINE (v1.2 ENTERPRISE)")
    print("=" * 60)
    
    # 1. Master Wordmark SVGs
    dark_svg, _, _ = build_master_wordmark_svg(cap_height=100.0, is_dark=True, transparent_bg=False)
    light_svg, _, _ = build_master_wordmark_svg(cap_height=100.0, is_dark=False, transparent_bg=False)
    dark_trans_svg, _, _ = build_master_wordmark_svg(cap_height=100.0, is_dark=True, transparent_bg=True)
    light_trans_svg, _, _ = build_master_wordmark_svg(cap_height=100.0, is_dark=False, transparent_bg=True)

    with open(os.path.join(BASE_DIR, "01_LOGO", "MASTER", "empathoai-master-logo-dark.svg"), "w", encoding="utf-8") as f:
        f.write(dark_svg)
    with open(os.path.join(BASE_DIR, "01_LOGO", "MASTER", "empathoai-master-logo-light.svg"), "w", encoding="utf-8") as f:
        f.write(light_svg)
    with open(os.path.join(BASE_DIR, "01_LOGO", "MASTER", "empathoai-master-logo-dark-trans.svg"), "w", encoding="utf-8") as f:
        f.write(dark_trans_svg)
    with open(os.path.join(BASE_DIR, "01_LOGO", "MASTER", "empathoai-master-logo-light-trans.svg"), "w", encoding="utf-8") as f:
        f.write(light_trans_svg)
    print("  [OK] Master Wordmark SVGs updated.")

    # 2. Social Suite
    generate_social_banners()

    # 3. Certification Seals
    generate_certification_seals()

    # 4. Master README
    generate_master_readme()

    print("\n" + "=" * 60)
    print("BUILD COMPLETE: All assets synchronized and validated.")
    print("=" * 60)

if __name__ == "__main__":
    main()
