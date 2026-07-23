# HyperFrames Motion Graphics Recipe

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Timing contract | Composition duration, fps, and source-frame boundaries are written before design | Slot `frame.md` | Partner agent | Required |
| Hero-frame design | The resolved end states work as still frames before motion is added | HyperFrames snapshots | Partner agent | Required |
| Deterministic animation | One synchronous paused GSAP timeline is registered under the composition ID | `index.html` + lint | Partner agent | Required |
| Mobile readability | Feed-scale type and labels survive a 360 px-wide preview | Contact sheet | Partner agent | Required |
| Motion verification | A `*.motion.json` sidecar asserts reveal order, in-frame state, and liveness | `npm run check` | Partner agent | Required |
| Caption safety | Critical content avoids the reserved lower band | `check --caption-zone` | Partner agent | Required |
| Human review | The human reviews HyperFrames Studio or the contact sheet before MP4 rendering | Approval in conversation | Human | Required |
| Exact delivery | Render is conformed and probed to the target frame count without touching the locked master | FFprobe record | Partner agent | Required |

## Scope

Use this recipe for repeatable script-video motion-design sections such as data graphics, logo cards,
typography, diagrams, and branded transitions. HyperFrames is the implementation surface; Remotion
guidance supplies frame-driven timing, easing, sequencing, and render-review principles. FFmpeg
remains the conform and assembly layer. The Ramayana entries below are verified examples, not brand
or story defaults.

## Build order

1. Read the current timeline or phrase map. Record exact source start frame, end frame, fps, aspect ratio, and caption-safe area.
2. Create one isolated slot under `<project>/edit/animations/`. Never author directly over a locked deliverable.
3. Run the official HyperFrames initializer and retain its exact CLI pin in `package.json`.
4. Copy only required local media into the slot's `assets/` directory.
5. Write `frame.md` first:

   - semantic beats and frame boundaries;
   - palette and typography;
   - final hero-frame state;
   - prohibited claims or visual implications;
   - mobile and caption-safe constraints.

6. Author one root at the project delivery dimensions with:

   - `data-composition-id`, `data-start="0"`, `data-duration`, `data-width`, `data-height`, and `data-fps`;
   - visible timed clips as direct children;
   - a paused, synchronous GSAP timeline registered in `window.__timelines`;
   - only deterministic, seek-safe motion.

7. For professional data motion:

   - preserve one visual space across related beats;
   - build with SVG/CSS and GSAP, not a chart library;
   - reveal one idea at a time;
   - use explicit easing and transforms/opacity;
   - avoid dashboards, grids, tick marks, legends, tiny labels, and generic glass cards;
   - never imply guaranteed financial growth when the message is cadence or discipline.

8. Add a matching `index.motion.json` sidecar.
9. Add `STORYBOARD.md` when the board will be used. For a completed single composition, reuse the
   real `index.html` as each frame's `src` and give each card its actual poster time. Storyboard
   durations must sum to the composition duration.
10. Run the first gate:

   ```powershell
   npm run check -- --snapshots --at <comma-separated-seconds> --caption-zone "x0=0;y0=.82;x1=1;y1=1;severity=error;seek=.2,.5,.8,.98"
   ```

11. Inspect every generated PNG. Correct visual defects before suppressing a finding. An
    informational transition warning is not proof that the transition is acceptable; the rendered
    frame immediately before and after each phrase boundary is authoritative.
12. Create a three-beat contact sheet and start Studio:

   ```powershell
   npm run dev -- --port <free-port>
   ```

   Hand back `http://localhost:<port>/#project/<slot-name>`.

13. Render only after human approval:

   ```powershell
   npm run render -- --quality standard --fps 30 --output renders/<name>_review.mp4
   ```

14. Probe duration, frame count, dimensions, codec, and pixel format. If necessary, create a separate conformed asset at the exact target frame count; preserve the original render.
15. Generate a post-render contact sheet and review the actual MP4 at all beat boundaries. For an
    integer-frame phrase map, derive animation boundaries as frame arithmetic such as `133 / 30`,
    not rounded decimal timestamps.
16. Insert into a new review cut only after the standalone asset passes. Captions remain last.

## Verified project learning — SIP graph v005

- Date: 2026-07-23.
- HyperFrames CLI: `0.7.68`.
- Target: 319 frames at 30 fps, 1080 × 1920.
- Beat boundaries: frame 133 (`same amount regularly`) and frame 245 (`through the ups and downs`).
- Design pattern: retain the K10 Ram Setu image as the cinematic world; place the uneven market line and fixed-cadence contribution path directly into the bridge perspective.
- Storyboard: three animated cards reuse `index.html` at poster times 2.2, 5.8, and 10.4 seconds; card durations sum to 10.633333 seconds.
- Final QA: lint 0 errors/0 warnings; runtime 0; layout 0; motion 0; contrast 38/38; caption-zone 0 errors.
- Render learning: the first actual MP4 exposed text overlap that the static auditor treated as informational. A second pass removed overlap but revealed a one-frame semantic lead. The selected third pass uses `133 / 30` and `245 / 30`, and its boundary contact sheet proves exact phrase ownership.
- Selected render: `Ramayana-ZebpaySIP/edit/animations/slot_sip_graph_v005/renders/sip-graph-v005_r3_1080x1920_30fps_hq.mp4`.
- Review asset: `Ramayana-ZebpaySIP/edit/animations/slot_sip_graph_v005/preview/sip-graph-v005-contact.png`.

## Verified project learning — ZebPay logo v005

- Date: 2026-07-23.
- HyperFrames CLI: `0.7.68`.
- Target: 100 frames at 30 fps, 1080 × 1920.
- Continuity pattern: extract the exact outgoing master frame and make it local frame 0. Begin the
  brand transition inside that image; do not hard-cut from the film into a generic card.
- Brand pattern: sample the supplied asset for the focal blue, animate the surrounding world, and
  leave the logo pixels unredrawn and undistorted.
- Closing rule: resolve the complete mark, wordmark, and CTA by the middle of the slot and hold them
  through the final rendered frame. Do not add an automatic end fade.
- Legal restraint: omit claims that are not required by the narration, including exchange-age,
  return, price, or rate claims.
- Caption rule: when the closing card renders the spoken CTA verbatim, omit the duplicate subtitle.
  For preceding motion graphics, burn captions only after assembly and inspect their actual overlap
  with the graph; a nominal safe zone is insufficient without a rendered contact sheet.
- Final QA: lint 0; runtime 0; layout 0 across 84 samples; motion 0; contrast 12/12; 100 decoded
  frames; no black interval.
- Selected render:
  `Ramayana-ZebpaySIP/edit/animations/slot_zebpay_logo_v005/renders/zebpay-logo-v005_1080x1920_30fps_hq.mp4`.
- Review cut integration: replace picture by exact frame ranges, concatenate on integer frame
  boundaries, and stream-copy the original audio. Verify audio preservation by elementary-stream
  MD5, not only by duration.

## Host parity

Codex and Claude use the same project slot, recipe, HTML, motion sidecar, and CLI pin. User-level HyperFrames skills live under `.agents/skills` for Codex and `.claude/skills` for Claude; this path difference is intentional, while the installed skill content must remain equivalent.
