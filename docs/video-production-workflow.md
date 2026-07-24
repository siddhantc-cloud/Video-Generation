# Idea-to-cinematic social-video workflow

This is the single human-readable source of truth for producing a cinematic social video from an
idea. Machine entrypoints, project templates, skills, and agent prompts link here instead of
repeating the procedure.

Non-technical companion deck: `docs/video-production-presentation.html`.

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Idea contract | Message, audience, platform, runtime, aspect ratio, and approval owner are explicit | `project/brief.md` | Producer / human | Required |
| Frozen script | One approved narration script is preserved before production adaptation | `scripts/source-script.md` | Human / script rewriter | Required |
| Audio clock | A continuous scratch narration defines the phrase and frame map | Phrase map and probed audio | Editor | Required |
| Visual system | Characters, locations, props, palette, camera character, and brand sources are approved | Asset records and contact sheets | Continuity / human | Required |
| Zero-spend proof | The complete keyframe animatic passes story, pacing, crop, and transition review | Encoded animatic and approval | Human | Required before paid motion |
| Shot routing | Every interval is classified as generative, deterministic, turnkey, or hold/reuse | `scripts/shot-tracker.md` | Director | Required |
| Spend control | Every Higgsfield job has current schema, quote, exact packet, attempt ID, and approval | Cost plan and job ledger | Producer / human | Required per paid job |
| Independent keeper gate | Every paid take is reviewed against criteria written before it existed | `review/takes/` | Reviewer | Required |
| Deterministic finish | Exact copy, numbers, graphs, captions, and logos are rendered outside the generative model | Render manifest and sources | Motion designer / editor | Required |
| Audio separation | Narration, native SFX, designed SFX, ambience, and music remain independently controllable | Audio manifest and stems | Editor | Required |
| Encoded QC | The actual review file passes probe, boundary, mix, caption, brand, and full-playback checks | QC report and human verdict | Reviewer / human | Required |
| Learning | New evidence updates the narrowest project record, then reusable skills only when justified | Learning diff and parity checks | Partner agent | Required |

## What this recipe produces

A 45–60 second vertical social film from a starting idea, with:

- a frozen source script and approved shooting script;
- a frame-locked narration phrase map;
- approved continuity assets and keyframes;
- a complete zero-Higgsfield-credit animatic;
- a costed Higgsfield motion plan;
- reviewed narrative motion selects;
- deterministic premium graphs, text, captions, and logo animation;
- separate narration, SFX, ambience, and music stems;
- versioned review cuts and one explicitly promoted final.

The canonical folder contract is `video-production-system/PRODUCTION_SYSTEM.md`. Create a new
workspace with `$script-video-bootstrap`; do not copy a previous film and clean it afterward.

## The production model

Treat the film as four lanes that meet only in the edit:

| Lane | Best tool class | What belongs there |
|---|---|---|
| Story clock | Narration + phrase map | Approved words, pauses, pronunciation, whole-frame timing |
| Organic picture | Higgsfield / Seedance | Characters, environments, physical action, camera motion, native diegetic SFX |
| Exact picture | HyperFrames / Remotion / FFmpeg | Graphs, claims, numbers, copy, captions, logos, exact brand geometry |
| Finish | video-use + FFmpeg/FFprobe | Conform, assembly, audio mix, caption burn, probe, hashes, delivery |

Do not ask a probabilistic video model to render what a deterministic renderer can make exact.
Do not use deterministic still motion as a substitute when the creative value is physical
performance, atmosphere, or camera movement.

## Phase 0 — Turn the idea into a production contract

1. Record the idea verbatim in `project/brief.md`.
2. Define one audience, one message, one call to action, and one emotional turn.
3. Lock the primary platform, aspect ratio, frame rate, target runtime, experiment resolution,
   brand/legal constraints, and approval owner.
4. Default social target only when the brief supports it: 9:16, 30 fps, 45–60 seconds.
5. Decide what must be literal and what may remain metaphorical.
6. Write acceptance checklist rows before creative prose.

### Idea-brief prompt

```text
Turn the idea below into a production brief for a 45–60 second social film.
Do not write shots yet. Return: audience, single message, emotional turn, call to action,
platform/runtime/aspect assumptions, literal requirements, metaphorical freedom, exact claims,
brand/legal questions, and approval gates. Mark every assumption.

IDEA:
<paste the idea>
```

## Phase 1 — Write and freeze the narration

1. Draft for spoken comprehension, not reading speed.
2. Remove duplicated setup and let images carry information already visible.
3. Separate narration, on-screen copy, native SFX, score intent, and legal/brand text.
4. Read it aloud and time it. A 60-second limit is a delivery constraint, not a word-count target.
5. Record every meaning-level change from the original idea.
6. Obtain human approval.
7. Preserve the approved script unchanged as `scripts/source-script.md`.
8. Put provider- and shot-friendly adaptation in `scripts/shooting-script.md`.

