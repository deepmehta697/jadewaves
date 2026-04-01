from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP
from html import escape
from pathlib import Path

import fitz
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = ROOT / "output" / "pdf"
DEFAULT_PREVIEW_DIR = ROOT / "tmp" / "pdfs"

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


def text(value: object, default: str = "") -> str:
    if value is None:
        return default
    return str(value).strip()


def escaped(value: object, default: str = "") -> str:
    return escape(text(value, default), quote=False)


def clean_lines(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [text(item) for item in value if text(item)]
    line = text(value)
    return [line] if line else []


def decimal_value(value: object, default: str = "0") -> Decimal:
    raw = text(value, default).replace(",", "")
    if not raw:
        raw = default
    return Decimal(raw)


def resolve_file(path_value: object, data_path: Path) -> Path | None:
    raw = text(path_value)
    if not raw:
        return None
    candidate = Path(raw).expanduser()
    if candidate.is_absolute():
        return candidate
    from_data = (data_path.parent / candidate).resolve()
    if from_data.exists():
        return from_data
    return (ROOT / candidate).resolve()


def money(value: Decimal) -> str:
    return f"{value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP):,.2f}"


def integerish(value: Decimal) -> str:
    normalized = value.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
    if normalized == normalized.to_integral():
        return str(int(normalized))
    return f"{normalized.normalize()}"


def amount_to_words(value: Decimal, currency: str) -> str:
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
    scales = [
        (1_000_000_000, "Billion"),
        (1_000_000, "Million"),
        (1_000, "Thousand"),
    ]

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

    whole = int(value.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    if whole == 0:
        return f"{currency.upper()} Zero Only"

    remaining = whole
    parts: list[str] = []
    for scale_value, scale_name in scales:
        if remaining >= scale_value:
            count = remaining // scale_value
            parts.append(f"{under_thousand(count)} {scale_name}")
            remaining %= scale_value
    if remaining:
        parts.append(under_thousand(remaining))

    return f"{currency.upper()} {' '.join(parts)} Only"


def paragraph_html(lines: list[str]) -> str:
    return "<br/>".join(escaped(line) for line in lines if text(line))


def build_context(data: dict, data_path: Path) -> dict:
    company_raw = data.get("company", {})
    invoice_raw = data.get("invoice", {})
    consignee_raw = data.get("consignee", {})
    notify_raw = data.get("notify") or consignee_raw
    bank_raw = data.get("bank", {})
    items_raw = data.get("items", [])
    if not items_raw:
        raise ValueError("Invoice data must include at least one item in the 'items' list.")

    company = {
        "name": text(company_raw.get("name"), "Jade Waves Enterprise"),
        "brand_name": text(company_raw.get("brand_name")) or text(company_raw.get("name"), "Jade Waves"),
        "address": clean_lines(company_raw.get("address")),
        "gstin": text(company_raw.get("gstin")),
        "iec": text(company_raw.get("iec")),
        "logo_path": resolve_file(company_raw.get("logo_path", "assets/jade-waves-logo-transparent.png"), data_path),
        "signature_path": resolve_file(company_raw.get("signature_path", "assets/coa-silica-sign-stamp.png"), data_path),
    }

    invoice = {
        "title": text(invoice_raw.get("title"), "Export Invoice"),
        "subtitle": text(
            invoice_raw.get("subtitle"),
            "Supply under Letter of Undertaking without payment of Integrated Tax (IGST)",
        ),
        "number": text(invoice_raw.get("number")),
        "date": text(invoice_raw.get("date")),
        "lut_no": text(invoice_raw.get("lut_no")),
        "country": text(invoice_raw.get("country"), "India"),
        "state_code": text(invoice_raw.get("state_code")),
        "port_loading": text(invoice_raw.get("port_loading")),
        "port_discharge": text(invoice_raw.get("port_discharge")),
        "final_destination": text(invoice_raw.get("final_destination")),
        "incoterm": text(invoice_raw.get("incoterm")),
        "payment_terms": text(invoice_raw.get("payment_terms")),
        "packages": text(invoice_raw.get("packages")),
        "currency": text(invoice_raw.get("currency"), "USD"),
        "declaration": text(
            invoice_raw.get("declaration"),
            "Certified that the particulars given above are true and correct.",
        ),
        "sr_no_label": text(invoice_raw.get("sr_no_label"), "Sr.No"),
        "description_column_label": text(invoice_raw.get("description_column_label"), "Item Description"),
        "quantity_column_label": text(invoice_raw.get("quantity_column_label"), "Quantity (Metric Ton)"),
        "rate_column_label": text(invoice_raw.get("rate_column_label"), "Rate Per Ton"),
        "amount_column_label": text(invoice_raw.get("amount_column_label"), "Amount"),
        "igst_column_label": text(invoice_raw.get("igst_column_label"), "IGST"),
        "total_column_label": text(invoice_raw.get("total_column_label"), "Total USD"),
        "quantity_summary_label": text(invoice_raw.get("quantity_summary_label"), "Total Quantity in Metric Tons"),
    }

    def normalize_party(raw: dict) -> dict:
        lines = clean_lines(raw.get("address"))
        for key in ("registration", "attention", "phone", "email"):
            value = text(raw.get(key))
            if value:
                lines.append(value)
        lines.extend(clean_lines(raw.get("extra_lines")))
        return {
            "name": text(raw.get("name")),
            "lines": lines,
        }

    consignee = normalize_party(consignee_raw)
    notify = normalize_party(notify_raw)

    bank_lines = clean_lines(bank_raw.get("address"))
    bank = {
        "account_name": text(bank_raw.get("account_name")),
        "bank_name": text(bank_raw.get("bank_name")),
        "account_number": text(bank_raw.get("account_number")),
        "ifsc": text(bank_raw.get("ifsc")),
        "swift": text(bank_raw.get("swift")),
        "address": bank_lines,
    }

    items = []
    subtotal = Decimal("0")
    total_igst = Decimal("0")
    total_quantity = Decimal("0")

    for index, item_raw in enumerate(items_raw, start=1):
        quantity = decimal_value(item_raw.get("quantity", item_raw.get("qty", "0")))
        rate = decimal_value(item_raw.get("rate", "0"))
        igst_rate = decimal_value(item_raw.get("igst_rate", "0"))
        description_lines = clean_lines(item_raw.get("description_lines"))
        if not description_lines and text(item_raw.get("description")):
            description_lines.append(text(item_raw.get("description")))
        hs_code = text(item_raw.get("hs_code"))
        if hs_code:
            description_lines.append(f"HS Code: {hs_code}")
        origin = text(item_raw.get("country_of_origin"))
        if origin:
            description_lines.append(f"Country of Origin: {origin}")

        amount = (quantity * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        igst_amount = (amount * igst_rate / Decimal("100")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        total = amount + igst_amount

        subtotal += amount
        total_igst += igst_amount
        total_quantity += quantity

        items.append(
            {
                "index": index,
                "product": text(item_raw.get("product"), f"Item {index}"),
                "description_lines": description_lines,
                "quantity": quantity,
                "rate": rate,
                "igst_rate": igst_rate,
                "amount": amount,
                "total": total,
            }
        )

    grand_total = subtotal + total_igst
    amount_words = text(invoice_raw.get("amount_words")) or amount_to_words(grand_total, invoice["currency"])

    return {
        "company": company,
        "invoice": invoice,
        "consignee": consignee,
        "notify": notify,
        "bank": bank,
        "items": items,
        "subtotal": subtotal,
        "total_igst": total_igst,
        "grand_total": grand_total,
        "total_quantity": total_quantity,
        "amount_words": amount_words,
    }


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.3,
        leading=10.2,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Small",
        parent=styles["Body"],
        fontSize=7.0,
        leading=8.4,
        textColor=INK_SOFT,
    )
)
styles.add(
    ParagraphStyle(
        name="HeaderSmall",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.4,
        leading=8.8,
        textColor=colors.HexColor("#D7E0EA"),
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="HeaderTiny",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=6.5,
        leading=7.8,
        textColor=colors.HexColor("#B7C4D1"),
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Label",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=6.5,
        leading=7.2,
        textColor=ACCENT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Value",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.7,
        leading=10.0,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="ValueTight",
        parent=styles["Value"],
        fontSize=7.8,
        leading=8.8,
    )
)
styles.add(
    ParagraphStyle(
        name="PartyTitle",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=8.4,
        leading=9.2,
        textColor=INK,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="TableCell",
        parent=styles["Body"],
        fontSize=7.7,
        leading=8.8,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="TableHeader",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=6.2,
        leading=7.1,
        textColor=WHITE,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="TableCellSmall",
        parent=styles["Small"],
        fontSize=7.0,
        leading=8.0,
        textColor=INK_SOFT,
    )
)
styles.add(
    ParagraphStyle(
        name="TotalsLabel",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=7.8,
        leading=8.8,
        textColor=INK_SOFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="TotalsValue",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=9.8,
        leading=10.8,
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
        fontSize=7.1,
        leading=8.1,
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


def paragraph_height(text_value: str, style_name: str, width: float) -> float:
    paragraph = Paragraph(text_value, styles[style_name])
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    return height


def draw_paragraph(pdf: canvas.Canvas, text_value: str, style_name: str, x: float, y_top: float, width: float) -> float:
    paragraph = Paragraph(text_value, styles[style_name])
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    paragraph.drawOn(pdf, x, y_top - height)
    return y_top - height


def draw_paragraph_fit(
    pdf: canvas.Canvas,
    text_value: str,
    style_names: list[str],
    x: float,
    y_top: float,
    width: float,
    max_height: float,
) -> float:
    chosen = style_names[-1]
    for style_name in style_names:
        if paragraph_height(text_value, style_name, width) <= max_height:
            chosen = style_name
            break
    paragraph = Paragraph(text_value, styles[chosen])
    _, height = paragraph.wrap(width, max_height)
    paragraph.drawOn(pdf, x, y_top - height)
    return y_top - height


def draw_kv_rows(pdf: canvas.Canvas, x: float, y_top: float, width: float, rows: list[tuple[str, str]], line_gap: float = 3.0) -> float:
    current_y = y_top
    for label, value in rows:
        if not text(value):
            continue
        current_y = draw_paragraph(pdf, escaped(label), "Label", x, current_y, width)
        current_y = draw_paragraph_fit(pdf, escaped(value), ["Value", "ValueTight"], x, current_y - 1, width, 18)
        current_y -= line_gap
    return current_y


def draw_header(pdf: canvas.Canvas, ctx: dict) -> None:
    company = ctx["company"]
    invoice = ctx["invoice"]

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
    pdf.drawString(MARGIN_X + 10, PAGE_HEIGHT - 96, invoice["title"])

    draw_paragraph(pdf, escaped(invoice["subtitle"]), "HeaderTiny", MARGIN_X + 10, PAGE_HEIGHT - 108, 320)

    pdf.setFillColor(colors.HexColor("#D7E0EA"))
    pdf.setFont("Helvetica-Bold", 10.2)
    pdf.drawString(MARGIN_X + 10, PAGE_HEIGHT - 139, company["name"].upper())
    draw_paragraph(pdf, paragraph_html(company["address"]), "HeaderSmall", MARGIN_X + 10, PAGE_HEIGHT - 146, 255)

    brand_x = PAGE_WIDTH - MARGIN_X - 140
    brand_y = PAGE_HEIGHT - 150
    draw_card(pdf, brand_x, brand_y, 130, 102, fill_color=PANEL, stroke_color=colors.HexColor("#2B3D50"), radius=18, line_width=1)
    logo_path = company["logo_path"]
    if logo_path and logo_path.exists():
        pdf.drawImage(str(logo_path), brand_x + 24, brand_y + 44, width=82, height=42, mask="auto", preserveAspectRatio=True)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 8.6)
    pdf.drawCentredString(brand_x + 65, brand_y + 30, company["brand_name"])
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica", 7.4)
    footer_line = ", ".join(company["address"][1:3]) if len(company["address"]) > 1 else "Ahmedabad, Gujarat, India"
    pdf.drawCentredString(brand_x + 65, brand_y + 19, footer_line[:38])


def draw_info_cards(pdf: canvas.Canvas, ctx: dict) -> None:
    company = ctx["company"]
    invoice = ctx["invoice"]
    top_y = 658
    card_h = 104
    gap = 12
    card_w = (CONTENT_W - (gap * 2)) / 3
    origin_state_code = " / ".join(part for part in [invoice["country"], invoice["state_code"]] if part)

    document_rows = [
        ("Invoice No", invoice["number"]),
        ("Invoice Date", invoice["date"]),
        ("LUT No", invoice["lut_no"]),
    ]
    shipment_rows = [
        ("Port of Loading", invoice["port_loading"]),
        ("Port of Discharge", invoice["port_discharge"]),
        ("Final Destination", invoice["final_destination"]),
    ]
    compliance_rows = [
        ("GSTIN", company["gstin"]),
        ("IEC", company["iec"]),
        ("Origin / State / Code", origin_state_code),
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
        pdf.setFont("Helvetica-Bold", 8.0)
        pdf.drawString(x + 14, y + card_h - 23, title.upper())
        draw_kv_rows(pdf, x + 14, y + card_h - 34, card_w - 28, rows)


def draw_party_cards(pdf: canvas.Canvas, ctx: dict) -> None:
    top_y = 530
    card_h = 82
    gap = 12
    card_w = (CONTENT_W - gap) / 2

    def draw_party(x: float, title: str, party: dict) -> None:
        y = top_y - card_h
        draw_card(pdf, x, y, card_w, card_h, fill_color=WHITE, stroke_color=BORDER, radius=16)
        pdf.setFillColor(GOLD)
        pdf.roundRect(x + 14, y + card_h - 11, 32, 2.2, 1.1, fill=1, stroke=0)
        pdf.setFillColor(INK_SOFT)
        pdf.setFont("Helvetica-Bold", 8.0)
        pdf.drawString(x + 14, y + card_h - 23, title.upper())
        draw_paragraph_fit(pdf, escaped(party["name"]), ["PartyTitle", "Value"], x + 14, y + card_h - 35, card_w - 28, 12)
        draw_paragraph_fit(pdf, paragraph_html(party["lines"]), ["Body", "Small"], x + 14, y + card_h - 46, card_w - 28, 40)

    draw_party(MARGIN_X, "Consignee", ctx["consignee"])
    draw_party(MARGIN_X + card_w + gap, "Notify", ctx["notify"])


def draw_commercial_strip(pdf: canvas.Canvas, ctx: dict) -> None:
    invoice = ctx["invoice"]
    y = 404
    h = 34
    gap = 10
    left_w = 178
    middle_w = 164
    right_w = CONTENT_W - left_w - middle_w - (gap * 2)

    cards = [
        (MARGIN_X, left_w, "Incoterm", invoice["incoterm"], GOLD_SOFT),
        (MARGIN_X + left_w + gap, middle_w, "Payment Terms", invoice["payment_terms"], PANEL_ALT),
        (MARGIN_X + left_w + middle_w + (gap * 2), right_w, "Packages", invoice["packages"], ACCENT_SOFT),
    ]

    for x, width, label, value, fill in cards:
        draw_card(pdf, x, y, width, h, fill_color=fill, stroke_color=BORDER, radius=14, line_width=0.9)
        pdf.setFillColor(INK_SOFT)
        pdf.setFont("Helvetica-Bold", 7.4)
        pdf.drawString(x + 12, y + h - 14, label.upper())
        draw_paragraph_fit(pdf, escaped(value), ["Value", "ValueTight"], x + 12, y + 14, width - 24, 14)


def build_items_table(ctx: dict) -> Table:
    invoice = ctx["invoice"]
    quantity_header = escaped(invoice["quantity_column_label"]).replace(" (", "<br/>(")
    rate_header = escaped(invoice["rate_column_label"]).replace(" Ton", "<br/>Ton")
    rows = [
        [
            Paragraph(escaped(invoice["sr_no_label"]), styles["TableHeader"]),
            Paragraph(escaped(invoice["description_column_label"]), styles["TableHeader"]),
            Paragraph(quantity_header, styles["TableHeader"]),
            Paragraph(rate_header, styles["TableHeader"]),
            Paragraph(escaped(invoice["amount_column_label"]), styles["TableHeader"]),
            Paragraph(escaped(invoice["igst_column_label"]), styles["TableHeader"]),
            Paragraph(escaped(invoice["total_column_label"]), styles["TableHeader"]),
        ]
    ]

    for item in ctx["items"]:
        description_lines = [item["product"], *item["description_lines"]]
        description_html = "<b>" + escaped(description_lines[0]) + "</b>"
        if len(description_lines) > 1:
            description_html += "<br/>" + "<br/>".join(escaped(line) for line in description_lines[1:])
        rows.append(
            [
                Paragraph(str(item["index"]), styles["TableCell"]),
                Paragraph(description_html, styles["TableCell"]),
                Paragraph(integerish(item["quantity"]), styles["TableCell"]),
                Paragraph(money(item["rate"]), styles["TableCell"]),
                Paragraph(money(item["amount"]), styles["TableCell"]),
                Paragraph(f"{integerish(item['igst_rate'])}%", styles["TableCell"]),
                Paragraph(money(item["total"]), styles["TableCell"]),
            ]
        )

    table = Table(rows, colWidths=[32, 182, 78, 72, 62, 40, 73], repeatRows=1)
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), HEADER_DARK),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 7.6),
            ("ALIGN", (0, 0), (0, -1), "CENTER"),
            ("ALIGN", (2, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("GRID", (0, 0), (-1, -1), 0.45, BORDER),
            ("LINEBELOW", (0, 0), (-1, 0), 1.0, GOLD),
        ]
    )
    for row_index in range(1, len(rows)):
        style.add("BACKGROUND", (0, row_index), (-1, row_index), WHITE if row_index % 2 else PANEL_ALT)
    table.setStyle(style)
    return table


def draw_items_section(pdf: canvas.Canvas, ctx: dict) -> None:
    section_top = 392
    max_section_height = 158
    table = build_items_table(ctx)
    _, table_h = table.wrap(CONTENT_W - 32, PAGE_HEIGHT)
    section_h = max(92, table_h + 34)
    if section_h > max_section_height:
        raise ValueError(
            f"Invoice has {len(ctx['items'])} items and exceeds this one-page template. "
            "Reduce item detail lines or extend the layout."
        )
    section_y = section_top - section_h
    draw_card(pdf, MARGIN_X, section_y, CONTENT_W, section_h, fill_color=PANEL, stroke_color=BORDER, radius=18)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 8.0)
    pdf.drawString(MARGIN_X + 16, section_y + section_h - 20, "ITEM DETAILS")
    table.drawOn(pdf, MARGIN_X + 16, section_y + 12)


