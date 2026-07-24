# Sarvam Bulbul v3 voiceover v009

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Indian-English route | Current Sarvam model and English voice recommendations are verified from official docs | Dated sources below | Voice producer | Pass |
| Credential safety | Key is loaded from ignored `.env` and never persisted | Credential/list endpoint check | Operator | Pass |
| Cheap audition | Difficult terms are tested across credible male voices before the full take | Four audition WAV metadata files and Scribe results | Voice producer | Pass |
| Pronunciation lock | SIP and ZebPay have explicit, versioned provider replacements | Dictionary `p_2811321e` and retest evidence | Sound editor | Pass; human phoneme check required |
| Natural settings | Voice uses native pace and warm storytelling temperature rather than compliance-style control | `mani`, pace 1.0, temperature 0.75 | Voice producer | Pass |
| Continuous performance | One full request carries the narration; only the closing same-voice phrase is comped from a verified retest | Raw v003, comp metadata, and raw v004 | Sound editor | Pass |
| Phrase lock | Narration is exactly 1,566 frames / 52.200 seconds | Phrase-lock EDL | Editor | Pass |
| Encoded review | Both variants decode, match frame/runtime, and share audio | v009 QC | Reviewer | Pass |
| Human listening | Owner accepts accent, naturalness, exact SIP initials, brand, pacing, and mix | `review/final-short-v009-human-rejection.md` | Human | Fail — rejected |

## Provider contract and selection

Verified 2026-07-24 against current official Sarvam documentation:

- Model: `bulbul:v3`
- Language: `en-IN`
- REST limit: 2,500 characters
- Selected speaker: `mani`
- Controls used: pace `1.0`, temperature `0.75`, WAV at 48 kHz
- Unsupported v3 controls: pitch and loudness
- Current beta price: ₹30 per 10,000 input characters

Official sources:

- <https://docs.sarvam.ai/api/getting-started/models/bulbul>
- <https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/change-the-speaker-voice>
- <https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/pronunciation-dictionary>
- <https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/best-practices>
- <https://docs.sarvam.ai/api/getting-started/pricing>

Sarvam recommends `ratan` for English, while `mani` has the lowest published production critical
error rate. The project audition made the production choice: `ratan` and `shubh` read the 145
characters in about 8.7 seconds; `mani` at temperature 0.75 took 12.971 seconds, recovered
`Vanaras`, `Ram Setu`, both SIP occurrences, and ZebPay, and better matched the film's measured
story cadence. The 0.80 `mani` retry became slower but lost reliable recovery of `vanaras` and the
brand, so 0.75 was selected.

## Pronunciation dictionary

Selected provider dictionary ID: `p_2811321e`.

```json
{
  "pronunciations": {
    "en-IN": {
      "SIP": "S I P",
      "ZebPay": "Zebb Pay"
    }
  }
}
```

The initial `Zeb Pay` replacement sometimes decoded as `Zepp Pay`. The same dictionary was updated
to `Zebb Pay`; the short retest then recovered `A SIP` and `Zebpay`. The final encoded review
recovers both SIP occurrences and `Zebpay`. ASR may merge the short article into the first acronym,
so exact phoneme and article acceptance remains a human listening decision.

## Generation and cost

The frozen display script is 606 characters, under the one-request limit. The selected full v003
take is 50.245 seconds. Its closing line was comped from a same-speaker, same-model, same-settings
pronunciation retest; the derived v004 raw performance is 50.372 seconds and preserves both source
hashes and edit points in its metadata.

| Operation | Requests | Characters | Estimated Sarvam cost |
|---|---:|---:|---:|
| Speaker/temperature auditions | 4 | 580 | ₹1.740 |
| Pronunciation retests | 2 | 154 | ₹0.462 |
| Full narration candidates | 3 | 1,818 | ₹5.454 |
| **Total TTS experiment** | **9** | **2,552** | **₹7.656** |

Dictionary create/update calls are not counted as TTS characters. ElevenLabs Scribe verification is
metered separately; the current key cannot read plan totals, so no currency amount is invented.

## Phrase lock and mix

- Comped raw WAV SHA-256:
  `1C76C9B893D133310D4BEE9F40048AD005C8E613E4B7756DF12E86E962DFF611`
- Phrase-locked WAV SHA-256:
  `15D5D24C125E582F2B9863A9A28DB5093B8227D86EFFD6522FE965C227C1B27F`
- Phrase-lock: 1,566 frames, 2,505,600 samples, 52.200 seconds
- Maximum phrase onset after cut: 30 ms
- Pitch-safe changed slots: K01 1.200x, K02 1.032x, K03 1.010x, G12 1.060x, K14 1.149x
- Reused native SFX stem: v006 at -10 dB, independently replaceable
- Audio master SHA-256:
  `5794DED38912658478210A70BF57A6A08D6ABC719BCC2C27087536FC7C7A132D`
- Encoded loudness: -16.06 LUFS integrated / -2.46 dBTP

## Verdict

`REJECTED`. Human playback on 2026-07-24 found the accent exaggerated enough to feel mocking, heard
the first article and acronym as the fused phrase “A SIP,” and found the dynamically normalized mix
less natural with the native SFX. The technical and ASR checks remain useful evidence, but they do
not qualify the performance for promotion. The approved v005 final remains unchanged.
