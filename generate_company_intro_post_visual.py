from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "output" / "linkedin"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SIZE = (1200, 627)
NAVY = "#102D49"
NAVY_DEEP = "#0B1A2B"
SAND = "#F4EFE8"
GOLD = "#B58C45"
MUTED = "#D7E0E8"
FONT_DIR = Path("/System/Library/Fonts/Supplemental")


def font(name: str, size: int):
    mapping = {
        "bold": FONT_DIR / "Arial Bold.ttf",
        "regular": FONT_DIR / "Arial.ttf",
        "display": FONT_DIR / "Didot.ttc",
    }
    return ImageFont.truetype(str(mapping[name]), size=size)


def fit_text(draw: ImageDraw.ImageDraw, text: str, max_width: int, style: str, start_size: int, min_size: int):
    size = start_size
    while size >= min_size:
        fnt = font(style, size)
        if draw.textbbox((0, 0), text, font=fnt)[2] <= max_width:
            return fnt
        size -= 2
    return font(style, min_size)


def cover_image(path: Path, size: tuple[int, int], centering=(0.5, 0.5)) -> Image.Image:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image).convert("RGB")
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=centering)


def add_shadow(canvas: Image.Image, box: tuple[int, int, int, int], radius: int, blur: int = 24, opacity: int = 105):
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle(box, radius=radius, fill=(0, 0, 0, opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    canvas.alpha_composite(shadow)


def tint_logo(path: Path, size: tuple[int, int], rgb: tuple[int, int, int]) -> Image.Image:
    logo = Image.open(path)
    logo = ImageOps.exif_transpose(logo).convert("RGBA")
    logo = ImageOps.contain(logo, size, method=Image.Resampling.LANCZOS)
    alpha = logo.getchannel("A")
    colored = Image.new("RGBA", logo.size, rgb + (255,))
    colored.putalpha(alpha)
    return colored


def main():
    background = cover_image(ROOT / "assets" / "web" / "company_port.jpg", SIZE, centering=(0.42, 0.5)).convert("RGBA")
    canvas = background.copy()

    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 1200, 627), fill=(10, 24, 39, 86))
    od.rectangle((0, 0, 720, 627), fill=(11, 26, 42, 228))
    od.ellipse((-180, -120, 320, 320), fill=(25, 56, 84, 82))
    canvas.alpha_composite(overlay)

    draw = ImageDraw.Draw(canvas)

    add_shadow(canvas, (84, 72, 334, 160), radius=22, blur=18, opacity=90)
    draw.rounded_rectangle((84, 72, 334, 160), radius=22, fill=(244, 239, 231, 246), outline=(181, 140, 69, 110), width=2)
    logo = tint_logo(ROOT / "assets" / "jade-waves-logo-transparent.png", (140, 68), (16, 45, 73))
    canvas.alpha_composite(logo, (134, 82))

    draw.rectangle((84, 194, 220, 200), fill=GOLD)

    kicker = font("bold", 18)
    title1 = fit_text(draw, "Industrial Mineral Supply", 560, "bold", 58, 40)
    title2 = fit_text(draw, "from India", 360, "display", 54, 38)
    body = fit_text(draw, "Specification-led sourcing for ceramics, glass, foundry, construction, and industrial processing buyers.", 560, "regular", 25, 18)
    footer = fit_text(draw, "Samples • Specs • Export-ready dispatch", 520, "regular", 22, 16)

    draw.text((84, 214), "JADE WAVES ENTERPRISE", font=kicker, fill=SAND)
    draw.text((84, 260), "Industrial Mineral Supply", font=title1, fill=SAND)
    draw.text((84, 330), "from India", font=title2, fill=(242, 232, 220))
    draw.text((84, 420), "Specification-led sourcing for ceramics,", font=body, fill=MUTED)
    draw.text((84, 452), "glass, foundry, construction, and", font=body, fill=MUTED)
    draw.text((84, 484), "industrial processing buyers.", font=body, fill=MUTED)
    draw.text((84, 554), "Samples • Specs • Export-ready dispatch", font=footer, fill=(197, 207, 216))

    out = OUT_DIR / "company-intro-post-visual.png"
    canvas.convert("RGB").save(out, quality=95, optimize=True)
    print(out)


if __name__ == "__main__":
    main()
