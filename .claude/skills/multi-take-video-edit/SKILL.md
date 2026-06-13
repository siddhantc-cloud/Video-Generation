---
name: multi-take-video-edit
description: "Orchestrate a full edit from a folder of takes to a finished, graded, overlay-titled video — the 'Fable launch video' method: transcribe every take locally (Whisper word timestamps), subagent-per-scene take selection with written rationale, a JSON EDL as the single source of truth, ffmpeg frame-accurate cut+concat, optional LUT grade, Remotion graphics cued off transcript timestamps, and self-verification by re-transcribing the cut. Works for ANY source — real camera footage (multiple takes, ums, log color) or AI-generated clips (Higgsfield/Kling/Veo segments). Use when the user has multiple takes/clips to assemble into a final video, says 'stitch these', 'pick the best takes', 'edit my recordings into the final cut', or wants an EDL-driven edit. For tightening ONE long recording use cut-video; for open-ended conversational editing with ElevenLabs transcription use video-use."
metadata:
  version: 1.0.0
  updated: 2026-06-12
  source: "https://thariqs.github.io/cc-video-editing-deck/ (How Fable Edited Its Own Video, June 2026)"
---

# Multi-Take Video Edit (the Fable method)

**Core idea: the edit is text.** Transcripts are JSON, the edit decision list is JSON, the grade is a `.cube` text file, the graphics are React components, the cue sheet greps word timestamps. No timeline, no project file — so the agent can read it, diff it, verify it, and re-render it. 17 takes / 25 GB went to a finished 4K 3:00 in 4 days with zero video editors opened.

## Division of labour (don't duplicate)

| Job | Use |
|---|---|
| Tighten ONE long recording (strip silences/ums, keep laughs) | `cut-video` skill (local Whisper+MFA) |
| Open-ended conversational editing, ElevenLabs Scribe transcripts | `video-use` skill (needs `ELEVENLABS_API_KEY`) |
| **Folder of takes → selected, stitched, graded, titled final cut** | **this skill** |

Borrow `video-use`'s hard rules when rendering — they're correctness, not taste: subtitles LAST in the filter chain · per-segment extract then lossless `-c copy` concat · 30ms audio fades at every boundary · never cut inside a word · pad cut edges 30–200ms.

## Does the video source matter? (mostly no — these adaptations)

The pipeline is source-agnostic: it operates on files + word-timestamped transcripts. What changes:

| | Real camera takes | AI-generated clips (Higgsfield etc.) |
|---|---|---|
| Selection signal | fewest ums, complete on-script, no dead pauses, warm-up trims ("Hey [name]" cut at the silence gap) | engine artifacts (label morph, identity drift, lip-sync misses), prompt adherence |
| Multiple takes | same scene re-shot N times | same prompt re-rolled / engine A-B takes |
| Grade step | REQUIRED if log footage (S-Log3 → Rec.709 via hand-written `.cube` LUT) | usually skip — engines output graded Rec.709; grade only to unify clips across engines |
| Audio | one continuous human voice | per-clip generated voices — voice consistency across cuts is the #1 risk; check before assembling |
| Transcription quality | Whisper mishears names ("Thariq"→"Sark") — fine, timestamps still land; cut on timestamps, not text | same, plus Hinglish → use `--model base`, no `--language` flag |

## The pipeline

### Step 0 — Intake
Organize by scene, not shooting order. Catalog: scene → takes → file paths. If a script exists (`script.md`), it's the selection ground truth ("only one fully on script" is a disqualifier the deck used).

### Step 1 — Transcribe every take locally (no API key needed)
Whisper from the `mfa` conda env on this box; word timestamps on:

```bash
CONDA=/c/Users/SE/miniforge3/Scripts/conda.exe
for f in takes/*.mp4; do
  n=$(basename "$f" .mp4)
  ffmpeg -y -i "$f" -vn -ac 1 -ar 16000 "work/audio/$n.wav"
  "$CONDA" run -n mfa whisper "work/audio/$n.wav" \
    --model tiny.en --word_timestamps True --output_format json \
    --output_dir work/transcripts   # Hinglish/mixed: --model base, drop .en
done
```

