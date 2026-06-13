---
name: audio-first-reel
description: "The multi-scene reel assembly system for this project: Veo 3.1 fast clips with NATIVE audio for all on-camera dialogue (hard rule: no audio replacement on visible lips — lip-sync needs a lip-sync model we don't have), free TTS voiceover ONLY for B-roll scenes where no lips are visible, Whisper-timed Latin-script subtitle overlay burned per scene, EDL assembly with fades, re-transcribe verification. Use when assembling multi-scene dialogue reels/ads, when the user says 'add subtitles', 'caption this video', 'combine the scenes', or 'build the reel'. Composes: higgsfield-ugc-playbook (generation specs), multi-take-video-edit (assembly+verification)."
metadata:
  version: 1.1.0
  updated: 2026-06-12
  verified: "every command executed for real on this box (scene1_veo_subtitled.mp4 + verify frames)"
---

# Reel Assembly System (v1.1 — native-audio architecture)

## THE HARD RULE (user-mandated 2026-06-12; amended same day by user direction)

**Engine-generated speech audio gets exactly ONE sanctioned transformation: a timing-preserving ElevenLabs Speech-to-Speech dub.** Everything else remains forbidden: TTS replacement (new timing → lips desync — rejected), delay/pad/fade "repairs" (rejected as muting), mixing, trimming-as-fix.

**Why STS is different and sanctioned (user-approved workflow 2026-06-12):** STS re-voices the *existing* audio — same words at the same milliseconds, only the voice timbre/quality changes — so the Veo lips stay in sync by construction. Verified on scene 1: duration 8.009→8.034s, first-word drift 0ms.

```bash
# per dialogue clip: extract → STS → remux (video untouched)
ffmpeg -y -i sN_veo.mp4 -vn -c:a libmp3lame -q:a 2 sN_orig.mp3
curl -s -X POST "https://api.elevenlabs.io/v1/speech-to-speech/<VOICE_ID>?output_format=mp3_44100_128" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" -F "audio=@sN_orig.mp3" -F "model_id=eleven_multilingual_sts_v2" -o sN_dub.mp3
ffmpeg -y -i sN_veo.mp4 -i sN_dub.mp3 -map 0:v -map 1:a -c:v copy -c:a aac -ar 48000 -ac 2 -b:a 192k sN_dubbed.mp4
```
Verify every dub: duration delta <50ms + a human lip-check on one line before batch-dubbing.

**What the STS dub buys:** one consistent voice ID per speaker across ALL scenes (voice-drift solved), ElevenLabs naturalness over engine TTS, per-speaker casting. What it does NOT fix: a first-word onset the engine never synthesized (cold-start limitation stands).

## Supporting laws

1. **Audio duration drives video duration** where TTS is legal (no-speech B-roll only): TTS first, measure, then generate ≥ audio. (8.93s TTS under an 8s clip cut the final word.)
2. TTS VO is permitted **only** over visuals with no engine speech — stills + Ken-Burns `zoompan` (preferred, 0 cr, no audio track at all) or video used picture-only on no-lips B-roll.
3. **No hyphens/dashes (`-` `—` `–`) in any line Veo will SPEAK.** Veo voices them as a word/garbage sound (burned 2026-06-13: em-dashes in spoken Devanagari lines came out as junk). Use a comma, a full stop (`।`/`.`), or rephrase so the pause is implied. (Burned captions can DISPLAY a dash fine — this is a spoken-audio rule only.)

## The complete Higgsfield × ElevenLabs workflow (v2.0, user-approved 2026-06-12)

```
1. PRE-PRO    script (≤21 words / 8s dialogue scene) · character+product sheets · NB Pro keyframes (2cr, verify before animating)
2. VIDEO      Veo 3.1 fast, native Hindi speech, pre-speech-beat prompt, 22cr/8s · verify pacing (≥2.7 w/s) + onset (RMS bin 0)
3. DUB        ElevenLabs STS per dialogue clip (one voice ID per speaker, ALL scenes) · verify duration <50ms delta + lip-check
4. B-ROLL VO  ElevenLabs TTS (upgrade from edge-tts) over stills/Ken-Burns · word timing via /with-timestamps endpoint (char-level) or edge-tts WordBoundary fallback
5. CAPTIONS   karaoke ASS (make_karaoke.py) — whisper-timed on dubbed dialogue, synthesis-timed on TTS lanes · per-scene MarginV, never cover the label
6. ASSEMBLY   EDL final-edit.json → -c copy concat → end-card
7. VERIFY     re-transcribe (lines in order) · frame-grabs (captions/labels/identity) · onset + words/s per scene · spend audit vs preflights
```

