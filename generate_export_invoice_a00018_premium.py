from __future__ import annotations

import shutil
from decimal import Decimal
from pathlib import Path

import fitz
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output" / "pdf" / "export-invoice-a00018-premium.pdf"
DELIVERY_OUTPUT = Path(
    "/Users/deepmehta/Documents/Jade Waves Enterprise/Clients/GrassPro Private Limited/A00018/Export Invoice_A00018_Premium.pdf"
)
PREVIEW = ROOT / "tmp" / "pdfs" / "export-invoice-a00018-premium-preview.png"
LOGO = ROOT / "assets" / "jade-waves-logo-transparent.png"
SIGNATURE = ROOT / "assets" / "coa-silica-sign-stamp.png"

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_X = 28
MARGIN_Y = 26
CONTENT_W = PAGE_WIDTH - (MARGIN_X * 2)

INK = colors.HexColor("#13243C")
INK_SOFT = colors.HexColor("#5A6A7F")
ACCENT = colors.HexColor("#2F6F67")
ACCENT_SOFT = colors.HexColor("#E9F3F1")
HEADER_DARK = colors.HexColor("#10263A")
PAGE_BG = colors.HexColor("#F3F0EA")
PANEL = colors.HexColor("#FCFBF8")
PANEL_ALT = colors.HexColor("#F7F4EE")
BORDER = colors.HexColor("#D8D6D0")
GOLD = colors.HexColor("#C7A35B")
GOLD_SOFT = colors.HexColor("#F5E8C8")
WHITE = colors.white

COMPANY = {
    "name": "Jade Waves Enterprise",
    "address": [
        "A-11 Florence Residency, Opposite Sola Police Chowky",
        "Ahmedabad, Gujarat 380060",
        "India",
    ],
    "gstin": "24AAUFJ5543K1ZU",
    "iec": "AAUFJ5543K",
}

INVOICE = {
    "number": "A00018",
    "date": "26 March 2026",
    "lut_no": "AD2403260494544",
    "country": "India",
    "state_code": "Gujarat / 380060",
    "port_loading": "Mundra, India",
    "port_discharge": "Male",
    "final_destination": "Maldives",
    "incoterm": "CIF",
    "payment_terms": "100% Advance",
    "packages": "933 bags of 30 kgs each",
}

PARTY = {
    "name": "Grass Pro Private Limited",
    "address": [
        "Yaagoothuge Lh Kurendhoo",
        "Republic of Maldives",
    ],
    "registration": "Company Registration Number: C0563/2022",
    "attention": "Attn: Mohamed hameed",
    "phone": "Tel: +9609926543",
}

ITEM = {
    "product": "Quartz Silica",
    "description_lines": [
        "Packed in 30 kg bags",
        "HS Code: 25061020",
        "Country of Origin: India",
    ],
    "qty_mts": Decimal("28"),
    "rate_usd": Decimal("101"),
    "igst_rate": Decimal("0"),
}

BANK = {
    "account_name": "JADE WAVES ENTERPRISE",
    "bank_name": "HDFC BANK",
    "account_number": "99905500000022",
    "ifsc": "HDFC0006638",
    "swift": "HDFCINBBXXX",
    "address": [
        "Ground Floor, Shop No. 3, City Center,",
        "Science City Road, Near Shukan Mall,",
        "Ahmedabad, Gujarat 380060 - India",
    ],
}


def money(value: Decimal) -> str:
    return f"{value:,.2f}"


def integerish(value: Decimal) -> str:
    if value == value.to_integral():
        return f"{int(value)}"
    return f"{value.normalize()}"


