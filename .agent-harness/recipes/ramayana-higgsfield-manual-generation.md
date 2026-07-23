# Ramayana Higgsfield Manual Generation Recipe

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Source control | Brief, script, shot intent, keyframe, and reference roles are named before a paid run | Per-shot generation record | Director/Operator | Pending per shot |
| Animatic source | The approved frame-locked animatic row and its narration interval are named before a paid run | `edit/edl/animatic-short-v004.json`; shot record | Director/Editor | Complete for short v004 |
| Vertical conformance | Every start/end frame used for generation is exact 9:16 | `keyframes/short-v004/conformed/`; image-dimension check | Art/Operator | Complete for short v004 |
| Identity continuity | Each recurring subject uses the same canonical identity asset and only shot-relevant references | Reference list in shot record | Director/Operator | Pending per shot |
| Location continuity | Every bridge shot uses the correct one of the four bridge-state references | Reference list in shot record | Director/Operator | Pending per shot |
| Reusable Elements | Four canonical Characters and four bridge-state Locations exist in the project library; unnecessary Props are absent | `Ramayana-ZebpaySIP/project/higgsfield-cinema-navigation-screens/032-location-elements-complete.jpg` | Art/Operator | Complete |
| Global visual law | Palette, lighting, texture, performance, and UI encoding are copied from one source of truth | `Ramayana-ZebpaySIP/project/global-visual-law.md` | Director/Art | Complete; pilot validation pending |
| Prompt discipline | One primary action, one primary camera move, positive locks, and explicit physics are present | Prompt preflight | Director/Operator | Pending per shot |
| Sound architecture | Seedance carries diegetic SFX/ambience only; narration and music remain separate stems | Prompt, generated clip, audio review | Sound/Operator | Pending per shot |
| Cost boundary | Current schema and exact generation cost are checked before approval | CLI/UI preflight captured in shot record | Human/Operator | Complete for K01-K10 and K14 short-v004 first pass |
| Keeper gate | Full-motion, frame, continuity, and audio checks pass before a take becomes a select | Review verdict with timestamps | Director/Operator | K01 v002 keeper; pending per remaining shot |
| Automation trace | Prompt, parameters, reference paths, cost, version, result path, and verdict are retained | Companion generation record and manifest | Operator | Active for short v004 |

## Purpose

This is the repeatable operator recipe for manually producing `Ramayana-ZebpaySIP` shots in Higgsfield. The authoritative, detailed method is:

- `Ramayana-ZebpaySIP/project/higgsfield-manual-generation-operating-spec.md`
- `Ramayana-ZebpaySIP/project/higgsfield-cinema-studio-navigation-runbook.md` for the evidence-based website click path and live UI observations

The recipe is intentionally one-shot-at-a-time. It does not authorize generation, credit spend, bulk submission, or final approval.

## Inputs

- Creative truth: `Ramayana-ZebpaySIP/project/brief.md`
- Shot intent and VO mapping: `Ramayana-ZebpaySIP/scripts/shooting-script.md`
- Progress: `Ramayana-ZebpaySIP/scripts/shot-tracker.md`
- Character, bridge, and style references: `Ramayana-ZebpaySIP/assets/`
- Start/end designs: `Ramayana-ZebpaySIP/keyframes/`
- Timed story reference: `Ramayana-ZebpaySIP/deliverables/review-cuts/animatic/`
- Acceptance bars: `Ramayana-ZebpaySIP/review/criteria/`
- Reusable look law: `Ramayana-ZebpaySIP/project/global-visual-law.md`

## Output structure

For each generated take:

- Raw take: `Ramayana-ZebpaySIP/footage/generated/<SHOT>_vNNN_<surface>_<quality>_sound.mp4`
- Companion record: `Ramayana-ZebpaySIP/footage/generated/<SHOT>_vNNN.md`
- Extracted native sound bed, when retained: `Ramayana-ZebpaySIP/audio/sfx/generated/<SHOT>_vNNN.wav`
- Approved select only: `Ramayana-ZebpaySIP/footage/selects/<SHOT>.mp4`
- Review note: `Ramayana-ZebpaySIP/review/` with shot ID, version, severity, timestamps, owner, and verdict

Never overwrite a raw take. Never promote a take without an explicit review verdict.

## Reusable Cinema Studio Element registration

Cinema Studio Element CRUD is not exposed by the installed Higgsfield CLI 1.1.19. Use the authenticated website manually or through UI automation; never treat a generic CLI media upload as an Element.

1. Prepare one approved identity-only Character reference or character-free Location reference. Keep source files unchanged and save cleanup edits separately.
2. In **Elements**, select the Ramayana project and click **New Element**.
3. Enter the stable name and compact invariant-only description. Under UI automation, wait about 600 ms after typing before the next observation or action.
4. Open **Category**, click the visible `Character`, `Location`, or `Prop` item, and confirm the closed field shows that category. Do not trust keyboard selection without this confirmation.
5. Open **Upload media**, upload or select the approved file, and reduce any persistent prior selection to exactly `1 selected`.
6. Click **Add to Element** and visually confirm the intended preview.
7. Click **Create** once; verify `Element created.` and the exact handle/category in the refreshed library accessibility record.
8. Capture one final library screenshot for the batch. Never click **Use** or **Generate** during library setup.

Current project inventory: four Characters and four Locations. Zero Props are intentional until a pilot proves an object needs an exact recurring design. The complete UI behavior and failure notes live in Steps 15–16 of the navigation runbook.

