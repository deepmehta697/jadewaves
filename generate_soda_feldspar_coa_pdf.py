from io import BytesIO
from pathlib import Path

import fitz
from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output" / "pdf" / "soda-feldspar-coa.pdf"
VECTOR_OUTPUT = ROOT / "tmp" / "pdfs" / "soda-feldspar-coa-vector.pdf"
FLATTENED_IMAGE = ROOT / "tmp" / "pdfs" / "soda-feldspar-coa-flattened.png"
LOGO = ROOT / "assets" / "jade-waves-logo-transparent.png"

PAGE_WIDTH, PAGE_HEIGHT = landscape(A4)
MARGIN_X = 26
MARGIN_Y = 22
CONTENT_W = PAGE_WIDTH - (MARGIN_X * 2)

INK = colors.HexColor("#16314F")
INK_SOFT = colors.HexColor("#5E7085")
ACCENT = colors.HexColor("#0B7CB5")
ACCENT_SOFT = colors.HexColor("#EAF6FB")
BORDER = colors.HexColor("#C9D8E6")
PANEL = colors.HexColor("#F8FBFD")
PANEL_ALT = colors.HexColor("#F1F7FB")
WHITE = colors.white

COMPANY_NAME = "Jade Waves Enterprise"
ADDRESS_LINES = [
    "A-11 Florence, Science City Road,",
    "Ahmedabad-380060 Gujarat, India",
]
CONTACT_LINE = "+91-999-883-5503  |  deep@jadewavesenterprise.com"
WEB_LINE = "www.jadewavesenterprise.com"

GRADE_ROWS = [
    ("1", "Grade", "First", "Second"),
    ("2", "SiO2", "68% (+/- 1%)", "72% (+/- 2%)"),
    ("3", "AL2O3", "18% (+/- 1%)", "17% (+/- 1%)"),
    ("4", "K2O", "0.50% (+/- 0.5%)", "2% (+/- 1%)"),
    ("5", "Na2O", "10% (+/- 1%)", "8% (+/- 1%)"),
    ("6", "Fe2O3", "0.10% (+/- 0.03%)", "0.15% (+/- 0.05%)"),
    ("7", "MgO", "0.1% (+/- 0.1%)", "0.2% (+/- 0.1%)"),
    ("8", "CaO", "0.05% (+/- 0.5%)", "0.2% (+/- 0.1%)"),
    ("9", "TiO2", "NIL", "NIL"),
    ("10", "LOI", "0.10%", "0.20%"),
    ("11", "Firing Result 1175C-1220C", "Milky White", "Off White"),
    ("12", "Firing Appearance", "White to Cream", "White to Cream"),
]

BUYER_REFERENCE = [
    (
        "Application",
        "Ceramic and tile production, sanitaryware manufacturing, glass production, and engineered stone or flux-driven mineral systems.",
    ),
    ("Forms", "Powder, available in 100-350 mesh BSS."),
    ("Typical grade range", "S1: Na2O 10% (+/- 1%). S2: Na2O 8% (+/- 1%). SiO2 68-72% and Fe2O3 0.10-0.15% across the shown grades."),
    ("Packing options", "Jumbo bags with export-ready packing aligned to buyer requirement."),
    ("HSN code", "25291020"),
    ("Inquiry contact", "deep@jadewavesenterprise.com  |  +91-999-883-5503"),
]

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.3,
        leading=10.2,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="BodySmall",
        parent=styles["Body"],
        fontSize=7.2,
        leading=8.6,
        textColor=INK_SOFT,
    )
)
styles.add(
    ParagraphStyle(
        name="InfoValue",
        parent=styles["Body"],
        fontSize=8.1,
        leading=9.4,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="TableCell",
        parent=styles["Body"],
        fontSize=8.6,
        leading=10.0,
        textColor=INK,
    )
)


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
    for style_name in style_names:
        if paragraph_height(text, style_name, width) <= max_height:
            chosen = style_name
            break
    paragraph = Paragraph(text, styles[chosen])
    _, height = paragraph.wrap(width, max_height)
    paragraph.drawOn(pdf, x, y_top - height)
    return y_top - height


def build_grade_table() -> Table:
    rows = [
        [
            Paragraph("<b>SR. NO.</b>", styles["TableCell"]),
            Paragraph("<b>PRODUCT</b>", styles["TableCell"]),
            Paragraph("<b>S1</b>", styles["TableCell"]),
            Paragraph("<b>S2</b>", styles["TableCell"]),
        ]
    ]
    for row in GRADE_ROWS:
        rows.append([Paragraph(cell, styles["TableCell"]) for cell in row])

    table = Table(rows, colWidths=[58, 220, 202, 202], repeatRows=1)
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 9.2),
            ("ALIGN", (0, 0), (0, -1), "CENTER"),
            ("ALIGN", (2, 1), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("GRID", (0, 0), (-1, -1), 0.55, BORDER),
        ]
    )
    for row_index in range(1, len(rows)):
        style.add("BACKGROUND", (0, row_index), (-1, row_index), WHITE if row_index % 2 else PANEL_ALT)
    table.setStyle(style)
    return table


def build_info_table() -> Table:
    rows = []
    for label, value in BUYER_REFERENCE:
        rows.append(
            [
                Paragraph(f"<b>{label}</b>", styles["Body"]),
                Paragraph(value, styles["InfoValue"]),
            ]
        )
    table = Table(rows, colWidths=[130, CONTENT_W - 158])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), WHITE),
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [PANEL_ALT, WHITE]),
                ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return table


