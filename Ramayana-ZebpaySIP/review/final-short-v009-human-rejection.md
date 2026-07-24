# Final short v009 human rejection

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Accent | Indian-English delivery feels natural and respectful | Complete v009 playback | Human | Fail |
| SIP phrase | The article and acronym do not fuse into an awkward phrase | Complete v009 playback | Human | Fail |
| Mix | Narration processing preserves the accepted native-SFX relationship | v009 versus v006 playback | Human | Fail |
| Promotion | Only an accepted voice and mix may replace the approved final | This rejection | Producer | Locked |

## Owner feedback

Recorded 2026-07-24:

- The Sarvam performance sounded too exaggeratedly Indian and risked feeling like a mockery.
- The first occurrence was heard as the fused phrase “A SIP,” despite the dictionary and ASR pass.
- The post-processing made the native SFX relationship feel weaker and less natural.

## Technical interpretation

The SFX stem itself remained at the nominal v006 level, but v009 applied two-pass dynamic
normalization to the complete mix. The denser narration and lower measured loudness range changed
masking and perceived balance. Therefore the correct repair is not “turn everything louder.” It is
to restore the accepted v006 narration/SFX coefficients, omit full-mix normalization, and add any
music as a separate ducked stem.

## Verdict

`REJECTED`. Automated transcription, timing, loudness, and decode passes do not override human
accent, phrasing, or mix judgment.
