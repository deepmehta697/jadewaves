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
OUTPUT = ROOT / "output" / "pdf" / "jade-waves-specs-samples-shipment-flow.pdf"

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 42
CONTENT_X = MARGIN + 20
CONTENT_Y = MARGIN + 24
CONTENT_W = PAGE_WIDTH - 2 * CONTENT_X
CONTENT_H = PAGE_HEIGHT - CONTENT_Y - 56

INK = colors.HexColor("#13243C")
INK_SOFT = colors.HexColor("#46566B")
SAND = colors.HexColor("#F4EFE8")
STONE = colors.HexColor("#E4DDD2")
PANEL = colors.HexColor("#F8F4EE")
GOLD = colors.HexColor("#B58C45")
WHITE = colors.white

IMAGE_CACHE: dict[tuple[str, int], ImageReader] = {}

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="BodySmall",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.2,
        leading=14.2,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyMuted",
        parent=styles["BodySmall"],
        textColor=INK_SOFT,
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
        name="StepBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.2,
        leading=11.6,
        textColor=INK_SOFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="StepBodyTight",
        parent=styles["StepBody"],
        fontSize=8.5,
        leading=10.5,
    )
)
styles.add(
    ParagraphStyle(
        name="StepBodyUltra",
        parent=styles["StepBody"],
        fontSize=7.8,
        leading=9.4,
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
        name="GoldNote",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=8.8,
        leading=11,
        textColor=GOLD,
        spaceAfter=0,
    )
)


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
        h = paragraph_height(text, style_name, width)
        chosen = style_name
        chosen_height = h
        if h <= max_height:
            break
    fitted_text = text
    if chosen_height > max_height:
        words = text.split()
        truncated = fitted_text
        while words:
            truncated = " ".join(words).rstrip(" .,;:") + "..."
            h = paragraph_height(truncated, chosen, width)
            if h <= max_height:
                fitted_text = truncated
                chosen_height = h
                break
            words.pop()
        else:
            fitted_text = text
            chosen_height = max_height
    paragraph = Paragraph(fitted_text, styles[chosen])
    _, chosen_height = paragraph.wrap(width, max_height)
    paragraph.drawOn(pdf, x, y_top - chosen_height)
    return y_top - chosen_height


def draw_card(pdf: canvas.Canvas, x: float, y: float, width: float, height: float, fill_color=PANEL) -> None:
    pdf.setFillColor(fill_color)
    pdf.roundRect(x, y, width, height, 16, fill=1, stroke=0)


def draw_number_badge(pdf: canvas.Canvas, number: str, x: float, y_top: float) -> None:
    pdf.setFillColor(GOLD)
    pdf.circle(x, y_top, 10, fill=1, stroke=0)
    pdf.setFillColor(WHITE)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawCentredString(x, y_top - 3.6, number)


def draw_bullets(pdf: canvas.Canvas, items: list[str], x: float, y_top: float, width: float, bullet_color=GOLD) -> float:
    cursor = y_top
    for item in items:
        pdf.setFillColor(bullet_color)
        pdf.circle(x + 4, cursor - 6, 2.1, fill=1, stroke=0)
        cursor = draw_paragraph(pdf, item, "BodySmall", x + 12, cursor, width - 12) - 8
    return cursor


def draw_pills(pdf: canvas.Canvas, labels: list[str], x: float, y_top: float, max_width: float) -> float:
    cursor_x = x
    cursor_y = y_top
    row_height = 22
    for label in labels:
        pill_w = stringWidth(label, "Helvetica-Bold", 8.5) + 18
        if cursor_x + pill_w > x + max_width:
            cursor_x = x
            cursor_y -= row_height
        pdf.setFillColor(colors.HexColor("#F6F1E9"))
        pdf.roundRect(cursor_x, cursor_y - 18, pill_w, 18, 9, fill=1, stroke=0)
        pdf.setFillColor(INK)
        pdf.setFont("Helvetica-Bold", 8.5)
        pdf.drawString(cursor_x + 9, cursor_y - 12.5, label)
        cursor_x += pill_w + 8
    return cursor_y - row_height + 6


def get_pdf_image(image_path: Path, max_px: int = 1800) -> ImageReader:
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
            image.save(buffer, format="JPEG", quality=82, optimize=True)
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


def draw_image_contain(pdf: canvas.Canvas, image_path: Path, x: float, y: float, width: float, height: float, radius: float = 16) -> None:
    draw_card(pdf, x, y, width, height, fill_color=colors.HexColor("#FBF8F3"))
    image = get_pdf_image(image_path)
    image_w, image_h = image.getSize()
    scale = min((width - 20) / image_w, (height - 20) / image_h)
    draw_w = image_w * scale
    draw_h = image_h * scale
    draw_x = x + (width - draw_w) / 2
    draw_y = y + (height - draw_h) / 2
    pdf.saveState()
    path = pdf.beginPath()
    path.roundRect(x, y, width, height, radius)
    pdf.clipPath(path, stroke=0, fill=0)
    pdf.drawImage(image, draw_x, draw_y, draw_w, draw_h, preserveAspectRatio=True, mask="auto")
    pdf.restoreState()


