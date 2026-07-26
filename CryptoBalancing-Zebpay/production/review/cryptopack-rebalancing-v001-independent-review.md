# Independent encoded-artifact review — CryptoPack Rebalancing v001

| Requirement | Pass condition | Evidence | Status |
|---|---|---|---|
| V01 — Source | Product UI comes from registered screenshots | Registered reference and render-copy hashes; encoded frames at 00:02.000, 00:17.500, 00:38.500, and 00:44.900 | PASS |
| V02 — Fidelity | Key UI is crisp and recognizable at full size and 360 px | Exact encoded 360×640 extractions and `cryptopack-rebalancing-v001-encoded-midpoints.png` | PASS |
| V03 — Claims | No prohibited or unsupported claim is audience-visible | Encoded frames 00:17.500–00:23.500 and 00:42.250–00:46.467; `../../docs/claims-register.md` | **FAIL — BLOCKER** |
| V04 — Illustrative | Fictional allocation movement is labelled “Illustrative” | Encoded frames 00:00.000–00:17.119 | PASS |
| V05 — Hierarchy | One new visual idea reveals at a time and supports the spoken idea | Full-timeline encoded sampling; 00:19.500–00:22.700 | REVISE — MAJOR |
| V06 — Captions | Captions are readable and not covered | 360 px encoded sampling across all six beats | PASS for readability; timing revision noted below |
| V07 — Narration | Correct words, acceptable voice, and approved pronunciation | Exact encoded-audio ASR; human listening still required | NEEDS HUMAN |
| V08 — Mix | Speech stays intelligible and the mix does not clip | Exact encoded audio: −16.36 LUFS-I, 2.00 LU LRA, −1.46 dBTP; full-stream ASR | PASS technically |
| V09 — Boundaries | No flash, blank, wrong state, or semantic lead at `n-1`, `n`, `n+1` | Frames around 260, 514, 814, 1082, and 1249; `cryptopack-rebalancing-v001-boundaries.png` | PASS |
| V10 — CTA | “Enable Rebalancing” is clear and held in the final two seconds | Encoded frames 00:43.500–00:46.467 | PASS |
| V11 — Technical | 1080×1920, 30 fps, expected frames, H.264/AAC, clean decode | Independent FFprobe/decode and `cryptopack-rebalancing-v001-probe.json` | PASS |

## Verdict

**BLOCK — not a keeper and not eligible for promotion.**

The encoded review cut is technically sound, visually coherent, readable at phone scale, and clear
about the product flow. It fails the pre-existing blocker-level claims criterion because
source-inherited product UI exposes prohibited or approval-required language. The newly authored
narration, captions, headings, and callouts do **not** introduce a prohibited claim; the failure is
inside the registered screenshot layer.

Artifact reviewed:

- File: `../deliverables/review-cuts/cryptopack-rebalancing-v001/cryptopack-rebalancing-review-v001.mp4`
- SHA-256: `80234699B8F4BB199F3CA967D75175F593B474FCBE8FC2677D8BAFC873ACAEC8`
- Status: review cut, not promoted
- Video: H.264 High, 1080×1920, yuv420p, 30/1 fps, 1,395 decoded frames, 46.500 s
- Audio: AAC-LC stereo, 48 kHz, 46.600 s
- Container duration: 46.600 s
- Full decode: no video or audio decode errors

## Blocking defect

### B01 — Source-inherited UI claims violate V03

Severity: **Blocker**

- At 00:17.500–00:23.500, the full-screen registered history UI visibly contains:
  - “Uses research-backed insights to manage risk and support long-term returns.”
  - “We may update allocation and tokens based on trends to boost overall performance.”
- At approximately 00:19.500–00:22.700, the treatment dims the rest of the UI and emphasizes the
  first of those lines, making the return-related statement more prominent.
- At 00:42.250–00:46.467, the registered enable UI visibly contains:
  - “Stay aligned with market shifts & protect your portfolio.”
  - “Uses research-backed signals for results.”
  - The dimmed “About Rebalancing” panel also retains the performance language.
- `../../docs/claims-register.md` explicitly prohibits “boost performance” language and requires
  legal/product approval for “protect your portfolio.” The other return/result formulations are
  outside the approved working-language list and are not supported by a disclaimer in this cut.

