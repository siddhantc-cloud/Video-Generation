# Higgsfield manual generation operating spec

**Project:** Ramayana-ZebPay SIP, “The Squirrel in Ram Setu”
**Status:** Proposed production operating method; human approval required before paid generation
**Research and live-schema freeze:** 2026-07-21, Asia/Calcutta
**Scope:** How to produce the video manually at cinema quality. This document does not generate media or authorize credit spend.

## Operating checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Creative truth | Brief, frozen narration, story order, and cultural constraints are accepted | `brief.md`, `../scripts/original-script.md` | Human/Creative | Exists; approval evidence absent |
| Shot plan | Each visual has one story purpose, one primary action, and one primary camera move | `../scripts/shooting-script.md` | Director | Complete |
| Timing plan | Narration-led animatic and per-shot frame timings are accepted | `../deliverables/review-cuts/animatic/`, `../edit/edl/animatic.json` | Human/Editor | Built; runtime approval absent |
| Character continuity | Rama, squirrel, lead vanara, and baby vanara canonical references are selected by role | `../assets/characters/` | Director/Art | All four references exist and are human-approved; per-shot role map pending |
| World continuity | Every bridge shot uses the correct bridge-state reference | `../assets/environments/bridge/`; Cinema Studio Elements evidence screen 032 | Director/Art | Ready: four Location Elements exist; states 01-03 use inspected character-free 941×1672 portrait plates |
| Vertical conformance | Every Seedance start/end frame is exact 9:16 | Conformed keyframe dimensions | Art/Operator | Blocked: 15 of 30 keyframes are 2:3 |
| Native sound method | Seedance generates diegetic SFX/ambience only; narration and music remain separate | Shot prompt, audio review, final mix stems | Sound/Operator | Method defined here; production pending |
| Current platform contract | Model schema, cost, parameters, and reference limits are checked before each production session | CLI/UI preflight | Operator | Verified 2026-07-21; recheck before spend |
| Pilot gate | Identity, contact physics, camera, and native SFX are proven on representative hard shots | Pilot review records | Director/Human | Existing silent pilots do not close the new sound gate |
| Per-shot keeper gate | A take passes full-motion, frame, continuity, cultural, and audio review | Versioned review verdict | Director/Human | Pending |
| Final assembly | Picture, native SFX beds, continuous narration, music, graphics, grade, and captions are locked | Timeline, stems, QC report | Editor/Sound/Human | Pending |
| Automation readiness | Every manual decision is captured as structured shot metadata | Companion take records | Operator | Template defined here; production pending |

## 1. Decision summary

The quality-first method for this film is:

1. Treat the film as a conventional production: script and timing first, then visual bible, keyframes, shot production, dailies, edit, sound mix, QC, and delivery.
2. Use **standalone Seedance 2.0 Standard** as the default final video engine because the current live model accepts start/end frames plus image, video, and audio references, supports 4–15 seconds, native audio, and up to 4K in `std` mode.
3. Generate **one controlled shot at a time**. Use internal multi-shot generation only when a short action genuinely needs a cut inside one 4–15 second clip and continuity is easier inside one pass than across separate rolls.
4. Use the approved keyframe as the opening-state anchor. Add canonical character and location references even when the character/location already appears in the keyframe.
5. Use a previous approved clip in one of two explicit roles only: direct scene continuation, or camera/motion reference. Never leave its role ambiguous.
6. Generate **diegetic SFX and ambience inside Seedance**, synchronized to visible action. Keep narration and music completely separate and mix them after picture selection.
7. During the learning phase, keep the exact `seedance_2_0` model in `std` mode with high bitrate and Sound On, and use 480p, the live minimum. Set duration from the complete visual beat and known failure window; four seconds is only a narrow mechanics probe, not the default. Do not substitute Fast, Mini, or Seedance 1.5 as fidelity evidence. Judge shot logic, blocking, camera direction, unwanted cuts, gross continuity, and SFX timing at 480p; do not approve fine identity, anatomy/contact, fur, texture, grade, or final delivery from it. A higher-resolution run is a new roll, not a deterministic rerender, so it must pass the complete review again.
8. For maximum quality, target Seedance 2.0 Standard, `4k`, `bitrate_mode=high`, 9:16, native sound on. The cost-controlled minimum final candidate is 1080p Standard. Cinema Studio 3.5 outputs currently top out at 1080p.
9. Use Cinema Studio 3.5 when its explicit genre, color, light, lens, focal-length, and aperture controls materially improve a shot. Use Supercomputer as an orchestrator with approval gates, not as the film’s memory or director of record.
10. Promote a take only after full-motion and audio review. A beautiful first frame is not evidence that the clip holds.

## 2. Authority and supersession

This document governs **manual Higgsfield execution**. The shooting script remains authoritative for story purpose, shot IDs, narration mapping, and fallback staging.

The user’s 2026-07-21 sound decision supersedes older execution notes that say `generate_audio=false` or describe every Seedance clip as silent. Those older files remain useful historical audits, but future production candidates should use:

- Native Seedance audio: **on**.
- Generated content: **diegetic SFX and location ambience only**.
- Generated speech: absent; characters remain visibly non-speaking.
- Narration: one separately produced Indian-English narrator stem.
- Music: one separately produced score stem.

This is not a decision to ask Seedance for the narrator. It is a decision to use Seedance for synchronized physical sound while preserving narration consistency and mix control in post.

## 3. Current verified platform state

The authenticated environment was read-only checked on 2026-07-21:

