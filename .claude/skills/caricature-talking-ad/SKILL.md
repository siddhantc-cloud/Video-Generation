---
name: caricature-talking-ad
description: "Produce a multi-scene 3D-caricature talking-character ad (So Sorry / Krishna's-SHAPEFIX 'ingredient army' style) with consistent characters and clean native lip-sync. Use when building an animated mascot/ingredient ad where cartoon characters speak Hindi/Hinglish dialogue across scenes. The validated pipeline: locked character-ID reference images → speaker-focused keyframe per scene → Veo 3.1 native-audio dialogue (colon syntax, half-second pause, no-subtitles, one-speaker mouth-guard) → crossfade assembly. Composes with higgsfield-cinematic (models) and the project's Hindi script. NOT for realistic human UGC (that's audio-first-reel) or face-detection lip-sync (LatentSync fails on cartoons)."
metadata:
  version: 1.0.0
  updated: 2026-06-12
  proven-on: "Clear Gut ingredient-army ad, scenes 1-2 (D:/startup_dev/so_sorry/simple_ads/production_v2)"
---

# Caricature Talking-Ad Pipeline (validated 2026-06-12)

Hard-won across a long build. Each rule below fixed a specific failure — don't skip them.

## Engine decisions (settled)
- **Video+voice = Veo 3.1 (`veo3_1`)** — it generates speech AND the matching mouth together = real lip-sync. (Kling's Hindi audio is garbage; ElevenLabs/overlay is never lip-synced; LatentSync's face-detection FAILS on cartoon faces — all dead ends, see [[hinglish-tts-bakeoff]].)
- Veo on Higgsfield CLI takes a **single `--image` (start frame) only** — no end-frame/multi-shot. Drive motion via prompt; get consistency from the keyframe.
- Keyframes/character refs = **Nano Banana Pro (`nano_banana_2`)**, up to 14 image refs.