def build_totals_table(ctx: dict) -> Table:
    rows = [
        [Paragraph(escaped(ctx["invoice"]["quantity_summary_label"]), styles["TotalsLabel"]), Paragraph(integerish(ctx["total_quantity"]), styles["TotalsValue"])],
        [Paragraph("Total Amount before Tax", styles["TotalsLabel"]), Paragraph(money(ctx["subtotal"]), styles["TotalsValue"])],
        [Paragraph("IGST", styles["TotalsLabel"]), Paragraph(money(ctx["total_igst"]), styles["TotalsValue"])],
        [Paragraph("Total Amount after Tax", styles["TotalsLabel"]), Paragraph(money(ctx["grand_total"]), styles["TotalsValue"])],
    ]
    table = Table(rows, colWidths=[168, 82])
    table.setStyle(
        TableStyle(
            [
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [WHITE, PANEL_ALT]),
                ("GRID", (0, 0), (-1, -1), 0.45, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return table


def build_bank_table(ctx: dict) -> Table:
    bank = ctx["bank"]
    rows = [
        [Paragraph("<b>Account Name</b>", styles["TableCellSmall"]), Paragraph(escaped(bank["account_name"]), styles["TableCell"])],
        [Paragraph("<b>Bank</b>", styles["TableCellSmall"]), Paragraph(escaped(bank["bank_name"]), styles["TableCell"])],
        [Paragraph("<b>Account Number</b>", styles["TableCellSmall"]), Paragraph(escaped(bank["account_number"]), styles["TableCell"])],
        [Paragraph("<b>IFSC</b>", styles["TableCellSmall"]), Paragraph(escaped(bank["ifsc"]), styles["TableCell"])],
        [Paragraph("<b>SWIFT</b>", styles["TableCellSmall"]), Paragraph(escaped(bank["swift"]), styles["TableCell"])],
        [Paragraph("<b>Bank Address</b>", styles["TableCellSmall"]), Paragraph(paragraph_html(bank["address"]), styles["TableCellSmall"])],
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


def draw_bottom_section(pdf: canvas.Canvas, ctx: dict) -> None:
    company = ctx["company"]
    invoice = ctx["invoice"]
    left_x = MARGIN_X
    right_x = MARGIN_X + 274
    bottom_y = 56
    words_y = bottom_y + 116
    words_h = 60

    draw_card(pdf, left_x, words_y, 260, words_h, fill_color=GOLD_SOFT, stroke_color=BORDER, radius=16)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 7.8)
    pdf.drawString(left_x + 14, words_y + words_h - 14, "TOTAL IN WORDS")
    draw_paragraph_fit(pdf, escaped(ctx["amount_words"]), ["Words", "ValueTight", "Small"], left_x + 14, words_y + words_h - 28, 232, 22)

    draw_card(pdf, left_x, bottom_y, 260, 100, fill_color=WHITE, stroke_color=BORDER, radius=16)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 8.0)
    pdf.drawString(left_x + 14, bottom_y + 83, "BANK DETAILS")
    bank_table = build_bank_table(ctx)
    bank_table.wrapOn(pdf, 232, 70)
    bank_table.drawOn(pdf, left_x + 14, bottom_y + 10)

    draw_card(pdf, right_x, bottom_y + 108, 260, 58, fill_color=WHITE, stroke_color=BORDER, radius=16)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 8.0)
    pdf.drawString(right_x + 14, bottom_y + 150, "TOTALS")
    totals_table = build_totals_table(ctx)
    totals_table.wrapOn(pdf, 232, 42)
    totals_table.drawOn(pdf, right_x + 14, bottom_y + 116)

    draw_card(pdf, right_x, bottom_y, 260, 98, fill_color=PANEL_ALT, stroke_color=BORDER, radius=16)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 8.0)
    pdf.drawString(right_x + 14, bottom_y + 79, "DECLARATION")
    draw_paragraph_fit(pdf, escaped(invoice["declaration"]), ["Small"], right_x + 14, bottom_y + 67, 136, 24)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 8.0)
    pdf.drawString(right_x + 14, bottom_y + 26, f"For {company['name']}")
    signature_path = company["signature_path"]
    if signature_path and signature_path.exists():
        pdf.drawImage(str(signature_path), right_x + 130, bottom_y + 16, width=102, height=42, mask="auto", preserveAspectRatio=True)
    pdf.setFillColor(INK_SOFT)
    pdf.setFont("Helvetica-Bold", 7.2)
    pdf.drawRightString(right_x + 244, bottom_y + 12, "Authorized Signatory")


