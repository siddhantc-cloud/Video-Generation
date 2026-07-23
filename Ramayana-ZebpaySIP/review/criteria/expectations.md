# Scene expectations (the BAR): ZebPay SIP - "The Squirrel in Ram Setu"

**Engine:** Seedance 2.0 image-to-video (Higgsfield), native diegetic SFX/ambience enabled on production candidates; characters remain non-speaking and there is no lip-sync.
**Format:** 9:16 vertical, 1080x1920, 24fps. **Look:** photoreal grounded-mythic (Nolan warm register + 2026 Ramayana film), ANTI-uncanny (must read photographed, not CGI).
**VO:** a single external ElevenLabs Indian-English narrator track, verbatim, added in the edit (NOT per clip). **Music:** separate post-production stem. **Text/logo:** Mode B (rendered), never generated.
**Machine contract:** `expectations.json` (the reviewer consumes that; this file is the human-readable mirror).

Source of truth: `01_script_AIFRIENDLY.md` (directed shot list + Gate A resolutions) and `00_input_script_HUMAN.md` (creative truth). Gate A audit folded in: `gateA_assistant_director_audit.md`.

---

## Definition of done

**PASS = zero FAILED blocker criteria** across all shots AND the final-timeline blockers.
- **Blocker** = ship-stopper (broken/wrong hero identity, fused/melted contact, morph where a locked still was specced, legible garbled text, wrong brand logo, wrong/garbled VO). Batch or ad is unshippable.
- **Major** = visible photoreal defect; Director triages (fix vs accept-with-reason).
- **Minor** = polish.

Every **needs-human** criterion (motion smoothness, jitter/flicker, morph-through-motion, contact no-fuse, identity-drift-through-motion, exact stripe stability, native SFX sync/content, VO quality) MUST be confirmed by the video-reviewer on PLAYBACK (Higgsfield video-analysis for motion, audio playback, and Whisper/UTMOS for the VO). Stills and transcripts cannot close them. A shot with an unresolved needs-human blocker is NOT done.

**Reviewer verdicts:** each criterion is marked **PASS / FAIL / NEEDS-HUMAN** with cited frame (or clip/timestamp) evidence.

**Reel windows are approximate** (pacing proposal). The VO is one continuous track; final durations are set at assembly. Do not fail a shot on reel timing alone.

---

## Global Mode C criteria (apply to every generative shot S1-a ... S7-a)

Listed once; each shot inherits them. Reviewer scores them per shot.

| ID | Dim | Criterion (PASS looks like) | Severity | How to check | Flag |
|---|---|---|---|---|---|
| G-aspect | spatial | native 9:16 (1080x1920), full-frame, no letterbox/pillarbox/stretch | major | frame@any | frame |
| G-photoreal | spatial | photoreal grounded-mythic texture (weathered stone, real fabric, fur/skin detail, grain); NOT smooth/plasticky/uncanny CGI | major | frame@mid | frame |
| G-no-burned-text | spatial | NO model-burned words/captions/subtitles/watermarks/UI anywhere | major | frame@start,mid,end | frame |
| G-warm-grade | spatial | warm golden-hour, high-contrast, crushed true blacks (not cool/desaturated/flat) | minor | frame@mid | frame |
| G-clean-firstframe | spatial | START frame is clean (no warped hand / fused digit / melted face for motion to amplify) | major | frame@0 | frame |
| G-one-move | temporal | EXACTLY the one specced camera move; no invented second move | major | motion | needs-human |
| G-smooth | temporal | smooth constant-speed motion; no jitter, flicker, or strobing | major | motion | needs-human |
| G-no-artifact | temporal | no melt/morph/smear of subject or props; no extra/fused limbs/digits; hands/paws not warped; no object pop-in/out | major | motion | needs-human |
| G-diegetic-audio | temporal | visible physical beats have synchronized, location-correct SFX and restrained ambience | major | audio+motion | needs-human |
| G-no-generated-speech | semantic | character mouths remain closed; generated track contains no speech, narrator, or music-like layer | blocker | audio+motion | needs-human |