### Script-compression prompt

```text
Rewrite this idea as one continuous narration for a <runtime>-second social film.
Preserve the message and call to action. Use short spoken sentences, one idea per breath,
and one clear emotional turn. Remove repeated explanation. Do not invent claims.
Return: narration, estimated read time, on-screen copy kept out of narration, pronunciation
risks, and a change log against the source idea.

BRIEF:
<paste the approved brief>
```

## Phase 2 — Make audio the clock

1. Generate or record one continuous scratch narration.
2. Probe its exact duration.
3. Transcribe or align words with timestamps.
4. Quantize every phrase boundary to integer frames.
5. Give each phrase one visual owner. Deliberate visual overlap must be explicit.
6. Store the map in a machine-readable timeline plus a human-readable shot tracker.
7. Do not replace narration after this point without remapping every boundary.

The scratch voice may be replaced after picture lock, but the replacement must be conformed to the
approved phrase slots. Keep synthesis orthography separate from display copy so pronunciation
spelling never leaks into captions.

## Phase 3 — Build the visual bible and continuity assets

1. Inventory recurring characters, locations, props, wardrobe states, and brand sources.
2. Define stable invariants separately from shot state.
3. Create clean canonical references and multi-view sheets only for assets that recur.
4. Approve one look-lock frame and one small contact sheet before producing every shot frame.
5. Generate shot keyframes from the exact phrase map, not from a generic moodboard.
6. Register provider Elements only after local approval.
7. Use identical element names locally and in the provider workspace.

### Keyframe prompt template

```text
Create one photoreal 9:16 film keyframe for beat <ID>.
Story meaning: <what the audience must understand now>.
Canonical references: <character/location/prop invariants>.
Shot state: <pose, expression, weather, action phase>.
Composition: <shot size, screen position, depth, eyeline, negative space>.
Look law: <palette, motivated lighting, texture, performance register>.
Continuity: <what must match the previous and next frame>.
Keep the frame free of captions, logos, watermarks, and invented text.
```

## Phase 4 — Build the complete free animatic

1. Place every approved keyframe on its phrase-owned whole-frame interval.
2. Add only simple deterministic pan, push, hold, crop, and transition tests.
3. Insert rough deterministic graph/logo placeholders where those sections will live.
4. Render an encoded MP4 with scratch narration.
5. Inspect every boundary at `n-1`, `n`, and `n+1`.
6. Watch the full encoded animatic at phone scale with sound.
7. Fix script, timing, shot order, crop, and continuity here.
8. Record human approval before any paid motion.

The animatic is the first complete film. It is not a slideshow preview of work that has not yet
been designed.

## Phase 5 — Route and design the shots

Classify each frame interval:

- **Generative:** physical performance, organic environments, creatures, atmospheric motion,
  non-exact camera work.
- **Deterministic:** exact text, claims, numbers, charts, captions, logos, UI, or branded geometry.
- **Turnkey:** a bounded provider workflow with predictable output.
- **Hold/reuse:** a valid partial take, freeze, crop, speed change, or deterministic continuation
  can cover the interval without another generation.

For every generative unit:

1. Use the longest coherent duration that still has one subject, one primary action, and one
   camera idea.
2. Define start state, action landing, usable source range, and cut-friendly first/last frames.
3. Assign references by role:
   - canonical image for identity;
   - `start_image` for the exact continuity start;
   - `end_image` only when the landing composition matters;
   - previous accepted video only for true temporal continuation or motion reference.
4. Do not re-describe identity already carried by a reference. Prompt the motion delta.
5. Request only native diegetic SFX. Keep narration and score out of the shot.
6. Write measurable pass criteria before generation.
7. Flag reflections, crowds, multiple simultaneous actions, exact object transfers, text, and
   unintended internal cuts as high risk.

If a source keyframe must begin the motion, attach it as `start_image`, not a generic image
reference. A generic reference may influence appearance without anchoring frame one.

## Phase 6 — Write the Higgsfield packet

First inspect the current model schema and price. Model names, limits, and credits are time-sensitive.
For Seedance 2.0:

```powershell
higgsfield account status --json
higgsfield model get seedance_2_0 --json
higgsfield generate cost seedance_2_0 <the exact final parameters> --json
```

The immutable packet contains:

- shot ID and attempt ID;
- model and surface;
- aspect ratio, duration, resolution, mode, bitrate, and audio switch;
- exact prompt;
- reference paths/IDs, hashes, order, and semantic roles;
- live per-job quote and total authorized cap;
- expected pass conditions;
- previous-attempt delta, if any.

