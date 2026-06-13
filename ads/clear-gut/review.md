# Clear Gut Ingredient Army - VIDEO REVIEW

Video: edit/final/ClearGut_IngredientArmy_FINAL.mp4 (1080x1920, 24fps, 63.456s, audio present)
Method: rubric (expectations.json, 83 criteria) + LLM-as-judge over the 1fps frame timeline s001-s063, ffmpeg sub-crops, full-reel Whisper transcript (content only).

## OVERALL: FAIL (2 failed blockers)

## Per-scene verdicts
- S1 (King hook, 0-8s): PASS - dominant comedic-menace King, faceless turned-away stomach, dark villain grade, no burned text, identity stable.
- S2 (Amla, 7.6-15.6s): PASS - solo, warm friendly hero, identity stable, no burned text.
- S3 (Ajwain, 15.2-23.2s): PASS - solo, warm energetic hero, identity stable, no burned text.
- S4 (Saunf, 22.8-30.8s): PASS - solo, calm gentle female-coded hero, identity stable, no burned text.
- S5 (Haritaki, 30.4-38.4s): PASS - VILLAIN-LEAKAGE GATE CLEARED. Benevolent warm grandfather throughout (kind twinkling amber eyes, warm smile), no menace, no mid-clip turn. The single highest-risk scene reads correct.
- S6 (Team-up VO, 38-46s): PASS - four heroes identifiable + inward around the happy stomach, King tiny/cowering, clean hands (no limb glitch), no burned text.
- S7 (Bottle reveal VO, 45.6-53.6s): PASS - amber Clear Gut dropper bottle forms as the focal subject, label legible, no stray characters, no burned text. (Major note: cap renders GOLD not WHITE.)
- S8 (Resolution+CTA VO, 53.2-61.2s): FAIL - happy stomach face+mouth turned TOWARD the lens instead of profile/away (blocker). Bottle and grade are good.
- S9 (Product card, 60.8-63.456s): FAIL - secondary brand sub-line aayurvedik is broken Devanagari (blocker). Real bottle and main gold tagline are correct.

## RANKED FIX LIST (blockers first) - for the video-editor

### BLOCKER 1 - S9 broken-Devanagari sub-line  (t=61.0-63.456s)
- Defect: the gray secondary line under the gold tagline renders aayurvedik with detached/floating matras and dotted-circle placeholder glyphs (font-shaping failure). The MAIN gold tagline (pet halka, din halka) is correct - DO NOT touch it.
- Smallest corrective action: S9 is an ffmpeg still card (NOT Veo), so this is a cheap, surgical re-render of the S9 card only. Re-burn the secondary line with a Devanagari-shaping-capable text path (libass/Pango with a proper Devanagari font + harfbuzz shaping), or drop the Devanagari word and keep only the Latin BLUMELIFE if shaping cannot be fixed in time. Verify the rebuilt sub-line glyphs combine (no dotted circles) before re-splicing. Do not re-render any Veo scene for this.

### BLOCKER 2 - S8 stomach face/mouth lens-facing  (t=54.0-60.0s)
- Defect: the happy stomach is posed with its body toward the bottle but its FACE and MOUTH are turned toward the lens (front grin); the rubric requires three-quarter profile, mouth turned AWAY, on this narrated shot. This also creates a front-facing mouth that is at high risk of being animated as talking under the VO (S8-stomach-mouth-closed, needs-human, elevated risk).
- Smallest corrective action: this is generative geometry, so it CANNOT be fixed by post-edit cropping/masking without losing the stomach. Re-generate S8 only, with the stomach in true three-quarter/profile, face+mouth turned away from lens toward the bottle, mouth closed (narrated shot). Keep the bottle, pedestal, warm grade, and caption as-is. If a full re-gen is too costly, the Director may ACCEPT-with-reason (the stomach is clearly happy and the bottle/label are correct), but note the open needs-human risk that the mouth may be visibly talking under the narrator VO - confirm on playback first.

## MAJOR to triage (not a blocker)
- S7 dropper-cap color (t=46-53s): the reveal bottle has a GOLD/brass dropper cap instead of the real WHITE cap. S8 (t=54-61s) correctly shows the WHITE cap. Director: accept as stylized reveal, or recolor the S7 cap to white if re-touching that clip.

## NEEDS-HUMAN (playback/ear pass before final sign-off; do not block the editor)
- Lip-sync precision S1-S5; only-speaker-mouth-moves S1-S5.
- S4 voice clearly FEMALE; voice quality/tone of all 8 lines (content already confirmed by transcript, in order).
- S6 no hero/stomach mouth moves under VO; S7 bottle no wobble; S8 bottle locked.
- S8 stomach mouth NOT talking under VO (HIGH RISK, tied to Blocker 2).
- Audio bed continuity/intelligibility; caption text exact via .ass diff; karaoke fill timing.

## Rubric notes (coverage gaps - fix the rubric, not the video)
- brand_truth says Clear Gut is BLUE text; the real asset is BLACK/dark text. Video is faithful to the asset.
- No explicit criterion for the S7 cap color, nor for the S9 secondary brand sub-line where the failing glyphs live.
