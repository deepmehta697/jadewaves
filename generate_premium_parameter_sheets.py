from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Image, LongTable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUTPUT_DIR = ASSETS / "grade-sheets"
LOGO = ASSETS / "jade-waves-logo-transparent.png"

PAGE_SIZE = landscape(A4)
PAGE_WIDTH, PAGE_HEIGHT = PAGE_SIZE
MARGIN_X = 16 * mm
MARGIN_Y = 14 * mm

INK = colors.HexColor("#1C2733")
INK_SOFT = colors.HexColor("#5A6878")
ACCENT = colors.HexColor("#0B71B7")
ACCENT_DARK = colors.HexColor("#123A5B")
ACCENT_SOFT = colors.HexColor("#EEF6FC")
BORDER = colors.HexColor("#D8E3EE")
PANEL = colors.white
PANEL_ALT = colors.HexColor("#F7FAFD")
PAGE_BG = colors.HexColor("#F4F7FA")
SUCCESS = colors.HexColor("#2F6F67")
SUCCESS_SOFT = colors.HexColor("#EDF6F4")


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="Kicker",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=8.2,
        leading=9.5,
        textColor=ACCENT,
        alignment=TA_LEFT,
        spaceAfter=0,
        uppercase=True,
        tracking=1.2,
    )
)
styles.add(
    ParagraphStyle(
        name="DocTitle",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=24,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="DocSub",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.8,
        leading=13.2,
        textColor=INK_SOFT,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Cell",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.6,
        leading=10.5,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="CellCenter",
        parent=styles["Cell"],
        alignment=TA_CENTER,
    )
)
styles.add(
    ParagraphStyle(
        name="MetricLabel",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=7.1,
        leading=8.8,
        textColor=ACCENT,
        alignment=TA_LEFT,
        spaceAfter=0,
        uppercase=True,
        tracking=1.1,
    )
)
styles.add(
    ParagraphStyle(
        name="MetricValue",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=12.8,
        leading=14.6,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="SectionTitle",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=10.4,
        leading=12.4,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="Footnote",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.8,
        leading=10,
        textColor=INK_SOFT,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="TopRight",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.1,
        leading=10.4,
        textColor=INK_SOFT,
        alignment=TA_RIGHT,
        spaceAfter=0,
    )
)


