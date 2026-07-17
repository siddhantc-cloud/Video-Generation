#!/usr/bin/env bash
cd /d/startup_dev/so_sorry/simple_ads/production
STYLE='3D animated caricature advertisement style, glossy Pixar/DreamWorks render, exaggerated expressive cartoon features, cinematic dramatic rim lighting, vibrant saturated colors, vertical 9:16, murky stylized human-body-interior cave with pinkish organic tissue ground and sickly-green gas wisps. ABSOLUTELY NO TEXT, no letters, no captions anywhere.'
# consistent hero designs (reused across scenes)
AMLA='the hero BHUI AMLA — a heroic glowing pale-green gooseberry character, round translucent green fruit body with faint vertical ridges, determined confident face, small muscular arms, a tiny green leaf sprout on top, soft golden healing glow'
AJWAIN='the hero AJWAIN — a feisty small carom-seed warrior, ridged tan-and-green oval seed body, spiky energetic posture, fierce grin, quick fighter stance'
SAUNF='the hero SAUNF — a graceful fennel-seed warrior, slender pale-green ridged body with feathery fennel fronds like hair, cool confident expression'
HARITAKI='the hero HARITAKI — an ancient wise myrobalan-fruit warrior, oval ribbed amber-brown body, glowing eyes, weathered powerful elder look, crackling golden thunder energy'
VILLAIN='the CONSTIPATION KING villain (crowned brown sludge-monster) and the sad pink anthropomorphized stomach character, matching the reference image'

gen(){ # outfile  prompt  refs...
  local out="$1"; shift; local prompt="$1"; shift
  echo "### $out"
  higgsfield generate create nano_banana_2 --prompt "$prompt" "$@" \
    --aspect_ratio 9:16 --resolution 2k --wait --json 2>&1 | grep -o '"result_url": "[^"]*"' | head -1
}

gen s2_key "$STYLE $AMLA crashes into frame in a heroic entry pose, confronting $VILLAIN who reacts with annoyance at the top; the pink stomach watches with hope. Amla is the main focus, lower-center." --image ./s1_keyframe_clean.png
gen s3_key "$STYLE $AJWAIN bursts in with action-movie energy beside $AMLA, both heroes facing $VILLAIN. Two herb heroes vs the villain." --image ./s1_keyframe_clean.png
gen s4_key "$STYLE $SAUNF slides in dramatically to join $AMLA and $AJWAIN — three herb heroes standing together facing $VILLAIN who looks less confident." --image ./s1_keyframe_clean.png
gen s5_key "$STYLE $HARITAKI lands with a golden thunder strike, joining the other three herb heroes; all FOUR herb heroes now assembled heroically while $VILLAIN looks worried and shrinking." --image ./s1_keyframe_clean.png
gen s6_key "$STYLE The FOUR herb heroes — $AMLA, $AJWAIN, $SAUNF, $HARITAKI — standing together in a triumphant team hero pose, glowing with power, while the Constipation King villain shrinks back in fear. Epic team shot." --image ./s1_keyframe_clean.png
gen s7_key "$STYLE More than ten glowing Ayurvedic herbs and the four heroes swirl together as streaks of golden light and MERGE into one single glowing amber glass dropper bottle of BLUMELIFE Clear Gut (matching the product reference), the bottle standing heroic and radiant in the center, triumphant golden light rays." --image ./clear_gut.png --image ./s1_keyframe_clean.png
gen s8_key "$STYLE The Constipation King villain is blasted away and dissolving into green smoke at the edge; the pink stomach character is now happy, bright, healthy and energetic with a big smile; the amber BLUMELIFE Clear Gut dropper bottle (matching the product reference) stands prominent and glowing in the warm clean foreground. Victory mood, bright and uplifting." --image ./clear_gut.png --image ./s1_keyframe_clean.png
echo "ALL_KEYFRAMES_DONE"
