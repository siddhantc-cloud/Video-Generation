---
name: storyboard-animatic
description: Build the pre-generation review gate for an AI video, a static storyboard board AND a frame-locked animatic (keyframes cut to a free Edge-TTS scratch narration), so a human can approve the whole film's flow, pacing and timing BEFORE any paid generation. Use after per-shot keyframes are locked and before the spend gate, for any narrated/VO video (ads, explainers, story films). All Mode B: zero generation credits. Guarantees narration and picture never drift (audio-master frame-lock) and never lag (a line owns its visuals). Composes with the project's keyframes + AI_VIDEO_WORKFLOW.md + AV_SYNC_SYSTEM.md + tools/av_sync_render.py. NOT for generating video or spending credits.
---

# storyboard-animatic (the pre-spend review gate)

The last free checkpoint before money. After every per-shot keyframe still is locked (Gate B) and before the spend gate turns them into paid clips, assemble the keyframes into two review artifacts and get human sign-off:

1. **Static storyboard** - a film-order board (each shot's keyframe + VO line + camera + mode/status), for a quick scan and to share with stakeholders. Rendered as a self-contained HTML page (downscaled base64 thumbnails), published via the Artifact tool.
2. **Animatic** - a timed video: the keyframes cut to a free Edge-TTS scratch narration with gentle Ken-Burns, so *pacing, timing, VO fit, and shot order* are visible before a single paid clip. Built by `tools/av_sync_render.py` from a `manifest.json`.

Both are Mode B (deterministic, local, ffmpeg + edge-tts): **zero credits**. The scratch voice is a placeholder; the final VO stays the real TTS/recording at assembly.

## Two hard rules (this is why the gate is trustworthy)

**1. Audio is the master clock, frame-locked.** Never eyeball a shot's duration. Each shot's on-screen time = `ceil((pause_in + measured_narration + pause_out) * fps)` FRAMES; the video (exactly that many frames) and the audio (exactly frames/fps seconds) are built from the same integer, so they cannot drift over any number of shots. The tool VERIFIES `|video - audio| < 1 frame` and prints `SYNC LOCKED` or exits non-zero. A build is not done until it says SYNC LOCKED. Full method: `AV_SYNC_SYSTEM.md`.

**2. A line owns its visuals (semantic sync).** The picture on screen must illustrate the words being spoken *right then*. If a line needs more than one picture (a start-and-settle, a grin then everyone-laughs), cut them WITHIN that line via `"images": [...]` + optional `"weights"`, so the line's audio plays continuously across them and the illustrating frame is always up while its words play. **NEVER place a picture that illustrates a line as a trailing SILENT beat after the line has ended** (that is the classic defect: the reaction appears in silence after its narration already finished). A silent `"hold"` is only for a deliberate pause with no line to illustrate.

## Text hygiene for the scratch VO

Send the TTS only the actual spoken words. Strip stage directions (`Pause.`, tone notes, scene headers). Remove em-dashes. An ellipsis becomes a comma or a pause, engines vocalize punctuation instead of pausing on it. (Same rule as the final ElevenLabs VO.)

## Procedure

1. **Confirm keyframes are locked** (Gate B passed). List them in film order.
2. **Write the manifest** `manifest.json` (the EDL source of truth):
   ```json
   {
     "fps": 30, "resolution": [1080,1920],
     "voice": "en-IN-PrabhatNeural", "rate": "-4%",
     "default_pause_in": 0.2, "default_pause_out": 0.4,
     "kenburns": true, "output": "<proj>/animatic/OUT.mp4",
     "shots": [
       {"id":"S1-a","image":"<proj>/keyframes/S1-a.png","vo":"..."},
       {"id":"S3-c","images":["S3-c.png","S3-f_grouplaugh.png"],"weights":[0.4,0.6],"vo":"He made sure everyone laughed with him."},
       {"id":"S4-d","image":"...","vo":"...","pause_out":1.0},
       {"id":"beat","image":"...","vo":null,"hold":1.2},
       {"id":"endcard","video":"endcard.mp4","vo":"brought to you by ZebPay..."}
     ]
   }
   ```
   Map every narration line to the visual(s) that illustrate it (rule 2). Add `pause_out` where a beat should land (e.g. after an emotional line).
3. **Render + verify:** `python tools/av_sync_render.py <proj>/animatic/manifest.json`. Requires ffmpeg + `edge-tts` (`pip install edge-tts`, free, no key). Read the printed EDL table and confirm `SYNC LOCKED`. Fix and re-run if not.
4. **Build the static board** (optional but recommended): downscale each keyframe to a base64 thumbnail, emit a film-order HTML board (shot id + camera + VO + mode/status chip per card, theme-aware), publish with the Artifact tool.
5. **Present both for human approval.** This is the gate: nothing proceeds to the spend gate until the human approves the whole film. Shareable with external stakeholders.

## Branded cards, captions, overlays (Mode B, HyperFrames)

Any shot can be a pre-rendered VIDEO instead of a still: set `"video": "clip.mp4"` on the shot and the tool fits it to that shot's exact frame count (`AV_SYNC_SYSTEM.md`), keeping the lock. Use this for the end card, kinetic captions, logo/lower-thirds, and text overlays (the राм inscription, the stripe reveal) - all deterministic, zero credits. Render them with **HyperFrames** (HeyGen's HTML/CSS-to-video engine, GSAP): `hyperframes init <name> --resolution portrait --example blank`, edit `index.html` (a `#root` with `data-duration` + `data-fps`, clip divs, and a paused GSAP timeline at `window.__timelines["main"]`), then `hyperframes render . -o card.mp4 --fps 30 --quality high`. On this box, point HyperFrames at Brave to skip its browser download: `PUPPETEER_EXECUTABLE_PATH="C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"` + `PUPPETEER_SKIP_DOWNLOAD=1` (see the `hyperframes-setup` memory). Render the card SILENT; the VO comes from the shot's narration segment.

## Verification checklist (before you call it done)

- [ ] `SYNC LOCKED` printed (drift < 1 frame); EDL written.
- [ ] Every narration line's visual is on screen WHILE the line plays (no trailing-silent-illustration lag) - spot-check the multi-image lines.
- [ ] No stage directions or em-dashes reached the TTS.
- [ ] Runtime is acceptable (flag it if far off the brief; runtime = generation cost later).
- [ ] Both artifacts delivered to the human; spend gate is BLOCKED until approval.

## References

- `AV_SYNC_SYSTEM.md` - the frame-lock method + the line-owns-visuals rule (repo root).
- `tools/av_sync_render.py` - the manifest-driven, self-verifying renderer.
- `AI_VIDEO_WORKFLOW.md` - where this gate sits (after Gate B keyframes, before the spend gate).
- The `video-editor` agent owns building these; the `video-reviewer` agent checks narration/picture sync.
