# Higgsfield Cinema Studio navigation runbook

**Production:** Ramayana-ZebPay SIP — “The Squirrel in Ram Setu”
**Workspace:** Higgsfield Cinema Studio 3.5
**Started:** 2026-07-21
**Purpose:** A click-by-click, evidence-based manual runbook that another operator can follow without guessing or spending credits accidentally.

## Operating checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Production workspace | The Cinema Studio project opens and its main composer is visible | User screenshot, 2026-07-21, recorded in Step 1 | Human operator | Complete |
| Canonical project name | Website project name exactly matches `Ramayana-ZebpaySIP` | Second user screenshot plus operator confirmation, 2026-07-21 | Human operator | Complete |
| Project brief | Story, format, visual laws, continuity rules, and sound architecture are entered and saved | Project Brief screen, autosave test, and operator completion confirmation on 2026-07-21 | Human + Director | Complete |
| Element library | Recurring characters and bridge states are saved with stable names and correct reference roles; Props are added only when continuity requires them | Elements inventory; four Characters in screen 031 and four Locations plus all Characters in screen 032 | Human + Art | Complete: four Character and four Location Elements; zero Props intentionally |
| Visual controls | Genre, Style, and Camera settings are deliberately chosen for the shot; Auto is retained only by decision | Per-shot settings record | Director | Complete for S1-a v002; pending subsequent shots |
| Output controls | Aspect ratio, resolution, duration, shot count, and Sound state match the approved shot packet | Composer screenshot before generation | Operator | Complete for S1-a v002; pending subsequent shots |
| Spend protection | The live Generate cost is reviewed before every paid run | Pre-generation screenshot/record plus account ledger | Human | Complete for S1-a v002; mandatory for every future run |
| Navigation accuracy | Every documented control has either been seen in the live UI or is marked unverified | Live Brave mapping plus `higgsfield-cinema-navigation-screens/`, 2026-07-21 | Operator | Complete for the current UI |

## Safety rule

Do not press **Generate** while learning the interface, building the brief, or registering Elements. Before any paid generation, capture and approve the prompt, references, Genre/Style/Camera selections, aspect ratio, quality, duration, shot count, Sound state, and the live cost shown on the Generate button.

## Recording convention

Each step records:

1. **Starting screen** — how the operator knows they are in the right place.
2. **Action** — one exact click or entry operation.
3. **Expected result** — only what has been confirmed from the live UI; unknown menus remain marked unverified until seen.
4. **Stop condition** — where to pause for review before taking another action.
5. **Learning** — what the navigation or control appears to govern.

Once a control pattern is confirmed, homologous fields are handled as one batch. Do not collect a screenshot for every identical text block. Capture only a new interaction state, an error, a destructive boundary, or one final verification after the batch.

For subsequent Character Elements, use a **one-packet workflow**: provide name, Category, reference file, compact identity-only description, and Create instruction together. Capture the filled form only when it reveals new behavior; otherwise one post-creation confirmation is enough. Do not repeat the field-by-field Rama discovery sequence.

## Step 1 — Open the production project

**Status:** Complete
**Observed:** 2026-07-21 from the user-provided Cinema Studio screenshot.

### Action performed

1. From the Higgsfield top navigation, open **Cinema Studio**.
2. Create or open the Ramayana–ZebPay SIP production project.
3. Stop when the empty Cinema Studio composer is visible.

### Confirmed result

The Cinema Studio project is open in **Video** mode with **Cinema Studio 3.5** selected. The central asset area says **Nothing here yet**, so no media has been generated or uploaded into this project view.

### Name correction

The first screenshot appeared to read `Ramayan-ZebpaySIP`, while the canonical local production folder and intended title are `Ramayana-ZebpaySIP`. The human operator subsequently corrected the website project name and confirmed the update. The second screenshot shows the corrected `Ramayana-Zebp...` prefix in the sidebar.

## Step 2 — Open the project options menu

**Status:** Complete
**Observed:** 2026-07-21 from the second user-provided screenshot.

### Starting screen

The Step 1 project screen is visible. In the left sidebar, the truncated project name has a vertical **three-dot** menu to its right.

### Action

Click the **three-dot menu** beside the project name once.

### Confirmed result

The menu opens as a panel titled **Actions** and contains the following five items in this order:

| Menu item | Confirmed UI detail | Operational treatment |
|---|---|---|
| Pin | Pin icon | Available; exact effect has not yet been tested |
| Edit | Pencil icon | Available; likely opens project metadata, but its contents have not yet been inspected |
| Add folder | Folder-plus icon | Available; folder-creation flow has not yet been inspected |
| Copy link | Chain-link icon | Available; likely copies a project link, but sharing scope has not yet been verified |
| Delete | Red trash icon and red label | **Destructive:** do not select during normal production; deletion impact and recovery behavior are unverified |

### Stop condition

After documenting the menu, click outside it to close it without changing project state. The project name is already corrected, so no menu action is required now.

## Step 3 — Open Project brief

**Status:** Complete
**Observed:** 2026-07-21 from the third user-provided screenshot.

### Starting screen

The project is open with the canonical name `Ramayana-ZebpaySIP`. Close the **Actions** menu if it is still visible.

### Action

Click **Project brief** in the left project navigation.

### Confirmed result

**Project brief** becomes selected in the left navigation. The page shows the canonical project name `Ramayana-ZebpaySIP`, an updated timestamp, a short-description placeholder, and seven structured brief sections.

### Confirmed Project Brief structure

| Order | Field/section | Visible guidance text |
|---|---|---|
| 1 | Short project description | `Short project description goes here.` |
| 2 | Context | `Why this project exists.` |
| 3 | Narrative | `Story, message, and audience.` |
| 4 | Visuals | `References, mood, color palette, and creative direction.` |
| 5 | Production | `Schedule, locations, crew, and logistics.` |
| 6 | Status | `Current progress, blockers, and next steps.` |
| 7 | Resources | `Script, moodboard, storyboard, schedule, and assets.` |
| 8 | Notes | `Key decisions, updates, and project history.` |

The page also shows the project account/avatar control and **Share** in the top-right corner.

### Editing behavior still unverified

No global **Edit** or **Save** button is visible in this screen state. The fields may be inline-editable and may autosave, but neither behavior has been confirmed. Do not paste the production brief until one field’s editing and persistence behavior has been tested.

## Step 4 — Test the short-description edit affordance

**Status:** Complete
**Observed:** 2026-07-21 from the fourth user-provided screenshot.

### Starting screen

The **Project brief** page from Step 3 is visible.

### Action

Click once directly on the text **Short project description goes here.**

### Confirmed result

A blinking caret appears directly at the end of the description text, confirming that the block is edited inline. A **plus** control and a six-dot block handle become visible to the left of the active block. No modal, editor toolbar, Save button, or Cancel button appears in this state.

### What remains unverified

