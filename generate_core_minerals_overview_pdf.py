from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output" / "pdf" / "jade-waves-core-minerals-overview.pdf"

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 42
CONTENT_X = MARGIN + 20
CONTENT_Y = MARGIN + 24
CONTENT_W = PAGE_WIDTH - 2 * CONTENT_X

INK = colors.HexColor("#13243C")
INK_SOFT = colors.HexColor("#4F5E70")
SAND = colors.HexColor("#F4EFE8")
STONE = colors.HexColor("#E5DDD1")
PANEL = colors.HexColor("#F8F4EE")
PANEL_WARM = colors.HexColor("#F2EBE0")
GOLD = colors.HexColor("#B58C45")
WHITE = colors.white

IMAGE_CACHE: dict[tuple[str, int], ImageReader] = {}

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.1,
        leading=14.1,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyTight",
        parent=styles["Body"],
        fontSize=9.2,
        leading=12.2,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyTiny",
        parent=styles["Body"],
        fontSize=8.5,
        leading=10.8,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyTinyTight",
        parent=styles["BodyTiny"],
        fontSize=7.8,
        leading=9.6,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyMuted",
        parent=styles["Body"],
        textColor=INK_SOFT,
    )
)
styles.add(
    ParagraphStyle(
        name="Kicker",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=12,
        textColor=GOLD,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="SectionTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=21,
        leading=25,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="SubTitle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="CardEyebrow",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=7.9,
        leading=10.0,
        textColor=GOLD,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="CardTitle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=15.5,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="WhiteTitle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=15.5,
        textColor=WHITE,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="WhiteBody",
        parent=styles["Body"],
        fontName="Helvetica",
        fontSize=9.2,
        leading=12.2,
        textColor=WHITE,
        spaceAfter=0,
    )
)


PORTFOLIO_FAMILIES = [
    {
        "index": "01",
        "count": "4 products",
        "title": "Silica, Quartz & Feldspar",
        "summary": "Purity-led grades for glass, ceramics, filtration, and engineered stone demand.",
        "pills": ["Glass", "Ceramics", "Filtration", "Engineered Stone"],
    },
    {
        "index": "02",
        "count": "3 products",
        "title": "Clays & Functional Fillers",
        "summary": "Functional minerals for drilling, coatings, absorbents, ceramics, and process use.",
        "pills": ["Drilling", "Ceramics", "Coatings", "Absorbents"],
    },
    {
        "index": "03",
        "count": "1 product",
        "title": "Industrial Salt Grades",
        "summary": "Salt grades arranged for chemical processing, treatment systems, utilities, and volume buying.",
        "pills": ["Chemical Processing", "Water Treatment", "Utilities"],
    },
    {
        "index": "04",
        "count": "2 products",
        "title": "Construction & Industrial Media",
        "summary": "Media and mineral inputs for concrete, blasting, infrastructure, and site-led demand.",
        "pills": ["Concrete", "Blasting", "Infrastructure"],
    },
]


SILICA_FAMILY = [
    {
        "eyebrow": "Glass / Filtration / Foundry / Construction",
        "name": "Silica Sand",
        "fit": "Best for glass manufacturing and water filtration media.",
        "key": "Published guide: SiO2 98-99%. Fe2O3 can be aligned for glass use. Grain size and packing are set against the end use.",
        "packs": ["50 Kg", "Jumbo Bags"],
    },
    {
        "eyebrow": "Ceramics / Coatings / Fillers / Construction",
        "name": "Silica Flour",
        "fit": "Best for ceramics, tile bodies, coatings, and controlled filler use.",
        "key": "Published guide: 80 mesh, 300 mesh, 500 mesh, and custom micron grading. SiO2 reported at 99.10%.",
        "packs": ["50 Kg", "Jumbo Bags"],
    },
    {
        "eyebrow": "Ceramics / Glass / Engineered Stone",
        "name": "Quartz Sand",
        "fit": "Best for tiles, ceramic body production, glass, and engineered stone.",
        "key": "Published guide: SiO2 above 99.0%, K2O 0.02% max, with grits, sand, and powder aligned to use.",
        "packs": ["Jumbo Bags"],
    },
    {
        "eyebrow": "Ceramics / Sanitaryware / Glass",
        "name": "Feldspar",
        "fit": "Best for ceramic and tile production, sanitaryware, and glass batches.",
        "key": "Published guide: Potash grades up to 12% K2O and soda grades up to 10% Na2O. Mesh and iron limits are aligned before dispatch.",
        "packs": ["Jumbo Bags"],
    },
]


