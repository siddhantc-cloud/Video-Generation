# Caricature Prompts — Modi, Shah, Kejriwal (So Sorry house style)

> Ready-to-use master-sheet prompts for the three caricatures. Generator-agnostic: paste into the Higgsfield UI, run via MCP `generate_image` (model `nano_banana_pro`, ~2 cr), or any image tool. For best fidelity, attach **1 real So Sorry frame** (in `refs/`) as a STYLE reference and keep the style-ref sentence.
>
> Aspect ratio: **3:4** (portrait, full-body). Background: plain white studio. One figure per image.

## STYLE BLOCK (already embedded in each prompt below)
*3D-rendered politoon caricature in the India Today "So Sorry" house style — heavily exaggerated oversized head on a smaller body, smooth stylized 3D surfacing, clean bright even studio lighting, bold saturated colors, crisp readable silhouette, expressive comedic features.*

---

## 1 · MODI — master sheet
> *Full-body 3D politoon caricature of Indian PM Narendra Modi in the India Today "So Sorry" cartoon style: heavily exaggerated oversized head on a smaller body, round face, full white beard, white side-parted hair, glasses, dignified saffron-and-white kurta with a sleeveless jacket. Smooth stylized 3D render, bright even studio lighting, bold saturated colors, crisp silhouette, gentle confident smile. Neutral standing pose (T-pose friendly), plain white studio background, high detail. `<<<style_frame>>>` is the STYLE reference ONLY — match its 3D render finish, head-to-body ratio, and lighting; do NOT copy its subject.*

## 2 · AMIT SHAH — master sheet
> *Full-body 3D politoon caricature of Amit Shah in the India Today "So Sorry" cartoon style: heavily exaggerated oversized head on a stocky smaller body, bald crown with short grey side hair, clean-shaven, glasses, white kurta with a dark sleeveless waistcoat. Shrewd, calculating "strategist" expression — slight knowing smirk. Smooth stylized 3D render, bright even studio lighting, bold saturated colors, crisp silhouette. Neutral standing pose, plain white studio background, high detail. `<<<style_frame>>>` is the STYLE reference ONLY — match its render finish, proportions, lighting; do NOT copy its subject.*

## 3 · KEJRIWAL — master sheet
> *Full-body 3D politoon caricature of Arvind Kejriwal in the India Today "So Sorry" cartoon style: heavily exaggerated oversized head on an ordinary everyman body, black mustache, glasses, simple grey V-neck sweater over a collared shirt, a muffler around the neck, slightly earnest expression. Smooth stylized 3D render, bright even studio lighting, bold saturated colors, crisp silhouette. Neutral standing pose, plain white studio background, high detail. `<<<style_frame>>>` is the STYLE reference ONLY — match its render finish, proportions, lighting; do NOT copy its subject.*

---

## MCP call template (per figure)
```
generate_image params: {
  "model": "nano_banana_pro",
  "prompt": "<one of the prompts above>",
  "aspect_ratio": "3:4",
  "medias": [{ "role": "image", "value": "<style_frame_uuid_or_url>" }]
}
```
*(Run `get_cost: true` first to preflight — ~2 cr each.)*

## Expression add-on (after the master passes — edit from the master, keep face identical)
> *Expression sheet — the SAME character from `<<<master>>>`, identical design and proportions, four expressions in a grid: (1) neutral, (2) sneaky scheming grin, (3) wide-eyed comic shock, (4) dazed/defeated with swirly eyes. Plain white background, consistent lighting. Keep face structure identical across all four.*

## Notes
- These caricature their real public-figure likenesses — standard political-cartoon satire (the So Sorry premise). For the private showcase this is fine.
- If a generator refuses "named politician," drop the name and describe by features only (the descriptors above are already feature-complete) — the caricature still reads.
- Once a master is approved, derive the **turnaround** (Higgsfield Angles or a four-view prompt) and register each as an `@tag` for the beat-board and the Seedance shot.