---

## Final-timeline criteria (scored on the assembled ad, not per clip)

| ID | Dim | Criterion | Severity | How to check | Flag |
|---|---|---|---|---|---|
| F-vo-verbatim | semantic | VO speaks the EXACT frozen script, in order, verbatim | blocker | transcribe/audio | needs-human |
| F-vo-clean | semantic | no voiced punctuation (the "And..." ellipsis is a PAUSE, not spoken); no dash garble; clean Indian-English pronunciation | blocker | audio | needs-human |
| F-vo-consistent | temporal | ONE consistent narrator voice across the whole ad | blocker | audio | needs-human |
| F-music-headroom | spatial | scored mythic-orchestral bed present, sits UNDER the VO (narration intelligible), no lyrics | major | audio | needs-human |
| F-sfx-continuity | temporal | native SFX beds cut smoothly, match visible action, and do not jump in ambience between neighboring shots | major | audio+timeline | needs-human |
| F-mix-intelligibility | temporal | narration remains intelligible over SFX and music; foreground effects are present without masking words | blocker | audio+timeline | needs-human |
| F-captions | spatial | any burned karaoke = exact script, correct spelling, clear of subject/logo; no stray Seedance-burned text survives | major | final-only | frame |
| F-vo-shot-sync | temporal | VO sentences land over their intended shots (natural alignment) | minor | audio+timeline | needs-human |

---

## Special bars encoded (call-outs)

- **Rama shots (S1-a, S4-a, S4-b, S4-c, S4-d):** identity-match-to-bible is a **BLOCKER**. Match to the bible SHEET, never re-derive from a video frame. Drift ceiling = no facial-feature morph start-to-end. **S1-a is the pilot**: it must also clear the Seedance content filter (photoreal deity face intact) before any other Rama shot is batched.
- **S4-c (hardest):** squirrel sits IN the palm WITHOUT fusing/melting; **small settle**, not a ground-to-palm teleport; Rama's face OUT of frame (macro on hands); hands anatomically clean. Four blockers.
- **S4-d:** the three stripes are **STABLE in-clip**; the reveal is a Mode B post overlay. Any in-clip stripe morph/brighten = FAIL.
- **S3-e (high risk):** the pinched stone must **survive the flick** (not vanish/warp/smear); tight two-subject frame; **both identities intact and un-blended**. Two blockers; two-shot cutaway is the fallback.
- **S5-e:** a camera push on a **LOCKED still** (Mode B Ken-Burns, O2 approved); **NO morph of pebbles into boulders**. Blocker if any content transforms.
- **Mode B shots (S6, S7-b, S5-e):** short bar - correct text/logo, legible, on-brand, timed; **no generative-artifact criteria**.

---

## Per-shot bars

### S1-a - PILOT + establish Rama (reverent, mythic)
VO: "Across this ocean waited a battle for dharma..."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S1a-identity-bible | spatial | Rama face/crown/jewelry/skin/attire match the Rama bible sheet | blocker | frame@0 vs sheet | frame |
| S1a-drift | temporal | no Rama identity drift through the push-in (no feature morph) | blocker | start-vs-end + motion | needs-human |
| S1a-filter | semantic | photoreal deity face rendered intact, NOT filtered/blurred/garbled (pilot gate) | blocker | frame@0,mid,end + gen-success | frame |
| S1a-props | spatial | Dhanush (bow) in hand, correct single form, not warped/duplicated | major | frame@0,end | frame |
| S1a-framing | spatial | heroic wide, low angle, centered full-height, facing the sea | major | frame@0 | frame |
| S1a-move | temporal | single slow push-in; hair/cloth drift; no 2nd move | major | motion | needs-human |
| S1a-register | semantic | reverent/heroic/solemn, not menacing/casual | major | frame@mid | frame |