CLAYS_FAMILY = [
    {
        "eyebrow": "Drilling / Foundry / Civil / Absorbent Grades",
        "name": "Bentonite",
        "fit": "Used where swelling, binding, viscosity, and moisture control matter.",
        "key": "Published guide: sodium or calcium grade can be aligned to drilling, foundry, civil, or absorbent applications. Packing: 50 Kg or jumbo bags.",
        "packs": ["50 Kg", "Jumbo Bags"],
    },
    {
        "eyebrow": "Ceramics / Coatings / Paper / Fillers",
        "name": "Kaolin (China Clay)",
        "fit": "Best for ceramics, tiles, coatings, paper systems, and industrial filler use.",
        "key": "Published guide: brightness target, Fe2O3 limit, and Al2O3 / SiO2 profile are confirmed before order locking. Packing: 50 Kg or jumbo bags.",
        "packs": ["50 Kg", "Jumbo Bags"],
    },
    {
        "eyebrow": "Plastics / Paints / Ceramics / Rubber",
        "name": "Talc",
        "fit": "Best for plastics, coatings, ceramics, rubber, cable, and detergent-linked fillers.",
        "key": "Published guide: application-specific mesh sizes, whiteness target, and MgO / SiO2 profile are matched to formulation needs. Packing: jumbo bags.",
        "packs": ["Jumbo Bags"],
    },
]


INDUSTRIAL_MEDIA = [
    {
        "eyebrow": "Chemical / Water Treatment / Utility / Food-Linked Supply",
        "name": "Salt",
        "fit": "Used in chemical processing, water treatment, utility demand, and food-linked supply chains.",
        "key": "Published guide: iodized and non-iodized grades, NaCl purity, iodine requirement, grain size, and monthly volume are aligned early. Packing: 50 Kg or jumbo bags.",
        "packs": ["50 Kg", "Jumbo Bags"],
    },
    {
        "eyebrow": "Concrete / Cement / Blocks / Roads",
        "name": "Fly Ash",
        "fit": "Best for cement, concrete, bricks, blocks, roads, and infrastructure mix design.",
        "key": "Published guide: SiO2 55.13%, Al2O3 24.45%, LOI below 1%, with packing and dispatch linked to the application schedule. Packing: jumbo bags.",
        "packs": ["Jumbo Bags"],
    },
    {
        "eyebrow": "Blasting / Surface Preparation / Construction",
        "name": "Copper Slag",
        "fit": "Best for abrasive blasting, surface preparation, and construction-linked media use.",
        "key": "Published guide: sieve size distribution, density, hardness, angular grain profile, and shipment volume are confirmed before dispatch. Packing: jumbo bags.",
        "packs": ["Jumbo Bags"],
    },
]


def draw_page_bg(pdf: canvas.Canvas) -> None:
    pdf.setFillColor(SAND)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    pdf.setFillColor(WHITE)
    pdf.roundRect(MARGIN, MARGIN, PAGE_WIDTH - 2 * MARGIN, PAGE_HEIGHT - 2 * MARGIN, 18, fill=1, stroke=0)


def draw_footer(pdf: canvas.Canvas, page_number: int) -> None:
    pdf.setStrokeColor(STONE)
    pdf.setLineWidth(1)
    pdf.line(MARGIN, 34, PAGE_WIDTH - MARGIN, 34)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica", 9)
    pdf.drawString(MARGIN, 20, "jadewavesenterprise.com")
    pdf.drawRightString(PAGE_WIDTH - MARGIN, 20, f"Page {page_number}")


