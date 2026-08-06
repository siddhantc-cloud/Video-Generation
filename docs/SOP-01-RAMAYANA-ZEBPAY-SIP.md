# SOP 01: Produce the Ramayana x ZebPay SIP film

Film title: **"The Squirrel in Ram Setu."** It is a vertical ZebPay SIP advertisement. It uses the
Ramayana squirrel story to show that small repeated contributions build something large.

Complete `docs/SOP-00-SETUP.md` before you start. This SOP assumes a verified machine.

## Film specification

| Property | Value |
|---|---|
| Resolution | 1080 x 1920 |
| Frame rate | 30 fps |
| Runtime | 52.2 seconds, exactly 1,566 frames |
| Narration | One continuous performance, 105 words, 15 phrase-owned beats |
| Promoted final | v005 captioned master, tracked in Git LFS |
| Newest creative-approved review | v011 clean and captioned cuts |
| Workspace | `Ramayana-ZebpaySIP/` |

The promotion rule is strict. v005 stays the final until the owner explicitly selects a replacement
that has documented music rights, voice entitlement, brand approval, legal approval, and regulatory
approval. Read `Ramayana-ZebpaySIP/WORKFLOW.md` for the live status.

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Environment | The setup script passes | `tools/setup-video-repo.ps1` | Operator | Required |
| Frozen script | The approved narration is unchanged | `scripts/original-script.md` | Human | Required |
| Audio clock | One continuous narration defines every frame boundary | Phrase map and EDL | Editor | Required |
| Zero-spend proof | The complete keyframe animatic passes human review | v004 animatic review | Human | Required before paid motion |
| Spend gate | Every Seedance job has a live quote and a human approval | Cost plan and job ledger | Human | Required per job |
| Keeper gate | Every take is judged against criteria written before it existed | `review/takes/` | Reviewer | Required |
| Encoded QC | The real encoded file passes probe, boundary, mix, and caption checks | Review QC record | Reviewer | Required |
| Human listening | A person judges voice, accent, and pronunciation | Owner playback record | Human | Required |
| Release | Music rights, brand, legal, and regulatory approval are documented | Release records | Human | Required before promotion |

## Read this before you promise a rebuild

**You cannot rebuild this film from a fresh clone.** The generated Seedance footage, the narration
audio, and the working mixes are intentionally outside Git. The clone gives you the scripts,
keyframes, storyboard, timelines, audio metadata, review records, cost ledger, and tools.

You have three honest options.

| Option | What it costs | What you get |
|---|---|---|
| Watch the delivered film | Nothing | `git lfs pull`, then play the v005 master or the packaged v011 review |
| Get the media from the owner | A file transfer | An exact local rebuild, because every timeline and manifest is in Git |
| Regenerate the motion | About 147 to 165 Higgsfield credits at 480p, plus ElevenLabs characters | A new film that follows the same plan. Generated takes are never byte-identical. |

The credit numbers are dated evidence from 2026-07-24. Re-quote live before you spend.

## Where everything lives

| Folder | Contents |
|---|---|
| `project/` | Brief, Higgsfield operating spec, Cinema Studio navigation runbook, cost and learning ledger |
| `scripts/` | Frozen original script, shooting script, shot tracker |
| `assets/` | Character bible, locations, props, brand, reference stills |
| `keyframes/` | Approved shot designs, including the `short-v004/` set |
| `storyboard/` | Film-order visual board, `index.html` |
| `audio/` | Voiceover versions, music, native SFX |
| `footage/` | `generated/` raw takes, `selects/` approved takes |
| `edit/` | Timelines, EDLs, HyperFrames animation slots, working audio |
| `review/` | Acceptance criteria, QC records, human rejection records |
| `deliverables/` | Review cuts and the promoted final |
| `tools/` | Reproducible local helpers |

## The production path that produced the film

Follow this order. Each step has real evidence in the repository.

### Phase 1. Freeze the script. HUMAN

The approved narration is 105 words. It stays unchanged in `scripts/original-script.md`. Production
adaptations go in `scripts/shooting-script.md` with a change log.

### Phase 2. Make audio the clock. AGENT OK

Generate one continuous scratch narration and capture word boundaries from the same request.

```powershell
python tools/edge_tts_word_timed.py `
  --text-file scripts/short-narration-v004.txt `
  --audio edit/audio/animatic-short-v004/narration-scratch.mp3 `
  --timings edit/audio/animatic-short-v004/narration-word-boundaries.json `
  --voice en-IN-PrabhatNeural --rate=-4%
```

