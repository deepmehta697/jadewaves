from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output" / "linkedin" / "clarity-early-supply-easier.png"

WIDTH = 1200
HEIGHT = 627

NAVY = "#112F4E"
SAND = "#F4EFE8"
GOLD = "#B58C45"
WHITE = "#FFFFFF"
INK = "#14283F"
MUTED = "#4C5E73"


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    base = Path("/System/Library/Fonts/Supplemental")
    paths = {
        "bold": base / "Arial Bold.ttf",
        "regular": base / "Arial.ttf",
    }
    return ImageFont.truetype(str(paths[name]), size=size)


def draw_wrapped(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, fill: str, box: tuple[int, int, int, int], line_gap: int = 8) -> int:
    x, y, max_w, _ = box
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_w:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)

    cursor_y = y
    for line in lines:
        draw.text((x, cursor_y), line, font=font, fill=fill)
        line_h = draw.textbbox((0, 0), line, font=font)[3]
        cursor_y += line_h + line_gap
    return cursor_y


def build() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    bg = Image.open(ROOT / "assets" / "container-loading-wide.jpeg")
    bg = ImageOps.exif_transpose(bg).convert("RGB")
    bg = ImageOps.fit(bg, (WIDTH, HEIGHT), method=Image.Resampling.LANCZOS, centering=(0.55, 0.45))

    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    odraw.rectangle((0, 0, WIDTH, HEIGHT), fill=(17, 47, 78, 132))
    odraw.rounded_rectangle((46, 40, 720, 587), radius=28, fill=(244, 239, 232, 235))
    odraw.rounded_rectangle((804, 48, 1148, 104), radius=18, fill=(17, 47, 78, 220))
    odraw.rectangle((86, 150, 146, 156), fill=GOLD)

    canvas = Image.alpha_composite(bg.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(canvas)

    font_title = load_font("bold", 66)
    font_sub = load_font("regular", 26)
    font_meta = load_font("bold", 18)
    font_small = load_font("regular", 22)

    logo = Image.open(ROOT / "assets" / "jade-waves-logo-transparent.png")
    logo = ImageOps.contain(ImageOps.exif_transpose(logo).convert("RGBA"), (170, 110), method=Image.Resampling.LANCZOS)
    canvas.alpha_composite(logo, (82, 58))

    draw.text((828, 64), "Jade Waves Enterprise", font=font_meta, fill=WHITE)

    draw.text((86, 178), "Clarity Early.", font=font_title, fill=INK)
    draw.text((86, 252), "Supply Easier.", font=font_title, fill=INK)

    next_y = draw_wrapped(
        draw,
        "Specification-led mineral supply from India for buyers who value repeatability, clear communication, and export-ready dispatch.",
        font_sub,
        MUTED,
        (86, 344, 586, 120),
        line_gap=10,
    )

    draw.text((86, next_y + 18), "Application. Sample. Dispatch.", font=font_small, fill=NAVY)
    draw.text((86, 542), "jadewavesenterprise.com", font=font_meta, fill=NAVY)

    canvas.convert("RGB").save(OUTPUT, quality=92)


if __name__ == "__main__":
    build()
