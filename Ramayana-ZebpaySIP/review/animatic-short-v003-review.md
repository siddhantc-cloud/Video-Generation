# Short animatic v003 review

## Review checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Runtime | Finished review cut is between 55 and 58 seconds | FFprobe; generated EDL | Editor | PASS: 57.900 seconds |
| Frame lock | Video and audio durations match within one frame | `ZebPay_Squirrel_SHORT_ANIMATIC_v003_EDL.json` | Editor | PASS: 0.0 ms drift; `SYNC LOCKED` |
| Delivery shape | H.264/AAC, 1080x1920, 30 fps, stereo 48 kHz | FFprobe | Editor | PASS |
| Decode integrity | Full file decodes without FFmpeg errors | FFmpeg null decode | Editor | PASS |
| Audio headroom | Scratch narration is intelligible without clipping | EBU R128 scan | Editor | PASS: -17.0 LUFS integrated; -4.8 dBFS true peak |
| Story coverage | Purpose, contribution, mockery, recognition, persistence, SIP parallel, payoff, and CTA appear in order | v003 EDL and boundary filmstrips | Creative/Editor | PASS for review |
| SIP section | The investing parallel does not hold on an empty placeholder | Three deterministic SIP keyframes | Editor | PASS |
| CTA copy | End card contains no unapproved oldest-exchange claim and no Like/Share/Subscribe copy | Clean end-card source and ending filmstrip | Brand/Editor | PASS for review; human brand/legal approval pending |
| Source safety | The 166.633-second original animatic remains byte-preserved | Original SHA-256 comparison | Editor | PASS |
| Human verdict | Human accepts story clarity, pacing, scratch-voice pronunciation, and visual choices | Human playback | Human | PENDING |

## Verdict

**READY FOR HUMAN REVIEW.** This is the current keeper candidate for the short-form animatic. It is
not picture lock, final narration, final sound design, or authorization for paid generation.

## Version history

- **v001:** technically frame-locked, but self-review rejected the 14.5-second empty-ocean SIP
  placeholder.
- **v002:** added deterministic SIP cards, but self-review rejected the reused legacy end card because
  it still displayed the unapproved "India's oldest crypto exchange" claim and Like/Share/Subscribe.
- **v003:** retains the SIP cards and replaces the legacy card with a clean deterministic ZebPay CTA.

## Evidence

- Review cut:
  `deliverables/review-cuts/animatic-short/ZebPay_Squirrel_SHORT_ANIMATIC_v003.mp4`
- Generated EDL:
  `deliverables/review-cuts/animatic-short/ZebPay_Squirrel_SHORT_ANIMATIC_v003_EDL.json`
- Canonical EDL copy: `edit/edl/animatic-short-v003.json`
- Timeline source: `edit/timelines/animatic-short-v003.json`
- Boundary filmstrips: `edit/verify/animatic-short-v003/`
- Short script: `scripts/short-script-v001.md`
- Scratch VO mix: `audio/voiceover/animatic-short-v003-scratch-mix.wav`
- Scratch VO lines: `audio/voiceover/animatic-short-v003-lines/`
- SIP-card source builder: `tools/build-short-sip-cards.ps1`
- v003 SHA-256: `3B326E0458D95C3ADD857F4D7B899398A5C0E6E55BFC2CD96F82271D45B2A1BB`
- Original long-animatic SHA-256:
  `1A299D194D42C5B0572E5B48F395226C4FE756F0CFEF5D370D88AA1D4F794DF1`

## Human review questions

1. Does the story remain emotionally clear at 57.9 seconds?
2. Is one mockery beat enough, or does it need a little more reaction time?
3. Does Rama's recognition land without showing the risky pickup endpoint?
4. Are the three SIP cards clear and on screen long enough?
5. Is the direct ZebPay CTA appropriate, subject to brand/legal review?
