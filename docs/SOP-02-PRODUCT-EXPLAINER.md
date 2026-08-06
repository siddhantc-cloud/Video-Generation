# SOP 02: Produce a deterministic product explainer video

Use this SOP to make **a new video in this category**, not only to reproduce the one that exists.

**Category B: the product explainer.** A short marketing video that explains a real product feature
using the real product interface. Every pixel is deterministic. No generative video model touches the
picture. Examples: an in-app feature announcement, an onboarding explainer, a settings walkthrough, a
pricing or fee explainer, a compliance-sensitive finance or health feature.

The reference case is the **ZebPay CryptoPack Rebalancing** video in `CryptoBalancing-Zebpay/`. Every
rule below has evidence in that workspace.

Complete `docs/SOP-00-SETUP.md` first. Use `docs/SOP-01-STORY-FILM.md` instead when the value is
emotion, character, or atmosphere.

## Yes, this category is effectively free

You asked whether this one only needs Claude, Codex, or Cursor. Almost. Here is the exact bill.

| Item | Cost | Why |
|---|---|---|
| The agent (Claude Code, Codex, or Cursor) | Your existing subscription | It does the work |
| Picture: HyperFrames compositions and local render | **Free** | Headless Chromium renders locally. No cloud render needed. |
| Screenshots and brand assets | **Free** | Supplied by the product team |
| Fonts | **Free** | The reference uses Inter under the SIL Open Font License |
| Music bed | **Free** | Seeded deterministic local synthesis, `production/tools/build_music_bed.py` |
| Sound effects | **Free** | Deterministic local synthesis, `production/tools/build_sfx.py` |
| Captions and SRT | **Free** | Derived from the narration timing |
| Encode, probe, hash, QC | **Free** | FFmpeg and FFprobe, local |
| **Narration** | **The only paid item** | ElevenLabs, 741 characters for the 46.6 second reference film |

So the marginal cost of a new video in this category is one small text-to-speech call. The reference
narration fits inside a normal monthly ElevenLabs allowance.

**You can make it completely free.** Use the Edge TTS helper that the story-film animatic uses. It
needs no API key.

```powershell
python Ramayana-ZebpaySIP\tools\edge_tts_word_timed.py `
  --text-file SCRIPT.txt --audio narration.mp3 --timings word-boundaries.json `
  --voice en-IN-PrabhatNeural --rate=-4%
```

The trade is voice quality. Edge TTS is good enough for internal review and for a first cut. For a
customer-facing release, a person should listen to both and choose. That listening decision is a
human gate either way.

There is no generative video spend in this category at all. That is the point of it.

## Is this the right category?

| Choose the product explainer when | Choose the story film when |
|---|---|
| A real app or product screen is the subject | Characters, places, or performance carry the meaning |
| Every number, label, and claim must be exact | A metaphor is allowed |
| Legal or a regulator may read every frame | The audience must feel something first |
| You want a repeatable near-zero marginal cost | You can spend generation credits |
| Rebuilds must be byte-reproducible | Each take is a fresh performance |

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Delivery contract | Audience, message, single action, placement, runtime, and canvas are fixed | `docs/production-plan.md` | Producer | Required |
| Claims freeze | Every spoken and on-screen phrase is in the claims register | `docs/claims-register.md` | Producer and the product owner | Required before narration |
| Source fidelity | Real product screenshots stay authoritative and unmodified | Asset register | Producer | Required |
| Deterministic picture | Copy, numbers, bars, and brand geometry come from the renderer | `npm run check` and boundary sheet | Motion | Required |
| Encoded QC | The real file passes probe, boundary, claims-scan, and mix checks | `production/review/` | Reviewer | Required |
| Human approval | A person listens, checks the UI currency, and approves the claim treatment | Approval record | Human | Required |
| Promotion | The owner approves the exact MP4 hash | Approval record | Human | Required |

## Step 0. Create the workspace

```powershell
powershell -ExecutionPolicy Bypass -File tools/New-VideoProject.ps1 `
  -ProjectName "Your-Product-Video" -AspectRatio "9:16" -Fps 30 -Resolution "1080x1920"
