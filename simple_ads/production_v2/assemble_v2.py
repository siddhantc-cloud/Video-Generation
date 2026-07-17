import subprocess, json, sys, os
FF = r"C:\Users\SE\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe"
FP = FF.replace("ffmpeg.exe", "ffprobe.exe")
D = 0.4  # crossfade seconds
CLIPS = ["s1_veo3.mp4","s2b_veo3.mp4","s3_veo.mp4","s4_veo.mp4","s5_veo.mp4","s6_veo.mp4","s7_veo.mp4","s8_veo.mp4"]

# 1. normalize each to identical params
segs=[]
for i,c in enumerate(CLIPS):
    if not os.path.exists(c): sys.exit(f"MISSING {c}")
    seg=f"nseg_{i}.mp4"
    subprocess.run([FF,"-y","-loglevel","error","-i",c,"-r","24",
        "-vf","scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1",
        "-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p",
        "-c:a","aac","-ar","48000","-ac","2","-b:a","192k",seg],check=True)
    segs.append(seg)

def dur(f): return float(subprocess.run([FP,"-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())
durs=[dur(s) for s in segs]

# 2. build chained xfade (video) + acrossfade (audio)
vlab=f"[0:v]"; alab=f"[0:a]"; fc=[]; running=durs[0]
for i in range(1,len(segs)):
    off=round(running - D, 3)
    vo=f"[v{i}]"; ao=f"[a{i}]"
    fc.append(f"{vlab}[{i}:v]xfade=transition=fade:duration={D}:offset={off}{vo}")
    fc.append(f"{alab}[{i}:a]acrossfade=d={D}{ao}")
    vlab, alab = vo, ao
    running = round(running + durs[i] - D, 3)

inputs=[]
for s in segs: inputs += ["-i", s]
cmd=[FF,"-y","-loglevel","error"]+inputs+["-filter_complex",";".join(fc),
     "-map",vlab,"-map",alab,"-r","24","-c:v","libx264","-preset","medium","-crf","18",
     "-pix_fmt","yuv420p","-c:a","aac","-ar","48000","-ac","2","-b:a","192k","clear_gut_AD_v2_FINAL.mp4"]
subprocess.run(cmd,check=True)
print("FINAL duration:", round(running,2), "s ->", "clear_gut_AD_v2_FINAL.mp4")