def draw_step_card(pdf: canvas.Canvas, number: str, title: str, body: str, x: float, y: float, width: float, height: float) -> None:
    draw_card(pdf, x, y, width, height)
    draw_number_badge(pdf, number, x + 22, y + height - 22)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x + 40, y + height - 26, title)
    draw_paragraph_fit(pdf, body, ["StepBody", "StepBodyTight", "StepBodyUltra"], x + 16, y + height - 44, width - 32, height - 58)


def cover_page(pdf: canvas.Canvas) -> None:
    draw_page_bg(pdf)

    logo = ROOT / "assets" / "jade-waves-logo-transparent.png"
    hero = ROOT / "assets" / "container-loading-wide.jpeg"

    pdf.drawImage(str(logo), CONTENT_X, PAGE_HEIGHT - 96, width=104, height=68, mask="auto", preserveAspectRatio=True)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(CONTENT_X + 110, PAGE_HEIGHT - 58, "Jade Waves Enterprise")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(CONTENT_X + 110, PAGE_HEIGHT - 74, "Industrial mineral exports from India")

    cursor = PAGE_HEIGHT - 130
    cursor = draw_paragraph(pdf, "EXPORT FLOW", "Kicker", CONTENT_X, cursor, CONTENT_W) - 8
    cursor = draw_paragraph(pdf, "How We Handle Specs, Samples and Shipment Flow", "SectionTitle", CONTENT_X, cursor, CONTENT_W) - 12
    cursor = draw_paragraph(
        pdf,
        "A short buyer-facing overview of how Jade Waves aligns technical requirements early, manages sample-first coordination, and keeps shipment movement visible from inquiry to dispatch.",
        "BodySmall",
        CONTENT_X,
        cursor,
        CONTENT_W,
    ) - 14

    cursor = draw_pills(
        pdf,
        ["Near Mundra Port", "FOB / CIF / CNF", "Sample-first support", "Export-ready dispatch"],
        CONTENT_X,
        cursor,
        CONTENT_W,
    ) - 8

    hero_y = CONTENT_Y + 26
    hero_h = 280
    draw_image_cover(pdf, hero, CONTENT_X, hero_y, CONTENT_W, hero_h, radius=18)

    pdf.setFillColor(colors.Color(0.07, 0.14, 0.24, alpha=0.9))
    pdf.roundRect(CONTENT_X + 18, hero_y + 18, 270, 70, 14, fill=1, stroke=0)
    pdf.setFillColor(WHITE)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(CONTENT_X + 34, hero_y + 61, "Clear details before cargo moves")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(CONTENT_X + 34, hero_y + 41, "Grade, packing, documents, and shipment terms are")
    pdf.drawString(CONTENT_X + 34, hero_y + 27, "clarified early so the first order feels settled.")

    draw_footer(pdf, 1)
    pdf.showPage()


def spec_page(pdf: canvas.Canvas) -> None:
    draw_page_bg(pdf)

    left_w = 250
    right_w = CONTENT_W - left_w - 18
    left_x = CONTENT_X
    right_x = left_x + left_w + 18
    top = PAGE_HEIGHT - 86

    top = draw_paragraph(pdf, "STEP 1", "Kicker", left_x, top, CONTENT_W) - 8
    top = draw_paragraph(pdf, "Start With the Spec", "SectionTitle", left_x, top, CONTENT_W) - 10
    top = draw_paragraph(
        pdf,
        "The work starts by aligning the material to the use case before pricing, sampling, or cargo planning begins.",
        "BodySmall",
        left_x,
        top,
        CONTENT_W,
    ) - 18

    left_card_y = CONTENT_Y + 128
    left_card_h = 388
    draw_card(pdf, left_x, left_card_y, left_w, left_card_h)
    inner_top = left_card_y + left_card_h - 20
    inner_top = draw_paragraph(pdf, "What gets aligned first", "SubTitle", left_x + 16, inner_top, left_w - 32) - 10
    draw_bullets(
        pdf,
        [
            "Application and end use: glass, ceramics, foundry, filtration, construction, drilling, or process use.",
            "Chemistry targets: SiO2, K2O, Na2O, Fe2O3, moisture, or any other application-led limits.",
            "Sizing requirements: grain size, mesh, micron range, and packing format.",
            "Commercial context: target volume, destination, and preferred Incoterm.",
            "Documentation needs before pricing or cargo planning starts.",
        ],
        left_x + 12,
        inner_top,
        left_w - 24,
    )

    draw_image_contain(pdf, ROOT / "assets" / "jumbo-bags.jpeg", right_x, CONTENT_Y + 286, right_w, 230, radius=18)

    callout_y = CONTENT_Y + 128
    callout_h = 138
    draw_card(pdf, right_x, callout_y, right_w, callout_h)
    callout_top = callout_y + callout_h - 18
    callout_top = draw_paragraph(pdf, "Why this matters", "SubTitle", right_x + 16, callout_top, right_w - 32) - 8
    draw_bullets(
        pdf,
        [
            "Reduces mismatch between the inquiry, quote, sample, and final cargo.",
            "Keeps shipment planning tied to the same technical context the buyer approved.",
            "Makes the first order easier to approve and the next order easier to repeat.",
        ],
        right_x + 12,
        callout_top,
        right_w - 24,
        bullet_color=INK,
    )

    draw_footer(pdf, 2)
    pdf.showPage()


