from io import BytesIO
from pathlib import Path
from typing import Optional

import fitz
from PIL import Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output" / "pdf" / "coa-quartz-grits-q2-premium.pdf"
VECTOR_OUTPUT = ROOT / "tmp" / "pdfs" / "coa-quartz-grits-q2-vector.pdf"
FLATTENED_IMAGE = ROOT / "tmp" / "pdfs" / "coa-quartz-grits-q2-flattened.png"
DELIVERY_OUTPUT = Path("/Users/deepmehta/Documents/Jade Waves Enterprise/Products/Quartz/COA Quartz Grits Q2 - Premium Final.pdf")
ASSET_OUTPUT: Optional[Path] = None
LOGO = ROOT / "assets" / "jade-waves-logo-transparent.png"

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_X = 36
MARGIN_Y = 28
CONTENT_W = PAGE_WIDTH - (MARGIN_X * 2)

INK = colors.HexColor("#13243C")
INK_SOFT = colors.HexColor("#5A6A7F")
ACCENT = colors.HexColor("#2F6F67")
ACCENT_SOFT = colors.HexColor("#E9F3F1")
BLUE = colors.HexColor("#0B69C7")
BLUE_SOFT = colors.HexColor("#EDF4FC")
BORDER = colors.HexColor("#D8D6D0")
PANEL = colors.HexColor("#FCFBF8")
PANEL_ALT = colors.HexColor("#F7F4EE")
WHITE = colors.white
ROW_BG = colors.HexColor("#FFFFFF")
ROW_BG_ALT = colors.HexColor("#F7F5F0")
PAGE_BG = colors.HexColor("#F3F0EA")
HEADER_DARK = colors.HexColor("#10263A")
GOLD = colors.HexColor("#C7A35B")
GOLD_SOFT = colors.HexColor("#F5E8C8")

IMAGE_CACHE: dict[tuple[str, int, int], ImageReader] = {}

COMPANY_NAME = "Jade Waves Enterprise"
ADDRESS_LINES = [
    "A-11 Florence, Science City Road,",
    "Ahmedabad-380060 Gujarat, India",
]
CONTACT_LINE = "+91-999-883-5503  |  info@jadewavesenterprise.com"
WEB_LINE = "www.jadewavesenterprise.com"
PRODUCT_NAME = "Quartz Grits - Q2"
HEADER_SUBTITLE = "Premium COA for Quartz Grits - Q2"
DOCUMENT_TITLE = "Jade Waves Enterprise - Premium COA - Quartz Grits Q2"
DOCUMENT_SUBJECT = "Certificate of Analysis for Quartz Grits - Q2"
SUMMARY_DETAIL = "Representative sample analysis from supplied spec image"
PRIMARY_METRIC_LABEL = "Silica (SiO2)"
PRIMARY_METRIC_VALUE = ">99.0%"
SECONDARY_METRIC_LABEL = "Color L"
SECONDARY_METRIC_VALUE = "90 min"
TERTIARY_METRIC_LABEL = "Humidity"
TERTIARY_METRIC_VALUE = "Max 0.3%"
BUYER_REFERENCE = [
    (
        "Application",
        "Ceramics, glass manufacturing, engineered stone, and building materials",
    ),
    ("Forms", "Quartz grits in graded size fractions"),
    ("Typical grade range", "Q2 grits, >99.0% SiO2, L 90 min, moisture max 0.3%"),
    ("Packing options", "Jumbo bags"),
    ("HSN code", "25061020"),
    ("Inquiry contact", "deep@jadewavesenterprise.com | +91-999-883-5503"),
]