### Seedance image-to-video prompt template

Use positive statements and observable motion. When the start frame already contains the subject
and world, keep the prompt to the motion delta.

```text
<Subject> performs <one visible action> in one continuous shot.
Camera: <one primary move plus, at most, one texture modifier>.
Temporal arc: <opening state>; <motion development>; <landing state>.
Physics: <cloth, hair, water, weight, contact, or atmosphere that must move naturally>.
Audio: <one or two diegetic sounds tied to visible actions; room tone/ambience>.
Locks: identity, anatomy, wardrobe, prop geometry, lighting, and environment remain stable;
cuts occur only if explicitly specified.
```

For a true continuation, attach the previous accepted clip, begin with “The scene continues,”
describe only what happens next, and do not repeat the prior action. Cap chained extensions at two
before re-anchoring from canonical references.

Keep a Cinema Studio prompt within its current visible character budget. Put selectable UI controls
in the settings packet, not redundantly in the prompt body.

## Phase 7 — Generate one pilot, then the batch

1. Choose one representative high-value/high-risk shot as the pilot.
2. Use the approved model at the lowest supported experiment resolution. Do not substitute a
   different model merely because it is cheaper.
3. Re-run schema and cost preflight immediately before approval.
4. Submit one job once. Record its provider ID before monitoring.
5. Download, hash, and probe the raw result without overwriting.
6. Review it against the prior rubric.
7. If it fails structurally, change one diagnosed variable. Do not buy stochastic rerolls for a
   deterministic prompt/reference mistake.
8. After two consecutive structural failures in one shot class, redesign the shot or use a
   deterministic fallback.
9. Generate the remaining approved packets one at a time and preserve rejected attempts.

A 480p result validates prompt structure, blocking, reference contamination, and the actual take at
480p. It is not a seed-locked preview that can be re-rendered identically at 1080p. A higher-resolution
generation is a fresh performance and needs a new review.

## Phase 8 — Review and salvage before retrying

Run technical, visual, temporal, continuity, audio, and full-playback passes. Return `PASS`, `FAIL`,
or `NEEDS HUMAN`.

Before a retry, ask:

- Is the useful range long enough for the phrase interval?
- Can a deterministic hold, crop, retime, insert, or cutaway hide the failure?
- Can native ambience be supplemented in post?
- Is the failure local enough for a surgical edit?
- Does the shot need redesign rather than another roll?

The Ramayana production kept a short valid range from a take whose prop later disappeared and
covered the remainder deterministically. That is cheaper and more controlled than a blind reroll.

### Take-review prompt

```text
Review the encoded candidate against the pre-existing shot criteria.
Probe first. Inspect first frame, action landing, last frame, and any suspected failure range.
Judge technical integrity, identity/anatomy, object persistence, unintended cuts, camera/action
coherence, continuity, native SFX, and editability. Return PASS, FAIL, or NEEDS HUMAN, timestamped
evidence, the usable source range, and the smallest next action. Do not edit or regenerate.
```

## Phase 9 — Build premium deterministic graphics

1. Lock the exact frame interval, copy/data/logo sources, safe area, and adjacent frames.
2. Create a design frame before animation.
3. Use HyperFrames or Remotion for graphs, typography, claims, and logo animation.
4. Make motion a pure function of frame number.
5. Match the incoming and outgoing picture state.
6. Render and inspect the real encoded section, including boundary frames.
7. Insert the deterministic render into the picture while preserving the approved audio clock.

### Motion-graphics brief prompt

```text
Design a premium deterministic <graph/logo/copy> section for frames <start>-<end> at <fps>,
<width>x<height>. Exact content: <copy/data/logo source>. Incoming state: <description/frame>.
Outgoing state: <description/frame>. Define hierarchy, grid, typography, palette, depth, motion
beats, easing, dwell time, and safe area. All text, values, and brand geometry must be exact.
Render seek-safe motion as a pure function of frame number and provide boundary-QC evidence.
```

## Phase 10 — Replace narration and finish audio

1. Audition difficult names, acronyms, and brand terms before a full TTS request.
2. Generate one continuous final narration after copy lock.
3. Preserve provider timing metadata and a versioned pronunciation dictionary.
4. Conform narration by whole phrase to the approved frame slots; do not globally time-stretch the
   entire performance unless measured semantic drift remains acceptable.
5. Derive captions from the conformed final narration.
6. Keep native SFX, designed SFX, ambience, and music on separate stems.
7. Use rights-cleared music for the final; demo music is not campaign approval.
8. Duck music under speech instead of globally making narration louder.
9. Measure the encoded mix, but keep human listening as the tone/pronunciation gate.

