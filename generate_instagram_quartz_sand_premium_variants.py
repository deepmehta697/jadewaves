from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "output" / "instagram"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SIZE = (1080, 1350)
SHEET_SIZE = (1200, 1500)
NAVY = "#102D49"
NAVY_DEEP = "#0B1A2B"
CREAM = "#F5F0E8"
WARM = "#E9DFD0"
GOLD = "#B58C45"
STONE = "#D8CCBC"
SLATE = "#56687A"
WHITE = "#FBFAF7"
FONT_DIR = Path("/System/Library/Fonts/Supplemental")


VARIANTS = [
    {
        "slug": "editorial",
        "eyebrow": "INDUSTRIAL MINERAL",
        "title": "Quartz Sand",
        "subhead": "Purity and size control for ceramic, glass, and engineered stone production.",
        "body": "Export-ready supply from India with >99% SiO2 options, sample support, and shipment planning aligned to your application.",
        "accent": ">99% SiO2",
        "layout": "editorial",
    },
    {
        "slug": "spec-sheet",
        "eyebrow": "TECHNICAL SUPPLY",
        "title": "Quartz Sand",
        "subhead": "Available as sand, grits, and powder.",
        "body": "A cleaner product-led layout for buyers who care about application fit, whiteness, and dispatch clarity.",
        "accent": "Sand  •  Grits  •  Powder",
        "layout": "spec_sheet",
    },
    {
        "slug": "campaign",
        "eyebrow": "EXPORT READY FROM INDIA",
        "title": "Quartz Sand",
        "subhead": "Samples, specs, and bulk dispatch on one clear track.",
        "body": "Built for B2B buyers in ceramics, glass, and engineered stone who need dependable product coordination before shipment.",
        "accent": "Ceramics  •  Glass  •  Engineered Stone",
        "layout": "campaign",
    },
]


def font(name: str, size: int):
    mapping = {
        "sans_bold": FONT_DIR / "Arial Bold.ttf",
        "sans": FONT_DIR / "Arial.ttf",
        "display": FONT_DIR / "Baskerville.ttc",
        "display_alt": FONT_DIR / "Didot.ttc",
        "geo": FONT_DIR / "Georgia.ttf",
        "future": FONT_DIR / "Futura.ttc",
        "gill": FONT_DIR / "GillSans.ttc",
    }
    return ImageFont.truetype(str(mapping[name]), size=size)


def fit_text(draw: ImageDraw.ImageDraw, text: str, max_width: int, style: str, start_size: int, min_size: int):
    size = start_size
    while size >= min_size:
        current_font = font(style, size)
        if draw.textbbox((0, 0), text, font=current_font)[2] <= max_width:
            return current_font
        size -= 2
    return font(style, min_size)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, max_width: int, current_font: ImageFont.FreeTypeFont):
    words = text.split()
    lines = []
    current = []
    for word in words:
        trial = " ".join(current + [word])
        if draw.textbbox((0, 0), trial, font=current_font)[2] <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def contain_image(path: Path, size: tuple[int, int]) -> Image.Image:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image).convert("RGBA")
    return ImageOps.contain(image, size, method=Image.Resampling.LANCZOS)


def cover_image(path: Path, size: tuple[int, int], centering=(0.5, 0.5)) -> Image.Image:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image).convert("RGB")
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=centering)


def add_shadow(canvas: Image.Image, box: tuple[int, int, int, int], radius: int, blur: int = 28, opacity: int = 88):
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle(box, radius=radius, fill=(0, 0, 0, opacity))
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
    tinted = Image.new("RGBA", logo.size, rgb + (255,))
    tinted.putalpha(alpha)
    return tinted


def centered_position(box: tuple[int, int, int, int], size: tuple[int, int]) -> tuple[int, int]:
    return (
        box[0] + (box[2] - box[0] - size[0]) // 2,
        box[1] + (box[3] - box[1] - size[1]) // 2,
    )


