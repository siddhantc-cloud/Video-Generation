# CryptoPack Rebalancing review package v001 — blocked

## Checklist

| Item | Pass condition | Evidence | Status |
|---|---|---|---|
| Review MP4 | Probed, hashed, playable mobile encode | QC report | Included locally |
| Captions | Exact sidecar for accessibility/review | SRT | Included |
| Contact sheet | Six story midpoints plus final hold | JPG | Included |
| Promotion | Owner approves the exact MP4 hash | Independent encoded review | Blocked; superseded by v002 |

## Package

| File | Purpose | SHA-256 |
|---|---|---|
| `cryptopack-rebalancing-review-v001.mp4` | 1080×1920 H.264/AAC review cut | `80234699B8F4BB199F3CA967D75175F593B474FCBE8FC2677D8BAFC873ACAEC8` |
| `cryptopack-rebalancing-v001.srt` | Exact 41-group English caption sidecar | `A66DCD1194396837E0E18D8B7D927EB0775E47DA27F75DB63A0A31C302D3B373` |
| `cryptopack-rebalancing-v001-contact-sheet.jpg` | Visual review sheet | `5979ABD35314DA7F98E3CEF63CA47A1E3FEB9736F0D9E8802A3962A04FCBC86C` |

The MP4 is intentionally ignored by Git and has not been promoted to `deliverables/final/`. The
source HyperFrames master remains at
`edit/animations/cryptopack-rebalancing/renders/video.mp4` with SHA-256
`4311BFA05B6DD3CF6E3FA5C31A1C16A117BC581F9D25E5AF1D78527F9E891224`.

See `review/cryptopack-rebalancing-v001-qc.md` and the independent review before approval.

The independent encoded review found audience-visible source-UI claims that conflict with the
project claims register and five early first-word caption highlights. This package is retained as
immutable review evidence only. Do not promote or distribute it; review v002 instead.
