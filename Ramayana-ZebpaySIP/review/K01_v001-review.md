# K01 v001 review

## Keeper checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Correct opening state | Frame 0 begins on the approved K01 Rama/army construction keyframe | `qc-frames/K01_v001_first.png`; first-frame SSIM 0.214 against the approved start | Director/Operator | Fail |
| Continuous shot | No invented scene or structural transition replaces the approved opening | `frames/K01_v001_2fps_contact.png`; scene-change activity at 3.125 and 3.792 s | Director/Operator | Fail |
| Approved visual content | Rama remains a calm witness while the workforce builds the early bridge | Contact sheet: Rama/workforce appear only late in the clip | Director/Operator | Fail |
| Technical validity | Decodable video and native audio exist for the requested duration | FFprobe: H.264 496x864/24 fps, stereo AAC, 6.060 s | Operator | Pass |
| Native SFX presence | Audio is present and not materially silent | Extracted WAV; mean -25.6 dB, peak -9.4 dB; no >0.35 s silence detected | Audio/Operator | Pass, content not promoted |
| Spend evidence | One job and one matching account charge exist | Job `fe298728-3bd0-4369-a167-bf22b3379f0e`; transaction -18 credits | Producer | Pass |
| Keeper gate | Every mandatory structural criterion passes | This review | Human/Director | Reject |

## Verdict

**Reject: structural wrong-media-role failure.**

Cinema Studio attached the uploaded K01 keyframe as a generic `image` reference, not a
`start_image`. The generated clip opens on an invented, mostly empty bridge and gradually
recomposes toward the approved Rama/army image near the end. The first frame has SSIM 0.214
against the approved keyframe; the last frame rises to 0.601, confirming convergence rather than
start-frame anchoring.

This is not a stochastic reroll case. K01 v002 changes exactly one control: submit the approved
K01 keyframe through the CLI's explicit `--start-image` role. Model, prompt, character/environment
references, 9:16, 480p, six seconds, High bitrate, Sound On, and one candidate remain unchanged.

## Evidence

- Raw take: `../footage/generated/K01_v001_seedance20_480p_sound.mp4`
- Native audio: `../audio/sfx/generated/K01_v001_native.wav`
- Contact sheet: `frames/K01_v001_2fps_contact.png`
- First frame: `qc-frames/K01_v001_first.png`
- Last frame: `qc-frames/K01_v001_last.png`
- Raw SHA-256: `D03AF9E39208CD698FC8BDF44E167C11493BB3CAA3E5937A04D2BF43F169DBA5`