def draw_lines(draw: ImageDraw.ImageDraw):
    draw.line((90, 186, 990, 186), fill=(181, 140, 69, 92), width=2)
    draw.line((90, 1166, 990, 1166), fill=(181, 140, 69, 92), width=2)


def create_base():
    background = cover_image(ROOT / "assets" / "quartz-sand-detail.png", SIZE, centering=(0.5, 0.5)).convert("RGBA")
    background = background.filter(ImageFilter.GaussianBlur(24))
    cream = Image.new("RGBA", SIZE, (245, 240, 232, 224))
    canvas = Image.alpha_composite(background, cream)

    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.ellipse((-120, -120, 280, 280), fill=(16, 45, 73, 22))
    overlay_draw.ellipse((780, -60, 1150, 310), fill=(181, 140, 69, 26))
    overlay_draw.ellipse((820, 1060, 1140, 1360), fill=(16, 45, 73, 20))
    canvas.alpha_composite(overlay)

    draw = ImageDraw.Draw(canvas)
    draw_lines(draw)

    logo_box = (388, 50, 692, 156)
    add_shadow(canvas, logo_box, radius=26, blur=16, opacity=70)
    draw.rounded_rectangle(logo_box, radius=26, fill=(251, 250, 247, 242), outline=(181, 140, 69, 118), width=2)
    logo = tint_logo(ROOT / "assets" / "jade-waves-logo-transparent.png", (190, 74), (16, 45, 73))
    canvas.alpha_composite(logo, centered_position(logo_box, logo.size))
    return canvas


def draw_editorial_variant(variant: dict):
    canvas = create_base()
    draw = ImageDraw.Draw(canvas)

    product_box = (120, 238, 960, 770)
    add_shadow(canvas, product_box, radius=34, blur=24, opacity=76)
    draw.rounded_rectangle(product_box, radius=34, fill=(251, 250, 247, 240), outline=(216, 204, 188, 160), width=2)
    product = contain_image(ROOT / "assets" / "quartz-sand.png", (650, 380))
    canvas.alpha_composite(product, centered_position((150, 272, 930, 700), product.size))

    eyebrow_font = font("future", 23)
    title_font = fit_text(draw, variant["title"], 760, "display_alt", 88, 58)
    subhead_font = fit_text(draw, variant["subhead"], 760, "gill", 30, 20)
    body_font = fit_text(draw, variant["body"], 760, "sans", 24, 18)
    accent_font = fit_text(draw, variant["accent"], 260, "future", 28, 18)

    draw.text((120, 832), variant["eyebrow"], font=eyebrow_font, fill=SLATE)
    draw.rectangle((120, 868, 282, 876), fill=GOLD)
    draw.text((120, 898), variant["title"], font=title_font, fill=NAVY_DEEP)
    next_y = 1002
    for line in wrap_text(draw, variant["subhead"], 820, subhead_font):
        draw.text((120, next_y), line, font=subhead_font, fill="#53677A")
        next_y += 36
    next_y += 24
    for line in wrap_text(draw, variant["body"], 820, body_font):
        draw.text((120, next_y), line, font=body_font, fill="#66798A")
        next_y += 30

    accent_box = (120, next_y + 16, 354, next_y + 92)
    add_shadow(canvas, accent_box, radius=20, blur=14, opacity=54)
    draw.rounded_rectangle(accent_box, radius=20, fill=(16, 45, 73, 235), outline=(181, 140, 69, 120), width=2)
    accent_bbox = draw.textbbox((0, 0), variant["accent"], font=accent_font)
    accent_x = accent_box[0] + ((accent_box[2] - accent_box[0]) - (accent_bbox[2] - accent_bbox[0])) / 2
    accent_y = accent_box[1] + ((accent_box[3] - accent_box[1]) - (accent_bbox[3] - accent_bbox[1])) / 2 - 2
    draw.text((accent_x, accent_y), variant["accent"], font=accent_font, fill=WHITE)
    return canvas