### S1-b - the vanara sena (scale)
VO: "And to get there, an army would build... A bridge across the sea."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S1b-subject | spatial | massed vanara crowd (thousands) behind Rama; one army | major | frame@0 | frame |
| S1b-crowd-faces | spatial | crowd distant/loose; no individual non-human face at macro | major | frame@end | frame |
| S1b-one-move | temporal | EXACTLY one move = slow aerial pull-back (not crane+dolly) | major | motion | needs-human |
| S1b-scale | semantic | pull-back reveals scale; reads "impossible build begins" | minor | start-vs-end | frame |

### S1-c - boulder hurl + splash
VO: "Stone by stone. Boulder by boulder. Each one marked with Ram's name..."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S1c-no-name-text | spatial | NO legible "Ram's name" or any readable letters on boulders | blocker | frame@0,mid,end | frame |
| S1c-subject | spatial | single large boulder arcing, ending on a large splash plume | major | start-vs-end | frame |
| S1c-object-survival | temporal | boulder stays large/readable through the arc; no vanish/tear/float | major | motion | needs-human |
| S1c-splash-physics | temporal | splash reads as real water physics, not torn/smeared/frozen sheet | major | motion | needs-human |
| S1c-framing | temporal | wide, eye level, static with slight tilt following the arc (one move) | minor | motion | needs-human |

### S2-a - establish the squirrel (curious, humble)
VO: "And in the middle of all that grandeur, something much smaller had also arrived."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S2a-identity | spatial | matches squirrel bible (Indian palm squirrel, correct body/face) | major | frame@0 vs sheet | frame |
| S2a-stripes | spatial | three stripes present, correct positions (baseline) | major | frame@0 | frame |
| S2a-scale | spatial | squirrel small in frame vs the vast construction | major | frame@0 | frame |
| S2a-move | temporal | single slow push-in, small head turn; no 2nd move | minor | motion | needs-human |
| S2a-register | semantic | curious/humble arrival, not a cartoon mascot | minor | frame@mid | frame |

### S2-b - squirrel picks up a pebble (strain)
VO: "It couldn't carry boulders."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S2b-identity | temporal | squirrel + stripes stable through motion | major | start-vs-end | needs-human |
| S2b-pebble | temporal | one pebble, ends in mouth; no vanish/float/duplicate | major | motion | needs-human |
| S2b-action | semantic | reads as pick-up with slight strain (weight) | major | start-vs-end | frame |
| S2b-framing | spatial | MCU, eye level, gentle push-in, telephoto, squirrel large | minor | frame@0 | frame |

### S2-c - squirrel places the pebble
VO: "So it carried what it could."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S2c-identity | temporal | squirrel + stripes stable vs bible | major | start-vs-end | needs-human |
| S2c-pebble | temporal | pebble from mouth into the gap; set by end; no vanish/warp | major | motion | needs-human |
| S2c-action | semantic | careful placement, then drawing back | major | start-vs-end | frame |
| S2c-bridge-state | spatial | boulder gap matches the bridge-state ref | major | frame@0 vs ref | frame |

### S3-a - squirrel at the gap (sets up mockery)
VO: "Of course, one of the vanaras noticed."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S3a-identity | temporal | squirrel + stripes stable | major | start-vs-end | needs-human |
| S3a-pebble | temporal | pebble nudged toward gap; survives | major | motion | needs-human |
| S3a-framing | spatial | CU, telephoto, squirrel large | minor | frame@0 | frame |

### S3-b - establish the lead vanara (boastful)
VO: "And... decided to make a point of it."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S3b-identity | spatial | lead vanara matches the vanara bible sheet (establishes lock) | major | frame@0 vs sheet | frame |
| S3b-action | temporal | hoists a massive boulder onto shoulder + flex; boulder no warp/float | major | motion | needs-human |
| S3b-framing | spatial | medium wide, low angle (looms), slow push-in, chiaroscuro | major | frame@0 | frame |
| S3b-hands | spatial | gripping hands correct: no warp, no extra/fused digits | major | frame@mid,end | frame |
| S3b-register | semantic | boastful/playful-mockery, not heroic-divine and not horror-menace | major | frame@mid | frame |

