from pathlib import Path

import generate_quartz_grits_q2_coa as base


base.OUTPUT = base.ROOT / "output" / "pdf" / "coa-quartz-grits-q1-premium-executive.pdf"
base.VECTOR_OUTPUT = base.ROOT / "tmp" / "pdfs" / "coa-quartz-grits-q1-executive-vector.pdf"
base.FLATTENED_IMAGE = base.ROOT / "tmp" / "pdfs" / "coa-quartz-grits-q1-executive-flattened.png"
base.DELIVERY_OUTPUT = Path("/Users/deepmehta/Documents/Jade Waves Enterprise/Products/Quartz/COA Quartz Grits Q1 - Premium Executive.pdf")
base.ASSET_OUTPUT = Path("/Users/deepmehta/Documents/Jade Waves Enterprise/Products/Quartz/assets/COA/all coas/COA Quartz Grits Q1 - Premium Executive.pdf")

base.PRODUCT_NAME = "Quartz Grits - Q1"
base.HEADER_SUBTITLE = "Premium COA for Quartz Grits - Q1"
base.DOCUMENT_TITLE = "Jade Waves Enterprise - Premium COA - Quartz Grits Q1"
base.DOCUMENT_SUBJECT = "Certificate of Analysis for Quartz Grits - Q1"
base.SUMMARY_DETAIL = "Representative sample analysis from supplied spec image"
base.PRIMARY_METRIC_LABEL = "Silica (SiO2)"
base.PRIMARY_METRIC_VALUE = ">99.0%"
base.SECONDARY_METRIC_LABEL = "Color L"
base.SECONDARY_METRIC_VALUE = "91 min"
base.TERTIARY_METRIC_LABEL = "Humidity"
base.TERTIARY_METRIC_VALUE = "Max 0.3%"

base.BUYER_REFERENCE = [
    (
        "Application",
        "Ceramics, glass manufacturing, engineered stone, and building materials",
    ),
    ("Forms", "Quartz grits in graded size fractions"),
    ("Typical grade range", "Q1 grits, >99.0% SiO2, L 91 min, moisture max 0.3%"),
    ("Packing options", "Jumbo bags"),
    ("HSN code", "25061020"),
    ("Inquiry contact", "deep@jadewavesenterprise.com | +91-999-883-5503"),
]

base.RESULT_ROWS = [
    ("1", "Chemical analysis", "SiO2", "> 99.0%"),
    ("2", "Chemical analysis", "Na2O", "0.05% max"),
    ("3", "Chemical analysis", "CaO", "0.03% max"),
    ("4", "Chemical analysis", "K2O", "0.05% max"),
    ("5", "Chemical analysis", "Fe2O3", "0.06% max"),
    ("6", "Chemical analysis", "K2O", "0.02% max"),
    ("7", "Chemical analysis", "TiO2", "0.04% max"),
    ("8", "Chemical analysis", "Al2O3", "0.1% max"),
    ("9", "Chemical analysis", "L.O.I.", "0.1 max"),
    ("10", "Color", "L", "91 min"),
    ("11", "Color", "a", "1.0 max"),
    ("12", "Color", "b", "2.5 max"),
    ("13", "Particle size distribution", "Grading performance", "Size in range > 90%; upper size < 5%; lower size < 5%"),
    ("14", "Impurity/100 gram", "Black Particle", "5"),
    ("15", "Impurity/100 gram", "Other colors particle", "5"),
    ("16", "Humidity", "Moisture", "Max 0.3%"),
    ("17", "Readily available sizes", "Standard fractions", "0.1-0.4 mm | 0.3-0.7 mm | 0.6-1.2 mm"),
    ("18", "Readily available sizes", "Extended fractions", "1.2-2.5 mm | 2.5-4.0 mm | 4.0-6.0 mm"),
]


if __name__ == "__main__":
    base.generate()
