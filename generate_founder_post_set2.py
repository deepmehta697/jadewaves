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


def add_shadow(canvas: Image.Image, box: tuple[int, int, int, int], radius: int, blur: int = 24, opacity: int = 100):
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle(box, radius=radius, fill=(0, 0, 0, opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    canvas.alpha_composite(shadow)


def paste_rounded(canvas: Image.Image, image: Image.Image, box: tuple[int, int, int, int], radius: int) -> None:
    x0, y0, x1, y1 = box
    image = image.resize((x1 - x0, y1 - y0), Image.Resampling.LANCZOS).convert("RGBA")
    mask = Image.new("L", (x1 - x0, y1 - y0), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, x1 - x0, y1 - y0), radius=radius, fill=255)
    canvas.paste(image, (x0, y0), mask)


def render_predictability():
    bg = cover_image(ROOT / "assets" / "web" / "company_port.jpg", SIZE, centering=(0.46, 0.48)).convert("RGBA")
    canvas = bg.copy()
    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 1200, 627), fill=(11, 26, 42, 72))
    od.rectangle((0, 0, 730, 627), fill=(11, 26, 42, 220))
    od.ellipse((-160, -120, 320, 320), fill=(27, 58, 86, 72))
    canvas.alpha_composite(overlay)
    draw = ImageDraw.Draw(canvas)

    draw.rectangle((84, 112, 220, 118), fill=GOLD)
    kicker = font("bold", 18)
    title1 = fit_text(draw, "Repeat Orders Come", 560, "bold", 58, 40)
    title2 = fit_text(draw, "from Predictability", 560, "display", 58, 40)
    body = fit_text(draw, "In mineral supply, consistency in process matters almost as much as consistency in material.", 560, "regular", 24, 18)
    footer = fit_text(draw, "Clarity • consistency • dispatch discipline", 520, "regular", 20, 16)

    draw.text((84, 132), "DEEP MEHTA", font=kicker, fill=SAND)
    draw.text((84, 184), "Repeat Orders Come", font=title1, fill=SAND)
    draw.text((84, 252), "from Predictability", font=title2, fill=(242, 232, 220))
    draw.text((84, 420), "In mineral supply, consistency in process", font=body, fill=MUTED)
    draw.text((84, 452), "matters almost as much as consistency", font=body, fill=MUTED)
    draw.text((84, 484), "in material.", font=body, fill=MUTED)
    draw.text((84, 552), "Clarity • consistency • dispatch discipline", font=footer, fill=(197, 207, 216))

    out = OUT_DIR / "founder-post-predictability.png"
    canvas.convert("RGB").save(out, quality=95, optimize=True)
    return out


def render_shipment_confidence():
    bg = cover_image(ROOT / "assets" / "process-loading-poster.png", SIZE, centering=(0.52, 0.42)).convert("RGBA")
    canvas = bg.copy()
    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 1200, 627), fill=(10, 24, 39, 72))
    od.rectangle((0, 0, 700, 627), fill=(11, 26, 42, 214))
    od.ellipse((-140, -100, 280, 260), fill=(26, 58, 88, 74))
    canvas.alpha_composite(overlay)
    draw = ImageDraw.Draw(canvas)

    draw.rectangle((84, 112, 220, 118), fill=GOLD)
    kicker = font("bold", 18)
    title1 = fit_text(draw, "Confidence Before", 540, "bold", 58, 40)
    title2 = fit_text(draw, "Shipment", 420, "display", 58, 40)
    body = fit_text(draw, "A buyer should know what happens between inquiry, documents, loading, and dispatch.", 540, "regular", 24, 18)
    footer = fit_text(draw, "Clear specs • clear docs • clear movement", 520, "regular", 20, 16)

    draw.text((84, 132), "DEEP MEHTA", font=kicker, fill=SAND)
    draw.text((84, 184), "Confidence Before", font=title1, fill=SAND)
    draw.text((84, 252), "Shipment", font=title2, fill=(242, 232, 220))
    draw.text((84, 420), "A buyer should know what happens", font=body, fill=MUTED)
    draw.text((84, 452), "between inquiry, documents, loading,", font=body, fill=MUTED)
    draw.text((84, 484), "and dispatch.", font=body, fill=MUTED)
    draw.text((84, 552), "Clear specs • clear docs • clear movement", font=footer, fill=(197, 207, 216))

    out = OUT_DIR / "founder-post-shipment-confidence.png"
    canvas.convert("RGB").save(out, quality=95, optimize=True)
    return out


def main():
    print(render_predictability())
    print(render_shipment_confidence())


if __name__ == "__main__":
    main()
