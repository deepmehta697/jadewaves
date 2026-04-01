from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "output" / "instagram"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SIZE = (1080, 1350)
SHEET_SIZE = (1200, 1500)
NAVY = "#102D49"
NAVY_DEEP = "#0B1A2B"
SAND = "#F4EFE8"
LIGHT = "#FAF8F4"
GOLD = "#B58C45"
MUTED = "#D7E0E8"
TEXT_DARK = "#24384D"
FONT_DIR = Path("/System/Library/Fonts/Supplemental")


VARIANTS = [
    {
        "slug": "product-spotlight",
        "kicker": "PRODUCT SPOTLIGHT",
        "title": "Quartz Sand",
        "subtitle": "From India for ceramics, glass, and engineered stone buyers.",
        "body": ">99% SiO2 options with export-ready packing and size control aligned to your application.",
        "chips": [">99% SiO2", "Custom sizing", "Jumbo Bags"],
        "layout": "classic",
    },
    {
        "slug": "technical-grade",
        "kicker": "TECHNICAL GRADE",
        "title": "Quartz Sand",
        "subtitle": "Purity, whiteness, and sizing built for production consistency.",
        "body": "Available as sand, grits, and powder for ceramic body, glass manufacturing, and engineered stone use.",
        "chips": ["Quartz Grits", "Quartz Powder", "Application fit"],
        "layout": "spec",
    },
    {
        "slug": "buyer-checklist",
        "kicker": "BUYER CHECKLIST",
        "title": "Quartz Sand",
        "subtitle": "Share your end use, target size, and packing preference.",
        "body": "We align sample, technical data, and dispatch planning before the shipment moves.",
        "chips": ["Ceramics", "Glass", "Engineered stone"],
        "layout": "centered",
    },
    {
        "slug": "export-ready",
        "kicker": "EXPORT READY",
        "title": "Quartz Sand",
        "subtitle": "Samples, specs, and Jumbo Bag dispatch coordinated from India.",
        "body": "FOB, CIF, and CNF support for buyers who need clear documents and consistent supply.",
        "chips": ["FOB / CIF / CNF", "Sample support", "Bulk dispatch"],
        "layout": "strip",
    },
]


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
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def cover_image(path: Path, size: tuple[int, int], centering=(0.5, 0.5)) -> Image.Image:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image).convert("RGB")
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=centering)


def contain_image(path: Path, size: tuple[int, int]) -> Image.Image:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image).convert("RGBA")
    return ImageOps.contain(image, size, method=Image.Resampling.LANCZOS)


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


def centered_position(box: tuple[int, int, int, int], size: tuple[int, int]) -> tuple[int, int]:
    x = box[0] + (box[2] - box[0] - size[0]) // 2
    y = box[1] + (box[3] - box[1] - size[1]) // 2
    return x, y


def draw_chip(canvas: Image.Image, box: tuple[int, int, int, int], text: str):
    add_shadow(canvas, box, radius=24, blur=16, opacity=72)
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(box, radius=24, fill=(244, 239, 232, 238), outline=(181, 140, 69, 120), width=2)
    chip_font = fit_text(draw, text, box[2] - box[0] - 32, "bold", 22, 15)
    bbox = draw.textbbox((0, 0), text, font=chip_font)
    x = box[0] + ((box[2] - box[0]) - (bbox[2] - bbox[0])) / 2
    y = box[1] + ((box[3] - box[1]) - (bbox[3] - bbox[1])) / 2 - 2
    draw.text((x, y), text, font=chip_font, fill=NAVY)


def draw_text_block(draw: ImageDraw.ImageDraw, x: int, y: int, lines: list[str], fnt: ImageFont.FreeTypeFont, fill: str, spacing: int):
    current_y = y
    for line in lines:
        draw.text((x, current_y), line, font=fnt, fill=fill)
        current_y += spacing
    return current_y