## Phase 11 — Assemble, QC, and promote

1. Build a frame manifest containing hashes, source ranges, layer order, transforms, and audio routing.
2. Assemble only approved ranges.
3. Add deterministic graphics.
4. Mix narration, SFX, ambience, and music.
5. Add captions last.
6. Render versioned clean and captioned review cuts.
7. Probe runtime, dimensions, frame count, frame rate, codecs, streams, loudness, and true peak.
8. Inspect all modified boundaries and watch the entire encoded file at delivery scale with sound.
9. Obtain separate creative, pronunciation, music-rights, brand, legal, and regulatory approval
   where applicable.
10. Promote one exact review cut to `deliverables/final/`; record SHA-256 and source verdict.
11. Add a final to Git LFS only when the owner explicitly requests repository delivery.

## Dated Higgsfield credit model for a similar 52.2-second film

Verified through the authenticated Higgsfield CLI on **2026-07-24**, account-plan-specific and
subject to change:

| Seedance 2.0 Standard tier | Live rate in tested 4–15 second range | 49 generated source seconds |
|---|---:|---:|
| 480p | 3 credits/second | 147 credits |
| 720p | 4.5 credits/second | 220.5 credits |
| 1080p | 9 credits/second | 441 credits |

Tested with 9:16, `mode=std`, high bitrate, and native audio on. In the tested matrix, audio on/off
and high/standard bitrate did not change the quote. A six-second job with an explicit `start_image`
also retained the same per-second quote. Recheck all of this live before spending.

The reference film's eleven keeper sources were 6, 4, 4, 4, 4, 4, 4, 4, 5, 4, and 6 seconds:
49 billed seconds total. The deterministic graph and logo occupied about 14 seconds of the final
52.2-second timeline and used no Higgsfield video credits.

| Budget interpretation | 480p credits |
|---|---:|
| One learned-path keeper pass | 147 |
| Actual final-path experiment (147 keepers + one 6s rejected setup) | 165 |
| Practical repeat reserve (about 1.5–2 passes) | 221–294 |
| Spend recorded in the current ledger, including an abandoned 100-credit Cinema Studio pilot | 265 |

For native 720p or 1080p, multiply the same 49-second source plan by the live rates above. A
practical 1.5–2-pass reserve is about **331–441 credits at 720p** or **662–882 credits at 1080p**.
These are planning caps, not promises of acceptance.

Higgsfield credits exclude still-image generation outside Higgsfield, TTS/provider charges, music
licensing, labor, local compute, storage, and optional upscaling. The current 1080x1920 social cut
uses 480p narrative generations inside a 1080p deterministic timeline; it is suitable for
low-cost direction/consistency evaluation but is not equivalent to native 1080p source footage.

## How the repeat gets cheaper

1. Reuse the project scaffold, phrase-map schema, review rubrics, and render manifests.
2. Reuse approved visual laws and shot classes, never campaign-specific characters or claims.
3. Generate stills and the full animatic before video spend.
4. Keep exact material deterministic.
5. Reuse known-good `start_image` role, duration classes, and prompt shapes.
6. Price by generated source seconds and expected attempts, not final runtime.
7. Pilot a new failure class once before batch work.
8. Keep partial usable ranges and solve local defects in post.
9. Change one diagnosed variable per retry.
10. Record every rejection so acceptance rate, not optimism, sets the next budget.

## Role and skill routing

| Stage | Atomic agent/prompt | Skill |
|---|---|---|
| Idea and narration | `script-rewriter` | `$script-video-bootstrap`, `$script-video-plan` |
| Shot feasibility | `assistant-director` | `$script-video-plan` |
| Pre-take rubric | `scene-expectations` | `$script-video-review` |
| Spend gate | `prompt-reviewer` | `$script-video-generate` |
| Assembly and graphics | `video-editor` | `$script-video-motion-graphics`, `$script-video-post` |
| Independent verdict | `video-reviewer` | `$script-video-review` |
| Evidence promotion | Partner agent | `$script-video-learn` |

No role certifies its own output. Provider-specific prompt work also reads the current `higgsfield`
root skill and its routed Cinema, Seedance, prompt, model, stack, audio, recall, and assist guidance.

## Evidence destinations

- Project facts and jobs: `<project>/project/`, `<project>/footage/`, `<project>/review/`.
- Reusable workflow: this document; project structure and tool routing:
  `video-production-system/PRODUCTION_SYSTEM.md`.
- Reusable atomic behavior: `.codex/skills/script-video-*` and
  `video-production-system/agents/`.
- Provider-navigation facts: the project's provider navigation runbook.
- Dated provider prices: the project cost plan, always with verification date and command.