The screenshot confirms inline entry but does not yet prove how changes are saved or persisted. The next step uses the intended project description as a controlled save test.

## Step 5 — Replace the description and test save behavior

**Status:** Complete
**Observed:** 2026-07-21 from the fifth user-provided screenshot and operator confirmation.

### Starting screen

The caret is blinking at the end of `Short project description goes here.`

### Exact replacement procedure

1. Press **Shift+Home** once to select the current description text from the caret back to the start of the line.
2. Paste this exact replacement:

   > A reverent, photoreal 9:16 mythological social film that uses the Ram Setu squirrel story to show how small, consistent SIP investments can build meaningful results, with ZebPay appearing only as the closing sponsor.

3. Click an empty area of the page outside the description block to remove the caret.
4. Wait a few seconds and observe whether the **Updated today at…** timestamp changes or any saved/saving indicator appears.

### Confirmed result

The new description remains visible after the block loses focus. The human operator confirmed that the page autosaves; no explicit Save action is required.

The displayed `Updated today at 08:46 PM` timestamp did not visibly change between the supplied before-and-after screenshots. Do not use that timestamp alone as the save indicator. The operational save check is that the replacement remains after focus leaves the block; for high-risk edits, navigate away and return before assuming persistence.

### Source of the wording

The sentence is derived from `project/brief.md`: 9:16 vertical format, grounded and reverent photoreal tone, the Ram Setu squirrel as the SIP analogy, consistent investing rather than market timing, and ZebPay restricted to the sponsor close.

## Step 6 — Batch-fill all remaining Project Brief fields

**Status:** Complete
**Confirmed:** 2026-07-21 by the human operator after batch entry.

### Starting screen

The short project description is saved. Context, Narrative, Visuals, Production, Status, Resources, and Notes still contain their template guidance text.

### Procedure — use once for each field

1. Click once at the end of the field’s current guidance text.
2. Press **Shift+Home** once to select that line.
3. Paste the corresponding replacement below.
4. Click outside the block and move to the next field.

### Context

> Create a culturally respectful, emotionally grounded film that uses the Ram Setu squirrel episode to explain systematic investing: consistent small contributions matter more than predicting the perfect market moment. ZebPay appears only in the closing sponsor message.

### Narrative

> For Indian digital audiences and first-time investors. Rama’s army builds Ram Setu while a small squirrel repeatedly contributes pebbles, is mocked, and is recognized by Rama for showing up without being asked. The repetition becomes the SIP lesson: invest the same amount consistently instead of timing the market. Close with restrained ZebPay sponsorship.

### Visuals

> 9:16 vertical, grounded and reverent photoreal mythological epic. Warm sun-faded coastal palette; natural skin, fur, stone and sea; restrained performances; physically believable scale and contact. Keep Rama’s face, costume and bow consistent; keep the squirrel’s proportions, three stripes and tail stable; preserve vanara and bridge-state continuity. Story clarity over spectacle. Add all text, captions and logos in post.

### Production

> Pre-production includes scripts, storyboard, 30 keyframes, four bridge states, a frame-locked 166.633s animatic and two silent pilots; final runtime is not yet approved. Virtual locations are the shoreline, sea and bridge across four construction states. Roles: human creative approver, director/operator, art/continuity, editor/sound and brand/legal. Generate one controlled shot at a time. Use standalone Seedance 2.0 Standard for final candidates and Cinema Studio 3.5 where locked look or optics help. Sound On for diegetic SFX and ambience only; narration, music, graphics, captions and branding remain separate. Human approval is required before paid generation.

### Status

> Ready: brief, scripts, assets, storyboard, 30 keyframes, animatic and S1-a/S4-c pilots. Blockers: 15 keyframes are 2:3 and need non-destructive 9:16 conformance; final runtime and legal approval of “India’s oldest crypto exchange” remain open; native-SFX pilots are still required. Next: finish this brief, build Elements, lock the look, test representative high-risk shots, then generate and review one shot at a time.

### Resources

> Under Ramayana-ZebpaySIP/: project/brief.md; project/production-decisions.md; scripts/original-script.md; scripts/shooting-script.md; scripts/shot-tracker.md; assets/characters/; assets/environments/bridge/; keyframes/; deliverables/review-cuts/animatic/; review/criteria/; project/higgsfield-manual-generation-operating-spec.md; project/higgsfield-cinema-studio-navigation-runbook.md.

### Notes

> 2026-07-21 decisions: future Seedance candidates use native diegetic SFX and ambience; narration and music remain separate. Existing S1-a and S4-c pilots are visual evidence only because they are silent. Never overwrite raw takes; promote only reviewed selects. The claim “India’s oldest crypto exchange” requires human/legal confirmation before delivery. An artifact existing does not equal approval; record approvals in review/.

### Stop condition

After all seven fields are replaced, click outside the active block and perform one final visual check that no guidance placeholder remains. One final screenshot or a simple operator confirmation is sufficient; per-field screenshots are unnecessary.

### Confirmed result

The human operator confirmed that all remaining Project Brief fields were completed. The Project Brief setup gate is closed; do not duplicate these same descriptions in later navigation steps unless a downstream field needs a purpose-specific subset.

## Step 7 — Open Elements

**Status:** Complete
**Observed:** 2026-07-21 from the sixth user-provided screenshot.

### Starting screen

The Project Brief is complete and saved.

### Action

Click **Elements** in the left project navigation.

### Confirmed result

Elements opens as a centered **modal library** over the current project page. The current `Ramayana-Ze...` project is selected and shows the empty state **No elements yet**, with the explanation `Reuse your characters, locations, and props across every generation.`

### Confirmed Elements modal map

| Area/control | Visible state | Operational meaning |
|---|---|---|
| Elements title | Top-left pill inside modal | Confirms the active modal |
| Close | `×` at top-right | Closes the modal without creating an Element |
| My Elements | Selected in left column | Personal/project element library surface |
| All Pinned | Available under Pinned | Cross-library pinned collection; not needed for initial canonical setup |
| Projects | Multiple projects listed | Elements can be browsed by project; remain on the Ramayana project to avoid cross-project contamination |
| Current project | `Ramayana-Ze...` selected | Correct project scope |
| Getting Started | Child folder visible | Existing project folder; no element content is shown |
| Show subfolders elements | Toggle On | Child-folder Elements would be included in the current view |
| Filter | Available | Filtering behavior not yet inspected |
| Search | Available | Searches the visible element library; behavior not yet inspected |
| Create Element | Primary empty-state button | Correct path for registering the film’s canonical custom assets |
| Browse all elements | Secondary empty-state button | Library/discovery path; do not use for Rama, squirrel, vanara, or bridge continuity assets |

### Production decision

Use **Create Element** for every canonical film asset. Do not substitute public or cross-project Elements for the approved character and bridge references already stored in `Ramayana-ZebpaySIP/assets/`.

## Step 8 — Open Create Element

**Status:** Complete
**Observed:** 2026-07-21 from the seventh user-provided screenshot.