These phrases are inherited from the authoritative UI screenshots, not authored by this video.
That provenance is confirmed by `../project/asset-register.md`: all four render assets are
byte-identical to their registered references. Provenance satisfies V01 but does not satisfy V03;
the viewer still sees the claims, and the video sometimes directs attention to them.

Smallest useful next action: crop, mask, or replace the risky screenshot copy while preserving the
recognizable UI. If the owner wants the phrases retained, record explicit product/legal/regulatory
approval and formally supersede the current claims-register restriction before re-review. The
currently prohibited “boost overall performance” line cannot pass under the existing register.

## Major revision findings

### M01 — The highlighted UI row does not match the spoken update-allocation idea

At 00:19.500–00:22.700, narration and captions discuss updating allocations or tokens as market
conditions change, but the visual focus remains on the preceding “manage risk and support
long-term returns” row. This weakens one-idea-at-a-time hierarchy and amplifies the riskiest
source-inherited claim. Move the focus to the allocation/token row or remove the row emphasis.

### M02 — Karaoke first-word highlights lead speech at phrase resets

Exact encoded-audio ASR compared with the burned caption timing shows the active first word
starting early after several paragraph silences:

| Phrase | Caption highlight starts | Encoded speech starts | Lead |
|---|---:|---:|---:|
| “CryptoPack…” | 00:08.669 | 00:09.320 | 0.651 s |
| “ZebPay’s…” | 00:17.119 | 00:17.820 | 0.701 s |
| “And…” | 00:27.132 | 00:27.420 | 0.288 s |
| “You…” | 00:36.076 | 00:36.420 | 0.344 s |
| “Keep…” | 00:41.637 | 00:42.100 | 0.463 s |

The caption groups remain readable, inside safe margins, and unobstructed, so V06’s stated
readability condition passes. The active-word timing should nevertheless be conformed to the real
speech onsets before promotion.

## Material passes

- **Story clarity:** The encoded sequence communicates market movement → allocation drift →
  automatic realignment → research/update context → transparent history → user control → enable
  CTA. The deterministic screens remain recognizable and the overall progression is easy to
  follow.
- **Product source and fidelity:** Registered reference hashes match the render copies exactly:
  `5908C66…12582`, `04E6AD66…042097`, `16B5A012…C563`, and `F6630EAF…98586`.
  No invented app screen or visibly malformed product UI was found in the encoded cut.
- **Illustrative handling:** The allocation target-band and realignment graphics carry a visible
  “Illustrative” label throughout the fictional movement.
- **Captions:** At 360×640, captions are high-contrast, large enough to read, clear of UI controls,
  and not clipped. The special copy and CTA render correctly.
- **Transitions and boundaries:** Inspected `n-1`, `n`, and `n+1` frames around the five phrase
  boundaries. Crossfades contain valid adjacent states; no black/white flash, blank frame, wrong
  screen, or one-frame corruption was found.
- **Audio presence and mix:** Narration, music, and designed accents are present across the encoded
  program. Integrated loudness is −16.36 LUFS with −1.46 dBTP; no clipping or corrupt audio frame
  was detected. Encoded-audio ASR recovers the approved narration except that “ZebPay’s” is heard
  by the recognizer as “ZEPE’s,” which requires a human pronunciation decision rather than a
  machine pass.
- **Final hold:** The enable sheet and its “ENABLE REBALANCING” button are established before the
  final spoken CTA and remain clear through the last decoded frame. The final caption also remains
  inside the safe area.

## Human approval items

1. **Product/legal/regulatory/brand:** Decide whether the source-inherited return, performance,
   portfolio-protection, and “results” phrases may appear. Under the current claims register they
   do not pass.
2. **Pronunciation and voice:** Listen to the exact encoded cut for the required “Zeb-pay” and
   “Crypto Pack” pronunciations and approve or reject the voice’s tone. ASR is not sufficient
   evidence, especially because it did not recover “ZebPay’s” reliably.
3. **Current-product fidelity:** Confirm that the registered PDF-extracted screenshots are still
   the product screens approved for campaign use; hash fidelity only proves that this cut used the
   registered files.
4. **Creative and promotion:** Approve the revised encoded artifact at phone scale with sound.
   This v001 file remains a review cut and must not be treated as a promoted final.