DOCS = [
    {
        "filename": "quartz-grits-q1-parameter-sheet.pdf",
        "title": "Quartz Grits Q1",
        "subtitle": "",
        "metrics": [
            ("Silica", "SiO<sub>2</sub> &gt; 99.0%"),
            ("Color", "L 91 min"),
            ("Humidity", "Max 0.3%"),
        ],
        "sections": [
            {
                "title": "Chemical Parameters",
                "headers": ["Parameter", "Result"],
                "widths": [120 * mm, 116 * mm],
                "rows": [
                    ("SiO<sub>2</sub>", "&gt; 99.0%"),
                    ("Na<sub>2</sub>O", "0.05% max"),
                    ("CaO", "0.03% max"),
                    ("Fe<sub>2</sub>O<sub>3</sub>", "0.06% max"),
                    ("K<sub>2</sub>O", "0.02% max"),
                    ("TiO<sub>2</sub>", "0.04% max"),
                    ("Al<sub>2</sub>O<sub>3</sub>", "0.1% max"),
                    ("L.O.I", "0.1 max"),
                ],
            },
            {
                "title": "Physical Parameters",
                "headers": ["Parameter", "Result"],
                "widths": [120 * mm, 116 * mm],
                "rows": [
                    ("Color L", "91 min"),
                    ("Color a", "1.0 max"),
                    ("Color b", "2.5 max"),
                    ("Particle size distribution", "Size in range &gt; 90%; upper size &lt; 5%; lower size &lt; 5%"),
                    ("Black particles / 100 g", "5"),
                    ("Other color particles / 100 g", "5"),
                    ("Humidity", "Max 0.3%"),
                ],
            },
            {
                "title": "Available Size Ranges",
                "headers": ["Size Range", "Availability"],
                "widths": [120 * mm, 116 * mm],
                "rows": [
                    ("0.1-0.4 mm", "Available"),
                    ("0.3-0.7 mm", "Available"),
                    ("0.6-1.2 mm", "Available"),
                    ("1.2-2.5 mm", "Available"),
                    ("2.5-4.0 mm", "Available"),
                    ("4.0-6.0 mm", "Available"),
                    ("Custom sizing available", "Available"),
                ],
            },
        ],
        "reference": [
            ("Forms", "Quartz grits"),
            ("Packing", "Jumbo bags"),
            ("Typical use", "Ceramics, glass manufacturing, engineered stone, and mineral systems"),
            ("HSN code", "25061020"),
        ],
        "note": "",
    },
    {
        "filename": "quartz-grits-q2-parameter-sheet.pdf",
        "title": "Quartz Grits Q2",
        "subtitle": "",
        "metrics": [
            ("Silica", "SiO<sub>2</sub> &gt; 99.0%"),
            ("Color", "L 90 min"),
            ("Humidity", "Max 0.3%"),
        ],
        "sections": [
            {
                "title": "Chemical Parameters",
                "headers": ["Parameter", "Result"],
                "widths": [120 * mm, 116 * mm],
                "rows": [
                    ("SiO<sub>2</sub>", "&gt; 99.0%"),
                    ("Na<sub>2</sub>O", "0.05% max"),
                    ("CaO", "0.03% max"),
                    ("Fe<sub>2</sub>O<sub>3</sub>", "0.06% max"),
                    ("K<sub>2</sub>O", "0.02% max"),
                    ("TiO<sub>2</sub>", "0.04% max"),
                    ("Al<sub>2</sub>O<sub>3</sub>", "0.1% max"),
                    ("L.O.I", "0.1 max"),
                ],
            },
            {
                "title": "Physical Parameters",
                "headers": ["Parameter", "Result"],
                "widths": [120 * mm, 116 * mm],
                "rows": [
                    ("Color L", "90 min"),
                    ("Color a", "2.0 max"),
                    ("Color b", "3.5 max"),
                    ("Particle size distribution", "Size in range &gt; 90%; upper size &lt; 5%; lower size &lt; 5%"),
                    ("Black particles / 100 g", "15"),
                    ("Other color particles / 100 g", "15"),
                    ("Humidity", "Max 0.3%"),
                ],
            },
            {
                "title": "Available Size Ranges",
                "headers": ["Size Range", "Availability"],
                "widths": [120 * mm, 116 * mm],
                "rows": [
                    ("0.1-0.4 mm", "Available"),
                    ("0.3-0.7 mm", "Available"),
                    ("0.6-1.2 mm", "Available"),
                    ("1.2-2.5 mm", "Available"),
                    ("2.5-4.0 mm", "Available"),
                    ("4.0-6.0 mm", "Available"),
                    ("Custom sizing available", "Available"),
                ],
            },
        ],
        "reference": [
            ("Forms", "Quartz grits"),
            ("Packing", "Jumbo bags"),
            ("Typical use", "Ceramics, glass manufacturing, engineered stone, and mineral systems"),
            ("HSN code", "25061020"),
        ],
        "note": "",
    },
    {
        "filename": "quartz-powder-c-parameter-sheet.pdf",
        "title": "Quartz Powder",
        "subtitle": "",
        "metrics": [
            ("Silica", "SiO<sub>2</sub> &gt; 99.0%"),
            ("Residue", "&lt; 1%"),
            ("Mesh", "200 / 325 / 400"),
        ],
        "sections": [
            {
                "title": "Chemical Parameters",
                "headers": ["Parameter", "Result"],
                "widths": [120 * mm, 116 * mm],
                "rows": [
                    ("SiO<sub>2</sub>", "&gt; 99.0%"),
                    ("Na<sub>2</sub>O", "0.05% max"),
                    ("CaO", "0.03% max"),
                    ("Fe<sub>2</sub>O<sub>3</sub>", "0.06% max"),
                    ("K<sub>2</sub>O", "0.02% max"),
                    ("TiO<sub>2</sub>", "0.04% max"),
                    ("Al<sub>2</sub>O<sub>3</sub>", "0.1% max"),
                    ("L.O.I", "0.1 max"),
                ],
            },
            {
                "title": "Color Profile",
                "headers": ["Metric", "Q1", "Q2"],
                "widths": [78 * mm, 79 * mm, 79 * mm],
                "rows": [
                    ("L", "91 min", "89 min"),
                    ("a", "1.0 max", "2.0 max"),
                    ("b", "2.5 max", "3.5 max"),
                ],
            },
            {
                "title": "Physical Parameters",
                "headers": ["Parameter", "Result"],
                "widths": [120 * mm, 116 * mm],
                "rows": [
                    ("Particle size distribution", "Residue &lt; 1%"),
                    ("Humidity", "Max 0.3%"),
                    ("Available mesh", "200 mesh BSS (75 microns) / 325 mesh BSS (45 microns) / 400 mesh BSS (38 microns)"),
                    ("Custom sizing available", "Available"),
                ],
            },
        ],
        "reference": [],
        "note": "",
    },
    {
        "filename": "soda-feldspar-parameter-sheet.pdf",
        "title": "Soda/Sodium Feldspar",
        "subtitle": "",
        "metrics": [
            ("S1 Grade", "Na<sub>2</sub>O 10% (±1%)"),
            ("S2 Grade", "Na<sub>2</sub>O 8% (±1%)"),
            ("Firing", "Milky white / off white"),
        ],
        "sections": [
            {
                "title": "Grade Matrix",
                "headers": ["Parameter", "S1", "S2"],
                "widths": [86 * mm, 75 * mm, 75 * mm],
                "rows": [
                    ("Grade", "First", "Second"),
                    ("SiO<sub>2</sub>", "68% (± 1%)", "72% (± 2%)"),
                    ("AL<sub>2</sub>O<sub>3</sub>", "18% (± 1%)", "17% (± 1%)"),
                    ("K<sub>2</sub>O", "0.50% (± 0.5%)", "2% (± 1%)"),
                    ("Na<sub>2</sub>O", "10% (± 1%)", "8% (± 1%)"),
                    ("Fe<sub>2</sub>O<sub>3</sub>", "0.10% (± 0.03%)", "0.15% (± 0.05%)"),
                    ("MgO", "0.1% (± 0.1%)", "0.02% (± 0.1%)"),
                    ("CaO", "0.05% (± 0.5%)", "0.2% (± 0.1%)"),
                    ("TiO<sub>2</sub>", "NIL", "NIL"),
                    ("LOI", "0.10%", "0.20%"),
                    ("Firing result 1175°C-1220°C", "Milky White", "Off white"),
                    ("Firing appearance", "White to Cream", "Pink to Cream"),
                ],
            },
            {
                "title": "Available Sizes",
                "headers": ["Size", "Availability"],
                "widths": [120 * mm, 116 * mm],
                "rows": [
                    ("100 Mesh", "Available"),
                    ("200 Mesh", "Available"),
                    ("325 Mesh", "Available"),
                    ("350 Mesh", "Available"),
                    ("Custom sizing available", "Available"),
                ],
            },
        ],
        "reference": [
            ("Forms", "Lumps and powder"),
            ("Packing", "Jumbo bags"),
            ("Typical use", "Ceramics, sanitaryware, glass, and flux-driven mineral systems"),
            ("HSN code", "25291020"),
        ],
        "note": "",
    },
    {
        "filename": "potash-feldspar-parameter-sheet.pdf",
        "title": "Potash/Potassium Feldspar",
        "subtitle": "",
        "metrics": [
            ("Potash", "K<sub>2</sub>O up to 12%"),
            ("Firing", "Milky white / super white"),
        ],
        "sections": [
            {
                "title": "Grade Matrix",
                "headers": ["Parameter", "P1", "P2", "P White"],
                "widths": [70 * mm, 52 * mm, 52 * mm, 62 * mm],
                "rows": [
                    ("Grade", "First", "Second", "First"),
                    ("SiO<sub>2</sub>", "66% (± 1%)", "68% (± 1%)", "69%"),
                    ("AL<sub>2</sub>O<sub>3</sub>", "18% (± 0.5%)", "17% (± 0.5%)", "16.5%"),
                    ("K<sub>2</sub>O", "12% (± 1%)", "10% (± 1%)", "10%"),
                    ("Na<sub>2</sub>O", "2.5% (± 0.5%)", "3% (± 1%)", "3%"),
                    ("Fe<sub>2</sub>O<sub>3</sub>", "0.06% (± 0.1%)", "0.08% (± 0.2%)", "0.07%"),
                    ("MgO", "NIL", "NIL", "NIL"),
                    ("CaO", "NIL", "NIL", "NIL"),
                    ("TiO<sub>2</sub>", "NIL", "NIL", "NIL"),
                    ("LOI", "0.10%", "0.20%", "0.25%"),
                    ("Firing result 1175°C-1220°C", "Milky White", "Off white", "Super White"),
                    ("Firing appearance", "White to Pink", "Pink to White", "White to White"),
                ],
            },
            {
                "title": "Available Sizes",
                "headers": ["Size", "Availability"],
                "widths": [120 * mm, 116 * mm],
                "rows": [
                    ("100 Mesh", "Available"),
                    ("200 Mesh", "Available"),
                    ("325 Mesh", "Available"),
                    ("350 Mesh", "Available"),
                    ("Custom sizing available", "Available"),
                ],
            },
        ],
        "reference": [
            ("Forms", "Lumps and powder"),
            ("Packing", "Jumbo bags"),
            ("Typical use", "Ceramics, sanitaryware, glass, and engineered stone systems"),
            ("HSN code", "25291020"),
        ],
        "note": "",
    },
]


