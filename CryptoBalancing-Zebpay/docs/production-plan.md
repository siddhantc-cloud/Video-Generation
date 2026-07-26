# CryptoPack Rebalancing — production plan

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Three scripts | Sell-and-explain, walkthrough, and conversion scripts are preserved | `scripts/` | Producer | Complete |
| Primary cut | Sell-and-explain version is rendered at approximately 45 seconds | 46.6 s review cut | Producer | Complete |
| Product fidelity | Real ZebPay screenshots remain authoritative | Asset register and encoded midpoint sheet | Producer | Complete |
| Claims safety | Newly authored copy avoids guaranteed returns, “optimal strategy,” and unsupported continuous-monitoring language | `claims-register.md` and QC report | Producer / ZebPay | Authored copy passes; source-UI approval required |
| Mobile delivery | 1080×1920 at 30 fps with readable captions and compatible audio | QC report | Producer | Complete |
| Human promotion | The owner explicitly approves a review cut before it is called final | Approval record | Owner | Required |

## Delivery contract

- Audience: ZebPay CryptoPack users who encounter rebalancing while using the mobile app.
- Message: market movements can shift a CryptoPack away from its target allocation; rebalancing
  brings it back in line while keeping changes transparent and controllable.
- Primary goal: sell and explain, then drive **Enable Rebalancing**.
- Primary placement: MoEngage mobile in-app video with a CTA.
- Runtime: approximately 45 seconds.
- Canvas: 1080×1920 portrait at 30 fps.
- Language: neutral international English.
- Tone: playful, enthusiastic, clear, and trustworthy.
- Narration: one continuous female ElevenLabs performance if the configured account and requested
  voice are available; otherwise stop at the narration gate rather than silently changing provider.
- Music: restrained, rights-cleared, light playful technology bed with small UI accents.
- Captions: burned in last and readable with audio muted.

## Primary beat map

| Beat | Target interval | Story function | Visual owner |
|---|---:|---|---|
| Hook | 00:00–00:06 | Markets move; a pack can drift | Product screen plus kinetic allocation motif |
| Drift | 00:06–00:15 | Show target allocation becoming uneven | Deterministic bars and clearly marked illustrative values |
| Realign | 00:15–00:24 | Explain automatic trimming and buying | Bars return to the target allocation |
| Research | 00:24–00:32 | Explain possible allocation/token updates without promising returns | History screen and research-signal callouts |
| Transparency | 00:32–00:39 | Show history, standard fees, and applicable taxes | Rebalancing History screen |
| Control and CTA | 00:39–00:45 | Establish choice and finish on enable | Disable sheet glimpse, then Enable Rebalancing sheet |

The final phrase map is derived from the narration word timings and snapped to integer frames.
Narration owns the clock; the target intervals above may move by a few frames.

## Production routing

- HyperFrames owns all deterministic UI staging, exact copy, numbers, allocation bars, callouts,
  transitions, and brand geometry.
- video-use plus FFmpeg/FFprobe owns conform, assembly, mix, captions, encoded-artifact review,
  probes, and hashes.
- The four unique images embedded in the PDF are the approved baseline. Fresh app PNGs may replace
  them before picture lock if the owner supplies them.
- Image generation is optional and deferred. It may create decorative background material or a
  separately reviewed restoration candidate, but it must never invent authoritative product UI,
  transactions, fees, or feature behavior.

## Approval and delivery gates

1. Script and claims are frozen before narration.
2. The full screenshot-led animatic is encoded before final polish.
3. Any provider cost is quoted immediately before use.
4. The actual encoded review cut is checked at all deterministic boundaries and watched at phone
   scale with sound.
5. Brand, legal, regulatory, pronunciation, music-rights, and creative approval remain human
   gates.
6. Review media remains ignored by Git. A video enters Git LFS only after the owner explicitly asks
   to promote that exact file.