### Starting screen

The Elements modal shows **No elements yet** for the selected Ramayana project.

### Action

Click **Create Element** once.

### Confirmed result

A **New Element** modal replaces the library view. It uses a two-column layout: metadata on the left and media upload on the right.

### Confirmed New Element form map

| Field/control | Visible state | Operational treatment |
|---|---|---|
| Enter name | Empty single-line field | Required naming convention will be set before the first Element |
| Add description | Empty multi-line field | Identity/location invariants belong here; shot motion does not |
| Category | Defaults to **Auto** with a dropdown | Live category choices still need inspection; do not assume labels |
| Upload media | Large drag-and-drop/click target | Exact formats, count limits, validation behavior, and multi-upload behavior are not shown in this state |
| Close | `×` at top-right | Exits the form; unsaved-change behavior is unverified |
| Cancel | Bottom action | Exits/cancels; unsaved-change behavior is unverified |
| Create | Bottom primary action | Submission control; required-field validation and any processing/cost behavior are unverified |

No credit cost or generation price is displayed in this initial form. Creating an Element may still trigger validation or processing after submission, so do not press **Create** until the complete first-element packet is approved.

## Step 9 — Inspect Category choices

**Status:** Complete
**Observed:** 2026-07-21 from the eighth user-provided screenshot.

### Starting screen

The empty **New Element** form is open and Category shows **Auto**.

### Action

Click the **Category: Auto** dropdown once.

### Confirmed result

The live Category dropdown contains exactly four visible choices:

| Category | Use in this film |
|---|---|
| Auto | Avoid for canonical assets; explicit categories make the library auditable |
| Character | Rama, squirrel, and lead vanara |
| Location | Ram Setu shoreline/sea/bridge environment states when stored as reusable locations |
| Prop | Recurring controlled objects only, such as a hero bow or stone/pebble asset if later proven necessary |

The current selection remains **Auto**. No media or metadata has been entered and Create has not been pressed.

### First-element decision

The first canonical Element will be Rama with Category **Character**. Its identity description will contain only stable appearance/costume invariants; shot action, camera movement, emotion, and temporary pose stay in per-shot prompts or controls.

## Step 10 - Populate the Rama Element packet

**Status:** Complete
**Observed:** 2026-07-21 from the ninth user-provided screenshot, archived as `026-rama-element-reference-loaded.png`. On 2026-07-22, the human operator reported that the first 563-character description was truncated near its first occurrence of `tilak`; the exact platform limit is not yet verified. The completed pre-submission form is archived as `027-rama-element-ready-to-create.png`.

### Confirmed current state

- Name: `Rama-Canonical-Character`
- Category: **Character**
- Media: `assets/characters/rama_ref.png` is loaded and its preview is visible.
- Description: the compact replacement below is entered. In screen 027, the field is vertically scrolled, so its opening words are above the visible viewport while the terminal `bow.` is visible.
- **Create** is visible but has not been pressed.

### Exact description to enter

> Young adult Rama: lean athletic, medium-brown skin, oval clean-shaven face, dark eyes, long wavy black hair, vertical tilak, gold crown, saffron-orange robes, dark wooden bow.

The compact replacement is 175 characters. It keeps the highest-value visible identity anchors while the uploaded reference image carries the finer jewellery, garment, and bow details. Screen 027 also proves that the description field scrolls; therefore the earlier apparent cut may have been viewport behavior rather than a hard character cap. Do not state a definitive field limit until it has been measured in the live UI.

This field locks identity and costume only. Do not add the shoreline, sunset, wind, pose, gaze, emotion, camera, or shot action from the reference image; those variables belong in the shot packet.

### Stop condition

The verification screen is complete and the packet is approved for submission. Click **Create** once, wait for the modal to respond, and do not click repeatedly while it processes. Capture the resulting Element library or any error before continuing.

### Confirmed result

The human operator clicked **Create** once. The modal returned to the project Elements library and displayed a Rama thumbnail card labelled **Character**, confirming successful creation. The card label is visibly truncated as `@Rama-Canonical-Charac...`; confirm the full inserted handle later from the composer `@` picker rather than inferring it from the truncated card. Hovering the thumbnail exposes **Check eligibility**; its purpose and effects are unverified, so it was not selected. The library also now shows a **New Element** tile for the next canonical asset. Evidence: `028-rama-element-created.png`.

## Step 11 - Create the canonical squirrel Character

**Status:** Complete
**Observed:** 2026-07-22 from `029-squirrel-element-reference-loaded.png` and the verified library in `030-character-elements-automation-result.png`.

### One-packet setup

- Name: `Squirrel-Canonical-Character`
- Category: **Character**
- Media: `assets/characters/squirrel_ref.png`
- Description (170 characters):

  > Indian palm squirrel: small lean body, tan-brown fur, three pale dorsal stripes, dark eyes, rounded ears, fine paws, long bushy tail; stable stripe count and proportions.

The name, Category, and reference preview are confirmed in screen 029. The compact description was entered, **Create** was clicked once through the authenticated UI automation surface, and the library returned with `@Squirrel-Canonical-Character` labelled **Character**. The exact handle is present in the accessibility record even though the visible card truncates it. Evidence: screen 030.

## Step 12 - Create the canonical lead-vanara Character

**Status:** Complete
**Observed:** 2026-07-22 from `030-character-elements-automation-result.png`.

### One-packet setup

- Name: `Lead-Vanara-Canonical-Character`
- Category: **Character**
- Media: `assets/characters/vanara_lead_ref.png`
- Description (175 characters):

  > Lead vanara: tall, heavily muscular, tawny-brown fur, broad ape-like face, dark eyes, long tail, gold circlet and armlets, ornate orange-brown dhoti; stable build and costume.

The authenticated UI automation entered the packet, uploaded the approved local reference, selected it in the media picker, attached it to the Element, and clicked **Create** once. Higgsfield showed `Element created.` and returned to the library. The accessibility record verifies `@Lead-Vanara-Canonical-Character` labelled **Character**, alongside the squirrel and Rama cards. No media generation occurred and no generation credits were spent.

### Automation boundary learned

The installed `higgsfield` CLI is version 1.1.19. Its available commands and generation workflows do not expose Cinema Studio project or Element CRUD. `upload` creates a generic media upload, and `soul-id` manages trained identity models; neither creates a project-scoped Cinema Studio Element card. Therefore:

1. Use the CLI for supported generation, upload, account/model inspection, Soul, and workflow operations.
2. Use the authenticated Cinema Studio UI (manually or through UI automation) for **Elements** until Higgsfield exposes an official Element command/API.
3. Never report a generic CLI upload as an Element creation.

## Step 13 - Generate the canonical baby-vanara reference

**Status:** Complete and human-approved on 2026-07-22
**Observed:** 2026-07-22 from `assets/characters/vanara_baby_ref.png`.

