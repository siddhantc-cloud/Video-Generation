# Gate A - Assistant Director pre-generation risk audit
## "The Squirrel in Ram Setu" (ZebPay SIP) - Seedance 2.0 image-to-video, silent

**Auditor:** assistant-director. **Advise only:** no generation, no credit spend, no script edit. **Date:** 2026-07-08.
**Audited artifact:** `01_script_AIFRIENDLY.md`. **Creative truth (not re-opened):** `00_input_script_HUMAN.md`.
**Locked facts honored:** Seedance 2.0 i2v, silent (generate_audio=false), start+end keyframes + image_references, photoreal grounded-mythic look, single ElevenLabs VO, no lip-sync, ~20 to 21 Mode C shots + Scene 6 and logo card as Mode B, character bible already generated.

---

## VERDICT

**REVISE (one light pass).** Creative intent is fully protected and the hardest failure modes are already decomposed well. The balance leans slightly too far toward "trust the plan" on five staging/asset items that photoreal will expose: (1) confirm a **bridge-state reference set exists** (continuity across ~15 shots), (2) confirm the Rama/squirrel locks are **multi-angle sheets, not expression-only**, (3) shrink the **S4-c keyframe layout delta** (biggest morph risk), (4) promote the **S4-d stripe reveal to a Mode B overlay** as the primary method, (5) fix the **S1-b two-move camera**. None are blockers. Fix these and it is BALANCE ACHIEVED.

---

## Model + research delta (live check, 2026-07-08)

Engine/interface confirmed: **Seedance 2.0 i2v on Higgsfield, silent.** What live research surfaced vs the file's baked notes:

- **Keyframe morph is driven by LAYOUT DELTA, not just speed.** The named fix is "keep framing, scale and subject placement close between start and end so the model interpolates MOTION, not a layout change"; large layout jumps produce melting / glitching / smearing. This is the sharpest new lever and it indicts the S4-c and S1-c keyframe pairs (big positional teleports), which the file does not yet address. ([wavespeed morph/jitter](https://wavespeed.ai/blog/posts/blog-fix-flicker-jitter-seedance-2-0/), [seedance FLF guide](https://www.seedance.tv/blog/seedance-first-and-last-frame))
- **A single reference gives a "2D read"; a multi-angle canonical sheet (front / profile / three-quarter, neutral light) is what actually anchors identity.** Optimal is **1 to 3 character refs, 3 to 5 total**, and "reduce to the 3 most consistent" if a face drifts. Confirms the "attach only the characters in the shot" rule and adds: the Rama/squirrel LOCK must be angle-coverage, not expression-only. ([magichour reference guide](https://magichour.ai/blog/seedance-20-reference-guide), [stensyl consistency deep-dive](https://stensyl.ai/blog/seedance-2-character-consistency-workflow-breakdown))
- **Disappearing / floating objects and warped hands hit ~10% of COMPLEX-action generations; water physics is accurate only for STANDARD scenarios and breaks on fast/complex.** Validates the H flags on 3e, 4c, 1c, 5b and the "keep it slow, keep the subject large" mitigation. ([wavespeed 5 issues](https://wavespeed.ai/blog/posts/seedance-2-0-review-issues-and-alternatives/))
- **Motion corruption comes from UNDER-constrained movement** (no clear single move, no constant speed, no stability rule = the model invents jitter). Supports the one-move rule and argues for adding explicit speed/stability language to prompts + negatives. ([wavespeed](https://wavespeed.ai/blog/posts/blog-fix-flicker-jitter-seedance-2-0/))
- **Content filters:** real-face and IP filters are strict, but there is NO documented block on original mythological / Hindu-deity characters. Rama is an original design, so filter risk stays low; the only untested piece is a photoreal deity FACE through the Seedance video filter (the still was proven on ChatGPT image-gen, a different engine). Pilot-confirm, do not assume. ([mindstudio restrictions](https://www.mindstudio.ai/blog/seedance-2-0-content-restrictions-workarounds))
- **Contradiction with a common fear, in our favor:** feature-averaging blend is worst between SAME-species / similar references. Our two-reference contact shots pair morphologically distinct subjects (Rama+squirrel, vanara+squirrel), so identity-BLEND risk is lower than the file implies; the real risk on those shots is contact-zone morph + the tiny object, not a hybrid creature. Re-weight the mitigations accordingly.

Nothing contradicts the locked 2.0 decision (2.5 not on Higgsfield). No change to engine binding.

---

## Prioritized findings

Severity: **blocker** (would break the film / waste the batch) > **major** (visible defect likely in photoreal) > **minor** (polish / cheap insurance). Ordered worst-first.

| # | Shot(s) | Risk | Severity | Recommended story / staging fix (intent preserved) | Human decision? |
|---|---|---|---|---|---|
| 1 | Bridge (S1-b, S1-c, S2, S3, S4, S5-d, S5-e, S7-a) | The "already generated" bible list is Rama + squirrel + lead vanara + expression refs. **A bridge-state reference set is NOT in that list.** The bridge appears in ~15 shots and must read as ONE structure evolving (empty sea, first boulders, half-built + pebble line, completed golden bridge). With no bridge lock attached, the structure will drift into a different rock pile every shot. | major | Before Gate B, generate and lock a **4-state bridge reference set** (matching bible plan section 6) and attach the matching state to every bridge shot. Zero intent change; pure continuity insurance. | YES: confirm the asset exists / commission it |
| 2 | Rama + squirrel locks (all their shots) | A single image gives a "2D read"; identity needs **front / profile / three-quarter** angle coverage. The bible is described as "expression refs," which is range, not ANGLE coverage. Photoreal makes any residual drift obvious (Q1 #1 risk). | major | Confirm each identity lock is a **multi-angle sheet (front + three-quarter + profile, neutral light)**, not only expression variants. Attach **1 to 3 of the most consistent Rama refs** per Rama shot (never all four characters). If a face drifts in a pilot, drop to the 3 most consistent. | YES: confirm sheet coverage before Gate B |
| 3 | S4-c (Rama's palm lifts the squirrel) | **Largest keyframe LAYOUT DELTA in the film:** start = squirrel on the ground / a pebble, end = squirrel resting in the cupped palm. That is a big positional teleport, and the confirmed morph driver is layout change between keyframes, giving melting / palm-squirrel fuse. Compounds the two-character contact risk. | major | Shrink the delta: stage the START frame with the squirrel **already at the edge of Rama's flat, ground-resting palm** (paws on the palm), and the END frame as the same palm lifting slightly with the squirrel settled. The model then interpolates a small settle-and-lift, not a teleport. Keep Rama's FACE partial / out of frame (macro on hands) so there is less face to drift. Keep pilot-first (Gate C) and the two-shot cutaway fallback. | Director staging call |
| 4 | S3-e (tight two-subject flick) | User locked the tighter framing (vanara fingers + squirrel face + tiny flicked pebble). The real H risk is **tiny fast object vanish/warp** (~10% glitch on fast small-object motion), NOT identity blend (vanara and squirrel are different species, so blend is L). The file over-weights blend and under-weights object-survival. | major | Keep the tight framing as the **pilot attempt** (honor the user's call), but re-tune for object survival: (a) make the pebble a **slightly larger small stone**, (b) make the flick **SLOW and short** so the END frame still shows the stone **large and near-frame mid-arc** (not a fast cross-frame exit where it disappears), (c) gate it hard: if the stone warps/vanishes by attempt 2, drop to the robust two-shot (macro insert of fingers flicking a stone + separate squirrel-reaction cutaway). The two-shot fallback is sound. | Director: confirm pilot-then-fallback discipline |
| 5 | S4-d (stroke + three-stripe reveal) | The single most delicate VFX beat. Even "soft brightening along the stroke path" is a texture animation the model tends to render as a smear (motion-blur feature smear is a named artifact). The stripe reveal as a generated morph is the fragile part, not the stroke. | minor (fallback exists), promote to primary | **Promote the Mode B overlay from fallback to PRIMARY:** generate the Seedance stroke with the stripes **already faintly present and unchanging** (no in-clip reveal), then animate the three-stripe brightening as a **Mode B overlay in post** on the locked still/clip. This removes the morph risk entirely and preserves the R7 beat 100%. Keep the two-character contact slow; keep Rama's face out of the macro frame. | Director: approve making the reveal a post overlay |
| 6 | S1-b (vanara sena reveal) | Camera reads "slow crane-up drifting back" = **two moves (vertical crane + dolly back)**, violating the one-move golden rule, giving jitter/morph risk on a wide photoreal crowd. | minor | Pick ONE move: a single slow **aerial pull-back** (reveals scale) OR a single **crane-up**, not both. Keep the "thousands" crowd loose and at distance; do NOT let any move bring individual crowd faces to macro (photoreal non-human crowd faces warp up close). | Director staging call |
| 7 | S1-c (boulder hurl + splash) | Triple-stacked: fast motion + big layout delta (mid-air boulder to splash plume) + water physics (accurate only for standard cases). Marked med; behaves closer to med-high. | minor (fallback sound) | Keep the boulder **large in frame** and the arc **slow**; end on the splash plume with the boulder still readable, not a fast vanish. Keep the documented fallback (locked splash-moment still + short Ken-Burns, Mode B). Confirm the keyframe does NOT try to render legible "Ram's name" TEXT on any boulder (VO carries the name; Seedance garbles text, so keep any marking illegible/distant or a Mode B overlay). | No: staging note |
| 8 | S5-b (squirrel in rough surf) | Small subject in water = float/vanish. | minor (handled) | Already good: squirrel large/foreground, moderate waves, end on firmer ground, calmer-surf fallback. Add: keep the squirrel's **paws visibly in contact** with wet sand / a rock so it does not read as floating. | No |
| 9 | All Rama shots | The file phrases S1-a as "this shot ESTABLISHES the Rama lock." The canonical lock is the **bible sheet (already generated)**, not the S1-a video output. Matching later shots to a drifted S1-a frame would compound drift. | minor | Clarify discipline: every Rama shot attaches the **same clean bible sheet**; match the KEYFRAME STILLS (built in Nano Banana from the sheet) to each other, never re-derive the canonical from a video frame. Same for the squirrel. | No: discipline note |
| 10 | All Mode C prompts | Negatives cover jitter/flicker/drift/bent-limbs but miss the **named Seedance artifacts**; motion is under-constrained on speed/stability. | minor | Add to every negative list: **avoid morphing, avoid melting, avoid disappearing objects, avoid extra limbs, avoid warped hands.** Add positive stability language to each prompt: **"smooth, slow, constant-speed motion; stable framing."** Cheap insurance against invented jitter. | No |
| 11 | Rama shots (filter) | Photoreal deity FACE animated through the Seedance video filter is untested (the still was proven on a different engine). Low risk, but a batch-killer if it flags. | minor | **Pilot one Rama animation early** (S1-a) to confirm BOTH the drift ceiling AND that the content filter passes a photoreal deity face, before batching the other Rama shots. Keep the depiction reverent. | No: pilot ordering |
| 12 | S5-e (macro no-morph) + O2 | Correctly re-specced as a camera push on a LOCKED still, not a morph. Can be a near-free Mode B Ken-Burns/parallax push. | minor (already resolved) | Approve O2: render S5-e as a **Mode B Ken-Burns push** on the locked macro still. Same visual, saves one paid clip, zero morph risk. | YES: approve O2 |

---

## What is already well-handled (do NOT over-correct)

- **Scene 3 decomposition** (five actions to five one-action shots S3-a..e) correctly kills the named "beat density" failure. Keep it.
- **S1-c and S2-b/c multi-action compression** (lift/carry and scurry live in the cut) is the right call; do not re-expand them into single clips.
- **Per-character reference attach** (never all four) is exactly right and research-backed; the two-reference contact shots pair distinct species, which LOWERS blend risk.
- **Text to Mode B** (logo card, kinetic type, Scene 6) correctly avoids Seedance's unreliable in-video text. Keep.
- **Single external VO, generate_audio=false, no lip-sync** is the correct audio architecture; the reasoning for not using native audio is sound and verified. No dialogue to add.
- **Punctuation hygiene** (no em-dashes/ellipses in prompts; ellipsis kept only as a TTS pause with break tags) is correctly handled; VO is verbatim.
- **One-move camera rule** is applied cleanly on all shots EXCEPT S1-b (finding 6). The Rama expression band (serene to tender only, no big swings) is already drift-friendly; keep it narrow.
- **Pilot-first on S4-c and the documented per-shot fallbacks** (two-shot cutaways, locked stills, calmer surf) are the right structure; my notes tighten them, they do not replace them.
- **Creative intent is 100% preserved** (VO verbatim, R7 stripe beat kept, mockery-to-reverence arc intact, photoreal/9:16/single-VO honored). Nothing here asks to cut a beat.

---

## Decisions the Director / human must make

1. **Bridge-state reference set (finding 1):** confirm it already exists, or commission a 4-state bridge lock before Gate B. This is the top continuity gap.
2. **Identity-lock angle coverage (finding 2):** confirm the Rama and squirrel locks are multi-angle sheets (front/profile/three-quarter), not expression-only.
3. **S4-c keyframe restage (finding 3):** approve staging the start frame with the squirrel already at the palm edge (small settle) instead of a ground-to-palm teleport.
4. **S3-e pilot-then-fallback (finding 4):** confirm the tight framing runs as a hard-gated pilot (larger stone, slow flick) with the two-shot cutaway ready if the object warps by attempt 2.
5. **S4-d stripe as a Mode B overlay (finding 5):** approve making the three-stripe reveal a post overlay (primary), with Seedance stroking a stripe-stable squirrel.
6. **O2 for S5-e (finding 12):** approve the near-free Mode B Ken-Burns push.
7. **Pilot ordering (finding 11):** approve piloting one Rama shot first to confirm drift + filter before batching.

Fix findings 1 to 6 and the plan reaches BALANCE ACHIEVED. Findings 7 to 12 are cheap insurance that can be applied during keyframe build.

---

*No em-dash characters used. Advisory only: no media generated, no credits spent, no edits made to either script file.*
