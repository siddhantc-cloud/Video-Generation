# V1 “The Freebie Trap” — Generation Prompts (all steps)

> Copy-paste-ready prompts for every generation step, with the MCP call and CLI equivalent. Apply the gates/QC in `production.md`.
>
> **Before running:** (1) **add credits** — account is at 0 (free plan); Seedance 14s = 63 cr, so budget accordingly. (2) **Drop 8–15 real So Sorry frames** into `bible/refs/` and upload them (`media_upload`) — they're the STYLE references that make this read as So Sorry.
>
> **Real per-job costs (confirmed via `get_cost`):** image (nano_banana_pro 1k) = **2 cr** · Kling 3.0 5s = **10 cr** · Seedance 2.0 14s/720p = **63 cr**.

---

## How to run each prompt

- **MCP:** `generate_image` / `generate_video` with the `params` block shown. Set `get_cost: true` first to preflight, then remove it to submit. Reference prior outputs by their returned `job_id`, uploaded files by `media_upload` UUID, or an `https://` URL — in the `medias[]` array with the right `role`.
- **CLI:** `higgsfield generate create <model> --prompt "<text>" [--start-image <id> --end-image <id> ...]`. Use `higgsfield model get <model>` for exact flags.
- **Style-ref rule:** when a real So Sorry frame supplies the *look* (not a character), say so verbatim in the prompt: *"`<<<style_frame>>>` is the STYLE reference ONLY — match its render finish, proportions, lighting; do NOT copy its subject."*

---

## GLOBAL STYLE BLOCK  *(prepend to every image prompt; calibrate against the real frames first)*

> **So Sorry house style:** 3D-rendered politoon caricature — heavily exaggerated **oversized head on a smaller body**, smooth stylized 3D surfacing, clean bright even studio lighting, bold saturated colors, crisp readable silhouettes, expressive cartoon features. Match the render finish, head-to-body ratio, and lighting of `<<<style_frame>>>`.

*(After 2.2 you replace the bracketed adjectives with whatever the real frames actually show — glossiness, palette, edge treatment.)*

---

## PHASE 2 — ASSET BIBLE

> Model for all sheets: **`nano_banana_pro`** (2 cr, high detail, handles text/labels). Pass a real So Sorry frame as a STYLE-only media. Generate → **Read & QC** → if a detail is off, **edit in place** (re-call with the prior `job_id` as `medias` + a targeted edit instruction), don't regenerate from scratch.

### 2.3–2.5 · Character master sheets (run per figure)

**MODI — master sheet**
> *[GLOBAL STYLE BLOCK] Full-body character sheet of a caricatured politoon of Narendra Modi: elderly Indian man, exaggerated oversized head, round face, full white beard, white side-parted hair, glasses, dignified saffron-and-white kurta. Neutral standing pose, T-pose-friendly, plain white studio background, soft even lighting, high detail. `<<<style_frame>>>` = STYLE reference only — match its 3D render look; do NOT copy its subject.*
```
generate_image params: { "model":"nano_banana_pro",
  "prompt":"<above>", "aspect_ratio":"3:4",
  "medias":[{"role":"image","value":"<style_frame_uuid_or_url>"}] }
```

**AMIT SHAH — master sheet**
> *[GLOBAL STYLE BLOCK] Full-body character sheet of a caricatured politoon of Amit Shah: stocky middle-aged Indian man, exaggerated oversized head, bald crown with short grey side hair, clean-shaven, glasses, white kurta with a dark sleeveless waistcoat. Shrewd "strategist" expression. Neutral standing pose, plain white studio background, soft even lighting. `<<<style_frame>>>` = STYLE reference only; do NOT copy its subject.*

**KEJRIWAL — master sheet**
> *[GLOBAL STYLE BLOCK] Full-body character sheet of a caricatured politoon of Arvind Kejriwal: ordinary-looking middle-aged Indian man, exaggerated oversized head, black mustache, glasses, simple grey V-neck sweater over a shirt, a muffler around the neck, slightly earnest everyman look. Neutral standing pose, plain white studio background, soft even lighting. `<<<style_frame>>>` = STYLE reference only; do NOT copy its subject.*