### S3-c - same vanara grins, two boulders
VO: "He made sure everyone laughed with him."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S3c-identity | temporal | reads as the SAME vanara as S3-b (continuous) | major | frame@0 vs S3-b | needs-human |
| S3c-action | semantic | a boulder in each hand raised, broad grin, chest out | major | start-vs-end | frame |
| S3c-hands | spatial | both hands grip a boulder; not warped/fused, no extra digits | major | frame@end | frame |
| S3c-register | semantic | playful-mockery grin, not menace | major | frame@mid | frame |

### S3-d - baby vanara strolls (comic contrast)
VO: "Even the babies were outdoing it without breaking a sweat."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S3d-identity | spatial | baby vanara matches ref, carrying a decent stone | major | frame@0 vs ref | frame |
| S3d-action | temporal | strolls mid-stride, casual; stone stable | major | motion | needs-human |
| S3d-framing | temporal | medium wide, eye level, single slow tracking | minor | motion | needs-human |
| S3d-register | semantic | casual/effortless comic contrast, not straining | minor | frame@mid | frame |

### S3-e - HIGH RISK: the flick (deadpan)
VO: "Naturally, nobody clapped."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S3e-two-identity | spatial | BOTH identities intact + un-blended in the tight frame (vanara + squirrel, no hybrid) | blocker | frame@0,mid,end | frame |
| S3e-stone-survival | temporal | the pinched stone SURVIVES the flick (present, large/near-frame; no vanish/warp/smear) | blocker | motion | needs-human |
| S3e-no-blend-motion | temporal | no vanara/squirrel blend or morph THROUGH the motion | major | motion | needs-human |
| S3e-framing | spatial | tight two-shot, macro-telephoto, fingers + squirrel face share frame, slight tilt on flick | major | frame@0 | frame |
| S3e-hands | spatial | flicking fingers not warped, no extra/fused digits | major | frame@mid | frame |
| S3e-register | semantic | deadpan vanara + squirrel reaction; comedic dismissal, not cruel/horror | major | frame@end | frame |
| S3e-fallback-flag | temporal | PROCESS: if stone warps/vanishes or identities blend by attempt 2, use the two-shot cutaway | minor | motion | needs-human |

### S4-a - Rama notices (warm, reverent) - identity must match S1-a
VO: "But someone else was watching too."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S4a-identity-bible | spatial | Rama matches the Rama bible sheet | blocker | frame@0 vs sheet | frame |
| S4a-identity-match-s1a | semantic | reads as the SAME Rama as S1-a (continuous crown/face/attire) | blocker | frame@0 vs S1-a | needs-human |
| S4a-drift | temporal | no drift through the push-in (no feature morph) | blocker | start-vs-end + motion | needs-human |
| S4a-props | spatial | bow in hand, correct form, not warped/duplicated | major | frame@0 | frame |
| S4a-framing | spatial | medium, eye level, slow push-in, telephoto, god-ray backlight; eyeline settles down | major | frame@0 | frame |
| S4a-register | semantic | reverent/warm/watching, not stern/menacing | major | frame@mid | frame |

### S4-b - Rama walks toward the squirrel
VO: "And he wasn't looking at the boulders."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S4b-identity | temporal | Rama identity + attire stable through the walk vs `assets/characters/` and `keyframes/S1-a.png` | blocker | start-vs-end + motion | needs-human |
| S4b-gait | temporal | natural walk; legs/feet not warped; no melt/morph | major | motion | needs-human |
| S4b-framing | temporal | medium wide, eye level, single slow tracking, telephoto | minor | motion | needs-human |
| S4b-action | semantic | reads as walking toward the squirrel, beginning to lower | major | start-vs-end | frame |

