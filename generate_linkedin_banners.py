from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "output" / "linkedin"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PROFILE_SIZE = (1584, 396)
COMPANY_SIZE = (4200, 700)

NAVY = "#102D49"
NAVY_SOFT = "#173A5A"
SAND = "#F4EFE8"
GOLD = "#B58C45"
WHITE = "#FFFFFF"
INK = "#12263D"
MUTED = "#55677B"
MUTED_LIGHT = "#D4DDE6"

FONT_DIR = Path("/System/Library/Fonts/Supplemental")


def font(name: str, size: int):
    mapping = {
        "bold": FONT_DIR / "Arial Bold.ttf",
        "regular": FONT_DIR / "Arial.ttf",
        "display": FONT_DIR / "Didot.ttc",
        "serif": FONT_DIR / "Baskerville.ttc",
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


def draw_wrapped(draw: ImageDraw.ImageDraw, text: str, x: int, y: int, max_width: int, fnt, fill: str, gap: int) -> int:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)

    cursor = y
    for line in lines:
        draw.text((x, cursor), line, font=fnt, fill=fill)
        bbox = draw.textbbox((0, 0), line, font=fnt)
        cursor += bbox[3] - bbox[1] + gap
    return cursor


def apply_gradient(base: Image.Image, left_to_right: bool = True, strength: int = 200) -> Image.Image:
    w, h = base.size
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    px = overlay.load()
    for x in range(w):
        t = x / max(1, w - 1)
        alpha = int((1 - t if left_to_right else t) * strength)
        for y in range(h):
            px[x, y] = (16, 45, 73, alpha)
    return Image.alpha_composite(base.convert("RGBA"), overlay)


def cover_image(path: Path, size: tuple[int, int], centering=(0.5, 0.5)) -> Image.Image:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image).convert("RGB")
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=centering)


def paste_rounded(canvas: Image.Image, image: Image.Image, box: tuple[int, int, int, int], radius: int) -> None:
    x0, y0, x1, y1 = box
    image = image.resize((x1 - x0, y1 - y0), Image.Resampling.LANCZOS).convert("RGBA")
    mask = Image.new("L", (x1 - x0, y1 - y0), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, x1 - x0, y1 - y0), radius=radius, fill=255)
    canvas.paste(image, (x0, y0), mask)


def add_shadow(canvas: Image.Image, box: tuple[int, int, int, int], radius: int, blur: int = 26, opacity: int = 120):
    x0, y0, x1, y1 = box
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=(0, 0, 0, opacity))
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


def profile_banner():
    size = PROFILE_SIZE
    canvas = Image.new("RGBA", size, NAVY)
    overlay = Image.new("RGBA", size, (16, 37, 60, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 1584, 396), fill=(11, 26, 42, 255))
    od.rectangle((0, 0, 420, 396), fill=(9, 22, 36, 255))
    od.ellipse((1180, -140, 1720, 320), fill=(18, 41, 66, 92))
    od.ellipse((1260, 200, 1700, 520), fill=(15, 35, 56, 88))
    canvas.alpha_composite(overlay)
    draw = ImageDraw.Draw(canvas)

    draw.rectangle((790, 122, 950, 128), fill=GOLD)

    kicker = font("bold", 17)
    headline = fit_text(draw, "Clarity in Supply.", 560, "display", 78, 60)
    sub = fit_text(draw, "Specification-led mineral sourcing for industrial buyers.", 560, "regular", 28, 20)
    footer = fit_text(draw, "Founder-led execution • Ahmedabad, India", 560, "regular", 19, 15)

    draw.text((790, 140), "FOUNDER | JADE WAVES ENTERPRISE", font=kicker, fill=SAND)
    draw.text((790, 170), "Clarity in Supply.", font=headline, fill=(247, 242, 236))
    draw.text((790, 264), "Specification-led mineral sourcing", font=sub, fill=(228, 235, 241))
    draw.text((790, 298), "for industrial buyers.", font=sub, fill=(228, 235, 241))
    draw.text((790, 336), "Founder-led execution • Ahmedabad, India", font=footer, fill=(183, 195, 207))

    out = OUT_DIR / "deep-mehta-linkedin-banner.jpg"
    canvas.convert("RGB").save(out, quality=92, optimize=True)
    return out