RESULT_ROWS = [
    ("1", "Chemical analysis", "SiO2", "> 99.0%"),
    ("2", "Chemical analysis", "Na2O", "0.05% max"),
    ("3", "Chemical analysis", "CaO", "0.03% max"),
    ("4", "Chemical analysis", "K2O", "0.05% max"),
    ("5", "Chemical analysis", "Fe2O3", "0.06% max"),
    ("6", "Chemical analysis", "K2O", "0.02% max"),
    ("7", "Chemical analysis", "TiO2", "0.04% max"),
    ("8", "Chemical analysis", "Al2O3", "0.1% max"),
    ("9", "Chemical analysis", "L.O.I.", "0.1 max"),
    ("10", "Color", "L", "90 min"),
    ("11", "Color", "a", "2.0 max"),
    ("12", "Color", "b", "3.5 max"),
    ("13", "Particle size distribution", "Grading performance", "Size in range > 90%; upper size < 5%; lower size < 5%"),
    ("14", "Impurity/100 gram", "Black Particle", "15"),
    ("15", "Impurity/100 gram", "Other colors particle", "15"),
    ("16", "Humidity", "Moisture", "Max 0.3%"),
    ("17", "Readily available sizes", "Standard fractions", "0.1-0.4 mm | 0.3-0.7 mm | 0.6-1.2 mm"),
    ("18", "Readily available sizes", "Extended fractions", "1.2-2.5 mm | 2.5-4.0 mm | 0.063-0.212 mm"),
]


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="TopRight",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.9,
        leading=10.0,
        alignment=TA_RIGHT,
        textColor=INK_SOFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.2,
        leading=13,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Muted",
        parent=styles["Body"],
        fontSize=8.5,
        leading=11.6,
        textColor=INK_SOFT,
    )
)
styles.add(
    ParagraphStyle(
        name="TableCell",
        parent=styles["Body"],
        fontSize=7.05,
        leading=7.8,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="InfoLabel",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=6.6,
        leading=7.4,
        textColor=ACCENT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="InfoValue",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=6.8,
        leading=7.6,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="InfoValueTight",
        parent=styles["InfoValue"],
        fontSize=6.1,
        leading=6.9,
    )
)
styles.add(
    ParagraphStyle(
        name="SummaryValue",
        parent=styles["BodyText"],
        fontName="Times-Bold",
        fontSize=14.2,
        leading=15.0,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="SummaryDetail",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.3,
        leading=8.0,
        textColor=INK_SOFT,
        )
)


def draw_paragraph(pdf: canvas.Canvas, text: str, style_name: str, x: float, y_top: float, width: float) -> float:
    paragraph = Paragraph(text, styles[style_name])
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    paragraph.drawOn(pdf, x, y_top - height)
    return y_top - height


def paragraph_height(text: str, style_name: str, width: float) -> float:
    paragraph = Paragraph(text, styles[style_name])
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    return height


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
    paragraph = Paragraph(text, styles[chosen])
    _, chosen_height = paragraph.wrap(width, max_height)
    paragraph.drawOn(pdf, x, y_top - chosen_height)
    return y_top - chosen_height


def get_faded_logo_reader(image_path: Path, alpha_percent: int = 11, max_width_px: int = 960) -> ImageReader:
    cache_key = (str(image_path), alpha_percent, max_width_px)
    cached = IMAGE_CACHE.get(cache_key)
    if cached is not None:
        return cached

    with Image.open(image_path).convert("RGBA") as image:
        if image.width > max_width_px:
            scale = max_width_px / image.width
            image = image.resize((int(image.width * scale), int(image.height * scale)), Image.LANCZOS)

        # Flatten the watermark to RGB so the exported PDF stays compatible with viewers
        # that struggle with live transparency / soft-mask combinations.
        white_bg = Image.new("RGBA", image.size, (255, 255, 255, 255))
        faded_logo = Image.new("RGBA", image.size, (255, 255, 255, 0))
        pixels = []
        for r, g, b, a in image.getdata():
            effective_alpha = int(a * alpha_percent / 100)
            pixels.append((r, g, b, effective_alpha))
        faded_logo.putdata(pixels)
        flattened = Image.alpha_composite(white_bg, faded_logo).convert("RGB")

        buffer = BytesIO()
        flattened.save(buffer, format="PNG", optimize=True)
        buffer.seek(0)
        reader = ImageReader(buffer)
        IMAGE_CACHE[cache_key] = reader
        return reader


def draw_card(
    pdf: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    fill_color=WHITE,
    stroke_color=BORDER,
    radius: float = 16,
    line_width: float = 1,
) -> None:
    pdf.setFillColor(fill_color)
    pdf.setStrokeColor(stroke_color)
    pdf.setLineWidth(line_width)
    pdf.roundRect(x, y, width, height, radius, fill=1, stroke=1)