### S4-c - HARDEST: squirrel settles into the palm (macro on hands, face OUT)
VO: "He was looking at the only one who showed up without being asked to."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S4c-no-fuse | temporal | squirrel is a SEPARATE body in/at the palm; NO fuse/melt/merge at contact | blocker | motion | needs-human |
| S4c-small-settle | temporal | small settle-and-lift (squirrel already at palm edge); NOT a ground-to-palm teleport | blocker | start-vs-end + motion | needs-human |
| S4c-face-oof | spatial | Rama's FACE OUT of frame the whole clip (macro on hands); face in frame = FAIL | blocker | frame@0,mid,end | frame |
| S4c-hands | spatial | palm/fingers anatomically correct; no warp, no extra/fused/floating digits | blocker | frame@0,mid,end | frame |
| S4c-squirrel-identity | temporal | squirrel + stripes intact and un-morphed at the palm | major | start-vs-end | needs-human |
| S4c-framing | spatial | macro on hands, eye level, very slow push-in, telephoto shallow DoF | major | frame@0 | frame |
| S4c-register | semantic | tender/reverent contact (chosen one held gently) | major | frame@end | frame |

### S4-d - stroke the back; stripes STABLE in-clip (reveal = post overlay)
VO: "Some bridges are built with strength. Some are built with heart. The wise ones know you need both."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S4d-stripes-stable | temporal | the three stripes stay STABLE/unchanged in-clip; NO in-clip morph/brighten/reveal | blocker | start-vs-end + motion | needs-human |
| S4d-no-smear | temporal | fur/back texture along the stroke path does NOT smear | major | motion | needs-human |
| S4d-face-oof | spatial | Rama's face OUT of frame (extreme CU on back + fingers) | major | frame@0,mid,end | frame |
| S4d-hands | spatial | two fingers/hand not warped, no extra digits | major | frame@mid | frame |
| S4d-squirrel-identity | temporal | squirrel back/coat matches bible; no identity morph | major | start-vs-end | needs-human |
| S4d-action | semantic | reads as two fingers stroking gently down the back (micro push-in) | major | start-vs-end | frame |

### S5-a - montage: calm sea pickup
VO: "Some days the sea was calm."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S5a-identity | temporal | squirrel + stripes stable | major | start-vs-end | needs-human |
| S5a-sea-state | spatial | calm/still water reads (contrast to S5-b) | major | frame@0 | frame |
| S5a-pebble | temporal | ends with pebble in mouth; survives | major | motion | needs-human |
| S5a-framing | spatial | medium, low/eye level, slow tracking, telephoto, squirrel large | minor | frame@0 | frame |

### S5-b - montage: rough surf struggle (float risk)
VO: "Some days it wasn't."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S5b-identity | temporal | squirrel + stripes stable in the water | major | start-vs-end | needs-human |
| S5b-no-float | temporal | paws visibly in contact with wet sand/rock; NOT floating/disappearing in surf | major | motion | needs-human |
| S5b-sea-state | spatial | rough surf/waves read (contrast to S5-a) | major | frame@0 | frame |
| S5b-action | semantic | struggles forward, reaches firmer ground w/ spray; effort-still-goes | major | start-vs-end | needs-human |

### S5-c - montage: wedge a pebble into the line
VO: "The squirrel never waited for the right day."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S5c-identity | temporal | squirrel + stripes stable | major | start-vs-end | needs-human |
| S5c-pebble-line | temporal | lengthening line of same-size pebbles; new one wedged; survives | major | motion | needs-human |
| S5c-bridge-state | spatial | matches bridge-state ref (half-built + pebble line) | major | frame@0 vs ref | frame |
| S5c-action | semantic | reads as wedging the pebble, then drawing back | major | start-vs-end | frame |

### S5-d - the growing bridge (slow pan reveal)
VO: "It didn't matter if the tide was high or low that day. The pebble went in anyway."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S5d-bridge-state | spatial | matches bridge-state ref; same evolving structure (continuity) | major | frame@0 vs ref | frame |
| S5d-one-move | temporal | single slow pan along the pebble line only; no 2nd move | major | motion | needs-human |
| S5d-pebble-consistency | spatial | pebbles roughly the same size along the line | minor | frame@mid | frame |
| S5d-no-morph | temporal | structure does not morph/shift/grow during the pan (reveal, not a build) | major | motion | needs-human |