def paragraph_height(text: str, style_name: str, width: float) -> float:
    paragraph = Paragraph(text, styles[style_name])
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    return height


def draw_paragraph(pdf: canvas.Canvas, text: str, style_name: str, x: float, y_top: float, width: float) -> float:
    paragraph = Paragraph(text, styles[style_name])
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    paragraph.drawOn(pdf, x, y_top - height)
    return y_top - height


def draw_paragraph_fit(
    pdf: canvas.Canvas,
    text: str,
    style_names: list[str],
    x: float,
    y_top: float,
    width: float,
    max_height: float,
) -> float:
    chosen = style_names[-1]
    chosen_height = 0.0
    for style_name in style_names:
        height = paragraph_height(text, style_name, width)
        chosen = style_name
        chosen_height = height
        if height <= max_height:
            break

    fitted_text = text
    if chosen_height > max_height:
        words = text.split()
        while words:
            trial = " ".join(words).rstrip(" .,;:") + "..."
            height = paragraph_height(trial, chosen, width)
            if height <= max_height:
                fitted_text = trial
                break
            words.pop()

    paragraph = Paragraph(fitted_text, styles[chosen])
    _, final_height = paragraph.wrap(width, max_height)
    paragraph.drawOn(pdf, x, y_top - final_height)
    return y_top - final_height


def draw_card(pdf: canvas.Canvas, x: float, y: float, width: float, height: float, fill_color=PANEL) -> None:
    pdf.setFillColor(fill_color)
    pdf.roundRect(x, y, width, height, 16, fill=1, stroke=0)


def draw_pills(pdf: canvas.Canvas, labels: list[str], x: float, y_top: float, max_width: float) -> float:
    cursor_x = x
    cursor_y = y_top
    row_height = 22
    for label in labels:
        pill_w = stringWidth(label, "Helvetica-Bold", 8.3) + 18
        if cursor_x + pill_w > x + max_width:
            cursor_x = x
            cursor_y -= row_height
        pdf.setFillColor(colors.HexColor("#F6F1E9"))
        pdf.roundRect(cursor_x, cursor_y - 18, pill_w, 18, 9, fill=1, stroke=0)
        pdf.setFillColor(INK)
        pdf.setFont("Helvetica-Bold", 8.3)
        pdf.drawString(cursor_x + 9, cursor_y - 12.4, label)
        cursor_x += pill_w + 8
    return cursor_y - row_height + 6


def draw_white_pills(pdf: canvas.Canvas, labels: list[str], x: float, y_top: float, max_width: float) -> float:
    cursor_x = x
    cursor_y = y_top
    row_height = 22
    for label in labels:
        pill_w = stringWidth(label, "Helvetica-Bold", 8.3) + 18
        if cursor_x + pill_w > x + max_width:
            cursor_x = x
            cursor_y -= row_height
        pdf.setFillColor(colors.HexColor("#2C3C54"))
        pdf.roundRect(cursor_x, cursor_y - 18, pill_w, 18, 9, fill=1, stroke=0)
        pdf.setFillColor(WHITE)
        pdf.setFont("Helvetica-Bold", 8.3)
        pdf.drawString(cursor_x + 9, cursor_y - 12.4, label)
        cursor_x += pill_w + 8
    return cursor_y - row_height + 6


def get_pdf_image(image_path: Path, max_px: int = 1400) -> ImageReader:
    cache_key = (str(image_path), max_px)
    cached = IMAGE_CACHE.get(cache_key)
    if cached is not None:
        return cached

    with Image.open(image_path) as image:
        image = ImageOps.exif_transpose(image)
        image.thumbnail((max_px, max_px))
        buffer = BytesIO()
        if image.mode in ("RGBA", "LA") or ("transparency" in image.info):
            image.save(buffer, format="PNG", optimize=True)
        else:
            image = image.convert("RGB")
            image.save(buffer, format="JPEG", quality=74, optimize=True)
        buffer.seek(0)
        reader = ImageReader(buffer)
        IMAGE_CACHE[cache_key] = reader
        return reader