Cache per source file; never re-transcribe unchanged sources.

### Step 2 — Take selection: one subagent per scene + a verifier
Spawn parallel subagents (Agent tool), one per scene. Each reads its scene's transcripts and returns, per the deck's pattern:
- the picked take + **written `selection_rationale`** ("C017 disqualified — 5.8s dead pause mid-sentence; C003 cleanest complete take: zero ums, clean ending")
- exact in/out timestamps with **every cut landing in a silent gap** (find the gap after the last warm-up word: "the 'Hey [name]' warm-up ends at 66.40; cut-in at 66.45 sits in the silent gap")
A verifier subagent double-checks picks against the script and the gap claims before anything renders.

### Step 3 — The EDL: `final-edit.json` (single source of truth)
```json
{ "scene": 1, "title": "Part 1: Intro",
  "candidate_takes": ["C003", "C017 (re-shoot)"],
  "selection_rationale": "C017 incomplete — 5.8s dead pause; C003 zero ums, clean ending.",
  "clips": [{ "clip": "A004C003", "start": 66.45, "end": 102.10,
              "first_words": "Hey everyone, it's..." }] }
```
Rationale is mandatory per scene — it's what makes the edit reviewable and re-derivable.

### Step 4 — ffmpeg executes the EDL
```bash
# one frame-accurate cut per pick (input-seek before -i is fast; re-encode for accuracy)
ffmpeg -ss 66.45 -to 102.10 -i A004C003.MP4 -c:v libx264 -preset fast -crf 18 \
  -af "afade=t=in:st=0:d=0.03,afade=t=out:st=35.62:d=0.03" cuts/seg1.mp4
# join the picks losslessly
ffmpeg -f concat -safe 0 -i concat.txt -c copy final_cut.mp4
```
Windows note: no `videotoolbox` — plain libx264 (or `h264_nvenc`/`h264_qsv` if GPU present).

### Step 5 — Verify like the deck did
1. **Re-transcribe the finished cut** and assert the failure you removed is gone ("zero ums") and the script lines are intact, in order.
2. Watchable rough cut FIRST, grade and graphics after — a verified 2:50 within minutes beats a polished wrong cut.

### Step 6 — Grade (only when needed)
Log footage: write `.cube` LUTs as plain text (S-Log3→Rec.709), generate 3–7 candidate grades, render one frame through each, let the user pick — then `ffmpeg -vf lut3d=luts/pick.cube` at encode. AI clips: skip, or one unifying LUT if engines mismatch.

### Step 7 — Graphics as code, cued by the transcript
- Rebuild designer PNGs / title cards as **Remotion JSX components** — every word, color, beat becomes a promptable parameter.
- ONE timing-knobs file (`anim.tsx`: entrance, sibling-gap, overlayIn/Out, emphasisDelay + one easing curve) — "make it snappier" must be a one-line change.
- The cue sheet times overlays by **grepping word timestamps** for the spoken phrase — overlays land on the word, never by scrubbing.
- Verify renders by screenshotting stills before any full render pass.
- Optional design round-trip: export components to Figma via MCP for the design team, import their pass back ("update the video to match").

### One-prompt orchestration pattern
The whole pipeline can run from a single kickoff (the deck's actual prompt shape): point at the folder + script, name the selection heuristics ("best takes are usually at the end with fewest ums", "cut the 'Hey [name]' warm-ups"), demand the EDL JSON + ffmpeg final, and arm an autonomous loop ("don't stop until you have a final video" — here: `/loop-until-done` with the re-transcribe check as the machine-verifiable done criterion).

## Output contract
Leave behind a repo-shaped edit, never just a video: `work/transcripts/*.json` · `final-edit.json` (with rationales) · `cuts/` · `luts/*.cube` (if graded) · `src/` components + `anim.tsx` (if graphics) · `final.mp4`. The edit must be reproducible from the text artifacts alone.
