# ElevenLabs v007 surgical SIP repair fallback

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Fault isolation | Only the rejected middle G12 SIP phrase is replaced | Frame range 1116-1228 and v007 word boundaries | Audio editor | Pass |
| Corrected initials | Replacement duration is consistent with distinct initials | Selected Scribe span 1.299 s | Audio QC | Pass; human listening required |
| Pitch safety | Patch is conformed without pitch shift | Rubber Band 1.015446x | Audio editor | Pass |
| Master safety | v006 and approved v005 assets remain unchanged | New v007 local artifacts | Editor | Pass |
| Promotion | Complete encoded cut is approved by a human | Not rendered after local route was selected | Human | Not selected |

Two patch candidates were generated for the G12 sentence. The selected candidate used
`S. I. P.` punctuation, then received a 49 ms leading trim, 1.015446x pitch-preserving tempo,
-1 dB gain, and 30 ms boundary fades to occupy the exact 3.733333-second G12 slot.

The sample-exact repaired narration is kept locally as
`edit/audio/elevenlabs-v007/narration-phrase-locked-v004-sip-repaired.wav`; its word timing is
`edit/audio/elevenlabs-v007/narration-word-boundaries-v004-sip-repaired.json`.

This remains a fallback only. The v008 local-Qwen route replaces the complete performance and has
its own encoded review. Neither v007 nor v008 may replace the approved v005 final without human
listening approval.
