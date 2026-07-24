---
name: ramayana-video-post
description: Assemble and verify Ramayana-ZebpaySIP selects, narration, generated diegetic SFX, music, captions, deterministic graphics, transitions, review cuts, and final masters. Use only after shots have written keeper verdicts or when building approved deterministic sections.
---

# Ramayana video post-production

Read:

- `Ramayana-ZebpaySIP/WORKFLOW.md`
- `Ramayana-ZebpaySIP/edit/AV_SYNC_SYSTEM.md`
- `Ramayana-ZebpaySIP/scripts/shooting-script.md`
- `Ramayana-ZebpaySIP/scripts/shot-tracker.md`
- the relevant review verdicts.

## Assembly rules

1. Ingest only approved selects; never edit directly from an unreviewed raw take. A documented
   partial keeper may contribute only its accepted time range; conform that range into a derived
   clip under `edit/` and never copy invalid frames into the master.
2. Keep narration, native diegetic SFX, music, captions, and graphics as separate stems/layers.
3. Preserve native SFX only when the human accepts its content; replace or omit rejected audio
   without changing the raw file. Fade every shot-local SFX segment in and out over 30 ms before
   mixing.
4. Add all text, Devanagari title copy, financial copy, captions, and ZebPay branding
   deterministically in post.
5. Use the audio-master, integer-frame timing system and update EDL/timeline records.
6. Prefer deterministic still moves for shots that do not need generative subject motion.
7. Apply burned captions after every picture overlay and deterministic graphic. Use compact
   phrase/word-boundary chunks that remain within the social safe area; do not duplicate a spoken
   CTA subtitle over an end card that already renders the same approved copy verbatim.
8. Render review cuts before final delivery. Preserve failed QC renders as evidence and cap
   self-correction at three passes.
9. For deterministic picture replacements, record half-open integer frame ranges in a timeline
   manifest and trim/concatenate by frame, not rounded decimal timestamps. When a film-to-brand
   transition should be continuous, make local frame 0 reproduce the exact outgoing master frame.
10. When the approved audio must remain unchanged, stream-copy it and compare the audio elementary
    stream MD5 across the base and every review variant. Matching duration alone does not prove
    audio identity.
11. Inspect captions on the assembled render. A nominal caption-safe band or static composition
    check is preliminary; if subtitles cross a graph, face, prop, or CTA focal area, reposition and
    burn them again after picture lock.
12. For the final narrator, verify both voice discovery and actual synthesis entitlement. The
    ElevenLabs Voice Library contains Ramayana-specific mythology voices, but the current free API
    tier rejects library-voice TTS. Use the account-owned original `NarratorZebPay` voice unless a
    later live preflight proves an approved library voice is usable.
13. Generate one continuous timestamped narrator performance with the project pronunciation
    dictionary. If it does not match the locked 1,566-frame phrase map, preserve natural delivery,
    pad shorter phrase tails, accelerate only overrunning phrases without pitch change, and rebuild
    captions from the conformed word timings. Never globally stretch when measured phrase drift
    exceeds the semantic tolerance.

## Final QC

- Recheck frame rate, dimensions, duration, sync, loudness, captions, safe areas, logo integrity,
  and legal copy.
- Inspect the actual rendered frame immediately before and after every replacement boundary and the
  final frame of every logo/CTA hold.
- Verify narration intelligibility over SFX/music and inspect every scene boundary.
- If optional music is unavailable, rejected before generation, or unlicensed, document the
  exception and deliver the clean narration/native-SFX architecture instead of inserting an
  unreviewed substitute.
- Require human picture lock and brand/legal approval before the final master.
- Record output paths and decisions; do not overwrite prior review cuts or masters.

## Verified v005 delivery

- The approved captioned master is
  `deliverables/final/Ramayana-ZebPaySIP_FINAL_v005_1080x1920_captioned.mp4`.
- It is a byte-identical promotion of the captioned v005 review cut: 47,805,218 bytes,
  1,566 frames, 52.200 seconds, 1080×1920 at 30 fps, SHA-256
  `DBB08C1682CFCB45CDA8DE90C53DEDA9319DF862F0C099A123991F855B899B47`.
- Human creative playback passed on 2026-07-24. Legal or regulatory release remains separate and
  must not be inferred from creative approval.
- When the owner requests repository delivery, track only this promoted final with Git LFS. Keep
  raw generations, review cuts, stems, and intermediate renders ignored.
