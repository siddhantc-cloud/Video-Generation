# Clear Gut ad — project

Boilerplate for producing the BLUMELIFE Clear Gut "Ingredient Army" caricature ad. Clean home replacing the scattered `simple_ads/production*` mess.

## Directory
```
ads/clear-gut/
├── 00_brief.md            product, concept, tone, audience, must-haves
├── 01_script.md           the script — single-speaker shots + narrated groups (v3)
├── 02_direction.md        shot list: blocking, camera, lighting per scene
├── prompts/
│   ├── keyframes.md       Nano Banana Pro keyframe prompts (per scene)
│   └── veo.md             Veo 3.1 video prompts (per scene)
├── research/
│   └── prompting-guide.md general → Veo → this-format prompting (3-level synthesis)
├── bible/                 character ID reference images (king, amla, ajwain, saunf, haritaki, stomach, bottle)
├── assets/                clear_gut_product.png (the real bottle — perfect label source)
├── keyframes/             [generated] per-scene start frames sN_start.png
├── clips/                 [generated] per-scene Veo clips sN.mp4
├── audio/                 [generated] music bed / VO if any
└── edit/                  assembly scripts, EDL, captions
    └── final/             final renders
```

## The method (locked — skill `caricature-talking-ad`)
1. **Character IDs:** reuse `bible/*.png` as refs so characters are identical across scenes.
2. **Keyframe per scene** (`prompts/keyframes.md`): one clear subject; dialogue shots are SOLO; bottle shots reference `assets/clear_gut_product.png`.
3. **Animate** (`prompts/veo.md`): Veo 3.1 `--image <keyframe>`, native audio. Dialogue shots = one speaker (colon syntax, half-second pause, no-subtitles). Group/product shots = NARRATOR voiceover.
4. **Assemble:** normalize 1080×1920/24fps → crossfade (xfade+acrossfade 0.4s) → music bed → optional burned Devanagari captions → **Scene 9 real-product card** (pixel-perfect close).

## Golden rules (why, from hard lessons)
- **One speaker per shot; groups → narrator.** Veo animates every visible mouth, so two talkers = "who's speaking?" mush.
- **Heroes look heroic (warm/bright/friendly); only the King looks evil (dark/red-eyes/green-murk).** Good-vs-evil must read in <1s.
- **Bottle drifts to a blank label in motion** → keep it still & sharp in-prompt + always end on the real-product still card.
- **No burned text:** always `no subtitles, no captions, no on-screen text`.

## Status
- ✅ Brief, script (v3), direction, prompts, research, bible, product — all written/migrated. **No video generated yet (awaiting go).**
- Prior attempts archived in `simple_ads/production_v2/` (v2 ad + bible source); reference only.

## To produce (when approved)
Generate keyframes from `prompts/keyframes.md` → review → generate clips from `prompts/veo.md` → review (right speaker, others mouths closed, no burned text, label sharp) → assemble per the method. Pilot 1–2 scenes before the full batch. ~24 cr/scene.
