# Final short v009 Sarvam Bulbul v3 voiceover QC

## Review checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Source safety | Approved v005 final remains unchanged | v005 is the immutable picture source | Editor | Pass |
| Provider truth | Current model, controls, speakers, limit, and price are official and dated | `VOICEOVER-v009.md` sources | Voice producer | Pass |
| Indian-English route | Selected voice is produced by an India-focused `en-IN` model | Sarvam request metadata | Voice producer | Pass; human accent gate pending |
| Required terms | Encoded ASR recovers Vanaras, Ram Setu, Rama, both SIP occurrences, and ZebPay | Final Scribe v2 transcript | Audio QC | Pass |
| Exact copy | Human confirms the short article before the first SIP and all approved words | Final Scribe merges the article acoustically; phrase timing contains it | Human/Audio QC | Needs human |
| Acronym timing | SIP does not collapse into the rejected near-instant occurrence | Encoded spans 0.399 s and 0.500 s; conformed first SIP span 0.811 s | Audio QC | Pass as rejection evidence; listening required |
| Semantic timing | Every phrase starts within the accepted picture tolerance | Maximum phrase onset after cut: 30 ms | Editor/QC | Pass |
| Pitch-safe conform | Maximum local compression does not exceed the prior 1.21x ceiling | Maximum 1.200x; five changed slots | Editor/QC | Pass; K01/K14 listening required |
| Stream lock | Both variants are 1,566 frames with 52.200-second video/audio | FFprobe | QC | Pass |
| Audio identity | Clean and captioned variants contain the same AAC stream | MD5 `bd104521069e1e068a1dce449040093e` | Audio QC | Pass |
| Loudness | Speech-led social mix is near -16 LUFS with true-peak headroom | -16.06 LUFS, -2.46 dBTP after AAC | Audio QC | Pass |
| Decode | Full video and audio decode reports no error | FFmpeg exit 0 for both variants | QC | Pass |
| Black-frame check | No black interval of 0.10 seconds or longer | FFmpeg blackdetect returned zero intervals | QC | Pass |
| Caption order | Captions are rebuilt from v009 timing and burned last | v009 SRT and contacts | Editor/QC | Pass |
| Graph/logo safety | Captions remain readable and G15 is subtitle-free | Overview and boundary contacts | Brand/QC | Pass |
| Human listening | Owner accepts voice, accent, terms, pace, compression, and mix | `review/final-short-v009-human-rejection.md` | Human | Fail — rejected |

## Technical evidence

- Timeline/audio manifest: `edit/timelines/final-short-v009-sarvam.json`
- Voice record: `audio/voiceover/sarvam-v009/VOICEOVER-v009.md`
- Phrase-lock EDL: `edit/audio/sarvam-v009/narration-phrase-locked-v001-edl.json`
- Overview contact: `edit/verify/final-short-v009/overview-caption-contact.png`
- Boundary contact: `edit/verify/final-short-v009/boundary-caption-contact.png`
- Encoded transcript:
  `edit/audio/sarvam-v009/scribe-final-mix/Ramayana-ZebPaySIP_REVIEW_v009_sarvam-mani_captioned.json`

The final encoded transcript contains 104 word tokens because Scribe merges or omits the short
article immediately before the first SIP. The conformed provider timing retains that article from
37.228 to 37.322 seconds and the following SIP from 37.379 to 38.190 seconds. This is useful timing
evidence, not permission to claim exact human-perceived copy. Human playback closes that blocker.

## Outputs

- Clean review:
  `deliverables/review-cuts/final-short-v009/Ramayana-ZebPaySIP_REVIEW_v009_sarvam-mani_clean.mp4`
  - SHA-256: `EE5C2C81FB36CDA1AB80FB51D8CC900DEA6442723B40E10BD9106E7927C46234`
  - 50,389,841 bytes
- Captioned review:
  `deliverables/review-cuts/final-short-v009/Ramayana-ZebPaySIP_REVIEW_v009_sarvam-mani_captioned.mp4`
  - SHA-256: `FEFB1FAAD69A82C2E532254E6C2969B4D4754262A0E247638C74DAF4AFA3ED8D`
  - 44,141,626 bytes

## Verdict

`REJECTED`. Owner playback supersedes the technical pass: the accent felt exaggerated, “A SIP”
fused into one phrase, and the normalized mix changed the perceived SFX relationship. v009 remains
rejection evidence and is not a replacement final.
