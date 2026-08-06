# SOP 01: Produce a story-driven generative brand film

Use this SOP to make **a new film in this category**, not only to reproduce the one that exists.

**Category A: the story film.** A short emotional film that carries a brand message through
characters, place, and performance. Organic motion is the point. A generative video model produces
the picture. Examples: a mythology or folk story mapped onto a product idea, a founder origin story,
a slice-of-life customer story, a seasonal or festival brand film.

The reference case is **"The Squirrel in Ram Setu"** in `Ramayana-ZebpaySIP/`. It is a ZebPay SIP
advertisement that uses the Ramayana squirrel story to show that small repeated contributions build
something large. Every rule below has evidence in that workspace.

Complete `docs/SOP-00-SETUP.md` first. Use `docs/SOP-02-PRODUCT-EXPLAINER.md` instead when the
subject is a product screen, exact data, or a claims-controlled feature.

## Is this the right category?

| Choose the story film when | Choose the product explainer when |
|---|---|
| The value is emotion, character, atmosphere, or performance | The value is clarity about a real product |
| The audience must feel something before it understands something | Every number, label, and claim must be exact |
| Real places, creatures, weather, or human action carry the meaning | App screens, charts, or UI carry the meaning |
| A metaphor is allowed | A regulator may read every frame |
| You can spend generation credits and iterate | You want a near-zero marginal cost |

Mixed films exist. The reference film is 74 percent generative picture and 26 percent deterministic
graphics. Route each interval separately, never the whole film at once.

## What it costs

Dated evidence from the reference film, verified 2026-07-24. Re-quote live before you spend.

| Item | Reference film | Notes |
|---|---|---|
| Generative motion | 49 billed source seconds, about 147 credits at 480p | 11 keeper takes of 4 to 6 seconds |
| Actual experiment spend | 165 credits, including one rejected setup | The ledger records 265 including an abandoned pilot |
| Practical repeat reserve | 221 to 294 credits at 480p | About 1.5 to 2 passes |
| Same plan at 720p | 331 to 441 credits | Multiply the same 49 seconds by the live rate |
| Same plan at 1080p | 662 to 882 credits | Same method |
| Keyframe stills | ChatGPT ImageGen or another approved still engine | Outside Higgsfield billing |
| Narration | ElevenLabs, about 700 characters for a 52 second film | Small |
| Deterministic graphics | Free, rendered locally | 14 seconds of the reference film |
| Music | Licensing cost, or produce your own | Demo music is never a release |

Budget by generated source seconds and expected attempts, not by final runtime.

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Idea contract | One audience, one message, one turn, one call to action | `project/brief.md` | Producer | Required |
| Frozen script | The approved narration is preserved unchanged | `scripts/source-script.md` | Human | Required |
| Audio clock | One continuous narration defines every frame boundary | Phrase map and EDL | Editor | Required |
| Visual system | Characters, locations, props, and brand sources are approved | Asset records | Continuity | Required |
| Zero-spend proof | The complete keyframe animatic passes human review | Encoded animatic | Human | Required before paid motion |
| Spend gate | Every job has a live quote and a human approval | Cost plan and job ledger | Human | Required per job |
| Keeper gate | Every take is judged against criteria written before it existed | `review/takes/` | Reviewer | Required |
| Deterministic finish | Exact copy, numbers, graphs, and logos are rendered outside the model | Render manifest | Motion | Required |
| Encoded QC | The real file passes probe, boundary, mix, and caption checks | QC record | Reviewer | Required |
| Human listening | A person judges voice, accent, and pronunciation | Playback record | Human | Required |
| Release | Music rights, brand, legal, and regulatory approval are recorded | Release records | Human | Required before promotion |

## Step 0. Create the workspace

Never copy a previous film and clean it afterwards. Scaffold a fresh one.

```powershell
powershell -ExecutionPolicy Bypass -File tools/New-VideoProject.ps1 `
  -ProjectName "Your-Film-Name" `
  -ScriptPath "D:\path\approved-script.md" `
  -AspectRatio "9:16" -Fps 30 -Resolution "480x854"
```

Or ask the agent to use the `script-video-bootstrap` skill. The folder contract is in
`video-production-system/PRODUCTION_SYSTEM.md`.

Record the delivery contract in `project/brief.md` before any creative prose: audience, single
message, emotional turn, call to action, platform, aspect ratio, frame rate, target runtime,
experiment resolution, brand and legal constraints, and the person who approves.

The social default is 9:16, 30 fps, 45 to 60 seconds. Use it only when the brief supports it.

## Step 1. Write and freeze the narration. HUMAN

Write for spoken comprehension, not reading speed. Let the pictures carry what they already show.
Read it aloud and time it. Record every meaning-level change from the original idea.

The reference film compressed a 166.6 second story into 105 words and 52.2 seconds.

Keep the approved script unchanged in `scripts/source-script.md`. Put provider-friendly adaptation in
`scripts/shooting-script.md` with a change log. The `script-rewriter` agent does this work.

## Step 2. Make the audio the clock. AGENT OK

Generate one continuous scratch narration and capture word timings from the same request. Free
Edge TTS is enough for scratch.

```powershell
python tools/edge_tts_word_timed.py `
  --text-file scripts/short-narration-v004.txt `
  --audio edit/audio/animatic/narration-scratch.mp3 `
  --timings edit/audio/animatic/narration-word-boundaries.json `
  --voice en-IN-PrabhatNeural --rate=-4%
