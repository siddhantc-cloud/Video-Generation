# CryptoPack Rebalancing v002 — encoded review QC

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Exact artifact | Review refers to one hashed MP4 | Probe JSON and SHA-256 | Reviewer | Pass |
| Mobile picture | 1080×1920, 30 fps, H.264, yuv420p | FFprobe | Reviewer | Pass |
| Mobile audio | Stereo AAC at 48 kHz | FFprobe | Reviewer | Pass |
| Loudness | Approximately −16 LUFS and true peak below −1 dBTP | FFmpeg loudnorm measurement | Reviewer | Pass |
| Claims | Restricted source-UI wording is not audience-legible | Claims scan and midpoint sheet | Reviewer | Pass |
| Captions | Phrase-reset highlights start with encoded speech | ASR onsets and caption metadata | Reviewer | Pass |
| Boundaries | No flash, blank, or wrong state at `n-1`, `n`, `n+1` | Boundary sheet | Reviewer | Pass |
| Promotion | Human brand, pronunciation, creative, and product approval is recorded | Approval record | Owner / ZebPay | Pending |

## Artifact

- File:
  `deliverables/review-cuts/cryptopack-rebalancing-v002/cryptopack-rebalancing-review-v002.mp4`.
- Status: technical keeper as a review cut; not promoted final.
- SHA-256: `3B90B00BC81BF90F0EEC6F19696E8FF7A3175C5F9591F3F66CCCE8389190FA76`.
- Duration: 46.600 seconds; 1,395 decoded video frames.
- Size: 12,263,458 bytes.
- Video: H.264, 1080×1920, 30/1 fps, yuv420p.
- Audio: AAC, stereo, 48 kHz.
- Integrated loudness: −16.36 LUFS.
- True peak: −1.46 dBTP.

## v001 blocker resolution

- The research/update scene replaces the two unsafe source rows with the approved working
  language `Research-backed process` and `Allocations or tokens may update`.
- The history scene uses the same safe replacement while retaining the real history rows and
  standard fees/taxes disclosure.
- The enable/disable comparison de-emphasizes screenshot copy but preserves recognizable states.
- The final enable sheet de-emphasizes body copy while keeping the authentic
  `ENABLE REBALANCING` control crisp.
- The v001 focus mismatch is resolved: the 19.5-second focus now matches the spoken allocation/token
  update idea.
- Phrase-reset caption starts now equal the encoded speech onsets:
  9.320, 17.820, 27.420, 36.420, and 42.100 seconds.

## Deterministic checks

- HyperFrames check: zero runtime, layout-warning, motion, or contrast errors. Remaining layout
  informational messages describe intentional clipped camera, shimmer, and CTA-crop behavior.
- Black detection: no interval at least 0.15 seconds.
- Full-mix silence detection: no interval at least 0.50 seconds below −45 dB.
- Freeze detection flags designed reading holds at 5.800–8.300, 29.533–32.533, 34.933–35.900,
  and the final CTA hold after 45.667 seconds. Visual inspection confirms valid held states rather
  than a stalled or corrupted render.
- Encoded midpoint sheet:
  `review/cryptopack-rebalancing-v002-encoded-midpoints.png`.
- Encoded `n-1`/`n`/`n+1` transition sheet:
  `review/cryptopack-rebalancing-v002-boundaries.png`.
- Encoded claims scan:
  `review/cryptopack-rebalancing-v002-claims-scan.png`.

## Human approval items

1. Listen to the exact encoded MP4 for the intended “Zeb-pay’s” and “Crypto Pack” pronunciations
   and approve the playful Jessica voice.
2. Confirm that the registered PDF-extracted screens are still the correct current product UI.
3. Approve the creative pacing, original music balance, and v002 claims treatment at phone scale.
4. Promote only this exact hash, or create a new version if anything changes.

Technical verdict: **keeper as a review cut**. Final promotion remains a human decision.