```

Then create the HyperFrames project inside `production/edit/animations/<slug>/`. Follow
`.agent-harness/recipes/hyperframes-motion-graphics.md`, and enter through the `hyperframes` skill so
the router picks the right workflow.

Write the delivery contract before creative work. The reference contract is:

| Field | Reference value |
|---|---|
| Audience | ZebPay CryptoPack users who meet rebalancing inside the app |
| Message | Market moves shift a pack off its target; rebalancing brings it back, transparently and under user control |
| Single action | Enable Rebalancing |
| Placement | MoEngage in-app video with a call to action |
| Runtime | About 45 seconds |
| Canvas | 1080 x 1920 at 30 fps |
| Tone | Playful, clear, trustworthy |

## Step 1. Write the claims register. THIS IS THE SAFETY SYSTEM

Do this before the script, not after. Read
`CryptoBalancing-Zebpay/docs/claims-register.md` as the working model.

A register has two lists.

**Approved working language.** Write each sentence the video is allowed to say. The reference
approves: allocation drift from market movement, trimming overweight coins and buying underweight
ones, realignment to the intended strategy, a research-backed process that may update allocations or
tokens, reviewable history, standard fees and applicable taxes, user control over enable and disable,
and the explicit statement that rebalancing does not guarantee profit.

**Prohibited or approval-required language, with a safer replacement for each.** The reference blocks
"optimal strategy", "protect your long-term returns", "protect your portfolio", "experts continuously
analyse", "boost performance", any guarantee of profit or loss prevention, and any unlabelled
fictional value.

Then get the product and legal owners to sign the register. It controls the working cut until final
approval is recorded.

### Two lessons that cost a whole version

1. **Prohibited language can arrive inside a screenshot.** Version v001 of the reference was blocked
   because the source app UI carried approval-required wording that was legible on screen. The
   register applies to every readable pixel, not only to the copy you wrote.
2. **The fix is presentation, not forgery.** v002 keeps the registered screenshots byte-identical. It
   masks or blurs the risky body copy in the composition, and replaces risky history rows with
   approved language. Control states, the illustration, and the call to action stay recognizable.
   **Never edit a source screenshot to change what the product appears to say.**

Any illustrative movement carries a visible `Illustrative` label.

## Step 2. Write the script and the beat map. HUMAN approves

Write one continuous narration that only uses register-approved language. Then map beats to visual
owners. The reference beat map:

| Beat | Interval | Story function | Visual owner |
|---|---|---|---|
| Hook | 00:00 to 00:06 | Markets move, a pack can drift | Product screen plus allocation motif |
| Drift | 00:06 to 00:15 | Target allocation becomes uneven | Deterministic bars, marked illustrative |
| Realign | 00:15 to 00:24 | Automatic trimming and buying | Bars return to target |
| Research | 00:24 to 00:32 | Allocations or tokens may update | History screen and callouts |
| Transparency | 00:32 to 00:39 | History, standard fees, applicable taxes | Rebalancing history screen |
| Control and action | 00:39 to 00:45 | Choice, then enable | Disable sheet, then enable sheet |

Narration owns the clock. These intervals may move by a few frames once the real narration exists.

Write three script options if the direction is unsettled. The reference produced sell-and-explain,
product walkthrough, and conversion-ad versions, and produced only the first. The other two stay
documented in `docs/scripts/`.

## Step 3. Collect the real product assets. PRODUCT TEAM

Real screenshots are authoritative. Register each one with a hash and keep it unmodified in
`production/assets/references/`.

Image generation is optional and deferred. It may create decorative background material. **It must
never invent product UI, a transaction, a fee, or feature behavior.**

## Step 4. Produce the narration. THE ONLY PAID STEP

`ELEVENLABS_API_KEY` must be in the process environment. From the HyperFrames project directory:

```powershell
node ..\..\..\tools\generate_elevenlabs_tts.mjs --project . --script SCRIPT.md
```

The generator parses `## Line N (Frame N)` headings out of `SCRIPT.md`, submits one continuous
request, splits the result into per-frame segments, and writes metadata with hashes.

