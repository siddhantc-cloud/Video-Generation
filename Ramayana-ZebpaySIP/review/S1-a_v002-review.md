# S1-a v002 review

## Review checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| File integrity | Downloaded raw file opens and has stable checksums | `footage/generated/S1-a_v002_cinema35_1080p_sound.mp4`; SHA-256 in generation record | Operator | PASS |
| Delivery format | 9:16, 1080x1920, 24 fps, approximately 10 seconds | FFprobe: H.264, 1080x1920, 24 fps, 10.100 s | Operator | PASS |
| Rama identity | Face, crown, jewellery, skin, and attire remain recognizable and stable | Frames at 0.0, 2.5, 5.0, 7.5, and 10.0 seconds | Director/Operator | PASS |
| Content-filter integrity | The deity face is intact rather than blurred or garbled | Sampled frames and full-motion review | Director/Operator | PASS |
| Hands and bow | Hands remain natural and exactly one bow stays intact | Sampled frames and full-motion review | Director/Operator | PASS |
| Performance register | Rama remains solemn, closed-mouth, and reverent | Sampled frames and full-motion review | Director/Operator | PASS |
| Camera continuity | One slow, continuous, uninterrupted Dolly In with no second move or cut | Scene detector and `timeline_5_5-8_0.png` | Director/Operator | **FAIL at 6.375 s** |
| Native audio present | Generated clip contains a stereo native track and no long digital silence | FFprobe, extracted WAV, and silence scan | Sound/Operator | PASS |
| Native audio content | Surf, coastal wind, and cloth only; no speech or score-like material | `audio/sfx/generated/S1-a_v002_native.wav` | Human/Sound | NEEDS HUMAN LISTEN |
| Keeper gate | All blocker/major criteria pass before select promotion | This review | Director/Human | **REJECTED** |

## Evidence

- Job: `75e86d55-60de-4415-9a52-1b973498dcd9` (`cinematic_studio_video_3_5`).
- Raw: `footage/generated/S1-a_v002_cinema35_1080p_sound.mp4`.
- Native audio: `audio/sfx/generated/S1-a_v002_native.wav`.
- Frame set: `review/frames/S1-a_v002/frame_0_0.png`, `frame_2_5.png`, `frame_5_0.png`, `frame_7_5.png`, and `frame_10_0.png`.
- Full timeline: `review/frames/S1-a_v002/timeline_0-10.png`.
- Cut-region timeline: `review/frames/S1-a_v002/timeline_5_5-8_0.png`.
- Spectrogram: `review/frames/S1-a_v002/audio_spectrogram.png`.
- FFmpeg scene scan using threshold 0.08 reports one change at 6.375 seconds.
- Audio analysis: -27.73 LUFS integrated, -12.99 dBTP true peak, 6.20 LU LRA; no interval longer than 0.25 seconds below -45 dB.

## Finding

The take holds Rama's identity and high-value continuity anchors unusually well. The failure is not character drift: it is an editorial discontinuity generated inside the shot. Between the adjacent samples around 6.375 seconds, the island/background disappears and the cloud/light layout resets. That reads as a cut or reframe, so the shot cannot serve as the intended unbroken establishment.

## Verdict and next action

**REJECT / DO NOT PROMOTE.** Keep the file as model and prompt evidence. Do not overwrite the older select and do not submit another paid run without fresh human approval.

For v003, keep the start frame, Character and Location Elements, style block, optics, duration, resolution, aspect ratio, candidate count, and sound request fixed. Change only the motion wording to explicitly require one uninterrupted take with no cut, transition, reframe, angle change, or background reset. Human audition of the v002 native track is still useful for deciding whether its sound-prompt pattern should remain unchanged.