def draw_image_cover(pdf: canvas.Canvas, image_path: Path, x: float, y: float, width: float, height: float, radius: float = 16) -> None:
    image = get_pdf_image(image_path)
    image_w, image_h = image.getSize()
    scale = max(width / image_w, height / image_h)
    draw_w = image_w * scale
    draw_h = image_h * scale
    draw_x = x - (draw_w - width) / 2
    draw_y = y - (draw_h - height) / 2
    pdf.saveState()
    path = pdf.beginPath()
    path.roundRect(x, y, width, height, radius)
    pdf.clipPath(path, stroke=0, fill=0)
    pdf.drawImage(image, draw_x, draw_y, draw_w, draw_h, preserveAspectRatio=True, mask="auto")
    pdf.restoreState()


def draw_image_grid_2x2(pdf: canvas.Canvas, paths: list[Path], x: float, y: float, width: float, height: float) -> None:
    gap = 10
    cell_w = (width - gap) / 2
    cell_h = (height - gap) / 2
    positions = [
        (x, y + cell_h + gap),
        (x + cell_w + gap, y + cell_h + gap),
        (x, y),
        (x + cell_w + gap, y),
    ]
    for image_path, (cell_x, cell_y) in zip(paths, positions):
        draw_image_cover(pdf, image_path, cell_x, cell_y, cell_w, cell_h, radius=16)


def draw_image_row(pdf: canvas.Canvas, paths: list[Path], x: float, y: float, width: float, height: float) -> None:
    gap = 10
    cell_w = (width - gap * (len(paths) - 1)) / len(paths)
    cursor_x = x
    for image_path in paths:
        draw_image_cover(pdf, image_path, cursor_x, y, cell_w, height, radius=16)
        cursor_x += cell_w + gap


def draw_family_card(pdf: canvas.Canvas, family: dict[str, object], x: float, y: float, width: float, height: float) -> None:
    draw_card(pdf, x, y, width, height, fill_color=PANEL)
    top = y + height - 16
    top = draw_paragraph(pdf, str(family["index"]), "CardEyebrow", x + 16, top, width - 32) - 2
    top = draw_paragraph(pdf, str(family["count"]), "BodyTiny", x + 16, top, width - 32) - 6
    top = draw_paragraph_fit(pdf, str(family["title"]), ["CardTitle", "SubTitle"], x + 16, top, width - 32, 34) - 8
    top = draw_paragraph_fit(pdf, str(family["summary"]), ["BodyTiny", "BodyTinyTight"], x + 16, top, width - 32, 34) - 10
    draw_pills(pdf, list(family["pills"]), x + 16, top, width - 32)


def draw_product_card(pdf: canvas.Canvas, product: dict[str, object], x: float, y: float, width: float, height: float) -> None:
    draw_card(pdf, x, y, width, height)
    top = y + height - 16
    top = draw_paragraph_fit(pdf, str(product["eyebrow"]), ["CardEyebrow", "BodyTinyTight"], x + 16, top, width - 32, 22) - 6
    top = draw_paragraph_fit(pdf, str(product["name"]), ["CardTitle", "SubTitle"], x + 16, top, width - 32, 22) - 6
    top = draw_paragraph_fit(pdf, str(product["fit"]), ["BodyTight", "BodyTiny"], x + 16, top, width - 32, 36) - 8
    bottom_for_pills = y + 18
    top_limit = top - bottom_for_pills
    draw_paragraph_fit(pdf, str(product["key"]), ["BodyTiny", "BodyTinyTight"], x + 16, top, width - 32, max(top_limit, 22))
    draw_pills(pdf, list(product["packs"]), x + 16, y + 28, width - 32)


