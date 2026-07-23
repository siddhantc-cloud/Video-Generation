#!/usr/bin/env python
"""
av_sync_render.py  -  Audio-master, frame-locked slideshow/animatic renderer.

THE GUARANTEE: the audio (narration) is the master clock. Each shot's on-screen
duration is derived from its MEASURED narration length + explicit pauses, then
QUANTIZED to a whole number of video frames. Both the video slide (exactly F
frames) and the audio segment (exactly F/fps seconds) are built from that same
integer F, so picture and narration are built from one number and cannot drift,
no matter the script or the number of shots. The tool then VERIFIES that the
final video duration equals the audio duration to within one frame, and writes
an EDL so every cut is inspectable.

Usage:  python tools/av_sync_render.py <manifest.json>

Manifest schema:
{
  "fps": 30, "resolution": [1080,1920],
  "voice": "en-IN-PrabhatNeural", "rate": "-6%",
  "default_pause_in": 0.25, "default_pause_out": 0.45,
  "kenburns": true,
  "output": "deliverables/review-cuts/animatic/OUT.mp4",
  "shots": [
    {"id":"S1-a","image":"keyframes/S1-a.png","vo":"..."},
    {"id":"S3-f","image":"...","vo":null,"hold":1.3},          # silent beat
    {"id":"S4-d","image":"...","vo":"...","pause_out":0.9}      # extra delay (a "delay where necessary")
  ]
}
"""
import json, math, os, subprocess, sys

def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    if r.returncode != 0:
        raise RuntimeError(cmd[0] + " failed: " + r.stderr.decode()[-500:])

def probe_dur(f):
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],
                       capture_output=True, text=True)
    return float(r.stdout.strip())

def probe_vframes(f):
    r = subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-count_frames",
                        "-show_entries","stream=nb_read_frames","-of","csv=p=0",f],
                       capture_output=True, text=True)
    return int(r.stdout.strip())

def tc(frames, fps):
    s, fr = divmod(int(frames), fps)
    m, s = divmod(s, 60); h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}:{fr:02d}"

