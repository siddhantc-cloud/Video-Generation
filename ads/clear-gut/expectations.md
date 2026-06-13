# Acceptance Rubric, BLUMELIFE Clear Gut "Ingredient Army"

**Engine:** Veo 3.1 (`veo3_1`, native audio) for S1-S8 · ffmpeg product card for S9
**Format:** 1080×1920 (9:16), 24fps · total 63.456s · 0.4s crossfades
**Frame timeline:** `edit/review_frames/sNNN.png` at 1fps → `NNN-1 = second` (s001 = t=0.0s, s009 = t=8.0s, s062 ≈ t=61s)
**Brand truth:** `assets/clear_gut_product.png`, amber/brown glass **dropper** bottle, **white** dropper cap, white+yellow label, "Clear Gut" in **blue**, "BLUMELIFE" wordmark, "30 Servings · 30ml".

## Definition of done
**PASS = zero FAILED blockers** across all scenes + the caption and brand layers. Failed **majors** are triaged by the Director (fix or accept-with-reason). **Minors** are nice-to-have. **needs-human** items cannot be passed on stills alone, a human must watch/listen to playback before final sign-off; an unconfirmed **blocker-severity needs-human** item blocks delivery.

## How to read `method` / `checkable`
- `frame@sNNN` = still-checkable on that frame · `frames:start-vs-end` = consistency across two frames · `motion` = needs playback · `transcribe/audio` = needs ear/ASR · `final-only` = only meaningful on the captioned final, not raw clips.
- `frame` = a still proves it · `needs-human` = motion smoothness, voice quality, exact lip-sync, mouth-movement-vs-narration ALWAYS need a human, stills/transcripts can't prove them.

## Reviewer notes (read first)
- At 1fps, the 0.4s crossfade makes boundary frames (s008-s015, s023-s031, s038-s046, s053-s061) **blends** of two scenes, grade leniently, never fail a scene on a transition frame. Identity/grade checks target interior frames.
- `G-no-burned-text` checks the **final visible** state; a covered/cropped burned strip reads as clean. Confirm with the editor if any cover was applied.
- `CAP-script-correct`: diff burned text against the `.ass` source, not OCR-by-eye, for reliable Devanagari matras/conjuncts.