def draw_product_strip(pdf: canvas.Canvas, product: dict[str, object], x: float, y: float, width: float, height: float) -> None:
    draw_card(pdf, x, y, width, height)
    text_x = x + 16
    top = y + height - 16
    top = draw_paragraph_fit(pdf, str(product["eyebrow"]), ["CardEyebrow", "BodyTinyTight"], text_x, top, width - 32, 20) - 4
    top = draw_paragraph_fit(pdf, str(product["name"]), ["CardTitle", "SubTitle"], text_x, top, width - 32, 22) - 5
    top = draw_paragraph_fit(pdf, str(product["fit"]), ["BodyTight", "BodyTiny"], text_x, top, width - 32, 24) - 6
    draw_paragraph_fit(pdf, str(product["key"]), ["BodyTiny", "BodyTinyTight"], text_x, top, width - 32, max(top - (y + 18), 20))


def cover_page(pdf: canvas.Canvas) -> None:
    draw_page_bg(pdf)

    logo = ROOT / "assets" / "jade-waves-logo-transparent.png"
    pdf.drawImage(str(logo), CONTENT_X, PAGE_HEIGHT - 98, width=104, height=68, mask="auto", preserveAspectRatio=True)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(CONTENT_X + 110, PAGE_HEIGHT - 59, "Jade Waves Enterprise")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(CONTENT_X + 110, PAGE_HEIGHT - 75, "Industrial mineral exports from India")

    left_w = 240
    right_w = CONTENT_W - left_w - 20
    top = PAGE_HEIGHT - 134
    top = draw_paragraph(pdf, "PORTFOLIO", "Kicker", CONTENT_X, top, left_w) - 8
    top = draw_paragraph(pdf, "Core Minerals Overview", "SectionTitle", CONTENT_X, top, left_w) - 12
    top = draw_paragraph(
        pdf,
        "A buyer-facing overview of Jade Waves' core mineral range, grouped by application family and export use.",
        "Body",
        CONTENT_X,
        top,
        left_w,
    ) - 14
    top = draw_paragraph(
        pdf,
        "The range is built for ceramics, glass, foundry, drilling, coatings, construction, and processing buyers who need clear specifications, sample-first coordination, and export-ready dispatch from India.",
        "BodyMuted",
        CONTENT_X,
        top,
        left_w,
    ) - 16
    draw_pills(
        pdf,
        ["Silica", "Quartz", "Feldspar", "Bentonite", "Kaolin", "Talc", "Salt", "Fly Ash", "Copper Slag"],
        CONTENT_X,
        top,
        left_w,
    )

    draw_image_grid_2x2(
        pdf,
        [
            ROOT / "assets" / "quartz-sand-main-visual.webp",
            ROOT / "assets" / "feldspar-lumps-visual.webp",
            ROOT / "assets" / "bentonite-powder.png",
            ROOT / "assets" / "container-loading-wide.jpeg",
        ],
        CONTENT_X + left_w + 20,
        CONTENT_Y + 126,
        right_w,
        408,
    )

    draw_card(pdf, CONTENT_X, CONTENT_Y + 18, CONTENT_W, 86, fill_color=INK)
    note_top = CONTENT_Y + 86
    note_top = draw_paragraph(pdf, "How the portfolio is meant to be used", "WhiteTitle", CONTENT_X + 18, note_top, CONTENT_W - 36) - 8
    note_top = draw_paragraph(
        pdf,
        "Use this overview to identify the right family first. Detailed specs, sample handling, and shipment planning are aligned after the application, destination, and packing format are confirmed.",
        "WhiteBody",
        CONTENT_X + 18,
        note_top,
        CONTENT_W - 36,
    ) - 12
    draw_white_pills(pdf, ["Application first", "Sample-first support", "Export-ready dispatch"], CONTENT_X + 18, note_top, CONTENT_W - 36)

    draw_footer(pdf, 1)
    pdf.showPage()