def draw_spec_sheet_variant(variant: dict):
    canvas = create_base()
    draw = ImageDraw.Draw(canvas)

    panel_box = (86, 238, 994, 1248)
    add_shadow(canvas, panel_box, radius=36, blur=26, opacity=72)
    draw.rounded_rectangle(panel_box, radius=36, fill=(11, 26, 42, 240), outline=(181, 140, 69, 88), width=2)

    photo_box = (126, 284, 954, 666)
    draw.rounded_rectangle(photo_box, radius=28, fill=(247, 244, 238, 240), outline=(255, 255, 255, 110), width=2)
    product = contain_image(ROOT / "assets" / "quartz-sand.png", (600, 300))
    canvas.alpha_composite(product, centered_position((156, 320, 924, 630), product.size))

    eyebrow_font = font("future", 22)
    title_font = fit_text(draw, variant["title"], 420, "display", 78, 56)
    subhead_font = fit_text(draw, variant["subhead"], 420, "gill", 28, 18)
    body_font = fit_text(draw, variant["body"], 420, "sans", 22, 16)
    stat_label_font = font("future", 18)
    stat_value_font = fit_text(draw, variant["accent"], 300, "gill", 28, 18)

    draw.text((126, 736), variant["eyebrow"], font=eyebrow_font, fill="#D8E0E7")
    draw.rectangle((126, 770, 284, 778), fill=GOLD)
    draw.text((126, 802), variant["title"], font=title_font, fill=WHITE)

    current_y = 892
    for line in wrap_text(draw, variant["subhead"], 420, subhead_font):
        draw.text((126, current_y), line, font=subhead_font, fill="#D8E0E7")
        current_y += 34
    current_y += 28
    for line in wrap_text(draw, variant["body"], 420, body_font):
        draw.text((126, current_y), line, font=body_font, fill="#AFC0CC")
        current_y += 28

    stats = [
        ("AVAILABLE FORMS", "Quartz Sand"),
        ("AVAILABLE FORMS", "Quartz Grits"),
        ("AVAILABLE FORMS", "Quartz Powder"),
        ("BUYER FIT", "Production-led supply"),
    ]
    boxes = [
        (630, 782, 930, 878),
        (630, 900, 930, 996),
        (630, 1018, 930, 1114),
        (630, 1136, 930, 1232),
    ]
    for (label, value), box in zip(stats, boxes):
        add_shadow(canvas, box, radius=24, blur=16, opacity=60)
        draw.rounded_rectangle(box, radius=24, fill=(247, 244, 238, 240), outline=(181, 140, 69, 124), width=2)
        draw.text((box[0] + 24, box[1] + 18), label, font=stat_label_font, fill=SLATE)
        value_font = fit_text(draw, value, box[2] - box[0] - 48, "gill", 30, 18)
        draw.text((box[0] + 24, box[1] + 44), value, font=value_font, fill=NAVY)
    return canvas