### S5-e - macro payoff push (Mode B Ken-Burns on a LOCKED still; NO morph)
VO: "One pebble, placed once, means nothing. The same pebble, placed again and again... that's what holds a bridge together."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S5e-no-morph | temporal | pebbles do NOT morph into boulders; ONLY change is the camera push on a static locked still (Mode C fallback = hard blocker + all globals) | blocker | start-vs-end + motion | needs-human |
| S5e-content | spatial | macro of the pebble-filled gap; pebbles read as load-bearing, indistinguishable from boulders | major | frame@0 | frame |
| S5e-smooth | temporal | smooth constant-speed Ken-Burns push; no jitter/parallax tear | major | motion | needs-human |
| S5e-no-burned-text | spatial | no burned text on the still | minor | frame@0 | frame |

### S7-a - the payoff hero shot (triumphant; the money frame)
VO: "You don't need to time the market... That's not a squirrel's trick. That's SIP."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S7a-squirrel-identity | spatial | squirrel large enough to hold identity, + three stripes, on a fused pebble | major | frame@0 vs sheet | frame |
| S7a-bridge-state | spatial | completed golden bridge matches the completed bridge-state ref | major | frame@0 vs ref | frame |
| S7a-framing | spatial | extreme wide, low-angle heroic, anamorphic; squirrel readable; golden light | major | frame@0 | frame |
| S7a-register | semantic | triumphant/golden payoff reads without the VO | major | frame@mid | frame |
| S7a-move | temporal | single slow push-in, light shimmer; near-static; no 2nd move, no morph | major | motion | needs-human |

---

## Mode B shots (rendered, not generated) - short bars

### S6 - the parallel (clean transition, no mythology)
VO: "Most people wait for the right time to invest... [Pause.] It showed up the same way, every time, and let the average take care of the rest."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S6-no-mythology | spatial | clean transition, NO mythology visuals; calm type/abstract field | major | frame@any | frame |
| S6-text-correct | spatial | any on-screen text = exact intended words (V17/V18), correct spelling | blocker | frame@each-card | frame |
| S6-legible | spatial | legible, on-brand type, high contrast, clear of edges | major | frame@any | frame |
| S6-timed | temporal | card timing holds under the VO with the Pause beat | major | timeline+audio | needs-human |
| S6-deterministic | spatial | rendered Mode B: no generative artifacts | major | frame@any | frame |

### S7-b - ZebPay logo card
VO: "This video is brought to you by ZebPay, India's oldest crypto exchange. Like, share, and subscribe."
| ID | Dim | Criterion | Sev | Check | Flag |
|---|---|---|---|---|---|
| S7b-logo-correct | spatial | correct official ZebPay lockup, accurate colors/proportions, not re-drawn/distorted | blocker | frame@any vs logo asset | frame |
| S7b-text | spatial | any card text spelled correctly, on-brand | blocker | frame@any | frame |
| S7b-placement | spatial | logo minimal, bottom corner, clear of edges, legible | major | frame@any | frame |
| S7b-timed | temporal | card timing matches the outro VO | minor | timeline+audio | needs-human |
| S7b-deterministic | spatial | rendered Mode B: no generative artifacts | major | frame@any | frame |

---

## Reviewer note

Hand `expectations.json` to the `video-reviewer`. For each shot, mark every criterion **PASS / FAIL / NEEDS-HUMAN** with cited frame (or clip + timestamp) evidence. The `frame` items are closable from stills / the bible sheet / the attached reference. The `needs-human` items (all motion, contact no-fuse, identity-drift-through-motion, exact stripe stability, and the whole final-timeline VO block) require playback / Whisper / UTMOS and cannot be closed from stills alone. Ship only when zero blockers FAIL and the Director has triaged the majors.

*No em-dash characters used.*
