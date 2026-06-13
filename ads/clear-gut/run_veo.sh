#!/usr/bin/env bash
cd /d/startup_dev/so_sorry/ads/clear-gut
# Pin recovered (already-paid, in-flight) job ids — never resubmit these
echo "66475254-6ab5-46ac-8695-9a8fd08115fe" > clips/s1.id
echo "cf32026b-d66a-4540-9371-d49b79ecc652" > clips/s3.id
echo "5a4c9145-fe62-470e-ab97-9ed7556bb6db" > clips/s4.id
TODO="s5 s6 s7 s8"
ALL="s1 s3 s4 s5 s6 s7 s8"

parse_id() { python -c "import json
try:
 d=json.load(open('$1',encoding='utf-8'))
 if isinstance(d,list) and d: print(d[0] if isinstance(d[0],str) else d[0].get('id',''))
 elif isinstance(d,dict): print(d.get('id',''))
 else: print('')
except Exception: print('')"; }

echo "=== SUBMIT $TODO (retry ONLY on rate_limit = not created) ==="
for s in $TODO; do
  for attempt in $(seq 1 15); do
    higgsfield generate create veo3_1 --image keyframes/${s}_start.png \
      --prompt "$(cat prompts/veo_${s}.txt)" \
      --duration 8 --aspect_ratio 9:16 --quality high --model veo-3-1-preview \
      --json > clips/${s}.create.json 2>clips/${s}.create.err
    id=$(parse_id clips/${s}.create.json)
    if [ -n "$id" ]; then echo "$id" > clips/${s}.id; echo "[submit] $s -> $id ($(date +%H:%M:%S))"; break; fi
    if grep -qi "rate_limit" clips/${s}.create.err clips/${s}.create.json 2>/dev/null; then
      echo "[$s] rate-limited (NOT created), wait 40s (try $attempt)"; sleep 40
    else
      echo "[$s] NON-rate-limit error, abort:"; head -c 250 clips/${s}.create.err clips/${s}.create.json; printf "" > clips/${s}.id; break
    fi
  done
  sleep 4
done

echo "=== POLL + download: $ALL ==="
for r in $(seq 1 90); do
  sleep 20
  higgsfield generate list --size 120 --json > clips/poll.json 2>/dev/null
  remaining=0
  for s in $ALL; do
    [ -f clips/${s}.mp4 ] && continue
    id=$(cat clips/${s}.id 2>/dev/null)
    [ -z "$id" ] && { remaining=$((remaining+1)); continue; }
    info=$(python -c "import json
try:
 d=json.load(open('clips/poll.json',encoding='utf-8')); items=d if isinstance(d,list) else []
 m=[j for j in items if isinstance(j,dict) and j.get('id')=='$id']
 print((m[0].get('status','')+'|'+(m[0].get('result_url') or '')) if m else 'notfound|')
except Exception: print('err|')" 2>/dev/null)
    status=${info%%|*}; url=${info#*|}
    if [ "$status" = "completed" ] && [ -n "$url" ]; then
      curl -sL "$url" -o clips/${s}.mp4 && echo "[done] $s ($(date +%H:%M:%S))"
    elif [ "$status" = "failed" ] || [ "$status" = "error" ]; then
      echo "[FAILED] $s status=$status"; echo FAILED > clips/${s}.failed
    else
      remaining=$((remaining+1))
    fi
  done
  echo "round $r: remaining=$remaining ($(date +%H:%M:%S))"
  [ $remaining -eq 0 ] && { echo "ALL RESOLVED"; break; }
done
echo "=== VEO BATCH COMPLETE ($(date +%H:%M:%S)) ==="; ls -la clips/*.mp4 2>/dev/null