*(Optional split for max control — generate face first, then outfit, then fuse: face prompt = head-and-shoulders only; outfit prompt = the clothing on a plain mannequin; fuse = "the face from `<<<image_1>>>` wearing the outfit from `<<<image_2>>>`, full body, white studio bg" passing both `job_id`s as `medias`.)*

### 2.6 · Expression sheet (run per figure — edit from that figure's master)
> *[GLOBAL STYLE BLOCK] Expression sheet — a grid of the SAME character from `<<<master>>>`, identical design and proportions, showing four expressions: (1) neutral, (2) sneaky scheming grin, (3) wide-eyed comic shock, (4) dazed/defeated. Plain white background, consistent lighting. Keep face structure identical across all four.*
```
generate_image params: { "model":"nano_banana_pro", "prompt":"<above>",
  "medias":[{"role":"image","value":"<master_job_id>"}] }
```

### 2.7 · Turnaround
> Preferred: **Higgsfield Angles** (UI/feature) — spin each master for front/L/R/back. MCP fallback (nano_banana_pro):
> *[GLOBAL STYLE BLOCK] Turnaround sheet of the SAME character from `<<<master>>>`: four full-body views — front, left profile, right profile, back — neutral T-pose, identical design, plain white background.*

### 2.8 · Location plate + freebie props
**Stage plate**
> *[GLOBAL STYLE BLOCK] Wide establishing shot of an empty TV-show stage: a single grand golden throne-style chair center, the word "PUNJAB" clearly written on its backrest, dramatic spotlights from above, dark backdrop. No characters. So Sorry politoon style.*

**Props sheet** (one image, for reference consistency)
> *[GLOBAL STYLE BLOCK] Prop sheet on plain white background, So Sorry politoon style: (1) a glowing yellow electricity wire/cable with a tag reading "FREE BIJLI", (2) a cluster of jute ration sacks tagged "FREE RATION", (3) a rolled-out blueprint scroll labelled "PLAN-B". Clean studio lighting.*

**GATE 2:** every figure (master + expressions + turnaround) and the plate pass a side-by-side vs a real So Sorry frame. No animation before this.

---

## PHASE 3 — BEAT-BOARD (storyboard = start & end frames)

> Model: **`nano_banana_pro`**. Reference the three master sheets + plate as `medias`. These two frames become the Seedance `start_image` / `end_image`.

### 3.2 · Frame A — START (the bait / tug-of-war)
> *[GLOBAL STYLE BLOCK] Wide stage shot: the golden "PUNJAB" chair center. On the LEFT, @kejriwal (from `<<<kejriwal_master>>>`) crouches holding a glowing "FREE BIJLI" electricity wire looped around the chair's left leg, sneaky grin. On the RIGHT, @modi (from `<<<modi_master>>>`) heaves ropes of "FREE RATION" sacks looped around the chair's right leg, with @shah (from `<<<shah_master>>>`) just behind him holding a "PLAN-B" blueprint, pointing. All three oversized-head caricatures, mid tug-of-war, comic strain. Bright stage spotlights, So Sorry style. Keep each face exactly as its master sheet.*

### 3.3 · Frame B — END (Punjab walks off)
> *[GLOBAL STYLE BLOCK] Same stage: the golden "PUNJAB" chair now stands on tiny cartoon legs at CENTER, alone under a bright spotlight, snapped wires and ropes dangling off it. @kejriwal sprawled on the floor far LEFT, @modi and @shah crashed in a heap on the RIGHT, all dazed with swirly eyes. Same style/lighting as the start frame. Keep each face exactly as its master sheet.*

**GATE 3:** both frames on-model, recognizable, visually consistent with each other.

---

## PHASE 4 — PREVIZ (cheap motion test)

