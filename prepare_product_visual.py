#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepare a consistent square product visual from any source image."
    )
    parser.add_argument("source", type=Path, help="Path to the source image")
    parser.add_argument("output", type=Path, help="Path to the generated output image")
    parser.add_argument("--size", type=int, default=1600, help="Square output size in pixels")
    parser.add_argument(
        "--padding",
        type=int,
        default=130,
        help="Padding around the contained source image inside the square output",
    )
    return parser


def soften_background(image: Image.Image, size: int) -> Image.Image:
    background = ImageOps.fit(image.convert("RGB"), (size, size), method=Image.Resampling.LANCZOS)
    background = ImageEnhance.Color(background).enhance(0.16)
    background = ImageEnhance.Contrast(background).enhance(0.84)
    background = ImageEnhance.Brightness(background).enhance(1.08)
    background = background.filter(ImageFilter.GaussianBlur(42)).convert("RGBA")

    wash = Image.new("RGBA", (size, size), (243, 246, 248, 212))
    background = Image.alpha_composite(background, wash)

    glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(glow)
    draw.ellipse((-100, -120, int(size * 0.72), int(size * 0.58)), fill=(255, 255, 255, 110))
    draw.ellipse((int(size * 0.38), int(size * 0.42), size + 120, size + 140), fill=(214, 224, 232, 78))
    glow = glow.filter(ImageFilter.GaussianBlur(56))
    return Image.alpha_composite(background, glow)


def contain_image(image: Image.Image, box_size: int) -> Image.Image:
    contained = ImageOps.contain(image, (box_size, box_size), method=Image.Resampling.LANCZOS)
    return contained.convert("RGBA")


def rounded_alpha(size: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return mask


def add_shadow(layer: Image.Image, offset_y: int = 26) -> Image.Image:
    shadow = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    alpha = layer.getchannel("A")
    shadow_alpha = ImageEnhance.Brightness(alpha).enhance(0.42)
    shadow_alpha = shadow_alpha.filter(ImageFilter.GaussianBlur(26))
    shadow = Image.new("RGBA", layer.size, (14, 18, 22, 0))
    shadow.putalpha(shadow_alpha)
    return ImageChops.offset(shadow, 0, offset_y)


def build_visual(source_path: Path, output_path: Path, size: int, padding: int) -> None:
    source = ImageOps.exif_transpose(Image.open(source_path)).convert("RGBA")
    canvas = soften_background(source, size)

    stage = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    stage_draw = ImageDraw.Draw(stage)
    stage_margin = max(56, padding // 2)
    stage_draw.rounded_rectangle(
        (stage_margin, stage_margin, size - stage_margin, size - stage_margin),
        radius=54,
        fill=(255, 255, 255, 148),
        outline=(255, 255, 255, 164),
        width=2,
    )
    stage = stage.filter(ImageFilter.GaussianBlur(0))
    canvas = Image.alpha_composite(canvas, stage)

    box_size = max(200, size - (padding * 2))
    foreground = contain_image(source, box_size)
    foreground.putalpha(rounded_alpha(foreground.size, 34))

    shadow = add_shadow(foreground)
    center_x = (size - foreground.width) // 2
    center_y = (size - foreground.height) // 2 - 10
    canvas.alpha_composite(shadow, (center_x, center_y))
    canvas.alpha_composite(foreground, (center_x, center_y))

    sheen = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sheen_draw = ImageDraw.Draw(sheen)
    sheen_draw.polygon(
        [
            (int(size * 0.08), 0),
            (int(size * 0.33), 0),
            (int(size * 0.58), size),
            (int(size * 0.33), size),
        ],
        fill=(255, 255, 255, 44),
    )
    sheen = sheen.filter(ImageFilter.GaussianBlur(34))
    canvas = Image.alpha_composite(canvas, sheen)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.suffix.lower() == ".png":
        canvas.save(output_path, optimize=True)
    else:
        canvas.convert("RGB").save(output_path, quality=88, method=6)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    build_visual(args.source, args.output, args.size, args.padding)


if __name__ == "__main__":
    main()