Then build a phrase map. Each visual names the first word it owns. Snap each cut to the nearest whole
frame. The full rule set is in `edit/AV_SYNC_SYSTEM.md`. Read it. It explains why integer frames
prevent drift, and why percentage weights do not prove semantic sync.

### Phase 3. Build the visual bible and keyframes. HUMAN plus image tool

ChatGPT ImageGen produced the reusable character, location, and bridge-state references, then the
eleven story keyframes. Approve one look-lock frame and a contact sheet before you make every shot
frame. Keep pebbles, weather, poses, and branding as shot state. Never let them contaminate a
reusable identity asset.

### Phase 4. Build the free animatic. AGENT OK

Place every keyframe on its phrase-owned interval and render the whole film with scratch narration.

```powershell
python tools/render_phrase_locked_animatic.py `
  edit/timelines/animatic-short-v004-phrase-map.json `
  --output deliverables/review-cuts/animatic-short/OUT.mp4
```

The v004 animatic contained exactly 1,566 frames, including graph and logo placeholders, before any
paid motion. It is the first complete film, not a preview.

Two checks are not optional:

1. Every cut must land within half a frame of its matching word. v004 measured 13.5 ms maximum.
2. Inspect the frames at `n-1`, `n`, and `n+1` around every boundary. This caught a ten-frame dark
   flash at K10 to G11 that automated stream checks reported as clean.

**A human must approve the animatic before any paid motion.** This is the money gate.

### Phase 5. Generate the motion. HUMAN APPROVES EACH JOB

Register the approved character and location references as Higgsfield Cinema Elements. Then generate
one beat at a time with Seedance.

Preflight every job:

```powershell
higgsfield account status --json
higgsfield model get seedance_2_0 --json
higgsfield generate cost seedance_2_0 <exact final parameters> --json
```

Rules that produced the keeper path:

- One subject, one action, one camera idea per job.
- Attach the exact start frame as `start_image`, not as a generic reference.
- Prompt the motion delta. Do not re-describe identity that a reference already carries.
- Request native diegetic SFX only. Keep narration and music out of the shot.
- Write the pass criteria before the take exists.
- Submit one job once. Record the provider ID before you monitor it.
- Change one diagnosed variable per retry. Do not buy random rerolls for a prompt mistake.

The learned keeper path used eleven takes of 6, 4, 4, 4, 4, 4, 4, 4, 5, 4, and 6 seconds. That is 49
billed source seconds at 480p. One take, K03, was a partial keeper. Its valid 0.00 to 1.50 second
range was slowed and held to fill four seconds instead of triggering a reroll.

Use `project/higgsfield-manual-generation-operating-spec.md` for the exact operating method and
`project/higgsfield-cinema-studio-navigation-runbook.md` for page navigation.

### Phase 6. Review every take before you retry. AGENT OK, human on taste

Probe first. Inspect the first frame, the action landing, the last frame, and any suspected failure
range. Return PASS, FAIL, or NEEDS HUMAN with timestamps and the usable source range.

Before a retry ask: is the usable range long enough, can a hold or crop hide the failure, can post
supply the ambience, is the defect local, or does the shot need a redesign? Salvage is cheaper and
more controlled than a blind reroll.

Only approved takes move from `footage/generated/` to `footage/selects/`.

### Phase 7. Build the deterministic graphics. AGENT OK

Two sections never go to a generative model.

| Slot | Content | Exact length |
|---|---|---|
| `edit/animations/slot_sip_graph_v005/` | The SIP graph: one uneven market curve plus equal contribution markers on a fixed bridge cadence | 319 frames |
| `edit/animations/slot_zebpay_logo_v005/` | The ZebPay brand close and `START YOUR SIP` call to action | 100 frames |

HyperFrames rendered both at the exact frame count, so no conform re-encode was needed. Motion must
be a pure function of frame number. The selected graph render is
`edit/animations/slot_sip_graph_v005/renders/sip-graph-v005_r3_1080x1920_30fps_hq.mp4`, and its
evidence is `edit/animations/slot_sip_graph_v005/render-report.md`.

A warning from the record: the first graph render had a 2 to 3 frame headline overlap that automated
checks reported only as informational. The third pass derived boundaries from integer frame
arithmetic. Inspect the real rendered frames every time.

### Phase 8. Produce the final narration. HUMAN CHOOSES THE VOICE

