# Independent encoded-artifact review — CryptoPack Rebalancing v002

| Requirement | Decisive encoded evidence | Status |
|---|---|---|
| V01 — Source | Registered reference files and render copies remain byte-identical; v002 uses deterministic masks/replacement copy over those sources | PASS |
| V02 — Fidelity | Product overview/history remain crisp; the enable/disable body is deliberately blurred, but the control states and CTA remain recognizable at 360 px and full size | PASS |
| V03 — Claims | Unsafe inherited copy is no longer legible; safe replacement copy is used in the history screen | PASS |
| V04 — Illustrative | Allocation movement retains the visible “Illustrative” label | PASS |
| V05 — Hierarchy | The allocation/token row now receives focus during the matching narration | PASS |
| V06 — Captions | Burned captions are readable, unobstructed, safe, and active-word timing is conformed to speech | PASS |
| V07 — Narration | Encoded transcript is complete; voice tone and brand pronunciation still require human listening | NEEDS HUMAN |
| V08 — Mix | −16.36 LUFS-I, 2.00 LU LRA, −1.46 dBTP; no clipping or decode fault | PASS technically |
| V09 — Boundaries | Frames around 260, 514, 814, 1082, and 1249 contain valid adjacent states with no flash or blank | PASS |
| V10 — CTA | Sharp “ENABLE REBALANCING” button is held through frame 1394 | PASS |
| V11 — Technical | H.264/AAC, 1080×1920, 30 fps, 1,395 decoded video frames, clean full decode | PASS |

## Verdict

**KEEPER at the encoded-artifact gate.**

No blocker remains in v002. The v001 B01, M01, and M02 findings are resolved in the exact encoded
file. This is still a review cut, not a promoted final; human voice, product, legal/regulatory,
brand, creative, and explicit promotion approvals remain separate gates.

Artifact reviewed:

- File: `../deliverables/review-cuts/cryptopack-rebalancing-v002/cryptopack-rebalancing-review-v002.mp4`
- SHA-256: `3B90B00BC81BF90F0EEC6F19696E8FF7A3175C5F9591F3F66CCCE8389190FA76`
- Hash result: exact match to the requested hash and `cryptopack-rebalancing-v002-probe.json`
- Video: H.264 High, yuv420p, 1080×1920, 30/1 fps, 1,395 frames, 46.500 s
- Audio: AAC-LC stereo, 48 kHz, 46.600 s
- Container: 46.600 s, 12,263,458 bytes
- Decode: all video and audio frames decoded without error

## v001 regression closure

### B01 — Source-inherited unsafe claims: resolved

The exact encoded claim scan and independently extracted frames show:

- At 00:17.500–00:27.132, the unsafe history-screen rows have been replaced or covered with
  “Research-backed process” and “Allocations or tokens may update.” The remaining readable rows
  state that the Pack is realigned to its original allocation and that standard fees and applicable
  taxes apply. These are within the approved working language.
- At 00:36.076–00:46.500, the unsafe body copy inside the enable/disable screenshots is
  deliberately blurred. The product-screen silhouette, control states, illustration, and action
  buttons remain recognizable; prohibited “boost performance,” return-support, portfolio-
  protection, and “signals for results” language is not legible.
- At full size and 360 px, no newly authored or source-inherited prohibited claim is audience-
  readable in the inspected encoded frames.

Evidence:

- `cryptopack-rebalancing-v002-claims-scan.png`
- `cryptopack-rebalancing-v002-encoded-midpoints.png`
- Exact encoded frames at 00:17.500, 00:19.500, 00:20.000, 00:21.000, 00:22.500,
  00:35.900, 00:38.500, 00:43.500, and 00:46.467
- `../../docs/claims-register.md`

The original source images remain registered and unmodified. Their render-copy hashes still match
the references exactly: `5908C66…12582`, `04E6AD66…042097`, `16B5A012…C563`, and
`F6630EAF…98586`. The v002 claim treatment is deterministic presentation over those sources.

### M01 — Mismatched row emphasis: resolved

At 00:19.900–00:23.560, while narration says the process may update allocations or tokens as market
conditions change, the highlighted row reads “Allocations or tokens may update.” The preceding
return-related row from v001 is neither focused nor legible. Visual hierarchy and narration now
carry the same idea.

### M02 — Early first-word karaoke highlights: resolved

Exact encoded-audio ASR onsets were compared with the first frame carrying the blue active-word
highlight:

| First word | Encoded speech onset | First highlighted frame | Offset |
|---|---:|---:|---:|
| CryptoPack | 00:09.320 | frame 280 / 00:09.333 | +0.013 s |
| ZebPay’s | 00:17.820 | frame 535 / 00:17.833 | +0.013 s |
| And | 00:27.420 | frame 823 / 00:27.433 | +0.013 s |
| You | 00:36.420 | frame 1093 / 00:36.433 | +0.013 s |
| Keep | 00:42.100 | frame 1264 / 00:42.133 | +0.033 s |

No active first-word highlight appears during the preceding paragraph silence. The offsets are at
or within one 30 fps display frame after the measured speech onset. The final “Enable” caption also
appears after, rather than before, its measured onset.

## Other material passes

- **Story and hierarchy:** The sequence still reads clearly as market movement → allocation drift
  → realignment → research-backed updates → transparent history → user control → enable CTA.
- **Phone-scale readability:** Captions, headings, allocation panels, history rows, enable/disable
  labels, and final button remain readable at 360×640. The blur is confined to source UI body copy
  that cannot pass the working claims register.
- **Boundaries:** `cryptopack-rebalancing-v002-boundaries.png` and independent checks of
  `n-1`, `n`, and `n+1` around frames 260, 514, 814, 1082, and 1249 show no blank, flash, corrupted
  frame, or wrong semantic state.
- **Audio:** Full-stream local ASR recovers the approved narration. It again renders “ZebPay’s” as
  “ZEPE’s”; that is not proof of a bad pronunciation, but it prevents a machine-only V07 pass.
  Loudness and true peak are unchanged from the technically clean v001 mix.
- **Final CTA:** The enable sheet is established before the last spoken sentence. The
  “ENABLE REBALANCING” button stays sharp and unobstructed from at least 00:43.500 through the final
  decoded frame at 00:46.467; the final caption remains inside the safe area.

## Human approval items before promotion

1. Listen to the exact v002 encode for “Zeb-pay,” “Crypto Pack,” voice tone, music/SFX balance, and
   overall creative pacing.
2. Confirm the registered screenshots are current product UI and approve the deterministic claim
   masking/replacement treatment for campaign use.
3. Obtain final product, legal/regulatory, and brand approval for the complete cut.
4. Explicitly promote the approved review file; this report does not promote or rename it.
