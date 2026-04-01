from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "output" / "instagram"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SIZE = (1080, 1350)
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


def wrap_text(draw: ImageDraw.ImageDraw, text: str, max_width: int, fnt: ImageFont.FreeTypeFont):
    words = text.split()
    lines = []
    current = []
    for word in words:
        trial = " ".join(current + [word])
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= max_width:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def cover_image(path: Path, size: tuple[int, int], centering=(0.5, 0.5)) -> Image.Image:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image).convert("RGB")
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=centering)


def add_shadow(canvas: Image.Image, box: tuple[int, int, int, int], radius: int, blur: int = 26, opacity: int = 112):
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle(box, radius=radius, fill=(0, 0, 0, opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    canvas.alpha_composite(shadow)


def tint_logo(path: Path, size: tuple[int, int], rgb: tuple[int, int, int]) -> Image.Image:
    logo = Image.open(path)
    logo = ImageOps.exif_transpose(logo).convert("RGBA")
    alpha_box = logo.getchannel("A").getbbox()
    if alpha_box:
        logo = logo.crop(alpha_box)
    logo = ImageOps.contain(logo, size, method=Image.Resampling.LANCZOS)
    alpha = logo.getchannel("A")
    colored = Image.new("RGBA", logo.size, rgb + (255,))
    colored.putalpha(alpha)
    return colored


def draw_chip(canvas: Image.Image, box: tuple[int, int, int, int], text: str):
    add_shadow(canvas, box, radius=24, blur=16, opacity=72)
    chip = ImageDraw.Draw(canvas)
    chip.rounded_rectangle(box, radius=24, fill=(244, 239, 232, 232), outline=(181, 140, 69, 120), width=2)
    chip_font = fit_text(chip, text, box[2] - box[0] - 40, "bold", 22, 16)
    bbox = chip.textbbox((0, 0), text, font=chip_font)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 2
    chip.text((x, y), text, font=chip_font, fill=NAVY)


def main():
    background = cover_image(ROOT / "assets" / "silica-sand-packing.jpg", SIZE, centering=(0.5, 0.44)).convert("RGBA")
    canvas = background.copy()

    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, *SIZE), fill=(9, 19, 31, 92))
    od.ellipse((-160, -140, 380, 360), fill=(24, 52, 80, 76))
    od.ellipse((760, -100, 1180, 260), fill=(181, 140, 69, 28))
    od.rounded_rectangle((46, 780, 1034, 1296), radius=42, fill=(10, 24, 39, 214), outline=(181, 140, 69, 84), width=2)
    canvas.alpha_composite(overlay)

    draw = ImageDraw.Draw(canvas)

    logo_box = (58, 58, 366, 174)
    add_shadow(canvas, logo_box, radius=26, blur=18, opacity=94)
    draw.rounded_rectangle(logo_box, radius=26, fill=(244, 239, 231, 246), outline=(181, 140, 69, 112), width=2)
    logo = tint_logo(ROOT / "assets" / "jade-waves-logo-transparent.png", (196, 92), (16, 45, 73))
    canvas.alpha_composite(logo, (103, 72))

    draw.rounded_rectangle((760, 78, 1008, 136), radius=20, fill=(11, 26, 42, 202), outline=(181, 140, 69, 112), width=2)
    badge_font = fit_text(draw, "India to Global", 190, "bold", 24, 18)
    draw.text((796, 95), "India to Global", font=badge_font, fill=SAND)

    draw.rectangle((78, 816, 246, 824), fill=GOLD)

    kicker = font("bold", 22)
    title1 = fit_text(draw, "Export-Ready", 860, "bold", 84, 56)
    title2 = fit_text(draw, "Mineral Supply", 860, "display", 86, 56)
    body_font = fit_text(draw, "From samples to bulk dispatch for global industrial buyers.", 860, "regular", 34, 24)
    footer_font = fit_text(draw, "Silica Sand  •  Quartz  •  Bentonite", 860, "regular", 24, 18)

    draw.text((78, 846), "JADE WAVES ENTERPRISE", font=kicker, fill=SAND)
    draw.text((78, 896), "Export-Ready", font=title1, fill=SAND)
    draw.text((78, 986), "Mineral Supply", font=title2, fill=(244, 232, 219))

    body_text = "From samples to bulk dispatch for global industrial buyers."
    body_lines = wrap_text(draw, body_text, 820, body_font)
    body_y = 1098
    for line in body_lines:
        draw.text((78, body_y), line, font=body_font, fill=MUTED)
        body_y += 42

    draw.text((78, 1196), "Silica Sand  •  Quartz  •  Bentonite", font=footer_font, fill=(202, 211, 219))

    draw_chip(canvas, (78, 1232, 334, 1290), "Samples Available")
    draw_chip(canvas, (354, 1232, 622, 1290), "Export Support")
    draw_chip(canvas, (642, 1232, 930, 1290), "Bulk Dispatch")

    out = OUT_DIR / "export-ready-mineral-supply-post.png"
    canvas.convert("RGB").save(out, quality=95, optimize=True)
    print(out)


if __name__ == "__main__":
    main()
