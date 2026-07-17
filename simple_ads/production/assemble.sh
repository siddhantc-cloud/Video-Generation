#!/usr/bin/env bash
cd /d/startup_dev/so_sorry/simple_ads/production
CLIPS="s1_veo_hindi.mp4 s2_veo.mp4 s3_veo.mp4 s4_veo.mp4 s5_veo.mp4 s6_veo.mp4 s7_veo.mp4 s8_veo.mp4"
i=0; : > concat.txt
for c in $CLIPS; do
  i=$((i+1)); seg=$(printf "seg_%02d.mp4" $i)
  # normalize to identical params for a clean concat (clips already 1080x1920/24fps)
  ffmpeg -y -loglevel error -i "$c" -r 24 \
    -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1" \
    -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \
    -c:a aac -ar 48000 -ac 2 -b:a 192k "$seg"
  echo "file '$seg'" >> concat.txt
done
ffmpeg -y -loglevel error -f concat -safe 0 -i concat.txt -c copy clear_gut_ad_FINAL.mp4
echo "duration: $(ffprobe -v error -show_entries format=duration -of csv=p=0 clear_gut_ad_FINAL.mp4)s"
echo "DONE"