> Model: **`kling3_0`** (10 cr), `sound:"off"`. Run ~10–15 from Frame A to block the gag motion before spending Seedance credits.
```
generate_video params: { "model":"kling3_0",
  "prompt":"<motion prompt below>", "duration":5,
  "params":{ "sound":"off" },
  "medias":[{"role":"start_image","value":"<frameA_job_id>"}] }
```
> *Motion: from this frame — a frantic tug-of-war over the PUNJAB chair, Kejriwal hauling his electricity wire from the left, Modi and Shah heaving ration-ropes from the right, the chair stretching and wobbling between them; then the chair sprouts tiny legs and SNAPS all the ropes, flinging everyone backward. Exaggerated cartoon slapstick, bright stage, So Sorry style.*

**GATE 4:** ≥1 pass shows bait → tug-of-war → snap-free at acceptable timing.

---

## PHASE 5 — FINAL HERO SHOT (Seedance 2.0)

> Model: **`seedance_2_0`**, `genre:"comedy"`, **Frame A as `start_image`, Frame B as `end_image`**, master/turnaround sheets tagged. 14s/720p = **63 cr per gen** — iterate deliberately; consider 720p for iteration, 1080p only for the keeper.
```
generate_video params: { "model":"seedance_2_0",
  "prompt":"<hero prompt below>", "duration":14, "aspect_ratio":"16:9",
  "params":{ "resolution":"720p", "genre":"comedy" },
  "medias":[
    {"role":"start_image","value":"<frameA_job_id>"},
    {"role":"end_image","value":"<frameB_job_id>"},
    {"role":"image","value":"<modi_turnaround_id>"},
    {"role":"image","value":"<shah_turnaround_id>"},
    {"role":"image","value":"<kejriwal_turnaround_id>"} ] }
```
**Hero prompt:**
> *Style & Mood: So Sorry 3D politoon caricature, bright stage lighting, bold saturated colors, exaggerated oversized-head characters. Dynamic Description: a golden chair labelled PUNJAB sits center-stage; @kejriwal tiptoes in from the left unspooling a glowing "FREE BIJLI" electricity wire and lassoes a chair-leg (sneaky grin); @modi strides in from the right with @shah behind holding a "PLAN-B" blueprint, whispering and pointing — Modi flings ration-sack ropes onto the other chair-leg; a frantic tug-of-war, the chair stretching and wobbling, bug-eyed strain, sweat-drops [VFX: motion lines, comic strain marks]; the chair suddenly sprouts tiny legs and SNAPS every wire and rope [VFX: TWANG snap, dust puff] — Kejriwal flies off left, Modi and Shah crash in a heap right — then the chair trots to center, alone and dignified under a spotlight. On-screen text in-style: "OPERATION: KURSI", "FREE BIJLI", "FREE RATION!", "TWANG!", final card "PUNJAB ISN'T FOR SALE — IT'S EARNED". Static Description: TV-show stage, golden PUNJAB chair, overhead spotlights, dark backdrop. Silent — no dialogue. Total: 14s / 3 beats / 16:9.*

**Per candidate:** extract frames (`ffmpeg -i clip.mp4 -vf fps=1 f_%02d.png` + grabs at ~2s/7s/13s), Read them → 3 figures on-model, no artifacts, beats present, text legible → then your motion verdict. Two-strikes → change approach, log `FAILURE.md`.

**GATE 5:** a clip passing multi-frame QC + your motion verdict.

---

## PHASE 6–7 — text legibility check, side-by-side vs real frame, export
See `production.md` §2 Phases 6–7. If in-shot text garbles, render the final card in the NLE instead.

---

## Cost note for V1 (real numbers)
- Assets: ~30–50 image gens × 2 cr ≈ **60–100 cr**
- Previz: ~10–15 Kling × 10 cr ≈ **100–150 cr**
- Finals: ~6–12 Seedance × 63 cr ≈ **380–760 cr**
- **V1 total ≈ 550–1,000 credits.** On **Plus** (1,000 cr/$39) that's ~one month; **Ultra** (3,000/$99) covers it with room. Free tier (0) cannot run it.
