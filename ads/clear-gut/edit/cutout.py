# -*- coding: utf-8 -*-
# Cut the real bottle out of its white product-sheet background WITHOUT removing
# the white label/dropper: flood-fill the background inward from the borders only.
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from scipy import ndimage

src = Image.open("edit/front_crop.png").convert("RGB")
w, h = src.size
SENT = (255, 0, 255)  # magenta sentinel = "this is background"
work = src.copy()

# Seed flood-fill from many border points so the whole outer white is caught.
seeds = []
for x in range(0, w, 12):
    seeds += [(x, 0), (x, h - 1)]
for y in range(0, h, 12):
    seeds += [(0, y), (w - 1, y)]
for sx, sy in seeds:
    r, g, b = work.getpixel((sx, sy))
    if r > 215 and g > 215 and b > 215:           # only start on near-white
        ImageDraw.floodfill(work, (sx, sy), SENT, thresh=22)

arr = np.array(work)
bg = np.all(arr == np.array(SENT), axis=-1)        # True where background (exterior only)
# Fill any interior holes: a pixel is foreground unless it's background CONNECTED to the border.
fg = ~bg
fg = ndimage.binary_fill_holes(fg)                 # close holes the flood-fill punched in the label
alpha = np.where(fg, 255, 0).astype("uint8")

rgba = np.dstack([np.array(src), alpha])
out = Image.fromarray(rgba, "RGBA")
# Feather the alpha edge slightly for clean compositing
a = out.split()[3].filter(ImageFilter.GaussianBlur(0.8))
out.putalpha(a)
out.save("edit/product_cutout.png")

cov = 100.0 * (alpha > 0).sum() / alpha.size
print(f"cutout saved {w}x{h}; opaque coverage = {cov:.1f}%")
