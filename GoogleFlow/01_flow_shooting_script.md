# Google Flow shooting script — "The Squirrel in Ram Setu" (ZebPay SIP ad)

**What this is:** the ZebPay Squirrel ad, re-cut as a *Google Flow-native* production script so you can
learn Flow by rebuilding a video you already know. It carries the exact narrator VO and the exact
shot list from `../zebpay/01_script_AIFRIENDLY.md`, but every shot is re-specced for **Flow / Veo 3.1**
instead of Seedance-on-Higgsfield.

**Nothing here spends credits until you generate.** Build Ingredients and lay out the storyboard first
(cheap/free), then generate shot by shot.

---

## 0. Why Flow fits this ad (the one strategic thing to know)

The original workflow picked Seedance over Veo for ONE reason: on Higgsfield, Veo exposed only a single
start image (no end frame, no reference images), so it had the *least* consistency control. **Google
Flow removes that limitation.** In Flow, Veo 3.1 gives you:

| Flow capability | What it solves for this ad |
|---|---|
| **Ingredients** (reference images held across scenes) | Rama / squirrel / vanara identity consistency — the #1 quality risk. This is the whole game. |
| **Frames to Video** (start + end frame) | The keyframed contact shots (S4-c, S2-b/c). Start/end keyframes are in `keyframes/`. |
| **Scene Extension** (>60s continuous) | Stitching the 7 scenes without hard cuts if you want. |
| **Native audio** (Veo 3.1) | Ambient SFX (waves, thuds, wind) baked per shot — see the audio rule below for the one trap. |

**You already own the hard part.** The `ingredients/` character sheets and the local `keyframes/`
stills drop straight into Flow as Ingredients and start/end frames. Porting = upload + prompt.

---

## 1. The one audio trap (read before you touch native audio)

Veo 3.1 generates native audio, including a spoken voice. **Do NOT let Flow narrate this ad.** Same
reason Seedance's native audio was rejected: the narrator voice is model-invented and **is not
consistent across separate clips**, so ~24 shots = up to 24 different narrator voices. There is no
on-camera speaker here anyway (it is all off-screen narration).

**Rule:**
- In every Flow prompt, ask for **ambient/diegetic sound only** (surf, wind, stone impacts, birds) and
  explicitly **"no spoken dialogue, no narration, no voiceover, no music, no on-screen text."**
- The single continuous **narrator track stays external** (ElevenLabs, Indian-English), layered in your
  editor exactly like the existing pipeline. Clean VO text is in `02_narration_VO.txt`.
- Music stays external too (one composed bed), for the same cross-clip consistency reason.
- **Learning exception:** it is fine to let Flow generate ambient SFX per shot and keep them — just never
  the voice. If ambient audio fights you, generate silent and add SFX in post.

---

## 2. Global facts (carried, do not re-open)

- **Aspect:** 9:16 vertical. **Look:** grounded photoreal mythological epic (see STYLE block).
- **Clip length:** Veo 3.1 does 4–8s clips. Keep each shot 5–8s; use **Scene Extension** only where a beat
  needs to run longer.
- **Deity depiction:** keep Rama reverent (renders fine, low filter risk). If Flow's filter ever balks
  on a face, soften to a backlit / three-quarter framing.
- **Mode B stays Mode B:** Scene 6 (calm transition) and the ZebPay logo card (S7-b) are NOT generated in
  Flow — render them as clean graphics (Remotion / HyperFrames) and drop the legible ZebPay logo /
  Devanagari राम in as overlays. Veo garbles legible text; never ask it for the logo or the carved name.

---

## 3. STYLE block — paste-append to EVERY shot prompt

> **[STYLE]:** Grounded photoreal mythological epic, large-format 65mm / IMAX clarity, deep focus,
> warm golden-hour grade, high contrast, crushed true blacks, protected warm highlights, subtle
> teal-and-amber separation, fine 65mm film grain. Motivated natural light, low golden sun, rim and
> backlight, volumetric haze. Gritty real optics: weathered stone, hand-forged metal, real fabric weave,
> dust, ember, water spray, visible skin pores. Photographed, not illustrated, no CGI gloss, no
> over-smoothing. 9:16 vertical, subject centered, full-height scale, stable horizon.
> **[AUDIO]:** ambient/diegetic sound only; no spoken dialogue, no narration, no voiceover, no music.
> **[NEG]:** no on-screen text, no captions, no watermark, no logo; avoid identity drift, morphing,
> melting, disappearing objects, extra limbs, warped hands, jitter, temporal flicker. Smooth, slow,
> constant-speed motion, stable framing.