def create_base_canvas():
    background = cover_image(ROOT / "assets" / "quartz-sand-detail.png", SIZE, centering=(0.5, 0.5)).convert("RGBA")
    background = background.filter(ImageFilter.GaussianBlur(18))
    tint = Image.new("RGBA", SIZE, (240, 236, 229, 208))
    canvas = Image.alpha_composite(background, tint)

    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse((-160, -120, 360, 380), fill=(16, 45, 73, 38))
    od.ellipse((760, -120, 1180, 300), fill=(181, 140, 69, 44))
    od.ellipse((720, 940, 1140, 1320), fill=(16, 45, 73, 34))
    canvas.alpha_composite(overlay)

    draw = ImageDraw.Draw(canvas)

    logo_box = (390, 54, 690, 164)
    add_shadow(canvas, logo_box, radius=28, blur=18, opacity=94)
    draw.rounded_rectangle(logo_box, radius=28, fill=(244, 239, 231, 246), outline=(181, 140, 69, 112), width=2)
    logo = tint_logo(ROOT / "assets" / "jade-waves-logo-transparent.png", (188, 74), (16, 45, 73))
    canvas.alpha_composite(logo, centered_position(logo_box, logo.size))

    product_box = (90, 198, 990, 700)
    add_shadow(canvas, product_box, radius=42, blur=30, opacity=96)
    draw.rounded_rectangle(product_box, radius=42, fill=(250, 248, 244, 245), outline=(255, 255, 255, 162), width=2)
    product_visual = contain_image(ROOT / "assets" / "quartz-sand.png", (780, 430))
    inner_box = (product_box[0] + 54, product_box[1] + 44, product_box[2] - 54, product_box[3] - 44)
    canvas.alpha_composite(product_visual, centered_position(inner_box, product_visual.size))
    return canvas


def draw_classic_variant(canvas: Image.Image, variant: dict):
    draw = ImageDraw.Draw(canvas)
    info_box = (60, 760, 1020, 1290)
    add_shadow(canvas, info_box, radius=40, blur=28, opacity=110)
    draw.rounded_rectangle(info_box, radius=40, fill=(11, 26, 42, 232), outline=(181, 140, 69, 84), width=2)
    draw.rectangle((94, 804, 250, 812), fill=GOLD)

    kicker = font("bold", 21)
    title = fit_text(draw, variant["title"], 840, "bold", 86, 58)
    subtitle = fit_text(draw, variant["subtitle"], 840, "regular", 31, 22)
    body = fit_text(draw, variant["body"], 840, "regular", 27, 20)

    draw.text((94, 830), variant["kicker"], font=kicker, fill=SAND)
    draw.text((94, 878), variant["title"], font=title, fill=SAND)
    subtitle_y = draw_text_block(draw, 94, 990, wrap_text(draw, variant["subtitle"], 840, subtitle), subtitle, "#EDE5D9", 38)
    draw_text_block(draw, 94, subtitle_y + 36, wrap_text(draw, variant["body"], 840, body), body, MUTED, 34)

    chip_boxes = [(94, 1208, 336, 1268), (362, 1208, 636, 1268), (662, 1208, 936, 1268)]
    for box, text in zip(chip_boxes, variant["chips"]):
        draw_chip(canvas, box, text)