**ElevenLabs account facts (verified 2026-06-12):** free tier — premade voices + own custom voices via API only; **library voices (Ani/Dev — the Indian males) require a paid plan** (`paid_plan_required` on STS). MCP server wired project-scoped in `.mcp.json` (`uvx elevenlabs-mcp`, loads after session restart); REST API with the key works directly meanwhile. Voice shortlist: Arvind → `pOk40AXK0gYhreBApvj7` Ani (paid) or premade `nPczCjzI2devNBz1zQrb` Brian (free, tested); Rajiv → `wX8msIkhz9iDOTSSJWNZ` Dev (paid) or premade `iP95p4xoKVk53GoZ742B` Chris; user's own customs (NehaIndianAccent etc.) also available.

## Scene-type routing — which lane builds which scene

| Scene type | Video | Voice | Example (Clear Gut script) |
|---|---|---|---|
| On-camera dialogue (lips visible) | `veo3_1` fast, sound ON, dialogue in prompt | **Veo native audio, untouched** (`-c:a copy` everywhere) | Scenes 1, 2, 3, 6 |

> **Cold-start: UNSOLVED engine limitation on `veo3_1` fast (status as of 2026-06-12 — do NOT claim any of these fixes work).** Veo clips the first word's onset in the synthesis itself. Everything tried failed the user's ear test:
> 1. Pre-speech-beat prompt — unreliable: produced 40–100ms runway across takes, never the requested half-second; onset attack still clipped (instant -49→-11dB in 20ms vs a natural 40–80ms vowel ramp).
> 2. Stream pad/delay/fade — REJECTED + forbidden by the hard rule (and the fade ate the onset).
> 3. EDL stub-prepend (0.4s silent freeze-frame segment, streams untouched) — insufficient: runway cannot restore a phoneme that was never synthesized.
>
> Untested candidate (user has declined further retries; only with explicit approval): Fable-style warm-up word — prepend a throwaway word ("Dekhiye —") to the dialogue so the engine clips THAT, then EDL-trim in at the silence gap after it. Otherwise: accept the artifact, or use a different engine/lip-sync-model route. Diagnostic recipe that localized this: 10ms-bin RMS onset profile; compare attack ramp shape against natural speech.

> **Pacing rule (diagnosed 2026-06-12, fix proven):** Veo sometimes renders dialogue in stretched slow-motion delivery (one take measured 2.47 words/s vs normal ~3.0 for conversational Hindi). Prevent in the prompt: *"Everything moves at real-time speed — normal playback, NOT slow motion … speaks at a natural, brisk conversational pace … lips sync at normal speaking speed."* Retake with this direction measured 2.96 w/s. Verify objectively after every dialogue take: whisper word span → words/s; flag anything under ~2.7 for Hindi. Both audio+captions seeming slow together = the GENERATION is slow (captions follow audio), never the pipeline.
| B-roll / cutaway (no lips) | `veo3_1_lite` (8 cr) / stills + Ken-Burns `zoompan` (0 cr) | **TTS VO** — edge-tts `hi-IN-MadhurNeural` (free, verified natural) or Sarvam/ElevenLabs w/ key | Scenes 4 (ingredients), 5 (dropper macro) |
| Every scene | + subtitle overlay (below) | — | all |

The B-roll lane is also the pressure valve for audio quality: the more of the reel carried by B-roll+TTS, the less Veo's TTS naturalness matters — without ever touching an on-camera lip.

## Subtitle overlay (verified end-to-end)

Captions are timed from the clip's **own speech** (Whisper word timestamps) but display the **exact Latin-script line** (ground truth — never Whisper's text, which emits Urdu script for Hindi):

```bash
export PYTHONUTF8=1; CONDA=/c/Users/SE/miniforge3/Scripts/conda.exe
# 1. word timestamps from the clip's own audio
ffmpeg -y -i scene.mp4 -vn -ac 1 -ar 16000 a.wav
"$CONDA" run -n mfa whisper a.wav --model base --language hi --word_timestamps True --output_format json --output_dir .
# 2. map the known Latin script line onto whisper timing, 4-word caption chunks,
#    proportional index mapping (whisper word count ≠ script word count is fine)
#    → scene_captions.srt   (python snippet: see UGC/ worked example from 2026-06-12)
# 3. burn — video re-encodes, AUDIO COPIED UNTOUCHED
ffmpeg -y -i scene.mp4 \
  -vf "subtitles=scene_captions.srt:force_style='FontName=Impact,FontSize=13,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,Alignment=2,MarginV=100'" \
  -c:v libx264 -preset fast -crf 18 -c:a copy scene_subtitled.mp4
```