**Camera rule (every shot):** exactly ONE shot size + ONE angle + ONE camera move + ONE lens. Multi-move
chains cause jitter/morph. Safe moves: slow push-in (safest), pull-out/reveal, aerial pull-back, crane,
orbit/arc, tracking, tilt, pan, rack focus, static.

**Prompt order (every shot):** Subject → Environment → Action → Lighting → Camera, then append [STYLE].

---

## 4. Ingredients to build first (your "characters" in Flow)

Create these as Ingredients before shooting. **Upload the ready-made sheets in `ingredients/`** — one
clean photoreal turnaround (front · 3/4 · profile · close-up) per character, already generated and
label-free for direct upload.

| Ingredient | Upload file (local) | Used in |
|---|---|---|
| **RAMA** | `ingredients/rama_sheet.png` (photoreal serial-devotional Rama) | S1-a, S4-a…d, S7 |
| **SQUIRREL** | `ingredients/squirrel_sheet.png` — Indian palm squirrel, three pale back-stripes, bushy tail | S2–S7 (the most-repeated character) |
| **LEAD VANARA** | `ingredients/lead_vanara_sheet.png` — boastful, muscular monkey-warrior | S3–S4 |
| **BABY VANARA** | `ingredients/baby_vanara_sheet.png` — small young vanara | S3-d only |
| **SENA (army)** | `ingredients/sena_sheet.png` — 5 crowd-soldier types, keep distant | S1-b, S3 |
| **BRIDGE STATES** | `keyframes/bridge/bridge_00_empty.png`, `bridge_01_first.png`, `bridge_02_half.png`, `bridge_03_complete.png` — attach the matching state per shot | S1-d, S5, S7 |
| **STYLE ref (optional)** | any locked keyframe, used as a look Ingredient so the grade carries | all |

**Ingredient discipline (from the research):** attach ONLY the character(s) actually in a shot — never all
four. Averaging many references blends identities and erodes features.

**Frames-to-Video source:** the per-shot START/END stills are in `keyframes/`
(e.g. `S1-a.png`, `S4-c_start.png`, `S4-c_end.png`, `S2-a.png` … `S7-a_v2.png`). For any shot with both a
start and end keyframe, prefer **Frames to Video** over Ingredients-to-Video for tighter control.

---

## 5. The storyboard — shot by shot (Flow prompts)

Each shot: the **VO** it plays under (external track, NOT generated), the **paste-ready Flow prompt**
(append [STYLE]), which **Ingredients/Frames** to attach, and **duration**. Devanagari/logo = overlay in post.

### SCENE 1 — THE PURPOSE

**S1-a** · VO: *"Across this ocean waited a battle for dharma. Sita had to be brought home. Ravana had to fall."*
- **Prompt:** Rama, a divine warrior-prince holding a great longbow, stands alone at the edge of a vast ocean shore. Dark hair and simple cloth drift in a steady sea wind as he gazes with calm resolve toward the distant horizon; wet dark rock and sea spray around him, low warm sun behind him rimming his silhouette. Heroic low-angle wide shot, slow push-in, large-format wide lens. + **[STYLE]**
- Ingredient: RAMA. Start frame: `keyframes/S1-a.png`. **8s.** *(Establishes the Rama look — get this one right first.)*

**S1-b** · VO: *"And to get there, an army would build what had never been built before. A bridge across the sea."*
- **Prompt:** A vast army of vanaras (monkey-warriors) stands massed on the shore behind Rama, thousands strong and determined, facing the sea. Extreme-wide establishing shot, high angle, single slow aerial pull-back to reveal scale, wide lens; crowd kept distant, no close faces. + **[STYLE]**
- Ingredient: LEAD VANARA (loose, distant crowd). **7s.** *(Keep the crowd far — photoreal non-human faces warp up close.)*