def draw_summary_card(pdf: canvas.Canvas, x: float, y: float, width: float, height: float, label: str, value: str, detail: str = "") -> None:
    draw_card(pdf, x, y, width, height, fill_color=WHITE, stroke_color=BORDER, radius=14)
    pdf.setFillColor(GOLD)
    pdf.roundRect(x + 14, y + height - 10, 54, 2.4, 1.2, fill=1, stroke=0)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 8.8)
    pdf.drawString(x + 16, y + height - 17, label.upper())
    draw_paragraph_fit(pdf, value, ["SummaryValue"], x + 16, y + height - 28, width - 32, 18)
    if detail:
        draw_paragraph_fit(pdf, detail, ["SummaryDetail"], x + 16, y + 15, width - 32, 10)


def draw_metric_card(
    pdf: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    label: str,
    value: str,
    fill_color,
    label_color,
    value_color,
    stroke_color,
) -> None:
    draw_card(pdf, x, y, width, height, fill_color=fill_color, stroke_color=stroke_color, radius=14)
    pdf.setFillColor(GOLD)
    pdf.roundRect(x + 12, y + height - 10, 34, 2, 1, fill=1, stroke=0)
    pdf.setFillColor(label_color)
    pdf.setFont("Helvetica-Bold", 7.8)
    pdf.drawString(x + 14, y + height - 20, label.upper())
    pdf.setFillColor(value_color)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(x + 14, y + 15, value)


def build_results_table() -> Table:
    header = ["Sr No.", "Section", "Parameter", "Specification"]
    rows = [header]
    for row in RESULT_ROWS:
        rows.append(
            [
                Paragraph(row[0], styles["TableCell"]),
                Paragraph(row[1], styles["TableCell"]),
                Paragraph(row[2], styles["TableCell"]),
                Paragraph(row[3], styles["TableCell"]),
            ]
        )

    table = Table(rows, colWidths=[30, 104, 116, 245], repeatRows=1)
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), HEADER_DARK),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 7.6),
            ("LEADING", (0, 0), (-1, 0), 8.6),
            ("ALIGN", (0, 0), (0, -1), "CENTER"),
            ("ALIGN", (2, 0), (2, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 2.1),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.1),
            ("LEFTPADDING", (0, 0), (-1, -1), 4.6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4.6),
            ("GRID", (0, 0), (-1, -1), 0.45, BORDER),
            ("LINEBELOW", (0, 0), (-1, 0), 1.0, GOLD),
        ]
    )

    for row_index in range(1, len(rows)):
        style.add("BACKGROUND", (0, row_index), (-1, row_index), ROW_BG if row_index % 2 else ROW_BG_ALT)

    table.setStyle(style)
    return table


def draw_analysis_watermark(pdf: canvas.Canvas, x: float, y: float, width: float, height: float) -> None:
    if not LOGO.exists():
        return

    image = get_faded_logo_reader(LOGO)
    image_w, image_h = image.getSize()
    scale = min((width * 0.8) / image_w, (height * 0.68) / image_h)
    draw_w = image_w * scale
    draw_h = image_h * scale
    draw_x = x + (width - draw_w) / 2
    draw_y = y + (height - draw_h) / 2 - 6
    pdf.drawImage(image, draw_x, draw_y, draw_w, draw_h, mask="auto", preserveAspectRatio=True)


def draw_info_item(pdf: canvas.Canvas, x: float, y: float, width: float, height: float, label: str, value: str) -> None:
    draw_card(pdf, x, y, width, height, fill_color=WHITE, stroke_color=BORDER, radius=10, line_width=0.8)
    pdf.setFillColor(GOLD)
    pdf.roundRect(x + 10, y + height - 9, 28, 1.8, 0.8, fill=1, stroke=0)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 6.6)
    pdf.drawString(x + 10, y + height - 10, label.upper())
    draw_paragraph_fit(pdf, value, ["InfoValue", "InfoValueTight"], x + 10, y + height - 14, width - 20, height - 16)


