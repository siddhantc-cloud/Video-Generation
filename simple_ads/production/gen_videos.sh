#!/usr/bin/env bash
cd /d/startup_dev/so_sorry/simple_ads/production
STYLE='Exaggerated 3D cartoon animation, glossy Pixar-villain render, big comedic performance, expressive moving mouths, murky body-cave with swirling green gas. Camera: gentle push-in, keep characters in frame. No text.'

anim(){ # key.png  outlabel  prompt
  local key="$1"; local label="$2"; local prompt="$3"
  echo "### $label"
  higgsfield generate create veo3_1 --prompt "$prompt $STYLE" \
    --image "./$key" --duration 8 --aspect_ratio 9:16 --quality high \
    --wait --wait-timeout 15m --json 2>&1 | grep -o '"result_url": "[^"]*"' | head -1
}

anim s2_key.png S2 'Starting from the provided image as the first frame. The green gooseberry hero Bhui Amla makes a heroic entrance and speaks boldly to camera in confident Hindi, mouth moving: "रुको ज़रा! मैं हूँ भुई आँवला! मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ!" The Constipation King villain scoffs above. Audio: a bright confident heroic male Hindi voice.'
anim s3_key.png S3 'Starting from the provided image as the first frame. The carom-seed hero Ajwain bursts in with action energy and declares in punchy Hindi, mouth moving: "अकेला नहीं! मैं हूँ अजवाइन! पेट की हेविनेस से लड़ने आया हूँ!" Amla stands beside him. Audio: an energetic feisty male Hindi voice.'
anim s4_key.png S4 'Starting from the provided image as the first frame. The fennel-seed hero Saunf slides in gracefully and says coolly in Hindi, mouth moving: "और मैं हूँ सौंफ! ब्लोटिंग के ख़िलाफ़ मैं भी टीम में हूँ!" Three heroes face the villain. Audio: a smooth cool male Hindi voice.'
anim s5_key.png S5 'Starting from the provided image as the first frame. The ancient myrobalan hero Haritaki lands with golden thunder and booms in a deep wise Hindi voice, mouth moving: "मैं हूँ हरीतकी! आयुर्वेद की सबसे ट्रस्टेड हर्ब्स में से एक। गेम ओवर, किंग!" The villain recoils. Audio: a deep powerful elder male Hindi voice with thunder.'
anim s6_key.png S6 'Starting from the provided image as the first frame. The four herb heroes strike a triumphant team pose; one says with rising excitement in Hindi, mouths moving: "बस हम चार ही हैं? अब असली सरप्राइज़ देखो!" The villain shrinks in fear. Audio: confident heroic Hindi voices, epic team-up energy.'
anim s7_key.png S7 'Starting from the provided image as the first frame. Ten-plus glowing herbs swirl as golden light and merge into the radiant Clear Gut dropper bottle; a warm trustworthy narrator speaks in Hindi over the reveal: "दस से ज़्यादा आयुर्वेदिक इंग्रीडिएंट्स की पावर, अब एक ही क्लियर गट ड्रॉप में।" Audio: a warm authoritative male Hindi narrator voiceover, uplifting.'
anim s8_key.png S8 'Starting from the provided image as the first frame. The villain dissolves into green smoke, the happy glowing stomach beams, the Clear Gut bottle shines; a warm narrator delivers the CTA in Hindi: "सिर्फ़ दस-पंद्रह ड्रॉप्स, सुबह और रात। पेट हल्का, दिन हल्का।" Audio: a warm confident male Hindi narrator, bright and conclusive.'
echo "ALL_VIDEOS_DONE"
