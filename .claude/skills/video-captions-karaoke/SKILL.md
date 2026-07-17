---
name: video-captions-karaoke
description: "Burn gold karaoke-style captions (word-by-word color fill) onto a finished video, timed to its spoken audio. Use when the user wants captions/subtitles burned, karaoke captions, animated word highlights, or Hindi/Devanagari reels captions. Handles the Hindi gotcha (Whisper emits Urdu script — display the KNOWN script text instead), placement that clears the product/face, and the burn-LAST rule. Built with ffmpeg + libass + Whisper (conda env `mfa`)."
metadata:
  version: 1.0.0
  updated: 2026-06-13
  proven-on: "Clear Gut ad scenes (gold \\kf karaoke, Devanagari)"
---

# Karaoke caption burn (gold word-fill)

Reels-style captions where color sweeps through each word as it's spoken. ASS `\kf` tags via libass, timed from the clip's own audio.

## Pipeline (per clip or per assembled reel)
1. **Get word timing from the clip's OWN audio** (so captions match the video):
   `ffmpeg -i clip.mp4 -vn -ac 1 -ar 16000 a.wav`
   `conda run -n mfa whisper a.wav --model base --language hi --word_timestamps True --output_format json` (use env-python directly, NOT `conda run`, to avoid output buffering: `<env>/python.exe -m whisper ...`).
2. **Display the KNOWN script text, not Whisper's output.** For Hindi, Whisper transcribes Devanagari as **Urdu script** — wrong on screen. So map your known caption words onto Whisper's word *timings* (proportional or phrase-window mapping); render YOUR text. (`make_karaoke.py` in `simple_ads/UGC/` does this — or hand-build phrase windows when Whisper merges words.)
3. **Build the `.ass`** — gold fill over white, Impact, placed clear of the product/face:
```
[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Cap,Impact,58,&H0000D7FF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,3,0,2,30,30,<MARGINV>,1
[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
Dialogue: 0,0:00:00.10,0:00:02.96,Cap,,0,0,0,,{\kf42}word1 {\kf24}word2 ...
```
   - `PrimaryColour &H0000D7FF` = gold #FFD700 (fill); `SecondaryColour` = white (unsung). ASS color is `&HAABBGGRR`.
   - `\kf<centiseconds>` per word = gap to next word's start; smooth fill. (`\k` = snap/pop instead of fill.)
   - **Placement:** `MarginV` from the bottom — raise it (≈200 @720×1280) so captions clear the product label / face. Frame-verify.
   - Devanagari needs a Devanagari-capable font (e.g. Noto Sans Devanagari); Latin Hinglish works with Impact.
4. **Burn LAST** (after any other overlays, audio untouched):
   `ffmpeg -i in.mp4 -vf "ass=caps.ass" -c:v libx264 -preset fast -crf 18 -c:a copy out.mp4`

## libass / ffmpeg build (CRITICAL — verified 2026-06-13)
- The conda-forge ffmpeg in envs `mfa` and `comfy` is built **WITHOUT libass** — no `ass`/`subtitles` filter (check: `ffmpeg -filters | grep -w subtitles`). drawtext is NOT a fallback: it has no HarfBuzz, so it mangles Devanagari shaping (matras/conjuncts misplaced).
- Fix: use a static **BtbN gpl build** (has `--enable-libass`): downloaded to `D:\startup_dev\so_sorry\tools\ffmpeg-libass\...\bin\ffmpeg.exe`. Use it for ALL text/burn steps.
- Devanagari font that shapes correctly with libass on Windows: **"Nirmala UI"** (`C:\Windows\Fonts\Nirmala.ttc`) — fontconfig finds it by family name; verified shaping पेट हल्का। दिन हल्का। correctly.
- Pass the `.ass` to the filter via a **relative path** (`ass=edit/captions.ass`) from the project cwd to dodge the Windows drive-letter `:` escaping issue.
- **Devanagari conjunct-breaker (verified 2026-06-13):** an ASS V4+ `Style` with `Spacing` > 0 (letter-spacing) **shatters Devanagari conjuncts** in libass — it injects space between glyphs so e.g. `र्वे` in `आयुर्वेदिक` renders as a detached matra / dotted-circle placeholder. **Always set `Spacing,0` for any Devanagari style.** (It's the 13th Style field. A doubled tagline rendered fine at Spacing=0 but the brand sub-line broke at Spacing=4 — same font, same size.)

## Rules
- **Burn captions LAST** in the filter chain — overlays before captions, else they cover the text (silent failure).
- **`-c:a copy`** — never re-encode/touch audio when only adding captions.
- **Half-second-pause offset:** Veo clips start speech ~0.4–0.5s in (the scripted pause), but Whisper reports the first word at t=0.0. Floor the karaoke onset at ~0.4s so the gold fill doesn't run ahead of the voice.
- **Caption text must MATCH THE ACTUAL AUDIO, not the script (verified 2026-06-13).** The model often speaks FEWER repetitions than the script wrote — e.g. script "हा हा हा" (3×) but Veo said "ha ha" (2×), and the caption over-counted. For repeated onomatopoeia/laughs/sounds, count the repetitions from Whisper's ACTUAL output and display that count. Also strip stray doubled punctuation (`!!`). Display the KNOWN script *words* (Urdu-script gotcha) but the ACTUAL *count/structure*.
- **Keep caption text in sync with the cleaned spoken line.** Display the SAME dash-free text as the spoken line (no `-`/`—`/`–`, no `जड़ी-बूटियों` hyphen — use a space/comma). After ANY edit to the script/lines, **regenerate the captions** — a previously-burned `.ass` keeps showing the old (e.g. still-dashed) text even after you clean the source.
- **Verify by frame-grab** at a mid-caption time: text legible, clears product/face, gold sweep advancing (grab two frames in one line — boundary must move).
- For TTS B-roll audio, get exact word boundaries from the synth (`edge-tts` WordBoundary / ElevenLabs with-timestamps) instead of Whisper.

## Where it fits
Final step of `caricature-talking-ad` and `audio-first-reel` assembly. The video is generated caption-free (`no subtitles` in the Veo prompt); these captions are the controlled on-brand layer added in post.