def draw_spec_variant(canvas: Image.Image, variant: dict):
    draw = ImageDraw.Draw(canvas)
    info_box = (60, 760, 1020, 1290)
    add_shadow(canvas, info_box, radius=40, blur=28, opacity=110)
    draw.rounded_rectangle(info_box, radius=40, fill=(11, 26, 42, 232), outline=(181, 140, 69, 84), width=2)

    draw.rectangle((94, 804, 250, 812), fill=GOLD)
    kicker = font("bold", 21)
    title = fit_text(draw, variant["title"], 470, "bold", 80, 54)
    subtitle = fit_text(draw, variant["subtitle"], 470, "regular", 28, 20)
    body = fit_text(draw, variant["body"], 470, "regular", 24, 18)

    draw.text((94, 830), variant["kicker"], font=kicker, fill=SAND)
    draw.text((94, 878), variant["title"], font=title, fill=SAND)
    next_y = draw_text_block(draw, 94, 976, wrap_text(draw, variant["subtitle"], 470, subtitle), subtitle, "#EDE5D9", 34)
    draw_text_block(draw, 94, next_y + 36, wrap_text(draw, variant["body"], 470, body), body, MUTED, 30)

    card_boxes = [
        ((618, 842, 948, 954), "Available Forms", variant["chips"][0]),
        ((618, 980, 948, 1092), "Available Forms", variant["chips"][1]),
        ((618, 1118, 948, 1230), "Buyer Fit", variant["chips"][2]),
    ]
    label_font = font("regular", 19)
    value_font = font("bold", 28)
    for box, label, value in card_boxes:
        add_shadow(canvas, box, radius=26, blur=18, opacity=78)
        draw.rounded_rectangle(box, radius=26, fill=(244, 239, 232, 236), outline=(181, 140, 69, 120), width=2)
        draw.text((box[0] + 24, box[1] + 22), label, font=label_font, fill=TEXT_DARK)
        wrapped = wrap_text(draw, value, box[2] - box[0] - 48, value_font)
        draw_text_block(draw, box[0] + 24, box[1] + 50, wrapped[:2], value_font, NAVY, 30)


def draw_centered_variant(canvas: Image.Image, variant: dict):
    draw = ImageDraw.Draw(canvas)
    info_box = (60, 760, 1020, 1290)
    add_shadow(canvas, info_box, radius=40, blur=28, opacity=110)
    draw.rounded_rectangle(info_box, radius=40, fill=(248, 245, 239, 242), outline=(181, 140, 69, 84), width=2)

    kicker = font("bold", 21)
    title = fit_text(draw, variant["title"], 860, "bold", 86, 58)
    subtitle = fit_text(draw, variant["subtitle"], 860, "regular", 30, 22)
    body = fit_text(draw, variant["body"], 780, "regular", 24, 18)

    bbox = draw.textbbox((0, 0), variant["kicker"], font=kicker)
    draw.rectangle((460, 810, 620, 818), fill=GOLD)
    draw.text(((SIZE[0] - (bbox[2] - bbox[0])) / 2, 836), variant["kicker"], font=kicker, fill=TEXT_DARK)

    title_bbox = draw.textbbox((0, 0), variant["title"], font=title)
    draw.text(((SIZE[0] - (title_bbox[2] - title_bbox[0])) / 2, 886), variant["title"], font=title, fill=NAVY_DEEP)

    subtitle_lines = wrap_text(draw, variant["subtitle"], 820, subtitle)
    current_y = 992
    for line in subtitle_lines:
        line_bbox = draw.textbbox((0, 0), line, font=subtitle)
        draw.text(((SIZE[0] - (line_bbox[2] - line_bbox[0])) / 2, current_y), line, font=subtitle, fill="#42586C")
        current_y += 36

    body_lines = wrap_text(draw, variant["body"], 760, body)
    current_y += 34
    for line in body_lines:
        line_bbox = draw.textbbox((0, 0), line, font=body)
        draw.text(((SIZE[0] - (line_bbox[2] - line_bbox[0])) / 2, current_y), line, font=body, fill="#5B6E7D")
        current_y += 30

    chip_boxes = [(104, 1208, 346, 1268), (419, 1208, 661, 1268), (734, 1208, 976, 1268)]
    for box, text in zip(chip_boxes, variant["chips"]):
        draw_chip(canvas, box, text)


