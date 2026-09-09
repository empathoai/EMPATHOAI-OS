import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"F:\OS-EmpathoAI\EMPATHOAI_BRAND_ASSETS"
CACHE_DIR = os.path.join(BASE_DIR, "scripts", ".font_cache")
PNG_DIR = os.path.join(BASE_DIR, "01_LOGO", "PNG")
MASTER_DIR = os.path.join(BASE_DIR, "01_LOGO", "MASTER")

os.makedirs(PNG_DIR, exist_ok=True)
os.makedirs(MASTER_DIR, exist_ok=True)

ibm_ttf = os.path.join(CACHE_DIR, "IBMPlexSans-Bold.ttf")
inter_ttf = os.path.join(CACHE_DIR, "Inter-Bold.ttf")

def render_master_logo(cap_height=120, is_dark=True, transparent=False, pad_x=80, pad_y=50):
    # Calibrate font size so flat H ink height equals cap_height
    # In IBM Plex Sans Bold and Inter Bold, let's find the exact font size
    test_img = Image.new("RGBA", (1000, 1000), (0,0,0,0))
    test_draw = ImageDraw.Draw(test_img)
    
    # Binary search font size for IBM Plex Sans
    size_ibm = cap_height * 1.4
    font_ibm = ImageFont.truetype(ibm_ttf, int(size_ibm))
    bbox_h = test_draw.textbbox((0, 0), "H", font=font_ibm)
    h_height = bbox_h[3] - bbox_h[1]
    scale_ibm = cap_height / h_height
    font_ibm = ImageFont.truetype(ibm_ttf, int(size_ibm * scale_ibm))
    
    # Binary search font size for Inter
    size_inter = cap_height * 1.4
    font_inter = ImageFont.truetype(inter_ttf, int(size_inter))
    bbox_h_inter = test_draw.textbbox((0, 0), "H", font=font_inter)
    h_height_inter = bbox_h_inter[3] - bbox_h_inter[1]
    scale_inter = cap_height / h_height_inter
    font_inter = ImageFont.truetype(inter_ttf, int(size_inter * scale_inter))
    
    # Colors
    bg_color = (0, 0, 0, 0) if transparent else ((10, 10, 11, 255) if is_dark else (255, 255, 255, 255))
    text_color = (245, 245, 245, 255) if is_dark else (10, 10, 11, 255)
    orange_color = (255, 68, 2, 255)
    
    # Dimensions & Spacing
    sq_size = cap_height
    sq_e_gap = int(0.31 * cap_height)
    a_i_gap = int(0.115 * cap_height)
    
    # Bounding boxes for text
    bbox_empathoa = test_draw.textbbox((0, 0), "EMPATHOA", font=font_ibm)
    empathoa_w = bbox_empathoa[2] - bbox_empathoa[0]
    
    bbox_i = test_draw.textbbox((0, 0), "I", font=font_inter)
    i_w = bbox_i[2] - bbox_i[0]
    
    total_w = pad_x * 2 + sq_size + sq_e_gap + empathoa_w + a_i_gap + i_w
    total_h = pad_y * 2 + cap_height
    
    img = Image.new("RGBA", (total_w, total_h), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw Signal Square
    sq_x0 = pad_x
    sq_y0 = pad_y
    draw.rectangle([sq_x0, sq_y0, sq_x0 + sq_size, sq_y0 + sq_size], fill=orange_color)
    
    # Draw EMPATHOA
    # Align ink top to pad_y
    text_x = sq_x0 + sq_size + sq_e_gap - bbox_empathoa[0]
    text_y = pad_y - bbox_empathoa[1]
    draw.text((text_x, text_y), "EMPATHOA", font=font_ibm, fill=text_color)
    
    # Draw Terminal I
    i_x = text_x + bbox_empathoa[2] + a_i_gap - bbox_i[0]
    i_y = pad_y - bbox_i[1]
    draw.text((i_x, i_y), "I", font=font_inter, fill=text_color)
    
    return img

configs = [
    ("empathoai-master-logo-dark.png", True, False, 140),
    ("empathoai-master-logo-light.png", False, False, 140),
    ("empathoai-master-logo-dark-trans.png", True, True, 140),
    ("empathoai-master-logo-light-trans.png", False, True, 140),
    ("empathoai-master-logo-dark-512.png", True, False, 70),
    ("empathoai-master-logo-light-512.png", False, False, 70),
    ("empathoai-master-logo-dark-trans-512.png", True, True, 70),
    ("empathoai-master-logo-light-trans-512.png", False, True, 70),
]

for fname, dark, trans, cap in configs:
    img = render_master_logo(cap_height=cap, is_dark=dark, transparent=trans)
    target_path = os.path.join(PNG_DIR, fname)
    img.save(target_path, "PNG")
    # Also save master variants to MASTER
    if "512" not in fname:
        img.save(os.path.join(MASTER_DIR, fname), "PNG")
    print(f"Generated {fname} ({img.width}x{img.height})")

print("All master wordmark PNGs rendered perfectly.")