```

Then build a phrase map. Each visual names the first word it owns and a whole-frame start. Quantize
every boundary to an integer frame.

Read `Ramayana-ZebpaySIP/edit/AV_SYNC_SYSTEM.md` before you write the map. It explains why integer
frames make drift impossible, and why percentage weights do not prove semantic sync. That was a real
defect in v003 of the reference film.

Do not change the narration after this point without remapping every boundary.

## Step 3. Build the visual bible and keyframes. HUMAN plus a still engine

1. Inventory the recurring characters, locations, props, wardrobe states, and brand sources.
2. Separate stable invariants from shot state.
3. Create clean canonical references and multi-view sheets only for assets that recur.
4. Approve one look-lock frame and a small contact sheet before you produce every shot frame.
5. Generate the shot keyframes from the phrase map and the approved references, never from memory.

Keyframe prompt shape:

```text
Create one photoreal 9:16 film keyframe for beat <ID>.
Story meaning: <what the audience must understand now>.
Canonical references: <character/location/prop invariants>.
Shot state: <pose, expression, weather, action phase>.
Composition: <shot size, screen position, depth, eyeline, negative space>.
Look law: <palette, motivated lighting, texture, performance register>.
Continuity: <what must match the previous and next frame>.
Keep the frame free of captions, logos, watermarks, and invented text.
```

Keep pebbles, weather, temporary poses, and branding as shot state. Never let them contaminate a
reusable identity asset. Register provider Elements only after local approval, using identical names
locally and in the provider workspace.

Use the `script-video-continuity` skill.

## Step 4. Build the complete free animatic. AGENT OK

Place every approved keyframe on its phrase-owned interval and render the whole film with scratch
narration and rough placeholders for the deterministic sections.

```powershell
python tools/render_phrase_locked_animatic.py `
  edit/timelines/animatic-phrase-map.json `
  --output deliverables/review-cuts/animatic/OUT.mp4
