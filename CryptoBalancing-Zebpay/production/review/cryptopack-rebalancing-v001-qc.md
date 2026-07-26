# CryptoPack Rebalancing v001 — encoded review QC

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Exact artifact | Review refers to one hashed MP4 | Probe JSON and SHA-256 | Reviewer | Pass |
| Mobile picture | 1080×1920, 30 fps, H.264, yuv420p | FFprobe | Reviewer | Pass |
| Mobile audio | Stereo AAC at 48 kHz; intelligible full-mix transcript | FFprobe and local ASR | Reviewer | Pass |
| Loudness | Approximately −16 LUFS with true peak below −1 dBTP | FFmpeg loudnorm measurement | Reviewer | Pass |
| Visual continuity | No black, frozen, or broken transition frames | Detectors and boundary sheet | Reviewer | Pass |
| Captions | 107 approved words remain inside the lower safe band | Caption metadata and midpoint sheet | Reviewer | Pass |
| Product truth | Four PDF-extracted UI images remain authoritative | Asset register and midpoint sheet | Reviewer | Pass |
| Promotion | Human brand, legal, pronunciation, and creative approval is recorded | Approval record | Owner / ZebPay | Pending |

## Artifact

- File: `deliverables/review-cuts/cryptopack-rebalancing-v001/cryptopack-rebalancing-review-v001.mp4`
- Status: review cut; not promoted final.
- SHA-256: `80234699B8F4BB199F3CA967D75175F593B474FCBE8FC2677D8BAFC873ACAEC8`
- Duration: 46.600 seconds.
- Size: 12,264,909 bytes.
- Video: H.264, 1080×1920, 30/1 fps, yuv420p.
- Audio: AAC, stereo, 48 kHz.
- Integrated loudness: −16.36 LUFS.
- True peak: −1.46 dBTP.

## Deterministic checks

- Black detection: no interval at least 0.15 seconds.
- Full-mix silence detection: no interval at least 0.50 seconds below −45 dB.
- Freeze detection: no interval at least 0.75 seconds.
- HyperFrames transition verifier: five cross-track transitions pass with positive overlap and no
  same-track overlap.
- HyperFrames final check: zero runtime, layout-warning, motion, or contrast errors. Eleven layout
  informational messages describe intentional clipped camera/shine movement and the CTA image crop.
- Encoded midpoint sheet:
  `review/cryptopack-rebalancing-v001-encoded-midpoints.png`.
- Encoded `n-1`/`n`/`n+1` transition sheet:
  `review/cryptopack-rebalancing-v001-boundaries.png`.

## Audio and language evidence

The six isolated phrase WAVs transcribe to the approved lines. The rendered full mix also
transcribes to the approved meaning with language probability 1.0. The unprompted local model
renders the brand possessive as “ZEPE’s,” so a human should listen specifically for the intended
“Zeb-pay’s” pronunciation. This ASR result is a review flag, not conclusive evidence of a defect;
no second paid synthesis was authorized.

## Claims and human gates

New narration and authored overlays stay inside `docs/claims-register.md`: they do not promise
returns, profit, performance, or loss prevention. The authentic UI images supplied inside the
source PDF visibly contain stronger product language, including references to long-term returns,
performance, and portfolio protection. Those strings were not newly authored or altered in this
cut, but they are visible marketing claims and require ZebPay product/legal confirmation.

Superseding verdict: **blocked by the independent encoded review**. The registered screenshots are
authentic, but their audience-visible claim wording conflicts with the working claims register.
The v001 artifact remains immutable review evidence and must not be promoted. See v002 for the
claims-safe and caption-timing revision.