**Placement rule (caught on frame-verify):** default `MarginV=55` lands captions ON the product label — an ad cannot cover its product. `MarginV=100` clears the bottle at chest level (verified at 720×1280). Always extract a mid-caption frame and LOOK at it before accepting: `ffmpeg -ss <t> -i out.mp4 -frames:v 1 f.png`.

**For TTS B-roll scenes, NEVER use Whisper timing — get exact word boundaries from the synthesis itself** (root-caused 2026-06-12: Whisper-proportional mapping drifted audibly mid-clip). edge-tts 7.x defaults to `SentenceBoundary`; request words explicitly in the Python API: `edge_tts.Communicate(text, voice, boundary="WordBoundary")` and collect `chunk["type"]=="WordBoundary"` events (offset/duration in 100-ns ticks ÷ 1e7 → seconds). Word count matches the input text 1:1 → captions aligned by construction. Synthesize audio + boundaries in ONE call (same synthesis = same timing); see `UGC/make_vo2.py`. The CLI's `--write-subtitles` is sentence-level only — don't use it for karaoke.

### Karaoke highlight captions (verified — `scene1_veo_karaoke.mp4`)

The reels-style "color sweeps through the words as spoken" effect = ASS `\kf` karaoke tags, burned by libass via `-vf "ass=file.ass"`. Same Whisper word timings; each word gets `{\kf<centiseconds>}` where duration = gap to the next word's start. Style block (720×1280):

```
PlayResX: 720 / PlayResY: 1280
Style: Cap,Impact,58,&H0000D7FF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,3,0,2,30,30,450,1
```
- `PrimaryColour &H0000D7FF` = gold #FFD700 (fill color — matched to the Clear Gut label; ASS colors are &HAABBGGRR)
- `SecondaryColour &H00FFFFFF` = white (unsung text); `\kf` sweeps Secondary→Primary smoothly
- `MarginV: 450` px @1280 ≈ the verified chest-level placement (=SRT MarginV 100 @288-ref); FontSize 58 ≈ SRT 13
- Per-word floor: `max(duration_cs, 12)` so short words still visibly flash; line end +0.08s hold
- Dialogue line shape: `Dialogue: 0,<start>,<end>,Cap,,0,0,0,,{\kf42}Agar {\kf16}aap {\kf48}roz {\kf30}subah`
- Burn with `-c:a copy` as always; verify with TWO frame-grabs inside one line (early + late) — the gold boundary must have MOVED between them.

## Assembly (the "combine different parts" setup)

1. Build each scene through its lane above → `work/scenes/sN.mp4` (all 9:16, same fps/resolution).
2. EDL `final-edit.json` per scene: `{scene, lane: "dialogue"|"broll", clip, voice: "veo-native"|"<tts voice>", srt, rationale}`.
3. Lossless concat, **no audio fades** (fades = touching generated audio → forbidden by the hard rule; engine clips start/end in room tone so boundary pops are unlikely — if one occurs, fix by reordering/regenerating, not by audio processing):
   `ffmpeg -f concat -safe 0 -i concat.txt -c copy reel_rough.mp4`
   (If captions are burned per-scene — preferred — concat is the last step. If using one master.srt instead, burn it LAST after concat, offsets shifted per scene.)
4. End-card: product hero still 2s + benefits text (script scene 6 spec), Ken-Burns, appended.

## Verification
- Re-transcribe the final reel → all script lines present, in order.
- Frame-grab at each scene boundary + one mid-caption frame per scene → label visible, captions clear of product, identity consistent.
- `ffprobe` every dialogue scene: `codec_name=aac` stream **identical duration to source** (proves audio untouched).
- Spend audit vs preflight plan (`higgsfield account transactions`).

## Cost shape
Dialogue scenes: Veo fast 22 cr/8s. B-roll: 8 cr (Lite) or 0 cr (stills). Captions/TTS/assembly: 0 cr. Clear Gut 6-scene estimate: 4×22 + 2×8 ≈ **104 cr** + retakes — preflight + spend gate before every generate.