```

The reference animatic contained exactly 1,566 frames before any paid motion. **It is the first
complete film, not a slideshow preview.**

Two checks are not optional:

1. Every cut lands within half a frame of its matching word. The reference measured 13.5 ms maximum
   at 30 fps.
2. Inspect frames `n-1`, `n`, and `n+1` around every boundary. This caught a ten-frame dark flash
   that stream-level checks reported as clean.

**A human approves the animatic before any paid motion.** This is the money gate. Fix script,
timing, shot order, crop, and continuity here, where changes are free.

## Step 5. Route every interval. DIRECTOR

Classify each frame interval before you spend.

| Route | Use it for |
|---|---|
| Generative | Physical performance, organic environments, creatures, atmosphere, non-exact camera work |
| Deterministic | Exact text, claims, numbers, charts, captions, logos, UI, branded geometry |
| Turnkey | A bounded provider workflow with predictable output |
| Hold or reuse | A valid partial take, freeze, crop, speed change, or deterministic continuation |

Never ask a probabilistic model to render what a deterministic renderer can make exact. Never use
deterministic still motion when the creative value is performance, atmosphere, or camera movement.

Record the routing in `scripts/shot-tracker.md`. The `assistant-director` agent audits it for known
model failure modes.

## Step 6. Design and price each generative shot. PRODUCER

For each generative unit:

1. Use the longest coherent duration that still has one subject, one primary action, and one camera
   idea. The reference keepers were 4 to 6 seconds.
2. Define the start state, the action landing, the usable source range, and cut-friendly first and
   last frames.
3. Assign references by role: canonical image for identity, `start_image` for the exact continuity
   start, `end_image` only when the landing composition matters, previous accepted video only for a
   true continuation.
4. Prompt the motion delta. Do not re-describe identity a reference already carries.
5. Request only native diegetic SFX. Keep narration and score out of the shot.
6. Write measurable pass criteria before the take exists. The `scene-expectations` agent does this.
7. Flag reflections, crowds, simultaneous actions, exact object transfers, on-screen text, and
   unintended internal cuts as high risk.

Preflight every job against the live provider:

```powershell
higgsfield account status --json
higgsfield model get seedance_2_0 --json
higgsfield generate cost seedance_2_0 <the exact final parameters> --json
```

Prompt shape for image-to-video:

```text
<Subject> performs <one visible action> in one continuous shot.
Camera: <one primary move plus, at most, one texture modifier>.
Temporal arc: <opening state>; <motion development>; <landing state>.
Physics: <cloth, hair, water, weight, contact, or atmosphere that must move naturally>.
Audio: <one or two diegetic sounds tied to visible actions; room tone>.
Locks: identity, anatomy, wardrobe, prop geometry, lighting, and environment remain stable;
cuts occur only if explicitly specified.
```

The `prompt-reviewer` agent is the blocking gate before spend. It compares the final packet with the
approved script, the continuity controls, the current schema, and the live quote.

## Step 7. Generate the pilot, then the batch. HUMAN APPROVES EACH JOB

1. Pick one representative high-value, high-risk shot as the pilot.
2. Use the approved model at the lowest supported experiment resolution. Do not switch to a cheaper
   model just because it is cheaper.
3. Re-run schema and cost preflight immediately before approval.
4. Submit one job once. Record the provider ID before you monitor.
5. Download, hash, and probe the raw result without overwriting anything.
6. Review it against the rubric you wrote earlier.
7. On a structural failure, change one diagnosed variable. Never buy random rerolls to fix a prompt
   or reference mistake.
8. After two consecutive structural failures in one shot class, redesign the shot or fall back to
   deterministic.

A 480p result validates prompt structure, blocking, reference contamination, and that actual take at
480p. It is not a seed-locked preview. A higher resolution run is a fresh performance and needs a new
review.

Use the `script-video-generate` skill. It enforces duplicate-spend protection.

## Step 8. Review and salvage before you retry. REVIEWER

Probe first. Inspect the first frame, the action landing, the last frame, and any suspected failure
range. Return PASS, FAIL, or NEEDS HUMAN with timestamps and the usable source range.

Before any retry, ask:

- Is the usable range long enough for the phrase interval?
- Can a hold, crop, retime, insert, or cutaway hide the failure?
- Can post supply the missing ambience?
- Is the defect local enough for a surgical edit?
- Does the shot need a redesign rather than another roll?

The reference film kept a 1.50 second valid range from a take whose prop later disappeared, slowed
it, and held it to fill four seconds. Salvage is cheaper and more controlled than a blind reroll.

Only approved takes move from `footage/generated/` to `footage/selects/`. Never overwrite a raw take.
A revision gets a new version.

## Step 9. Build the deterministic sections. AGENT OK

Anything exact goes to HyperFrames, Remotion, or FFmpeg. Never to the video model.

1. Lock the exact frame interval, the copy or data source, the safe area, and the adjacent frames.
2. Create a design frame before animation.
3. Make motion a pure function of frame number.
4. Match the incoming and outgoing picture state.
5. Render and inspect the real encoded section, including boundary frames.

The reference film has two such slots: a 319 frame SIP graph and a 100 frame brand close.
HyperFrames rendered both at the exact frame count, so no conform re-encode was needed. Evidence is
in `Ramayana-ZebpaySIP/edit/animations/slot_sip_graph_v005/render-report.md`.

A warning from that record: the first graph render had a 2 to 3 frame headline overlap that automated
checks reported only as informational. Inspect the real rendered frames every time.

Use `script-video-motion-graphics` and follow
`.agent-harness/recipes/hyperframes-motion-graphics.md`.

## Step 10. Produce the final narration. HUMAN CHOOSES THE VOICE

1. Audition difficult names, acronyms, and brand terms before a full request.
2. Generate one continuous performance after copy lock.
3. Preserve the provider timing metadata and a versioned pronunciation dictionary.
4. Keep synthesis spelling separate from display copy. The reference synthesizes
   `S. I. P. lets you invest the same amount regularly.` while the caption reads `SIP lets you invest`.
5. Conform by whole phrase into the approved frame slots. Do not globally stretch the performance.
6. Derive captions from the conformed final narration.

Follow `.agent-harness/recipes/elevenlabs-phrase-locked-narration.md`. The verified conformer is
`Ramayana-ZebpaySIP/tools/build_elevenlabs_phrase_locked_audio.py`.

**The most useful lesson in this repository is here.** Three technically perfect voices were rejected
by ear:

| Version | Route | Machine result | Human decision |
|---|---|---|---|
| v006 | ElevenLabs owned voice | All 105 words recovered, frame lock held | Became the baseline |
| v008 | Local Qwen3-TTS | All terms recovered, QC passed | Rejected. Accent felt foreign, SIP sounded robotic. |
| v009 | Sarvam Bulbul v3 | Timing, ASR, loudness, decode passed | Rejected. Accent felt exaggerated, "A SIP" fused. |
| v011 | ElevenLabs, one phrase repaired | Same measured lock | Accepted by the owner |

A machine transcript is never a voice approval. Budget for listening rounds.

Do not reinstall Qwen3-TTS. The owner removed it on 2026-07-25. It needs explicit approval and about
15 GiB.

## Step 11. Assemble, mix, caption, and QC. AGENT OK

1. Build a frame manifest with hashes, source ranges, layer order, transforms, and audio routing.
2. Assemble only approved ranges.
3. Insert the deterministic sections.
4. Mix narration, native SFX, ambience, and music as separate stems. The reference keeps native SFX
   at -10 dB under narration.
5. Duck music under speech instead of raising the narration.
6. Add captions last, in the lower safe band, clear of any focal graphic.
7. Render versioned clean and captioned review cuts.
8. Probe runtime, dimensions, frame count, frame rate, codecs, streams, loudness, and true peak.
9. Inspect every modified boundary and watch the whole file at delivery scale with sound.

`tools/av_sync_render.py` prints `SYNC LOCKED` only when the streams match by construction. A run is
not finished before that line appears.

The reference v011 measures -16.5 LUFS, 4.2 LU LRA, and -3.2 dBTP.

Use `script-video-post` and `script-video-review`. The `video-reviewer` agent returns the independent
verdict. No role certifies its own output.

## Step 12. Promote. HUMAN ONLY

1. A person watches the complete encoded file with sound.
2. A person approves voice, accent, pronunciation, music taste, and SFX balance.
3. Brand, legal, and regulatory owners approve.
4. Music rights and commercial voice entitlement are documented. Demo music is never a release.
5. Only then, promote one exact file to `deliverables/final/` and record its SHA-256.
6. Add it to Git LFS only when the owner asks. Follow
   `.agent-harness/recipes/git-lfs-video-delivery.md`.

## How the next film gets cheaper

1. Reuse the project scaffold, the phrase-map schema, the review rubrics, and the render manifests.
2. Reuse approved visual laws and shot classes, never campaign-specific characters or claims.
3. Generate stills and the whole animatic before any video spend.
4. Keep exact material deterministic.
5. Reuse known-good `start_image` roles, duration classes, and prompt shapes.
6. Price by generated source seconds and expected attempts.
7. Pilot each new failure class once before batch work.
8. Keep partial usable ranges and solve local defects in post.
9. Change one diagnosed variable per retry.
10. Record every rejection, so acceptance rate rather than optimism sets the next budget.

## The reference film, as delivered

| Property | Value |
|---|---|
| Resolution and rate | 1080 x 1920 at 30 fps |
| Runtime | 52.2 seconds, exactly 1,566 frames |
| Narration | One continuous performance, 105 words, 15 phrase-owned beats |
| Generative picture | 11 keeper takes, 49 billed source seconds at 480p |
| Deterministic picture | 319 frame SIP graph plus 100 frame brand close |
| Promoted final | v005 captioned master, in Git LFS |
| Newest approved review | v011 clean and captioned cuts |
| Open gates | Music rights, voice entitlement, brand, legal, regulatory, promotion |

The promotion rule is strict. v005 stays the final until the owner explicitly selects a replacement
with all approvals documented. Live status is in `Ramayana-ZebpaySIP/WORKFLOW.md`.

The clone now carries the reproduction set through Git LFS: the approved selects, their native SFX,
the raw and repaired narration, the phrase-locked masters, and the two deterministic renders. Run
`git lfs pull`. Rejected takes, superseded versions, working renders, and the third-party demo music
stay local. The demo music source is recorded in `Ramayana-ZebpaySIP/audio/music/demo-v011/SOURCE.md`.

## Skills and agents

| Task | Skill | Agent |
|---|---|---|
| Whole workflow | `script-video-production` | |
| Scaffold | `script-video-bootstrap` | `script-rewriter` |
| Shots, timing, cost | `script-video-plan` | `assistant-director` |
| References and identity | `script-video-continuity` | |
| Animatic | `script-video-animatic` | |
| Pre-take rubric | `script-video-review` | `scene-expectations` |
| Spend gate | `script-video-generate` | `prompt-reviewer` |
| Deterministic motion | `script-video-motion-graphics` | `video-editor` |
| Assembly and mastering | `script-video-post` | `video-editor` |
| Independent verdict | `script-video-review` | `video-reviewer` |
| Record new evidence | `/learn` | |

For the reference film specifically, use the `ramayana-*` skills. They hold its navigation runbook,
provider IDs, cost ledger, and review evidence.

## Do not do this

- Do not spend a credit before a human approves the animatic.
- Do not put text, captions, logos, or exact brand geometry inside a generative shot.
- Do not use a different voice per shot. One continuous narrator owns the film.
- Do not overwrite a raw take or promote one without a written verdict.
- Do not treat a passing QC as a creative approval, or a review cut as a final.