def amount_to_words(value: Decimal) -> str:
    units = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def under_thousand(number: int) -> str:
        parts: list[str] = []
        hundreds = number // 100
        remainder = number % 100
        if hundreds:
            parts.append(f"{units[hundreds]} Hundred")
        if remainder:
            if remainder < 20:
                parts.append(units[remainder])
            else:
                parts.append(tens[remainder // 10])
                if remainder % 10:
                    parts.append(units[remainder % 10])
        return " ".join(part for part in parts if part)

    whole = int(value.quantize(Decimal("1")))
    if whole == 0:
        return "USD Zero Only"

    parts: list[str] = []
    thousands = whole // 1000
    remainder = whole % 1000
    if thousands:
        parts.append(f"{under_thousand(thousands)} Thousand")
    if remainder:
        parts.append(under_thousand(remainder))

    return f"USD {' '.join(parts)} Only"


ITEM_AMOUNT = ITEM["qty_mts"] * ITEM["rate_usd"]
IGST_AMOUNT = Decimal("0")
TOTAL_AMOUNT = ITEM_AMOUNT + IGST_AMOUNT
AMOUNT_WORDS = amount_to_words(TOTAL_AMOUNT)


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.7,
        leading=11,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Small",
        parent=styles["Body"],
        fontSize=7.3,
        leading=9,
        textColor=INK_SOFT,
    )
)
styles.add(
    ParagraphStyle(
        name="HeaderSmall",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.7,
        leading=9.2,
        textColor=colors.HexColor("#D7E0EA"),
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="HeaderTiny",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=6.7,
        leading=8.2,
        textColor=colors.HexColor("#B7C4D1"),
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Label",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=6.8,
        leading=7.6,
        textColor=ACCENT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Value",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.1,
        leading=10.5,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="ValueTight",
        parent=styles["Value"],
        fontSize=8.0,
        leading=9.0,
    )
)
styles.add(
    ParagraphStyle(
        name="ValueRight",
        parent=styles["Value"],
        alignment=TA_RIGHT,
    )
)
styles.add(
    ParagraphStyle(
        name="CardTitle",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=8.2,
        leading=9,
        textColor=INK_SOFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="PartyTitle",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=8.8,
        leading=10,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="TableCell",
        parent=styles["Body"],
        fontSize=8.1,
        leading=9.3,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="TableCellSmall",
        parent=styles["Small"],
        fontSize=7.5,
        leading=8.6,
        textColor=INK_SOFT,
    )
)
styles.add(
    ParagraphStyle(
        name="TotalsLabel",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=8.1,
        leading=9,
        textColor=INK_SOFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="TotalsValue",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=10.3,
        leading=11.4,
        textColor=INK,
        alignment=TA_RIGHT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Words",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=7.3,
        leading=8.5,
        textColor=INK,
        spaceAfter=0,
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


def draw_kv_rows(pdf: canvas.Canvas, x: float, y_top: float, width: float, rows: list[tuple[str, str]], line_gap: float = 4.5) -> float:
    current_y = y_top
    for label, value in rows:
        current_y = draw_paragraph(pdf, label, "Label", x, current_y, width)
        current_y = draw_paragraph_fit(pdf, value, ["Value", "ValueTight"], x, current_y - 1, width, 22)
        current_y -= line_gap
    return current_y


def draw_header(pdf: canvas.Canvas) -> None:
    pdf.setFillColor(PAGE_BG)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    draw_card(pdf, MARGIN_X - 6, MARGIN_Y - 10, CONTENT_W + 12, PAGE_HEIGHT - (MARGIN_Y * 2) + 18, fill_color=WHITE, stroke_color=BORDER, radius=22)
    draw_card(pdf, MARGIN_X - 6, PAGE_HEIGHT - 164, CONTENT_W + 12, 136, fill_color=HEADER_DARK, stroke_color=HEADER_DARK, radius=22, line_width=0)

    pdf.setFillColor(GOLD)
    pdf.roundRect(MARGIN_X + 10, PAGE_HEIGHT - 56, 120, 2.5, 1.2, fill=1, stroke=0)
    pdf.setFont("Helvetica-Bold", 8.2)
    pdf.drawString(MARGIN_X + 10, PAGE_HEIGHT - 70, "COMMERCIAL EXPORT DOCUMENT")

    pdf.setFillColor(WHITE)
    pdf.setFont("Times-Bold", 28)
    pdf.drawString(MARGIN_X + 10, PAGE_HEIGHT - 96, "Export Invoice")

    subtitle = "Supply under Letter of Undertaking without payment of Integrated Tax (IGST)"
    draw_paragraph(pdf, subtitle, "HeaderTiny", MARGIN_X + 10, PAGE_HEIGHT - 108, 305)

    pdf.setFillColor(colors.HexColor("#D7E0EA"))
    pdf.setFont("Helvetica-Bold", 10.5)
    pdf.drawString(MARGIN_X + 10, PAGE_HEIGHT - 139, COMPANY["name"].upper())

    address_text = "<br/>".join(COMPANY["address"])
    draw_paragraph(pdf, address_text, "HeaderSmall", MARGIN_X + 10, PAGE_HEIGHT - 146, 240)

    brand_x = PAGE_WIDTH - MARGIN_X - 140
    brand_y = PAGE_HEIGHT - 150
    draw_card(pdf, brand_x, brand_y, 130, 102, fill_color=PANEL, stroke_color=colors.HexColor("#2B3D50"), radius=18, line_width=1)
    if LOGO.exists():
        pdf.drawImage(str(LOGO), brand_x + 24, brand_y + 44, width=82, height=42, mask="auto", preserveAspectRatio=True)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 8.6)
    pdf.drawCentredString(brand_x + 65, brand_y + 30, "Jade Waves")
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica", 7.5)
    pdf.drawCentredString(brand_x + 65, brand_y + 19, "Ahmedabad, Gujarat, India")


def draw_info_cards(pdf: canvas.Canvas) -> None:
    top_y = 662
    card_h = 116
    gap = 12
    card_w = (CONTENT_W - (gap * 2)) / 3

    document_rows = [
        ("Invoice No", INVOICE["number"]),
        ("Invoice Date", INVOICE["date"]),
        ("LUT No", INVOICE["lut_no"]),
    ]
    shipment_rows = [
        ("Port of Loading", INVOICE["port_loading"]),
        ("Port of Discharge", INVOICE["port_discharge"]),
        ("Final Destination", INVOICE["final_destination"]),
    ]
    compliance_rows = [
        ("GSTIN", COMPANY["gstin"]),
        ("IEC", COMPANY["iec"]),
        ("Origin / State / Code", f"{INVOICE['country']} / {INVOICE['state_code']}"),
    ]

    cards = [
        ("Document Summary", document_rows, PANEL),
        ("Shipment Route", shipment_rows, ACCENT_SOFT),
        ("Compliance", compliance_rows, PANEL_ALT),
    ]

    for index, (title, rows, fill_color) in enumerate(cards):
        x = MARGIN_X + index * (card_w + gap)
        y = top_y - card_h
        draw_card(pdf, x, y, card_w, card_h, fill_color=fill_color, stroke_color=BORDER, radius=16)
        pdf.setFillColor(GOLD)
        pdf.roundRect(x + 14, y + card_h - 11, 42, 2.2, 1.1, fill=1, stroke=0)
        pdf.setFillColor(INK_SOFT)
        pdf.setFont("Helvetica-Bold", 8.1)
        pdf.drawString(x + 14, y + card_h - 24, title.upper())
        draw_kv_rows(pdf, x + 14, y + card_h - 36, card_w - 28, rows, line_gap=3.8)


def draw_party_cards(pdf: canvas.Canvas) -> None:
    top_y = 528
    card_h = 96
    gap = 12
    card_w = (CONTENT_W - gap) / 2

    def draw_party(x: float, title: str) -> None:
        y = top_y - card_h
        draw_card(pdf, x, y, card_w, card_h, fill_color=WHITE, stroke_color=BORDER, radius=16)
        pdf.setFillColor(GOLD)
        pdf.roundRect(x + 14, y + card_h - 11, 32, 2.2, 1.1, fill=1, stroke=0)
        pdf.setFillColor(INK_SOFT)
        pdf.setFont("Helvetica-Bold", 8.2)
        pdf.drawString(x + 14, y + card_h - 24, title.upper())
        draw_paragraph(pdf, PARTY["name"], "PartyTitle", x + 14, y + card_h - 36, card_w - 28)
        details = "<br/>".join(PARTY["address"] + [PARTY["registration"], PARTY["attention"], PARTY["phone"]])
        draw_paragraph_fit(pdf, details, ["Body", "Small"], x + 14, y + card_h - 48, card_w - 28, 52)

    draw_party(MARGIN_X, "Consignee")
    draw_party(MARGIN_X + card_w + gap, "Notify")


def draw_commercial_strip(pdf: canvas.Canvas) -> None:
    y = 404
    h = 38
    gap = 10
    left_w = 178
    middle_w = 164
    right_w = CONTENT_W - left_w - middle_w - (gap * 2)

    cards = [
        (MARGIN_X, left_w, "Incoterm", INVOICE["incoterm"], GOLD_SOFT),
        (MARGIN_X + left_w + gap, middle_w, "Payment Terms", INVOICE["payment_terms"], PANEL_ALT),
        (MARGIN_X + left_w + middle_w + (gap * 2), right_w, "Packages", INVOICE["packages"], ACCENT_SOFT),
    ]

    for x, width, label, value, fill in cards:
        draw_card(pdf, x, y, width, h, fill_color=fill, stroke_color=BORDER, radius=14, line_width=0.9)
        pdf.setFillColor(INK_SOFT)
        pdf.setFont("Helvetica-Bold", 7.5)
        pdf.drawString(x + 12, y + h - 15, label.upper())
        draw_paragraph_fit(pdf, value, ["Value", "ValueTight"], x + 12, y + 16, width - 24, 14)


def build_items_table() -> Table:
    description = (
        f"<b>{ITEM['product']}</b><br/>"
        f"{ITEM['description_lines'][0]}<br/>"
        f"{ITEM['description_lines'][1]}<br/>"
        f"{ITEM['description_lines'][2]}"
    )
    rows = [
        [
            Paragraph("<b>No.</b>", styles["TableCell"]),
            Paragraph("<b>Description</b>", styles["TableCell"]),
            Paragraph("<b>Qty (MT)</b>", styles["TableCell"]),
            Paragraph("<b>Rate (USD)</b>", styles["TableCell"]),
            Paragraph("<b>Amount (USD)</b>", styles["TableCell"]),
            Paragraph("<b>IGST</b>", styles["TableCell"]),
            Paragraph("<b>Total (USD)</b>", styles["TableCell"]),
        ],
        [
            Paragraph("1", styles["TableCell"]),
            Paragraph(description, styles["TableCell"]),
            Paragraph(integerish(ITEM["qty_mts"]), styles["TableCell"]),
            Paragraph(money(ITEM["rate_usd"]), styles["TableCell"]),
            Paragraph(money(ITEM_AMOUNT), styles["TableCell"]),
            Paragraph("0%", styles["TableCell"]),
            Paragraph(money(TOTAL_AMOUNT), styles["TableCell"]),
        ],
    ]

    table = Table(rows, colWidths=[28, 206, 51, 68, 76, 39, 71], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HEADER_DARK),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 7.7),
                ("ALIGN", (0, 0), (0, -1), "CENTER"),
                ("ALIGN", (2, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
                ("LINEBELOW", (0, 0), (-1, 0), 1.0, GOLD),
                ("BACKGROUND", (0, 1), (-1, -1), WHITE),
            ]
        )
    )
    return table


