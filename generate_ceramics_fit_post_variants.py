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


def no_logo_variant():
    canvas = Image.new("RGBA", SIZE, NAVY_DEEP)
    draw = ImageDraw.Draw(canvas)

    draw.rectangle((0, 0, 1200, 627), fill=NAVY_DEEP)
    draw.rectangle((0, 0, 672, 627), fill=NAVY)
    draw.ellipse((-180, -120, 300, 260), fill=(29, 62, 92, 82))
    draw.ellipse((360, 440, 820, 860), fill=(17, 39, 61, 72))
    draw.line((674, 62, 674, 562), fill=(181, 140, 69, 118), width=2)

    draw.rectangle((86, 112, 224, 118), fill=GOLD)
    kicker = font("bold", 18)
    title1 = fit_text(draw, "Ceramics Buyers", 500, "bold", 56, 40)
    title2 = fit_text(draw, "Need Production Fit", 520, "display", 58, 40)
    body = fit_text(draw, "Quartz and feldspar must fit the process, not just the quotation.", 500, "regular", 24, 18)
    footer = fit_text(draw, "Quartz • Feldspar • Application-led supply", 500, "regular", 20, 16)

    draw.text((86, 132), "JADE WAVES ENTERPRISE", font=kicker, fill=SAND)
    draw.text((86, 180), "Ceramics Buyers", font=title1, fill=SAND)
    draw.text((86, 248), "Need Production Fit", font=title2, fill=(242, 232, 220))
    draw.text((86, 404), "Quartz and feldspar must fit", font=body, fill=MUTED)
    draw.text((86, 436), "the process, not just the quotation.", font=body, fill=MUTED)
    draw.text((86, 552), "Quartz • Feldspar • Application-led supply", font=footer, fill=(197, 207, 216))

    quartz = cover_image(ROOT / "assets" / "quartz-lumps-1-visual.webp", (392, 442), centering=(0.52, 0.5))
    feldspar = cover_image(ROOT / "assets" / "feldspar-powder.jpeg", (280, 204), centering=(0.52, 0.58))
    add_shadow(canvas, (748, 88, 1140, 530), radius=28, blur=24, opacity=108)
    paste_rounded(canvas, quartz, (748, 88, 1140, 530), 28)
    add_shadow(canvas, (854, 368, 1138, 562), radius=22, blur=18, opacity=106)
    paste_rounded(canvas, feldspar, (854, 368, 1138, 562), 22)

    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rounded_rectangle((748, 88, 1140, 530), radius=28, outline=(244, 239, 231, 108), width=2)
    od.rounded_rectangle((786, 108, 1064, 170), radius=16, fill=(11, 26, 42, 220), outline=(181, 140, 69, 98), width=2)
    od.rounded_rectangle((884, 390, 1098, 442), radius=14, fill=(11, 26, 42, 220), outline=(181, 140, 69, 96), width=2)
    od.rounded_rectangle((854, 368, 1138, 562), radius=22, outline=(244, 239, 231, 108), width=2)
    canvas.alpha_composite(overlay)

    small = fit_text(draw, "QUARTZ", 180, "bold", 24, 18)
    tiny = fit_text(draw, "Purity • sizing • consistency", 240, "regular", 15, 12)
    small2 = fit_text(draw, "FELDSPAR", 160, "bold", 20, 16)
    tiny2 = fit_text(draw, "Chemistry • mesh • process fit", 190, "regular", 14, 11)
    draw.text((842, 122), "QUARTZ", font=small, fill=SAND)
    draw.text((842, 146), "Purity • sizing • consistency", font=tiny, fill=(212, 220, 228))
    draw.text((916, 404), "FELDSPAR", font=small2, fill=SAND)
    draw.text((916, 426), "Chemistry • mesh • process fit", font=tiny2, fill=(212, 220, 228))

    out = OUT_DIR / "ceramics-production-fit-post-no-logo.png"
    canvas.convert("RGB").save(out, quality=95, optimize=True)
    return out


def single_image_variant():
    background = cover_image(ROOT / "assets" / "quartz-lumps-1-visual.webp", SIZE, centering=(0.55, 0.5)).convert("RGBA")
    canvas = background.copy()

    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 1200, 627), fill=(10, 24, 39, 74))
    od.rectangle((0, 0, 720, 627), fill=(11, 26, 42, 218))
    od.ellipse((-140, -100, 260, 240), fill=(27, 58, 86, 74))
    canvas.alpha_composite(overlay)
    draw = ImageDraw.Draw(canvas)

    draw.rectangle((86, 112, 224, 118), fill=GOLD)
    kicker = font("bold", 18)
    title1 = fit_text(draw, "Ceramics Buyers", 520, "bold", 58, 40)
    title2 = fit_text(draw, "Need Production Fit", 520, "display", 58, 40)
    body = fit_text(draw, "Quartz and feldspar must fit the process, not just the quotation.", 520, "regular", 24, 18)
    footer = fit_text(draw, "Purity • chemistry • mesh • consistency", 520, "regular", 20, 16)

    draw.text((86, 132), "FOUNDER POST", font=kicker, fill=SAND)
    draw.text((86, 180), "Ceramics Buyers", font=title1, fill=SAND)
    draw.text((86, 248), "Need Production Fit", font=title2, fill=(242, 232, 220))
    draw.text((86, 404), "Quartz and feldspar must fit", font=body, fill=MUTED)
    draw.text((86, 436), "the process, not just the quotation.", font=body, fill=MUTED)
    draw.text((86, 552), "Purity • chemistry • mesh • consistency", font=footer, fill=(197, 207, 216))

    tag = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    td = ImageDraw.Draw(tag)
    td.rounded_rectangle((824, 86, 1076, 146), radius=18, fill=(11, 26, 42, 220), outline=(181, 140, 69, 102), width=2)
    td.rounded_rectangle((792, 496, 1112, 560), radius=18, fill=(11, 26, 42, 220), outline=(181, 140, 69, 102), width=2)
    canvas.alpha_composite(tag)

    tag_font = fit_text(draw, "QUARTZ FOR CERAMICS", 220, "bold", 24, 18)
    tiny = fit_text(draw, "Production consistency starts with fit.", 280, "regular", 16, 12)
    draw.text((852, 100), "QUARTZ FOR CERAMICS", font=tag_font, fill=SAND)
    draw.text((822, 516), "Production consistency starts with fit.", font=tiny, fill=(212, 220, 228))

    out = OUT_DIR / "ceramics-production-fit-post-single-image.png"
    canvas.convert("RGB").save(out, quality=95, optimize=True)
    return out


def main():
    print(no_logo_variant())
    print(single_image_variant())


if __name__ == "__main__":
    main()