## Operator sequence

1. Read the operating spec and the named shot row in the shooting script.
2. Confirm the shot's target edit duration from the narration-led animatic/EDL.
3. Treat multiple images inside one animatic row as editorial coverage, not automatic Seedance
   start/end endpoints. Check that identity, scale, hand/prop geometry, camera, and spatial state
   make the proposed motion physically reachable. The recovered S4-c pair is currently unsafe.
4. Confirm the start/end frames are exact 9:16. Conform non-9:16 images without overwriting the source.
5. Select the minimum canonical references: subject identity, costume/state if needed, correct bridge state/location, and optionally one camera-motion video.
6. Complete a shot packet using the template in the operating spec and copy the global Manual Style block unchanged unless an approved override is recorded.
7. Run the current read-only model checks:

   ```powershell
   higgsfield model get seedance_2_0 --json
   higgsfield generate cost seedance_2_0 --prompt "<approved prompt>" <exact flags>
   ```

8. Present the exact settings, reference roles, and cost to the human. Wait for approval.
9. Generate one take or an explicitly approved small candidate batch.
10. When a shot needs the approved keyframe as its opening state, send it through the explicit CLI
    `--start-image` field. A Cinema Studio picker upload observed as role `image` is only a generic
    reference and caused K01 v001 to converge toward the image late instead of opening from it.
11. After submission, verify a new Processing asset or job ID before doing anything else. The
    composer and Generate button may remain visible; never click twice merely because the form
    remains on screen. For an approved multi-shot batch, persist every returned job ID immediately
    and skip any manifest row that already has one.
12. Download/save the raw output and companion record immediately.
13. Review the whole clip in motion, then inspect start/middle/end frames and solo the native audio.
14. Treat `start_image` as image conditioning, not a guaranteed pixel-identical first frame. Check
    the actual first frame for story state, identity, geography, direction, and editability; record a
    similarity metric only as supporting evidence.
15. Classify failure as systematic or stochastic. Change one variable only on a systematic retry; keep the packet fixed for stochastic candidate rolls.
16. Copy only an approved take to `footage/selects/<SHOT>.mp4`; update the tracker and retain the original.
17. Add the extracted SFX bed to the separate audio workflow. Narration and music are never baked into the Seedance request.

### Cinema Studio website preflight notes

- Avoid **Turn to video** from an uploaded asset detail when the packet requires Cinema Studio; the observed action routed to a generic composer and selected Kling 2.6.
- Use project composer -> explicit **Cinema Studio 3.5** selection -> composer add/upload picker.
- Run any one-time **Check eligibility** offered for the start frame or Elements, then verify every intended reference thumbnail remains attached.
- Treat Duration as a slider and verify its bottom-toolbar label; do not assume a typed value was accepted.
- Re-read the final price after aspect, quality, duration, candidate count, and Sound state are all set. S1-a v002 showed 100 credits at 10 seconds while the site banner separately showed a 30% offer on 2026-07-22; future prices must be checked again.
- After clicking Generate once, require a new Processing asset or CLI job ID. The composer can remain visible after a successful submission; a second click risks a duplicate paid job.

## Surface routing

| Surface | Use | Constraint |
|---|---|---|
| Standalone Seedance 2.0 Standard | Default final shot generation, 4K, explicit start/end and image/video references | `std` is required for 1080p/4K |
| Seedance Fast/Unlimited website mode | Prompt/motion exploration at 480p/720p | Not the final-quality path; availability and terms change |
| Cinema Studio 3.5 | Look development and shots that materially benefit from locked genre/style/light/optics | Current workflow tops out at 1080p |
| Supercomputer | Optional orchestration, cost preview, and approved artifact handoffs | One shot/sequence per chat; do not let it rewrite locked references or submit without approval |

## Audio rule

For production candidates, enable native audio and prompt a diegetic-only bed tied to visible action. The soundtrack request names only the required physical sounds and location ambience. Character mouths stay closed; narration and score are supplied in post. If an otherwise exceptional visual take contains unusable generated audio, retain the visual only with a recorded exception and replace the sound in post.

## Previous-clip rule

- Continuation: attach the approved prior clip as context, also attach the canonical identity/location reference, open with `The scene continues`, and describe only the new beat.
- Camera/motion borrowing: declare the video as camera/motion reference only; identity, wardrobe, location, and source audio come from the current shot packet.
- Prefer the prior clip's final frame as the next start frame for a direct continuation.
- Re-anchor after two chained continuations; three is the hard project ceiling before returning to canonical references.

## Host parity

| Host | Manual method | Execution surface | Status |
|---|---|---|---|
| Codex | Reads this shared recipe and the film operating spec | Authenticated Higgsfield CLI plus website UI automation/manual website | Supported |
| Claude | Reads this shared recipe and the film operating spec | Authenticated Higgsfield CLI plus website UI automation/manual website | Supported |
| Human | Uses the same shot packet, cost gate, and review checklist | Higgsfield website/Cinema Studio/Supercomputer | Primary approval owner |

Any future automation must consume the same companion generation records and must preserve the human cost and keeper gates.

## Evidence destination

Environment verification remains in `.agent-harness/evidence/video-environment/`. Per-shot creative evidence stays inside `Ramayana-ZebpaySIP/footage/`, `audio/`, and `review/` so the complete film context remains in its clean production workspace.
