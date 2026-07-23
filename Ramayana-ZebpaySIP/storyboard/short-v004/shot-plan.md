# Short animatic v004 — phrase-locked visual plan

## Production checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Narration master | One continuous scratch narration and word-boundary JSON exist | `edit/audio/animatic-short-v004/` | Editor | Complete |
| Phrase lock | Each cut starts on the first word of its matching phrase, within one frame | v004 visual EDL | Editor | Complete |
| Continuity | Rama, squirrel, lead vanara, and bridge stage match canonical references | Keyframe contact sheet and continuity review | Image/Continuity | Complete |
| Visual quality | Frames are grounded, tactile, varied in scale, and free of generated text | Keyframe review | Creative/Human | Self-review pass; human pending |
| SIP metaphor | Regular contributions remain visually steady through an up/down path without promises | Motion-graphic review | Editor/Brand | Complete |
| Deterministic brand | All copy and the ZebPay logo are added in post | End-card source and render | Editor | Complete |
| Cost | No Higgsfield credits are used for v004 | Generation log | Editor | Locked |

## Locked visual law

- Native intent: vertical 9:16 social film; compose important action inside the center-safe crop.
- Finish: grounded photoreal coastal epic, tactile stone/cloth/fur/skin, fine film grain, controlled
  highlights, true blacks, muted earths, restrained amber, salt haze, and motivated natural light.
- Direction: vary shot scale and weather; do not repeat a centered poster portrait.
- Continuity: use only the canonical characters actually visible in a shot and the matching clean
  bridge stage. References lock identity and geography; they do not lock the old framing.
- Hard negatives: no generated words, logos, captions, watermarks, modern objects, plastic CGI,
  oversmoothed skin/fur, duplicate characters, extra limbs, warped hands, or devotional glow effects.
- Rama is reverent and observant, the squirrel is determined rather than cute/comic, and mockery is
  shown without humiliation or slapstick.

## Phrase-level beats

| ID | Narration phrase that owns the cut | Designed image/action | Reference assets | Transition rule | Status |
|---|---|---|---|---|---|
| K01 | “An army of vanaras was building Ram Setu, boulder by boulder.” | Epic high-wide coastal construction: many vanaras moving differently scaled stones along the first bridge stage; Rama is a small, calm witness rather than a poster hero | `rama_ref.png`, `bridge_01_first_clean_location.png` | Film opens here; hold across the whole sentence | Complete |
| K02 | “At the edge of the shore,” | Ground-level scale reveal: tiny squirrel in the lower foreground, enormous wet stones and working vanaras receding behind it | `squirrel_ref.png`, `bridge_01_first_clean_location.png` | Cut on “At” | Complete after one corrective regeneration |
| K03 | “a tiny squirrel carried one pebble at a time.” | Intimate side-tracking composition of the squirrel carrying a single pebble toward a real gap; paws planted, pebble clearly readable | `squirrel_ref.png`, `bridge_01_first_clean_location.png` | Cut on “a tiny” | Complete |
| K04 | “The others laughed.” | Low squirrel eyeline toward the lead vanara and two background workers; lead vanara shows restrained disbelief while balancing a huge stone | `squirrel_ref.png`, `vanara_lead_ref.png`, `bridge_02_half_clean_location.png` | Cut on “The” | Complete |
| K05 | “What difference could something so small make?” | Extreme scale contrast: tiny pebble and squirrel in crisp foreground; massive boulder and vanara legs cross the background | `squirrel_ref.png`, `bridge_02_half_clean_location.png` | Cut on “What” | Complete |
| K06 | “But Rama saw what they missed.” | Emotional two-shot: Rama kneels at the squirrel’s level, both in profile, eye-lines meeting; no pickup and no difficult hand contact | `rama_tender.png`, `squirrel_ref.png`, `bridge_02_half_clean_location.png` | Cut on “But”; hold through the sentence | Complete |
| K07 | “The squirrel kept showing up, whether the tide was calm” | Cool early-morning return: squirrel moving along the same bridge seam with a pebble; quiet water and soft haze | `squirrel_ref.png`, `bridge_02_half_clean_location.png` | Cut on “The squirrel” | Complete |
| K08 | “or rough.” | Same geography and direction of travel under hard rain, spray, and a rough tide; squirrel remains grounded and determined | `squirrel_ref.png`, `bridge_02_half_clean_location.png` | Cut exactly on “or” | Complete |
| K09 | “And with every return, another gap was filled.” | Macro structural payoff: a line of small pebbles tightly fills a visible joint between giant stones; squirrel present at frame edge, not anthropomorphic paw-work | `squirrel_ref.png`, `bridge_02_half_clean_location.png` | Cut on “And”; optional gentle push-in | Complete |
| K10 | “Investing can work the same way.” | Visual bridge between story and explanation: repeated pebbles form a calm rhythmic path along the causeway, leaving clean negative space for restrained post graphics | `bridge_03_complete_clean_location.png` | Cut on “Investing” | Complete |
| G11 | “You do not need to predict the perfect market moment.” | Over K10, an elegant cobalt path rises and falls like tide/market movement while equal contribution markers continue at fixed intervals | Official brand palette; no generated imagery required | Reveal begins on “predict”; no wordy card | Complete |
| G12 | “A SIP lets you invest the same amount regularly,” | The equal markers continue with identical size and spacing; one concise deterministic label may appear only if needed for comprehension | Official brand palette | State change on “same amount regularly” | Complete |
| G13 | “through the ups and downs.” | The path moves down and up while the contribution rhythm remains unchanged; no return arrow, rupee growth, or implied outcome | Official brand palette | State change on “through” | Complete |
| K14 | “Small steps, repeated consistently, can build something bigger.” | Earned hero wide: squirrel on a foreground stone, the completed bridge stretching through soft dawn haze; large human-scale world, small subject, no triumphant fantasy rays | `squirrel_ref.png`, `bridge_03_complete_clean_location.png` | Cut on “Small”; hold to CTA | Complete |
| G15 | “Start your SIP with ZebPay.” | Premium deterministic end card using the official ZebPay logo, one CTA, generous negative space, and no unsupported claims | `assets/brand/zebpay_logo.png` | Cut on “Start”; final hold at least one second | Complete |