## Engine failure modes anticipated (each is a negative-check below)
Burned/garbled captions (Veo's #1 artifact, often Devanagari) · Veo animates **every** visible mouth (multi-mouth in S1/S6/S8) · off-beat lip-sync (S1-S5) · fine label warp (S7/S8 tolerated, S9 only legible frame) · character morph/identity drift · tone leakage (Haritaki bible ref is itself fierce) · bottle morph · hand/limb glitches (S6 fists) · audio hard-fail / wrong line.

---

## Global criteria (apply to whole reel)
| ID | Dim | Severity | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| G-no-burned-text | spatial | blocker | No model-burned subs/captions/watermarks/gibberish (Latin or Devanagari) anywhere in S1-S8. Only legit text = the post gold karaoke layer + the S9 card. | scan every second s001-s061 | frame |
| G-aspect-res | spatial | major | Every frame 9:16 1080×1920, no bars, no squash. | s001,s010,s020,s030,s040,s050,s060 | frame |
| G-style-consistent | temporal | major | Consistent glossy 3D caricature look/grade; no live-action/2D/photoreal drift. | start-vs-end all scenes | frame |
| G-good-evil-read | semantic | blocker | <1s good/evil read: King dark/green/menacing; herbs + healthy stomach bright/warm. No dark hero scene, no warm King scene. | s004,s011,s019,s027,s035,s043,s050,s057 | frame |
| G-crossfade-continuity | temporal | major | Crossfades in right order S1→…→S9; no out-of-order scene, no black gap. | s008,s015,s023,s031,s038,s046,s053,s061 | frame |
| G-audio-bed | temporal | minor | One continuous bed, no seam dropouts; speech intelligible. | full runtime | needs-human |
| G-lines-in-order | semantic | blocker | Transcript = 8 scripted lines in order, each in its window, clean Hindi, none swapped/dropped/duplicated. | full runtime | needs-human |

## Caption layer (the intended gold karaoke, NOT model-burned)
| ID | Dim | Severity | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| CAP-present | semantic | blocker | Gold Devanagari karaoke present across S1-S8. | final s003,s011,s019,s027,s035,s043,s050,s057 | frame |
| CAP-script-correct | semantic | blocker | Per-scene caption = verbatim Devanagari script line (no typo/transliteration/wrong-scene). | final, per-scene readable frame + transcribe | needs-human |
| CAP-gold | spatial | major | Gold styling, legible (contrast/outline), not edge-clipped. | final s003…s057 | frame |
| CAP-placement | spatial | major | Lower-third clear of face/mouth and clear of the bottle label (S7/S8/S9). | final s011,s035,s050,s057,s062 | frame |
| CAP-karaoke-timing | temporal | minor | Highlight fill tracks the spoken words. | playback | needs-human |
| CAP-not-double | spatial | blocker | Gold caption NOT stacked on a Veo-burned caption (no doubled strips). | final s003…s057 | frame |

## Brand / product fidelity
| ID | Dim | Severity | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| BRAND-S9-legible | spatial | blocker | S9 = real bottle, fully legible BLUMELIFE + blue "Clear Gut", undistorted. The one guaranteed-legible frame. | s062,s063 | frame |
| BRAND-S9-tagline | semantic | blocker | S9 tagline = exactly "पेट हल्का। दिन हल्का।" + BLUMELIFE Clear Gut, correct, no typo. | s062,s063 | frame |
| BRAND-bottle-colorway | spatial | major | S7/S8 stylized bottle matches real colorway (amber glass, white dropper cap, yellow/white label). | s050,s053,s057,s060 vs asset | frame |
| BRAND-no-wrong-product | semantic | blocker | No competing/incorrect product; no pill/capsule/jar/spray substituted for the dropper bottle. | s050,s053,s057,s060,s062 | frame |

---

## S1, King (dialogue) · 0.0-8.0s · s001-s008
**Intent:** HOOK, comedic-menace villain establishes the problem.
**Line:** हा हा हा! मैं हूँ कॉन्स्टिपेशन किंग! तुम्हारा पेट मैं कभी साफ़ नहीं होने दूँगा!

| ID | Dim | Sev | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| S1-dominant-king | semantic | blocker | King (bible/king.png: brown boulder, gold crown, glowing eyes, jagged grin) dominant upper-center, comically gross, NOT horror. | s002,s004,s006 | frame |
| S1-stomach-faceless | spatial | blocker | Stomach ONLY a dim turned-away shadow at lower edge, no visible face, no mouth. | s002,s004,s006,s008 | frame |
| S1-single-mouth | temporal | blocker | Only King's mouth moves; shadow-stomach has no moving mouth. | motion | needs-human |
| S1-king-faces-lens | spatial | major | King faces lens, low-angle medium, slow push-in. | s002,s005,s008 | frame |
| S1-dark-grade | semantic | major | Dark gut-cave, sickly-green gas, hard top-light. | s003,s006 | frame |
| S1-no-burned-text | spatial | blocker | No burned subs/captions/gibberish. | s001,s003,s005,s007 | frame |
| S1-king-consistent | temporal | major | King identity stable start→end, no morph. | s001-vs-s008 | frame |
| S1-line-audio | semantic | blocker | Exact line, deep gravelly comic-villain voice, clean, post-pause start. | transcribe/audio | needs-human |
| S1-lipsync | temporal | major | King lip movement matches the line. | motion | needs-human |

## S2, Amla SOLO (dialogue) · 7.6-15.6s · s009-s015
**Intent:** Hero 1, warm, reassuring. **Line:** मैं हूँ भुई आँवला! मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ!

| ID | Dim | Sev | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| S2-amla-solo | spatial | blocker | Amla (pale-green gooseberry, single leaf, bible/amla.png) ALONE, centered MCU, facing camera. No other character. | s010,s012,s014 | frame |
| S2-warm-hero | semantic | blocker | Warm golden rim-glow; friendly GOOD-guy read, not menacing. | s011,s013 | frame |
| S2-single-mouth | temporal | major | Only Amla's mouth moves, animates while speaking. | motion | needs-human |
| S2-no-burned-text | spatial | blocker | No burned subs/captions/gibberish. | s009,s011,s013,s015 | frame |
| S2-consistent | temporal | major | Identity stable start→end vs bible. | s009-vs-s015 | frame |
| S2-line-audio | semantic | blocker | Exact line, warm confident heroic male voice, clean. | transcribe/audio | needs-human |
| S2-lipsync | temporal | major | Lip movement matches line. | motion | needs-human |

## S3, Ajwain SOLO (dialogue) · 15.2-23.2s · s016-s023
**Intent:** Hero 2, upbeat, energetic. **Line:** मैं हूँ अजवाइन! पेट का भारीपन और गैस, मेरा काम!

| ID | Dim | Sev | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| S3-ajwain-solo | spatial | blocker | Ajwain (tan/green ribbed carom seed, bible/ajwain.png) ALONE, centered MCU, facing camera, energetic. No other character. | s017,s019,s021 | frame |
| S3-warm-hero | semantic | blocker | Bright warm punchy; upbeat GOOD-guy read, not menacing. | s018,s020 | frame |
| S3-single-mouth | temporal | major | Only Ajwain's mouth moves, animates while speaking. | motion | needs-human |
| S3-no-burned-text | spatial | blocker | No burned subs/captions/gibberish. | s016,s018,s020,s022 | frame |
| S3-consistent | temporal | major | Identity stable start→end vs bible. | s016-vs-s023 | frame |
| S3-line-audio | semantic | blocker | Exact line, bright fast energetic voice, clean. | transcribe/audio | needs-human |
| S3-lipsync | temporal | major | Lip movement matches line. | motion | needs-human |

## S4, Saunf SOLO (dialogue, FEMALE) · 22.8-30.8s · s023-s030
**Intent:** Hero 3, calm, gentle; female voice. **Line:** मैं हूँ सौंफ! खाने के बाद की ब्लोटिंग को शांत करती हूँ!

| ID | Dim | Sev | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| S4-saunf-solo | spatial | blocker | Saunf (pale-green fennel bulb + feathery green fronds, bible/saunf.png) ALONE, centered MCU, facing camera, calm. No other character. | s024,s026,s028 | frame |
| S4-warm-hero | semantic | blocker | Bright soft gentle; calm GOOD-guy read, not menacing. | s025,s027 | frame |
| S4-single-mouth | temporal | major | Only Saunf's mouth moves, animates while speaking. | motion | needs-human |
| S4-female-voice | semantic | major | Voice clearly FEMALE (smooth gentle calm), not male. | audio | needs-human |
| S4-no-burned-text | spatial | blocker | No burned subs/captions/gibberish. | s023,s025,s027,s029 | frame |
| S4-consistent | temporal | major | Identity stable start→end vs bible. | s023-vs-s030 | frame |
| S4-line-audio | semantic | blocker | Exact line, clean female pronunciation. | transcribe/audio | needs-human |
| S4-lipsync | temporal | major | Lip movement matches line. | motion | needs-human |

## S5, Haritaki SOLO (dialogue) · 30.4-38.4s · s031-s038  ⚠ HIGH-RISK villain-leakage gate
**Intent:** Hero 4, wise warm elder. Bible ref `haritaki.png` is itself fierce (angry brow, glowing eyes, lightning), must read BENEVOLENT.
**Line:** मैं हूँ हरीतकी! आयुर्वेद की सबसे भरोसेमंद जड़ी बूटियों में से एक!

| ID | Dim | Sev | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| S5-haritaki-solo | spatial | blocker | Haritaki (amber/brown myrobalan elder, bible/haritaki.png form) ALONE, centered MCU, facing camera. No other character. | s032,s034,s036 | frame |
| S5-benevolent-not-villain | semantic | blocker | Reads BENEVOLENT: warm gold light, KIND/twinkling eyes, warm smile. NOT menacing, no harsh angry glowing eyes, no scowl, no threatening posture. Primary leakage gate. | s033,s035,s037 | frame |
| S5-warm-grade | spatial | major | Warm gold + gentle (non-threatening) shimmer; not dark/electric-storm. | s033,s036 | frame |
| S5-single-mouth | temporal | major | Only Haritaki's mouth moves, animates while speaking. | motion | needs-human |
| S5-no-burned-text | spatial | blocker | No burned subs/captions/gibberish. | s031,s033,s035,s037 | frame |
| S5-consistent | temporal | major | Identity stable start→end; benevolent expression holds all clip (no mid-clip turn to menacing). | s031-vs-s038 | frame |
| S5-line-audio | semantic | blocker | Exact line, deep wise kindly elder voice (warm, not threatening), clean. | transcribe/audio | needs-human |
| S5-lipsync | temporal | major | Lip movement matches line. | motion | needs-human |

## S6, Team (NARRATOR VO) · 38.0-46.0s · s039-s046
**Intent:** Team-up swell, 4 heroes shield the stomach; narrated, NO lip-sync. **Line:** ये चार ही नहीं, दस से ज़्यादा आयुर्वेदिक जड़ी बूटियों की पूरी फौज!

| ID | Dim | Sev | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| S6-four-heroes-shield | spatial | blocker | All 4 heroes in 3/4-profile TURNED INWARD shielding the hopeful stomach; King tiny/dark/cowering far back. | s040,s042,s044 | frame |
| S6-no-lens-mouths | spatial | blocker | NONE of the heroes (nor stomach) faces the lens, no front mouths to animate. | s040,s042,s044 | frame |
| S6-no-talking-mouths | temporal | blocker | Under narrator VO, NO character mouth moves / no visible talking. Narrated shot. | motion | needs-human |
| S6-heroes-good | semantic | major | Heroes bright/warm/heroic; King's corner dark/green/small. Contrast intact. | s041,s044 | frame |
| S6-no-burned-text | spatial | blocker | No burned subs/captions/gibberish. | s039,s041,s043,s045 | frame |
| S6-no-limb-glitch | spatial | major | Fists-up pose: no hand/finger/limb glitch, no fused/extra limbs, no warped faces. | s040,s043,s046 | frame |
| S6-identity-vs-bible | temporal | major | Each hero still recognizable vs bible (no merge/swap in crowd). | s039-vs-s046 | frame |
| S6-narration-audio | semantic | blocker | Exact narrator line, warm trustworthy male Hindi, clean. | transcribe/audio | needs-human |

## S7, Product reveal (NARRATOR VO) · 45.6-53.6s · s046-s053
**Intent:** Spectacle, herbs coalesce into a glowing stylized bottle. **Label legibility NOT required here.** **Line:** सबकी ताक़त, अब एक ही, आयुर्वेदिक क्लियर गट ड्रॉप्स में!

| ID | Dim | Sev | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| S7-bottle-forming | spatial | blocker | Centered: golden-light/herb streaks coalesce into ONE amber dropper-bottle form (stylized 3D). Bottle is the focal subject. | s048,s050,s052 | frame |
| S7-bottle-stable | temporal | major | Once formed, bottle stays still, no morph/wobble/melt into another shape. | s050-vs-s053 + motion | needs-human |
| S7-label-soft-ok | spatial | minor | Soft/glowing/illegible label is ACCEPTABLE by design. Do NOT fail S7 for a blurry label (unless it reads as a different product or a non-bottle). | s050,s052 | frame |
| S7-colorway | spatial | major | Reads as amber/brown dropper bottle with Clear Gut colorway, not a random bottle/jar/spray. | s050,s052 vs asset | frame |
| S7-no-characters | semantic | major | No herb-heroes/King in the reveal; flag stray character faces. | s048,s050,s052 | frame |
| S7-no-burned-text | spatial | blocker | No burned subs/captions/gibberish (soft real-label ok; floating gibberish not). | s047,s049,s051,s053 | frame |
| S7-narration-audio | semantic | blocker | Exact narrator line, warm trustworthy male Hindi, clean. | transcribe/audio | needs-human |

## S8, Resolution + CTA (NARRATOR VO) · 53.2-61.2s · s054-s061
**Intent:** Happy stomach beside the locked glowing bottle; narrated. **Line:** रोज़ सुबह और शाम, सिर्फ़ दस से पंद्रह बूँदें। पेट हल्का, दिन हल्का!

| ID | Dim | Sev | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| S8-happy-stomach | semantic | blocker | Stomach now HAPPY/bright/healthy (NOT the sad S1 stomach), clear transformation. | s055,s057,s059 | frame |
| S8-stomach-profile-offlens | spatial | blocker | Stomach in 3/4-profile looking AT the bottle; face/mouth turned AWAY from lens. | s055,s057,s059 | frame |
| S8-stomach-mouth-closed | temporal | blocker | Under narrator VO, stomach's mouth does NOT move / no visible talking. | motion | needs-human |
| S8-bottle-locked | temporal | major | Bottle on still pedestal, locked/steady, no morph/wobble; stays sharp. | s054-vs-s061 + motion | needs-human |
| S8-bottle-sharp-colorway | spatial | major | Bottle sharp (not forming) and matches colorway. Full label legibility NOT required (S9 carries it), don't fail solely for unreadable fine text. | s056,s058,s060 vs asset | frame |
| S8-no-burned-text | spatial | blocker | No burned subs/captions/gibberish. | s054,s056,s058,s060 | frame |
| S8-warm-grade | semantic | major | Bright clean healthy warm victory grade, not dark. | s056,s059 | frame |
| S8-narration-audio | semantic | blocker | Exact narrator CTA line, warm confident male Hindi, clean. | transcribe/audio | needs-human |

## S9, Product card (ffmpeg, NOT Veo) · 60.8-63.456s · s061-s063
**Intent:** Pixel-perfect brand close, real bottle still + Ken-Burns + burned tagline. The only guaranteed-legible brand frame.
**Text:** पेट हल्का। दिन हल्का। · BLUMELIFE Clear Gut

| ID | Dim | Sev | Criterion (PASS) | How to check | Frame/Human |
|---|---|---|---|---|---|
| S9-real-bottle | spatial | blocker | Real product image, centered, undistorted; BLUMELIFE + blue "Clear Gut" fully legible; pixel-perfect, no stylization/warp. | s062,s063 | frame |
| S9-tagline-correct | semantic | blocker | Tagline = exactly "पेट हल्का। दिन हल्का।" + BLUMELIFE Clear Gut; correct Devanagari, no typo/clip. | s062,s063 | frame |
| S9-clean-studio | spatial | major | Clean studio-warm card, gentle Ken-Burns, text clear of the label. | s062,s063 | frame |
| S9-no-veo-artifacts | spatial | major | Still card, no generative artifacts, no morph, no extra burned gibberish. | s062,s063 | frame |

---
*Authored by the scene-expectations agent. Hand `expectations.json` to the `video-reviewer`. This agent sets the bar; it does not score, generate, or edit.*