def draw_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PAGE_BG)
    canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    inset_x = 8 * mm
    inset_y = 7 * mm
    canvas.setFillColor(PANEL)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(1)
    canvas.roundRect(
        inset_x,
        inset_y,
        PAGE_WIDTH - (inset_x * 2),
        PAGE_HEIGHT - (inset_y * 2),
        18,
        fill=1,
        stroke=1,
    )

    canvas.setFillColor(ACCENT_DARK)
    canvas.roundRect(
        inset_x,
        PAGE_HEIGHT - 34 * mm,
        PAGE_WIDTH - (inset_x * 2),
        27 * mm,
        18,
        fill=1,
        stroke=0,
    )

    canvas.setFillColor(ACCENT)
    canvas.roundRect(MARGIN_X, PAGE_HEIGHT - 17 * mm, 34 * mm, 1.8 * mm, 0.8 * mm, fill=1, stroke=0)

    if LOGO.exists():
        logo_card_w = 34 * mm
        logo_card_h = 18 * mm
        logo_card_x = PAGE_WIDTH - MARGIN_X - logo_card_w
        logo_card_y = PAGE_HEIGHT - 28 * mm
        canvas.setFillColor(colors.white)
        canvas.setStrokeColor(BORDER)
        canvas.setLineWidth(0.7)
        canvas.roundRect(logo_card_x, logo_card_y, logo_card_w, logo_card_h, 8, fill=1, stroke=1)
        canvas.drawImage(
            str(LOGO),
            logo_card_x + 5 * mm,
            logo_card_y + 3 * mm,
            width=24 * mm,
            height=12 * mm,
            preserveAspectRatio=True,
            mask="auto",
        )

    canvas.setFillColor(INK_SOFT)
    canvas.setFont("Helvetica", 7.6)
    canvas.drawString(MARGIN_X, 8 * mm, "Jade Waves Enterprise | Technical Reference Sheet")
    canvas.drawRightString(PAGE_WIDTH - MARGIN_X, 8 * mm, "deep@jadewavesenterprise.com | +91-999-883-5503")
    canvas.restoreState()