The user authorized creation with the project-local `chatgpt-imagegen` workflow. This route used the authenticated `codex` backend and ChatGPT/Codex subscription quota, not Higgsfield credits. The lead-vanara reference was supplied as a species, realism, palette, and costume-language reference rather than as the baby’s identity.

### Generation packet

- Output: `assets/characters/vanara_baby_ref.png`
- Size: `1024x1536` PNG
- Quality reported by the tool: **medium**
- Reference: `assets/characters/vanara_lead_ref.png`
- Backend: `codex`
- Final prompt:

  > Use the image_generation tool to render a canonical full-body character reference for a juvenile baby vanara in the same grounded photoreal mythological world, species design, natural fur realism, warm coastal palette, and restrained ancient-Indian costume language as the reference image. The baby vanara is small and childlike but anatomically believable, with warm tawny-brown fur, a gentle rounded ape-like face, bright dark eyes, a long tail, a carefree neutral expression, a simple ochre dhoti, and only minimal gold wrist and ankle ornaments; standing naturally with the entire body, hands, feet, and tail visible against an uncluttered softly lit warm neutral coastal backdrop. Identity reference only: no stone, no action pose, no exaggerated muscles, no adult proportions, no crown, no weapons, no text, no watermark, no extra characters.

Visual review confirmed juvenile proportions, one complete tail, visible hands and feet, photoreal fur, the warm coastal palette, compatible ochre-gold costume language, and no stone, text, watermark, weapon, or extra character. The image is suitable as an identity reference; the human operator should still approve the final face and costume before production shots rely on it.

## Step 14 - Create the canonical baby-vanara Character

**Status:** Complete
**Observed:** 2026-07-22 from `031-baby-vanara-element-created.png`.

### One-packet setup

- Name: `Baby-Vanara-Canonical-Character`
- Category: **Character**
- Media: `assets/characters/vanara_baby_ref.png`
- Description (168 characters):

  > Baby vanara: small childlike build, warm tawny-brown fur, rounded ape-like face, large dark eyes, long tail, simple ochre dhoti, minimal gold wrist and ankle ornaments.

Authenticated UI automation entered the packet, uploaded and attached the generated reference, and clicked **Create** once. Higgsfield showed `Element created.` and returned to the project library. The accessibility record verifies `@Baby-Vanara-Canonical-Character` labelled **Character**, alongside lead vanara, squirrel, and Rama. No Higgsfield generation occurred and no Higgsfield credits were spent.

## Step 15 - Derive clean bridge-state Location plates

**Status:** Complete
**Observed:** 2026-07-22 from the saved files and visual inspection.

The three bridge-state source frames contained baked-in vanaras or workers, so they were not safe reusable Location references. Image editing produced separate, character-free portrait plates while preserving the original source files:

| Bridge state | Clean Location plate | Dimensions | Verification |
|---|---|---|---|
| Early / first stones | `assets/environments/bridge/bridge_01_first_clean_location.png` | 941×1672, near-native 9:16 | No characters remain |
| Half-built | `assets/environments/bridge/bridge_02_half_clean_location.png` | 941×1672, near-native 9:16 | A second cleanup pass removed the final tiny silhouette; no characters remain |
| Complete | `assets/environments/bridge/bridge_03_complete_clean_location.png` | 941×1672, near-native 9:16 | No characters or flags remain |

These are Location references, not exact 9:16 start/end frames. Preserve the originals as provenance; never overwrite a source when removing baked-in subjects.

## Step 16 - Register all bridge-state Location Elements

**Status:** Complete
**Observed:** 2026-07-22 from `032-location-elements-complete.jpg` and the live accessibility record.

The human operator created `@Ram-Setu-Shoreline-Canonical-Location` from `bridge_00_empty.png`. Authenticated UI automation then registered the three clean bridge plates as explicit **Location** Elements:

| Element handle | Media | Compact description |
|---|---|---|
| `@Ram-Setu-Bridge-Early-Location` | `bridge_01_first_clean_location.png` | Early Ram Setu construction: first weathered stone blocks extending from a rocky shore into the sea, distant island, warm golden low sun and god rays. |
| `@Ram-Setu-Bridge-HalfBuilt-Location` | `bridge_02_half_clean_location.png` | Half-built Ram Setu: twin rows of massive weathered stone blocks with a central pebble channel, ocean and distant island under warm golden god rays. |
| `@Ram-Setu-Bridge-Complete-Location` | `bridge_03_complete_clean_location.png` | Completed Ram Setu: continuous weathered stone causeway reaching a distant island across the sea, warm golden low sun, dramatic clouds and god rays. |

### Confirmed repeatable UI procedure

1. In **Elements**, select the Ramayana project and click **New Element**.
2. Enter the stable name and compact location-only description. With UI automation, wait about 600 ms after typing before reading or clicking again because the web fields update asynchronously.
3. Open **Category** and click the visible **Location** menu item. Confirm the closed field reads `Location`; keyboard-selection experiments could return the field to `Auto`.
4. Click **Upload media**, then the upload tile. In the native file dialog, enter the clean filename and open it.
5. Wait for the media grid to refresh. Higgsfield can preserve selections from earlier picker sessions, so deselect unrelated thumbnails and require exactly **1 selected**.
6. Click **Add to Element** and verify that the intended clean plate appears in the form preview.
7. Click **Create** once and wait for `Element created.` plus the new card in the library. Do not double-submit.

Automation must refresh the accessibility tree after every modal or menu transition; stale element indexes are not reliable. The installed CLI still exposes no Cinema Studio Element CRUD, so authenticated UI automation is the supported automation path discovered in this environment.

The verified library now contains four Locations and four Characters. No Prop Elements were created: Rama's bow remains in his Character reference; pebbles and boulders remain prompt-level objects; the `राम` inscription and ZebPay logo remain deterministic post-production assets. No Higgsfield video generation occurred and no Higgsfield generation credits were spent.

## Step 17 - Stage S1-a v002 and stop before Generate

**Status:** Complete through paid-action checkpoint
**Observed:** 2026-07-22 from the authenticated Brave project and `033-s1a-v002-staged.png`.

### Avoid the asset-detail routing trap

Do not use **Turn to video** from the uploaded start-frame asset detail for this Cinema Studio packet. In the observed UI, that action opened a generic video composer and changed the model to Kling 2.6. Return to the project composer, explicitly select **Cinema Studio 3.5**, and attach the start frame through the composer's add/upload picker instead.

### Confirmed staging procedure