def samples_page(pdf: canvas.Canvas) -> None:
    draw_page_bg(pdf)

    top = PAGE_HEIGHT - 86
    top = draw_paragraph(pdf, "STEP 2", "Kicker", CONTENT_X, top, CONTENT_W) - 8
    top = draw_paragraph(pdf, "Handle Samples Without Losing the Thread", "SectionTitle", CONTENT_X, top, CONTENT_W) - 10
    top = draw_paragraph(
        pdf,
        "Jade Waves uses a sample-first flow so grade fit, chemistry expectations, and packing context are settled before the order moves into full dispatch planning.",
        "BodySmall",
        CONTENT_X,
        top,
        CONTENT_W,
    ) - 18

    image_w = 206
    image_h = 208
    draw_image_contain(pdf, ROOT / "assets" / "bentonite-packing.png", CONTENT_X + CONTENT_W - image_w, CONTENT_Y + 328, image_w, image_h, radius=18)

    left_w = CONTENT_W - image_w - 18
    intro_h = 96
    draw_card(pdf, CONTENT_X, CONTENT_Y + 440 - intro_h, left_w, intro_h)
    intro_top = CONTENT_Y + 440 - 16
    intro_top = draw_paragraph(pdf, "Sample-first coordination", "SubTitle", CONTENT_X + 16, intro_top, left_w - 32) - 8
    draw_bullets(
        pdf,
        [
            "Sample is aligned to the agreed grade, sizing, and end use.",
            "Quote and shipment planning stay connected to the approved sample context.",
            "The goal is simple: make the first order feel more certain before loading starts.",
        ],
        CONTENT_X + 12,
        intro_top,
        left_w - 24,
        bullet_color=INK,
    )

    card_w = (CONTENT_W - 12) / 2
    card_h = 108
    row_one_y = CONTENT_Y + 202
    row_two_y = CONTENT_Y + 82
    step_cards = [
        ("1", "Request", "Buyer shares the application, target spec, and destination context.", CONTENT_X, row_one_y),
        ("2", "Align", "Sample is matched to the right grade, packing style, and intended use.", CONTENT_X + card_w + 12, row_one_y),
        ("3", "Review", "Buyer checks material fit before cargo planning or commercial locking advances.", CONTENT_X, row_two_y),
        ("4", "Carry Forward", "The same approved context carries into pricing, documents, and shipment flow.", CONTENT_X + card_w + 12, row_two_y),
    ]
    for number, title, body, x, y in step_cards:
        draw_step_card(pdf, number, title, body, x, y, card_w, card_h)

    draw_footer(pdf, 3)
    pdf.showPage()


def shipment_page(pdf: canvas.Canvas) -> None:
    draw_page_bg(pdf)

    top = PAGE_HEIGHT - 86
    top = draw_paragraph(pdf, "STEP 3", "Kicker", CONTENT_X, top, CONTENT_W) - 8
    top = draw_paragraph(pdf, "Keep Shipment Flow Visible", "SectionTitle", CONTENT_X, top, CONTENT_W) - 10
    top = draw_paragraph(
        pdf,
        "Once the grade, sample, and commercials are aligned, the work shifts into a short, visible export sequence: documents locked early, loading updates kept in view, and dispatch tracked through cargo movement.",
        "BodySmall",
        CONTENT_X,
        top,
        CONTENT_W,
    ) - 18

    card_w = (CONTENT_W - 12) / 2
    card_h = 110
    first_row_y = CONTENT_Y + 286
    second_row_y = CONTENT_Y + 170
    step_cards = [
        ("01", "Inquiry", "Product, application, destination, and target volume are shared.", CONTENT_X, first_row_y),
        ("02", "Quote or sample", "Pricing or sampling stays tied to the right grade and packing.", CONTENT_X + card_w + 12, first_row_y),
        ("03", "Documentation", "Commercial terms and export documents are locked before loading.", CONTENT_X, second_row_y),
        ("04", "Dispatch", "Updates continue through loading, vessel planning, and cargo movement.", CONTENT_X + card_w + 12, second_row_y),
    ]
    for number, title, body, x, y in step_cards:
        draw_step_card(pdf, number, title, body, x, y, card_w, card_h)

    visual_y = CONTENT_Y + 18
    visual_h = 146
    visual_w = (CONTENT_W - 12) / 2
    draw_image_cover(pdf, ROOT / "assets" / "container-loading-wide.jpeg", CONTENT_X, visual_y, visual_w, visual_h, radius=18)
    draw_image_cover(pdf, ROOT / "assets" / "bentonite-packing.png", CONTENT_X + visual_w + 12, visual_y, visual_w, visual_h, radius=18)

    draw_footer(pdf, 4)
    pdf.showPage()


