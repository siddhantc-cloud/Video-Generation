# ElevenLabs voiceover v006

## Production checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Provider truth | Higgsfield and ElevenLabs catalogs are checked live before choosing a voice | Catalog/API check below | Voice producer | Complete |
| Rights-safe identity | Voice is an owned/designed voice or an authorized library voice | `NarratorZebPay`, category `generated`, already in the account | Voice producer | Complete |
| Indian mythological register | Voice is mature, resonant, Indian-English, reverent, and not an imitation of a public person | Voice description and generated audition | Voice producer | Complete |
| Exact copy | All 105 approved words survive synthesis and the final SFX mix | Scribe transcript, language probability 1.0 | Audio QC | Pass |
| Pronunciation | Vanaras, Ram Setu, Rama, SIP, and ZebPay are controlled and recoverable by ASR | Pronunciation dictionary r2 plus final-mix transcript | Audio QC | Pass |
| Frame lock | Narration and final mix are exactly 2,505,600 samples / 1,566 frames / 52.200 seconds | Phrase-lock EDL and FFprobe | Editor | Pass |
| Loudness | Social review mix remains near -16 LUFS and below -1.5 dBTP | -16.01 LUFS, -3.28 dBTP after AAC | Audio QC | Pass |
| Human voice approval | Owner listens to the complete encoded cut and accepts tone, pace, and pronunciation | v006 captioned review cut | Human | Pending |

## Verified provider decision

The earlier phrase “ElevenLabs introduced a mythology voice” was imprecise. ElevenLabs currently
**hosts** multiple Hindu-mythology voices in its Voice Library; they are not exposed as named
mythology presets in the live Higgsfield voice catalog, and the evidence does not prove they are
ElevenLabs-made premade voices.

The strongest exact match found on 2026-07-24 was:

- `Shardul K - Hindu Mythology Storyteller`
- ElevenLabs Voice Library ID: `6EphsklDopDQ6eRkwNHT`
- Hindi/India-trained, deep, middle-aged, reverent, and explicitly described for Ramayana narration
- Current account/API result: HTTP 402 `paid_plan_required`; free users cannot use Voice Library
  voices through the API
- No Shardul media was generated or charged by the failed request

The project therefore uses the account-owned Voice Design result already created for this film:

- Name: `NarratorZebPay`
- Voice ID: `al4r3VzsNW11MRVgGcBe`
- Category: `generated`
- Description: male, 38-48, Indian usage, deep/resonant, authoritative and grounded documentary
  narrator, measured delivery without theatrical exaggeration
- This is an original designed voice, not a clone or imitation of an actor/public figure

## Selected synthesis packet

| Field | Selected value |
|---|---|
| Provider | ElevenLabs direct API |
| Model | `eleven_v3` |
| Language | `en` |
| Stability | `0.50` |
| Similarity boost | `0.82` |
| Style | `0.12` |
| Speaker boost | `true` |
| Requested speed | `1.08` |
| Seed | `24072026` |
| Output | MP3, 44.1 kHz mono, 128 kbps |
| Source script | `scripts/short-narration-v004.txt` |
| Script SHA-256 | `8DA5B9AF90DA21ACADAE812F0A6D551406C0DE500551B0727C7ADB4308BE510D` |

Selected pronunciation dictionary:

- Name: `Ramayana-ZebPaySIP-v006-r2`
- Dictionary ID: `GvrRJdhzLD9Zwyp5IuX9`
- Version ID: `CYyuBmHultCS0TAMWTZd`
- r1 is superseded because its hyphenated `Zeb-pay` alias transcribed as “Zeppi”

| Written form | Synthesis alias |
|---|---|
| `vanaras` / `Vanaras` | `vaa-nuh-raas` |
| `Ram Setu` | `Raam Say-too` |
| `Rama` | `Raa-muh` |
| `SIP` | `ess eye pee` |
| `ZebPay` | `Zeb Pay` |

## Timing and mix

The raw continuous performance is 48.080 seconds. It is not globally stretched because that would
move some phrase starts by as much as 868 ms relative to the approved picture. Instead:

1. ElevenLabs character timestamps are converted to word timestamps.
2. Each mapped phrase starts no more than 30 ms after its existing picture beat.
3. Shorter phrases keep their natural delivery and receive silence at the tail.
4. Only K06, K07, and K09 overrun their slots; Rubber Band accelerates them by 1.005x, 1.210x, and
   1.048x respectively without pitch change.
5. Every slot has a 30 ms boundary fade and an exact integer sample count.
6. Approved native SFX stems are rebuilt against the same frame map at -10 dB.
7. The complete mix receives only +0.2 dB; no limiter or destructive dynamic normalization is used.

## Usage evidence

The restricted API key cannot read subscription/quota totals, so currency or plan-credit cost is
unknown and must not be invented.

| Operation | Measured usage |
|---|---:|
| Successful TTS auditions | 2 × 120 characters |
| Successful final TTS | 606 characters |
| Successful TTS total | 846 characters |
| Failed Shardul request | 0 media; HTTP 402 |
| Scribe verification total | 175.68 seconds / 2.928 minutes |

## Selected local artifacts

- Raw continuous narration:
  `Ramayana-ZebPaySIP_NARRATION_v006_raw_v001.mp3`
  (`01FEBE4ED8AF656C545D9D55697E1064FB3077B72C741F6FD993AE549080368C`)
- Phrase-locked narration:
  `../../../edit/audio/elevenlabs-v006/narration-phrase-locked-v003.wav`
  (`FAB95B9CDD65B8B9D5746177C1E3688BF5E81DD9D6A7A4088CC8F5E5A2D78CD5`)
- Native-SFX stem:
  `../../../edit/audio/elevenlabs-v006/sfx-native-phrase-locked-v001.wav`
  (`5462EEAB829501766AB36F7D91C7641205746D187A7FF58F4B0A87A1FC24539C`)
- 48 kHz stereo mix master:
  `../../../edit/audio/elevenlabs-v006/Ramayana-ZebPaySIP_AUDIO_MASTER_v006.wav`
  (`E9360849C099534511F6498DDE206E7B60260280574B74F9927C2D9CEDF516B4`)
- Caption timing:
  `../../../edit/master-short-v006-elevenlabs.srt`
- Review cut:
  `../../../deliverables/review-cuts/final-short-v006/Ramayana-ZebPaySIP_REVIEW_v006_elevenlabs_captioned.mp4`

## Current verdict

`NEEDS HUMAN`: technical, transcript, timing, loudness, SFX, caption, and encoded-file checks pass.
The owner must still listen to the complete review cut and approve the narrator’s subjective
mythological authority, commercial warmth, pace, and exact brand pronunciation before v006 can be
promoted over the approved v005 master.
