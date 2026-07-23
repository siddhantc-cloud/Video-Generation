# Final short v003 QC

## Delivery checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Picture lock | Reviewed motion replaces the approved v004 cells without changing phrase timing | `edit/timelines/final-short-v001-phrase-map.json`; final EDL | Editor | Pass |
| K03 repair | Only the pebble-valid range is used; no disappearing-pebble frames enter the master | `edit/clips_graded/K03_v001_valid-conform.mp4`; conform contact sheet | Editor | Pass |
| Stream lock | 1,566 frames at 30 fps; video and audio are both exactly 52.200 s | FFprobe final master | QC | Pass |
| Decode | Complete video and audio decode with no reported error | `ffmpeg -v error` full pass | QC | Pass |
| Audio mix | Narration remains intelligible over shot-local native SFX | -16.22 LUFS integrated; -3.45 dB true peak | Sound/QC | Pass |
| Captions | Compact phrase-timed captions are readable and rendered after all graphics | 26-block SRT; v003 overview and boundary sheets | Editor/QC | Pass |
| Brand card | ZebPay logo and deterministic CTA remain unobstructed | `edit/verify/final-short-v003/end-card-contact.png` | Brand/QC | Pass |
| Boundaries | Every internal cut is free of an unintended black flash or corrupt frame | `edit/verify/final-short-v003/boundary-pairs-captioned.png` | QC | Pass |
| Black-frame check | No black interval of 0.10 s or longer outside the intentional short fades | FFmpeg `blackdetect` returned none | QC | Pass |
| Delivery variants | Captioned master, clean master, and poster are present and hashed | `deliverables/final/` | Editor/QC | Pass |
| Human/legal sign-off | Human watches the delivered master and confirms final brand/legal release | Delivery playback | Human/Brand | Pending |

## Self-QC passes

1. **v001:** rejected because long captions wrapped into large multi-line blocks and covered the
   vertical imagery.
2. **v002:** picture/caption readability passed, but the final spoken CTA caption duplicated and
   overlapped the deterministic ZebPay card.
3. **v003:** compact 3-5-word captions pass; the redundant G15 subtitle is omitted because the card
   already displays the spoken CTA verbatim. End-card and all boundary evidence pass.

The three-pass cap is reached with no unresolved operator-QC defect.

## Final deliverables

- Primary captioned master:
  `../deliverables/final/Ramayana-ZebPaySIP_FINAL_v003_1080x1920_captioned.mp4`
  - SHA-256: `3ECAEF672AB60B19A9B09D9E9B59013A8559019D0E3DD038E6C5DA9045176448`
  - 43,760,376 bytes
- Clean master:
  `../deliverables/final/Ramayana-ZebPaySIP_FINAL_v003_1080x1920_clean.mp4`
  - SHA-256: `E8DB9005891259091B678018ECCBC84D42FF96D79A8F04728B3E45623911CEA4`
  - 43,887,791 bytes
- Poster:
  `../deliverables/final/Ramayana-ZebPaySIP_FINAL_v003_poster.png`
  - SHA-256: `C23D83155EFF9E3B43AA1F2B1DD622DA47E4DB86C643E0E6C4F4EF233958DB0D`

## Audio exception

An optional 52.2-second ElevenLabs music-v2 request was attempted once and rejected by the provider
with HTTP 402 before media generation. No music file or charge was produced. The delivered mix uses
the approved narration and the reviewed Seedance-native ambience/SFX only; no low-quality substitute
was inserted.
