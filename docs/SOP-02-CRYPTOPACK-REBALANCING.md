# SOP 02: Produce the CryptoPack Rebalancing video

This is a ZebPay in-app marketing video. It explains CryptoPack Rebalancing and drives one action:
**Enable Rebalancing.**

Complete `docs/SOP-00-SETUP.md` before you start. This SOP assumes a verified machine.

## Film specification

| Property | Value |
|---|---|
| Resolution | 1080 x 1920 |
| Frame rate | 30 fps |
| Runtime | 46.600 seconds, 1,395 decoded video frames |
| Narration | One continuous ElevenLabs performance, 6 segments |
| Current review cut | v002, SHA-256 `3B90B00BC81BF90F0EEC6F19696E8FF7A3175C5F9591F3F66CCCE8389190FA76` |
| Status | Keeper at the encoded-artifact gate. Not promoted. |
| Workspace | `CryptoBalancing-Zebpay/` |
| Source brief | `CryptoBalancing-Zebpay/Cryptopack Rebalacing In-App Marketing Video.pdf` |

This film uses **no generative video**. Every picture frame is deterministic HyperFrames output over
real ZebPay app screenshots. That makes it far cheaper and far more repeatable than the Ramayana
film. The only paid provider call is the narration.

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Environment | The setup script passes | `tools/setup-video-repo.ps1` | Operator | Required |
| Claims freeze | Every spoken and on-screen phrase is in the claims register | `docs/claims-register.md` | Producer / ZebPay | Required before narration |
| Product fidelity | Real ZebPay screenshots stay authoritative and unmodified | Asset register | Producer | Required |
| Deterministic picture | Copy, numbers, bars, and brand geometry come from HyperFrames | `npm run check` and boundary sheet | Motion | Required |
| Encoded QC | The real file passes probe, boundary, claims-scan, and mix checks | `production/review/` | Reviewer | Required |
| Human approval | A person listens, checks the UI, and approves the claim treatment | Approval record | Human | Required |
| Promotion | The owner approves the exact MP4 hash | Approval record | Human | Not approved |

## What a fresh clone can rebuild

| Element | In Git? | How you get it back |
|---|---|---|
| HyperFrames compositions, `index.html`, six frame files, captions | Yes | Nothing to do |
| App screenshots and Inter fonts | Yes | Nothing to do |
| Caption groups, audio metadata, frame plan | Yes | Nothing to do |
| Music bed | No, ignored | Regenerate exactly. It is seeded deterministic synthesis, seed `20260726`. |
| SFX | No, ignored | Regenerate exactly. Deterministic local synthesis. |
| Narration WAVs and provider master | No, ignored | One paid ElevenLabs synthesis. A new take is not byte-identical. |
| The v002 review MP4 | Yes, through Git LFS in the meeting package | `git lfs pull` |

So a clone can rebuild the picture exactly, the music and SFX exactly, and the narration only as a
fresh performance.

## Where everything lives

| Path | Contents |
|---|---|
| `docs/production-plan.md` | The 45 second delivery contract and beat map |
| `docs/claims-register.md` | Approved and prohibited claim language. Read this first. |
| `docs/scripts/01-sell-and-explain.md` | The produced script |
| `docs/scripts/02-*.md`, `03-*.md` | Documented alternates, not produced |
| `production/edit/animations/cryptopack-rebalancing/` | The HyperFrames project. This is where the picture is built. |
| `production/tools/` | Narration, music, SFX, caption, and packaging helpers |
| `production/review/` | QC records, claims scan, boundary sheets, probe JSON |
| `production/deliverables/review-cuts/` | v001 and v002 packages with delivery records |

## The claims register is the safety system

Read `CryptoBalancing-Zebpay/docs/claims-register.md` before you write or change one word.

Approved working language includes: drift from target allocation, trimming overweight coins and
buying underweight coins, realignment to the intended strategy, a research-backed process that may
update allocations or tokens, reviewable history, standard fees and applicable taxes, user control
over enabling and disabling, and the fact that rebalancing does not guarantee profit.