def company_banner():
    size = COMPANY_SIZE
    background = cover_image(ROOT / "assets" / "web" / "company_port.jpg", size, centering=(0.48, 0.48)).convert("RGBA")
    canvas = background.copy()

    overlay = Image.new("RGBA", size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 4200, 700), fill=(10, 24, 39, 88))
    od.rectangle((0, 0, 2320, 700), fill=(11, 26, 42, 244))
    od.rectangle((2320, 0, 4200, 700), fill=(10, 24, 39, 82))
    canvas.alpha_composite(overlay)
    draw = ImageDraw.Draw(canvas)

    draw.line((2356, 70, 2356, 628), fill=(181, 140, 69, 120), width=2)
    add_shadow(canvas, (430, 56, 742, 158), radius=24, blur=20, opacity=92)
    draw.rounded_rectangle((430, 56, 742, 158), radius=24, fill=(244, 239, 231, 246), outline=(181, 140, 69, 110), width=2)
    logo = tint_logo(ROOT / "assets" / "jade-waves-logo-transparent.png", (164, 84), (16, 45, 73))
    canvas.alpha_composite(logo, (504, 72))

    draw.rectangle((430, 190, 620, 206), fill=GOLD)

    factory = cover_image(ROOT / "assets" / "web" / "company_factory.jpg", (760, 276), centering=(0.62, 0.46))
    add_shadow(canvas, (3000, 344, 3890, 590), radius=28, blur=26, opacity=118)
    paste_rounded(canvas, factory, (3000, 344, 3890, 590), 28)
    glass = Image.new("RGBA", size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glass)
    gd.rounded_rectangle((3000, 344, 3890, 590), radius=28, outline=(244, 239, 231, 105), width=2)
    gd.rounded_rectangle((3000, 286, 3460, 366), radius=20, fill=(12, 28, 45, 228), outline=(181, 140, 69, 110), width=2)
    canvas.alpha_composite(glass)

    label_font = fit_text(draw, "EXPORT EXECUTION", 340, "bold", 28, 20)
    label_sub = fit_text(draw, "Containerized dispatch and shipment visibility", 420, "regular", 18, 14)
    draw.text((3032, 300), "EXPORT EXECUTION", font=label_font, fill=SAND)
    draw.text((3032, 330), "Containerized dispatch and shipment visibility", font=label_sub, fill=(210, 219, 227))

    kicker_font = font("bold", 24)
    title_font = fit_text(draw, "Specification-Led Industrial Mineral Supply", 1720, "bold", 72, 56)
    title_font_2 = fit_text(draw, "from India", 600, "display", 64, 48)
    body_font = fit_text(draw, "Clear specs. Sample-first support. Export-ready dispatch.", 1440, "regular", 34, 26)
    industry_font = fit_text(draw, "Ceramics • Glass • Foundry • Construction • Industrial Processing", 1440, "regular", 29, 21)
    family_font = fit_text(draw, "Feldspar • Quartz • Silica Sand • Bentonite • Kaolin • Talc • Salt • Fly Ash • Copper Slag", 1650, "regular", 24, 18)

    draw.text((430, 232), "JADE WAVES ENTERPRISE", font=kicker_font, fill=SAND)
    draw.text((430, 286), "Specification-Led Industrial Mineral Supply", font=title_font, fill=(247, 242, 236))
    draw.text((430, 370), "from India", font=title_font_2, fill=(244, 239, 231))
    draw.text((430, 460), "Clear specs. Sample-first support. Export-ready dispatch.", font=body_font, fill=(232, 237, 242))
    draw.text((430, 532), "Ceramics • Glass • Foundry • Construction • Industrial Processing", font=industry_font, fill=(202, 211, 219))
    draw.text((430, 586), "Feldspar • Quartz • Silica Sand • Bentonite • Kaolin • Talc • Salt • Fly Ash • Copper Slag", font=family_font, fill=(202, 211, 219))

    out = OUT_DIR / "jade-waves-company-linkedin-banner.jpg"
    canvas.convert("RGB").save(out, quality=92, optimize=True)
    return out


def main():
    profile = profile_banner()
    company = company_banner()
    print(profile)
    print(company)


if __name__ == "__main__":
    main()