def draw_header(pdf: canvas.Canvas) -> None:
    pdf.setFillColor(colors.HexColor("#F8FBFD"))
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_card(pdf, MARGIN_X - 8, MARGIN_Y - 4, CONTENT_W + 16, PAGE_HEIGHT - (MARGIN_Y * 2) + 8, fill_color=WHITE, stroke_color=BORDER, radius=18)

    pdf.setFillColor(ACCENT)
    pdf.roundRect(MARGIN_X - 8, PAGE_HEIGHT - 20, CONTENT_W + 16, 6, 3, fill=1, stroke=0)
    pdf.setFillColor(ACCENT)
    pdf.setFont("Helvetica-Bold", 8.5)
    pdf.drawString(MARGIN_X, PAGE_HEIGHT - 42, "PRODUCT QUALITY DOCUMENT")

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 30)
    pdf.drawString(MARGIN_X, PAGE_HEIGHT - 76, "Soda Feldspar")
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(MARGIN_X, PAGE_HEIGHT - 96, "Certificate of Analysis / Grade Matrix")
    pdf.setStrokeColor(ACCENT)
    pdf.setLineWidth(1.8)
    pdf.line(MARGIN_X, PAGE_HEIGHT - 108, MARGIN_X + 180, PAGE_HEIGHT - 108)

    draw_card(pdf, MARGIN_X, PAGE_HEIGHT - 148, 170, 28, fill_color=ACCENT_SOFT, stroke_color=BORDER, radius=12, line_width=0.8)
    pdf.setFillColor(ACCENT)
    pdf.setFont("Helvetica-Bold", 9.2)
    pdf.drawString(MARGIN_X + 12, PAGE_HEIGHT - 131, "AVAILABLE IN 100-350 MESH BSS")
    draw_card(pdf, MARGIN_X + 182, PAGE_HEIGHT - 148, 95, 28, fill_color=PANEL_ALT, stroke_color=BORDER, radius=12, line_width=0.8)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 9.2)
    pdf.drawString(MARGIN_X + 195, PAGE_HEIGHT - 131, "S1: FIRST")
    draw_card(pdf, MARGIN_X + 287, PAGE_HEIGHT - 148, 108, 28, fill_color=PANEL_ALT, stroke_color=BORDER, radius=12, line_width=0.8)
    pdf.drawString(MARGIN_X + 300, PAGE_HEIGHT - 131, "S2: SECOND")

    if LOGO.exists():
        pdf.drawImage(str(LOGO), PAGE_WIDTH - MARGIN_X - 102, PAGE_HEIGHT - 96, width=102, height=62, mask="auto", preserveAspectRatio=True)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawRightString(PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 108, COMPANY_NAME)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica", 8.2)
    pdf.drawRightString(PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 121, "Ahmedabad, Gujarat, India")
    draw_paragraph(
        pdf,
        "S1 and S2 are shown here as separate soda feldspar grades based on the client-provided reference chart.",
        "BodySmall",
        PAGE_WIDTH - 260,
        PAGE_HEIGHT - 136,
        232,
    )


def build_vector_pdf(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pdf = canvas.Canvas(str(output_path), pagesize=landscape(A4))
    pdf.setTitle("Jade Waves Enterprise - Soda Feldspar COA")
    pdf.setAuthor(COMPANY_NAME)
    pdf.setSubject("Soda Feldspar COA / Grade Matrix")

    draw_header(pdf)

    table_card_y = 192
    table_card_h = 245
    draw_card(pdf, MARGIN_X, table_card_y, CONTENT_W, table_card_h, fill_color=PANEL, stroke_color=BORDER, radius=16)
    pdf.setFillColor(ACCENT)
    pdf.setFont("Helvetica-Bold", 8.2)
    pdf.drawString(MARGIN_X + 14, table_card_y + table_card_h - 16, "GRADE MATRIX")

    table = build_grade_table()
    table.wrapOn(pdf, CONTENT_W - 20, table_card_h - 24)
    table.drawOn(pdf, MARGIN_X + 10, table_card_y + 10)

    info_card_y = 40
    info_card_h = 132
    draw_card(pdf, MARGIN_X, info_card_y, CONTENT_W, info_card_h, fill_color=WHITE, stroke_color=BORDER, radius=16)
    pdf.setFillColor(ACCENT)
    pdf.setFont("Helvetica-Bold", 8.2)
    pdf.drawString(MARGIN_X + 14, info_card_y + info_card_h - 16, "BUYER REFERENCE")

    info_table = build_info_table()
    info_table.wrapOn(pdf, CONTENT_W - 20, info_card_h - 28)
    info_table.drawOn(pdf, MARGIN_X + 10, info_card_y + 10)

    pdf.setStrokeColor(BORDER)
    pdf.setLineWidth(1)
    pdf.line(MARGIN_X, 28, PAGE_WIDTH - MARGIN_X, 28)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica", 8.1)
    pdf.drawCentredString(PAGE_WIDTH / 2, 16, f"{ADDRESS_LINES[0]}  |  {ADDRESS_LINES[1]}  |  {CONTACT_LINE}  |  {WEB_LINE}")

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


if __name__ == "__main__":
    generate()
