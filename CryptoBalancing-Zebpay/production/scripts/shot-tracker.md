# Shot tracker

All picture intervals are deterministic. No generative video jobs or provider IDs are required.
Exact frames are populated from the final narration timing.

| Shot | Target | Route | Source/asset | Pass condition | Status |
|---|---:|---|---|---|---|
| S01 Hook/drift | 0–8.669s | Deterministic | Product overview + illustrative SVG bars | Product context and labelled drift read immediately | Encoded |
| S02 Realign | 8.669–17.119s | Deterministic | Product overview + illustrative SVG bars | Overweight trim and underweight buy resolve to target | Encoded |
| S03 Research | 17.119–27.132s | Deterministic | History screen + signal callouts | Narration avoids performance promises; source UI remains authentic | Encoded; source-claim approval required |
| S04 Transparency | 27.132–36.076s | Deterministic | History and About Rebalancing | Change history, fees, and taxes are clear | Encoded |
| S05 Control | 36.076–41.637s | Deterministic | Disable and enable screens | User choice is clear | Encoded |
| S06 CTA | 41.637–46.486s | Deterministic | Enable screen | Enable CTA owns the final resolved hold | Encoded |

Transition boundaries are frame-locked at approximately 8.669, 17.119, 27.132, 36.076, and
41.637 seconds. The boundary sheet inspects the encoded `n-1`, `n`, and `n+1` frames.
