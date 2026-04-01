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


def tint_logo(path: Path, size: tuple[int, int], rgb: tuple[int, int, int]) -> Image.Image:
    logo = Image.open(path)
    logo = ImageOps.exif_transpose(logo).convert("RGBA")
    logo = ImageOps.contain(logo, size, method=Image.Resampling.LANCZOS)
    alpha = logo.getchannel("A")
    colored = Image.new("RGBA", logo.size, rgb + (255,))
    colored.putalpha(alpha)
    return colored


def main():
    canvas = Image.new("RGBA", SIZE, NAVY)
    draw = ImageDraw.Draw(canvas)

    draw.rectangle((0, 0, 1200, 627), fill=NAVY)
    draw.rectangle((0, 0, 640, 627), fill=NAVY_DEEP)
    draw.ellipse((-160, -120, 300, 280), fill=(28, 59, 88, 78))
    draw.ellipse((340, 440, 780, 860), fill=(17, 39, 61, 72))
    draw.line((664, 66, 664, 560), fill=(181, 140, 69, 118), width=2)

    add_shadow(canvas, (88, 68, 338, 156), radius=22, blur=18, opacity=88)
    draw.rounded_rectangle((88, 68, 338, 156), radius=22, fill=(244, 239, 231, 246), outline=(181, 140, 69, 112), width=2)
    logo = tint_logo(ROOT / "assets" / "jade-waves-logo-transparent.png", (138, 66), (16, 45, 73))
    canvas.alpha_composite(logo, (140, 78))

    draw.rectangle((88, 192, 226, 198), fill=GOLD)

    title1 = fit_text(draw, "Ceramics Buyers", 500, "bold", 56, 38)
    title2 = fit_text(draw, "Need Production Fit", 500, "display", 54, 38)
    body = fit_text(draw, "Quartz and feldspar must fit the process, not just the quotation.", 500, "regular", 24, 18)
    footer = fit_text(draw, "Quartz • Feldspar • Application-led supply", 500, "regular", 20, 16)
    kicker = font("bold", 18)

    draw.text((88, 214), "FOUNDER POST", font=kicker, fill=SAND)
    draw.text((88, 258), "Ceramics Buyers", font=title1, fill=SAND)
    draw.text((88, 328), "Need Production Fit", font=title2, fill=(242, 232, 220))
    draw.text((88, 432), "Quartz and feldspar must fit", font=body, fill=MUTED)
    draw.text((88, 464), "the process, not just the quotation.", font=body, fill=MUTED)
    draw.text((88, 552), "Quartz • Feldspar • Application-led supply", font=footer, fill=(197, 207, 216))

    quartz = cover_image(ROOT / "assets" / "quartz-lumps-1-visual.webp", (370, 430), centering=(0.52, 0.5))
    feldspar = cover_image(ROOT / "assets" / "feldspar-powder.jpeg", (280, 220), centering=(0.52, 0.55))

    add_shadow(canvas, (742, 92, 1134, 530), radius=28, blur=24, opacity=110)
    paste_rounded(canvas, quartz, (742, 92, 1134, 530), 28)

    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rounded_rectangle((742, 92, 1134, 530), radius=28, outline=(244, 239, 231, 110), width=2)
    canvas.alpha_composite(overlay)

    add_shadow(canvas, (864, 364, 1138, 560), radius=24, blur=20, opacity=108)
    paste_rounded(canvas, feldspar, (864, 364, 1138, 560), 24)

    tag = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    td = ImageDraw.Draw(tag)
    td.rounded_rectangle((790, 114, 1032, 174), radius=18, fill=(11, 26, 42, 228), outline=(181, 140, 69, 104), width=2)
    td.rounded_rectangle((886, 386, 1088, 438), radius=16, fill=(11, 26, 42, 216), outline=(181, 140, 69, 96), width=2)
    canvas.alpha_composite(tag)

    small = fit_text(draw, "QUARTZ", 180, "bold", 24, 18)
    small2 = fit_text(draw, "FELDSPAR", 170, "bold", 22, 16)
    tiny = fit_text(draw, "Purity • sizing • consistency", 220, "regular", 16, 12)
    tiny2 = fit_text(draw, "Chemistry • mesh • process fit", 180, "regular", 15, 12)
    draw.text((842, 128), "QUARTZ", font=small, fill=SAND)
    draw.text((842, 152), "Purity • sizing • consistency", font=tiny, fill=(212, 220, 228))
    draw.text((916, 400), "FELDSPAR", font=small2, fill=SAND)
    draw.text((916, 422), "Chemistry • mesh • process fit", font=tiny2, fill=(212, 220, 228))

    out = OUT_DIR / "ceramics-production-fit-post.png"
    canvas.convert("RGB").save(out, quality=95, optimize=True)
    print(out)


if __name__ == "__main__":
    main()