The narrator is the account-owned ElevenLabs Voice Design voice `NarratorZebPay`.

```powershell
python tools/generate_elevenlabs_tts.py <arguments>
python tools/transcribe_elevenlabs_scribe.py <arguments>
python tools/build_elevenlabs_phrase_locked_audio.py <arguments>
```

Rules:

- Audition difficult names and acronyms before a full request.
- Generate one continuous performance after copy lock.
- Keep synthesis spelling separate from display copy. v011 synthesizes `S. I. P. lets you invest the
  same amount regularly.` while the caption reads `SIP lets you invest`.
- Conform by whole phrase into the approved frame slots. Do not globally stretch the performance.
  v011 conforms the 4.320 second repair into frames 1116 to 1227 at `1.144017857x`, pitch preserved.
- Derive captions from the conformed final narration.

The voice history is the most useful lesson in this project.

| Review | Route | Machine result | Human decision |
|---|---|---|---|
| v006 | ElevenLabs `NarratorZebPay` | All 105 words recovered, 1,566-frame lock | Became the baseline |
| v008 | Local Qwen3-TTS | All terms recovered, QC passed | Rejected. The accent felt foreign and SIP sounded robotic. |
| v009 | Sarvam Bulbul v3 `mani` | Timing, ASR, loudness, decode passed | Rejected. The accent felt exaggerated and "A SIP" fused. |
| v011 | ElevenLabs, G12 phrase repaired only | Same measured lock | Accepted on 2026-07-24, reconfirmed 2026-07-25 |

Three technically perfect voices were rejected by ear. **A machine transcript is never a voice
approval.** Do not reinstall Qwen3-TTS. The owner removed it on 2026-07-25.

### Phase 9. Mix, caption, assemble, and QC. AGENT OK

Keep narration, native SFX, ambience, and music on separate stems. Native SFX sits at -10 dB under
narration. Music ducks under speech instead of raising the narration. Add captions last, in the lower
safe band, below the graph focal curve.

```powershell
python tools/build_narration_sfx_music_mix.py <arguments>
python tools/av_sync_render.py <manifest.json>
```

A run is only finished when the tool prints `SYNC LOCKED`. Then probe the encoded result: runtime,
dimensions, frame count, frame rate, codecs, loudness, and true peak. Inspect every modified
boundary. Watch the whole file at phone scale with sound.

v011 measures -16.5 LUFS, 4.2 LU LRA, and -3.2 dBTP. Exact hashes are in
`review/final-short-v011-elevenlabs-music-demo-qc.md`.

### Phase 10. Promote. HUMAN ONLY

1. A person watches the complete encoded file with sound.
2. A person approves voice, accent, pronunciation, music taste, and SFX balance.
3. Brand, legal, and regulatory owners approve.
4. Music rights and commercial voice entitlement are documented.
5. Only then, promote one exact file to `deliverables/final/` and record its SHA-256.
6. Add it to Git LFS only when the owner asks. Follow
   `.agent-harness/recipes/git-lfs-video-delivery.md`.

The demo music in v011 is Mixkit `Sun and His Daughter`, used for the review only. It is not
campaign-cleared. Replace it before release.

## Open gates today

| Gate | Status |
|---|---|
| v011 creative playback | Passed on 2026-07-24, reconfirmed 2026-07-25 |
| Final-campaign music rights | Pending |
| Commercial voice entitlement | Pending |
| Brand, legal, and regulatory release | Pending |
| Promotion of v011 over v005 | Not requested |

## Skills to use

| Task | Skill |
|---|---|
| Whole workflow | `script-video-production` |
| Cinema Studio pages and Elements | `ramayana-cinema-navigation`, `ramayana-elements-continuity` |
| Shot planning and cost | `ramayana-video-plan` |
| One paid shot | `ramayana-shot-generate` |
| Take and cut review | `ramayana-video-review` |
| Assembly and mastering | `ramayana-video-post` |
| Recording new evidence | `/learn`, which uses `ramayana-learn` |

Use the `ramayana-*` skills for this film. Use `script-video-*` for a new film.

## Do not do this

- Do not overwrite a raw take. A revision gets a new version.
- Do not move a take into `footage/selects/` without a written verdict.
- Do not put text, captions, the inscription, the stripe reveal, or ZebPay branding inside a
  generative shot. Post owns them.
- Do not use a different voice per shot. The narrator is one continuous external voice.
- Do not treat a passing QC as a release.