## Image-generation order

1. Lock four representative frames first: K01 wide, K03 squirrel action, K06 recognition, K08 rough
   persistence.
2. Review identity, geography, lighting, realism, and center-safe 9:16 composition.
3. Generate K02, K04, K05, K07, K09, K10, and K14 only after the look lock passes.
4. Reject variants that merely repeat the canonical reference framing. References are continuity
   anchors, not finished storyboards.

## Verified timing map

The scratch performance is one 51.792-second audio file. The v004 picture timeline is 1,566 frames
(52.200 seconds) at 30 fps, which leaves 1.380 seconds after the final spoken word for the end-card
hold. Cut frames are the nearest whole frame to the matching Edge TTS word boundary.

| Beat | First word | Boundary | Cut frame | Timeline time | Difference from word boundary |
|---|---|---:|---:|---:|---:|
| K01 | An | 0.102 s | 0 | 0.000 s | Opening pre-roll |
| K02 | At | 5.872 s | 176 | 5.867 s | -0.005 s |
| K03 | a | 7.773 s | 233 | 7.767 s | -0.006 s |
| K04 | The | 11.758 s | 353 | 11.767 s | +0.009 s |
| K05 | What | 13.880 s | 416 | 13.867 s | -0.013 s |
| K06 | But | 17.500 s | 525 | 17.500 s | 0.000 s |
| K07 | The | 20.260 s | 608 | 20.267 s | +0.007 s |
| K08 | or | 23.828 s | 715 | 23.833 s | +0.005 s |
| K09 | And | 25.391 s | 762 | 25.400 s | +0.009 s |
| K10 | Investing | 29.714 s | 891 | 29.700 s | -0.014 s |
| G11 | You | 32.760 s | 983 | 32.767 s | +0.007 s |
| G12 | A | 37.201 s | 1116 | 37.200 s | -0.001 s |
| G13 | through | 40.925 s | 1228 | 40.933 s | +0.008 s |
| K14 | Small | 43.398 s | 1302 | 43.400 s | +0.002 s |
| G15 | Start | 48.867 s | 1466 | 48.867 s | 0.000 s |

## Why this is better than v003

The narration remains unchanged, so the comparison is fair. What changes is the directing logic:
fewer arbitrary cuts, exact phrase ownership, intentional coverage, a coherent environmental arc from
warm workday to cool calm to rough weather to soft dawn, and a single visual analogy that connects
pebbles to regular investment without becoming a slideshow.