1. Open the project's **All assets** video composer and explicitly select **Cinema Studio 3.5** before attaching references.
2. Use the composer's add control, open **Uploads**, and choose `S1-a_9x16_1080x1920.png` as the start frame.
3. If Higgsfield offers **Check eligibility**, run it once and wait for the asset to pass. Reusable Elements may require the same one-time check on first use.
4. Attach `@Rama-Canonical-Character` and `@Ram-Setu-Shoreline-Canonical-Location`; confirm all three thumbnails remain visible.
5. Select **Epic**. Enable **Manual** Style and paste the locked block from `global-visual-law.md` unchanged.
6. Set Camera to **Fine Film / Clinical Sharp / 35 mm / f/11 Deep Focus**.
7. Enter the exact 244-character prompt from `footage/generated/S1-a_v002.md`.
8. Set **9:16 / 1080p / 10s / `1/4` / Sound On**. Duration is a slider: click the desired increment and verify the bottom label. Do not type into it as though it were a text field.
9. Read the Generate button only after every control is set. At this checkpoint it showed **100 credits**, discounted from 120, while the site banner showed a 30% offer.
10. Capture the state, stop, and obtain immediate human approval. Do not press **Generate** during staging.

### Confirmed result

Screen 033 records the exact start frame, two eligible Elements, prompt, creative controls, 9:16, 1080p, 10 seconds, one candidate, Sound On, and the 100-credit live price. The staging run stopped before Generate; no credits were spent at this step. Submission occurred only after the later approval recorded in Step 18.

## Step 18 - Submit, verify, download, and review S1-a v002

**Status:** Complete; take rejected at keeper gate
**Observed:** 2026-07-22 from the authenticated project, Higgsfield CLI job/account records, downloaded media, and local QC evidence.

### Approved submission

1. Recheck that the Step 17 composer state and 100-credit price are unchanged.
2. Obtain immediate human approval for this exact job.
3. Click **Generate** exactly once.
4. Do not click Generate again merely because the form or yellow button remains visible. In the observed UI, the composer remained on screen after submission.
5. Verify submission independently: the project asset count increased from one to two and the new item showed **Processing**. The CLI job list then exposed job `75e86d55-60de-4415-9a52-1b973498dcd9`.

This double-check is the duplicate-spend guard. A visible composer is not proof that the first click failed; a new Processing asset or job ID is authoritative.

### Completion and cost verification

- Job type: `cinematic_studio_video_3_5`.
- State sequence: queued -> in progress -> completed.
- The account transaction ledger records exactly one 100-credit `Cinematic Studio 3.5 Video` spend at `2026-07-22T15:24:17.420565Z`.
- Post-run balance: 4019.03 credits.
- No second candidate or retry was submitted.

### Download and review result

The completed clip was saved as `footage/generated/S1-a_v002_cinema35_1080p_sound.mp4`; its native track was extracted to `audio/sfx/generated/S1-a_v002_native.wav`. FFprobe confirmed H.264 at 1080x1920/24 fps with stereo AAC audio and a 10.100-second duration.

The take preserved Rama's identity, hands, costume, and one bow, but a scene/background change at 6.375 seconds broke the required uninterrupted Dolly In. The take was therefore rejected and was not copied to `footage/selects/`. Full evidence and the audio-listen hold are in `review/S1-a_v002-review.md`.

## Step 19 - Stage K01 v001 with actual Seedance 2.0 at 480p

**Status:** Complete through paid-action checkpoint
**Observed:** 2026-07-23 from the authenticated Brave project, live accessibility state, CLI schema/cost checks, and `034-k01-v001-seedance-staged-480p.png`.

### Engine and workspace distinction

Cinema Studio is the project workspace. `Cinema Studio 3.5` and `Seedance 2.0` are separate engines inside its model picker. For the locked experiment, choose the Featured **Seedance 2.0** entry. Do not leave the engine at Cinema Studio 3.5, and do not substitute Seedance 2.0 Fast or Mini.

Switching engines cleared the prompt and reusable Elements but retained the previously attached start image. Always audit and remove any stale frame after an engine change before staging a new packet.

### Confirmed Seedance staging procedure

1. In the project Video composer, select **Seedance 2.0**.
2. Remove every stale start frame, prompt, and Element. Confirm the composer is empty.
3. Open the add picker -> **Uploads** -> **Upload media**. The native Windows file picker reliably accepts a full path after `Alt+N` focuses **File name**; type the path and press Enter.
4. Wait for both upload completion and the content check. Select the newly uploaded K01 frame as the start image.
5. Open **Elements**, select `@Ram-Setu-Bridge-Early-Location`, then click the bottom **Use** action. Repeat for `@Rama-Canonical-Character`. Selecting a card alone does not attach it.
6. Confirm three thumbnails: K01 start frame, Early Bridge Location, and Rama Character.
7. Enter the locked motion-and-SFX prompt. Existing Element mentions remain visible as inline tags.
8. Set **9:16**, **480p**, **6s**, and one candidate. Keep **High** bitrate and **Sound On**. Keep **Unlimited mode Off** unless the live UI explicitly proves that the active bundle covers standard Seedance 2.0.
9. Duration is a slider. Click it, use Left/Right one second at a time, and verify the displayed value; direct value assignment was not reliable.
10. Read the Generate button only after every reference and control is final. K01 v001 displayed **36 crossed out / 18 credits final**.
11. Capture the staged state and stop. Obtain immediate approval for exactly one 18-credit job before clicking Generate.

The Seedance 2.0 composer does not expose the Cinema Studio 3.5 Genre, Manual Style, or Camera panels. Encode the shot mood, camera behavior, continuity, and native SFX in the prompt and references. The visible Seedance controls are model, aspect ratio, quality, duration, candidate count, bitrate, Sound, Unlimited mode, and Generate.

No generation occurred during Step 19. Account balance remained unchanged and no new job ID was created.

## Step 20 - Submit the 480p Seedance motion pass safely

**Status:** Complete; eleven v004 motion cells reviewed and conformed
**Observed:** 2026-07-23 from Cinema Studio, Higgsfield CLI job/account records, downloaded outputs,
and local motion/QC evidence.

### Generic image is not a start image

K01 v001 was submitted once from the staged Step 19 UI for 18 credits. The UI upload picker sent the
approved K01 frame as a generic `image` role. Job
`fe298728-3bd0-4369-a167-bf22b3379f0e` completed, but the clip opened on an invented mostly empty
bridge and converged toward Rama/workforce late. It was rejected as `wrong-start-role`.

K01 v002 changed one control only: the same frame was submitted through the CLI's explicit
`--start-image`. Job `b503b2d0-c3c6-478f-88ba-ef4cd4b1e3bd` charged 18 credits and passed as an
editorial keeper. Use `higgsfield generate get <job-id> --json` to verify the first media record is
`"role": "start_image"`; do not infer this role from a visible thumbnail.

`start_image` is still a conditioning control, not a guaranteed pixel lock. K01 v002 preserved the
story state, identity, geography, and direction, but its first-frame SSIM against the conformed
keyframe was 0.286. Review the actual opening frame; never approve it from the request packet alone.

### Confirmed first-pass batch procedure

1. Keep a manifest row for every shot with exact prompt, conformed start frame, image references,
   duration, model, mode, aspect, resolution, bitrate, Sound state, and candidate count.