def draw_header(pdf: canvas.Canvas) -> None:
    pdf.setFillColor(PAGE_BG)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    draw_card(
        pdf,
        MARGIN_X - 6,
        MARGIN_Y - 8,
        PAGE_WIDTH - (MARGIN_X * 2) + 20,
        PAGE_HEIGHT - (MARGIN_Y * 2) + 8,
        fill_color=colors.HexColor("#E6E0D6"),
        stroke_color=colors.HexColor("#E6E0D6"),
        radius=22,
        line_width=0,
    )
    draw_card(
        pdf,
        MARGIN_X - 10,
        MARGIN_Y - 4,
        PAGE_WIDTH - (MARGIN_X * 2) + 20,
        PAGE_HEIGHT - (MARGIN_Y * 2) + 8,
        fill_color=WHITE,
        stroke_color=BORDER,
        radius=20,
    )

    draw_card(
        pdf,
        MARGIN_X - 10,
        PAGE_HEIGHT - 166,
        PAGE_WIDTH - (MARGIN_X * 2) + 20,
        126,
        fill_color=HEADER_DARK,
        stroke_color=HEADER_DARK,
        radius=20,
        line_width=0,
    )

    pdf.setFillColor(GOLD)
    pdf.roundRect(MARGIN_X, PAGE_HEIGHT - 64, 110, 2.5, 1.2, fill=1, stroke=0)
    pdf.setFillColor(GOLD)
    pdf.setFont("Helvetica-Bold", 8.2)
    pdf.drawString(MARGIN_X, PAGE_HEIGHT - 78, "EXPORT QUALITY CERTIFICATE")

    pdf.setFillColor(WHITE)
    pdf.setFont("Times-Bold", 27)
    pdf.drawString(MARGIN_X, PAGE_HEIGHT - 104, "Certificate of Analysis")

    pdf.setFillColor(colors.HexColor("#D7E0EA"))
    pdf.setFont("Helvetica", 11.0)
    pdf.drawString(MARGIN_X, PAGE_HEIGHT - 123, HEADER_SUBTITLE)

    brand_w = 126
    brand_h = 92
    brand_x = PAGE_WIDTH - MARGIN_X - brand_w
    brand_y = PAGE_HEIGHT - 150
    draw_card(pdf, brand_x, brand_y, brand_w, brand_h, fill_color=colors.HexColor("#FBFAF7"), stroke_color=colors.HexColor("#2B3D50"), radius=16, line_width=1)
    pdf.drawImage(str(LOGO), brand_x + 28, brand_y + 36, width=68, height=40, mask="auto", preserveAspectRatio=True)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 8.5)
    pdf.drawCentredString(brand_x + (brand_w / 2), brand_y + 28, COMPANY_NAME)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica", 7.7)
    pdf.drawCentredString(brand_x + (brand_w / 2), brand_y + 17, "Ahmedabad, Gujarat, India")


