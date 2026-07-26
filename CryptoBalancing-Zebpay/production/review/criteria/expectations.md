# Review expectations

| ID | Scope | Severity | Check method | Pass condition | Status |
|---|---|---|---|---|---|
| V01-source | All screens | Blocker | Hash + visual comparison | Product UI comes from registered screenshots | Pending |
| V02-fidelity | All screens | Blocker | 360 px and full-size playback | Key UI remains crisp and recognizable | Pending |
| V03-claims | Copy and narration | Blocker | Claims-register audit | No prohibited or unsupported claim | Pending |
| V04-illustrative | Drift animation | Blocker | Frame inspection | Fictional movement is labelled “Illustrative” | Pending |
| V05-hierarchy | Every beat | Major | Full playback | One new visual idea reveals at a time | Pending |
| V06-captions | Full cut | Blocker | Muted playback | Captions are readable and not covered | Pending |
| V07-audio | Narration | Blocker | Human listen + transcript | Correct words, acceptable voice and pronunciation | Needs human |
| V08-mix | Full cut | Major | Loudness probe + listen | Speech stays intelligible; no clipping | Pending |
| V09-boundaries | Every beat | Blocker | Frames n-1, n, n+1 | No flash, blank, wrong state, or semantic lead | Pending |
| V10-cta | Final frame | Blocker | Last two seconds | Enable Rebalancing is clear and held | Pending |
| V11-technical | Encoded artifact | Blocker | FFprobe/decode | 1080×1920, 30 fps, expected frames, H.264/AAC | Pending |

Return `PASS`, `FAIL`, or `NEEDS HUMAN` with timestamped evidence. Technical success does not waive
brand, legal, regulatory, music-rights, pronunciation, or creative approval.