2. Run `higgsfield generate cost` on the fully referenced packet. K02-K08/K10 quoted 12 credits for
   four seconds, K09 quoted 15 for five seconds, and K14 quoted 18 for six seconds.
3. Submit only manifest rows without a persisted job ID.
4. Persist the returned job ID and actual account delta immediately after each `generate create`.
5. The observed account limit is eight concurrent `seedance_2_0` jobs. When K09 occupied the eighth
   slot, K10/K14 returned `rate_limit_reached` before job creation or charge. Wait for one active job
   to finish, then submit only those two missing rows.
6. Poll by job ID, download immutable raw media, extract the native WAV, build a contact sheet, and
   classify the take before promotion.
7. Copy only reviewed keeper bytes to `footage/selects/`; verify the raw/select hashes match.

The K02-K10/K14 batch charged exactly its 129-credit preflight cap. Including rejected K01 v001 and
accepted K01 v002, the complete new short-v004 learning/production spend was 165 credits. The
post-pass account balance was 3854.03.

### Output and editorial findings

- The `480p` outputs decoded as H.264 496x864 at 24 fps with stereo 44.1 kHz AAC.
- No K02-K10/K14 take produced a scene hit above the 0.35 cut-detection threshold.
- Ten motion cells were full keepers.
- K03 preserved the pebble only through its opening 0.00-1.50 seconds. The edit uses that valid
  range slowed to two seconds and holds the last valid frame for the remainder, avoiding a blind
  reroll.
- Seedance-native audio remained separate from narration and was mixed as shot-local ambience with
  30 ms boundary fades.

Review evidence is in `review/short-v004-motion-first-pass-review.md`; final conform and QC are in
`review/final-short-v003-qc.md`.

## Confirmed map of the project screen

The following controls were verified in the authenticated Brave `MythyaVerse` profile on 2026-07-21. The evidence set is indexed in `higgsfield-cinema-navigation-screens/README.md`.

### Left project navigation

| Control | Confirmed visual state | Working interpretation |
|---|---|---|
| All assets | Selected | Project-wide media/generation view |
| Project brief | Available and inspected | Structured production brief with inline-autosaving blocks for description, Context, Narrative, Visuals, Production, Status, Resources, and Notes |
| Elements | Available and inspected | Opens a modal, project-scoped reusable library with Create Element, Browse all elements, project navigation, pinned items, filtering, and search |
| Canvas | Inspected | Opens a split project canvas with Select, Pan, Draw, Sticky Note, Shape, Text, Arrow, Reaction, Comment, Folder, Add node, zoom, minimap, home, menu, full-view, and close controls |
| Chat | Inspected | Opens the project member chat with Start call, message field, attachment/add control, send control, and Close chat; no call or message was started |
| AI Director | Inspected | Opens an assistant panel with Pick a camera, Set up my look, Write my prompt, Break down my scene, a scene field, image attachment, and send; no request was submitted |
| Add folder | Visible below “Folders” | State-changing organization control; human approval required before use |
| Getting Started | Existing folder | Default project folder |

### Main composer

| Control | Visible state | Production implication |
|---|---|---|
| Mode | Video selected; Image also available | We are on the video-generation surface |
| Engine | Cinema Studio 3.5 | Correct Cinema Studio version for this runbook |
| Genre | General | Menu choices verified: General, Action, Horror, Comedy, Noir, Drama, Epic |
| Style | Auto | Three-part Style Settings system: Color Palette, Lighting, and Camera Moveset Style; Manual Style is Off |
| Camera | Auto | Four-part Camera Settings system: Camera, Lens, Focal Length, and Aperture |
| Prompt field | Empty; mentions `@` for characters and locations | References can be called from the prompt after Elements are built |
| Aspect ratio | Auto | Menu choices verified: Auto, 1:1, 3:4, 9:16, 4:3, 16:9, 21:9 |
| Quality | 1080p | Menu choices verified: 480p, 720p, 1080p, 4k; availability/cost may depend on model and plan |
| Duration | 8s | Opens a slider; live accessibility did not expose its minimum or maximum, so do not infer the range |
| Shot counter | `1/4` | One internal shot currently selected; the UI exposes a maximum of four |
| Sound | On | Matches the project rule to generate diegetic SFX/ambience, not narration or score |
| Generate | Visible with a live discounted value of 80 during the mapping pass | Paid action; price is time-sensitive and must be approved live |

### Top-right project controls

`Filter`, `View`, project members, `Upload`, and `Share` are visible.

- **Filter** was inspected. Type filters are All, Image, Video, PDF, TXT, MD, HTML, DOCX, and PPTX. Date filters are All period, Today, Last 7 days, Last 30 days, or a custom calendar range. Status filters are All, In progress, Needs review, and Approved. Activity filters are All, Generated, Uploaded, Liked, and Downloaded.
- **View** was inspected. Layout choices are Square and Masonry, with a Card size slider; Masonry was selected in the observed state.
- **Project members** was inspected read-only and showed one owner. The visible account identity is retained only in the private screenshot evidence, not duplicated in this runbook.
- **Upload** and **Share** were deliberately not opened because they can create external or project-state changes. They remain human-action boundaries.

### Confirmed Style Settings choices

| Group | Live choices |
|---|---|
| Color Palette | Auto, Naturalistic Clean, Bleached Warm, Hyper Neon, Teal Orange Epic, Sodium Decay, Cold Steel, Bleach Bypass, Classic Bw |
| Lighting | Auto, Soft Cross, Contre Jour, Overhead Fall, Window, Practicals, Silhouette |
| Camera Moveset Style | Auto, Classic Static, Silent Machine, One Take, Epic Scale, Intimate Observer, Impossible Camera, Documentary Snap, Raw Chaos, Dreamy Flow |

### Confirmed Camera Settings choices

| Group | Live choices |
|---|---|
| Camera | Auto, Raw 16mm, Fine Film, Clean Digital |
| Lens | Auto, Clinical Sharp, Extreme Macro, Anamorphic, Warm Halation, Vintage Haze |
| Focal Length | Auto, 75 mm, 50 mm, 35 mm, 14 mm, 8 mm |
| Aperture | Auto, f/11 Deep Focus, f/1.4 Wide Open, f/4 Moderate |

### Confirmed model selector

The current selection is **Cinema Studio 3.5**. The live selector also exposed Cinema Studio 3.0, Cinema Studio 2.5, Seedance 2.0, Seedance 2.0 Mini, Seedance 2.0 Fast, Gemini Omni Flash, Kling 3.0, Kling 3.0 Turbo, Kling 3.0 Motion Control, HappyHorse, Grok Imagine, Grok Imagine 1.5, Google Veo 3.1 Lite, and Wan 2.7. It also exposed model-family routes for Minimax Hailuo, Kling, OpenAI Sora 2, Google Veo, Higgsfield, Wan, Seedance, Grok Imagine, and HappyHorse. Treat model availability, resolution, duration, and cost as live data that must be rechecked before every paid run.

