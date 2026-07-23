#!/usr/bin/env python
"""Render a frame-exact still/video animatic against one continuous narration."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def run(command: list[str]) -> None:
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(
            f"{command[0]} failed ({result.returncode}):\n{result.stderr[-2000:]}"
        )


def ffprobe_float(path: Path, stream: str | None = None) -> float:
    command = ["ffprobe", "-v", "error"]
    if stream:
        command.extend(["-select_streams", stream])
        command.extend(
            ["-show_entries", "stream=duration", "-of", "csv=p=0"]
        )
    else:
        command.extend(
            ["-show_entries", "format=duration", "-of", "csv=p=0"]
        )
    command.append(str(path))
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return float(result.stdout.strip())


def ffprobe_frames(path: Path) -> int:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-count_frames",
            "-show_entries",
            "stream=nb_read_frames",
            "-of",
            "csv=p=0",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return int(result.stdout.strip())


def render_still(
    source: Path,
    output: Path,
    frames: int,
    fps: int,
    width: int,
    height: int,
    zoom_in: bool,
    first: bool,
) -> None:
    if zoom_in:
        zoom = "min(zoom+0.00018,1.04)"
    else:
        zoom = "if(eq(on,1),1.04,max(zoom-0.00018,1.0))"
    filters = (
        f"scale={width * 2}:{height * 2}:force_original_aspect_ratio=increase,"
        f"crop={width * 2}:{height * 2},"
        f"zoompan=z='{zoom}':d={frames}:"
        f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
        f"s={width}x{height}:fps={fps},format=yuv420p"
    )
    if first:
        filters += ",fade=t=in:st=0:d=0.35"
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-loop",
            "1",
            "-i",
            str(source),
            "-vf",
            filters,
            "-frames:v",
            str(frames),
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-video_track_timescale",
            "90000",
            str(output),
        ]
    )


def render_video_range(
    source: Path,
    output: Path,
    source_in_frame: int,
    frames: int,
    fps: int,
    width: int,
    height: int,
) -> None:
    filters = (
        f"trim=start_frame={source_in_frame},setpts=PTS-STARTPTS,"
        f"fps={fps},scale={width}:{height}:force_original_aspect_ratio=increase,"
        f"crop={width}:{height},tpad=stop_mode=clone:stop_duration=30,"
        "format=yuv420p"
    )
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(source),
            "-vf",
            filters,
            "-frames:v",
            str(frames),
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-video_track_timescale",
            "90000",
            str(output),
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    manifest_path = args.manifest.resolve()
    project = manifest_path.parents[2]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    timing_path = project / manifest["narration"]["word_boundaries"]
    timing = json.loads(timing_path.read_text(encoding="utf-8"))
    words = timing["words"]
    fps = int(manifest["fps"])
    width, height = map(int, manifest["resolution"])
    total_frames = int(manifest["total_frames"])
    total_seconds = total_frames / fps
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    work = output.parent / "_work_v004"
    work.mkdir(parents=True, exist_ok=True)

    segments: list[Path] = []
    edl_beats: list[dict[str, object]] = []
    for index, beat in enumerate(manifest["beats"]):
        start = int(beat["start_frame"])
        end = int(beat["end_frame"])
        frames = end - start
        if frames <= 0:
            raise ValueError(f"{beat['id']} has no frames")
        source = project / beat["source"]
        if not source.exists():
            raise FileNotFoundError(source)
        segment = work / f"{index:02d}_{beat['id']}.mp4"
        if source.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
            render_still(
                source,
                segment,
                frames,
                fps,
                width,
                height,
                zoom_in=index % 2 == 0,
                first=index == 0,
            )
            source_in = None
        else:
            source_in = int(beat.get("source_in_frame", 0))
            render_video_range(
                source,
                segment,
                source_in,
                frames,
                fps,
                width,
                height,
            )
        actual_frames = ffprobe_frames(segment)
        if actual_frames != frames:
            raise RuntimeError(
                f"{beat['id']} rendered {actual_frames} frames, expected {frames}"
            )
        segments.append(segment)
        first_word_index = int(beat["first_word_index"])
        first_word = words[first_word_index]
        word_start = float(first_word["start_sec"])
        cut_time = start / fps
        semantic_delta_ms = (cut_time - word_start) * 1000
        edl_beats.append(
            {
                "id": beat["id"],
                "phrase": beat["phrase"],
                "first_word_index": first_word_index,
                "first_word": first_word["text"],
                "word_start_sec": round(word_start, 6),
                "semantic_delta_ms": round(semantic_delta_ms, 3),
                "opening_preroll": index == 0,
                "source": str(source.relative_to(project)).replace("\\", "/"),
                "source_in_frame": source_in,
                "start_frame": start,
                "end_frame": end,
                "frames": frames,
                "start_sec": round(start / fps, 6),
                "end_sec": round(end / fps, 6),
            }
        )

    concat_list = work / "video-concat.txt"
    concat_list.write_text(
        "".join(f"file '{segment.as_posix()}'\n" for segment in segments),
        encoding="utf-8",
    )
    video_master = work / "video-master.mp4"
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c",
            "copy",
            str(video_master),
        ]
    )

    narration = project / manifest["narration"]["audio"]
    audio_master = work / "audio-master.wav"
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(narration),
            "-af",
            "apad",
            "-t",
            f"{total_seconds:.6f}",
            "-ar",
            "48000",
            "-ac",
            "2",
            str(audio_master),
        ]
    )
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(video_master),
            "-i",
            str(audio_master),
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-movflags",
            "+faststart",
            "-t",
            f"{total_seconds:.6f}",
            str(output),
        ]
    )

    actual_frames = ffprobe_frames(output)
    video_seconds = ffprobe_float(output, "v:0")
    audio_seconds = ffprobe_float(output, "a:0")
    drift = abs(video_seconds - audio_seconds)
    one_frame = 1 / fps
    semantic_errors = [
        abs(float(beat["semantic_delta_ms"]))
        for beat in edl_beats
        if not beat["opening_preroll"]
    ]
    max_semantic_error_ms = max(semantic_errors, default=0.0)
    semantic_locked = max_semantic_error_ms <= (1000 / fps) / 2
    locked = (
        actual_frames == total_frames
        and drift < one_frame
        and abs(video_seconds - total_seconds) < one_frame
        and semantic_locked
    )
    edl = {
        "schema": 1,
        "fps": fps,
        "resolution": [width, height],
        "total_frames": total_frames,
        "expected_sec": round(total_seconds, 6),
        "video_frames": actual_frames,
        "video_sec": round(video_seconds, 6),
        "audio_sec": round(audio_seconds, 6),
        "drift_sec": round(drift, 6),
        "sync_locked": locked,
        "semantic_locked": semantic_locked,
        "max_semantic_error_ms": round(max_semantic_error_ms, 3),
        "semantic_tolerance_ms": round((1000 / fps) / 2, 3),
        "continuous_audio": True,
        "beats": edl_beats,
    }
    edl_path = output.with_name(output.stem + "_EDL.json")
    edl_path.write_text(json.dumps(edl, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(edl, indent=2))
    if not locked:
        raise SystemExit("Frame-lock verification failed.")


if __name__ == "__main__":
    main()