def build_pdf(ctx: dict, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output_path), pagesize=A4)
    title = f"{ctx['company']['name']} - {ctx['invoice']['title']} {ctx['invoice']['number']}".strip()
    pdf.setTitle(title)
    pdf.setAuthor(ctx["company"]["name"])
    pdf.setSubject("Premium export invoice template")

    draw_header(pdf, ctx)
    draw_info_cards(pdf, ctx)
    draw_party_cards(pdf, ctx)
    draw_commercial_strip(pdf, ctx)
    draw_items_section(pdf, ctx)
    draw_bottom_section(pdf, ctx)
    pdf.save()


def render_preview(pdf_path: Path, preview_path: Path) -> None:
    preview_path.parent.mkdir(parents=True, exist_ok=True)
    with fitz.open(pdf_path) as document:
        page = document[0]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
        pix.save(preview_path)


def default_output_path(data_path: Path) -> Path:
    return DEFAULT_OUTPUT_DIR / f"{data_path.stem}.pdf"


def default_preview_path(data_path: Path) -> Path:
    return DEFAULT_PREVIEW_DIR / f"{data_path.stem}-preview.png"


def generate_invoice(data_path: Path, output_path: Path | None = None, preview_path: Path | None = None) -> tuple[Path, Path]:
    data = json.loads(data_path.read_text())
    ctx = build_context(data, data_path)
    final_output = output_path or default_output_path(data_path)
    final_preview = preview_path or default_preview_path(data_path)
    build_pdf(ctx, final_output)
    render_preview(final_output, final_preview)
    return final_output, final_preview


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a premium export invoice PDF from a JSON file.")
    parser.add_argument("data_file", help="Path to the invoice JSON file.")
    parser.add_argument("--output", help="Optional PDF output path.")
    parser.add_argument("--preview", help="Optional preview PNG path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data_path = Path(args.data_file).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve() if args.output else None
    preview_path = Path(args.preview).expanduser().resolve() if args.preview else None
    pdf_path, png_path = generate_invoice(data_path, output_path, preview_path)
    print(f"PDF: {pdf_path}")
    print(f"Preview: {png_path}")


if __name__ == "__main__":
    main()