## Human-action boundary for the generation phase

The mapping pass authorizes read-only navigation and reversible menu inspection only. The human operator must explicitly approve or perform these actions:

- upload any character, location, prop, keyframe, or previous-video reference;
- press **Create** for an Element;
- change sharing or project membership;
- create or delete folders or projects;
- start a call or send Chat/AI Director messages;
- press **Generate** or take any action that can spend credits;
- approve the exact prompt, references, model, aspect ratio, resolution, duration, shot count, Sound state, and displayed cost immediately before generation.

During the mapping pass, an exploratory click briefly selected **Naturalistic Clean** in Style Settings. It was immediately restored to **Auto**. `025-final-neutral-composer.png` verifies the final neutral state: General / Auto / Auto / Cinema Studio 3.5 / Auto aspect ratio / 1080p / 8s / 1 of 4 / Sound On, with an empty prompt.

## Planned setup sequence

1. **Complete:** Project Brief is populated and autosaved.
2. **Complete:** `Rama-Canonical-Character` was created from `assets/characters/rama_ref.png`; screen 028 confirms its Character card.
3. **Complete:** `Squirrel-Canonical-Character` and `Lead-Vanara-Canonical-Character` were created from their approved references; screen 030 verifies all three Character cards together.
4. **Complete and human-approved:** `vanara_baby_ref.png` was generated with `chatgpt-imagegen`, and `Baby-Vanara-Canonical-Character` was created; screen 031 verifies all four scripted Character cards. The user confirmed visual approval on 2026-07-22.
5. **Complete:** `Ram-Setu-Shoreline-Canonical-Location` plus Early, HalfBuilt, and Complete bridge Location Elements are registered from clean references; screen 032 verifies the complete four-Location/four-Character library. No Prop Elements are required before pilots.
6. **Complete:** the reusable palette, lighting law, texture, performance register, and UI encoding are locked in `global-visual-law.md`.
7. **Complete through approval checkpoint:** S1-a v002 is packeted in `../footage/generated/S1-a_v002.md` and staged with the exact prompt, references, Manual Style, camera, 9:16, 1080p, 10s, one candidate, and Sound On. Screen 033 records the live 100-credit price. Generate remains unpressed pending immediate human approval.
8. **Complete through approval checkpoint:** K01 v001 is packeted in `../footage/generated/K01_v001.md` and staged with actual Seedance 2.0, the approved K01 start frame, Early Bridge and Rama Elements, 9:16, 480p, 6s, one candidate, High bitrate, Sound On, and Unlimited Off. Screen 034 records the final 18-credit live price. Generate remains unpressed pending immediate human approval.
9. **Complete:** K01 v001 was submitted once and rejected for a generic-image role; K01 v002 used
   explicit `start_image` and became the opening keeper.
10. **Complete:** K02-K10/K14 were generated at 480p Standard within the 129-credit batch cap,
    reviewed, promoted or range-restricted, and conformed into the 52.2-second v003 delivery.

This sequence is setup-first. The normal central prompt box is not the next production step.

## Navigation and learning log