def main(mpath):
    M = json.load(open(mpath, encoding="utf-8"))
    root = os.path.dirname(os.path.abspath(mpath))
    fps = int(M.get("fps", 30))
    W, H = M.get("resolution", [1080, 1920])
    voice = M.get("voice", "en-IN-PrabhatNeural"); rate = M.get("rate", "-6%")
    dpin = float(M.get("default_pause_in", 0.25)); dpout = float(M.get("default_pause_out", 0.45))
    kb = bool(M.get("kenburns", True))
    out = os.path.abspath(os.path.join(os.getcwd(), M["output"]))
    work = os.path.join(os.path.dirname(out), "_work"); os.makedirs(work, exist_ok=True)

    def split_frames(F, weights):
        # distribute F frames across len(weights) images; remainder to last; each >=1
        tot = float(sum(weights)); out = []; acc = 0
        for k, w in enumerate(weights):
            if k < len(weights) - 1:
                fk = max(1, int(round(F * w / tot))); out.append(fk); acc += fk
            else:
                out.append(max(1, F - acc))
        # if rounding overshot, trim from the largest
        while sum(out) != F:
            j = out.index(max(out)); out[j] += (1 if sum(out) < F else -1)
        return out

    edl, vlist, alist = [], [], []
    start = 0  # cumulative start frame -> the master timeline
    N = len(M["shots"])
    for i, sh in enumerate(M["shots"]):
        sid = sh["id"]
        # A line may OWN several pictures: they cut WITHIN the line so the visual is
        # always on screen while its narration is spoken (never a trailing silent beat).
        images = [os.path.abspath(x) for x in (sh.get("images") or ([sh["image"]] if sh.get("image") else []))]
        weights = sh.get("weights") or [1] * len(images)
        seg = os.path.join(work, f"{i:02d}_{sid}.wav")
        if sh.get("vo") or sh.get("vo_audio"):
            pin = float(sh.get("pause_in", dpin)); pout = float(sh.get("pause_out", dpout))
            if sh.get("vo_audio"):
                # A REAL narration track (ElevenLabs / recorded). Used as-is; still frame-locked.
                mp3 = os.path.abspath(sh["vo_audio"])
            else:
                # Free scratch TTS (Edge) for the animatic.
                mp3 = os.path.join(work, f"{i:02d}_{sid}.mp3")
                subprocess.run(["python","-m","edge_tts","--voice",voice,"--rate",rate,
                                "--text",sh["vo"],"--write-media",mp3], check=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            vod = probe_dur(mp3)
            F = math.ceil((pin + vod + pout) * fps)          # ceil: never clip the narration
            dur = F / fps
            pin_ms = int(round(pin * 1000))
            run(["ffmpeg","-y","-i",mp3,"-af",f"adelay={pin_ms}:all=1,apad",
                 "-t",f"{dur:.6f}","-ar","48000","-ac","2",seg])
        else:  # a genuine silent PAUSE (not an illustration); kept intentional
            vod, pin, pout = 0.0, 0.0, 0.0
            F = max(int(round(float(sh.get("hold", 1.3)) * fps)), fps // 2)
            dur = F / fps
            run(["ffmpeg","-y","-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-t",f"{dur:.6f}",seg])
        alist.append(seg)  # ONE audio segment spans the whole line/entry

        # A shot may be a pre-rendered VIDEO (HyperFrames/Remotion card, or a final generated
        # clip): fit it to EXACTLY F frames (clone last frame if short, trim if long), silent.
        if sh.get("video"):
            vid = os.path.abspath(sh["video"])
            slide = os.path.join(work, f"{i:02d}_{sid}.mp4")
            vf = (f"fps={fps},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
                  f"format=yuv420p,tpad=stop_mode=clone:stop_duration=3600")
            if i == N - 1: vf += f",fade=t=out:st={max(F/fps-0.6,0):.3f}:d=0.6"
            run(["ffmpeg","-y","-i",vid,"-vf",vf,"-frames:v",str(F),
                 "-c:v","libx264","-preset","veryfast","-pix_fmt","yuv420p",slide])
            vlist.append(slide)
            edl.append({"i":i,"id":sid,"vo_sec":round(vod,3),"pause_in":pin,"pause_out":pout,
                        "frames":F,"on_screen_sec":round(F/fps,3),
                        "images":[{"image":os.path.basename(vid)+" (video)","frames":F,
                                   "start":tc(start,fps),"end":tc(start+F,fps)}]})
            start += F
            continue

        subF = split_frames(F, weights)                       # frames per image, summing to F
        sub = []
        for k, (img, fk) in enumerate(zip(images, subF)):
            zin = ((i + k) % 2 == 0)
            z = "min(zoom+0.0006,1.14)" if zin else "if(eq(on,1),1.14,max(zoom-0.0006,1.0))"
            vf = (f"scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
                  f"zoompan=z='{z}':d={fk}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={fps},"
                  f"format=yuv420p") if kb else \
                 (f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},format=yuv420p")
            if i == 0 and k == 0: vf += ",fade=t=in:st=0:d=0.5"
            if i == N - 1 and k == len(images) - 1: vf += f",fade=t=out:st={max(fk/fps-0.6,0):.3f}:d=0.6"
            slide = os.path.join(work, f"{i:02d}_{k}_{sid}.mp4")
            run(["ffmpeg","-y","-loop","1","-i",img,"-r",str(fps),"-frames:v",str(fk),"-vf",vf,
                 "-c:v","libx264","-preset","veryfast","-pix_fmt","yuv420p",slide])
            vlist.append(slide)
            sub.append({"image":os.path.basename(img),"frames":fk,
                        "start":tc(start,fps),"end":tc(start+fk,fps)}); start += fk
        edl.append({"i":i,"id":sid,"vo_sec":round(vod,3),"pause_in":pin,"pause_out":pout,
                    "frames":F,"on_screen_sec":round(dur,3),"images":sub})

    vtxt = os.path.join(work,"v.txt"); atxt = os.path.join(work,"a.txt")
    open(vtxt,"w").write("".join(f"file '{p}'\n" for p in vlist))
    open(atxt,"w").write("".join(f"file '{p}'\n" for p in alist))
    vcat = os.path.join(work,"_v.mp4"); acat = os.path.join(work,"_a.wav")
    run(["ffmpeg","-y","-f","concat","-safe","0","-i",vtxt,"-c","copy",vcat])
    run(["ffmpeg","-y","-f","concat","-safe","0","-i",atxt,"-c","copy",acat])
    run(["ffmpeg","-y","-i",vcat,"-i",acat,"-c:v","copy","-c:a","aac","-b:a","160k",
         "-movflags","+faststart",out])

    # ---- VERIFY (audio-master frame lock) ----
    total_F = sum(e["frames"] for e in edl)
    expect = total_F / fps
    vdur = probe_dur(out); adur_ok = True
    # re-probe muxed audio duration
    r = subprocess.run(["ffprobe","-v","error","-select_streams","a:0","-show_entries",
                        "stream=duration","-of","csv=p=0",out], capture_output=True, text=True)
    adur = float(r.stdout.strip()) if r.stdout.strip() else vdur
    drift = abs(vdur - adur); frame = 1.0 / fps
    locked = drift < frame and abs(vdur - expect) < 2 * frame

    edl_path = os.path.splitext(out)[0] + "_EDL.json"
    json.dump({"fps":fps,"total_frames":total_F,"expected_sec":round(expect,3),
               "video_sec":round(vdur,3),"audio_sec":round(adur,3),
               "drift_sec":round(drift,4),"sync_locked":locked,"shots":edl},
              open(edl_path,"w"), indent=2)

    print(f"{'ID':<8}{'imgs':>5}{'on-screen':>11}{'vo':>8}   {'start':<12}{'end':<12}")
    for e in edl:
        st = e['images'][0]['start']; en = e['images'][-1]['end']
        print(f"{e['id']:<8}{len(e['images']):>5}{e['on_screen_sec']:>11}{e['vo_sec']:>8}   {st:<12}{en:<12}")
    print("-"*52)
    print(f"total frames {total_F} @ {fps}fps = expected {expect:.3f}s")
    print(f"video {vdur:.3f}s   audio {adur:.3f}s   drift {drift*1000:.1f} ms  (1 frame = {frame*1000:.1f} ms)")
    print("SYNC LOCKED" if locked else "!!! SYNC FAIL !!!")
    print("output:", out); print("EDL:", edl_path)
    if not locked: sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1])