def overview_page(pdf: canvas.Canvas) -> None:
    draw_page_bg(pdf)

    top = PAGE_HEIGHT - 86
    top = draw_paragraph(pdf, "PORTFOLIO VIEW", "Kicker", CONTENT_X, top, CONTENT_W) - 8
    top = draw_paragraph(pdf, "Range Built Around Industrial Demand", "SectionTitle", CONTENT_X, top, CONTENT_W) - 10
    top = draw_paragraph(
        pdf,
        "The product mix is organized the same way buyers usually think: by end use, process fit, and whether the material is going into glass, ceramics, drilling, construction, blasting, treatment systems, or general industrial demand.",
        "Body",
        CONTENT_X,
        top,
        CONTENT_W,
    ) - 18

    draw_image_row(
        pdf,
        [
            ROOT / "assets" / "container-loading-wide.jpeg",
            ROOT / "assets" / "jumbo-bags.jpeg",
            ROOT / "assets" / "bentonite-packing.png",
        ],
        CONTENT_X,
        CONTENT_Y + 430,
        CONTENT_W,
        108,
    )

    card_w = (CONTENT_W - 12) / 2
    card_h = 126
    family_positions = [
        (CONTENT_X, CONTENT_Y + 280),
        (CONTENT_X + card_w + 12, CONTENT_Y + 280),
        (CONTENT_X, CONTENT_Y + 138),
        (CONTENT_X + card_w + 12, CONTENT_Y + 138),
    ]
    for family, (x, y) in zip(PORTFOLIO_FAMILIES, family_positions):
        draw_family_card(pdf, family, x, y, card_w, card_h)

    draw_footer(pdf, 2)
    pdf.showPage()


def silica_family_page(pdf: canvas.Canvas) -> None:
    draw_page_bg(pdf)

    top = PAGE_HEIGHT - 86
    top = draw_paragraph(pdf, "FAMILY 01", "Kicker", CONTENT_X, top, CONTENT_W) - 8
    top = draw_paragraph(pdf, "Silica, Quartz & Feldspar", "SectionTitle", CONTENT_X, top, CONTENT_W) - 10
    top = draw_paragraph(
        pdf,
        "Purity-led minerals for glass, ceramics, filtration, engineered stone, and body-linked production where chemistry, mesh, whiteness, and packing format need to stay visible from the first sample onward.",
        "Body",
        CONTENT_X,
        top,
        CONTENT_W,
    ) - 18

    draw_image_row(
        pdf,
        [
            ROOT / "assets" / "silica-sand-visual.webp",
            ROOT / "assets" / "quartz-sand-main-visual.webp",
            ROOT / "assets" / "feldspar-bags-visual.webp",
        ],
        CONTENT_X,
        CONTENT_Y + 382,
        CONTENT_W,
        120,
    )

    card_w = (CONTENT_W - 12) / 2
    card_h = 154
    positions = [
        (CONTENT_X, CONTENT_Y + 212),
        (CONTENT_X + card_w + 12, CONTENT_Y + 212),
        (CONTENT_X, CONTENT_Y + 42),
        (CONTENT_X + card_w + 12, CONTENT_Y + 42),
    ]
    for product, (x, y) in zip(SILICA_FAMILY, positions):
        draw_product_card(pdf, product, x, y, card_w, card_h)

    draw_footer(pdf, 3)
    pdf.showPage()


def clays_family_page(pdf: canvas.Canvas) -> None:
    draw_page_bg(pdf)

    top = PAGE_HEIGHT - 86
    top = draw_paragraph(pdf, "FAMILY 02", "Kicker", CONTENT_X, top, CONTENT_W) - 8
    top = draw_paragraph(pdf, "Clays & Functional Fillers", "SectionTitle", CONTENT_X, top, CONTENT_W) - 10
    top = draw_paragraph(
        pdf,
        "This part of the range is used when the buyer is balancing performance, brightness, swelling behavior, absorption, or process smoothness rather than treating the mineral as a commodity input.",
        "Body",
        CONTENT_X,
        top,
        CONTENT_W,
    ) - 18

    draw_image_row(
        pdf,
        [
            ROOT / "assets" / "bentonite-powder.png",
            ROOT / "assets" / "china-clay-powder.png",
            ROOT / "assets" / "talc-powder.png",
        ],
        CONTENT_X,
        CONTENT_Y + 402,
        CONTENT_W,
        110,
    )

    strip_h = 108
    gap = 12
    y = CONTENT_Y + 270
    for product in CLAYS_FAMILY:
        draw_product_strip(pdf, product, CONTENT_X, y, CONTENT_W, strip_h)
        y -= strip_h + gap

    draw_footer(pdf, 4)
    pdf.showPage()