def build_vector_pdf(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pdf = canvas.Canvas(str(output_path), pagesize=A4)
    pdf.setTitle(DOCUMENT_TITLE)
    pdf.setAuthor(COMPANY_NAME)
    pdf.setSubject(DOCUMENT_SUBJECT)

    draw_header(pdf)

    summary_y = 614
    summary_h = 62
    gap = 14
    card_w = (CONTENT_W - gap) / 2
    draw_summary_card(
        pdf,
        MARGIN_X,
        summary_y,
        card_w,
        summary_h,
        "Product",
        PRODUCT_NAME,
        SUMMARY_DETAIL,
    )
    draw_summary_card(
        pdf,
        MARGIN_X + card_w + gap,
        summary_y,
        card_w,
        summary_h,
        "Authorized By",
        "Deep Mehta",
        "Managing Partner",
    )

    metric_y = 544
    metric_h = 52
    metric_gap = 12
    metric_w = (CONTENT_W - (metric_gap * 2)) / 3
    draw_metric_card(pdf, MARGIN_X, metric_y, metric_w, metric_h, PRIMARY_METRIC_LABEL, PRIMARY_METRIC_VALUE, INK, WHITE, WHITE, INK)
    draw_metric_card(
        pdf,
        MARGIN_X + metric_w + metric_gap,
        metric_y,
        metric_w,
        metric_h,
        SECONDARY_METRIC_LABEL,
        SECONDARY_METRIC_VALUE,
        BLUE_SOFT,
        BLUE,
        INK,
        BORDER,
    )
    draw_metric_card(
        pdf,
        MARGIN_X + ((metric_w + metric_gap) * 2),
        metric_y,
        metric_w,
        metric_h,
        TERTIARY_METRIC_LABEL,
        TERTIARY_METRIC_VALUE,
        ACCENT_SOFT,
        ACCENT,
        INK,
        BORDER,
    )

    table_card_x = MARGIN_X
    table_card_y = 182
    table_card_h = 336
    draw_card(pdf, table_card_x, table_card_y, CONTENT_W, table_card_h, fill_color=PANEL, stroke_color=BORDER, radius=18)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 7.8)
    pdf.drawString(table_card_x + 18, table_card_y + table_card_h - 20, "TECHNICAL ANALYSIS")
    pdf.setFillColor(INK)
    pdf.setFont("Times-Bold", 13.5)
    pdf.drawString(table_card_x + 18, table_card_y + table_card_h - 38, "Representative material specification")
    pdf.setStrokeColor(GOLD)
    pdf.setLineWidth(1.1)
    pdf.line(table_card_x + 18, table_card_y + table_card_h - 46, table_card_x + 156, table_card_y + table_card_h - 46)
    draw_analysis_watermark(pdf, table_card_x + 20, table_card_y + 18, CONTENT_W - 40, table_card_h - 70)
    table = build_results_table()
    table_w, table_h = table.wrap(CONTENT_W - 28, table_card_h - 76)
    table.drawOn(pdf, table_card_x + 14, table_card_y + 16)

    footer_card_y = 48
    footer_h = 118
    draw_card(pdf, MARGIN_X, footer_card_y, CONTENT_W, footer_h, fill_color=PANEL, stroke_color=BORDER, radius=14)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 8)
    pdf.drawString(MARGIN_X + 16, footer_card_y + footer_h - 16, "COMMERCIAL REFERENCE")
    pdf.setStrokeColor(GOLD)
    pdf.setLineWidth(1)
    pdf.line(MARGIN_X + 16, footer_card_y + footer_h - 20, MARGIN_X + 88, footer_card_y + footer_h - 20)

    inner_gap = 8
    inner_w = (CONTENT_W - 32 - inner_gap) / 2
    row_heights = [28, 24, 22]
    current_top = footer_card_y + footer_h - 34
    for row_index, row_height in enumerate(row_heights):
        y = current_top - row_height
        left_label, left_value = BUYER_REFERENCE[row_index * 2]
        right_label, right_value = BUYER_REFERENCE[(row_index * 2) + 1]
        draw_info_item(pdf, MARGIN_X + 16, y, inner_w, row_height, left_label, left_value)
        draw_info_item(pdf, MARGIN_X + 16 + inner_w + inner_gap, y, inner_w, row_height, right_label, right_value)
        current_top = y - 4

    pdf.setStrokeColor(BORDER)
    pdf.setLineWidth(1)
    pdf.line(MARGIN_X, 40, PAGE_WIDTH - MARGIN_X, 40)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica", 8.2)
    pdf.drawCentredString(PAGE_WIDTH / 2, 27, f"{ADDRESS_LINES[0]}  |  {ADDRESS_LINES[1]}")
    pdf.drawCentredString(PAGE_WIDTH / 2, 15, f"{CONTACT_LINE}  |  {WEB_LINE}")

    pdf.showPage()
    pdf.save()


def flatten_pdf_to_compat(vector_path: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    FLATTENED_IMAGE.parent.mkdir(parents=True, exist_ok=True)

    with fitz.open(vector_path) as doc:
        page = doc[0]
        pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), alpha=False)
        pix.save(str(FLATTENED_IMAGE))

    with fitz.open(str(FLATTENED_IMAGE)) as image_doc:
        pdf_bytes = image_doc.convert_to_pdf()

    output_path.write_bytes(pdf_bytes)


def generate() -> None:
    build_vector_pdf(VECTOR_OUTPUT)
    flatten_pdf_to_compat(VECTOR_OUTPUT, OUTPUT)
    DELIVERY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    DELIVERY_OUTPUT.write_bytes(OUTPUT.read_bytes())
    if ASSET_OUTPUT is not None:
        ASSET_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        ASSET_OUTPUT.write_bytes(OUTPUT.read_bytes())


if __name__ == "__main__":
    generate()
