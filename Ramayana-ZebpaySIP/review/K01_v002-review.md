# K01 v002 review

## Keeper checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Correct opening state | The approved Rama/bridge construction state is present from frame 0 | `qc-frames/K01_v002_first.png`; Rama, bridge line, island, sea, and dawn are present | Director/Operator | Pass with generative recomposition |
| Continuous shot | One coherent move without an internal cut or unrelated scene | `frames/K01_v002_2fps_contact.png`; no scene activity above the 0.28 threshold | Director/Operator | Pass |
| Approved visual content | Rama remains a calm witness and the move reveals the bridge workforce | Contact sheet and last frame | Director/Operator | Pass |
| Identity and anatomy | Rama, bow, workforce, bridge, and island remain usable throughout the selected duration | 2 fps contact sheet | Director/Operator | Pass |
| Technical validity | Decodable video and native audio exist for the requested duration | FFprobe: H.264 496x864/24 fps, stereo AAC, 6.060 s | Operator | Pass |
| Native SFX presence | Audio is present and not materially silent | Extracted WAV; mean -25.6 dB, peak -11.6 dB; no >0.35 s silence detected | Audio/Operator | Pass |
| Spend evidence | One job and one matching account charge exist | Job `b503b2d0-c3c6-478f-88ba-ef4cd4b1e3bd`; transaction -18 credits | Producer | Pass |
| Keeper gate | Every mandatory editorial criterion passes | This review | Director/Operator | Keeper |

## Verdict

**Keeper for the v004 edit.**

The explicit `start_image` role fixes the structural failure seen in v001. The clip opens in the
approved story state, holds one continuous camera move, and reveals active bridge construction as
Rama leaves frame. The native surf, wind, and stone ambience is usable underneath separate
narration.

`start_image` is an image-conditioning control, not a literal first-frame lock in this result. The
generated first frame semantically preserves the approved composition but changes the sun position,
Rama scale, bridge population, and color temperature; its first-frame SSIM against the conformed
keyframe is 0.286. This is acceptable for this experimental edit because continuity of story,
identity, direction, and motion passes. It must not be cited as evidence of pixel-locked keyframe
adherence.

## Evidence

- Raw take: `../footage/generated/K01_v002_seedance20_480p_sound.mp4`
- Native audio: `../audio/sfx/generated/K01_v002_native.wav`
- Contact sheet: `frames/K01_v002_2fps_contact.png`
- First frame: `qc-frames/K01_v002_first.png`
- Last frame: `qc-frames/K01_v002_last.png`
- Raw SHA-256: `11010BBBA940D15495CDC5BE88F6021400B3D8537D87EA9271661A96D1509CFF`
- Native WAV SHA-256: `556018BE75EE454BF48B87DBEEA240320774A463A9D46D240D62F0B2A59169BF`
