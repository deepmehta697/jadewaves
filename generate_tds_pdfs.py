from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "assets" / "tds"
LOGO = ROOT / "assets" / "jade-waves-logo-transparent.png"


PRODUCTS = {
    "quartz-sand-technical-data-sheet.pdf": {
        "title": "Quartz Sand Technical Data Sheet",
        "subtitle": "Quartz sand, grits, and powder for ceramics, glass, construction, and related process use.",
        "summary": [
            ("Forms", "Quartz Sand / Quartz Grits / Quartz Powder"),
            ("Packing", "Jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Sizes", "0.1-0.4 mm / 0.3-0.7 mm / 0.6-1.2 mm / 1.2-2.5 mm / 2.5-4.0 mm / 4.0-6.0 mm / 200 / 325 / 400 Mesh"),
        ],
        "technical": [
            "SiO2 content aligned to the selected end use and size range.",
            "L value reported at 91 min.",
            "Humidity reported at 0.3% max.",
            "Particle distribution aligned to the selected size range.",
            "Size in range reported above 90%.",
        ],
        "application": "Ceramics, glass, construction, and engineered stone where whiteness, particle range, and shipment consistency matter.",
    },
    "feldspar-technical-data-sheet.pdf": {
        "title": "Feldspar Technical Data Sheet",
        "subtitle": "Potassium feldspar and sodium feldspar supplied in lump and powder forms for ceramic, sanitaryware, glass, and engineered stone buyers.",
        "summary": [
            ("Forms", "Lumps and powder"),
            ("Packing", "Jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Sizes", "100 / 200 / 325 / 350 Mesh"),
        ],
        "technical": [
            "Potassium feldspar grades run up to 12% K2O.",
            "Sodium feldspar grades run up to 10% Na2O.",
            "Fe2O3 ranges from 0.06% to 0.15% depending on grade.",
            "Firing outputs cover milky white, off white, and super white results.",
        ],
        "application": "Ceramics, sanitaryware, glass, and engineered stone where potassium or sodium contribution must stay aligned to firing behavior.",
    },
    "silica-sand-technical-data-sheet.pdf": {
        "title": "Silica Sand Technical Data Sheet",
        "subtitle": "Silica sand supplied in grits and powder forms for glass, foundry, filtration, turf, and construction buyers.",
        "summary": [
            ("Forms", "Grits and powder"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Application fit", "Glass / foundry / construction / water treatment / turf"),
        ],
        "technical": [
            "SiO2 aligned to 98-99%.",
            "K2O reported below 0.01%.",
            "Moisture reported below 0.10%.",
            "Glass-oriented supply can be aligned to 150-200 PPM Fe2O3 where required.",
            "Selected grain size is aligned to the application and packing basis.",
        ],
        "application": "Glass manufacturing, water filtration media, foundry moulding systems, turf infill, and other industrial uses where grain range and chemistry clarity matter.",
    },
    "bentonite-technical-data-sheet.pdf": {
        "title": "Bentonite Technical Data Sheet",
        "subtitle": "Bentonite grades supplied in lump and powder form for drilling, piling, HDD, foundry, sealing, earthing, absorbent, and coating use.",
        "summary": [
            ("Forms", "Lumps and powder"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Grade direction", "Sodium / calcium / application-specific bentonite"),
        ],
        "technical": [
            "Moisture specified at 14% max.",
            "Liquid limit specified at 450 min.",
            "Gel index specified at 60 min.",
            "Marsh funnel viscosity specified at 50 sec min.",
            "Grade is aligned to application, swelling direction, and handling basis before quote.",
        ],
        "application": "Oil drilling, piling, HDD, foundry, earthing, pond sealing, cat litter, and paint systems where viscosity or swell response matters.",
    },
    "salt-technical-data-sheet.pdf": {
        "title": "Salt Technical Data Sheet",
        "subtitle": "Industrial, pool, iodized, de-icing, and raw salt grades supplied for utility, treatment, processing, and consumption-linked demand.",
        "summary": [
            ("Forms", "Crystal"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Grades", "Industrial / Pool / Triple Refined Iodized / De-icing / Raw / Iodized"),
        ],
        "technical": [
            "NaCl reported at 99.00% min.",
            "Moisture reported at 0.2% max.",
            "Consumption salt typically carries 25-30 PPM iodine and can be customized.",
            "Iodine is NIL for grades supplied outside consumption use.",
            "Grain size and packing are aligned to the selected salt grade.",
        ],
        "application": "Chemicals, water treatment, infrastructure, food processing, and related programs where purity and grain consistency matter.",
    },
}


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="DocTitle",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            textColor=colors.HexColor("#16263d"),
            alignment=TA_LEFT,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="DocMeta",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=16,
            textColor=colors.HexColor("#5f6f82"),
            spaceAfter=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionLabel",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#74839a"),
            alignment=TA_LEFT,
            spaceAfter=6,
            uppercase=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCopy",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=16,
            textColor=colors.HexColor("#29384d"),
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallRight",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#74839a"),
            alignment=TA_RIGHT,
        )
    )
    return styles


def summary_table(rows):
    body = []
    for key, value in rows:
        body.append(
            [
                Paragraph(f"<b>{key}</b>", STYLES["BodyCopy"]),
                Paragraph(value, STYLES["BodyCopy"]),
            ]
        )

    table = Table(body, colWidths=[42 * mm, 124 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#d7dfeb")),
                ("INNERGRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#d7dfeb")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]
        )
    )
    return table


def build_story(product):
    story = []

    logo = Image(str(LOGO), width=48 * mm, height=19 * mm)
    header = Table(
        [
            [
                logo,
                Paragraph("Manufacturer & Exporter of Minerals", STYLES["SmallRight"]),
            ]
        ],
        colWidths=[88 * mm, 92 * mm],
    )
    header.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    story.extend([header, Spacer(1, 8)])

    story.append(Paragraph(product["title"], STYLES["DocTitle"]))
    story.append(Paragraph(product["subtitle"], STYLES["DocMeta"]))

    story.append(Paragraph("Commercial Summary", STYLES["SectionLabel"]))
    story.append(summary_table(product["summary"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Technical Focus", STYLES["SectionLabel"]))
    for line in product["technical"]:
        story.append(Paragraph(f"- {line}", STYLES["BodyCopy"]))

    story.append(Spacer(1, 4))
    story.append(Paragraph("End Use", STYLES["SectionLabel"]))
    story.append(Paragraph(product["application"], STYLES["BodyCopy"]))

    story.append(Spacer(1, 8))
    note = (
        "Published values on this sheet reflect the current website product positioning and are aligned again against the selected grade, "
        "mesh size, packing basis, and shipment requirement before final order confirmation."
    )
    story.append(Paragraph("Buyer Note", STYLES["SectionLabel"]))
    story.append(Paragraph(note, STYLES["BodyCopy"]))

    footer = Table(
        [[Paragraph("Jade Waves Enterprise | deep@jadewavesenterprise.com | +91-999-883-5503", STYLES["SmallRight"])]],
        colWidths=[180 * mm],
    )
    footer.setStyle(TableStyle([("TOPPADDING", (0, 0), (-1, -1), 14)]))
    story.extend([Spacer(1, 8), footer])
    return story


def build_pdf(name, product):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / name
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
    )
    doc.build(build_story(product))
    return path


if __name__ == "__main__":
    STYLES = build_styles()
    for filename, product in PRODUCTS.items():
        build_pdf(filename, product)
        print(filename)
