# Production decisions

## Locked-decision checklist

| Decision | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Story | Ram Setu squirrel story remains the creative spine | `scripts/original-script.md` | Human/Creative | Locked |
| Message | Consistency beats trying to time the market | Script close and SIP parallel | Human/Creative | Locked |
| Format | Entire film is designed for 9:16 vertical presentation | Keyframes and review exports | Director/Editor | Locked |
| Look | Grounded photoreal mythological epic; canonical palette, lighting, texture, performance, and UI encoding | `project/global-visual-law.md`, short-v004 motion review | Director/Art | Creative law and 480p motion behavior validated; fine-detail production validation remains separate |
| Structure | Mythological story → investment parallel → sponsor close | v004 storyboard, animatic, and final phrase map | Director/Human | Locked at 52.2 seconds |
| Narration | One continuous Indian-English narrator carries the film | v004 narration and word-boundary source | Human/Sound | Locked for the v003 experimental delivery |
| Generated sound | Seedance production candidates carry diegetic SFX and ambience only; narration and music remain separate stems | Operating spec and final mix | Human/Sound | Native SFX mixed; optional music unavailable and documented |
| Text | `राम`, captions, financial copy, and logo are created in post | End-card assets and shooting script | Editor/Brand | Locked |
| Shot discipline | One clear action and one camera move per moving shot | `scripts/shooting-script.md` | Director | Locked |
| Edit timing | Audio-master, integer-frame timeline prevents drift | `edit/AV_SYNC_SYSTEM.md` and EDLs | Editor | Locked |
| Animatic-first conform | The frame-locked keyframe animatic is the editorial source of truth; approved moving footage replaces its cells without losing the narration clock | `edit/timelines/final-short-v001-phrase-map.json`; final EDL | Human/Editor | Complete for v003 |
| Experiment engine | Learning-phase video trials keep `seedance_2_0` in `std` mode, high bitrate, and Sound On; change only resolution, duration, prompt, or approved references; Fast, Mini, and Seedance 1.5 are not fidelity proxies | Human direction plus live CLI/model evidence, 2026-07-23 | Human/Director | Locked |
| Experiment resolution | Learning-phase Seedance trials use 480p, the live minimum; a 480p pass is diagnostic and cannot become a final-detail approval | Live CLI schema/cost preflight, 2026-07-23 | Human/Director | Locked |
| Experiment duration | Use the duration required by the complete visual beat and its known failure window; four seconds is only a narrow mechanics probe, while 15 seconds is used only when one coherent oner or purposeful multi-shot scene genuinely needs it | EDL, Seedance 4–15 s schema, S1-a late-cut evidence | Human/Director | Locked |
| Continuity inputs | Fresh shots re-anchor from the shot start frame plus canonical character/location assets; an end frame is optional; the previous accepted video is attached only for direct continuation or an explicitly limited motion/camera role | Operating spec §§7–9 | Director/Continuity | Locked |
| Final runtime | Human approves duration for the destination platform | Approved short v004 and final v003 are 52.2 seconds | Human/Editor | Locked |

## Current production state

- The 52.2-second v004 animatic, continuous narration, phrase map, deterministic SIP graphics, and
  ZebPay end card are the approved short-form source of truth.
- Eleven short-v004 motion cells have immutable 480p Seedance outputs. Ten are full keepers; K03 is
  a documented partial keeper using only its valid 0.00-1.50-second range.
- Captioned and clean v003 masters plus a poster are in `deliverables/final/`; operator QC passes
  frame count, duration, decode, sync, loudness, captions, boundaries, and end-card integrity.
- The delivered v003 picture is a 1080x1920 master built from 480p diagnostic source clips. It is the
  completed low-resolution experimental film, not evidence of final facial/fur/texture detail at a
  higher Seedance resolution.
- Human playback and brand/legal release approval remain external gates.
- Older `generate_audio=false` notes are historical. The 2026-07-21 operating spec controls future
  production: native diegetic SFX/ambience on, with narration and music produced separately.
- A 480p Standard experiment may approve shot purpose, blocking, screen direction, camera behavior,
  unwanted internal cuts, gross continuity, and native-SFX timing. It does not approve final facial
  detail, hands/contact anatomy, fur/stripe detail, texture, or true high-resolution delivery
  quality. A later high-resolution candidate is a fresh roll and must pass the complete keeper
  review again.

## Creative rules

- Preserve Rama’s face, costume, bow, and reverent presence across scenes.
- Preserve the squirrel’s body proportions, three stripes, and tail.
- Keep crowd faces distant unless a named character is required.
- Do not rely on generated text or logos.
- Use deterministic graphics for the investing parallel and sponsor card.
- Prefer story clarity and emotional continuity over complex motion.
- Pilot high-risk contact shots before producing a batch.

## Approval gates

1. Human approves brief and script.
2. Human approves storyboard and keyframes.
3. Human approves timed animatic and runtime.
4. Director approves pilot footage quality.
5. Director approves every selected shot.
6. Human approves picture lock.
7. Human/brand/legal approve claims, logo, captions, and sponsor close.
8. Human approves the QC-passed master.

An artifact existing is not the same as an approval. Record approvals and revision notes in `review/`.
