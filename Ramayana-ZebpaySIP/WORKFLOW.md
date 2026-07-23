# Manual video-production workflow

## Master stage checklist

| Stage | Requirement | Pass condition | Evidence in this workspace | Owner | Status |
|---|---|---|---|---|---|
| 1. Development | Lock the idea, audience, message, format, and script | Brief and human script are approved | `project/brief.md`, `scripts/original-script.md` | Human/Creative | Script exists; approval record absent |
| 2. Pre-production | Convert the script into shots and plan the visual world | Shooting script, shot tracker, assets, storyboard, and keyframes are reviewable | `scripts/`, `assets/`, `storyboard/`, `keyframes/` | Director/Producer | Built; human approval record absent |
| 3. Animatic | Prove story, timing, and pacing before expensive production | Whole film plays in order with scratch VO and no sync drift | v004 animatic, phrase map, and EDL | Editor/Human | Complete: human approved 52.2-second v004 |
| 4. Production | Create every approved moving cell | Each cell has raw versions, an approved select or documented range repair, and a review verdict | `footage/generated/`, `footage/selects/`, `review/short-v004-motion-first-pass-review.md` | Production/Director | Complete for short v004 |
| 5. Post-production | Assemble picture, VO, SFX, graphics, captions, and optional music | Picture and sound are locked; all overlays are correct | `edit/`, `audio/`, final phrase map | Editor/Sound | Complete for v003; optional music unavailable and documented |
| 6. Review and QC | Clear creative, continuity, sound, technical, and operator brand checks | No operator-QC blockers; external sign-off is recorded separately | `review/final-short-v003-qc.md` | Human/Producer/QC | Operator QC complete; human/brand/legal release pending |
| 7. Delivery | Export platform masters and archive the project | Masters open correctly and match delivery specs | `deliverables/final/DELIVERY-v003.md` | Editor/Human | Captioned/clean/poster delivered; human release pending |

## 1. Development

This is where a normal production answers: What are we making, for whom, why, in what format, and
what must the audience understand or feel?

For this film:

- `project/brief.md` is the one-page production brief.
- `scripts/original-script.md` is the immutable human source.
- Changes to the message should happen here, before shot work is revised.

## 2. Pre-production

Pre-production turns words into a plan before shooting.

1. Break the script into scenes and single-purpose shots.
2. Assign a shot ID and narration span to every visual beat.
3. Lock character, environment, prop, wardrobe, lighting, and brand references in `assets/`.
4. Draw/build the storyboard in film order.
5. Approve keyframes individually.
6. Assemble the keyframes with scratch narration as an animatic.
7. Review pacing and continuity across the whole film.
8. Record approvals or revision notes before producing footage.

The shooting script is canonical for shot intent. The shot tracker is canonical for progress.

## 3. Production

Production creates moving footage. Treat generated shots like camera dailies:

Follow `project/higgsfield-manual-generation-operating-spec.md` for the current Seedance/Cinema Studio/
Supercomputer method, reference roles, cost gate, native-SFX architecture, and per-take records.
Before any paid run, also update `project/production-learning-and-cost-plan.md` with the live quote,
maximum authorized jobs, and estimated cumulative spend.

1. Start from the approved keyframe and shot specification.
2. Produce one action and one camera move per shot.
3. Save every raw version in `footage/generated/` without overwriting earlier versions.
4. Review identity, anatomy, motion, continuity, contact, artifacts, and framing.
5. Move/copy only the approved version to `footage/selects/` using the shot ID as its filename.
6. Update `scripts/shot-tracker.md` with the verdict and evidence path.

Pilot difficult shots before batch production. This workspace contains pilots for S1-a and S4-c.

## 4. Post-production

Post-production turns selected shots into the film:

1. Replace animatic slides with approved moving selects while preserving shot timing.
2. Record or generate the final continuous narrator track.
3. Edit dialogue/VO, room tone, ambience, SFX, and music as separate stems.
4. Add deterministic graphics: `राम`, captions, stripe reveal, and ZebPay end card.
5. Apply consistent color, grain, framing, and loudness.
6. Lock picture first, then finish/mix audio against the locked timeline.
7. Export a review cut with a version number and date.

The timeline is audio-master and frame-quantized. See `edit/AV_SYNC_SYSTEM.md`. Rebuild with:

```powershell
python tools/av_sync_render.py edit/timelines/animatic.json
```

The run passes only when it reports `SYNC LOCKED`.

## 5. Review and revision

Use three distinct reviews:

- Creative review: story clarity, emotion, pacing, performance, and continuity.
- Brand/legal review: logo, financial claims, mandatory language, and depiction approvals.
- Technical QC: resolution, frame rate, captions, audio peaks/loudness, black frames, corrupt frames,
  sync, spelling, and export playback.

Review notes belong in `review/` and must name a shot ID, severity, owner, and evidence.

## 6. Delivery and archive

Deliverables normally include:

- 1080×1920 vertical master.
- Captioned social version.
- Clean version without captions when needed.
- Thumbnail/poster frame.
- Final script, captions, music/license records, and brand/legal sign-off.
- Project archive containing the approved timeline, selected footage, audio stems, and graphics.

No final master is currently present; `deliverables/final/` is intentionally waiting for approval.
