from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parent
ASSETS_DIR = ROOT / "assets"
TDS_DIR = ASSETS_DIR / "tds"
COA_DIR = ASSETS_DIR / "coas"
LOGO = ASSETS_DIR / "jade-waves-logo-transparent.png"


PRODUCTS = [
    {
        "slug": "silica-sand",
        "name": "Silica Sand",
        "tds_file": "silica-sand-technical-data-sheet.pdf",
        "coa_file": "silica-sand-sample-coa.pdf",
        "subtitle": "Silica sand supplied in grits and powder forms for glass, foundry, filtration, turf, and construction buyers.",
        "summary": [
            ("Forms", "Grits and powder"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Applications", "Glass / foundry / filtration / turf / construction"),
        ],
        "technical": [
            "SiO2 aligned to 98-99%.",
            "Fe2O3 for glass manufacturing can be aligned to 150-200 PPM where required.",
            "Moisture reported below 0.10% on the website reference range.",
            "Selected grain size is aligned to the end use and packing basis.",
        ],
        "application": "Used in glass manufacturing, water filtration media, foundry moulding systems, turf infill, and related mineral demand.",
        "coa": [
            ("Appearance", "Off-white silica grains"),
            ("SiO2", "98-99%"),
            ("Fe2O3", "150-200 PPM for glass-oriented demand"),
            ("Moisture", "Below 0.10%"),
            ("Packing basis", "50 Kg bags / jumbo bags"),
        ],
    },
    {
        "slug": "silica-flour",
        "name": "Silica Flour",
        "tds_file": "silica-flour-technical-data-sheet.pdf",
        "coa_file": "silica-flour-sample-coa.pdf",
        "subtitle": "Silica flour supplied in powder form for ceramic, coating, filler, and process use where mesh and whiteness matter.",
        "summary": [
            ("Forms", "Powder"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Grades", "80 Mesh / 300 Mesh / 500 Mesh"),
        ],
        "technical": [
            "Mesh is aligned to the selected process and dispersion requirement.",
            "Brightness and powder profile are checked against the approved grade.",
            "Packing basis is fixed before dispatch planning begins.",
        ],
        "application": "Used in ceramic bodies, coatings, fillers, and mineral process demand where powder size and consistency matter.",
        "coa": [
            ("Appearance", "White mineral powder"),
            ("Form", "Powder"),
            ("Mesh", "80 / 300 / 500 Mesh options"),
            ("Moisture", "Aligned to grade"),
            ("Packing basis", "50 Kg bags / jumbo bags"),
        ],
    },
    {
        "slug": "quartz-sand",
        "name": "Quartz Sand",
        "tds_file": "quartz-sand-technical-data-sheet.pdf",
        "coa_file": "quartz-sand-sample-coa.pdf",
        "subtitle": "Quartz sand, grits, and powder for ceramics, glass, construction, and related process use.",
        "summary": [
            ("Forms", "Quartz Sand / Quartz Grits / Quartz Powder"),
            ("Packing", "Jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Sizes", "0.1-0.4 / 0.3-0.7 / 0.6-1.2 / 1.2-2.5 / 2.5-4.0 / 4.0-6.0 mm / 200 / 325 / 400 Mesh"),
        ],
        "technical": [
            "SiO2 content is aligned to the selected end use and size range.",
            "L value is reported at 91 min on the current website reference range.",
            "Humidity is reported at 0.3% max on the reference sheet.",
            "Particle distribution stays aligned to the selected size range.",
        ],
        "application": "Used in ceramics, glass, construction, and engineered stone where whiteness and size consistency matter.",
        "coa": [
            ("Appearance", "White to milky white quartz grains"),
            ("SiO2", "Aligned to approved grade"),
            ("L value", "91 min"),
            ("Humidity", "0.3% max"),
            ("Packing basis", "Jumbo bags"),
        ],
    },
    {
        "slug": "bentonite",
        "name": "Bentonite",
        "tds_file": "bentonite-technical-data-sheet.pdf",
        "coa_file": "bentonite-sample-coa.pdf",
        "subtitle": "Bentonite grades supplied in lump and powder form for drilling, piling, HDD, foundry, sealing, earthing, absorbent, and coating use.",
        "summary": [
            ("Forms", "Lumps and powder"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Grade direction", "Sodium / calcium / application-specific bentonite"),
        ],
        "technical": [
            "Moisture specified at 14% max on the reference sheet.",
            "Liquid limit specified at 450 min.",
            "Gel index specified at 60 min.",
            "Marsh funnel viscosity specified at 50 sec min.",
        ],
        "application": "Used across drilling, piling, HDD, foundry, earthing, pond sealing, absorbent, and coating systems.",
        "coa": [
            ("Appearance", "Brown mineral powder / lumps"),
            ("Moisture", "14% max"),
            ("Liquid limit", "450 min"),
            ("Gel index", "60 min"),
            ("Packing basis", "50 Kg bags / jumbo bags"),
        ],
    },
    {
        "slug": "china-clay",
        "name": "China Clay",
        "tds_file": "china-clay-technical-data-sheet.pdf",
        "coa_file": "china-clay-sample-coa.pdf",
        "subtitle": "China clay supplied in lump and powder form for ceramic, filler, coating, and mineral processing use.",
        "summary": [
            ("Forms", "Lumps and powder"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Color", "White"),
        ],
        "technical": [
            "Whiteness and particle profile are aligned to the selected end use.",
            "Packing basis is fixed before dispatch planning.",
            "Reference values are aligned again against the selected grade before order confirmation.",
        ],
        "application": "Used in ceramics, fillers, coatings, and related industrial mineral demand where whiteness and powder behavior matter.",
        "coa": [
            ("Appearance", "White clay powder / lumps"),
            ("Color", "White"),
            ("Form", "Lumps / powder"),
            ("Packing basis", "50 Kg bags / jumbo bags"),
            ("Reference", "Sample reference only"),
        ],
    },
    {
        "slug": "talc",
        "name": "Talc",
        "tds_file": "talc-technical-data-sheet.pdf",
        "coa_file": "talc-sample-coa.pdf",
        "subtitle": "Talc supplied in powder, chips, and lump form for filler, coating, ceramic, and process use.",
        "summary": [
            ("Forms", "Powder / chips / lumps"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Brightness", "90%"),
        ],
        "technical": [
            "Brightness is aligned to the selected talc grade.",
            "Particle profile is matched to the selected end use.",
            "Packing basis is fixed before cargo planning starts.",
        ],
        "application": "Used in fillers, coatings, ceramics, and mineral process demand where brightness and softness profile matter.",
        "coa": [
            ("Appearance", "White talc powder / chips / lumps"),
            ("Brightness", "90%"),
            ("Form", "Powder / chips / lumps"),
            ("Packing basis", "50 Kg bags / jumbo bags"),
            ("Reference", "Sample reference only"),
        ],
    },
    {
        "slug": "feldspar",
        "name": "Feldspar",
        "tds_file": "feldspar-technical-data-sheet.pdf",
        "coa_file": "feldspar-sample-coa.pdf",
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
        "application": "Used in ceramics, sanitaryware, glass, and engineered stone where potassium or sodium contribution must stay aligned to firing behavior.",
        "coa": [
            ("Appearance", "Off white to light pink mineral lumps / powder"),
            ("Potassium / sodium", "Aligned to approved grade"),
            ("Fe2O3", "Aligned to approved grade"),
            ("Mesh", "100 / 200 / 325 / 350 Mesh"),
            ("Packing basis", "Jumbo bags"),
        ],
    },
    {
        "slug": "salt",
        "name": "Salt",
        "tds_file": "salt-technical-data-sheet.pdf",
        "coa_file": "salt-sample-coa.pdf",
        "subtitle": "Industrial, pool, iodized, de-icing, and raw salt grades supplied for utility, treatment, processing, and consumption-linked demand.",
        "summary": [
            ("Forms", "Crystal"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Grades", "Industrial / Pool / Triple Refined Iodized / De-icing / Raw / Iodized"),
        ],
        "technical": [
            "NaCl reported at 99.00% min on the website reference grade.",
            "Moisture reported at 0.2% max.",
            "Consumption salt typically carries 25-30 PPM iodine and can be customized.",
            "Iodine is NIL for grades supplied outside consumption use.",
        ],
        "application": "Used in chemicals, water treatment, infrastructure, food processing, and related demand where purity and grain consistency matter.",
        "coa": [
            ("Appearance", "White salt crystals"),
            ("NaCl", "99.00% min"),
            ("Moisture", "0.2% max"),
            ("Iodine", "Aligned to selected salt grade"),
            ("Packing basis", "50 Kg bags / jumbo bags"),
        ],
    },
    {
        "slug": "fly-ash",
        "name": "Fly Ash",
        "tds_file": "fly-ash-technical-data-sheet.pdf",
        "coa_file": "fly-ash-sample-coa.pdf",
        "subtitle": "Fly ash supplied in powder form for concrete, blocks, cement blending, and related mineral filler demand.",
        "summary": [
            ("Forms", "Powder"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Color", "Beige"),
        ],
        "technical": [
            "Powder profile is aligned to the selected concrete or blending use.",
            "Packing basis is fixed before cargo planning begins.",
            "Reference values are aligned again against the approved supply basis.",
        ],
        "application": "Used in concrete, blocks, cement blending, and related filler demand where powder consistency matters.",
        "coa": [
            ("Appearance", "Beige powder"),
            ("Form", "Powder"),
            ("Packing basis", "50 Kg bags / jumbo bags"),
            ("Reference", "Sample reference only"),
            ("Use", "Concrete / blocks / cement blending"),
        ],
    },
    {
        "slug": "copper-slag",
        "name": "Copper Slag",
        "tds_file": "copper-slag-technical-data-sheet.pdf",
        "coa_file": "copper-slag-sample-coa.pdf",
        "subtitle": "Copper slag supplied for abrasive blasting, surface preparation, and related industrial use.",
        "summary": [
            ("Forms", "Granular"),
            ("Packing", "50 Kg bags / jumbo bags"),
            ("Shipment basis", "FCL with FOB / CIF / CNF options"),
            ("Color", "Black"),
        ],
        "technical": [
            "Grain profile is aligned to the selected blasting or surface-preparation use.",
            "Packing basis is fixed before dispatch planning starts.",
            "Reference values are aligned against the approved grade before final order confirmation.",
        ],
        "application": "Used in abrasive blasting and related industrial demand where grain profile and movement basis matter.",
        "coa": [
            ("Appearance", "Black granular slag"),
            ("Form", "Granular"),
            ("Packing basis", "50 Kg bags / jumbo bags"),
            ("Reference", "Sample reference only"),
            ("Use", "Abrasive blasting / surface preparation"),
        ],
    },
]


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


def key_value_table(rows):
    body = []
    for key, value in rows:
        body.append(
            [
                Paragraph(f"<b>{key}</b>", STYLES["BodyCopy"]),
                Paragraph(value, STYLES["BodyCopy"]),
            ]
        )

    table = Table(body, colWidths=[44 * mm, 122 * mm])
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


def build_header():
    logo = Image(str(LOGO), width=48 * mm, height=19 * mm)
    header = Table(
        [[logo, Paragraph("Manufacturer & Exporter of Minerals", STYLES["SmallRight"])]],
        colWidths=[88 * mm, 92 * mm],
    )
    header.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    return header


def build_tds_story(product):
    story = [build_header(), Spacer(1, 8)]
    story.append(Paragraph(f'{product["name"]} Technical Data Sheet', STYLES["DocTitle"]))
    story.append(Paragraph(product["subtitle"], STYLES["DocMeta"]))
    story.append(Paragraph("Commercial Summary", STYLES["SectionLabel"]))
    story.append(key_value_table(product["summary"]))
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
        "mesh, packing basis, and shipment requirement before final order confirmation."
    )
    story.append(Paragraph("Buyer Note", STYLES["SectionLabel"]))
    story.append(Paragraph(note, STYLES["BodyCopy"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Jade Waves Enterprise | deep@jadewavesenterprise.com | +91-999-883-5503", STYLES["SmallRight"]))
    return story


def build_coa_story(product):
    story = [build_header(), Spacer(1, 8)]
    story.append(Paragraph(f'{product["name"]} Sample COA', STYLES["DocTitle"]))
    story.append(
        Paragraph(
            "Representative sample reference prepared for buyer review. Current lot values are reconfirmed against the approved grade and order basis.",
            STYLES["DocMeta"],
        )
    )
    story.append(Paragraph("Sample Reference", STYLES["SectionLabel"]))
    story.append(key_value_table(product["coa"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Commercial Use", STYLES["SectionLabel"]))
    story.append(Paragraph(product["application"], STYLES["BodyCopy"]))
    story.append(Spacer(1, 10))
    note = (
        "This sample COA is a client-facing reference sheet only. Final shipment documents are aligned to the approved grade, packing basis, "
        "and destination requirement before dispatch."
    )
    story.append(Paragraph("Important Note", STYLES["SectionLabel"]))
    story.append(Paragraph(note, STYLES["BodyCopy"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Jade Waves Enterprise | deep@jadewavesenterprise.com | +91-999-883-5503", STYLES["SmallRight"]))
    return story


def write_pdf(path, story):
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
    )
    doc.build(story)


if __name__ == "__main__":
    STYLES = build_styles()
    for product in PRODUCTS:
        write_pdf(TDS_DIR / product["tds_file"], build_tds_story(product))
        write_pdf(COA_DIR / product["coa_file"], build_coa_story(product))
        print(product["tds_file"])
        print(product["coa_file"])
