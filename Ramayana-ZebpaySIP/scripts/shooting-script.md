# 01 - AI-video-friendly shot decomposition: "The Squirrel in Ram Setu" (ZebPay SIP)

**Gate 0 output. This is the script-rewriter pass. No media generated, no credits spent.**
Source of truth (immutable): `00_input_script_HUMAN.md`. This file decomposes that script into
generation-ready shots. **Narrator VO wording is verbatim from the frozen script.** Only the
*visual staging* is re-specced for the engine, and the *which-sentence-plays-over-which-shot*
alignment is a pacing proposal (the VO remains one continuous, unedited track).

> **Execution update (2026-07-21):** `../project/higgsfield-manual-generation-operating-spec.md`
> supersedes this document's historical `generate_audio=false` instructions. Future Seedance
> production candidates generate diegetic SFX/ambience only; narration and music remain separate,
> and characters remain non-speaking. Shot intent, staging, VO mapping, and fallbacks below remain
> authoritative.

---

## Header: locked production facts (carried, not re-opened)

- **Engine:** Seedance 2.0 image-to-video. Every shot = a locked START keyframe (+ optional END
  keyframe) + a short prompted motion between them + which character reference(s) to attach.
- **Style:** photoreal cinematic mythological allegory. **Aspect:** 9:16 vertical mobile reel.
- **Audio:** ALL narration is a single NARRATOR VOICEOVER (ElevenLabs, Indian-English). **No
  on-camera dialogue, no lip-sync anywhere.** `generate_audio=false` on every Seedance clip.
  On-camera characters keep neutral / closed mouths and must not read as speaking. (The lead
  vanara's grin / laugh is an *expression*, not synced dialogue, and is fine.)
- **Captions:** burned in post (Mode B). **Music:** ElevenLabs `compose_music`.
- **Modes:** Scenes 1 to 5 + Scene 7 hero shot = generative (Mode C). Scene 6 (clean transition,
  no mythology) and the Scene 7 ZebPay logo card = **Mode B: render in Remotion / HyperFrames,
  do NOT generate.**
- **Character bible (locked):** Rama, the squirrel (Indian palm squirrel, three stripes), the
  boastful lead vanara, a baby vanara. Deity depiction renders fine (already proven via ChatGPT
  image-gen); keep it reverent.
- **Reference-attach discipline (from research below):** attach ONLY the character(s) actually in
  the shot, never all four. Averaging many references causes identity blend.

---

## Engine + research delta (live check, 2026-07-07)

Target confirmed: **Seedance 2.0 (image-to-video)** on Higgsfield, silent mode. Findings folded in:

- **"Too many actions in a short time" is a NAMED Seedance failure mode** ("beat density"
  violation); recommended prompt length is 30 to 100 words and the fix is "simplify the action,
  reduce distinct movements per shot." This directly validates decomposing Scene 3 (~5 actions)
  and splitting Scene 2's pick-up-then-place into two shots.
  ([seedanceai.cc](https://www.seedanceai.cc/guides/seedance-2-0-troubleshooting),
  [innovareacademics.in](https://innovareacademics.in/blog/why-most-seedance-2-0-prompts-fail-before-the-first-frame/))
- **Identity blend / feature erosion when averaging MULTIPLE references** is documented; the fix is
  "reduce to the ~3 most consistent references and strengthen identity-lock language." So we attach
  only the character(s) in a given shot, not the whole cast.
  ([magichour.ai](https://magichour.ai/blog/how-to-use-seedance-20),
  [crepal.ai](https://crepal.ai/blog/aivideo/blog-seedance-2-0-character-consistency/))
- **Fast / complex interactions make objects float or disappear and characters move unnaturally.**
  This hits the exact shots we already flagged hard: 4c (Rama + squirrel contact), 3e (fast pebble
  flick), 1c (boulder splash), 5b (squirrel in rough surf). Mitigation baked in: keyframe both
  endpoints, keep the motion slow/gentle, keep the moving object large enough to survive, and carry
  the listed fallbacks.
  ([wavespeed.ai](https://wavespeed.ai/blog/posts/seedance-2-0-review-issues-and-alternatives/))
- **In-video text is unreliable** (a shared 2026 weakness across models). Confirms the ZebPay card
  and any legible label stay **Mode B**, never asked of Seedance.
  ([magichour.ai reference guide](https://magichour.ai/blog/seedance-20-reference-guide))
- **NEW vs our binding: Seedance 2.5 shipped early July 2026** (longer clips, better consistency).
  Our binding is 2.0. Flagged as a possible upgrade for the identity-critical Rama shots, to
  confirm at the spend gate (do not switch blindly: cost/availability on Higgsfield unverified).
  ([seedance.tv 2.5 review](https://www.seedance.tv/blog/seedance-2-5-review-2026))
- **Content / IP / face filters exist on Seedance**, but original characters plus a respectful
  deity depiction already generate fine; low content-filter risk here. Keep Rama reverent.
  ([mindstudio.ai](https://www.mindstudio.ai/blog/seedance-2-0-content-restrictions-workarounds))

---

## Direction bible (global style)

**Target look: "grounded photoreal mythological epic."** The register of the 2026 Ramayana film
(Nitesh Tiwari / DNEG: IMAX-scale, photoreal, burnished gold and desaturated stone, solemn and
mythic), DIRECTED with Christopher Nolan's method. Reusable spec:

- **Director / method reference: Christopher Nolan.** His constant is motivated real light, high
  contrast, deep true blacks, and large-format clarity, NOT cool desaturation. He goes warm when the
  source motivates it (Interstellar, the Los Alamos light). We use his WARM register.
- **Anti-uncanny (critical).** The Ramayana teaser drew criticism for an "AI / over-smoothed CGI"
  look. Deliberately lean into GRIT and real optics: weathered stone, hand-forged metal, real fabric
  weave, dust, ember, water spray, skin pores, fine film grain. Photographed, not illustrated.
- **Palette / grade.** Warm golden-hour, high contrast, crushed true blacks, protected warm
  highlights, subtle teal-and-amber separation, fine 65mm grain. Saturation up, gloss off.
- **Light.** Motivated / natural: low golden-hour sun, rim and backlight, god rays and volumetric
  haze for the divine (Rama) beats; chiaroscuro and harder shadow for the mockery.
- **Lens / format.** Large-format 65mm / IMAX clarity, deep focus to keep the world legible,
  wide-angle immersion for scale. Use telephoto compression and shallow depth of field ONLY for the
  intimate squirrel and Rama-contact beats.
- **Aspect.** 9:16 vertical mobile reel, composed with Nolan's "taller is more immersive" instinct:
  subject centered, full-height scale, headroom for grandeur.
- **Composition.** Clean, center-weighted, immersive scale (a tiny figure against a vast world),
  stable horizon.
- **Editing / pacing (for the assembly).** Two speeds: hold the epic golden wides long so scale
  registers, then cut sharp on action; crosscut the squirrel's humble effort against the vanaras'
  boasting; ticking-clock acceleration into the SIP payoff; cut on motion; let the score carry
  momentum across cuts.

**Camera rule (applies to every shot table below).** Exactly ONE shot size + ONE angle + ONE camera
move + ONE lens per shot (multi-move chains cause jitter/morph). Reliable move vocabulary: slow
push-in (safest), pull-out/reveal, crane up/down, aerial, orbit/arc, tracking, tilt, pan, rack
focus, static/locked.

---

## The decomposed shot list

Column key. **Camera** = one size + one angle + one move + one lens (the golden rule). **Refs** =
which locked reference(s) to attach. **Risk** low/med/high; fallbacks for med/high are footnoted
under each scene. "Single frame + camera move" = no end keyframe needed.

### SCENE 1: THE PURPOSE (Mode C)

| Shot | VO (verbatim) | Visual action (one subject / one action) | Camera | START frame | END frame | Refs | Risk |
|---|---|---|---|---|---|---|---|
| S1-a | "Across this ocean waited a battle for dharma. Sita had to be brought home. Ravana had to fall." | Rama stands at the shore, Dhanush in hand, hair in the wind, gazing to the distant horizon. | Heroic wide, low angle, slow push-in, large-format wide lens. | Rama in hero pose at shore, facing sea, bow in hand. | Single frame + slow camera push-in; hair and cloth drift in wind. | Rama (this shot ESTABLISHES the Rama lock) | med [1] |
| S1-b | "And to get there, an army would build what had never been built before. A bridge across the sea." | The vanara sena stands gathered behind Rama, thousands, determined. | Extreme wide establishing, high angle, single slow aerial pull-back (ONE move), wide lens; crowd distant, no macro faces. | Wide: massed vanara army on the shore behind Rama, still. | Single frame + slow aerial pull-back to reveal scale. | vanara (crowd, loose, distant) | low |
| S1-c | "Stone by stone. Boulder by boulder." | A single boulder is hurled into the sea with a thunderous splash. | Wide, eye level, static with a slight tilt to follow the arc, wide lens. | Boulder released mid-air, arcing down toward the water. | Boulder impacts the sea, large splash plume rising. | none (or vanara arms at frame edge) | med [1] |
| S1-d | "Each one marked with Ram's name, and his faith." | A vanara sets a massive boulder inscribed with the golden Devanagari name राम into the bridge, other marked boulders behind. | Close-up on the inscribed stone, eye level, god-ray backlight, telephoto (a wide alt of many marked boulders also exists). | Vanara hand on the boulder, the carved golden राम catching light. | Boulder settled into the bridge line. | vanara + bridge-state | med [1b] |

Fallbacks:
- [1] **S1-a** (Rama establishing): this still IS the canonical Rama; if drift/anatomy is off, iterate
  the STILL cheaply before any motion, and keep motion near-static (breath + wind only).
- [1] **S1-c** (water physics / fast motion): if the boulder floats or the splash tears, slow the
  arc, keep the boulder large in frame, or fall back to a locked splash-moment still with a short
  Ken-Burns push (Mode B). The lift-and-carry from the frozen visual is intentionally compressed to
  the single hurl-plus-splash beat (see change log).
- [1b] **S1-d** (legible sacred text): image-gen renders Devanagari only roughly, so the final carved राम is composited as a CLEAN Mode B text/engraving overlay on the locked still (guaranteed correct), not generated live. Two keyframes exist: `S1-d_inscription` (close-up) and `S1-d_inscription_wide` (many marked boulders).

### SCENE 2: THE SQUIRREL ARRIVES (Mode C)

| Shot | VO (verbatim) | Visual action | Camera | START frame | END frame | Refs | Risk |
|---|---|---|---|---|---|---|---|
| S2-a | "And in the middle of all that grandeur, something much smaller had also arrived." | A small squirrel appears at the edge of the shore, watching the vanaras work. | Wide to medium, low / eye level (small-creature POV), slow push-in, wide lens. | Squirrel at the shore edge, small in frame, facing the construction. | Single frame + slow push-in; small head turn toward the work. | squirrel (this shot ESTABLISHES the squirrel lock) | med [2] |
| S2-b | "It couldn't carry boulders." | The squirrel picks up a tiny pebble in its mouth, straining slightly at the weight. | Medium close-up, eye level, gentle push-in, telephoto shallow DoF. | Squirrel beside a pebble on the sand. | Pebble held in the squirrel's mouth, a slight strain in the pose. | squirrel | low-med [2] |
| S2-c | "So it carried what it could." | The squirrel places the pebble carefully into a gap between two boulders. | Close-up, eye level, gentle push-in, telephoto shallow DoF. | Squirrel at the bridge gap, pebble in mouth, leaning in. | Pebble set into the gap; squirrel drawing back. | squirrel | low-med [2] |

Fallbacks:
- [2] **S2-a** (squirrel establishing): this still IS the canonical squirrel; perfect it as a STILL
  first. **S2-b / S2-c** (squirrel identity through motion): if the squirrel wobbles, keep the shots
  short and the squirrel large/foreground; re-lock the reference. The frozen "scurries up to the
  bridge" travel is covered by the cut between S2-b and S2-c (see change log).

### SCENE 3: THE MOCKERY (Mode C) - the dense scene, split one-action-per-shot

| Shot | VO (verbatim) | Visual action | Camera | START frame | END frame | Refs | Risk |
|---|---|---|---|---|---|---|---|
| S3-a | "Of course, one of the vanaras noticed." | The squirrel tries to place its pebble between two boulders. | Close-up, eye level, gentle push-in, telephoto shallow DoF (squirrel large). | Squirrel at the gap, pebble in mouth, reaching in. | Pebble nudged toward the gap; squirrel focused. | squirrel | low-med [3] |
| S3-b | "And... decided to make a point of it." | The lead vanara hoists a massive boulder onto his shoulder and flexes, eyes cast down. | Medium wide, low angle (he looms), slow push-in, wide-to-normal lens, harder chiaroscuro. | Vanara lifting a large boulder from the ground. | Boulder on his shoulder, muscles flexed, glaring downward. | lead vanara (this shot ESTABLISHES the vanara lock) | low-med [3] |
| S3-c | "He made sure everyone laughed with him." | The same vanara grins, hefting two boulders, one in each hand. | Medium, low angle, static, normal lens, harder chiaroscuro. | Vanara gripping a boulder in each hand at his sides. | Both boulders raised, broad grin, chest out. | lead vanara (same) | low-med [3] |
| S3-d | "Even the babies were outdoing it without breaking a sweat." | A baby vanara strolls casually past, carrying a decent-sized stone, unbothered. | Medium wide, eye level, slow tracking with the stroll, normal lens. | Baby vanara entering frame with a stone, mid-stride. | Baby vanara strolling out of frame, still casual. | baby vanara | low |
| S3-e | "Naturally, nobody clapped." | The vanara holds the squirrel's pebble right at the squirrel's face, then flicks it away, deadpan. | Tight two-shot, eye level, static (slight tilt as it flicks), macro-telephoto (vanara's fingers and the squirrel's face sharing the frame). | Pebble pinched in the vanara's fingers, held up at the squirrel's face. | Pebble flicked and arcing away; squirrel's reaction; flat vanara expression. | lead vanara + squirrel (both in frame) | **high** [3] |

Fallbacks:
- [3] **S3-b / S3-c** (vanara identity across the two beats): keep the SAME reference and similar
  framing so the character reads as one vanara. **S3-e** (fast flick + tiny object + two-character
  proximity, now the TIGHTER two-subject framing per user, higher risk): the vanara's fingers and the
  squirrel's face share the frame. If the tiny pebble warps, the fast flick makes it vanish, or the two identities blend, fall back to a
  two-shot: (a) a macro insert of the fingers flicking a small stone (no squirrel), then (b) a
  separate cutaway of the squirrel's reaction. A slightly larger stone survives the flick better.

### SCENE 4: LORD RAMA NOTICES (Mode C) - contains the two hardest shots

| Shot | VO (verbatim) | Visual action | Camera | START frame | END frame | Refs | Risk |
|---|---|---|---|---|---|---|---|
| S4-a | "But someone else was watching too." | Rama, bow in hand, watches the bridge; his gaze settles on the squirrel. | Medium, eye level, slow push-in, telephoto (isolates him), god-ray backlight. | Rama at the shore, bow in hand, looking out over the work. | Single frame + slow push-in; eyeline drifts down to settle. | Rama (must MATCH S1-a) | med [4] |
| S4-b | "And he wasn't looking at the boulders." | Rama walks toward the squirrel; the laughter fades. | Medium wide, eye level, slow tracking with him, telephoto. | Rama standing, beginning to step forward. | Rama arriving near the squirrel, starting to lower. | Rama | med [4] |
| S4-c | "He was looking at the only one who showed up without being asked to." | Rama's flat palm rests on the ground with the squirrel already at its edge; the palm lifts slightly as the squirrel settles in (small settle, NOT a ground-to-palm teleport). | Macro on the hands (Rama's face OUT of frame), eye level, very slow push-in, telephoto shallow DoF. | Rama's flat palm on the ground, squirrel already at the palm's edge, paws on the palm. | Same palm lifting slightly, squirrel settled in the cupped palm. | Rama (hands only) + squirrel | **high** [4] |
| S4-d | "Some bridges are built with strength. Some are built with heart. The wise ones know you need both." | Rama's two fingers stroke down the squirrel's back; the three stripes stay faint but STABLE in-clip (the brightening reveal is a Mode B post overlay, not a generated morph). | Extreme close-up on the back and fingers (Rama's face OUT), eye level, micro push-in, macro. | Rama's two fingers on the squirrel's back, stripes faintly present. | Fingers having stroked down; stripes unchanged in-clip (post overlay adds the reveal). | Rama (hand only) + squirrel | med [4] |

Fallbacks:
- [4] **S4-a** (Rama identity match to Scene 1, the main quality risk): reuse the Rama lock, keep
  composition close to S1-a, re-lock at this reappearance. **S4-b** (identity through motion): short
  walk, keyframed endpoints. **S4-c** (HARDEST: two-character physical contact + gentle fine
  motion): pilot this shot FIRST (Gate C). Keyframe both endpoints as specified; keep the lift slow.
  If contact breaks (palm/squirrel fuse, squirrel floats), fall back to a **two-shot cutaway**: (a)
  Rama's face/upper body kneeling and looking down (Rama ref only), then (b) a separate insert of the
  squirrel settling into a cupped palm (squirrel ref + a generic hand, no full Rama identity needed).
  **S4-d** (contact + subtle stripe reveal): specify the stripes as a soft *brightening* along the
  stroke path, NOT a morph. If the generative reveal fails, do the stroke as a macro insert
  (fingers + squirrel back only, no full Rama face) or add the three-stripe glow as a **Mode B
  overlay** on a locked still.

### SCENE 5: THE BRIDGE GETS COMPLETED (Mode C montage + Mode B assembly)

| Shot | VO (verbatim) | Visual action | Camera | START frame | END frame | Refs | Risk |
|---|---|---|---|---|---|---|---|
| S5-a | "Some days the sea was calm." | On a calm sea, the squirrel returns to the shore and picks up a pebble. | Medium, low / eye level, slow tracking, telephoto (squirrel large). | Calm shore, squirrel approaching a pebble. | Pebble in the squirrel's mouth; still water behind. | squirrel | low-med [5] |
| S5-b | "Some days it wasn't." | On a rough sea, the squirrel struggles forward through the waves, and still goes. | Medium, low level, tracking, telephoto (squirrel large). | Rough surf, squirrel low against the water, pushing in. | Squirrel reaching firmer ground, spray around it. | squirrel | med [5] |
| S5-c | "The squirrel never waited for the right day." | The squirrel wedges a pebble into the lengthening pebble line. | Medium close-up, eye level, static, telephoto. | Squirrel at the pebble line, pebble in mouth. | Pebble set into the line; squirrel drawing back. | squirrel | low-med [5] |
| S5-d | "It didn't matter if the tide was high or low that day. The pebble went in anyway." | The bridge, growing: boulders on one side, a lengthening line of same-size pebbles wedged between them. | Extreme wide, high / eye level, slow pan along the pebble line, wide lens. | Wide of the half-built bridge, boulders + a short pebble line. | Single frame + slow pan along the lengthening pebble line. | bridge-state (no character) | low-med [5] |
| S5-e | "One pebble, placed once, means nothing. The same pebble, placed again and again, regardless of the day, that's what holds a bridge together." | Slow macro push-in on the gap where the pebbles now sit, load-bearing, indistinguishable from the boulders. | Extreme close-up / macro on the fused pebbles, eye level, slow push-in on a LOCKED still (no morph), macro. | Locked macro still of the pebble-filled gap (wider). | Single locked still + slow camera push-in to tight on the fused pebbles. NO morph. | bridge-state (no character) | low [5] |

Fallbacks:
- [5] **S5-a/b/c** are the montage (quick cuts, assembled Mode B); each is a distinct day/tide.
  **S5-b** (small subject in rough water, float/disappear risk): keep the squirrel large/foreground
  and the waves moderate; if it tears, use calmer surf. **S5-d** (bridge-state continuity): attach
  the bridge-state reference so it reads as the same structure evolving; keep motion to a slow pan.
  **S5-e**: re-specced as a **camera move on a locked still, not a morph** (per direction). It can be
  a minimal Mode C push OR a near-free **Mode B Ken-Burns / parallax push** on the locked macro
  still (see open questions, a credit-saving option).

### SCENE 6: THE PARALLEL - **Mode B (render in Remotion / HyperFrames, do NOT generate)**

- **Visual:** clean transition, NO mythology, calm space for the thought to land (kinetic type or a
  calm abstract field for the VO to sit on). Rendered deterministically, zero generation credits.
- **VO (verbatim):**
  - V17: "Most people wait for the right time to invest. The market down, wait. The market up, too late. The squirrel never checked the tide before showing up."
  - **Pause.** (VO-track timing beat, hold the calm frame)
  - V18: "It showed up the same way, every time, and let the average take care of the rest."

### SCENE 7: OUTRO (Mode C hero shot + Mode B card)

| Shot | VO (verbatim) | Visual action | Camera | START frame | END frame | Refs | Risk / mode |
|---|---|---|---|---|---|---|---|
| S7-a | "You don't need to time the market. You need to keep showing up, same amount, every time. That's not a squirrel's trick. That's SIP." | The completed bridge in golden light, wide; the squirrel sits on one of its own pebbles, now fused into the structure. | Extreme wide, low-angle heroic, slow push-in, anamorphic wide lens (squirrel large enough to hold identity). | Wide of the finished golden bridge, squirrel perched on a fused pebble. | Single frame + slow push-in; golden light shimmer on the water. | squirrel + bridge-state (completed) | low-med [6] |
| (Pause.) | | VO-track timing beat before the card. | | | | | |
| S7-b | "This video is brought to you by ZebPay, India's oldest crypto exchange. Like, share, and subscribe." | ZebPay logo, minimal, bottom corner. | n/a (Mode B card, not a Seedance shot) | | | | **Mode B: render, do NOT generate** |

Fallbacks:
- [6] **S7-a** (the payoff hero shot): perfect the STILL first (this is the money frame); keep the
  squirrel large enough to hold identity; motion is near-static (light + breath only).

---

## Prompt construction + negatives

Build every Seedance shot prompt in this order:
**Subject -> Environment -> Action -> Lighting -> Style (the Direction bible look) -> Camera LAST.**

Always attach negatives on every clip: **avoid jitter, avoid temporal flicker, avoid identity
drift, avoid bent limbs, avoid morphing, avoid melting, avoid disappearing objects, avoid extra
limbs, avoid warped hands.** Add positive stability language to every prompt: **"smooth, slow,
constant-speed motion, stable framing."** `generate_audio=false` on every clip.

---

## Prompt and VO text hygiene (engines vocalize punctuation)

Two hard rules, because generation engines SPEAK punctuation instead of pausing on it:

- **Seedance (video) prompts are VISUAL ONLY.** Never put the narrator VO or any in-quotes dialogue into a Seedance prompt. The VO lines in the tables are alignment/timing metadata, not prompt text. With `generate_audio=false` Seedance speaks nothing, and keeping spoken text out also prevents accidental on-screen text. Keep prompt punctuation plain: no em-dashes, no ellipses, no quotation marks around lines.
- **ElevenLabs VO text is CLEANED before TTS.** Send only the actual spoken words. Strip every stage direction (`Pause.`, scene headers, tone parentheticals). Remove em-dashes. Convert pause punctuation the TTS would otherwise pronounce: an ellipsis like `And... decided` becomes a controlled pause via an ElevenLabs break tag (`<break time="0.4s"/>`) or a comma, so the engine PAUSES rather than voicing the punctuation. A clean spoken-only `02_vo_script.txt` is prepared at the VO step and fed to TTS; the `Pause.` beats become silence or `<break>` there and in the edit.

This is the same failure the script-rewriter guards against (punctuation voiced as garbage), enforced at the moment text is sent to any speaking engine.

---

## Music (ElevenLabs compose_music)

Epic Indian-mythological orchestral, Hans Zimmer meets A.R. Rahman (their real 2026 Ramayana
pairing): full symphony orchestra + taiko / tabla / dhol + bansuri / sarangi / sitar +
Sanskrit-chant choir, key of D minor, leaving headroom under the narrator VO. Timestamped arc for a
~75s ad:

- 0:00 sparse sacred open (solo bansuri + soft strings, ~75 BPM)
- 0:12 warm build (add tabla + low string ostinato, ~95 BPM)
- 0:30 playful lighter mockery middle (pizzicato strings, light tabla, cheeky sitar motif, ~105 BPM)
- 0:45 tender swell (solo sarangi + bansuri over hushed choir, near-silence then rising)
- 0:58 triumphant SIP payoff (full orchestra + taiko + epic choir + brass fanfare, ~122 BPM, clean final impact)

Recommend calling `create_composition_plan` first to lock section timing, then `compose_music`.
Ready string (verbatim):

```
Epic Indian-mythological orchestral score, Hans Zimmer meets A.R. Rahman: full symphony orchestra fused with taiko drums, tabla and Indian percussion, bansuri, sarangi and sitar, sweeping string ostinato, heroic French-horn theme, and a Sanskrit-chant choir. Key of D minor, reverent and cinematic, leaving space under a narrator. 75-second arc: 0:00 sparse sacred opening with solo bansuri and soft strings ~75 BPM; 0:12 warm build adding tabla and low string ostinato ~95 BPM; 0:30 lighter playful comic middle with pizzicato strings, light tabla and a cheeky sitar motif ~105 BPM; 0:45 tender bittersweet swell with solo sarangi and bansuri over hushed choir; 0:58 triumphant climax with full orchestra, taiko, epic choir and brass fanfare to a clean final impact ~122 BPM. Mythic, majestic, emotional, cinematic. Exclude: modern electronic elements, drum machine, vocals with lyrics.
```

---

## Audio: why one VO track, not Seedance native audio

Yes, Seedance 2.0 CAN generate audio (put a character line in double quotes and it voices it,
lip-synced). It is still the wrong tool for THIS film, for grounded reasons (verified 2026-07-08):
- **No on-camera speaker.** Native audio voices ON-CAMERA lip-synced dialogue; our narration is an
  OFF-screen narrator over visuals with no speaking character, so there is no mouth to sync. It would
  give us ambient sound, not our narration.
- **The voice is model-invented and inconsistent across clips.** The voice fingerprint is inferred
  from the character description, and the docs are explicit: timbre locks WITHIN a clip but NOT
  across separate generations. So ~20 clips = up to 20 different narrator voices; you cannot get one
  continuous narrator this way.
- **Reported quality is unreliable** (users get exaggerated, high-pitched, cartoonish voices, "not
  what you asked for").
- **It costs more** Higgsfield credits per clip, and bakes audio in so it cannot be re-timed or
  re-mixed against the music.
- **Industry best practice matches ours:** Seedance for the visuals, a controllable TTS (ElevenLabs)
  for a specific consistent brand voice layered on top.
Therefore `generate_audio=false` on every clip, and the VO is a single external ElevenLabs track
(Sarvam if keyed): one consistent, directed, exact-script Indian-English narrator across the whole
film.

---

## Change log

Each entry: **SANCTIONED** = a generation-friendliness fix I made (no creative-intent change), or
**OPTIONAL** = a creative/pacing suggestion that needs human sign-off (nothing silently changed).

| # | Scene / shot | Original | Rewrite | Failure mode it prevents | Cost | Type |
|---|---|---|---|---|---|---|
| C1 | Scene 3 (whole) | Five actions packed under four VO lines (squirrel places, vanara hoists+flexes, vanara grins with two boulders, baby strolls, vanara flicks). | Split into 5 discrete one-action shots S3-a..S3-e. | Seedance "beat density" / multiple-actions-per-shot failure. | Adds shots (more paid clips), each far more likely to pass. | SANCTIONED |
| C2 | S1-c | "The first boulder lifted, carried, hurled into the water with a thunderous splash." | One beat: boulder hurled, splash (start = mid-air, end = splash). Lift/carry compressed into the cut. | Multiple actions + fast water physics (float/tear). | Loses the on-screen lift/carry (VO "stone by stone" still carries it). | SANCTIONED |
| C3 | S2-b / S2-c | "picks up a tiny pebble... struggles slightly... scurries up to the bridge... places it carefully." (four actions, one VO line) | Split into pick-up (S2-b) and place (S2-c); the "scurry" travel lives in the cut. | Beat-density failure; identity wobble through multi-action motion. | Adds one shot; travel is implied, not shown. | SANCTIONED |
| C4 | S3-e | "picks up the pebble between two fingers, holds it up in front of the squirrel's face, and flicks it away." | Single flick beat (start = pebble pinched/held up, end = flicked away, deadpan); squirrel is eyeline/small, not tight contact. | Fast small-object motion (vanish/warp) + two-character proximity + multi-action. | Slightly less "in your face"; recover via the two-shot fallback if needed. | SANCTIONED |
| C5 | S4-c | "Rama kneels. Picks up the squirrel gently in his palm." | Re-specced as keyframe pair (start = open palm near squirrel, end = squirrel resting in palm), slow motion; two-shot cutaway fallback documented; **pilot first**. | Two-character physical-contact interaction (the single hardest Seedance shot). | None to intent; adds a re-roll/pilot budget. | SANCTIONED |
| C6 | S4-d | "strokes the squirrel's back with two fingers." (+ R7 stripe reveal) | Keyframe pair with the stripes as a soft *brightening* along the stroke path (not a morph); macro-insert / Mode-B-overlay fallback. | Fine contact motion + unstable VFX morph. | None; the stripe beat is preserved, just made renderable. | SANCTIONED |
| C7 | S5-c (macro) | "Camera pushes into the gap where the pebbles sit... indistinguishable from the boulders." | Specced as a slow camera push-in on a LOCKED macro still, explicitly NO morph. | Morph/transform hallucination (pebbles melting into boulders). | None; same visual read, achieved by camera not morph. | SANCTIONED |
| C8 | Scene 5 montage | "quick repeated cuts of the squirrel returning... some days calm... some days rough... it still goes." | Made explicit as 3 short one-action clips (S5-a calm pickup, S5-b rough-sea struggle, S5-c place) assembled Mode B. | Undefined multi-action montage in one clip. | Adds shots; gives a clean cuttable montage. | SANCTIONED |
| C9 | All shots | (bible has 4 characters) | Attach ONLY the character(s) present in each shot (never all 4). | Identity-blend / feature-erosion from averaging references. | None. | SANCTIONED |
| C10 | Scenes 6, 7b | (script describes them as visuals) | Marked **Mode B** (Remotion/HyperFrames), not generated. | Unreliable in-video text (logo/label) + wasted credits on deterministic content. | None (saves credits). | SANCTIONED |
| C11 | Scenes 6, 7 | "Pause." | Kept as VO-track timing markers (not per-clip audio; audio is one external track). | Mis-timed VO / lost breathing room. | None. | SANCTIONED |
| C12 | All shots | (no camera direction) | Added a per-shot Camera column (one size + one angle + one move + one lens) plus a global Direction bible, prompt-order + negatives, and a scored music spec. | Multi-move chains cause jitter/morph; undirected look reads uncanny/flat; wrong prompt order and native audio waste credits. | None (additive craft direction). | SANCTIONED |
| O1 | S3-e | "holds it up right in front of the squirrel's face" | OPTIONAL: soften to an eyeline instead of a tight two-subject frame (already reflected as the primary spec; flag if you want the tighter, riskier framing attempted first). | Reduces re-roll risk. | Slightly less confrontational comedy beat. | OPTIONAL |
| O2 | S5-e | (a generated push-in) | OPTIONAL: render S5-e as a **Mode B Ken-Burns/parallax push** on the locked macro still instead of a paid Seedance clip. | Saves one paid clip. | None visible (it is already a camera-move-on-still). | OPTIONAL |
| O3 | Whole VO | 20 verbatim narrator segments | OPTIONAL: at VO record time, consider one extra half-beat of silence after S4-d ("...you need both.") before Scene 5, to let the emotional peak land. Pure timing, zero wording change. | Pacing. | None. | OPTIONAL |

**No wording changes were made to the narrator VO.** Every line above is verbatim; C1 to C12 change
only staging/mode/direction, and O1 to O3 are suggestions awaiting your call.

---

## Deliberately kept (creative intent protected)

- **The narrator VO, 100% verbatim.** This is the brand voice; not one word was altered, reordered,
  or "smoothed." The ellipsis in "And... decided to make a point of it." is kept (a TTS pause, not a
  dash). No em-dashes or hyphens exist in the VO, so no dialogue-cleanup was needed.
- **The R7 stripe beat at S4-d** (Rama's finger-marks becoming the squirrel's three stripes) is kept,
  just made renderable as a soft brightening, not cut.
- **The mockery-then-tenderness emotional arc** (Scene 3 comedy into Scene 4 reverence) is untouched;
  splitting shots preserves every named beat.
- **Rama's reverent depiction and the Dhanush (bow) as a static hero prop** are kept; low
  content-filter risk, no need to sanitize.
- **The "indistinguishable from the boulders" payoff** (S5-e) is kept in full meaning; only the
  *method* (camera push, not morph) changed.
- **Photoreal, 9:16, single-VO, no-lip-sync** production facts are honored exactly.

---

## Open questions for human

1. **Shot-count / budget: APPROVED (2026-07-08).** Keep the one-action splits (~20 to 21 Mode C
   shots). The user wants more, shorter, higher-pass-rate paid clips for best quality.
2. **S5-e as Mode B (O2)?** Approve rendering the macro push-in as a free Ken-Burns move on a locked
   still, or keep it a paid Seedance clip?
3. **S3-e framing: DECIDED (2026-07-08), tighter framing first.** Per the user's "we want better
   results", S3-e is now the tighter two-subject beat (the vanara holding the pebble right at the
   squirrel's face) as the PRIMARY attempt for the stronger comedy; the two-shot cutaway stays the
   fallback if the tiny object warps or the two identities blend. (Interpretation: "better results"
   = the more impactful framing, protected by the fallback. Say so if you meant the safer eyeline.)
4. **Model: LOCKED = Seedance 2.0 (2026-07-08).** 2.5 is not on Higgsfield (verified: roster is only
   1.5 Pro, 2.0, 2.0 Mini) and the user chose to lock 2.0 rather than wire an alternate provider. 2.0
   is the most control-capable model available (start+end keyframes + image_references + up to 4k),
   run in silent mode (`generate_audio=false`). No 2.5 chase.
5. **VO-to-shot alignment.** The sentence-per-shot mapping above is a pacing proposal; the VO is one
   continuous track. Confirm the alignment, or adjust which sentence sits over which visual.

---

**APPROVAL GATE:** APPROVE to hand this decomposed shot list to the assistant-director (Gate A) and
to build per-shot keyframes against it / tell me what to revise. Nothing proceeds, and no keyframe
is generated, until you approve.

---

## Gate A resolutions (Assistant Director audit reconciled, 2026-07-08)

Verdict was REVISE (one light pass), now **BALANCE ACHIEVED** after these. Full audit:
`gateA_assistant_director_audit.md`.

Applied to the tables above:
- **S4-c restaged** to a small settle (squirrel already at the palm edge, macro on hands, Rama's face out of frame) instead of a ground-to-palm teleport (morph is driven by keyframe layout delta).
- **S4-d stripe reveal is now a Mode B post overlay** (Seedance strokes a stripe-stable squirrel), removing the most fragile in-clip VFX morph; risk drops to med.
- **S1-b fixed to a single move** (aerial pull-back), crowd kept distant (photoreal non-human faces warp up close).
- **Negatives augmented** (morphing / melting / disappearing-objects / extra-limbs / warped-hands) + positive stability language on every prompt.

Accepted as build-time discipline (applied during keyframe + generation):
- **S3-e** runs as a hard-gated pilot with a slightly LARGER stone and a SLOW short flick (end frame keeps the stone large and near-frame, not a fast vanish); two-shot cutaway ready if it warps by attempt 2.
- **S1-c / S1-d**: the "marked with Ram's name" beat now has its OWN shot (S1-d). Because Seedance/image-gen garble Devanagari, the carved राम is finalized as a CLEAN Mode B text/engraving overlay on the locked still (guaranteed legible), not generated live. S1-c stays the splash.
- **S5-b**: keep the squirrel's paws visibly in contact with wet sand/rock so it does not read as floating.
- **Identity discipline**: every Rama/squirrel shot attaches the clean bible sheet and matches KEYFRAME STILLS to each other; never re-derive the canonical from a video frame. S1-a does NOT define the lock (the bible sheet does).
- **Pilot ordering**: pilot one Rama shot (S1-a) first to confirm both the drift ceiling AND that the photoreal deity face passes the Seedance video content filter, before batching the other Rama shots.
- **O2 approved**: S5-e renders as a free Mode B Ken-Burns push on the locked macro still (identical look, zero morph, saves a clip).

Reference assets commissioned to close the two continuity gaps (generated free before Gate B):
- **4-state bridge reference set** (empty sea, first boulders, half-built + pebble line, completed golden bridge), attach the matching state to every bridge shot.
- **Multi-angle identity sheets** (front + three-quarter + profile, neutral light) for Rama and the squirrel, so identity is anchored by ANGLE coverage, not just expression.