Reference parameters:

| Parameter | Value |
|---|---|
| Voice ID | `cgSgspJ2msm6clMCkdW9` |
| Voice name | Jessica, Playful, Bright, Warm |
| Model | `eleven_multilingual_v2` |
| Submitted characters | 741 |

Override any of them with `--voice-id`, `--voice-name`, or `--model`.

Phrase boundaries come from FFmpeg `silencedetect` at -36 dB over 0.20 s, taking the midpoint of each
paragraph silence. Word timing comes from local `faster-whisper small.en`. **The approved copy is
kept exactly. Never let a transcript rewrite approved copy.**

If a performance already exists in the provider history, recover it instead of paying twice:

```powershell
python ..\..\..\tools\recover_and_align_narration.py --project . --history-item-id <id>
```

That is how the reference v001 audio was produced. Its metadata records
`recovery_mode: history audio download; no second synthesis`.

## Step 5. Produce the free audio. AGENT OK

```powershell
python ..\..\..\tools\build_music_bed.py --project . --duration 46.486
python ..\..\..\tools\build_sfx.py --project .
```

Both are seeded deterministic local synthesis, so a rebuild is byte-identical. The reference music
seed is `20260726` at 112 BPM, 48 kHz stereo. Compare the output hashes with
`assets/audio/music/music-v001-metadata.json` and `assets/audio/sfx/sfx-v001-metadata.json`. A
matching hash proves the rebuild is exact.

Keep narration, music, and SFX as separate stems so each stays independently controllable.

## Step 6. Build and check the composition. AGENT OK

```powershell
npm run check
npm run dev      # long-running preview server, run it in the background
```

Fix every error before you render. Review the warnings.

Composition rules that must hold:

- Every timed element needs `data-start`, `data-duration`, and `data-track-index`.
- Every timed element needs `class="clip"`.
- Timelines are paused and registered on `window.__timelines`.
- No `Date.now()`, no `Math.random()`, no network fetches. The render must be deterministic.

The project pins an exact HyperFrames version so it re-renders the same way over time. The reference
pins `hyperframes@0.7.71`. Do not change the pin without a reason and a re-review.

Use `hyperframes-core` for the composition contract, `hyperframes-animation` for motion, and
`hyperframes-cli` for the build loop.

## Step 7. Render and package. AGENT OK

```powershell
npm run render
```

Then encode the delivery cut and capture its evidence in one step:

```powershell
powershell -ExecutionPolicy Bypass -File ..\..\..\tools\package_review_cut.ps1 `
  -Source renders\video-v002.mp4 `
  -Output ..\..\..\deliverables\review-cuts\<slug>-v002\<slug>-review-v002.mp4
```

The packager encodes 1080 x 1920 at 30 fps, H.264 `-preset slow` at 2400 kbps, AAC 48 kHz 160 kbps,
`loudnorm I=-16 TP=-1.5 LRA=11`, and `+faststart`. It then probes, hashes, and writes a JSON report
marked `review-cut-not-promoted`. That status is deliberate.

Build the caption sidecar:

```powershell
python ..\..\..\tools\build_srt.py --groups caption_groups.json --out <output>.srt
```

## Step 8. Review the encoded file. AGENT OK, human on taste

Judge the encoded artifact, never the timeline. Reuse these eleven requirements.

| ID | Requirement | How to check |
|---|---|---|
| V01 | Source integrity | Registered screenshots and render copies stay byte-identical |
| V02 | Fidelity | Product screens read clearly at 360 px and at full size |
| V03 | Claims | No prohibited wording is audience-legible in any frame |
| V04 | Illustrative | Simulated movement keeps its visible label |
| V05 | Hierarchy | The focused element matches the narration at that moment |
| V06 | Captions | Readable, unobstructed, inside the safe area, timing conformed to speech |
| V07 | Narration | Complete transcript. Tone and pronunciation need a human. |
| V08 | Mix | Measure LUFS, LRA, and true peak |
| V09 | Boundaries | Inspect `n-1`, `n`, `n+1` at every deterministic boundary |
| V10 | Call to action | The action element stays sharp and unobstructed to the last frame |
| V11 | Technical | Codecs, dimensions, frame rate, frame count, clean full decode |