| Item | Verified state |
|---|---|
| Higgsfield CLI | `1.1.19`, build dated 2026-07-18 |
| Account | Authenticated; subscription type reported as `max` |
| Seedance catalog | Seedance 1.5 Pro, Seedance 2.0, Seedance 2.0 Mini |
| Primary job type | `seedance_2_0` |
| Aspect ratios | `auto`, `16:9`, `9:16`, `4:3`, `3:4`, `1:1`, `21:9` |
| Duration | Integer from 4 through 15 seconds; 3 and 16 were rejected by non-generating cost validation |
| Resolution | `480p`, `720p`, `1080p`, `4k` |
| Mode | `std`, `fast`; `fast` is limited to 480p/720p |
| Audio | `generate_audio` boolean, default currently `true` |
| Quality | `bitrate_mode`: `standard` or `high` |
| Image references | At most 9 counting start and end images |
| Video references | At most 3 |
| Audio references | At most 3 and only when an image/video/start/end reference is also present |
| Total reference files | At most 12 across images, videos, audio, start, and end |
| Cinema Studio 3.5 workflow | 480p/720p/1080p; start/end/image/video/audio references; multi-shot controls; native audio toggle |

The live schema is more authoritative than an old tutorial or remembered UI label. Before every production session, run:

```powershell
higgsfield model list --json
higgsfield model get seedance_2_0 --json
higgsfield account status --json
```

Before each approved run, calculate the exact cost with the final prompt, duration, quality, audio setting, and references:

```powershell
higgsfield generate cost seedance_2_0 `
  --prompt "<approved shot prompt>" `
  --aspect_ratio 9:16 `
  --duration <4-15> `
  --resolution <720p|1080p|4k> `
  --mode std `
  --bitrate_mode high `
  --generate_audio true
```

Add the exact start/end/image/video flags used by the shot. Cost checks do not create a job. Prices and promotions change; never budget from a blog screenshot.

## 4. Surface routing: which Higgsfield tool does what

| Surface | Use it for | Do not use it for | Project rule |
|---|---|---|---|
| Standalone Seedance 2.0 Standard | Default final shot, 4K, exact start/end, image/video continuity references, native SFX | Whole-film improvisation | Primary production surface |
| Seedance Fast or a Fast-only Unlimited route | Rapid 480p/720p exploration on a different inference tier | Evidence for locked Standard-mode consistency or final cinema master | Do not use for this project's fidelity experiments; an Unlimited route is eligible only if the UI explicitly includes standard `seedance_2_0` |
| Cinema Studio 3.5 | Look development; explicit genre, color, lighting, camera body, lens, focal length, aperture; bounded multi-shot clips | Native 4K final output | Use when parameter locks are more valuable than 4K |
| Cinema Studio 3.0 | Optional alternate for a physics-heavy or character-heavy shot after a controlled comparison | Silent model switching across the whole film | Exception only; log the reason and compare against Seedance |
| Supercomputer | Plan steps, preserve an in-chat chain, show cost, hand an approved image into Seedance, optional review/VO audition | Autonomous whole-film direction or unreviewed spend | One shot or tightly connected sequence per chat; approve every paid step |
| CLI | Reproducible schema, cost, upload, generation, result, and automation-ready logs | Inventing prompts | Execution and verification layer |

### Recommended default

Use standalone Seedance 2.0 Standard for the final clips. Use Cinema Studio 3.5 to establish or test the optical/look recipe and for shots where its settings deliver a visibly better result. If a Cinema Studio 1080p take is the best performance, keep it and upscale/finish it rather than recreating a weaker take solely to claim native 4K.

### Cinema Studio 3.5 starting recipe for this film

This is a starting test, not an automatic setting for every shot:

| Control | Epic/world shot | Tender/contact shot |
|---|---|---|
| Genre | Epic | Drama |
| Color | Bleached Warm or Naturalistic Clean | Bleached Warm |
| Camera moveset | Epic Scale or Silent Machine | Intimate Observer or Silent Machine |
| Lighting | Contre-jour | Soft Cross or Contre-jour |
| Camera | Fine Film | Fine Film |
| Lens | Anamorphic for wide scale | Warm Halation or Extreme Macro |
| Focal length | 14mm or 35mm | 50mm or 75mm |
| Aperture | f/11 for world geography | f/4; f/1.4 only when background loss is intentional |

Keep optical choices in the Cinema Studio controls. Do not repeat a conflicting virtual camera/lens stack inside the prompt.

## 5. Production architecture

```text
Frozen story + narration timing
        ↓
Character/location/prop/style bible
        ↓
Exact 9:16 start/end keyframes
        ↓
Pilot: identity + hardest contact + native SFX
        ↓
Per-shot packet → schema/cost gate → candidate takes
        ↓
Motion/frame/audio/continuity review → approved select
        ↓
Picture edit with handles
        ↓
Extracted native SFX beds + separate narration + separate music
        ↓