## The 4 rules that make it work
1. **Character IDs = locked reference images.** Generate ONE clean single-character sheet per character on a neutral background (`bible/<char>.png`); pass the relevant ones as `--image` refs into every keyframe. This is what keeps characters identical across scenes (independent text-gen → morphing, the v1 failure).
2. **Speaker-focused framing (the big one).** Veo animates the mouth of EVERY prominent character in frame → wrong characters appear to talk. Fix: each dialogue line is a shot where the **speaker is LARGE in the foreground facing camera** and everyone else is **smaller/in the background**. Reference Krishna ad does exactly this — one focused shot per ingredient. Group/team shots only at non-dialogue beats (or a unison shout). **Narrated group/resolution shots: a character can still turn to the lens and OPEN its mouth even from a mouth-closed/profile keyframe (Veo re-poses it) → reads as if it's talking under the VO. Stage such characters in HARD profile or minimized/fully turned away, not just "three-quarter"; expect re-rolls and flag for review.** (Burned on the Clear Gut S8 stomach, 2026-06-13.)
3. **Veo dialogue syntax** (clean lip-sync, no burned text):
   `<Speaker> looks at camera and says in a <tone> Hindi voice, natural lip sync, line begins after a half-second pause: देवनागरी लाइन`
   - **colon** triggers lip-sync · **Devanagari** for correct Hindi · **"line begins after a half-second pause"** kills cold-start clipping · ONE short line per clip.
   - **NO hyphens or dashes (`-` `—` `–`) inside the SPOKEN line** — Veo VOICES them as a word/sound, garbling the audio. Use a comma, a full stop (`।` / `.`), or just rephrase so the pause is implied. (Burned 2026-06-13: em-dashes in the S3/S6/S7 lines came out as junk audio.)
   - Append the **mouth-guard**: `Other characters keep their mouths firmly CLOSED and stay SILENT, only reacting with expression.`
   - Append negatives: `no subtitles, no captions, no on-screen text` (else Veo burns Devanagari text on screen).
   - Audio layer: one line + `Ambient: faint <scene> room-tone, no music` (don't overload). Also append `no audience, no laugh track` (Veo hallucinates a sitcom laugh-bed on comedic/laugh shots).
   - **Audio-bed leakage (don't let visual words become sound):** sound-suggestive descriptors in a `no music` prompt — "swell", "chime", "uplifting", "thunder", "soft chime" — get SYNTHESIZED as audio by Veo. Mark them visual/POST: `golden shimmer (visual only); any swell/chime is added in post — generate NO music`. (Both prompt-authoring agents tripped on this; caught by prompt-reviewer 2026-06-14.)
   - **Mouth-guard must reconcile with who's actually in frame:** if a non-speaking figure IS visible (e.g. a faceless stomach silhouette behind the King), do NOT write "no other character is visible" — it contradicts the frame, so Veo either drops the figure or animates a 2nd mouth. Write `only <Speaker>'s mouth moves; any other figure is faceless, mouthless and silent`. (Same 2026-06-14 catch.)
4b. **Zero-cost product-fidelity fix (no re-gen):** when Veo's bottle in a STATIC-camera scene isn't the real product, composite the REAL photo in programmatically. (a) Crop the front view; flood-fill the white bg inward from the borders (PIL `ImageDraw.floodfill`, low thresh ~22) + `scipy.ndimage.binary_fill_holes` so the white LABEL/dropper stay opaque → clean transparent cutout. (b) Build a "glowing product" sprite = cutout on a soft warm radial halo (small ellipse + heavy Gaussian blur, transparent margins → no visible box). (c) `overlay` it over the AI bottle on the per-clip video sized to fully cover it (overlay `shortest=1`, `-c:a copy` so audio is untouched), fade-in for "reveal" scenes. Then re-assemble + re-burn captions. Works because static-camera clips need no motion tracking. (Proven on Clear Gut S7/S8, 2026-06-13.)
4. **Assembly = crossfade.** Normalize clips to uniform 1080×1920/24fps, then `xfade` (video) + `acrossfade` (audio), ~0.4s. The half-second dialogue pause means the speaker's silent lead-in overlaps the previous tail → no dialogue collision. Then: music bed → **gold karaoke captions burned LAST** (skill `video-captions-karaoke` — Veo generates caption-free via the no-subtitles negative; we add controlled on-brand captions in post) → **end on a clean real-product still card** (Veo blurs the bottle label in motion, so the guaranteed-perfect brand moment is an ffmpeg Ken-Burns card from the real product PNG).

## Orchestration
Multi-scene runs follow a Director + subagents flow with human gates (plan → bible → keyframes [gate] → animate [pilot gate] → captions → edit → verify). Full diagram + role/QA checklists: the project's `workflow.md`. Subagents fan out per-scene keyframe/animation/QA; the Director owns script, prompts, spend gates, and final assembly.

## Per-scene procedure
1. Compose speaker keyframe: `nano_banana_2 --prompt "<speaker> LARGE foreground facing camera; <others> smaller in background, mouths closed; <setting>" --image bible/<speaker>.png --image bible/<other>.png ...`
2. Animate: `veo3_1 --image <keyframe> --duration 8 --aspect_ratio 9:16 --quality high --prompt "<shot> ... <dialogue block per rule 3> ... <mouth-guard> ... no subtitles..."`  (audio is NATIVE — no separate VO).
3. Frame-chain optional: compose next scene's keyframe continuing positions.

## Op notes (cost + reliability)
- Cost (verified 2026-06-13): keyframe `nano_banana_2` = **2 cr**; `veo3_1` **`--model veo-3-1-preview --quality high --duration 8` = 58 cr/clip** (fast/basic is cheaper ~22). A full 8-clip ad ≈ 16 cr keyframes + ~464 cr Veo. `account status` / `account transactions` audit spend — check before AND after a batch.
- **CLI batch-submit money rules (learned the hard way — a parse bug caused ~640 cr of duplicate jobs):**
  1. `generate create <model> --json` WITH `--wait` returns an array of **objects** (`[{"id","status","result_url",...}]`). WITHOUT `--wait` it returns a bare array of **id strings** (`["<uuid>"]`). VERIFY the response shape with ONE call before scripting a batch — don't assume.
  2. **NEVER auto-retry a `create` call on parse failure.** A "failed parse" is usually a *successful, charged* submission you misread → the retry creates a duplicate paid job. Retry ONLY when the response explicitly says `rate_limit_reached` (that means NOT created → safe to retry).
  3. Concurrency cap (ultra plan) = **8 jobs**; exceeding it returns `{"error_type":"rate_limit_reached"}` (no charge). Submit ≤8, or stagger.
  4. Robust pattern: submit each (no `--wait`) → save the id → poll `higgsfield generate list --size 120 --json`, match by `id`, download `result_url` when `status==completed`. `--wait` works but its long poll can 502 *after* the job is charged+rendering — recover such clips from `generate list` by id (don't resubmit).
- **Capture URLs robustly:** pull from `higgsfield generate list --json` and match by job id — never rely on `tail` (truncates) or `&`-parallel (interleaves/loses output).
- Verify every clip: extract 2-3 frames (speaker mouth moving? others' mouths closed? no burned subtitles? characters consistent?) + whisper-transcribe the final (lines present, in order). Stills + transcription are all the agent can verify — **motion smoothness and voice quality need the user's eyes/ears**; never declare those "verified."
- Lip-sync on cartoons is approximate (loose mouths) — acceptable for the style; don't chase perfection.

## Full reference
Scene blocking + dialogue: project `simple_ads/production_v2/SCENE_DIRECTION.md` (Hindi) + `VEO3_UGC_GUIDE.md` (prompt recipes + sources). Character bible: `production_v2/bible/`.
