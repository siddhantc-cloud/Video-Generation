# Audio-Master Frame-Lock: the sync system (any script, never drifts)

The repeatable method for making narration and picture line up perfectly in every assembly (animatic AND final video), no matter the script, the shot count, or the durations. It cannot mismatch by construction, and it verifies itself.

Tools:

- `tools/av_sync_render.py` for line-locked narration blocks.
- `tools/edge_tts_word_timed.py` plus `tools/render_phrase_locked_animatic.py` for continuous,
  phrase-locked narration.

Source of truth: a versioned timeline JSON. Output: the video plus an `_EDL.json`.

---

## The one rule

**The audio (narration) is the master clock. A picture stays on screen for exactly as long as its narration segment plus its deliberate pauses, quantized to a whole number of frames.** Video and audio for each shot are built from the *same integer frame count*, so they are the same length to the sample, and the error cannot accumulate.

## Mapping rule: a spoken idea owns its visual

Sync is not only stream alignment, it is *semantic*: the picture on screen must illustrate the words
being spoken *right then*.

There are two valid modes:

### Mode A — one visual idea per narration block

Use `tools/av_sync_render.py`. One line owns one image or one pre-rendered clip. The audio and picture
share one measured integer frame count. This remains the simplest reliable mode.

### Mode B — several visual ideas inside continuous narration

Use one continuous narration file and capture word-boundary events from the same synthesis request:

```powershell
python tools/edge_tts_word_timed.py `
  --text-file scripts/short-narration-v004.txt `
  --audio edit/audio/animatic-short-v004/narration-scratch.mp3 `
  --timings edit/audio/animatic-short-v004/narration-word-boundaries.json `
  --voice en-IN-PrabhatNeural --rate=-4%
```

Create a phrase map where each visual names the first word it owns and a whole-frame start. Snap the
cut to the nearest frame to that word boundary, then render with:

```powershell
python tools/render_phrase_locked_animatic.py `
  edit/timelines/animatic-short-v004-phrase-map.json `
  --output deliverables/review-cuts/animatic-short/OUT.mp4
```

**Do not use percentage weights to claim semantic sync.** Percentage weights keep pictures inside the
correct audio block, but they do not prove that a cut lands on “laughed,” “rough,” or “Investing.”
That was the v003 defect. Weights are acceptable only when the images are interchangeable coverage
of the same idea. When the pictures illustrate different phrases, use Mode B.

Never place a picture that illustrates a line as a trailing silent beat after the line has ended. A
silent hold is only for a deliberate pause with no line to illustrate.

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
  "output": "deliverables/review-cuts/animatic/OUT.mp4",
  "shots": [
    {"id": "S1-a", "image": "keyframes/S1-a.png", "vo": "..."},
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

Phrase-locked mode adds two more required checks:

1. Calculate `cut_time - matching_word_start` for every cut. The absolute error must be at most half
   a frame; v004 measured 13.5 ms maximum at 30 fps.
2. Inspect the frames immediately before and after every boundary. This caught a ten-frame dark flash
   at K10→G11 in the first v004 render even though the streams were perfectly synchronized. Fix,
   rerender, and regenerate boundary evidence before reporting a pass.

## Where this applies

- **The animatic** (storyboard reel): keyframes + Edge-TTS scratch VO, built by this tool.
- **The final video** (Phase 3 assemble): the SAME manifest and frame math. Each generated clip (Seedance) is fit to its shot's `F` frames (trim, or generate at that length), and the final VO (ElevenLabs) replaces the scratch track segment-for-segment. Because the timeline is defined in frames from the audio, swapping scratch VO for final VO or a draft clip for a final clip preserves the lock.
- **Pre-rendered VIDEO shots:** a shot can be a `"video"` (a Mode-B HyperFrames/Remotion branded card, kinetic captions, a logo/lower-third, or a final generated clip) instead of a still. The tool fits it to the shot's exact `F` frames (clones the last frame if short, trims if long), silent, so the frame-lock holds. This is the same mechanism that fits the final Seedance clips, use it for the end card and any motion-graphic overlay. (HyperFrames renders locally via Brave, see the `hyperframes-setup` note; zero credits.)

## Usage

```
python tools/av_sync_render.py <manifest.json>
```
Requires FFmpeg and `edge-tts` (free, no API key). Reusable across projects: choose the correct mode,
write the timeline, render, check the EDL, calculate semantic cut error when using Mode B, and inspect
every boundary.