def para(text: str, style_name: str = "Cell") -> Paragraph:
    return Paragraph(text, styles[style_name])


def metric_cards(metrics):
    card_width = (228 * mm) / max(len(metrics), 1)
    cells = []
    for label, value in metrics:
        inner = Table(
            [[para(label, "MetricLabel")], [para(value, "MetricValue")]],
            colWidths=[card_width - (2 * mm)],
        )
        inner.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), PANEL_ALT),
                    ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                    ("LEFTPADDING", (0, 0), (-1, -1), 10),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ]
            )
        )
        cells.append(inner)
    table = Table([cells], colWidths=[card_width] * len(cells))
    table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return table


def data_table(headers, rows, widths):
    table_rows = [[para(cell, "Cell") for cell in headers]]
    for row in rows:
        table_rows.append([para(cell, "Cell") for cell in row])

    table = LongTable(table_rows, colWidths=widths, repeatRows=1)
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (1, 1), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
            ("INNERGRID", (0, 0), (-1, -1), 0.55, BORDER),
        ]
    )
    for idx in range(1, len(table_rows)):
        style.add("BACKGROUND", (0, idx), (-1, idx), PANEL if idx % 2 else PANEL_ALT)
    table.setStyle(style)
    return table


def reference_table(rows):
    data = []
    for label, value in rows:
        data.append([para(f"<b>{label}</b>", "Cell"), para(value, "Cell")])
    table = Table(data, colWidths=[54 * mm, 182 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), SUCCESS_SOFT),
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [SUCCESS_SOFT, PANEL]),
                ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.55, BORDER),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return table


def build_pdf(spec):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / spec["filename"]
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=PAGE_SIZE,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=39 * mm,
        bottomMargin=18 * mm,
    )

    story = [
        para("Parameter Sheet", "Kicker"),
        Spacer(1, 3 * mm),
        para(spec["title"], "DocTitle"),
    ]
    if spec.get("subtitle"):
        story.extend([Spacer(1, 2 * mm), para(spec["subtitle"], "DocSub"), Spacer(1, 7 * mm)])
    else:
        story.append(Spacer(1, 6 * mm))
    story.extend([metric_cards(spec["metrics"]), Spacer(1, 6 * mm)])

    for section in spec["sections"]:
        story.append(para(section["title"], "SectionTitle"))
        story.append(Spacer(1, 2.5 * mm))
        story.append(data_table(section["headers"], section["rows"], section["widths"]))
        story.append(Spacer(1, 5 * mm))

    if spec.get("reference"):
        story.append(para("Supply Reference", "SectionTitle"))
        story.append(Spacer(1, 2.5 * mm))
        story.append(reference_table(spec["reference"]))
    if spec.get("note"):
        story.append(Spacer(1, 4 * mm))
        story.append(para(spec["note"], "Footnote"))

    doc.build(story, onFirstPage=draw_page, onLaterPages=draw_page)
    return output_path


def main():
    for spec in DOCS:
        path = build_pdf(spec)
        print(f"Created {path}")


if __name__ == "__main__":
    main()