| Date | Screen/action | Evidence-backed learning | Confidence |
|---|---|---|---|
| 2026-07-21 | Cinema Studio project home | Projects expose All assets, Project brief, Elements, Canvas, Chat, AI Director, and folder organization in the left sidebar | Confirmed visually |
| 2026-07-21 | Cinema Studio 3.5 video composer | Genre, Style, and Camera are three top-level creative control pills; all currently use defaults | Confirmed visually |
| 2026-07-21 | Bottom output toolbar | 1080p, 8s, `1/4`, and Sound On are selected; Generate displays 80 on this configuration | Confirmed visually; cost is time-sensitive |
| 2026-07-21 | Project identity | First screenshot appeared to omit the final “a” in “Ramayana”; this triggered a name-normalization check | Confirmed visually; later resolved |
| 2026-07-21 | Project **Actions** menu | Menu contains Pin, Edit, Add folder, Copy link, and Delete, in that order | Confirmed visually |
| 2026-07-21 | Project identity correction | Human operator confirmed the name was updated; sidebar now begins `Ramayana-Zebp...` | Confirmed by operator and screenshot |
| 2026-07-21 | Project Brief navigation | Clicking Project brief opens a structured page with a summary plus Context, Narrative, Visuals, Production, Status, Resources, and Notes | Confirmed visually |
| 2026-07-21 | Project Brief editing controls | No global Edit or Save control is visible in the resting screen state; inline-edit and persistence behavior remain unknown | Confirmed visually / behavior unverified |
| 2026-07-21 | Short-description block | Clicking the text places a caret inline and reveals a plus control plus a six-dot block handle; no modal or global Save/Cancel appears | Confirmed visually |
| 2026-07-21 | Project Brief persistence | Text remains after focus leaves the block and the operator confirms autosave; no Save button is required | Confirmed visually and by operator |
| 2026-07-21 | Project Brief timestamp | The displayed update time did not visibly change in the supplied before/after screens | Confirmed visually; do not treat as the sole save signal |
| 2026-07-21 | Repeated Project Brief fields | Once inline autosave is proven, all remaining homologous text fields can be populated as one batch with one final verification | Confirmed workflow; avoids redundant evidence |
| 2026-07-21 | Project Brief completion | Human operator confirmed all seven remaining fields were populated and autosaved | Confirmed by operator |
| 2026-07-21 | Elements navigation | Elements opens as a modal library; the current Ramayana project is selected and has no Elements yet | Confirmed visually |
| 2026-07-21 | Elements empty state | Create Element is the primary custom-asset path; Browse all elements is a separate discovery/library path | Confirmed visually |
| 2026-07-21 | New Element form | The form exposes name, description, Category (default Auto), media upload, Cancel, and Create; no cost is shown | Confirmed visually |
| 2026-07-21 | Element categories | The live dropdown contains Auto, Character, Location, and Prop | Confirmed visually |
| 2026-07-21 | Authenticated Brave navigation pass | Project pages, creative controls, model selector, output controls, asset filters/view, folder controls, and project-member surface were mapped without creating or generating assets | Confirmed by screens 001–024 |
| 2026-07-21 | Neutral-state verification | Composer ended at General / Style Auto / Camera Auto / Cinema Studio 3.5 / aspect Auto / 1080p / 8s / 1 of 4 / Sound On with an empty prompt | Confirmed by screen 025 |
| 2026-07-21 | Rama Element setup | `Rama-Canonical-Character` is categorized as Character and `rama_ref.png` is loaded; description and Create remain pending | Confirmed by screen 026 |
| 2026-07-22 | Element description truncation | The 563-character Rama draft was reported to truncate near its first `tilak`; replace it with the 175-character identity lock and treat the exact field cap as unverified | Confirmed by human operator; exact cap unknown |
| 2026-07-22 | Rama pre-submission checkpoint | The compact identity description is entered with its final `bow.` visible; the reference, Character category, and name are present; Create is authorized but not yet pressed | Confirmed by screen 027 |
| 2026-07-22 | Rama Element created | Elements library displays the new Rama Character card; the visible `@` label is truncated and hover exposes an untested `Check eligibility` action | Confirmed by screen 028 |
| 2026-07-22 | Squirrel Element setup | `Squirrel-Canonical-Character` is categorized as Character and `squirrel_ref.png` is loaded; the repeated workflow is now delivered as one complete packet | Confirmed by screen 029 |
| 2026-07-22 | CLI capability check | Higgsfield CLI 1.1.19 has no Cinema Studio project/Element CRUD; generic upload and Soul commands are not Element creation | Confirmed from installed CLI command and workflow inventory |
| 2026-07-22 | Character Element automation | Authenticated UI automation created the squirrel and lead-vanara cards from approved local references; the library verifies Rama, squirrel, and lead vanara as Character Elements | Confirmed by screen 030 and live accessibility record |
| 2026-07-22 | Baby vanara inventory | The script calls for a baby vanara, but no approved baby-vanara reference is present in `assets/characters/`; its Element is deferred rather than invented | Confirmed from project asset inventory |
| 2026-07-22 | Baby vanara reference generation | `chatgpt-imagegen` created `vanara_baby_ref.png` at 1024x1536 using the lead vanara as a world/species reference; visual review passed and the user approved it | Confirmed from saved PNG, tool result, and user sign-off |
| 2026-07-22 | Baby vanara Element created | The library displays `@Baby-Vanara-Canonical-Character` labelled Character alongside lead vanara, squirrel, and Rama | Confirmed by screen 031 and live accessibility record |
| 2026-07-22 | Clean bridge Location plates | Image editing produced three separate 941×1672 character-free Location references while preserving every original bridge-state source | Confirmed from the saved PNGs and visual inspection |
| 2026-07-22 | Category selection under automation | Clicking the visible `Location` menu item and confirming the closed field is reliable; keyboard selection can appear checked yet return to `Auto` | Confirmed in the final Complete-Location registration |
| 2026-07-22 | Element media picker | Media selections can persist between sessions; require exactly `1 selected` before **Add to Element** | Confirmed across the three Location registrations |
| 2026-07-22 | Location Element automation | Authenticated UI automation created Early, HalfBuilt, and Complete Locations from the clean plates; the library now contains four Locations and four Characters | Confirmed by screen 032 and live accessibility record |
| 2026-07-22 | Global visual-law lock | Palette, motivated-light rule, tactile material treatment, contained performance register, and deterministic-post text rule were consolidated into one reusable 899-character Manual Style block | Confirmed in `global-visual-law.md`; output validation pending |
| 2026-07-22 | S1-a source preflight | The original is 941×1672, effectively but not mathematically exact 9:16; a non-destructive Lanczos conform was created at 1080×1920 | Confirmed by FFprobe and `keyframes/conformed/S1-a_9x16_1080x1920.png` |
| 2026-07-22 | `Turn to video` asset action | Using this from the uploaded start-frame detail routed to a generic composer and changed the model to Kling 2.6; the correct Cinema Studio path is project composer -> Cinema Studio 3.5 -> add/upload picker | Confirmed live; recovered without generation |
| 2026-07-22 | Reference eligibility | The exact start frame and each reusable Element can require a one-time eligibility check before they become attachable | Confirmed for the S1-a frame, Rama, and Shoreline |
| 2026-07-22 | Duration control | Duration is a slider, not a dependable text field; use the slider and verify the bottom label after every change | Confirmed while setting 8s -> 9s -> 10s |
| 2026-07-22 | S1-a v002 staged checkpoint | Cinema Studio 3.5 / Epic / Manual / Fine Film / Clinical Sharp / 35 mm / f/11 / 9:16 / 1080p / 10s / 1 candidate / Sound On shows a live price of 100 credits while the site banner separately shows a 30% offer | Confirmed by screen 033; Generate not pressed |
| 2026-07-23 | Engine switch in project composer | Cinema Studio is the workspace; Cinema Studio 3.5 and Seedance 2.0 are different engines. Switching to Seedance cleared prompt/Elements but retained the old start frame | Confirmed live; stale frame removed before K01 staging |
| 2026-07-23 | Seedance upload picker | In the native file dialog, `Alt+N` focuses File name; entering the full local path and pressing Enter uploads the image, followed by a separate content check | Confirmed while uploading the conformed K01 start frame |
| 2026-07-23 | Seedance Element attachment | Selecting an Element only marks it; the bottom `Use` action attaches it and inserts its inline prompt tag | Confirmed for Early Bridge and Rama |
| 2026-07-23 | Seedance duration control | The slider responds to Left/Right in one-second increments; direct accessibility value assignment was unreliable | Confirmed while changing 8s -> 7s -> 6s |
| 2026-07-23 | K01 v001 staged checkpoint | Seedance 2.0 / 9:16 / 480p / 6s / 1 candidate / High / Sound On / Unlimited Off displayed 36 crossed out and 18 credits final | Confirmed by screen 034 and live accessibility state; Generate not pressed |
| 2026-07-23 | K01 v001 submitted from UI picker | The visible uploaded frame was sent as generic `image`, not `start_image`; the take converged toward the requested composition late and was rejected | Confirmed by job params, contact sheet, first/last-frame comparison, and review |
| 2026-07-23 | K01 v002 explicit CLI start role | `--start-image` fixed the structural opening-state failure, but the resulting first frame was still a generative recomposition rather than a pixel lock | Confirmed by job media role, SSIM 0.286, contact sheet, and keeper review |
| 2026-07-23 | Seedance batch concurrency | The account accepted eight simultaneous Seedance 2.0 jobs; further requests returned `rate_limit_reached` without a job or charge | Confirmed by K09 acceptance, K10/K14 rejection, account deltas, and later clean submission |
| 2026-07-23 | Short-v004 first-pass economics | K02-K08/K10 cost 12 credits each, K09 15, K14 18; the remaining batch charged exactly 129 credits | Confirmed by fully referenced quotes and account ledger |
| 2026-07-23 | 480p output characteristics | Requested `480p` Seedance files decoded as 496x864 H.264/24 fps with stereo 44.1 kHz AAC | Confirmed by FFprobe across K02-K10/K14 |
| 2026-07-23 | Partial-keeper editorial repair | K03's valid 0.00-1.50-second pebble-carry range can be slowed and held to fill its locked cell without using later disappearing-object frames | Confirmed by detail audit, 120-frame conform, and final boundary review |

## Related production documents

- `higgsfield-manual-generation-operating-spec.md` — authoritative generation method and review gates.
- `brief.md` — local creative brief.
- `production-decisions.md` — accepted production decisions.
- `../../.agent-harness/recipes/ramayana-higgsfield-manual-generation.md` — repeatable operator recipe.
