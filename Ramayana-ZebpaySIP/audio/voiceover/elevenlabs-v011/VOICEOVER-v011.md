# ElevenLabs phrase repair v011

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Known voice | Reuse the previously acceptable account-owned narrator | Voice ID and v006 record | Voice producer | Pass |
| No unnecessary upgrade | Current owned voice can synthesize through the API | Successful 51-character request | Producer | Pass for demo |
| SIP repair | The middle phrase begins with a clearly articulated initialism and no fused article | Candidate and encoded Scribe transcripts | Audio QC | Pass; human listening required |
| Surgical scope | Only G12 narration changes; picture, all other narration, and native SFX remain locked | Patch metadata and timeline | Editor | Pass |
| Music separation | Demo music is rights-recorded, independently replaceable, and ducked under speech | Music source and mix metadata | Sound editor | Pass |
| Human approval | Owner accepts the voice, SIP cadence, ZebPay, music, and SFX balance | Complete captioned v011 playback | Human | Pending |

## Voice identity and entitlement

- Provider: ElevenLabs direct API
- Model: `eleven_v3`
- Voice: `NarratorZebPay`
- Voice ID: `al4r3VzsNW11MRVgGcBe`
- Category: account-owned generated Voice Design voice
- Candidate seed: `24072029`
- Text: `S. I. P. lets you invest the same amount regularly.`

This is the same voice used in v006. It was not a named Higgsfield mythology preset. The restricted
API key cannot read the subscription object, so the current plan tier is unknown; however, synthesis
with this owned voice succeeded, so a paid upgrade was not required for this demo repair.

The stored request retains the v006 voice-setting fields for reproducibility. Current Eleven v3
documentation says speed, similarity, and speaker boost are not available controls on that model,
so those fields are request metadata rather than proof that v3 applied them.

The live Voice Library also contains `Shardul K – Hindu Mythology Storyteller`
(`6EphsklDopDQ6eRkwNHT`). It was not selected: current ElevenLabs documentation says free users
cannot use Voice Library voices through the API, and the already familiar owned narrator minimizes
another voice-direction variable. If the current account is free, move to a paid plan before
commercial campaign release because ElevenLabs assigns commercial rights to paid-plan generated
content.

Official references verified 2026-07-24:

- <https://elevenlabs.io/docs/overview/capabilities/voices>
- <https://elevenlabs.io/docs/eleven-creative/voices/voice-library>
- <https://elevenlabs.io/docs/overview/administration/billing>
- <https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries>
- <https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices>

## Pronunciation repair

The rejected structure put the short article immediately before the acronym. v011 removes that
article and starts the G12 phrase with the initialism. This is a copy edit, not merely a spelling
trick:

- rejected perception: `A SIP ...`
- selected synthesis: `S. I. P. lets ...`
- approved display copy for this review: `SIP lets ...`

The raw candidate is 4.320 seconds. Scribe v2 recovers `SIP` from 0.079 to 1.480 seconds and the
complete phrase. The candidate is pitch-preserving conformed into G12 frames 1116–1227 at
`1.144017857x`, with 30 ms boundary fades. The final encoded mixed-media transcript recovers the
complete narration including `SIP lets you invest...` and the closing `Start your SIP with Zebpay`.

Estimated text cost at the currently published $0.10 / 1,000 Multilingual v2/v3 character rate is
$0.0051 for this 51-character request, before any account discounts. This is an estimate, not a
claim about the inaccessible subscription balance.

## Mix

- Narration/SFX coefficients are restored to the v006 reference.
- Narration: +0.2 dB after equal-power mono-to-stereo conversion.
- Native SFX: net -9.8 dB.
- Master normalization: none.
- Limiter: none.
- Demo music: Mixkit `Sun and His Daughter`, static -15.42 dB, ducked another 6 dB during speech.
- Encoded result: -16.5 LUFS integrated, 4.2 LU LRA, -3.2 dBTP.

## Verdict

`NEEDS HUMAN`. The phrase, timing, encoded transcript, streams, captions, and mix architecture pass.
Human playback must accept the exact S-I-P cadence, narrator tone, ZebPay pronunciation, music
choice, and SFX balance before any promotion.