def industrial_media_page(pdf: canvas.Canvas) -> None:
    draw_page_bg(pdf)

    top = PAGE_HEIGHT - 86
    top = draw_paragraph(pdf, "FAMILY 03 / 04", "Kicker", CONTENT_X, top, CONTENT_W) - 8
    top = draw_paragraph(pdf, "Salt, Fly Ash & Copper Slag", "SectionTitle", CONTENT_X, top, CONTENT_W) - 10
    top = draw_paragraph(
        pdf,
        "These lines serve treatment systems, utilities, cement and concrete demand, blasting programs, and site-led industrial work where packing, dispatch rhythm, and use-case fit matter as much as the material itself.",
        "Body",
        CONTENT_X,
        top,
        CONTENT_W,
    ) - 18

    draw_image_row(
        pdf,
        [
            ROOT / "assets" / "salt-sample.png",
            ROOT / "assets" / "fly-ash-0.png",
            ROOT / "assets" / "copper-slag-closeup-in-hand.png",
        ],
        CONTENT_X,
        CONTENT_Y + 410,
        CONTENT_W,
        112,
    )

    strip_h = 82
    gap = 10
    y = CONTENT_Y + 322
    for product in INDUSTRIAL_MEDIA:
        draw_product_strip(pdf, product, CONTENT_X, y, CONTENT_W, strip_h)
        y -= strip_h + gap

    left_w = 246
    right_w = CONTENT_W - left_w - 12
    draw_card(pdf, CONTENT_X, CONTENT_Y + 18, left_w, 112, fill_color=INK)
    contact_top = CONTENT_Y + 112
    contact_top = draw_paragraph(pdf, "Request a product match", "WhiteTitle", CONTENT_X + 16, contact_top, left_w - 32) - 8
    contact_top = draw_paragraph(
        pdf,
        "Share the product, use case, destination, packing format, and target volume. Jade Waves can then align the right product sheet, sample, and dispatch conversation.",
        "WhiteBody",
        CONTENT_X + 16,
        contact_top,
        left_w - 32,
    )

    draw_card(pdf, CONTENT_X + left_w + 12, CONTENT_Y + 18, right_w, 112, fill_color=PANEL_WARM)
    info_top = CONTENT_Y + 112
    info_top = draw_paragraph(pdf, "Contact", "SubTitle", CONTENT_X + left_w + 28, info_top, right_w - 32) - 8
    for line in [
        "deep@jadewavesenterprise.com",
        "+91-999-883-5503",
        "www.jadewavesenterprise.com",
        "Ahmedabad, Gujarat, India",
    ]:
        info_top = draw_paragraph(pdf, line, "BodyTiny", CONTENT_X + left_w + 28, info_top, right_w - 32) - 4

    draw_footer(pdf, 5)
    pdf.showPage()


def build_pdf() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUTPUT), pagesize=A4)
    pdf.setTitle("Core Minerals Overview | Jade Waves Enterprise")
    pdf.setAuthor("Jade Waves Enterprise")
    pdf.setSubject("Buyer-facing overview of Jade Waves' core mineral portfolio")

    cover_page(pdf)
    overview_page(pdf)
    silica_family_page(pdf)
    clays_family_page(pdf)
    industrial_media_page(pdf)

    pdf.save()


if __name__ == "__main__":
    build_pdf()