Reference v002 results: -16.36 LUFS, 2.00 LU LRA, -1.46 dBTP, 1,395 decoded frames, boundaries at
frames 260, 514, 814, 1082, and 1249, and a clean full decode.

A note on V07. Local ASR renders "ZebPay's" as "ZEPE's". That is not proof of bad pronunciation, and
not proof of good pronunciation either. It only blocks a machine-only pass. A person must listen.

Write the verdict into `production/review/` beside the existing records. Use `script-video-review`
and the `video-reviewer` agent.

## Step 9. Promote. HUMAN ONLY

1. Listen to the exact encode with sound at phone scale. Judge voice tone, brand pronunciation, and
   the music and SFX balance.
2. Confirm the registered screenshots show current product UI.
3. Approve the deterministic claim mask and replacement treatment for campaign use.
4. Obtain product, legal, regulatory, and brand approval.
5. Explicitly promote the exact MP4 hash to `deliverables/final/`.

Review media stays ignored by Git. A video enters Git LFS only when the owner asks for that exact
file. Follow `.agent-harness/recipes/git-lfs-video-delivery.md`.

## How the next video in this category gets faster

1. Copy the claims-register shape, not its contents. Each feature needs its own register.
2. Reuse the HyperFrames project structure, the caption skin, and the packaging script.
3. Reuse the music and SFX generators. Change the seed and the duration.
4. Reuse the eleven review requirements as the starting rubric.
5. Keep the narration script short. 741 characters produced 46.6 seconds.
6. Recover an existing performance from provider history rather than paying to synthesize again.

Nothing in this list costs credits, so the second video in this category is mostly writing and
review time.

## The reference video, as delivered

| Property | Value |
|---|---|
| Resolution and rate | 1080 x 1920 at 30 fps |
| Runtime | 46.600 seconds, 1,395 decoded frames |
| Narration | One continuous ElevenLabs performance, 6 segments |
| Generative video | None |
| Review cut | v002, SHA-256 `3B90B00BC81BF90F0EEC6F19696E8FF7A3175C5F9591F3F66CCCE8389190FA76` |
| Status | Keeper at the encoded-artifact gate. Not promoted. |

| Gate | Status |
|---|---|
| Encoded-artifact review | KEEPER. No blocker remains in v002. |
| v001 | Blocked by its claims review. Preserved as evidence. |
| Human listening | Pending |
| Screenshot currency and claim-treatment approval | Pending |
| Product, brand, legal, regulatory approval | Pending |
| Promotion to final | Not requested |

The clone now carries the reproduction set through Git LFS: the six narration segments, the provider
master, the seeded music bed, and the six SFX files. Run `git lfs pull`, then `npm run check` and
`npm run render`. The picture, music, and SFX rebuild exactly.

## Skills and agents

| Task | Skill | Agent |
|---|---|---|
| Whole workflow | `script-video-production` | |
| Scaffold | `script-video-bootstrap` | `script-rewriter` |
| Composition and rendering | `hyperframes`, `hyperframes-core`, `hyperframes-cli` | |
| Deterministic craft | `script-video-motion-graphics` | `video-editor` |
| Assembly, mix, captions | `script-video-post` | `video-editor` |
| Encoded review | `script-video-review` | `video-reviewer` |
| Record new evidence | `/learn` | |

## Do not do this

- Do not edit a source screenshot to change what the product appears to say. Mask or replace in the
  composition instead.
- Do not invent product UI, a transaction, a fee, or feature behavior with an image generator.
- Do not add a claim that is missing from the register, even if it sounds harmless.
- Do not let a transcript rewrite approved copy.
- Do not change the pinned renderer version without a re-review.
- Do not call a technically clean encode a final.