Prohibited or approval-required language includes: "optimal strategy", "protect your long-term
returns", "protect your portfolio", "experts continuously analyse", "boost performance", any
guarantee of profit or loss prevention, and any unlabelled fictional value.

Two lessons from v001, both real:

1. **Prohibited language can arrive inside a screenshot.** v001 was blocked because the source app
   UI carried approval-required wording that was legible on screen. The register applies to every
   readable pixel, not only to authored copy.
2. **The fix is presentation, not forgery.** v002 keeps the registered screenshots byte-identical.
   It masks or blurs the risky body copy in the composition and replaces the risky history rows with
   approved language. Control states, the illustration, and the call to action stay recognizable.
   Never edit a source screenshot to change what the product appears to say.

Any illustrative allocation movement carries a visible `Illustrative` label.

## Build the video

Work from the HyperFrames project directory.

```powershell
cd CryptoBalancing-Zebpay\production\edit\animations\cryptopack-rebalancing
```

The commands below come from the tracked tools and their recorded metadata. Run each tool with
`--help` first if you are unsure. Verify the flags before you spend anything.

### Step 1. Restore the audio. Narration is PAID

Regenerate the deterministic stems first. They cost nothing and reproduce exactly.

```powershell
python ..\..\..\tools\build_music_bed.py --project . --duration 46.486
python ..\..\..\tools\build_sfx.py --project .
```

Check the results against the recorded hashes in
`assets/audio/music/music-v001-metadata.json` and `assets/audio/sfx/sfx-v001-metadata.json`. A
matching hash proves the rebuild is exact.

Now the narration. **This calls a paid provider.** `ELEVENLABS_API_KEY` must be in the process
environment.

```powershell
node ..\..\..\tools\generate_elevenlabs_tts.mjs --project . --script SCRIPT.md
```

Recorded parameters for v001:

| Parameter | Value |
|---|---|
| Voice ID | `cgSgspJ2msm6clMCkdW9` |
| Voice name | Jessica, Playful, Bright, Warm |
| Model | `eleven_multilingual_v2` |
| Submitted characters | 741 |
| Source script | `SCRIPT.md` |

The v001 audio in the record was not synthesized twice. It was recovered from ElevenLabs history with
`recover_and_align_narration.py --project . --history-item-id <id>`. Use that path if you want the
original performance and it is still in the account history. Otherwise a new synthesis produces a new
performance, and every phrase boundary must be re-measured.

Phrase boundaries come from FFmpeg `silencedetect` at -36 dB over 0.20 s, taking the midpoint of each
paragraph silence. The recorded boundaries are 0.0, 8.669, 17.119, 27.132, 36.076, 41.637, and
46.486349 seconds. Word timing came from local `faster-whisper small.en`, and the approved copy was
kept exactly. Never let a transcript rewrite approved copy.

### Step 2. Check the composition. AGENT OK

```powershell
npm run check
```

Fix every error before you render. Review the warnings. The project pins `hyperframes@0.7.71` so it
re-renders the same way over time. Do not change the pin without a reason and a re-review.

To preview while you work, run the dev server in the background. It is a long-running process.

```powershell
npm run dev
```

### Step 3. Render. AGENT OK

```powershell
npm run render
```

The render lands in `renders/`. The v002 source render is `renders/video-v002.mp4` with SHA-256
`C9CA5CE8452EAD28189B0D09CA2C0598B1413378DBF46001BF455123777A6AF6`. Render logs are kept beside it.

Composition rules that must hold, from the project `AGENTS.md`:

- Every timed element needs `data-start`, `data-duration`, and `data-track-index`.
- Every timed element needs `class="clip"`.
- Timelines are paused and registered on `window.__timelines`.
- No `Date.now()`, no `Math.random()`, no network fetches. The render must be deterministic.

### Step 4. Package the review cut. AGENT OK

```powershell
powershell -ExecutionPolicy Bypass -File ..\..\..\tools\package_review_cut.ps1 `
  -Source renders\video-v002.mp4 `
  -Output ..\..\..\deliverables\review-cuts\cryptopack-rebalancing-v002\cryptopack-rebalancing-review-v002.mp4
```