Graphics/captions/grade/mix/QC/delivery
```

This sequence is deliberate. Better prompting cannot rescue an unstable character design, a wrong bridge state, a non-vertical start frame, or an action that should have been two shots.

### Duration and cut discipline

Duration is chosen from the scene, not from a cost minimum or the 15-second ceiling:

1. Use the **intended edit duration** when evaluating a candidate's continuity, camera behavior, or
   unwanted-cut risk. The test must include the full failure window.
2. Use **15 seconds** when one coherent continuous action genuinely needs it, or when an intentional
   Seedance multi-shot scene can fit 1–3 purposeful cuts inside it. State `one continuous shot, the
   camera does not cut on its own` for an oner; for a multi-shot, name and time every intended cut.
3. Do not pad a 4–7 second action to 15 seconds. Empty time invites improvised action, internal cuts,
   identity drift, or background replacement and costs the same per second.
4. A longer clip can reduce the number of exported files and editorial joins, but it does not
   automatically reduce the number of visible cuts: Seedance may create internal cuts, and an
   intentional multi-shot clip contains cuts baked into the generation.
5. Group adjacent storyboard rows only when they share the same character set, location, temporal
   unit, and reference packet, and the combined action density remains controllable within 15 seconds.
   Split on location changes, major entrances/exits, high-risk contact, or dense action.

## 6. Current project asset audit

### Assets that already exist

- Rama: face, front, profile, hero/costume reference, and tender-expression images.
- Squirrel: front, profile, hero, content, and straining images.
- Lead-vanara and human-approved baby-vanara references.
- Four bridge states: empty, first stones, half built, complete.
- Thirty shot keyframes.
- A full storyboard and narration-led animatic.
- Two 720×1280, 24 fps pilot videos: S1-a and S4-c.
- Shot-specific visual QC criteria.

### Element library routing decision

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Canonical shoreline | One clean Location Element anchors coast, ocean, distant island, rock language, sun direction, and palette | `../assets/environments/bridge/bridge_00_empty.png`; S1/S2/S4/S5 shot rows | Art/Operator | Complete: `Ram-Setu-Shoreline-Canonical-Location`; reference-only source, not a start/end frame |
| Early bridge state | A character-free portrait plate preserves state-01 bridge geometry and the canonical world | `../assets/environments/bridge/bridge_01_first_clean_location.png`; S1-d, S2-c, S3-a-e, S4-a-b | Art/Operator | Complete: 941×1672 plate inspected and `Ram-Setu-Bridge-Early-Location` created |
| Half-built bridge state | A character-free portrait plate preserves state-02 geometry and the canonical world | `../assets/environments/bridge/bridge_02_half_clean_location.png`; S5-c-e | Art/Operator | Complete: 941×1672 plate inspected after a second cleanup pass and `Ram-Setu-Bridge-HalfBuilt-Location` created |
| Complete bridge state | A character-free portrait plate preserves state-03 geometry and the canonical world | `../assets/environments/bridge/bridge_03_complete_clean_location.png`; S7-a | Art/Operator | Complete: 941×1672 plate inspected and `Ram-Setu-Bridge-Complete-Location` created |
| Prop discipline | Only an object whose exact design must recur becomes a Prop Element | Shooting script and deterministic-post rules | Director/Art | No Prop Elements required before pilots |

The four Location Element names are `Ram-Setu-Shoreline-Canonical-Location`, `Ram-Setu-Bridge-Early-Location`, `Ram-Setu-Bridge-HalfBuilt-Location`, and `Ram-Setu-Bridge-Complete-Location`. They are now registered. States 01-03 use separate clean edits that preserve bridge geometry, island position, rock materials, water, sun direction, and grade while removing every character; the original source frames remain untouched. These near-native 9:16 Location references are not substitutes for exact 9:16 start/end frames.

The bow remains part of Rama's canonical character reference unless a pilot proves it drifts. Pebbles, ordinary stones, and boulders remain prompt-level objects because their exact design need not persist. The Devanagari inscription and ZebPay logo remain deterministic post elements, never generated Prop Elements.

### Immediate blocker: keyframe aspect ratio

Fifteen keyframes are 1024×1536 (2:3), not 9:16. They can be used as composition/style/identity references, but should not be used directly as start/end frames for a locked 9:16 generation:

- `S1-c.png`
- `S1-d_inscription_wide.png`
- `S2-b.png`
- `S2-c.png`
- `S3-b.png`
- `S3-c.png`
- `S4-a.png`
- `S4-b.png`
- `S4-c_end.png`
- `S4-d.png`
- `S5-a.png`
- `S5-a2_overcast.png`
- `S5-c.png`
- `S5-d.png`
- `S5-e.png`

Conform them non-destructively by extending/outpainting or recomposing to exact 9:16. Do not overwrite the originals. A center crop is acceptable only when it preserves the action, contact points, eyelines, and edit-safe headroom.

### Pilot interpretation

The existing S1-a and S4-c clips prove that 720×1280 moving images exist, but they were produced under the old silent architecture. They may be used as:

- Visual quality evidence.
- Camera/motion references.
- Continuity context where their identity is acceptable.

They do not prove the new diegetic-SFX workflow and should not automatically become final selects.

## 7. Reference discipline

Seedance is multimodal, but more references are not automatically better. Every reference must have one declared job.

### Project reference-role convention

| Role | Typical file | What it controls |
|---|---|---|
| Start image | `keyframes/<SHOT>*.png` | Opening composition, subject scale, pose, lighting, spatial state |
| End image | Only where a precise endpoint is required | Final physical state; use only when layout delta is small |
| Character identity | One clear canonical face/angle file | Face/species geometry and distinguishing marks |
| Character body/costume | One full-body or costume/state file | Proportions, wardrobe, jewelry, bow, stripes |
| Location/state | Correct `bridge_00` through `bridge_03` | World geometry and construction continuity |
| Style/grade | `assets/reference-stills/s1_establishing.png` or an approved hero frame | Palette, contrast, atmosphere, surface realism |
| Motion/camera video | Approved pilot, purpose-shot reference, or prior clip | Camera path, speed, performance rhythm only |
| Audio reference | Optional rhythm/atmosphere guide | Only when visual timing must follow it; not the narrator for this film |

### Canonical-over-plate rule

If Rama is already visible in the start keyframe, still attach the canonical Rama identity asset for a Rama shot. The start image carries the shot state; the canonical identity reference carries who he is. Apply the same rule to the squirrel and lead vanara.

### Minimum useful reference set

For most shots:

1. Exact 9:16 start keyframe.
2. One canonical subject identity/body reference.
3. One correct location/bridge-state reference when the environment recurs.
4. Optional end keyframe or one motion/camera video, only when needed.

Start with this. Add another reference only to fix a specific missing constraint. Remove any stale or contradictory reference.

### Character-specific routing

- Rama close/medium: use `rama_face.png` or the closest clean angle, plus one costume/body reference if needed.
- Rama full body/hero: use `rama_front.png` or `rama_ref.png`; use `rama_profile.png` for profile-led shots.
- Squirrel front/interaction: use `squirrel_front.png` or `squirrel_ref.png`; use `squirrel_profile.png` for lateral action; use the state image only when the emotion/action requires it.
- Lead vanara: use `vanara_lead_ref.png`. A distant crowd is an environment/population, not a repeated clone of this lead.
- Bridge: attach exactly one state per shot. Never mix half-built and complete state references in one generation unless the bridge transformation itself is the visible action.

### Fictional characters and Soul ID

Soul ID is principally valuable for a real person or a face trained from many rights-cleared photographs. Rama and the squirrel are fictional designs with already-built canonical assets, so Soul ID is not the default here. Use Cast/Elements or locked reference images. Consider a persistent trained identity only if current references repeatedly fail after the pilot gate and the platform supports the fictional-character workflow without changing the approved design.

### Avoid one ambiguous collage

The current assets are separate front/profile/face files, which is useful. Higgsfield’s recent short-film workflow notes that a character sheet containing multiple visible faces can confuse Seedance’s face lock. Do not blindly merge every angle into one multi-face image. Feed the one or two angles that match the shot, with an explicit role for each.

## 8. Start/end-frame discipline

### Start frame

Every opening frame should:

- Be exact 9:16.
- Already show the subject in the correct location, wardrobe/state, scale, eyeline, and lighting.
- Start with useful asymmetry and physical grounding.
- Show contact points clearly: feet on ground, paw on sand, squirrel on palm.
- Leave room in the direction of movement.
- Contain only the story elements needed by the shot.

### End frame

Use an end frame when the exact physical result matters: squirrel settled in the palm, pebble seated in a gap, boulder at impact, or a planned match cut.

The start/end frames must be close enough in framing, scale, and subject placement that the model interpolates motion rather than inventing a layout teleport. If the end state requires a large reframe, location jump, major body transformation, or multiple new contacts, split the shot.

### When a start frame alone is better

Use start-only image-to-video for:

- Hair/cloth/water/atmosphere motion.
- Slow push-in or pull-back.
- Small gaze or posture change.
- Near-static hero shots.
- Actions whose endpoint can be allowed to settle naturally.

## 9. Previous video as reference

Previous footage is powerful only when its role is explicit.

### A. Direct continuation of the same scene

Use when the next clip begins from the accepted state of the prior clip.

1. Export the approved previous clip without narration/music overlays.
2. Extract and inspect its final frame.
3. Use the final frame as the next start image where possible.
4. Add the previous clip as a video context reference.
5. Reattach the canonical character and location references, especially if the final frame hides the face.
6. Open the prompt with `The scene continues from the supplied video context.`
7. Describe only the next action/state change. The source carries the existing state.
8. Preserve aspect ratio, timing character, lighting direction, grade, and movement axis.
9. Cut at a motivated camera-angle change in the editor; do not expect the platform to create the final invisible join by itself.

Project cap: chain at most two continuations before returning to the original canonical references and a clean keyframe. Three is the hard ceiling. Each continuation inherits small errors from the prior output.

### B. Camera or performance reference only

Use an existing clip when its move is hard to describe in text.

Declare:

- The clip supplies camera path, speed, framing, shake, and/or action timing only.
- The current shot’s canonical image references supply identity, wardrobe, location, lighting, and style.
- The current SFX request replaces the source audio.

Do not let an unrelated video silently carry its face, clothing, color temperature, location, or soundtrack into the Ramayana shot.

### C. Continuity between separate shots

For a normal edit rather than a continuous extension, prefer a cut on matching action or eyeline. End shot A and begin shot B on the same gesture, direction, or physical beat. This is more robust than trying to extend every clip.

## 10. Prompt construction

### Core rule

References carry the **state**. Prompt text carries the **change**.

Do not spend prompt space re-describing every pixel already locked by the start frame. Use the prompt to define action, camera, performance, physics, lighting behavior, audio, and the few invariants that must not drift.

### Prompt size and mode

- Simple one-shot prompt: approximately 50–80 words.
- Production block prompt: use only the required blocks and keep the copy-ready prompt under roughly 200 words when possible.
- One primary subject action and one primary camera move per clip.
- Internal multi-shot: normally 1–3 purposeful cuts; every cut changes both shot size and camera character.
- Prompt language: English.

### Short-prompt order

1. Subject and starting physical state.
2. One visible action.
3. Setting and spatial relationship.
4. One camera instruction.
5. Lighting and surface behavior.
6. Performance/physics.
7. Diegetic audio.
8. Positive locks.

### Production-block order

Use these labels only when the shot needs them:

```text
SCENE CONTEXT
ACTIVE REFERENCES
FIRST FRAME / BLOCKING
FORMAT MODE
OPTICS
CAMERA
ACTION
PERFORMANCE
PHYSICS
LIGHTING / COLOR
AUDIO
POSITIVE LOCKS
```

### Language rules

- Use visible behavior instead of abstract emotion: breath slows, gaze softens, jaw releases, shoulders lower.
- Use measurable movement: `slow constant-speed push-in`, `one step`, `palm lifts five centimeters`.
- Describe left/right from the camera’s view.
- Keep characters physically separated until a contact beat is unavoidable.
- Limit tracked hero subjects to three; two is safer.
- Treat crowds as an environmental mass unless a named individual is featured.
- Keep reflections and mirrors out of identity-critical shots.
- Put brand copy, captions, Devanagari inscription, financial text, stripes glow, and logo animation in post.
- Translate internal filmmaker/film references into measurable light, color, texture, blocking, and camera behavior before pasting into Seedance.
- Use positive locks: `stable facial geometry`, `closed relaxed mouth`, `three stripes remain fixed`, `smooth constant-speed movement`, `hands remain anatomically grounded`.

The existing direction bible may retain creative inspirations internally. The execution prompt should not rely on a named filmmaker, named cinematographer, camera brand, or contradictory virtual equipment stack to achieve the look.

### Format modes

- **Oner:** default; one continuous shot, no cuts.
- **Sequential cuts:** cut order is fixed but timing can breathe.
- **Timed multi-shot:** use only when specific beat timing is essential.
- **Freestyle:** avoid for identity/contact-critical production shots.

## 11. Native SFX and separate narration

### Audio architecture

| Layer | Created where | Production rule |
|---|---|---|
| Diegetic action SFX | Seedance with the visual | Synchronized to visible physical events |
| Location ambience | Seedance with the visual | Two or three restrained layers, matched to space |
| Narration | Separate voice workflow | One continuous narrator identity; never fed to Seedance for these shots |
| Music | Separate score workflow | Mixed across cuts; never regenerated per shot |
| Graphics/caption sounds | Post | Deterministic and frame-accurate |

### Why this split is correct

Seedance can synchronize a splash, cloth rustle, pebble scrape, surf, wind, footfall, and impact to the generated motion. It cannot guarantee one identical off-screen narrator voice across twenty separate clips. A separate narrator track preserves exact copy, pronunciation, pacing, revisions, and mix control.

### How to write the SFX block

Tie sound to visible cause and time. Name one foreground sound per beat and at most two or three ambient layers.

Pattern:

```text
AUDIO: Diegetic-only soundscape. [Visible action] produces [specific sound] at [beat].
The space carries [ambience 1] and [ambience 2] with [acoustic character].
Character mouths remain closed; narration and score are supplied in post.
```

Project examples:

- S1-c: stone air-whoosh → heavy water impact → broad splash tail; low surf and coastal wind underneath.
- S2-b: tiny claws on damp sand, pebble scrape, quiet strained breath; distant surf.
- S2-c/S3-a: pebble taps stone and settles into grit; close stone resonance, soft water ambience.
- S4-c: cloth and jewelry micro-rustle, palm against sand, squirrel claws settling; gentle surf and wind.
- S5-b: wave wash, wet paw impacts, spray, strained breath; rough surf without a musical swell.

Avoid generic instructions such as `cinematic sound` or `dramatic hit`; they can invite score-like audio. Describe the physical source.

### Draft and final sound policy

1. Use a short 480p Standard **Sound On** pilot to prove the SFX vocabulary and ensure Seedance does not invent speech/music.
2. A silent 480p Standard diagnostic may be used only when audio is deliberately outside the test; it is never a keeper and does not close the audio gate. The current no-reference cost quote does not become cheaper when sound is disabled, so Sound On is the default.
3. Final candidates use native sound on from the start.
4. Review native audio solo before selecting the take.
5. Extract and archive an approved take’s audio as a separate SFX bed.
6. Mix narration over the bed and duck SFX/ambience where intelligibility requires it.

Native sound is fused into the generated file. If the visual is exceptional but the generated audio contains an unwanted voice, music-like layer, or unusable artifact, retain the visual only as a documented exception, strip the audio, and rebuild that SFX in post. Do not throw away a rare perfect visual take solely to preserve a tool preference.

### Narration timing

The film is narration-led. Use the existing scratch narration and integer-frame EDL as the timing master before generating expensive footage. Record/approve the final narrator before final picture lock when possible. Give each generated clip enough visual handle to trim against its narration segment without changing semantic alignment.

Do not attach the narration as `@Audio` to Seedance. That would condition visuals and can invite lip-sync or voice-linked behavior that this film does not need.

### Verified ElevenLabs narration path (2026-07-24)

1. Search both the live Higgsfield preset list and the underlying ElevenLabs Voice Library. A voice
   being discoverable does not prove the current account can synthesize it through the API.
2. ElevenLabs currently hosts Hindu-mythology voices explicitly described for Ramayana narration,
   but the current free/API entitlement returns HTTP 402 for Voice Library TTS. Higgsfield's live
   voice list does not expose those mythology labels or accent metadata.
3. Use the account-owned original Voice Design voice `NarratorZebPay` for this film. Never imitate
   or clone a real actor/public person without rights and consent.
4. Use Eleven v3 with one versioned pronunciation dictionary. Current selected aliases are:
   `vanaras` → `vaa-nuh-raas`, `Ram Setu` → `Raam Say-too`, `Rama` → `Raa-muh`, `SIP` →
   `ess eye pee`, and `ZebPay` → `Zeb Pay`. The earlier hyphenated `Zeb-pay` alias is rejected.
5. Generate one continuous take with character timestamps. Do not generate isolated sentences and
   hope they share cadence.
6. If the continuous take is shorter than the locked picture, do not globally stretch it. Global
   scaling moved some v006 phrase starts by up to 868 ms. Partition in inter-phrase silence, keep
   naturally shorter phrases intact and pad their tails, and accelerate only phrases that overrun
   their exact frame slots. Rebuild captions from the conformed word timings.
7. Mix approved native SFX as a separate stem with 30 ms shot-boundary fades. The selected v006
   mix uses SFX at -10 dB, final gain +0.2 dB, and measures -16.01 LUFS / -3.28 dBTP after AAC.
8. The automated transcript/loudness/sync gate cannot approve timbre. The owner must listen to the
   encoded review cut before promotion.

Evidence and exact IDs/settings live in
`../audio/voiceover/elevenlabs-v006/VOICEOVER-v006.md`, not in this general operating section.

## 12. Manual step-by-step production procedure

### Phase 0: Freeze the production truth

1. Read `brief.md`, the original script, shooting script, storyboard, animatic, shot tracker, and QC criteria.
2. Confirm the destination format remains 1080×1920 vertical and confirm/adjust the 166.633-second animatic runtime.
3. Approve the story, narration wording, shot order, and cultural/reverence rules.
4. Mark unresolved brand/legal claims; they remain outside generative footage.
5. Treat each shot ID as an independent production unit with an explicit fallback.

**Gate:** do not spend on full production until script, storyboard/keyframes, and animatic timing have human approval evidence.

### Phase 1: Conform and lock assets

1. Conform the fifteen 2:3 keyframes to exact 9:16 without overwriting sources.
2. Inspect every conformed frame at mobile size and full size.
3. Select one primary and one alternate identity angle for Rama, squirrel, and lead vanara.
4. Confirm each bridge-state image has one stable construction logic and lighting direction.
5. Create a contact-safe S4-c start/end pair with minimal layout delta.
6. Keep the stripe reveal, Devanagari inscription, investing graphics, captions, and brand logo deterministic in post.

**Gate:** a shot cannot enter final generation if any start/end asset has the wrong aspect, wrong subject state, wrong bridge state, bad anatomy, or unresolved composition.

### Phase 2: Lock the global look

1. Choose one grade doctrine: warm low sun, compressed palette, real fabric/stone/skin texture, true blacks, controlled highlights, fine grain.
2. Choose the lighting direction for each location state and preserve it across reverse angles.
3. In Cinema Studio 3.5, create small tests of the recommended Epic and Tender recipes.
4. Compare full-motion output, not just still frames.
5. Approve one global look recipe and document any scene override.
6. Use the same style/grade reference in standalone Seedance shots where useful.

**Gate:** one approved world/lighting/texture test and one approved Rama/squirrel close-detail test.

### Phase 3: Run three pilots before the film

Pilot order:

1. **S1-a:** validates reverent Rama identity, face stability, simple camera movement, wind/cloth/surf SFX, and content filtering.
2. **S4-c:** validates the hardest two-subject contact, palm/squirrel separation, hand anatomy, micro-lift, and close foley.
3. **S2-b or S2-c:** validates squirrel identity/stripes, small-object survival, paw/pebble contact, and delicate foley.

For each pilot:

1. Build the shot packet.
2. Run the exact `seedance_2_0` model at 480p Standard, high bitrate, and Sound On. Use the intended beat duration for continuity/cut evaluation; use four seconds only when the complete test is observable within four seconds.
3. Change only one variable per systematic retry.
4. When the mechanics are correct, run a final-quality Standard candidate with sound on.
5. Review identity, motion, contact, camera, and audio independently.
6. Freeze the successful reference roles and wording patterns into the project’s next shot packets.

**Gate:** all three pilot categories pass before any batch of remaining shots.

### Phase 4: Build one shot packet

Copy this template into the companion record before generation:

```text
SHOT ID / VERSION:
STORY PURPOSE:
VO RANGE / TARGET EDIT FRAMES:
RISK LEVEL / FALLBACK:

SURFACE / MODEL:
ASPECT / DURATION / RESOLUTION / MODE / BITRATE / AUDIO:

START IMAGE:
END IMAGE (optional):
IMAGE REFERENCES + ROLE:
VIDEO REFERENCES + ROLE:
AUDIO REFERENCES + ROLE:

OPENING BLOCKING:
PRIMARY ACTION:
PRIMARY CAMERA MOVE:
PERFORMANCE / PHYSICS:
LIGHTING / COLOR:
DIEGETIC SFX / AMBIENCE:
POSITIVE LOCKS:

PROMPT:
SCHEMA CHECK DATE:
ESTIMATED COST:
HUMAN APPROVAL:
```

Reject the packet before generation if any field leaves the engine to decide a story-critical identity, contact, location state, direction of movement, text, or audio layer.

### Phase 5: Preflight the exact shot

1. Re-read the live model schema.
2. Confirm 9:16, duration, resolution, `std`/`fast`, bitrate, and sound state.
3. Confirm every media reference is accessible and its role is written.
4. Count references against live limits.
5. Read the prompt once as visible/audible instructions only.
6. Remove old scene numbers, `as before`, contradictory camera moves, stale references, speech, score, and model-rendered text.
7. Calculate the exact credit cost.
8. Present prompt, settings, references, and cost to the human.
9. Generate only after explicit approval.

### Phase 6: Generate and save dailies

Quality-first CLI shape after approval:

```powershell
higgsfield generate create seedance_2_0 `
  --prompt "<approved prompt>" `
  --start-image "<path>" `
  --image "<canonical reference path>" `
  --aspect_ratio 9:16 `
  --duration <4-15> `
  --resolution 4k `
  --mode std `
  --bitrate_mode high `
  --generate_audio true `
  --wait