def commercial_page(pdf: canvas.Canvas) -> None:
    draw_page_bg(pdf)

    left_w = 268
    right_w = CONTENT_W - left_w - 18
    left_x = CONTENT_X
    right_x = left_x + left_w + 18
    top = PAGE_HEIGHT - 86

    top = draw_paragraph(pdf, "COMMERCIAL VIEW", "Kicker", left_x, top, CONTENT_W) - 8
    top = draw_paragraph(pdf, "Commercial Clarity Before Loading", "SectionTitle", left_x, top, CONTENT_W) - 10
    top = draw_paragraph(
        pdf,
        "The process stays short on purpose: lock the material context, make the sample count, settle documents early, and keep cargo movement visible.",
        "BodySmall",
        left_x,
        top,
        CONTENT_W,
    ) - 18

    left_card_y = CONTENT_Y + 216
    left_card_h = 266
    draw_card(pdf, left_x, left_card_y, left_w, left_card_h)
    left_top = left_card_y + left_card_h - 18
    left_top = draw_paragraph(pdf, "Commercial clarity", "SubTitle", left_x + 16, left_top, left_w - 32) - 10
    draw_bullets(
        pdf,
        [
            "Incoterms: FOB / CIF / CNF",
            "Lead time: 7 to 10 days",
            "Loading context: near Mundra Port",
            "Orders: LCL / FCL accepted",
            "Flow: sample-first, document-led, dispatch visible",
            "Goal: make the first order clear and the next one easier",
        ],
        left_x + 12,
        left_top,
        left_w - 24,
        bullet_color=INK,
    )

    bottom_card_y = CONTENT_Y + 18
    bottom_card_h = 178
    draw_card(pdf, left_x, bottom_card_y, left_w, bottom_card_h)
    bottom_top = bottom_card_y + bottom_card_h - 18
    bottom_top = draw_paragraph(pdf, "What the buyer sends", "SubTitle", left_x + 16, bottom_top, left_w - 32) - 10
    draw_bullets(
        pdf,
        [
            "Product, grade, or closest requirement",
            "Destination country or port",
            "Expected volume and packing format",
            "Sizing, chemistry, and any critical document points",
        ],
        left_x + 12,
        bottom_top,
        left_w - 24,
        bullet_color=INK,
    )

    draw_image_cover(pdf, ROOT / "assets" / "container-1604.jpeg", right_x, CONTENT_Y + 252, right_w, 230, radius=18)

    draw_card(pdf, right_x, CONTENT_Y + 18, right_w, 214, fill_color=INK)
    contact_top = CONTENT_Y + 214
    pdf.setFillColor(WHITE)
    contact_top = draw_paragraph(pdf, "Request a quote or sample", "SubTitle", right_x + 16, contact_top, right_w - 32) - 12
    for line in [
        "deep@jadewavesenterprise.com",
        "+91-999-883-5503",
        "www.jadewavesenterprise.com",
        "Jade Waves Enterprise, Ahmedabad, Gujarat, India",
    ]:
        contact_top = draw_paragraph(pdf, line, "BodySmall", right_x + 16, contact_top, right_w - 32) - 7

    draw_paragraph(
        pdf,
        "Clear specs. Cleaner communication. Visible dispatch.",
        "GoldNote",
        right_x + 16,
        CONTENT_Y + 74,
        right_w - 32,
    )

    draw_footer(pdf, 5)
    pdf.showPage()


def build_pdf() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUTPUT), pagesize=A4)
    pdf.setTitle("How Jade Waves Handles Specs, Samples and Shipment Flow")
    pdf.setAuthor("Jade Waves Enterprise")
    pdf.setSubject("Industrial mineral export process overview")

    cover_page(pdf)
    spec_page(pdf)
    samples_page(pdf)
    shipment_page(pdf)
    commercial_page(pdf)

    pdf.save()


if __name__ == "__main__":
    build_pdf()
