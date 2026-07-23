#!/usr/bin/env python
"""Build the v004 SIP metaphor and deterministic ZebPay end card.

The graphics are full-frame clips, not text baked into generated imagery. They
share the K10 blue-hour bridge plate so the story does not fall into a slide
deck when the narration reaches the investment parallel.
"""

from __future__ import annotations

import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


W, H, FPS = 1080, 1920, 30
FONT_REGULAR = Path(r"C:\Windows\Fonts\segoeui.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\segoeuib.ttf")
COBALT = (46, 124, 246)
WHITE = (242, 246, 255)
MUTED = (166, 180, 203)
NAVY = (3, 14, 43)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def ease_out_cubic(t: float) -> float:
    t = clamp(t)
    return 1 - (1 - t) ** 3


def ease_in_out_cubic(t: float) -> float:
    t = clamp(t)
    if t < 0.5:
        return 4 * t**3
    return 1 - (-2 * t + 2) ** 3 / 2


def cover(image: Image.Image, width: int = W, height: int = H) -> Image.Image:
    image = image.convert("RGB")
    scale = max(width / image.width, height / image.height)
    resized = image.resize(
        (round(image.width * scale), round(image.height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - width) // 2
    top = (resized.height - height) // 2
    return resized.crop((left, top, left + width, top + height))


def darken_for_graph(base: Image.Image) -> Image.Image:
    base = ImageEnhance.Color(base).enhance(0.84)
    base = ImageEnhance.Contrast(base).enhance(1.06)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pixels = overlay.load()
    for y in range(H):
        # More room for the graph in the sky; keep bridge texture alive below.
        alpha = int(118 - 55 * clamp((y - 150) / 1500))
        for x in range(W):
            pixels[x, y] = (NAVY[0], NAVY[1], NAVY[2], alpha)
    return Image.alpha_composite(base.convert("RGBA"), overlay)


def alpha_text(
    layer: Image.Image,
    text: str,
    xy: tuple[int, int],
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    alpha: int,
    anchor: str = "mm",
) -> None:
    draw = ImageDraw.Draw(layer)
    draw.text(xy, text, font=font, fill=(*fill, alpha), anchor=anchor)


def polyline_prefix(
    points: list[tuple[float, float]], progress: float
) -> list[tuple[float, float]]:
    progress = clamp(progress)
    lengths = [
        math.dist(points[index], points[index + 1])
        for index in range(len(points) - 1)
    ]
    total = sum(lengths)
    target = total * progress
    result = [points[0]]
    consumed = 0.0
    for index, length in enumerate(lengths):
        start, end = points[index], points[index + 1]
        if consumed + length <= target:
            result.append(end)
            consumed += length
            continue
        remaining = max(0.0, target - consumed)
        ratio = remaining / length if length else 0.0
        result.append(
            (
                start[0] + (end[0] - start[0]) * ratio,
                start[1] + (end[1] - start[1]) * ratio,
            )
        )
        break
    return result


def pipe_video(frames, output: Path, total_frames: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "-s",
        f"{W}x{H}",
        "-r",
        str(FPS),
        "-i",
        "-",
        "-an",
        "-frames:v",
        str(total_frames),
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "17",
        "-pix_fmt",
        "yuv420p",
        "-video_track_timescale",
        "90000",
        str(output),
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    assert process.stdin is not None
    try:
        for frame in frames:
            process.stdin.write(frame.convert("RGB").tobytes())
    finally:
        process.stdin.close()
    return_code = process.wait()
    if return_code:
        raise SystemExit(f"ffmpeg failed with exit code {return_code}")


def sip_frames(base: Image.Image, total_frames: int):
    base = darken_for_graph(base)
    title_font = ImageFont.truetype(str(FONT_BOLD), 40)
    small_font = ImageFont.truetype(str(FONT_REGULAR), 25)

    plot_points = [
        (115, 690),
        (220, 520),
        (325, 655),
        (430, 455),
        (535, 720),
        (640, 545),
        (745, 645),
        (850, 440),
        (965, 575),
    ]
    marker_xs = [135, 255, 375, 495, 615, 735, 855, 965]
    phase_two = 133
    phase_three = 245

    for frame_index in range(total_frames):
        frame = base.copy()
        graphics = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw = ImageDraw.Draw(graphics)

        # Quiet glass field: not a separate card, just enough contrast in the sky.
        draw.rounded_rectangle(
            (65, 165, 1015, 865),
            radius=34,
            fill=(3, 14, 43, 82),
            outline=(155, 181, 226, 36),
            width=2,
        )

        if frame_index < phase_two:
            label = "THE MARKET MOVES"
            label_alpha = int(220 * ease_out_cubic(frame_index / 18))
            path_progress = 0.78 * ease_in_out_cubic(frame_index / (phase_two - 1))
        elif frame_index < phase_three:
            label = "SAME AMOUNT. REGULARLY."
            local = frame_index - phase_two
            label_alpha = int(235 * ease_out_cubic(local / 16))
            path_progress = 0.78 + 0.22 * ease_in_out_cubic(local / 55)
        else:
            label = "THROUGH UPS AND DOWNS"
            local = frame_index - phase_three
            label_alpha = int(235 * ease_out_cubic(local / 12))
            path_progress = 1.0

        alpha_text(
            graphics,
            label,
            (W // 2, 235),
            title_font,
            WHITE,
            label_alpha,
        )
        alpha_text(
            graphics,
            "MARKET PATH",
            (116, 830),
            small_font,
            MUTED,
            170,
            anchor="lm",
        )

        # A soft cobalt glow beneath the market path.
        visible_path = polyline_prefix(plot_points, path_progress)
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow)
        if len(visible_path) > 1:
            glow_draw.line(visible_path, fill=(*COBALT, 130), width=14, joint="curve")
            glow = glow.filter(ImageFilter.GaussianBlur(10))
            graphics = Image.alpha_composite(graphics, glow)
            draw = ImageDraw.Draw(graphics)
            draw.line(visible_path, fill=(*COBALT, 245), width=5, joint="curve")

        # Equal contribution markers appear at fixed intervals and identical size.
        marker_reveal = 0
        if frame_index >= phase_two:
            marker_reveal = int((frame_index - phase_two) / 14) + 1
        marker_reveal = min(marker_reveal, len(marker_xs))
        baseline_y = 790
        draw.line(
            [(115, baseline_y), (965, baseline_y)],
            fill=(196, 209, 230, 72),
            width=2,
        )
        for index, x in enumerate(marker_xs):
            if index >= marker_reveal:
                break
            age = frame_index - (phase_two + index * 14)
            scale = 0.75 + 0.25 * ease_out_cubic(age / 9)
            radius = round(10 * scale)
            glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            glow_draw = ImageDraw.Draw(glow_layer)
            glow_draw.ellipse(
                (x - radius * 2, baseline_y - radius * 2, x + radius * 2, baseline_y + radius * 2),
                fill=(*COBALT, 90),
            )
            glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(8))
            graphics = Image.alpha_composite(graphics, glow_layer)
            draw = ImageDraw.Draw(graphics)
            draw.ellipse(
                (x - radius, baseline_y - radius, x + radius, baseline_y + radius),
                fill=(*WHITE, 245),
                outline=(*COBALT, 255),
                width=4,
            )

        alpha_text(
            graphics,
            "EQUAL CONTRIBUTIONS",
            (W // 2, 912),
            small_font,
            MUTED,
            180 if frame_index >= phase_two else 0,
        )

        # K10 immediately precedes this clip with the same base plate. Do not
        # fade from navy here: that creates a one-frame dark flash at the cut.
        composed = Image.alpha_composite(frame, graphics).convert("RGB")
        yield composed


def end_card_frames(base: Image.Image, logo: Image.Image, total_frames: int):
    base = cover(base).filter(ImageFilter.GaussianBlur(8))
    base = ImageEnhance.Color(base).enhance(0.55)
    navy_layer = Image.new("RGBA", (W, H), (*NAVY, 214))
    base = Image.alpha_composite(base.convert("RGBA"), navy_layer)

    wordmark_font = ImageFont.truetype(str(FONT_BOLD), 76)
    cta_font = ImageFont.truetype(str(FONT_BOLD), 43)
    logo = logo.convert("RGBA")

    for frame_index in range(total_frames):
        local = ease_out_cubic(frame_index / 18)
        frame = base.copy()
        draw = ImageDraw.Draw(frame)

        # Restrained architectural echo of the bridge.
        draw.line((180, 1450, 900, 1450), fill=(*COBALT, 55), width=2)
        draw.line((265, 1510, 815, 1510), fill=(*COBALT, 30), width=2)

        logo_size = round(192 * (0.88 + 0.12 * local))
        logo_frame = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        logo_frame.putalpha(int(255 * local))
        logo_x = (W - logo_size) // 2
        logo_y = 580 - (logo_size // 2)
        shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.rounded_rectangle(
            (logo_x - 12, logo_y - 12, logo_x + logo_size + 12, logo_y + logo_size + 12),
            radius=32,
            fill=(0, 0, 0, int(95 * local)),
        )
        shadow = shadow.filter(ImageFilter.GaussianBlur(22))
        frame = Image.alpha_composite(frame, shadow)
        frame.alpha_composite(logo_frame, (logo_x, logo_y))

        text_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        alpha_text(
            text_layer,
            "ZebPay",
            (W // 2, 850),
            wordmark_font,
            WHITE,
            int(255 * ease_out_cubic((frame_index - 5) / 18)),
        )
        alpha_text(
            text_layer,
            "START YOUR SIP",
            (W // 2, 980),
            cta_font,
            WHITE,
            int(245 * ease_out_cubic((frame_index - 10) / 18)),
        )
        line_progress = ease_out_cubic((frame_index - 12) / 20)
        line_half = round(135 * line_progress)
        ImageDraw.Draw(text_layer).line(
            (W // 2 - line_half, 1042, W // 2 + line_half, 1042),
            fill=(*COBALT, int(255 * line_progress)),
            width=5,
        )
        frame = Image.alpha_composite(frame, text_layer).convert("RGB")

        if frame_index >= total_frames - 14:
            fade = ease_in_out_cubic(
                (frame_index - (total_frames - 14)) / 13
            )
            frame = Image.blend(frame, Image.new("RGB", (W, H), NAVY), 0.22 * fade)
        yield frame


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    base_path = project / "keyframes/short-v004/K10-regular-path.png"
    logo_path = project / "assets/brand/zebpay_logo.png"
    output_dir = project / "edit/animations/animatic-short-v004"

    base = cover(Image.open(base_path))
    logo = Image.open(logo_path)
    sip_output = output_dir / "sip-metaphor.mp4"
    end_output = output_dir / "end-card.mp4"

    pipe_video(sip_frames(base, 319), sip_output, 319)
    pipe_video(end_card_frames(base, logo, 100), end_output, 100)
    print(sip_output)
    print(end_output)


if __name__ == "__main__":
    main()