```

Add end/video/reference flags only when the packet calls for them. The manual website path uses the same values.

Save immediately as:

```text
footage/generated/<SHOT>_vNNN_seedance2_std_4k_sound.mp4
footage/generated/<SHOT>_vNNN.md
```

The companion record retains the exact prompt, parameters, reference paths/roles, cost, result path, and later review verdict. Never overwrite a take.

### Phase 7: Review every take

Review in this order:

1. Watch once at normal speed without pausing for story/emotion.
2. Watch again for identity, anatomy, contact, object survival, physics, and camera.
3. Inspect opening, middle, and final frames at full resolution.
4. Compare subject identity with the canonical asset, not with a potentially drifted prior video frame.
5. Compare location/bridge state with its canonical reference.
6. Solo the native audio and verify each foreground sound is synchronized.
7. Check for generated speech, music-like material, clicks, warbles, sudden ambience changes, or fake off-screen action.
8. Compare the cut-in and cut-out against adjacent storyboard shots and the animatic.
9. Record PASS/FAIL/NEEDS-HUMAN with timestamps and evidence.

Do not promote a take because the thumbnail looks good.

### Phase 8: Iterate scientifically

Classify the failure:

- **Systematic:** the same failure repeats. Change one causal variable: keyframe, reference, prompt action, camera, duration, or shot design.
- **Stochastic:** failures vary and near-keepers appear. Freeze the packet and roll a small approved candidate batch.

Use this diagnostic order:

1. Subject/identity.
2. Action/contact/physics.
3. Camera/framing.
4. Style/light/color.
5. Audio.
6. Output quality.

Fallback rules:

- Repeated contact fusion → split into reaction + insert.
- Tiny object disappears → enlarge it, slow the action, keep it in frame, or use an insert.
- Large start/end morph → reduce layout delta or split the shot.
- Camera jitters → use one slower move or lock the camera.
- Background drifts → restore one correct location reference and remove competing plates.
- Native audio invents speech/music → restate diegetic-only physical sources; if the visual is the keeper, replace audio in post with an exception record.
- Text/logo fails → move it to deterministic post; never keep rerolling the video model.

### Phase 9: Promote a select

A take becomes `footage/selects/<SHOT>.mp4` only when:

- All blocker criteria pass.
- Major defects are accepted or resolved.
- Native SFX is usable or a documented replacement plan exists.
- The shot cuts with its neighbors.
- Director/human verdict is recorded.

Copy the take; do not move or rename away the raw original. Update `shot-tracker.md` with the exact source version and evidence path.

### Phase 10: Assemble and mix

1. Replace animatic frames with approved selects while preserving narration-led timing.
2. Trim clips at whole frames; preserve short visual handles where available.
3. Extract retained native audio beds into `audio/sfx/generated/`.
4. Build a continuous SFX/ambience edit; smooth ambience across cuts with room tone and crossfades.
5. Add the one continuous narration stem.
6. Add music under narration, preserving headroom.
7. Add deterministic text, `राम`, stripe glow/reveal, captions, investing graphics, and ZebPay end card.
8. Apply final color matching and grain only after picture selection.
9. Run the existing frame-lock render and require `SYNC LOCKED`.
10. Review on headphones, phone speaker, and a larger display.

## 13. Quality-control rubric

### Blockers

Reject the take if any is present:

- Rama’s face/costume/reverent presence is materially wrong or drifts.
- The squirrel loses its species/proportions/three-stripe identity.
- Human hand, paw, body, or contact zone fuses, melts, or gains anatomy.
- Story-critical prop disappears or changes state incorrectly.
- Wrong bridge construction state or obvious environment replacement.
- Character appears to speak or generated voice is heard.
- Unwanted generated music masks later narration.
- Sacred/brand/financial text is garbled in-frame.
- Camera move or action contradicts the shot’s story purpose.
- Cultural depiction becomes comic, horror-coded, sexualized, or disrespectful.
- File is corrupt, wrong aspect, wrong duration, or contains unusable black/frozen frames.

### Major criteria

- Identity and wardrobe hold across the full motion.
- Lighting direction and grade match adjacent shots.
- Movement carries believable weight and contact.
- Camera follows the specified single move at stable speed.
- Native SFX events land on the visible actions.
- Ambience matches the location and does not jump unnaturally.
- Squirrel remains readable in mobile framing.
- Crowd remains varied and distant enough to avoid clone/melt artifacts.

### Minor/polish criteria

- Grain, edge softness, bloom, and sharpness match the approved look.
- Motion blur is plausible.
- Hair, fabric, fur, spray, and dust react consistently.
- Eyelines and screen direction cut cleanly.
- Audio tails and ambience can crossfade cleanly.

## 14. Shot-risk strategy for this film

| Category | Shots | Primary control | Fallback |
|---|---|---|---|
| Identity pilot | S1-a | Start frame + canonical Rama ref; minimal motion | Near-static shot or still/parallax |
| Scale/crowd | S1-b | Distant population + bridge/location anchor | Separate wide plate and editorial scale |
| Fast object/water | S1-c | Large boulder, slow readable arc, exact impact state | Splash still/parallax + post SFX |
| Small-object contact | S2-b, S2-c, S3-a, S5-c | Squirrel large; visible contact; slow action | Macro insert or two-shot edit |
| Two-character comedy | S3-e | Hard-gated short slow flick; larger pebble | Fingers insert + squirrel reaction |
| Rama walk | S4-b | Short action, canonical identity, simple tracking | Start/end cutaway pair |
| Hand/squirrel contact | S4-c | Minimal layout delta; palm grounded; macro; sound on pilot | Rama reaction + generic-hand squirrel insert |
| Stripe moment | S4-d | Stable stripes in Seedance; stroke only | Stripe reveal entirely in post |
| Rough surf | S5-b | Squirrel foreground; paw contact; moderate wave | Calmer surf plus stronger sound design |
| Bridge progression | S5-d | Correct state reference, slow pan | Still/parallax |
| Macro bridge payoff | S5-e | Deterministic Ken Burns/parallax | Already Mode B; no paid generation needed |
| Investing/brand | S6, S7-b | Deterministic motion graphics | Never Seedance |
| Final hero | S7-a | Perfect still first; near-static 4K with sound | Still/parallax with designed SFX |

## 15. Supercomputer operating guide

Supercomputer can help, but it should execute this production system rather than invent one.

### Setup

1. Create a project/chat named `Ramayana-ZebpaySIP`.
2. Provide the creative brief, this operating spec, and only the current shot packet.
3. Upload only the references named in that packet.
4. Tell it to propose the plan, model, parameters, reference roles, and exact cost first.
5. Require an approval pause before every paid step.

### Per-shot instruction shape

```text
Work on one shot only: <SHOT ID>.
Follow the attached operating spec and shot packet exactly.
Preserve the named canonical identity and location references.
Use Seedance 2.0 Standard with diegetic SFX/ambience only.
Narration and score are supplied separately in post.
First show the planned inputs, parameters, and exact credit cost.
Do not generate until I approve.
```

### Rules

- One shot, or one tightly connected two-clip continuation, per chat thread.
- Do not ask Supercomputer to make the whole film from the original script in one run.
- Download and log every accepted artifact locally; chat memory is not the source of truth.
- If it proposes a different model, require a written reason and a controlled comparison.
- Use previous video context only with the continuation/motion rules in this spec.
- Unlimited website access does not apply to Supercomputer; its generations are credit-based according to Higgsfield’s current official guidance.
- Current account authentication and `max` subscription were verified, but actual Supercomputer feature access must be confirmed in the UI.

Supercomputer is most useful after the production choices are locked: it can preserve context, hand an approved image into video, show costs, and reduce re-upload friction. It is not a substitute for the local versioned shot record or human keeper review.

## 16. Automation contract for later

Manual production becomes automatable only if each take records the same fields.

Minimum record:

```yaml
shot_id: S4-c
version: 1
source_revision: shooting-script-date-or-hash
surface: standalone-seedance
model: seedance_2_0
schema_checked_at: 2026-07-21T00:00:00+05:30
parameters:
  aspect_ratio: 9:16
  duration: 7
  resolution: 4k
  mode: std
  bitrate_mode: high
  generate_audio: true