**S1-c** · VO: *"Stone by stone. Boulder by boulder."*
- **Prompt:** A single massive boulder is hurled into the sea, arcing down and striking the water with a thunderous splash and a rising plume of spray. Wide shot, eye level, static with a slight tilt following the arc, wide lens. + **[STYLE]**
- Frames: start `keyframes/S1-c` (boulder mid-air) → end (splash plume). **5s.** *(Keep the boulder large in frame so it survives the motion.)*

**S1-d** · VO: *"Each one marked with Ram's name, and his faith."*
- **Prompt:** A vanara sets a huge boulder into the growing bridge line, its surface catching golden backlight; other placed boulders behind it. Close-up on the stone, eye level, god-ray backlight, telephoto. + **[STYLE]**
- Ingredient: LEAD VANARA + BRIDGE (first-boulders). Start frame: `keyframes/S1-d_inscription.png`. **6s.**
- **Post:** composite the golden Devanagari **राम** as a clean overlay — do NOT ask Flow to render the text.

### SCENE 2 — THE SQUIRREL ARRIVES

**S2-a** · VO: *"And in the middle of all that grandeur, something much smaller had also arrived."*
- **Prompt:** A small Indian palm squirrel appears at the edge of the shore, tiny against the construction, and turns its head to watch the vanaras work. Wide-to-medium, low/eye level (small-creature POV), slow push-in, wide lens. + **[STYLE]**
- Ingredient: SQUIRREL. Start frame: `keyframes/S2-a.png`. **7s.** *(Establishes the squirrel look.)*

**S2-b** · VO: *"It couldn't carry boulders."*
- **Prompt:** The squirrel picks up a tiny pebble in its mouth, straining slightly at the weight. Medium close-up, eye level, gentle push-in, telephoto shallow depth of field, squirrel large in frame. + **[STYLE]**
- Frames: start `keyframes/S2-b` (beside pebble) → end (pebble in mouth). **5s.**

**S2-c** · VO: *"So it carried what it could."*
- **Prompt:** The squirrel leans into a gap between two boulders and sets the pebble carefully into place, then draws back. Close-up, eye level, gentle push-in, telephoto shallow DoF. + **[STYLE]**
- Frames: start `keyframes/S2-c` (leaning in) → end (pebble set). Ingredient: SQUIRREL + BRIDGE (half). **5s.**

### SCENE 3 — THE MOCKERY  *(dense scene, one action per shot)*

**S3-a** · VO: *"Of course, one of the vanaras noticed."*
- **Prompt:** The squirrel reaches into the gap to place its pebble, focused and small. Close-up, eye level, gentle push-in, telephoto shallow DoF, squirrel large. + **[STYLE]**
- Ingredient: SQUIRREL. **5s.**

**S3-b** · VO: *"And decided to make a point of it."*
- **Prompt:** The lead vanara hoists a massive boulder onto his shoulder and flexes, eyes cast down with a smirk. Medium-wide, low angle so he looms, slow push-in, wide-to-normal lens, harder chiaroscuro shadow. + **[STYLE]**
- Ingredient: LEAD VANARA. Start frame: `keyframes/S3-b.png`. **6s.** *(Establishes the vanara look.)*

**S3-c** · VO: *"He made sure everyone laughed with him."*
- **Prompt:** The same vanara grins broadly, hefting a boulder in each hand, chest out. Medium, low angle, static, normal lens, harder chiaroscuro. + **[STYLE]**
- Ingredient: LEAD VANARA (same, keep framing similar to S3-b). Start frame: `keyframes/S3-c.png`. **5s.**

**S3-d** · VO: *"Even the babies were outdoing it without breaking a sweat."*
- **Prompt:** A baby vanara strolls casually past carrying a decent-sized stone, completely unbothered. Medium-wide, eye level, slow tracking with the stroll, normal lens. + **[STYLE]**
- Ingredient: BABY VANARA. Start frame: `keyframes/S3-d.png`. **5s.**