def draw_strip_variant(canvas: Image.Image, variant: dict):
    draw = ImageDraw.Draw(canvas)
    header_box = (60, 760, 1020, 1030)
    footer_box = (60, 1048, 1020, 1290)
    add_shadow(canvas, header_box, radius=38, blur=24, opacity=102)
    add_shadow(canvas, footer_box, radius=38, blur=24, opacity=102)
    draw.rounded_rectangle(header_box, radius=38, fill=(11, 26, 42, 232), outline=(181, 140, 69, 84), width=2)
    draw.rounded_rectangle(footer_box, radius=38, fill=(248, 245, 239, 242), outline=(181, 140, 69, 84), width=2)

    kicker = font("bold", 21)
    title = fit_text(draw, variant["title"], 840, "bold", 84, 56)
    subtitle = fit_text(draw, variant["subtitle"], 840, "regular", 30, 22)
    draw.rectangle((94, 804, 250, 812), fill=GOLD)
    draw.text((94, 830), variant["kicker"], font=kicker, fill=SAND)
    draw.text((94, 878), variant["title"], font=title, fill=SAND)
    draw_text_block(draw, 94, 972, wrap_text(draw, variant["subtitle"], 830, subtitle), subtitle, "#EDE5D9", 36)

    body = fit_text(draw, variant["body"], 840, "regular", 27, 18)
    draw_text_block(draw, 94, 1088, wrap_text(draw, variant["body"], 840, body), body, TEXT_DARK, 32)

    chip_boxes = [(94, 1208, 374, 1268), (400, 1208, 680, 1268), (706, 1208, 986, 1268)]
    for box, text in zip(chip_boxes, variant["chips"]):
        draw_chip(canvas, box, text)


def create_variant(variant: dict):
    canvas = create_base_canvas()
    if variant["layout"] == "classic":
        draw_classic_variant(canvas, variant)
    elif variant["layout"] == "spec":
        draw_spec_variant(canvas, variant)
    elif variant["layout"] == "centered":
        draw_centered_variant(canvas, variant)
    else:
        draw_strip_variant(canvas, variant)

    out = OUT_DIR / f"quartz-sand-{variant['slug']}.png"
    canvas.convert("RGB").save(out, quality=95, optimize=True)
    return out


def create_contact_sheet(paths: list[Path]):
    sheet = Image.new("RGB", SHEET_SIZE, "#EFEAE3")
    draw = ImageDraw.Draw(sheet)
    margin = 50
    gap = 36
    card_w = (SHEET_SIZE[0] - (margin * 2) - gap) // 2
    card_h = (SHEET_SIZE[1] - (margin * 2) - gap) // 2
    title_font = font("bold", 24)

    for index, path in enumerate(paths):
        row = index // 2
        col = index % 2
        x = margin + col * (card_w + gap)
        y = margin + row * (card_h + gap)
        card_box = (x, y, x + card_w, y + card_h)
        shadow_canvas = Image.new("RGBA", SHEET_SIZE, (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow_canvas)
        shadow_draw.rounded_rectangle(card_box, radius=26, fill=(0, 0, 0, 80))
        shadow_canvas = shadow_canvas.filter(ImageFilter.GaussianBlur(18))
        sheet = Image.alpha_composite(sheet.convert("RGBA"), shadow_canvas).convert("RGB")

        draw = ImageDraw.Draw(sheet)
        draw.rounded_rectangle(card_box, radius=26, fill=LIGHT, outline=(181, 140, 69), width=2)
        preview = Image.open(path).convert("RGB")
        preview = ImageOps.fit(preview, (card_w - 28, card_h - 84), method=Image.Resampling.LANCZOS, centering=(0.5, 0.0))
        sheet.paste(preview, (x + 14, y + 14))
        label = path.stem.replace("quartz-sand-", "").replace("-", " ").title()
        draw.text((x + 20, y + card_h - 54), label, font=title_font, fill=NAVY)

    out = OUT_DIR / "quartz-sand-variant-sheet.png"
    sheet.save(out, quality=95, optimize=True)
    return out


def main():
    paths = [create_variant(variant) for variant in VARIANTS]
    sheet = create_contact_sheet(paths)
    for path in paths:
        print(path)
    print(sheet)


if __name__ == "__main__":
    main()