def draw_campaign_variant(variant: dict):
    canvas = create_base()
    draw = ImageDraw.Draw(canvas)

    image_box = (94, 232, 986, 720)
    add_shadow(canvas, image_box, radius=42, blur=26, opacity=70)
    draw.rounded_rectangle(image_box, radius=42, fill=(251, 250, 247, 240), outline=(216, 204, 188, 160), width=2)
    product = contain_image(ROOT / "assets" / "quartz-sand.png", (700, 360))
    canvas.alpha_composite(product, centered_position((130, 270, 950, 684), product.size))

    band_box = (46, 810, 1034, 1118)
    add_shadow(canvas, band_box, radius=34, blur=22, opacity=86)
    draw.rounded_rectangle(band_box, radius=34, fill=(11, 26, 42, 236), outline=(181, 140, 69, 100), width=2)

    eyebrow_font = font("future", 22)
    title_font = fit_text(draw, variant["title"], 780, "display_alt", 86, 58)
    subhead_font = fit_text(draw, variant["subhead"], 780, "gill", 30, 20)
    body_font = fit_text(draw, variant["body"], 880, "sans", 22, 17)
    accent_font = fit_text(draw, variant["accent"], 860, "future", 23, 16)

    draw.text((86, 850), variant["eyebrow"], font=eyebrow_font, fill="#D9E1E8")
    draw.rectangle((86, 886, 262, 894), fill=GOLD)
    draw.text((86, 916), variant["title"], font=title_font, fill=WHITE)
    current_y = 1006
    for line in wrap_text(draw, variant["subhead"], 860, subhead_font):
        draw.text((86, current_y), line, font=subhead_font, fill="#D8E0E7")
        current_y += 34

    footer_box = (94, 1150, 986, 1272)
    add_shadow(canvas, footer_box, radius=28, blur=18, opacity=58)
    draw.rounded_rectangle(footer_box, radius=28, fill=(251, 250, 247, 242), outline=(181, 140, 69, 118), width=2)
    for line in wrap_text(draw, variant["body"], 838, body_font):
        draw.text((126, 1180), line, font=body_font, fill=SLATE)
        break
    accent_bbox = draw.textbbox((0, 0), variant["accent"], font=accent_font)
    accent_x = footer_box[0] + ((footer_box[2] - footer_box[0]) - (accent_bbox[2] - accent_bbox[0])) / 2
    draw.text((accent_x, 1230), variant["accent"], font=accent_font, fill=NAVY)
    return canvas


def render_variant(variant: dict):
    if variant["layout"] == "editorial":
        canvas = draw_editorial_variant(variant)
    elif variant["layout"] == "spec_sheet":
        canvas = draw_spec_sheet_variant(variant)
    else:
        canvas = draw_campaign_variant(variant)

    out = OUT_DIR / f"quartz-sand-premium-{variant['slug']}.png"
    canvas.convert("RGB").save(out, quality=95, optimize=True)
    return out


def create_contact_sheet(paths: list[Path]):
    sheet = Image.new("RGB", SHEET_SIZE, "#EFE7DD")
    draw = ImageDraw.Draw(sheet)
    margin = 48
    gap = 34
    cols = 2
    rows = 2
    card_w = (SHEET_SIZE[0] - (margin * 2) - gap) // cols
    card_h = (SHEET_SIZE[1] - (margin * 2) - gap) // rows
    label_font = font("future", 21)

    for index, path in enumerate(paths):
        row = index // 2
        col = index % 2
        if len(paths) % 2 == 1 and index == len(paths) - 1:
            row = len(paths) // 2
            col = 0
        x = margin + col * (card_w + gap)
        if len(paths) % 2 == 1 and index == len(paths) - 1:
            x = (SHEET_SIZE[0] - card_w) // 2
        y = margin + row * (card_h + gap)
        box = (x, y, x + card_w, y + card_h)
        preview = Image.open(path).convert("RGB")
        preview = ImageOps.fit(preview, (card_w - 22, card_h - 72), method=Image.Resampling.LANCZOS, centering=(0.5, 0.0))
        draw.rounded_rectangle(box, radius=26, fill=WHITE, outline=(181, 140, 69), width=2)
        sheet.paste(preview, (x + 11, y + 11))
        label = path.stem.replace("quartz-sand-premium-", "").replace("-", " ").title()
        draw.text((x + 18, y + card_h - 46), label, font=label_font, fill=NAVY)
    return sheet


def main():
    outputs = [render_variant(variant) for variant in VARIANTS]
    sheet = create_contact_sheet(outputs)
    sheet_path = OUT_DIR / "quartz-sand-premium-variant-sheet.png"
    sheet.save(sheet_path, quality=95, optimize=True)
    for output in outputs:
        print(output)
    print(sheet_path)


if __name__ == "__main__":
    main()