**S3-e** · VO: *"Naturally, nobody clapped."*  **(hardest comedy beat)**
- **Prompt:** The vanara pinches the squirrel's small pebble between two fingers, holds it up right at the squirrel's face, then flicks it away with a flat, deadpan expression. Tight two-shot, eye level, static with a slight tilt on the flick, macro-telephoto sharing the vanara's fingers and the squirrel's face. + **[STYLE]**
- Frames: start `keyframes/S3-e` (pebble held up) → end (flicked, arcing away). Ingredient: LEAD VANARA + SQUIRREL. **6s.**
- **Fallback if it warps:** two shots — (a) macro of fingers flicking a slightly larger stone (no squirrel), (b) cutaway of the squirrel's reaction. Use a slightly larger stone so it survives the flick.

### SCENE 4 — LORD RAMA NOTICES  *(the two hardest shots — you already piloted these)*

**S4-a** · VO: *"But someone else was watching too."*
- **Prompt:** Rama, bow in hand, watches the bridge; his gaze drifts down and settles on the tiny squirrel. Medium, eye level, slow push-in, telephoto isolating him, god-ray backlight. + **[STYLE]**
- Ingredient: RAMA (must match S1-a). Start frame: `keyframes/S4-a.png`. **6s.**

**S4-b** · VO: *"And he wasn't looking at the boulders."*
- **Prompt:** Rama steps forward and walks toward the squirrel, calm and deliberate. Medium-wide, eye level, slow tracking with him, telephoto. + **[STYLE]**
- Frames: start `keyframes/S4-b` (beginning to step) → end (arriving, lowering). Ingredient: RAMA. **6s.**

**S4-c** · VO: *"He was looking at the only one who showed up without being asked to."*  **(pilot ✓)**
- **Prompt:** Rama's flat open palm rests on the ground with the squirrel already at the palm's edge, paws on the skin; the palm lifts slightly as the squirrel settles into the cupped hand. A small, slow settle — no teleport. Macro on the hands only, Rama's face out of frame, eye level, very slow push-in, telephoto shallow DoF. + **[STYLE]**
- **Frames (required):** start `keyframes/S4-c_start.png` → end `keyframes/S4-c_end.png`. Ingredient: RAMA (hands) + SQUIRREL. **6s.**
- **Fallback:** two-shot — (a) Rama's face/upper body kneeling and looking down, (b) separate insert of the squirrel settling into a cupped palm with a generic hand.

**S4-d** · VO: *"Some bridges are built with strength. Some are built with heart. The wise ones know you need both."*
- **Prompt:** Rama's two fingers stroke gently down the squirrel's back; the three pale stripes stay faint but stable. Extreme close-up on the back and fingers, Rama's face out of frame, eye level, micro push-in, macro lens. + **[STYLE]**
- Frames: start `keyframes/S4-d` → end. Ingredient: RAMA (hand) + SQUIRREL. **7s.**
- **Post:** the "stripe reveal" brightening is a Mode B overlay, NOT a generated morph — keep stripes stable in-clip.

### SCENE 5 — THE BRIDGE GETS COMPLETED  *(montage: short clips, cut in post)*

**S5-a** · VO: *"Some days the sea was calm."*
- **Prompt:** On a glassy calm sea, the squirrel returns to the shore and picks up a pebble. Medium, low/eye level, slow tracking, telephoto, squirrel large. + **[STYLE]**
- Ingredient: SQUIRREL. Start frame: `keyframes/S5-a.png` (or `S5-a2_overcast.png`). **5s.**

