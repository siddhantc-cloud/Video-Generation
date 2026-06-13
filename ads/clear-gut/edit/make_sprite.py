# -*- coding: utf-8 -*-
# Build a "glowing product" sprite: real bottle cut-out on a soft warm-golden
# radial halo. The halo masks the AI bottle behind it and blends into the warm scenes.
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

bottle = Image.open("edit/product_cutout.png").convert("RGBA")
bw, bh = bottle.size

# Canvas generously larger than the bottle so the glow fades to 0 well inside the edges
CW, CH = int(bw*2.6), int(bh*1.7)
canvas = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))

# --- warm radial glow: small-ish ellipse + heavy blur => clean oval, transparent margin (no box) ---
glow_alpha = Image.new("L", (CW, CH), 0)
d = ImageDraw.Draw(glow_alpha)
cx, cy = CW//2, CH//2
ew, eh = int(CW*0.30), int(CH*0.33)
d.ellipse([cx-ew, cy-eh, cx+ew, cy+eh], fill=205)
glow_alpha = glow_alpha.filter(ImageFilter.GaussianBlur(CW*0.135))
glow = Image.new("RGBA", (CW, CH), (255, 198, 100, 0))   # warm gold
glow.putalpha(glow_alpha)
canvas = Image.alpha_composite(canvas, glow)

# --- bottle, centered, sized so a tasteful halo remains around it ---
target_h = int(CH*0.74)
scale = target_h / bh
nb = bottle.resize((int(bw*scale), target_h), Image.LANCZOS)
canvas.alpha_composite(nb, ((CW-nb.size[0])//2, (CH-nb.size[1])//2))

canvas.save("edit/product_sprite.png")
print("sprite", canvas.size, "bottle scaled to h=", target_h)
