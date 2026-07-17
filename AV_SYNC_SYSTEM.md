# Audio-Master Frame-Lock: the sync system (any script, never drifts)

The repeatable method for making narration and picture line up perfectly in every assembly (animatic AND final video), no matter the script, the shot count, or the durations. It cannot mismatch by construction, and it verifies itself.

Tool: `tools/av_sync_render.py` · Source of truth: a per-project `manifest.json` · Output: the video + an `_EDL.json`.

---

## The one rule

**The audio (narration) is the master clock. A picture stays on screen for exactly as long as its narration segment plus its deliberate pauses, quantized to a whole number of frames.** Video and audio for each shot are built from the *same integer frame count*, so they are the same length to the sample, and the error cannot accumulate.

## Mapping rule: a line owns its visuals

Sync is not only stream alignment, it is *semantic*: the picture on screen must illustrate the words being spoken *right then*. So a narration line **owns** its visual(s). If a line needs more than one picture (a start-and-settle, or a grin then everyone-laughs), the pictures are cut **within** that one line: the line's audio plays continuously across them (`"images": [...]` with optional `"weights"`), so the illustrating frame is always up while its words are spoken. **Never place a picture that illustrates a line as a trailing SILENT beat after the line has ended**, that was the original defect (the group-laugh shot appeared in silence *after* "He made sure everyone laughed with him" had already finished). A silent `"hold"` is only for a deliberate pause that has no line to illustrate.

## Why it can never drift (the integer-frame principle)

Drift is caused by rounding: if a slide is "about 4.41 s" of video but "exactly 4.41 s" of audio, each shot is off by a fraction of a frame, and across 27 shots those fractions add up to a visible slip (this is the "gradual drift" every editor warns about). The fix is to never let a shot have a fractional-frame duration:

For each shot, in order:
1. **Measure** the narration length `vo` (ffprobe on the rendered TTS). Silent beats have `vo = 0`.
2. **Frames** `F = ceil((pause_in + vo + pause_out) * fps)`. `ceil` guarantees the whole line fits, never clipped.
3. **Duration** `dur = F / fps`. This is exact and frame-aligned.
4. **Audio segment** = `pause_in` silence, then the narration, then silence padded to exactly `dur` (`adelay` + `apad` + `-t dur`).
5. **Video slide** = exactly `F` frames of the keyframe (`-frames:v F`, with the Ken-Burns `zoompan d=F`).

Then concatenate all video slides and all audio segments. Total video = `sum(F)` frames = `sum(F)/fps` seconds. Total audio = `sum(dur)` = `sum(F)/fps` seconds. **Identical by construction.** No `-shortest`, no guessing, no per-shot slip.

## "Delays wherever necessary"

Timing is controlled per shot, not left to chance:
- **`pause_in`** / **`pause_out`** (seconds): breathing room before/after the line so narration never butts against a cut. Defaults are small; override per shot for emphasis (e.g., a long `pause_out` after an emotional line so the beat lands).
- **`hold`** (seconds): a silent shot (a reaction beat, a cutaway) stays up for exactly this long.
These are the "delays": explicit, inspectable, and part of the frame math, so adding one can never desync anything downstream.

## The manifest (source of truth / EDL input)

```json
{
  "fps": 30, "resolution": [1080, 1920],
  "voice": "en-IN-PrabhatNeural", "rate": "-4%",
  "default_pause_in": 0.2, "default_pause_out": 0.4,
  "kenburns": true,
  "output": "zebpay/animatic/OUT.mp4",
  "shots": [
    {"id": "S1-a", "image": "zebpay/keyframes/S1-a.png", "vo": "..."},
    {"id": "S3-c", "images": ["S3-c.png", "S3-f_grouplaugh.png"], "weights": [0.4, 0.6], "vo": "He made sure everyone laughed with him."},
    {"id": "S4-d", "image": "...", "vo": "...", "pause_out": 1.0},
    {"id": "beat", "image": "...", "vo": null, "hold": 1.2},
    {"id": "endcard", "video": "endcard.mp4", "vo": "brought to you by ZebPay..."}
  ]
}
```

## Verification (built in, non-optional)

After muxing, the tool re-probes the output and asserts `|video_sec - audio_sec| < 1 frame` and that the total equals `sum(F)/fps`. It prints a per-shot table with in/out timecodes and writes `<output>_EDL.json` (the edit decision list: every cut, inspectable). If sync is off by even one frame it exits non-zero. A run is only "done" when it prints `SYNC LOCKED`.

Example (ZebPay animatic): `video 171.133s   audio 171.133s   drift 0.0 ms   SYNC LOCKED`.

## Where this applies

- **The animatic** (storyboard reel): keyframes + Edge-TTS scratch VO, built by this tool.
- **The final video** (Phase 3 assemble): the SAME manifest and frame math. Each generated clip (Seedance) is fit to its shot's `F` frames (trim, or generate at that length), and the final VO (ElevenLabs) replaces the scratch track segment-for-segment. Because the timeline is defined in frames from the audio, swapping scratch VO for final VO or a draft clip for a final clip preserves the lock.
- **Pre-rendered VIDEO shots:** a shot can be a `"video"` (a Mode-B HyperFrames/Remotion branded card, kinetic captions, a logo/lower-third, or a final generated clip) instead of a still. The tool fits it to the shot's exact `F` frames (clones the last frame if short, trims if long), silent, so the frame-lock holds. This is the same mechanism that fits the final Seedance clips, use it for the end card and any motion-graphic overlay. (HyperFrames renders locally via Brave, see the `hyperframes-setup` note; zero credits.)

## Usage

```
python tools/av_sync_render.py <manifest.json>
```
Requires ffmpeg + `edge-tts` (free, no API key). Reusable across projects: write a manifest, run, read the `SYNC LOCKED` line and the EDL. Referenced by the assembly step in `AI_VIDEO_WORKFLOW.md`.