**S5-b** · VO: *"Some days it wasn't."*
- **Prompt:** On a rough sea, the squirrel pushes forward low against breaking waves, paws visibly gripping wet sand, and still keeps going. Medium, low level, tracking, telephoto, squirrel large. + **[STYLE]**
- Ingredient: SQUIRREL. Start frame: `keyframes/S5-b.png` (or `S5-b2_mist.png`). **6s.** *(Keep paws in contact so it doesn't read as floating; moderate the waves.)*

**S5-c** · VO: *"The squirrel never waited for the right day."*
- **Prompt:** The squirrel wedges a pebble into the lengthening line of pebbles, then draws back. Medium close-up, eye level, static, telephoto. + **[STYLE]**
- Ingredient: SQUIRREL + BRIDGE (half). Start frame: `keyframes/S5-c.png`. **5s.**

**S5-d** · VO: *"It didn't matter if the tide was high or low that day. The pebble went in anyway."*
- **Prompt:** The half-built bridge: massive boulders on one side, a lengthening line of same-size pebbles wedged between them. Extreme-wide, high/eye level, slow pan along the pebble line, wide lens, no characters. + **[STYLE]**
- Ingredient: BRIDGE (half). Start frame: `keyframes/S5-d.png`. **6s.**

**S5-e** · VO: *"One pebble, placed once, means nothing. The same pebble, placed again and again, regardless of the day, that's what holds a bridge together."*
- **Prompt:** Slow macro push-in on the gap where the pebbles now sit, load-bearing and indistinguishable from the boulders. Extreme close-up / macro, eye level, slow push-in, macro lens, NO morphing or transformation. + **[STYLE]**
- Ingredient: BRIDGE (complete). Start frame: `keyframes/S5-e.png`. **7s.**
- **Cheaper option:** this is a camera move on a still — you can render it as a free Ken-Burns push in your editor instead of generating.

### SCENE 6 — THE PARALLEL  *(MODE B — do NOT generate in Flow)*
Clean transition, no mythology: kinetic type or a calm abstract field for the VO to land on. Render as
graphics. VO (external): *"Most people wait for the right time to invest. The market down, wait. The
market up, too late. The squirrel never checked the tide before showing up."* … (pause) … *"It showed up
the same way, every time, and let the average take care of the rest."*

### SCENE 7 — OUTRO

**S7-a** · VO: *"You don't need to time the market. You need to keep showing up, same amount, every time. That's not a squirrel's trick. That's SIP."*
- **Prompt:** The completed bridge glows in golden light, wide; the squirrel sits on one of its own pebbles, now fused seamlessly into the structure. Extreme-wide, low-angle heroic, slow push-in, anamorphic wide lens, squirrel large enough to hold identity, golden shimmer on the water. + **[STYLE]**
- Ingredient: SQUIRREL + BRIDGE (complete). Start frame: `keyframes/S7-a_v2.png`. **8s.** *(The money shot — perfect the frame first.)*

**S7-b** · VO: *"This video is brought to you by ZebPay, India's oldest crypto exchange. Like, share, and subscribe."*
- **MODE B:** ZebPay logo card, minimal, bottom corner. Render the card (`../zebpay/brand/zebpay_logo.png`) as
  a graphic — do NOT generate. Veo cannot render the legible logo reliably.

---

## 6. Suggested learning order (don't shoot all 24 at once)

1. **Build 2 Ingredients:** RAMA and SQUIRREL (upload the bible sheets). This alone teaches you the
   Ingredients panel.
2. **Shoot S1-a** (Ingredients-to-Video, 8s). Judge the Rama identity — this is your quality ceiling.
3. **Shoot S2-a** (squirrel establish), then **S4-c** using **Frames to Video** with the start/end
   keyframes. That teaches you both generation modes and tests the hardest shot early — exactly how the
   Seedance pilot was run.
4. Compare Flow's S1-a / S4-c against your existing pilots in `../zebpay/clips/PILOTS_REEL.mp4`. Same two
   shots, different engine — a clean A/B of Flow vs Seedance on your own content.
5. If identity holds, batch the rest scene by scene. Assemble + layer the external VO/music/captions in
   your editor (or try Flow's Scene Extension to stitch inside Flow).

## 7. What stays OUTSIDE Flow (unchanged from your pipeline)
- **Narrator VO** — one external ElevenLabs track (`02_narration_VO.txt`). Never let Flow speak it.
- **Music** — one external composed bed.
- **Legible text** — the राम carving (S1-d) and the ZebPay logo card (S7-b) are post overlays/graphics.
- **Scene 6** — rendered graphics, not generated.
- **Captions** — burned last, in post.

---

*Source script (immutable): `../zebpay/00_input_script_HUMAN.md`. Decomposition carried verbatim from
`../zebpay/01_script_AIFRIENDLY.md`. VO wording is unchanged; only staging is re-specced for Flow / Veo 3.1.*