references:
  - path: keyframes/S4-c_start_9x16.png
    role: start_image
  - path: keyframes/S4-c_end_9x16.png
    role: end_image
  - path: assets/characters/squirrel_front.png
    role: character_identity
prompt: "<exact approved prompt>"
estimated_credits: null
approved_by: null
output: footage/generated/S4-c_v001_seedance2_std_4k_sound.mp4
review:
  verdict: pending
  blocker_count: null
  notes: []
```

Future automation may fill fields, run read-only schema/cost validation, upload references, submit an approved job, download output, probe files, and create review frames. It may not remove the human cost approval, cultural review, or keeper gate.

## 17. Operational acceptance criteria

This manual method is ready to use when:

- The human accepts the audio override and surface-routing decisions.
- The fifteen 2:3 keyframes are conformed to exact 9:16 or deliberately replaced.
- Global look settings are approved.
- S1-a, S4-c, and a squirrel/pebble pilot pass with the new sound architecture.
- A companion generation record is used for every new take.
- The exact live schema and cost are checked before every paid generation.
- No take enters `footage/selects/` without a timestamped review verdict.

The film is complete only under the broader definition in `brief.md`: all planned shots have approved selects, narration/music/SFX are locked, deterministic graphics and captions are correct, creative/brand/legal reviews are recorded, the vertical master passes technical QC, and the human owner approves the export.

## 18. Research sources

Primary/current sources used for this operating method:

- [Higgsfield: How to Avoid Distortions in AI Videos (2026-07-18)](https://higgsfield.ai/blog/how-to-avoid-distortions-ai-videos) — multi-angle references, single-direction camera moves, locked lenses/light, location anchors, frame locks, hardest-shot-first.
- [Higgsfield: Cinema Studio 3.5 Full Tutorial (2026-07-15)](https://higgsfield.ai/blog/cinema-studio-3.5-full-tutorial) — current genre, color, camera-moveset, lighting, camera, lens, focal-length, and aperture controls.
- [Higgsfield: Generating with Seedance 2.0 (2026-06-24)](https://higgsfield.ai/blog/generating-with-seedance-2-0) — multimodal references, native sound, 720p diagnostics, one-variable iteration, full-clip review, image-to-video, and SFX prompting.
- [Higgsfield: Realistic AI Human Movement (2026-07)](https://higgsfield.ai/blog/realistic-ai-human-movement) — character/location/keyframe context, physical cause-and-effect, and previous-clip continuation.
- [Higgsfield: Seedance 4K VFX Workflow (2026-06-26)](https://higgsfield.ai/blog/VFX-with-Seedance-4k) — video motion/camera locking and diegetic-only SFX replacement.
- [Higgsfield: Seedance 2.0 Pricing and Modes (2026-06-24)](https://higgsfield.ai/blog/seedance-2-0-pricing-2026) — 4–15 second range, 480p–4K, Standard/Fast/Mini, reference/audio cost factors.
- [Higgsfield: Supercomputer Guide (2026-07-03)](https://higgsfield.ai/blog/higgsfield-supercomputer-guide) — plan → cost → approval → execution flow and artifact chaining.
- [Official Higgsfield CLI](https://github.com/higgsfield-ai/cli) — authenticated live model/workflow discovery and non-generating cost validation.

Platform marketing claims were treated as capability leads, not automatic proof of shot quality. The live authenticated schema and this project’s own playback/QC remain the production truth.