def draw_items_section(pdf: canvas.Canvas) -> None:
    x = MARGIN_X
    y = 250
    h = 138
    draw_card(pdf, x, y, CONTENT_W, h, fill_color=PANEL, stroke_color=BORDER, radius=18)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 8.2)
    pdf.drawString(x + 16, y + h - 22, "ITEM DETAILS")
    table = build_items_table()
    table.wrapOn(pdf, CONTENT_W - 32, 100)
    table.drawOn(pdf, x + 16, y + 18)


def build_totals_table() -> Table:
    rows = [
        [Paragraph("Total Quantity in Metric Tons", styles["TotalsLabel"]), Paragraph(integerish(ITEM["qty_mts"]), styles["TotalsValue"])],
        [Paragraph("Total Amount before Tax", styles["TotalsLabel"]), Paragraph(money(ITEM_AMOUNT), styles["TotalsValue"])],
        [Paragraph("IGST", styles["TotalsLabel"]), Paragraph(money(IGST_AMOUNT), styles["TotalsValue"])],
        [Paragraph("Total Amount after Tax", styles["TotalsLabel"]), Paragraph(money(TOTAL_AMOUNT), styles["TotalsValue"])],
    ]
    table = Table(rows, colWidths=[168, 82])
    table.setStyle(
        TableStyle(
            [
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [WHITE, PANEL_ALT]),
                ("GRID", (0, 0), (-1, -1), 0.45, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return table


def build_bank_table() -> Table:
    rows = [
        [Paragraph("<b>Account Name</b>", styles["TableCellSmall"]), Paragraph(BANK["account_name"], styles["TableCell"])],
        [Paragraph("<b>Bank</b>", styles["TableCellSmall"]), Paragraph(BANK["bank_name"], styles["TableCell"])],
        [Paragraph("<b>Account Number</b>", styles["TableCellSmall"]), Paragraph(BANK["account_number"], styles["TableCell"])],
        [Paragraph("<b>IFSC</b>", styles["TableCellSmall"]), Paragraph(BANK["ifsc"], styles["TableCell"])],
        [Paragraph("<b>SWIFT</b>", styles["TableCellSmall"]), Paragraph(BANK["swift"], styles["TableCell"])],
        [Paragraph("<b>Bank Address</b>", styles["TableCellSmall"]), Paragraph("<br/>".join(BANK["address"]), styles["TableCellSmall"])],
    ]
    table = Table(rows, colWidths=[84, 164])
    table.setStyle(
        TableStyle(
            [
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [WHITE, PANEL_ALT]),
                ("GRID", (0, 0), (-1, -1), 0.45, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def draw_bottom_section(pdf: canvas.Canvas) -> None:
    left_x = MARGIN_X
    right_x = MARGIN_X + 274
    bottom_y = 58
    words_y = bottom_y + 116
    words_h = 66

    draw_card(pdf, left_x, words_y, 260, words_h, fill_color=GOLD_SOFT, stroke_color=BORDER, radius=16)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 7.9)
    pdf.drawString(left_x + 14, words_y + words_h - 15, "TOTAL IN WORDS")
    draw_paragraph_fit(pdf, AMOUNT_WORDS, ["Words", "ValueTight", "Small"], left_x + 14, words_y + words_h - 28, 232, 28)

    draw_card(pdf, left_x, bottom_y, 260, 112, fill_color=WHITE, stroke_color=BORDER, radius=16)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 8.2)
    pdf.drawString(left_x + 14, bottom_y + 92, "BANK DETAILS")
    bank_table = build_bank_table()
    bank_table.wrapOn(pdf, 232, 78)
    bank_table.drawOn(pdf, left_x + 14, bottom_y + 12)

    draw_card(pdf, right_x, bottom_y + 86, 260, 94, fill_color=WHITE, stroke_color=BORDER, radius=16)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 8.2)
    pdf.drawString(right_x + 14, bottom_y + 160, "TOTALS")
    totals_table = build_totals_table()
    totals_table.wrapOn(pdf, 232, 74)
    totals_table.drawOn(pdf, right_x + 14, bottom_y + 98)

    draw_card(pdf, right_x, bottom_y, 260, 78, fill_color=PANEL_ALT, stroke_color=BORDER, radius=16)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 8.2)
    pdf.drawString(right_x + 14, bottom_y + 60, "DECLARATION")
    declaration = "Certified that the particulars given above are true and correct."
    draw_paragraph_fit(pdf, declaration, ["Small"], right_x + 14, bottom_y + 49, 138, 18)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 8.1)
    pdf.drawString(right_x + 14, bottom_y + 24, f"For {COMPANY['name']}")
    if SIGNATURE.exists():
        pdf.drawImage(str(SIGNATURE), right_x + 132, bottom_y + 16, width=100, height=38, mask="auto", preserveAspectRatio=True)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 7.4)
    pdf.drawRightString(right_x + 244, bottom_y + 10, "Authorized Signatory")


def build_pdf(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output_path), pagesize=A4)
    pdf.setTitle("Jade Waves Enterprise - Export Invoice A00018 - Premium")
    pdf.setAuthor(COMPANY["name"])
    pdf.setSubject("Premium export invoice generated from A00018")

    draw_header(pdf)
    draw_info_cards(pdf)
    draw_party_cards(pdf)
    draw_commercial_strip(pdf)
    draw_items_section(pdf)
    draw_bottom_section(pdf)

    pdf.save()


def render_preview(pdf_path: Path, preview_path: Path) -> None:
    preview_path.parent.mkdir(parents=True, exist_ok=True)
    with fitz.open(pdf_path) as document:
        page = document[0]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
        pix.save(preview_path)


def main() -> None:
    build_pdf(OUTPUT)
    render_preview(OUTPUT, PREVIEW)
    DELIVERY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(OUTPUT, DELIVERY_OUTPUT)
    print(f"PDF: {OUTPUT}")
    print(f"Preview: {PREVIEW}")
    print(f"Delivery copy: {DELIVERY_OUTPUT}")


if __name__ == "__main__":
    main()
