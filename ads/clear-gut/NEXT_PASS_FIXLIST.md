# Clear Gut — issues found (v5 review) + fix list for the next pass

Captured 2026-06-13 after the AV-senses review + a human manual pass + a full visual check of v5
(`edit/final/ClearGut_IngredientArmy_FINAL_v5.mp4`). Each issue links to the guardrail added so it
doesn't recur.

## BLOCKER / must-fix on the next (regeneration) pass
1. **Lip-sync is imperfect (S1–S5).** Human-confirmed weak. Veo cartoon lip-sync is only approximate.
   Next pass: try tighter speaker-dominant framing + shorter lines; otherwise accept and flag, or change
   shot construction. *(Guardrail: video-reviewer now treats any wired "looks synced" as a WEAK signal — lip-sync precision stays needs-human, never auto-PASS.)*
2. **S1 caption count mismatch.** Caption shows "हा हा हा!" (3×) but the audio says "ha ha" (2×); also a stray "!!" on दूँगा.
   Cause: karaoke was built from the SCRIPT text, not the ACTUAL audio. Next pass: for onomatopoeia / repeated
   sounds, count the repetitions from Whisper's actual output and match the caption to it. *(Guardrail: video-captions-karaoke + video-reviewer.)*
3. **Audio still carries the dashes (S3/S6/S7).** v5 used the original clips, whose Veo audio voiced the em-dashes
   as garbage. The clean dash-free script is already in the prompt files — regenerating those 3 clips fixes it. *(Guardrail already in place: the no-dash-in-spoken-lines rule across skills/agents.)*
4. **S8 stomach faces the lens with an open mouth under the narrator VO.** Recurs even though the keyframe was
   regenerated in profile/mouth-closed — Veo turned it to camera + opened the mouth. Next pass: stage the
   narrated character in HARD profile or minimized/turned fully away, expect re-rolls, flag for review. *(Guardrail: assistant-director + caricature-talking-ad.)*

## MAJOR / cosmetic (post-only, no regeneration)
5. **Captions display dashes** (S3 "गैस — मेरा काम", S6 "नहीं — दस…" + "जड़ी-बूटियों", S7 "एक ही — आयुर्वेदिक", S5 "जड़ी-बूटियों").
   The burned `captions.ass` predates the dash-cleanup of `make_karaoke.py`. Regenerate captions from the
   cleaned text. *(Guardrail: video-captions-karaoke — caption display text must use the SAME cleaned/dash-free
   text as the spoken line; regenerate captions after any script edit.)*
6. **S7 dropper cap reads gold, not white** (real product = white cap). S8/S9 are correct. Accept as stylized
   reveal, or recolor.

## PROCESS bugs found (and fixed)
7. **Stale frame timeline.** The review scored the S9 card against frames extracted from the ORIGINAL cut (v1),
   producing a false "garbled Devanagari" blocker; v5's card was actually clean. *(Guardrail: video-reviewer must
   re-extract the frame timeline from the EXACT file under review — verify filename + duration — never reuse a stale one.)*
8. **CLI duplicate-spend bug (earlier).** `generate create` without `--wait` returns a bare id-string array; a
   mis-parse + auto-retry created duplicate paid Veo jobs. *(Guardrail already in caricature-talking-ad.)*

## Reference facts (don't re-derive)
- **DaVinci Resolve free has NO Python scripting API** (Studio-only, ~$295). Can't be agent-driven on the free tier.
- **UTMOS MOS is English-TTS-trained** → on Hindi/character/ambient the absolute score reads low; use RELATIVE
  ranking + re-roll trend, isolate the voice first. (Lowest in v5: S3 Ajwain 1.46.)
- **Higgsfield video_analysis** gives real motion/audio/lip-sync-qualitative/composition perception, free, ~25s/clip.

## What was solid in v5 (don't touch)
S1 villain · S2–S5 hero solos (S5 Haritaki warm, not villain) · S6 team (lens-facing = flexing, OK per human) ·
S7 swirl reveal · S9 real-product card (full bottle, legible label, clean tagline + sub-line) · all captions
correctly shaped · no morphing / no model-burned text.