The script encodes 1080x1920 at 30 fps, H.264 with `-preset slow` at 2400 kbps, AAC at 48 kHz and
160 kbps, `loudnorm I=-16 TP=-1.5 LRA=11`, and `+faststart`. It then probes the output, hashes it,
and writes a JSON report marked `review-cut-not-promoted`. That status is deliberate.

Build the caption sidecar:

```powershell
python ..\..\..\tools\build_srt.py --groups caption_groups.json --out ..\..\..\deliverables\review-cuts\cryptopack-rebalancing-v002\cryptopack-rebalancing-review-v002.srt
```

### Step 5. Review the encoded file. AGENT OK, human on taste

Judge the encoded artifact, never the timeline. The v002 review used eleven requirements. Reuse them.

| ID | Requirement | How to check |
|---|---|---|
| V01 | Source integrity | Registered screenshots and render copies stay byte-identical |
| V02 | Fidelity | Product screens read clearly at 360 px and at full size |
| V03 | Claims | No prohibited wording is audience-legible in any frame |
| V04 | Illustrative | Allocation movement keeps its visible label |
| V05 | Hierarchy | The focused row matches the narration at that moment |
| V06 | Captions | Readable, unobstructed, safe area, timing conformed to speech |
| V07 | Narration | Complete transcript. Tone and pronunciation need a human. |
| V08 | Mix | Measure LUFS, LRA, and true peak. v002 measured -16.36, 2.00, -1.46. |
| V09 | Boundaries | Inspect `n-1`, `n`, `n+1` at every deterministic boundary |
| V10 | Call to action | The enable button stays sharp and unobstructed to the last frame |
| V11 | Technical | Codecs, dimensions, frame rate, frame count, clean full decode |

The recorded v002 boundary frames are 260, 514, 814, 1082, and 1249.

A note on V07. Local ASR renders "ZebPay's" as "ZEPE's". That is not proof of bad pronunciation, and
it is not proof of good pronunciation either. It only blocks a machine-only pass. A person must
listen.

Write the verdict into `production/review/`, next to the existing v001 and v002 records.

### Step 6. Promote. HUMAN ONLY

The video is not final until a person does all of this:

1. Listens to the exact encode with sound at phone scale. Judge voice tone, "Zeb-pay", "Crypto
   Pack", and the music and SFX balance.
2. Confirms the registered screenshots show current product UI.
3. Approves the deterministic claim masking and replacement treatment for campaign use.
4. Obtains product, legal, regulatory, and brand approval.
5. Explicitly promotes the exact MP4 hash to `deliverables/final/`.

Review media stays ignored by Git. A video enters Git LFS only when the owner asks for that exact
file. Follow `.agent-harness/recipes/git-lfs-video-delivery.md`.

## Current status

| Gate | Status |
|---|---|
| Encoded-artifact review | KEEPER. No blocker remains in v002. |
| v001 | Blocked by its claims review. Preserved as evidence. |
| Human listening | Pending |
| Screenshot currency and claim-treatment approval | Pending |
| Product, brand, legal, regulatory approval | Pending |
| Promotion to final | Not requested |

## Skills to use

| Task | Skill |
|---|---|
| Whole workflow | `script-video-production` |
| Composition and rendering | `hyperframes`, `hyperframes-core`, `hyperframes-cli` |
| Deterministic graphics craft | `script-video-motion-graphics` |
| Assembly, mix, captions, mastering | `script-video-post` |
| Encoded review | `script-video-review` |
| Recording new evidence | `/learn` |

Follow `.agent-harness/recipes/hyperframes-motion-graphics.md` for HyperFrames work.

## Do not do this

- Do not edit a source screenshot to change what the product appears to say. Mask or replace in the
  composition instead.
- Do not invent product UI, a transaction, a fee, or a feature behavior with an image generator.
- Do not let an image model produce authoritative product screens.
- Do not add a claim that is missing from the register, even if it sounds harmless.
- Do not change the pinned HyperFrames version without a re-review.
- Do not call a technically clean encode a final.
