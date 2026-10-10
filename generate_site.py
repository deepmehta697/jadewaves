from __future__ import annotations

import json
import os
import re
from datetime import date, datetime
from html import escape
from pathlib import Path
from textwrap import dedent

from templates import material_layout, material_pages, material_support
from templates.material_media import enhance_images


ROOT = Path(__file__).parent


def load_local_env(path: Path) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.removeprefix("export ").strip()
        if not key or key in os.environ:
            continue

        os.environ[key] = value.strip().strip('"').strip("'")


load_local_env(ROOT / ".env.local")

BASE_URL = "https://jadewavesenterprise.com"
PROJECT_PAGES_REPO = "jadewaves"
TODAY = date.today().isoformat()
BUILD_VERSION = os.environ.get("SITE_BUILD_VERSION", datetime.utcnow().strftime("%Y%m%d%H%M%S"))
CEO_LINKEDIN_URL = "https://www.linkedin.com/in/deep-mehta-034230226/"
GA4_MEASUREMENT_ID = "G-9BRL4JKNN6"
INQUIRY_ENDPOINT = os.environ.get("INQUIRY_ENDPOINT", "/api/inquiry").strip() or "/api/inquiry"
RECAPTCHA_SITE_KEY = os.environ.get("RECAPTCHA_SITE_KEY", "").strip()

CONTACT = {
    "company": "Jade Waves Enterprise",
    "phone": "+91-999-883-5503",
    "sales_email": "deep@jadewavesenterprise.com",
    "address": "A-11 Florence, Science City Road, Ahmedabad, Gujarat 380060, India",
    "port": "Near Mundra Port",
}

INDUSTRIES = [
    (
        "Glass",
        "Purity-led silica, quartz, and feldspar for glass batches where low iron and steadier melt behavior carry through.",
    ),
    (
        "Ceramics",
        "Quartz sand, feldspar, and silica sand for ceramic bodies, tiles, and glaze-linked production.",
    ),
    (
        "Construction",
        "Silica sand and feldspar for construction systems and mineral-heavy site demand.",
    ),
    (
        "Foundry",
        "Silica sand for foundry systems that depend on repeatable sizing and cleaner supply control.",
    ),
]


INDUSTRY_ICONS = {
    "Glass": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h14v2l-5 6v5l-4 3v-8L5 6V4z"/></svg>',
    "Ceramics": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/></svg>',
    "Construction": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9h18v11H3z"/><path d="M3 5h18v3H3z"/><path d="M9 12v8M15 12v8"/></svg>',
    "Chemicals": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 3v5l-5 9a3 3 0 0 0 2.6 4.5h8.8A3 3 0 0 0 19 17l-5-9V3"/><path d="M9 11h6"/></svg>',
    "Drilling": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l7-7"/><path d="M9 4l11 11"/><path d="M14 3l7 7"/></svg>',
    "Agriculture": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20c5-1 8-5 8-11-6 0-10 3-11 8"/><path d="M4 13c1 4 4 7 8 7"/><path d="M12 20V9"/></svg>',
    "Foundry": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg>',
}

PRODUCTS = [
    {
        "slug": "silica-sand",
        "name": "Silica Sand",
        "family": "Silica, Quartz & Feldspar",
        "anchor": "silica-quartz-feldspar",
        "theme": "silica",
        "eyebrow": "Glass / Filtration / Foundry / Construction",
        "seo_title": "Silica Sand Supplier & Exporter from India | Jade Waves Enterprise",
        "meta_description": "Silica sand supplier and exporter from India for glass manufacturing, filtration, foundry, and construction buyers across Vietnam, Thailand, UAE, Saudi Arabia, Mauritius, and Maldives.",
        "hero_copy": "Silica sand for glass manufacturing, filtration, foundry, and construction buyers who need clean chemistry, steady grain size, and export handling that stays under control.",
        "short_copy": "Silica sand supplier for glass manufacturing, filtration, foundry, and construction use.",
        "summary_spec": "SiO2 98.07% / Fe2O3 customizable to 150-200 PPM for glass",
        "applications": [
            "Glass manufacturing",
            "Water filtration media",
            "Foundry moulding systems",
            "Artificial turfs",
            "Paints",
            "Construction and specialty fillers",
        ],
        "benefits": [
            "SiO2 reported at 98.07%",
            "Fe2O3 reported at 0.30%",
            "Moisture reported below 0.10%",
            "K2O reported below 0.01%",
            "For glass industries, Fe2O3 can be customized to 150-200 PPM",
        ],
        "specs": [
            "SiO2 98.07%",
            "Fe2O3 0.30%",
            "Moisture below 0.10%",
            "K2O below 0.01%",
        ],
        "booking_points": [
            "Grain size",
            "SiO2 content",
            "Fe2O3 content, including 150-200 PPM glass-grade requirement",
            "Packing and order volume",
        ],
        "forms": ["Silica Sand", "Silica Flour"],
        "packing": "50 Kg/Jumbo Bags",
        "size_options": [
            "8 Mesh",
            "16 Mesh",
            "24 Mesh",
            "30 Mesh",
            "50 Mesh",
            "Custom AFS/Sizing available",
        ],
        "parameter_docs": [
            ("Silica Sand", "/assets/grade-sheets/silica-sand-parameter-sheet.pdf"),
        ],
        "parameter_docs_copy": "Chemical and physical parameter file for silica sand.",
        "commercial_fit": "For buyers who need silica that holds up in process and in transit.",
        "industries": ["Glass", "Foundry", "Construction", "Water Treatment"],
        "source_url": "https://jadewavesenterprise.com/silica-sand",
        "related": ["silica-flour", "quartz-sand-for-ceramics", "feldspar"],
    },
    {
        "slug": "silica-flour",
        "name": "Silica Flour",
        "family": "Silica, Quartz & Feldspar",
        "anchor": "silica-quartz-feldspar",
        "theme": "silica",
        "eyebrow": "Ceramics / Coatings / Fillers / Construction",
        "seo_title": "Silica Flour Supplier from India for Import Buyers | Jade Waves Enterprise",
        "meta_description": "Silica flour supplier from India for import buyers in Vietnam, Thailand, Malaysia, UAE, Saudi Arabia, Mauritius, and Maldives.",
        "hero_copy": "Silica flour with controlled sizing for ceramics, coatings, fillers, sealants, and construction systems that depend on a reliable micron profile.",
        "short_copy": "Controlled-size silica flour for ceramics, coatings, fillers, and specialty construction.",
        "summary_spec": "SiO2 99.10% / Fe2O3 0.036%",
        "applications": [
            "Ceramics and tile bodies",
            "Paints and coatings",
            "Construction fillers and specialty mixes",
            "Oil well cementing and sealant systems",
        ],
        "benefits": [
            "SiO2 reported at 99.10%",
            "Fe2O3 reported at 0.036%",
            "Al2O3 reported at 0.49%",
            "TiO2 reported at 0.018%",
        ],
        "specs": [
            "SiO2 99.10%",
            "Fe2O3 0.036%",
            "Al2O3 0.49%",
            "TiO2 0.018%",
        ],
        "booking_points": [
            "Mesh or micron grade",
            "SiO2 purity",
            "Whiteness target",
            "Packing and order volume",
        ],
        "forms": ["80 mesh silica flour", "300 mesh silica flour", "500 mesh silica flour", "Custom micron grading"],
        "packing": "50 Kg/Jumbo Bags",
        "commercial_fit": "For buyers who care more about particle discipline than generic silica supply.",
        "industries": ["Ceramics", "Construction", "Coatings", "Chemicals"],
        "source_url": "https://jadewavesenterprise.com/silica-flour",
        "related": ["silica-sand", "quartz-sand-for-ceramics", "kaolin--china-clay"],
    },
    {
        "slug": "quartz-sand-for-ceramics",
        "name": "Quartz Sand",
        "family": "Silica, Quartz & Feldspar",
        "anchor": "silica-quartz-feldspar",
        "theme": "quartz",
        "eyebrow": "Ceramics / Glass / Engineered Stone / Building Materials",
        "seo_title": "Quartz Sand Supplier from India | Grits & Powder Exporter | Jade Waves Enterprise",
        "meta_description": "Quartz sand supplier from India for ceramics, glass, and engineered stone buyers needing quartz grits and quartz powder supply across Vietnam, Thailand, Malaysia, UAE, and Saudi Arabia.",
        "hero_copy": "Quartz sand supplier from India for ceramics, glass, and engineered stone buyers needing quartz grits, quartz powder, and dependable export handling.",
        "short_copy": "Quartz sand supplier from India for ceramics, glass, and engineered stone.",
        "summary_spec": "SiO2 >99.0% / L value 91 min",
        "applications": [
            "Tiles and ceramic body production",
            "Glass manufacturing",
            "Engineered stone manufacturing",
            "Building material systems",
        ],
        "benefits": [
            "L value reported at 91 min",
            "Humidity reported at 0.3% max",
            "Particle distribution aligned to the selected size range",
            "Size in range reported above 90%",
        ],
        "specs": [
            "SiO2 >99.0%",
            "K2O 0.02% max",
            "Humidity 0.3% max",
            "L value 91 min",
        ],
        "booking_points": [
            "SiO2 >99.0%",
            "K2O 0.02% max",
            "Form & Grain/Mesh Size",
            "Color and whiteness target",
        ],
        "forms": ["Quartz Sand", "Quartz Grits", "Quartz Powder"],
        "size_options": [
            "0.1-0.4 mm",
            "0.3-0.7 mm",
            "0.6-1.2 mm",
            "1.2-2.5 mm",
            "2.5-4.0 mm",
            "4.0-6.0 mm",
            "200 Mesh",
            "325 Mesh",
            "400 Mesh",
            "Custom size available",
        ],
        "parameter_docs": [
            ("Quartz Grits Q1", "/assets/grade-sheets/quartz-grits-q1-parameter-sheet.pdf"),
            ("Quartz Grits Q2", "/assets/grade-sheets/quartz-grits-q2-parameter-sheet.pdf"),
            ("Quartz Powder", "/assets/grade-sheets/quartz-powder-c-parameter-sheet.pdf"),
        ],
        "parameter_docs_copy": "Chemical and physical parameter files for active quartz grits and powder grades.",
        "packing": "50 Kg/Jumbo Bags",
        "commercial_fit": "For ceramic, glass, and engineered stone lines where purity and brightness show up in the finish.",
        "industries": ["Ceramics", "Glass", "Construction"],
        "source_url": "https://jadewavesenterprise.com/quartz-sand-for-ceramics",
        "related": ["silica-sand", "silica-flour", "feldspar"],
    },
    {
        "slug": "bentonite",
        "name": "Bentonite",
        "family": "Clays & Functional Fillers",
        "anchor": "clays-fillers",
        "theme": "clay",
        "eyebrow": "Drilling / Foundry / Civil / Absorbent Grades",
        "seo_title": "Bentonite Supplier & Exporter from India | Jade Waves Enterprise",
        "meta_description": "Bulk bentonite supplier and exporter from India for drilling, foundry, sealing, and absorbent buyers in Vietnam, UAE, Oman, Qatar, Bahrain, Saudi Arabia, and Malaysia.",
        "hero_copy": "Bentonite for drilling, foundry, sealing, absorbent, and bleaching grades where swelling, viscosity, and moisture control need to stay dependable for bulk export buyers.",
        "short_copy": "Bentonite supplier for drilling, foundry, sealing, absorbent, and bleaching use.",
        "summary_spec": "pH 9-11 / Liquid limit 450 min",
        "applications": [
            "Drilling fluids for oil, gas, and HDD",
            "Foundry and casting systems",
            "Construction, sealing, and waterproofing work",
            "Cat litter and absorbent applications",
            "Activated bleaching earth and filtration use",
        ],
        "benefits": [
            "Moisture specified at 14% max",
            "Liquid limit specified at 450 min",
            "Gel index specified at 60 min",
            "Marsh funnel viscosity specified at 50 sec min",
        ],
        "specs": [
            "pH at 2% bentonite suspension: 9-11",
            "200 BSS mesh passing: 85 min",
            "Filtrate loss: 18 max",
            "Slurry density: 1.0 to 1.20 gm/cc",
        ],
        "booking_points": [
            "Application",
            "Sodium or calcium grade",
            "pH, liquid limit, and viscosity target",
            "Moisture and filtrate loss",
            "Packing and order volume",
        ],
        "forms": ["Sodium bentonite", "Calcium bentonite", "Application-specific bentonite grades", "Activated Bleaching Earth"],
        "packing": "50 Kg/Jumbo Bags",
        "commercial_fit": "For operations that need bentonite to perform the same way from batch to batch.",
        "industries": ["Drilling", "Foundry", "Construction", "Treatment"],
        "source_url": "https://jadewavesenterprise.com/bentonite#ace72553-7437-4a98-b346-2b25da28c515",
        "related": ["kaolin--china-clay", "talc", "fly-ash"],
    },
    {
        "slug": "kaolin--china-clay",
        "name": "Kaolin (China Clay)",
        "family": "Clays & Functional Fillers",
        "anchor": "clays-fillers",
        "theme": "kaolin",
        "eyebrow": "Ceramics / Coatings / Paper / Fillers",
        "seo_title": "China Clay Supplier from India | Kaolin Exporter | Jade Waves Enterprise",
        "meta_description": "China clay supplier from India for import buyers in Vietnam, Thailand, Malaysia, UAE, and Saudi Arabia.",
        "hero_copy": "Kaolin with high brightness and a cleaner impurity profile for ceramics, coatings, paper, rubber, and filler systems.",
        "short_copy": "High-brightness kaolin for ceramics, coatings, paper, rubber, and fillers.",
        "summary_spec": "Whiteness 86.17 / Fe2O3 0.29%",
        "applications": [
            "Ceramics and tiles",
            "Paints and coatings",
            "Paper systems",
            "Rubber and industrial fillers",
        ],
        "benefits": [
            "Whiteness reported at 86.17",
            "L* reported at 94.48",
            "Residue at 240# after 2 min grinding reported at 0.13",
            "Water absorption reported at 22.81%",
        ],
        "specs": [
            "SiO2 47.43%",
            "Al2O3 37.01%",
            "Fe2O3 0.29%",
            "LOI 13.21%",
        ],
        "booking_points": [
            "Brightness target",
            "Fe2O3 limit",
            "Al2O3 and SiO2 profile",
            "Form, packing, and order volume",
        ],
        "forms": ["Lumps & Powder"],
        "packing": "Jumbo Bags",
        "commercial_fit": "For buyers chasing brightness, cleaner firing, and a tighter filler profile.",
        "industries": ["Ceramics", "Paper", "Coatings", "Fillers"],
        "source_url": "https://jadewavesenterprise.com/kaolin--china-clay",
        "related": ["talc", "feldspar", "silica-flour"],
    },
    {
        "slug": "talc",
        "name": "Talc",
        "family": "Clays & Functional Fillers",
        "anchor": "clays-fillers",
        "theme": "talc",
        "eyebrow": "Plastics / Paints / Ceramics / Rubber",
        "seo_title": "Talc Powder Supplier from India for Import Buyers | Jade Waves Enterprise",
        "meta_description": "Talc powder supplier from India for import buyers in Vietnam, Thailand, Malaysia, UAE, Oman, Qatar, Bahrain, and Saudi Arabia.",
        "hero_copy": "Talc powder for plastics, paints, ceramics, rubber, cable, detergents, and fillers where whiteness, fineness, and smoother processing matter.",
        "short_copy": "High-whiteness talc powder for plastics, coatings, ceramics, rubber, cable, detergents, and fillers.",
        "applications": [
            "Plastics and polymer compounds",
            "Paints and coatings",
            "Ceramics",
            "Rubber and industrial fillers",
            "Detergents and soaps",
            "Cables and wire compounds",
            "Pharma and drug filler use",
        ],
        "benefits": [
            "High whiteness",
            "Ultra-fine particle size",
            "Smoothness in processing",
            "Chemical stability",
        ],
        "specs": [
            "Various grain/mesh sizes",
            "High MgO orientation",
            "SiO2 profile aligned to grade",
            "High whiteness",
        ],
        "booking_points": [
            "Form & Grain/Mesh Size",
            "Whiteness target",
            "MgO and SiO2 profile",
            "Packing and order volume",
        ],
        "forms": ["Talc powder in application-specific mesh sizes"],
        "packing": "Jumbo Bags",
        "commercial_fit": "For formulations that depend on whiteness, smoothness, and finer control.",
        "industries": ["Plastics", "Coatings", "Ceramics", "Rubber"],
        "source_url": "https://jadewavesenterprise.com/talc",
        "related": ["kaolin--china-clay", "feldspar", "silica-flour"],
    },
    {
        "slug": "feldspar",
        "name": "Feldspar",
        "family": "Silica, Quartz & Feldspar",
        "anchor": "silica-quartz-feldspar",
        "theme": "feldspar",
        "eyebrow": "Ceramics / Sanitaryware / Glass",
        "seo_title": "Potash & Soda Feldspar Supplier from India | Jade Waves Enterprise",
        "meta_description": "Potash and soda feldspar supplier from India for ceramics, sanitaryware, glass, and engineered stone buyers in Vietnam, Thailand, the Philippines, UAE, Malaysia, and Saudi Arabia.",
        "hero_copy": "Potash and soda feldspar supplied for ceramic, sanitaryware, tile, glass, and engineered stone production where flux behavior, melting control, and cleaner firing matter.",
        "short_copy": "Potash and soda feldspar for ceramics, sanitaryware, glass, and engineered stone production.",
        "summary_spec": "K2O up to 12% / Na2O up to 10%",
        "applications": [
            "Ceramic and tile production",
            "Sanitaryware manufacturing",
            "Glass production",
            "Engineered stone and flux-driven mineral systems",
        ],
        "benefits": [
            "Potassium feldspar grades run up to 12% K2O",
            "Sodium feldspar grades run up to 10% Na2O",
            "Fe2O3 ranges from 0.06% to 0.15% depending on grade",
            "Firing results cover milky white, off white, and super white outputs",
        ],
        "specs": [
            "Potassium feldspar 10-12% K2O",
            "Sodium feldspar 8-10% Na2O",
            "Fe2O3 0.06-0.15% by grade",
            "100 Mesh to 350 Mesh and custom sizing",
        ],
        "booking_points": [
            "Potassium feldspar 10-12% K2O",
            "Sodium feldspar 8-10% Na2O",
            "K2O% or Na2O%",
            "Fe2O3 limit",
            "Form, mesh, and order volume",
        ],
        "forms": ["Lumps & Powder"],
        "size_options": ["100 Mesh", "200 Mesh", "325 Mesh", "350 Mesh", "Custom sizing available"],
        "parameter_docs": [
            ("Sodium Feldspar", "/assets/grade-sheets/soda-feldspar-parameter-sheet.pdf"),
            ("Potassium Feldspar", "/assets/grade-sheets/potash-feldspar-parameter-sheet.pdf"),
        ],
        "parameter_docs_copy": "Chemical and physical parameter files for sodium and potassium feldspar grades.",
        "packing": "Jumbo Bags",
        "commercial_fit": "For manufacturers who need flux contribution to be predictable, not approximate.",
        "industries": ["Ceramics", "Sanitaryware", "Glass", "Engineered Stone"],
        "source_url": "https://jadewavesenterprise.com/feldspar",
        "related": ["quartz-sand-for-ceramics", "kaolin--china-clay", "talc"],
    },
    {
        "slug": "salt",
        "name": "Salt",
        "family": "Industrial Salt Grades",
        "anchor": "salt-grades",
        "theme": "salt",
        "eyebrow": "Chemical / Water Treatment / Utility / Food-Linked Supply",
        "seo_title": "Industrial Salt Supplier & Exporter from India | Jade Waves Enterprise",
        "meta_description": "Industrial salt supplier and exporter from India for water treatment, chemical processing, de-icing, and iodized salt buyers in UAE, Oman, Qatar, Bahrain, Saudi Arabia, Mauritius, and Maldives.",
        "hero_copy": "Industrial and iodized salt grades for water treatment, chemical processing, infrastructure, and food-linked demand, with flexible packing and dependable export flow.",
        "short_copy": "Iodized and non-iodized salt grades for water treatment, chemical, utility, and food-linked supply.",
        "summary_spec": "NaCl 99.00% / Moisture 0.2% max",
        "applications": [
            "Chemical and industrial processing",
            "Water treatment applications",
            "De-icing and utility use",
            "Food processing and commercial supply",
        ],
        "benefits": [
            "NaCl reported at 99.00% min",
            "Moisture reported at 0.2% max",
            "Consumption salt typically carries 25-30 PPM iodine and can be customized",
            "Iodine is NIL for salt grades supplied outside consumption use",
        ],
        "specs": [
            "Whiteness reported at 92",
            "NaCl 99.00% min",
            "Iodine 25-30 PPM for edible grades",
            "Iodine NIL for non-consumption grades",
        ],
        "booking_points": [
            "Required salt grade",
            "NaCl purity and iodine requirement",
            "Grain size",
            "Packing and monthly volume",
        ],
        "forms": [
            "Triple refined iodized salt",
            "Free flow iodized salt",
            "Industrial salt",
            "De-icing salt",
            "Crystalline salt",
            "Raw salt",
        ],
        "packing": "50 Kg/Jumbo Bags",
        "commercial_fit": "For buyers managing multiple grades, steady volumes, and flexible packing requirements.",
        "industries": ["Chemicals", "Water Treatment", "Infrastructure", "Food Processing"],
        "source_url": "https://jadewavesenterprise.com/salt",
        "related": ["silica-sand", "bentonite", "fly-ash"],
    },
    {
        "slug": "fly-ash",
        "name": "Fly Ash",
        "family": "Construction & Industrial Media",
        "anchor": "construction-media",
        "theme": "ash",
        "eyebrow": "Concrete / Cement / Blocks / Roads",
        "seo_title": "Fly Ash Supplier from India for Import Buyers | Jade Waves Enterprise",
        "meta_description": "Fly ash supplier from India for import buyers in the Philippines, Malaysia, UAE, Oman, Qatar, Bahrain, and Saudi Arabia.",
        "hero_copy": "Fly ash for cement, concrete, blocks, and infrastructure work that depends on steady dispatch and consistent replacement performance.",
        "short_copy": "Fly ash supplied for cement, concrete, blocks, and infrastructure work.",
        "summary_spec": "SiO2 55.13% / Al2O3 24.45% / LOI <1%",
        "applications": [
            "Cement and concrete production",
            "Fly ash bricks and blocks",
            "Roads and embankments",
            "Infrastructure-linked mineral substitution",
        ],
        "benefits": [
            "SiO2 reported at 55.13%",
            "Al2O3 reported at 24.45%",
            "Loss on ignition reported below 1%",
            "Residue on 45 micron sieve reported below 12%",
        ],
        "specs": [
            "SiO2 55.13%",
            "Al2O3 24.45%",
            "Fe2O3 7.43%",
            "CaO 3.54%",
        ],
        "booking_points": [
            "Application and replacement target",
            "SiO2 and Al2O3 profile",
            "Packing format",
            "Dispatch volume and schedule",
        ],
        "forms": ["Dry fly ash", "Bulk fly ash"],
        "packing": "50 Kg/Jumbo Bags",
        "commercial_fit": "For cement and infrastructure buyers who need dispatch discipline as much as material fit.",
        "industries": ["Construction", "Cement", "Infrastructure"],
        "source_url": "https://jadewavesenterprise.com/fly-ash",
        "related": ["copper-slag", "silica-sand", "bentonite"],
    },
    {
        "slug": "copper-slag",
        "name": "Copper Slag",
        "family": "Construction & Industrial Media",
        "anchor": "construction-media",
        "theme": "copper",
        "eyebrow": "Blasting / Surface Preparation / Construction",
        "seo_title": "Copper Slag Supplier from India for Import Buyers | Jade Waves Enterprise",
        "meta_description": "Copper slag supplier from India for import buyers in UAE, Oman, Qatar, Bahrain, Saudi Arabia, Malaysia, and Singapore.",
        "hero_copy": "Copper slag abrasive for blasting and surface preparation where hardness, angularity, and cleaner handling matter.",
        "short_copy": "Copper slag grit supplied for blasting, surface preparation, and construction use.",
        "summary_spec": "Moh's 6.0-7.0 / Specific gravity 3.51",
        "applications": [
            "Abrasive blasting",
            "Surface preparation",
            "Construction and concrete systems",
            "Industrial maintenance and fabrication work",
        ],
        "benefits": [
            "Hardness reported at 6.0-7.0 on Moh's scale",
            "Specific gravity reported at 3.51",
            "Granules are angular, sharp-edged, and multi-faced",
            "Electrical conductivity reported at 2 mS/m",
        ],
        "specs": [
            "Fe 42-48%",
            "SiO2 26-30%",
            "Cu 0.60-0.70%",
            "pH 7.0-7.5",
        ],
        "booking_points": [
            "Sieve size distribution",
            "Density and hardness",
            "Angular grain profile",
            "Packing and shipment volume",
        ],
        "forms": ["Copper slag grit"],
        "size_options": [
            "4.00-3.00 mm",
            "3.00-2.36 mm",
            "2.36-1.00 mm",
            "1.00-0.50 mm",
            "0.50-0.212 mm",
            "0.212 mm & below",
        ],
        "packing": "50 Kg/Jumbo Bags",
        "commercial_fit": "For abrasive work where particle performance and dependable supply both matter.",
        "industries": ["Blasting", "Surface Preparation", "Construction"],
        "source_url": "https://jadewavesenterprise.com/copper-slag",
        "related": ["fly-ash", "silica-sand", "feldspar"],
    },
    {
        "slug": "rubber-granules",
        "name": "Rubber Granules",
        "family": "Rubber & Surface Media",
        "anchor": "rubber-surface-media",
        "category": "Industrial Material",
        "theme": "rubber",
        "eyebrow": "Artificial Turf / Sports / Safety Surfaces",
        "seo_title": "Rubber Granules Supplier from India | Jade Waves Enterprise",
        "meta_description": "Rubber granules supplier from India for artificial turf, sports surfaces, playground flooring, and impact-absorbing applications with export-ready packing and dispatch support.",
        "hero_copy": "Rubber granules for artificial turf, sports surfaces, playground flooring, and impact-absorbing systems where particle consistency and dependable export handling matter.",
        "short_copy": "Rubber granules for artificial turf, sports, playground, and safety surface applications.",
        "summary_spec": "Application-specific granule sizing / clean, dry export supply",
        "applications": [
            "Artificial turf infill",
            "Sports and athletic surfaces",
            "Playground and safety flooring",
            "Rubber-modified construction systems",
        ],
        "benefits": [
            "Particle size aligned to the selected application",
            "Clean, dry material handling for export packing",
            "Sample-led confirmation before repeat supply",
            "Packing and dispatch planning aligned to order volume",
        ],
        "specs": [
            "Particle size and grading",
            "Material type and composition",
            "Cleanliness and moisture condition",
            "Packing and order volume",
        ],
        "booking_points": [
            "Application and surface system",
            "Required particle size",
            "Material type and color requirement",
            "Packing and order volume",
        ],
        "forms": ["SBR rubber granules", "Crumb rubber", "Application-specific grades"],
        "packing": "50 Kg/Jumbo Bags",
        "commercial_fit": "For sports, recreation, and surface-system buyers who need a practical granule specification and a clear route to repeat supply.",
        "industries": ["Artificial Turf", "Sports Surfaces", "Playground Flooring", "Construction"],
        "source_url": "https://jadewavesenterprise.com/rubber-granules",
        "related": ["copper-slag", "silica-sand", "fly-ash"],
    },
]

PACKING_BY_SLUG = {
    "silica-sand": "50 Kg/Jumbo Bags",
    "silica-flour": "50 Kg/Jumbo Bags",
    "quartz-sand-for-ceramics": "Jumbo Bags",
    "bentonite": "50 Kg/Jumbo Bags",
    "kaolin--china-clay": "50 Kg/Jumbo Bags",
    "fly-ash": "Jumbo Bags",
    "copper-slag": "Jumbo Bags",
    "rubber-granules": "50 Kg/Jumbo Bags",
}

for product in PRODUCTS:
    packing = PACKING_BY_SLUG.get(product["slug"])
    if packing:
        product["packing"] = packing

CORE_PRODUCT_SLUGS = [
    "silica-sand",
    "silica-flour",
    "quartz-sand-for-ceramics",
    "bentonite",
    "kaolin--china-clay",
    "talc",
    "feldspar",
    "salt",
    "fly-ash",
    "copper-slag",
    "rubber-granules",
]
PRODUCTS = [product for product in PRODUCTS if product["slug"] in CORE_PRODUCT_SLUGS]

PRODUCTS_BY_SLUG = {product["slug"]: product for product in PRODUCTS}

PRODUCT_FAMILIES = [
    {
        "id": "silica-quartz-feldspar",
        "name": "Silica, Quartz & Feldspar",
        "copy": "Purity-led grades for glass, ceramics, filtration media, and engineered stone manufacturing.",
        "best_for": ["Glass", "Ceramics", "Filtration", "Engineered Stone"],
        "products": ["silica-sand", "silica-flour", "quartz-sand-for-ceramics", "feldspar"],
        "visual_slug": "quartz-sand-for-ceramics",
    },
    {
        "id": "clays-functional-fillers",
        "name": "Clays & Functional Fillers",
        "copy": "Application-led grades for drilling, ceramics, coatings, absorbents, and process filler demand.",
        "best_for": ["Drilling", "Ceramics", "Coatings", "Fillers"],
        "products": ["bentonite", "kaolin--china-clay", "talc"],
        "visual_slug": "kaolin--china-clay",
    },
    {
        "id": "industrial-salt-grades",
        "name": "Industrial Salt Grades",
        "copy": "Salt supplied for chemical processing, water treatment, utilities, and consumption-linked programs where iodine can be specified separately.",
        "best_for": ["Chemicals", "Water Treatment", "Utilities", "Consumption"],
        "products": ["salt"],
        "visual_slug": "salt",
    },
    {
        "id": "industrial-media-pozzolans",
        "name": "Industrial Media & Pozzolans",
        "copy": "Copper slag and fly ash for blasting, concrete systems, blocks, and infrastructure-led buying programs.",
        "best_for": ["Blasting", "Concrete", "Blocks", "Infrastructure"],
        "products": ["copper-slag", "fly-ash"],
        "visual_slug": "copper-slag",
    },
    {
        "id": "rubber-surface-media",
        "name": "Rubber & Surface Media",
        "copy": "Granulated rubber supply for artificial turf, sports surfaces, playground flooring, and impact-absorbing systems.",
        "best_for": ["Artificial Turf", "Sports Surfaces", "Playground Flooring", "Safety Surfaces"],
        "products": ["rubber-granules"],
        "visual_slug": "rubber-granules",
    },
]

HOME_FEATURED = ["silica-sand", "quartz-sand-for-ceramics", "feldspar"]

BLOGS = [
    {
        "slug": "quartz-sand-supplier-india-vietnam-buyers-guide",
        "title": "Quartz Sand Supplier from India: Buyer Checklist for Vietnam Ceramics and Glass Teams",
        "eyebrow": "Quartz Sand / Vietnam / Ceramics-Glass",
        "summary": "What import buyers should confirm before RFQ when sourcing quartz sand, grits, and powder from India.",
        "marquee_title": "Quartz Sand for Vietnam Buyers",
        "seo_title": "Quartz Sand Supplier from India for Vietnam Buyers | Jade Waves Guide",
        "meta_description": "Buyer guide for Vietnam importers sourcing quartz sand from India for ceramics and glass. Learn key checks before quote and dispatch.",
        "product_slug": "quartz-sand-for-ceramics",
        "sections": [
            {
                "heading": "Start with end use, not only product name",
                "body": "Quartz requirements change by process. A tile body brief, float glass brief, and engineered stone brief should not be priced the same way.",
                "points": [
                    "Confirm application first: ceramic body, glass batch, or engineered stone line.",
                    "Ask for chemistry aligned to use, not generic lab values.",
                    "Fix acceptable color and whiteness range before trial quantity.",
                ],
            },
            {
                "heading": "Lock sizing and consistency before commercial terms",
                "body": "Most trial failures happen due to particle distribution mismatch, not because the product name was wrong.",
                "points": [
                    "Specify required grain/mesh range and tolerance.",
                    "Confirm moisture expectation at dispatch stage.",
                    "Request batch consistency approach for repeat orders.",
                ],
            },
            {
                "heading": "Align packing and shipment basis early",
                "body": "For import teams, landed performance depends on how material is packed and moved, not only on sample chemistry.",
                "points": [
                    "Confirm 50 Kg vs jumbo bag basis with loading plan.",
                    "Lock shipment basis (FOB/CIF/CNF) in writing.",
                    "Check dispatch timeline against production planning window.",
                ],
            },
        ],
        "questions": [
            "Can you share the grade against our exact end use?",
            "Which size range can you hold consistently in production batches?",
            "What packing format is best for our unloading setup?",
            "What document set comes with each shipment?",
            "What is practical lead time for trial and repeat volume?",
        ],
    },
    {
        "slug": "potassium-vs-sodium-feldspar-import-buyer-guide",
        "title": "Potassium vs Sodium Feldspar: What Import Buyers Should Confirm Before Buying",
        "eyebrow": "Feldspar / Ceramics-Glass / Import Guide",
        "summary": "How buyers compare potash and soda feldspar grades for ceramic and glass applications before quote.",
        "marquee_title": "Potassium vs Sodium Feldspar",
        "seo_title": "Potassium vs Sodium Feldspar Import Guide | Jade Waves Enterprise",
        "meta_description": "Import buyer guide on selecting potassium feldspar vs sodium feldspar from India for ceramic and glass applications.",
        "product_slug": "feldspar",
        "sections": [
            {
                "heading": "Choose the feldspar type based on process behavior",
                "body": "Potassium and sodium feldspar are not interchangeable in every ceramic or glass process.",
                "points": [
                    "Define whether melt behavior or body strength is the priority.",
                    "Share production constraints where flux response matters.",
                    "Confirm target chemistry profile before asking for price.",
                ],
            },
            {
                "heading": "Ask for chemistry and form together",
                "body": "Chemistry without particle form creates trial uncertainty.",
                "points": [
                    "Confirm potassium/sodium content expectation.",
                    "Select form and mesh according to process feed system.",
                    "Request typical impurity limits relevant to end use.",
                ],
            },
            {
                "heading": "Reduce import risk with a trial-first structure",
                "body": "A clean trial plan makes repeat ordering faster and safer.",
                "points": [
                    "Start with controlled trial volume and fixed grade.",
                    "Use same packing basis intended for repeat orders.",
                    "Pre-align documents and dispatch timeline for quick scale-up.",
                ],
            },
        ],
        "questions": [
            "Which feldspar type do you recommend for our use case and why?",
            "Can you hold this chemistry and mesh in repeat supply?",
            "What is standard packing and shipment basis for our destination?",
            "Which technical and commercial documents will be provided?",
        ],
    },
    {
        "slug": "silica-sand-import-checklist-glass-foundry-filtration",
        "title": "Silica Sand Import Checklist for Glass, Foundry, and Filtration Buyers",
        "eyebrow": "Silica Sand / Buyer Checklist",
        "summary": "A practical import checklist for buyers comparing silica sand suppliers and preparing a clean RFQ.",
        "marquee_title": "Silica Sand Import Checklist",
        "seo_title": "Silica Sand Import Checklist for Buyers | Jade Waves Enterprise",
        "meta_description": "Silica sand buyer checklist covering grain size, SiO2, Fe2O3, packing, shipment basis, and documents before import order.",
        "product_slug": "silica-sand",
        "sections": [
            {
                "heading": "Define technical requirement by application",
                "body": "Glass, foundry, and filtration buyers need different control points, even if all are sourcing silica sand.",
                "points": [
                    "Share intended end use with operating condition.",
                    "Specify target SiO2 range and relevant impurity limits.",
                    "Confirm acceptable grain size range and tolerance.",
                ],
            },
            {
                "heading": "Evaluate supplier response quality, not just rate",
                "body": "A low quote without clear technical alignment creates avoidable delays at trial stage.",
                "points": [
                    "Ask whether grade is matched to your exact use case.",
                    "Review TDS and sample COA for the discussed grade.",
                    "Check how quickly technical clarifications are handled.",
                ],
            },
            {
                "heading": "Prepare dispatch flow before final confirmation",
                "body": "Import execution improves when packing, documents, and shipment basis are settled early.",
                "points": [
                    "Select packing size based on unloading capability.",
                    "Lock shipment basis and destination port plan.",
                    "Confirm document set and communication owner for updates.",
                ],
            },
        ],
        "questions": [
            "Can you support Fe2O3 range needed for our application?",
            "What size options can be supplied consistently?",
            "Can we align trial grade and repeat grade from the start?",
            "What is expected lead time from PO to dispatch?",
        ],
    },
    {
        "slug": "bentonite-grade-selection-guide-for-importers",
        "title": "Bentonite Grade Selection Guide for Drilling, Foundry, and Civil Buyers",
        "eyebrow": "Bentonite / Grade Selection",
        "summary": "How buyers shortlist bentonite grades by application and avoid mismatched trials.",
        "marquee_title": "Bentonite Grade Selection",
        "seo_title": "Bentonite Grade Selection Guide for Import Buyers | Jade Waves",
        "meta_description": "Import guide for selecting bentonite grades for drilling, foundry, piling, HDD, and earthing applications.",
        "product_slug": "bentonite",
        "sections": [
            {
                "heading": "Map grade to application performance",
                "body": "Bentonite buying should be led by function: swelling behavior, viscosity response, and moisture stability.",
                "points": [
                    "Define exact application: drilling, foundry, piling, HDD, earthing, or sealing.",
                    "Share process condition where rheology matters.",
                    "Confirm handling and storage realities at destination.",
                ],
            },
            {
                "heading": "Clarify form and usage plan",
                "body": "Lumps and powder behave differently in handling and blending systems.",
                "points": [
                    "Choose supply form based on your dosing method.",
                    "Share expected monthly volume and trial target.",
                    "Ask for grade consistency approach for repeat shipments.",
                ],
            },
            {
                "heading": "Commercial fit should follow technical fit",
                "body": "Quoting first and qualifying later often increases cost and delay.",
                "points": [
                    "Confirm grade shortlist before rate comparison.",
                    "Align packing and shipment terms to your site setup.",
                    "Keep documentation and dispatch updates in one owner flow.",
                ],
            },
        ],
        "questions": [
            "Which bentonite grade fits our exact application?",
            "What technical references can you share for that grade?",
            "How do you handle repeat-batch consistency?",
            "What are the practical timelines for shipment?",
        ],
    },
    {
        "slug": "industrial-salt-import-guide-gulf-buyers",
        "title": "Industrial Salt Import Guide for UAE, Oman, Qatar, and Kuwait Buyers",
        "eyebrow": "Salt / Gulf Importers",
        "summary": "A buyer-side guide for industrial salt sourcing from India with packaging and dispatch clarity.",
        "marquee_title": "Industrial Salt for Gulf Buyers",
        "seo_title": "Industrial Salt Import Guide for Gulf Buyers | Jade Waves Enterprise",
        "meta_description": "Industrial salt import guide for UAE, Oman, Qatar, and Kuwait buyers covering grades, packing, and shipment planning.",
        "product_slug": "salt",
        "sections": [
            {
                "heading": "Select grade by process requirement",
                "body": "Industrial salt inquiries work best when application context is shared first.",
                "points": [
                    "Clarify if requirement is chemical processing, treatment, or utility use.",
                    "Share grade preference and acceptance range.",
                    "Align crystal size with process handling setup.",
                ],
            },
            {
                "heading": "Avoid confusion in RFQ language",
                "body": "Using generic salt terms creates back-and-forth that delays purchasing cycles.",
                "points": [
                    "Use clear grade name and packing basis in RFQ.",
                    "Include destination and shipment term expectation.",
                    "Mention monthly or project volume range for practical quote.",
                ],
            },
            {
                "heading": "Treat logistics as part of product quality",
                "body": "Packing integrity and dispatch consistency directly affect usable material at destination.",
                "points": [
                    "Confirm packing protection for transit conditions.",
                    "Align loading plan to receiving infrastructure.",
                    "Ensure document set is finalized before vessel planning.",
                ],
            },
        ],
        "questions": [
            "Which salt grade is best for our end use?",
            "Can you support our packing and unloading format?",
            "What documents are supplied with each shipment?",
            "What lead time should we plan for repeat orders?",
        ],
    },
    {
        "slug": "potassium-feldspar-supplier-for-ceramic-tiles",
        "title": "Potassium Feldspar Supplier for Ceramic Tiles: Export-Ready Supply for Manufacturers",
        "display_title_lines": [
            "Potassium Feldspar for Ceramic Tiles",
            "Export-Ready Supply",
        ],
        "eyebrow": "Potassium Feldspar / Ceramic Tiles",
        "summary": "A direct buyer guide for ceramic tile manufacturers reviewing potassium feldspar grade fit, particle size alignment, and export handling from India.",
        "marquee_title": "Potassium Feldspar for Ceramic Tiles",
        "seo_title": "Potassium Feldspar Supplier for Ceramic Tiles | Export Supply from India",
        "meta_description": "Looking for a potassium feldspar supplier for ceramic tiles? Get export-ready supply from India with grade alignment, mesh customization, packing options, and shipment support for ceramic manufacturers.",
        "product_slug": "feldspar",
        "sections": [
            {
                "heading": "What we supply for ceramic tile manufacturers",
                "body": "If your team is sourcing potassium feldspar for ceramic tiles, the first step is to align body or glaze use, particle size direction, and shipment basis before quotation starts.",
                "points": [
                    "Supply discussions can be aligned for body and glaze applications",
                    "Potassium feldspar powder is handled as the primary ceramic tile supply format",
                    "Custom particle size feasibility can be discussed during RFQ stage",
                ],
            },
            {
                "heading": "How potassium feldspar is used in ceramic tiles",
                "body": "Ceramic buyers usually evaluate feldspar not only by chemistry, but by how consistently it fits formulation, firing behavior, and repeat production planning.",
                "points": [
                    "Tile body formulations",
                    "Glaze formulations",
                    "Plant trials before repeat-order alignment",
                    "Production planning where consistency matters lot to lot",
                ],
            },
            {
                "heading": "What buyers usually require before quotation",
                "body": "Ceramic tile teams tend to move faster when the requirement is translated into a commercial brief early instead of being left as a generic feldspar inquiry.",
                "points": [
                    "Application fit for body or glaze use",
                    "Particle size or mesh requirement aligned to process setup",
                    "Trial-to-bulk continuity and repeat shipment basis",
                    "Packing, destination, and shipment planning handled in the same conversation",
                ],
            },
            {
                "heading": "Export and shipment support",
                "body": "For import buyers, supply reliability includes how the material is packed, documented, and moved, not just whether the chemistry looks workable on paper.",
                "points": [
                    "Flexible packing discussion based on handling preference",
                    "Containerized export planning for ceramic raw material procurement",
                    "Document and shipment coordination based on buyer instructions and destination",
                ],
            },
        ],
        "questions": [
            "Tile body or glaze application",
            "Required particle size or mesh range",
            "Monthly volume and trial quantity",
            "Destination port and preferred packing basis",
            "Any grade or chemistry checkpoints that must be matched first",
        ],
    },
    {
        "slug": "kaolin-supplier-for-paint-industry",
        "title": "Kaolin Supplier for Paint Industry: What We Supply",
        "eyebrow": "Kaolin / Paint Industry",
        "summary": "A direct kaolin supply guide for paint and coatings buyers reviewing forms, brightness focus, and export handling from India.",
        "marquee_title": "Kaolin for Paint Industry",
        "seo_title": "Kaolin Supplier for Paint Industry | Forms, Brightness Focus, Export Supply",
        "meta_description": "Kaolin supply for paint industry buyers with forms, quality focus points, and export handling support from India.",
        "product_slug": "kaolin--china-clay",
        "sections": [
            {
                "heading": "What we offer",
                "body": "If your team is sourcing kaolin for paint industry use, the first step is to align the form, brightness direction, and shipment basis before quotation starts.",
                "points": [
                    "Current supply forms include lumps and powder",
                    "Paint and coatings discussions are aligned to application before commercial offer",
                    "Packing and shipment planning are handled together with the grade conversation",
                ],
            },
            {
                "heading": "Where the kaolin line is used",
                "body": "Kaolin requirements change by end use, so paint buyers usually need cleaner alignment on performance and impurity expectations early.",
                "points": [
                    "Paints and coatings",
                    "Ceramics and tiles",
                    "Paper systems",
                    "Rubber and industrial fillers",
                ],
            },
            {
                "heading": "Quality focus before quotation",
                "body": "Technical alignment helps paint-industry buyers avoid trial drift between the sample basis and repeat supply basis.",
                "points": [
                    "Brightness target and Fe2O3 limit are aligned first",
                    "Al2O3 and SiO2 profile are reviewed against application need",
                    "Form, packing, and order volume are handled with the quality discussion",
                ],
            },
            {
                "heading": "Supply and export setup",
                "body": "The material fit matters, but the shipment basis needs to stay equally clear when import planning starts.",
                "points": [
                    "Packing: 50 Kg bags and jumbo bags",
                    "Shipment mode: FCL",
                    "Export handling includes sample alignment, document alignment, and shipment planning from India based on destination and order size",
                ],
            },
        ],
        "questions": [
            "Paint or coating application and process context",
            "Required brightness, whiteness, and impurity limits",
            "Preferred form: lumps or powder",
            "Trial quantity and expected monthly volume",
            "Destination port and preferred packing basis",
        ],
    },
    {
        "slug": "bentonite-supplier-india",
        "title": "Bentonite Supplier India: What We Offer",
        "eyebrow": "Bentonite / India Supply",
        "summary": "A direct bentonite supply guide for buyers comparing grades, application fit, and export handling from India.",
        "marquee_title": "Bentonite Supplier India",
        "seo_title": "Bentonite Supplier India | Grades, Quality Focus, and Export Supply",
        "meta_description": "Bentonite supply from India with sodium and calcium grades, quality focus points, and export support for industrial buyers.",
        "product_slug": "bentonite",
        "sections": [
            {
                "heading": "What we offer",
                "body": "If your requirement is bentonite from India, the first step is to align the right grade against the actual application rather than treat every bentonite discussion as interchangeable.",
                "points": [
                    "Supply includes sodium bentonite, calcium bentonite, and application-specific grades",
                    "Activated bleaching earth sits within the broader bentonite portfolio",
                    "Commercial discussion is aligned to application, grade type, and packing basis together",
                ],
            },
            {
                "heading": "Where the bentonite line is used",
                "body": "Bentonite performance depends heavily on the end use, so buyers usually need application fit clarified before pricing moves too far.",
                "points": [
                    "Drilling fluids for oil, gas, and HDD",
                    "Foundry and casting systems",
                    "Construction, sealing, and waterproofing work",
                    "Cat litter, absorbent use, and bleaching earth programs",
                ],
            },
            {
                "heading": "Quality focus before quotation",
                "body": "Technical alignment matters most when buyers need trial approval and repeat shipment performance to stay on the same basis.",
                "points": [
                    "Application requirement and sodium or calcium grade are aligned first",
                    "pH, liquid limit, viscosity, moisture, and filtrate loss are reviewed against end use",
                    "Packing and order volume are handled with the quality discussion",
                ],
            },
            {
                "heading": "Supply and export setup",
                "body": "Export execution becomes cleaner when sample, document, and shipment basis are kept in one buyer-facing conversation from the start.",
                "points": [
                    "Packing: 50 Kg bags and jumbo bags",
                    "Shipment mode: FCL",
                    "Export handling includes sample alignment, document alignment, and shipment planning from India",
                ],
            },
        ],
        "questions": [
            "Application and process context",
            "Required grade type: sodium, calcium, or application-specific",
            "Key acceptance parameters such as viscosity, pH, liquid limit, and filtrate loss",
            "Trial quantity and expected monthly volume",
            "Destination port and preferred packing basis",
        ],
    },
    {
        "slug": "fly-ash-exporter-from-india-bulk-shipment",
        "title": "Fly Ash Exporter from India Bulk Shipment: What We Supply",
        "eyebrow": "Fly Ash / Bulk Shipment",
        "summary": "A direct fly ash supply guide for buyers reviewing forms, application fit, and bulk shipment handling from India.",
        "marquee_title": "Fly Ash Bulk Shipment",
        "seo_title": "Fly Ash Exporter from India Bulk Shipment | Forms, Quality Focus, Export Supply",
        "meta_description": "Fly ash export supply from India with dry and bulk forms, quality focus points, and dispatch planning for import buyers.",
        "product_slug": "fly-ash",
        "sections": [
            {
                "heading": "What we offer",
                "body": "If your team is sourcing fly ash from India, the first step is to align the supply form and unloading setup before quotation and dispatch planning start.",
                "points": [
                    "Current supply discussions include dry fly ash and bulk fly ash",
                    "Application fit is aligned before commercial discussion",
                    "Packing, unloading, and shipment planning are handled together with the material conversation",
                ],
            },
            {
                "heading": "Where the fly ash line is used",
                "body": "Buyers usually need the replacement role and handling basis clarified early because fly ash decisions are tied closely to the receiving process.",
                "points": [
                    "Cement and concrete production",
                    "Fly ash bricks and blocks",
                    "Roads and embankments",
                    "Infrastructure-linked mineral substitution",
                ],
            },
            {
                "heading": "Quality focus before quotation",
                "body": "Technical alignment should happen before pricing so the quoted supply basis matches the replacement target and receiving setup.",
                "points": [
                    "Application and replacement target are aligned first",
                    "SiO2 and Al2O3 profile are reviewed against the required basis",
                    "Packing format, dispatch volume, and schedule are handled with the quality discussion",
                ],
            },
            {
                "heading": "Supply and export setup",
                "body": "For bulk-oriented fly ash buying, the shipment basis matters almost as much as the chemistry once dispatch planning begins.",
                "points": [
                    "Packing: jumbo bags",
                    "Shipment mode: FCL",
                    "Export handling includes sample alignment, document alignment, and shipment planning from India based on destination and order size",
                ],
            },
        ],
        "questions": [
            "End use and replacement target",
            "Required chemistry or acceptance basis",
            "Preferred packing and unloading setup",
            "Trial quantity and expected monthly volume",
            "Destination port and delivery timing",
        ],
    },
    {
        "slug": "copper-slag-supplier-for-shipyard-blasting",
        "title": "Copper Slag Supplier for Shipyard Blasting: What We Supply",
        "eyebrow": "Copper Slag / Shipyard Blasting",
        "summary": "A direct copper slag grit guide for shipyard blasting buyers reviewing sizes, performance focus, and export handling from India.",
        "marquee_title": "Copper Slag for Shipyard Blasting",
        "seo_title": "Copper Slag Supplier for Shipyard Blasting | Sizes and Export Supply",
        "meta_description": "Copper slag grit supply for shipyard blasting with available sizes, key performance focus points, and export handling support.",
        "product_slug": "copper-slag",
        "sections": [
            {
                "heading": "What we offer",
                "body": "If your requirement is copper slag for shipyard blasting, the first step is to align the required size range and blasting basis before quotation.",
                "points": [
                    "Current supply form is copper slag grit",
                    "Commercial discussion is aligned to blasting requirement and size range together",
                    "Packing and shipment planning are handled with the performance discussion",
                ],
            },
            {
                "heading": "Readily available sizes",
                "body": "Blasting buyers usually need the size range locked early because it directly affects surface preparation outcome and material consumption.",
                "points": [
                    "4.00-3.00 mm",
                    "3.00-2.36 mm",
                    "2.36-1.00 mm",
                    "1.00-0.50 mm, 0.50-0.212 mm, and 0.212 mm and below",
                ],
            },
            {
                "heading": "Performance focus before quotation",
                "body": "Technical alignment matters before PO so the blasting media basis stays clear through sample, quotation, and dispatch.",
                "points": [
                    "Sieve size distribution is aligned first",
                    "Density, hardness, and angular grain profile are reviewed against blasting need",
                    "Packing and shipment volume are handled together with the size discussion",
                ],
            },
            {
                "heading": "Supply and export setup",
                "body": "Shipyard blasting programs usually move faster when the size basis, cargo handling, and dispatch timeline are aligned early.",
                "points": [
                    "Packing: jumbo bags",
                    "Shipment mode: FCL",
                    "Export handling includes sample alignment, document alignment, and shipment planning from India based on destination and order size",
                ],
            },
        ],
        "questions": [
            "Required blasting size range",
            "Surface preparation requirement or blasting standard",
            "Trial quantity and expected monthly volume",
            "Destination port and preferred packing basis",
            "Required delivery timing",
        ],
    },
    {
        "slug": "industrial-salt-exporter",
        "title": "Industrial Salt Exporter: What We Supply",
        "eyebrow": "Industrial Salt / Export Supply",
        "summary": "A direct supply guide for buyers comparing industrial salt grades, packing basis, and export handling from India.",
        "marquee_title": "Industrial Salt Exporter",
        "seo_title": "Industrial Salt Exporter | Grades, Packing, and Export Supply from India",
        "meta_description": "Industrial salt export supply from India with multiple grades, quality focus points, and shipment support for import buyers.",
        "product_slug": "salt",
        "sections": [
            {
                "heading": "What we offer",
                "body": "If your team is looking for an industrial salt exporter, the first step is to align the required grade against the actual end use before quotation begins.",
                "points": [
                    "Current portfolio includes industrial salt, raw salt, crystalline salt, de-icing salt, and iodized grades",
                    "Commercial discussion is aligned to grade, purity direction, and shipment basis together",
                    "Packing and dispatch planning are handled in the same conversation as the grade discussion",
                ],
            },
            {
                "heading": "Where the salt line is used",
                "body": "Salt requirements shift by application, so buyers usually need grade direction and iodine basis settled before the offer is finalized.",
                "points": [
                    "Chemical and industrial processing",
                    "Water treatment applications",
                    "De-icing and utility use",
                    "Food processing and commercial supply",
                ],
            },
            {
                "heading": "Quality focus before quotation",
                "body": "Technical and commercial alignment matter most when buyers want the same grade basis to hold through trial and repeat shipments.",
                "points": [
                    "Required salt grade is aligned first",
                    "NaCl purity, iodine requirement, and grain size are reviewed against end use",
                    "Packing and monthly volume are handled with the quality discussion",
                ],
            },
            {
                "heading": "Supply and export setup",
                "body": "The order moves more cleanly when sample basis, document flow, and shipment plan are aligned before cargo planning starts.",
                "points": [
                    "Packing: 50 Kg bags and jumbo bags",
                    "Shipment mode: FCL",
                    "Export handling includes sample alignment, document alignment, and shipment planning from India based on destination and order size",
                ],
            },
        ],
        "questions": [
            "Required grade and end use",
            "NaCl purity and iodine requirement",
            "Required grain size and packing basis",
            "Trial quantity and expected monthly volume",
            "Destination port and delivery timing",
        ],
    },
    {
        "slug": "quartz-powder-supplier-for-engineered-stone",
        "title": "Quartz Powder Supplier for Engineered Stone: What We Supply",
        "eyebrow": "Quartz Powder / Engineered Stone",
        "summary": "A direct supply guide for engineered stone buyers reviewing available forms, sizes, quality focus, and export handling from India.",
        "marquee_title": "Quartz Powder for Engineered Stone",
        "seo_title": "Quartz Powder Supplier for Engineered Stone | Sizes, Specs, and Export Supply",
        "meta_description": "Quartz powder supply for engineered stone buyers from India, including available sizes, key quality focus points, and export handling support.",
        "product_slug": "quartz-sand-for-ceramics",
        "sections": [
            {
                "heading": "What we supply for engineered stone buyers",
                "body": "If your requirement is quartz powder for engineered stone, the first step is to align the right form against your process, not only the product name.",
                "points": [
                    "Supply options include quartz sand, quartz grits, and quartz powder.",
                    "Grade and size range are aligned to engineered stone end use before quotation.",
                    "Commercial discussion is tied to form, packing basis, and shipment planning together.",
                ],
            },
            {
                "heading": "Sizes available in the current supply range",
                "body": "Engineered stone buyers usually need both powder and controlled sized inputs depending on the production line and blend requirement.",
                "points": [
                    "0.1-0.4 mm, 0.3-0.7 mm, 0.6-1.2 mm, 1.2-2.5 mm, 2.5-4.0 mm, and 4.0-6.0 mm",
                    "200 mesh, 325 mesh, and 400 mesh",
                    "Custom size discussion available against application requirement",
                ],
            },
            {
                "heading": "Quality focus before quotation",
                "body": "For engineered stone programs, technical alignment needs to happen before pricing so the offer matches production needs.",
                "points": [
                    "SiO2 above 99.0 percent with low potassium profile",
                    "Form and grain or mesh size alignment before sample movement",
                    "Color, whiteness, and consistency discussion before commercial finalization",
                ],
            },
            {
                "heading": "Packing and export handling",
                "body": "Shipment planning matters as much as technical fit because engineered stone buyers often need the same basis to hold through trial and repeat orders.",
                "points": [
                    "Current packing basis: jumbo bags",
                    "Current shipment mode: FCL",
                    "Sample alignment, document alignment, and shipment planning are handled from India based on destination and order size",
                ],
            },
        ],
        "questions": [
            "End use, slab line, and process requirement",
            "Required form and size range: powder, grits, or sand",
            "SiO2 target, whiteness expectation, and key impurity limits",
            "Trial quantity and expected monthly volume",
            "Destination port and preferred packing basis",
        ],
    },
    {
        "slug": "silica-sand-exporter-from-india",
        "title": "Silica Sand Exporter from India: What We Supply",
        "eyebrow": "Silica Sand / Export Supply",
        "summary": "A direct supply guide for import buyers reviewing silica sand forms, application fit, quality focus points, and export handling from India.",
        "marquee_title": "Silica Sand Exporter from India",
        "seo_title": "Silica Sand Exporter from India | Forms, Quality Focus, and Export Supply",
        "meta_description": "Silica sand export supply from India with available forms, quality focus points, and shipment support for import buyers.",
        "product_slug": "silica-sand",
        "sections": [
            {
                "heading": "What we offer",
                "body": "If your team is sourcing silica sand from India, the first step is to align the right supply form against application and shipment basis.",
                "points": [
                    "Current silica line includes silica sand and silica flour",
                    "Supply discussion is aligned to end use before quotation",
                    "Packing and shipment planning are handled together with the grade discussion",
                ],
            },
            {
                "heading": "Where the silica line is used",
                "body": "Silica requirements change by process, so application fit needs to be clear before commercial discussion.",
                "points": [
                    "Glass manufacturing",
                    "Water filtration media",
                    "Foundry moulding systems",
                    "Paints, construction, and specialty fillers",
                ],
            },
            {
                "heading": "Quality focus before quotation",
                "body": "Technical alignment matters most when import teams want trials and repeat shipments to stay on the same basis.",
                "points": [
                    "Grain size, SiO2 content, and Fe2O3 requirement are aligned first",
                    "For glass use, Fe2O3 requirements can be discussed against the required grade",
                    "Packing and order volume are handled together with quality alignment",
                ],
            },
            {
                "heading": "Supply and export setup",
                "body": "The practical side of the order matters just as much as the material itself when shipment planning starts.",
                "points": [
                    "Packing: 50 Kg bags and jumbo bags",
                    "Shipment mode: FCL",
                    "Export handling includes sample alignment, document alignment, and shipment planning from India based on destination and order size",
                ],
            },
        ],
        "questions": [
            "End use: glass, foundry, filtration, construction, or another line",
            "Required grain size or mesh range",
            "SiO2 target and Fe2O3 limit for the intended process",
            "Trial quantity and expected monthly requirement",
            "Destination port, packing basis, and delivery timing",
        ],
    },
    {
        "slug": "how-to-check-tds-and-sample-coa-before-mineral-import",
        "title": "How to Check TDS and Sample COA Before You Place a Mineral Import Order",
        "eyebrow": "TDS / COA / Buyer Process",
        "summary": "A practical review framework for buyers before trial, quotation, and bulk dispatch.",
        "marquee_title": "How to Read TDS and Sample COA",
        "seo_title": "How to Review TDS and Sample COA for Mineral Imports | Jade Waves",
        "meta_description": "Step-by-step guide for import buyers to review technical data sheets and sample COA before placing mineral orders.",
        "product_slug": "silica-sand",
        "sections": [
            {
                "heading": "Use TDS to understand capability range",
                "body": "TDS shows the grade profile and typical range, but should be read with application context.",
                "points": [
                    "Check if the listed parameters match your process-critical checks.",
                    "Separate typical range from strict acceptance requirement.",
                    "Confirm form, size, and packing references in the same sheet.",
                ],
            },
            {
                "heading": "Use sample COA to validate trial relevance",
                "body": "A sample COA helps validate whether trial material is close to your buying basis.",
                "points": [
                    "Match sample COA to the exact grade being quoted.",
                    "Check testing basis and parameter naming consistency.",
                    "Clarify any value that sits near your rejection threshold.",
                ],
            },
            {
                "heading": "Convert documents into buying decisions",
                "body": "Documents are useful only when they are translated into a clear commercial and dispatch plan.",
                "points": [
                    "Lock technical acceptance points before final quote approval.",
                    "Align trial outcome with repeat-order specification.",
                    "Confirm dispatch documents and communication process early.",
                ],
            },
        ],
        "questions": [
            "Is this TDS matched to the same grade quoted to us?",
            "Can you share sample COA for the discussed mesh/form?",
            "How close is sample data to repeat shipment target?",
            "What is your process if one parameter drifts near limit?",
        ],
    },
]

CORE_BLOG_SLUGS = [
    "quartz-sand-supplier-india-vietnam-buyers-guide",
    "potassium-vs-sodium-feldspar-import-buyer-guide",
    "silica-sand-import-checklist-glass-foundry-filtration",
    "potassium-feldspar-supplier-for-ceramic-tiles",
    "quartz-powder-supplier-for-engineered-stone",
    "silica-sand-exporter-from-india",
    "how-to-check-tds-and-sample-coa-before-mineral-import",
]
BLOGS = [post for post in BLOGS if post["slug"] in CORE_BLOG_SLUGS]

CURRENT_BLOG_SLUGS = CORE_BLOG_SLUGS

LEGACY_REDIRECTS = {
    "silica-sand": "/products/silica-sand/",
    "silica-flour": "/products/silica-flour/",
    "quartz-sand-for-ceramics": "/products/quartz-sand-for-ceramics/",
    "bentonite": "/products/bentonite/",
    "kaolin--china-clay": "/products/kaolin--china-clay/",
    "talc": "/products/talc/",
    "feldspar": "/products/feldspar/",
    "potash-&-soda-feldspar": "/products/feldspar/",
    "potash-%26-soda-feldspar": "/products/feldspar/",
    "salt": "/products/salt/",
    "fly-ash": "/products/fly-ash/",
    "copper-slag": "/products/copper-slag/",
    "activated-bleaching-earth": "/products/",
    "blogs/f/activated-bleaching-earth": "/products/",
    "blogs/f/bentonite-suppliers-in-malaysia": "/products/",
    "blogs/f/silica-sand-maldives": "/products/silica-sand/",
    "blogs/f/silica-sand-suppliers-in-kenya": "/products/silica-sand/",
    "blogs/f/silica-sand-suppliers-in-mauritius-jade-waves-enterprise": "/products/silica-sand/",
    "about-us": "/industrial-minerals-exporter-india/",
    "contact-1": "/#contact",
    "faq": "/",
    "infrastructure": "/operations/",
    "blog/bentonite-grade-selection-guide-for-importers": "/blog/",
    "blog/industrial-salt-import-guide-gulf-buyers": "/blog/",
    "blog/kaolin-supplier-for-paint-industry": "/blog/",
    "blog/bentonite-supplier-india": "/blog/",
    "blog/fly-ash-exporter-from-india-bulk-shipment": "/blog/",
    "blog/copper-slag-supplier-for-shipyard-blasting": "/blog/",
    "blog/industrial-salt-exporter": "/blog/",
}


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def make_project_pages_safe(markup: str) -> str:
    base_bootstrap = dedent(
        f"""
        <script>
          window.__JWE_SITE_BASE_PATH__ = (function() {{
            var repoPath = "/{PROJECT_PAGES_REPO}";
            var pathname = window.location.pathname;
            if (pathname === repoPath || pathname.indexOf(repoPath + "/") === 0) {{
              return repoPath;
            }}
            return "";
          }})();
          var baseHref = window.__JWE_SITE_BASE_PATH__ ? window.__JWE_SITE_BASE_PATH__ + "/" : "/";
          document.write('<base href="' + baseHref + '">');
        </script>
        """
    ).strip()
    safe_markup = markup.replace(
        "<head>",
        f"<head>\n                {base_bootstrap}",
        1,
    )
    for source, target in (
        ('href="/#', 'href="./#'),
        ('href="/"', 'href="./"'),
        ('href="/', 'href="'),
        ('src="/', 'src="'),
        ('poster="/', 'poster="'),
        ('srcset="/', 'srcset="'),
    ):
        safe_markup = safe_markup.replace(source, target)
    # Every candidate must follow the base element on GitHub project hosting,
    # not just the first URL in the attribute.
    safe_markup = re.sub(
        r'srcset="([^"]+)"',
        lambda match: 'srcset="' + ', '.join(
            candidate.strip()[1:] if candidate.strip().startswith('/')
            and not candidate.strip().startswith('//') else candidate.strip()
            for candidate in match.group(1).split(',')
        ) + '"',
        safe_markup,
    )
    safe_markup = safe_markup.replace('<head>', f'<head>\n<noscript><base href="{BASE_URL}/"></noscript>', 1)
    return safe_markup


def render_redirect_page(legacy_path: str, target_path: str) -> str:
    legacy_url = f"{BASE_URL}/{legacy_path.strip('/')}/"
    target_url = f"{BASE_URL}{target_path}"
    target_label = target_path.strip("/") or "homepage"
    return dedent(
        f"""
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>Moved | {escape(CONTACT["company"])}</title>
            <meta name="robots" content="noindex, follow" />
            <meta name="description" content="This page has moved to {escape(target_label)}." />
            <link rel="canonical" href="{escape(target_url)}" />
            <meta http-equiv="refresh" content="0; url={escape(target_url)}" />
            <script>
              window.location.replace({json.dumps(target_url)});
            </script>
          </head>
          <body>
            <main>
              <h1>This page has moved</h1>
              <p>
                The Jade Waves Enterprise page at
                <a href="{escape(legacy_url)}">{escape(legacy_url)}</a>
                now lives at
                <a href="{escape(target_url)}">{escape(target_url)}</a>.
              </p>
            </main>
          </body>
        </html>
        """
    ).strip()


def analytics_snippet() -> str:
    if not GA4_MEASUREMENT_ID:
        return ""
    return dedent(
        f"""
        <script async src="https://www.googletagmanager.com/gtag/js?id={GA4_MEASUREMENT_ID}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{GA4_MEASUREMENT_ID}');
        </script>
        """
    ).strip()


def recaptcha_script_markup() -> str:
    if not RECAPTCHA_SITE_KEY:
        return ""
    return '<script src="https://www.google.com/recaptcha/api.js" async defer></script>'


def page_shell(title: str, meta_description: str, path: str, body: str, schema: list[dict], body_class: str = "") -> str:
    page_url = f"{BASE_URL}{path}"
    # The project-pages base element points to the site root, so bare fragment
    # links need the current page path to stay on product and article pages.
    body = body.replace('href="#', f'href="{path}#')
    body = re.sub(r'<main\b([^>]*)>', lambda match: '<main' + match.group(1) +
                  ('' if 'id=' in match.group(1) else ' id="main-content"') +
                  ('' if 'tabindex=' in match.group(1) else ' tabindex="-1"') + '>', body, count=1)
    body = enhance_images(body)
    schema_blob = json.dumps(schema, ensure_ascii=False)
    tracking_markup = analytics_snippet()
    recaptcha_markup = recaptcha_script_markup()
    return make_project_pages_safe(
        dedent(
            f"""
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>{escape(title)}</title>
                <meta name="description" content="{escape(meta_description)}" />
                <meta name="robots" content="index,follow" />
                <link rel="canonical" href="{escape(page_url)}" />
                <meta property="og:title" content="{escape(title)}" />
                <meta property="og:description" content="{escape(meta_description)}" />
                <meta property="og:type" content="website" />
                <meta property="og:url" content="{escape(page_url)}" />
                <meta property="og:site_name" content="{escape(CONTACT["company"])}" />
                <meta property="og:image" content="{BASE_URL}/assets/jade-waves-logo-transparent.png" />
                <link rel="preconnect" href="https://fonts.googleapis.com" />
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
                <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet" />
                <link rel="stylesheet" href="/styles.css?v={BUILD_VERSION}" />
                {tracking_markup}
                {recaptcha_markup}
                <script type="application/ld+json">{schema_blob}</script>
                <script defer src="/script.js?v={BUILD_VERSION}"></script>
              </head>
              <body class="antialiased {escape(body_class)}">
                {body}
              </body>
            </html>
            """
        ).strip()
    )


PRODUCT_VISUALS = {
    "silica-sand": {
        "hero": "/assets/silica-sand-samples.png",
        "thumb": "/assets/silica-sand-samples.png",
        "alt": "Silica sand size samples in laboratory trays",
    },
    "silica-flour": {
        "hero": "/assets/silica-flour-visual.webp",
        "thumb": "/assets/silica-flour-visual.webp",
        "alt": "Silica flour powder product image",
    },
    "quartz-sand-for-ceramics": {
        "hero": "/assets/quartz-sand-detail-visual.webp",
        "thumb": "/assets/quartz-lumps-3-visual.webp",
        "alt": "Quartz sand and quartz mineral material detail",
    },
    "bentonite": {
        "hero": "/assets/bentonite-sample-reference.png",
        "thumb": "/assets/bentonite-sample-reference.png",
        "alt": "Bentonite powder sample in a glass dish",
    },
    "kaolin--china-clay": {
        "hero": "/assets/china-clay-powder.png",
        "thumb": "/assets/china-clay-lumps.png",
        "alt": "China clay and kaolin material image",
    },
    "talc": {
        "hero": "/assets/talc-powder.png",
        "thumb": "/assets/talc-chips.png",
        "alt": "Talc powder product image",
    },
    "feldspar": {
        "hero": "/assets/feldspar-lumps-visual.webp",
        "thumb": "/assets/feldspar-lumps-visual.webp",
        "alt": "Feldspar mineral product image",
    },
    "salt": {
        "hero": "/assets/salt-sample-reference.png",
        "thumb": "/assets/salt-sample-reference.png",
        "alt": "Industrial salt crystals in a wooden scoop",
    },
    "fly-ash": {
        "hero": "/assets/stock-fly-ash-clean.png",
        "thumb": "/assets/stock-fly-ash-clean.png",
        "alt": "Fly ash powder product image",
    },
    "copper-slag": {
        "hero": "/assets/copper-slag-processing.png",
        "thumb": "/assets/copper-slag-processing.png",
        "alt": "Copper slag abrasive material image",
    },
    "rubber-granules": {
        "hero": "/assets/rubber-granules-samples.png",
        "thumb": "/assets/rubber-granules-samples.png",
        "alt": "Colored rubber granule samples for sports and safety surfaces",
    },
}


TDS_BY_SLUG = {
    "silica-sand": "/assets/tds/silica-sand-technical-data-sheet.pdf",
    "silica-flour": "/assets/tds/silica-flour-technical-data-sheet.pdf",
    "quartz-sand-for-ceramics": "/assets/tds/quartz-sand-technical-data-sheet.pdf",
    "bentonite": "/assets/tds/bentonite-technical-data-sheet.pdf",
    "kaolin--china-clay": "/assets/tds/china-clay-technical-data-sheet.pdf",
    "talc": "/assets/tds/talc-technical-data-sheet.pdf",
    "feldspar": "/assets/tds/feldspar-technical-data-sheet.pdf",
    "salt": "/assets/tds/salt-technical-data-sheet.pdf",
    "fly-ash": "/assets/tds/fly-ash-technical-data-sheet.pdf",
    "copper-slag": "/assets/tds/copper-slag-technical-data-sheet.pdf",
}


def product_visual(slug: str, kind: str = "hero") -> tuple[str, str]:
    visual = PRODUCT_VISUALS.get(slug, {})
    src = visual.get(kind) or visual.get("hero") or "/assets/optimized/quarry-quartz.jpg"
    alt = visual.get("alt") or "Industrial mineral material visual"
    return src, alt


def sentence_fragment(text: str) -> str:
    clean = " ".join(text.split())
    if not clean:
        return clean
    first_word = clean.split()[0].strip(",:;()/-")
    if any(ch.isdigit() for ch in first_word) or sum(ch.isupper() for ch in first_word) >= 2:
        return clean
    return clean[0].lower() + clean[1:]


def render_faq(product: dict) -> tuple[str, list[dict]]:
    booking_points = product.get("booking_points", product["specs"])
    faqs = [
        {
            "q": f"What applications is {product['name']} supplied for?",
            "a": f"{product['name']} is supplied for {sentence_fragment(product['applications'][0])}, {sentence_fragment(product['applications'][1])}, and {sentence_fragment(product['applications'][2])}, with grade and sizing aligned to the end use.",
        },
        {
            "q": f"What should be confirmed before ordering {product['name']}?",
            "a": f"Confirm {sentence_fragment(booking_points[0])}, {sentence_fragment(booking_points[1])}, {sentence_fragment(booking_points[2])}, and {sentence_fragment(booking_points[3])} so pricing, sampling, and dispatch can be aligned correctly.",
        },
        {
            "q": f"How is {product['name']} handled for export?",
            "a": f"Supply formats include {product['packing']}. Jade Waves aligns samples, export documents, and shipment planning from India to suit the destination and order size.",
        },
    ]
    markup = "".join(
        dedent(
            f"""
            <details class="faq-item" data-reveal>
              <summary>{escape(item["q"])}</summary>
              <p>{escape(item["a"])}</p>
            </details>
            """
        ).strip()
        for item in faqs
    )
    schema = [
        {
            "@type": "Question",
            "name": item["q"],
            "acceptedAnswer": {"@type": "Answer", "text": item["a"]},
        }
        for item in faqs
    ]
    return markup, schema


def nav_html() -> str:
    return material_layout.render_nav(globals())


def footer_html() -> str:
    return material_layout.render_footer(globals())


def form_block(product_name: str = "") -> str:
    return material_layout.render_form(globals(), product_name)


def render_homepage() -> str:
    return material_pages.render_homepage(globals())


def render_products_index() -> str:
    return material_pages.render_products_index(globals())


def render_product_page(product: dict) -> str:
    return material_pages.render_product_page(globals(), product)


def render_export_markets_page() -> str:
    return material_pages.render_export_markets_page(globals())


def render_exporter_profile_page() -> str:
    return material_pages.render_exporter_profile_page(globals())


def render_ceo_page() -> str:
    return material_pages.render_ceo_page(globals())


def render_blog_index_page() -> str:
    return material_pages.render_blog_index_page(globals())


def render_blog_post_page(post: dict) -> str:
    return material_pages.render_blog_post_page(globals(), post)


STYLES = (ROOT / "templates" / "material-ledger.css").read_text(encoding="utf-8").strip()
SCRIPT = (ROOT / "templates" / "material-ledger.js").read_text(encoding="utf-8").strip()


def render_robots() -> str:
    return dedent(
        f"""
        User-agent: *
        Allow: /

        Sitemap: {BASE_URL}/sitemap.xml
        """
    ).strip()


def render_sitemap() -> str:
    # Publish only routes assembled into the production artifact. Workspace
    # previews and other applications must not leak into the public sitemap.
    urls = ['/', '/products/', '/blog/', '/operations/', '/export-markets/',
            '/hear-from-ceo/', '/industrial-minerals-exporter-india/']
    urls += [f'/products/{product["slug"]}/' for product in PRODUCTS]
    urls += [f'/blog/{post["slug"]}/' for post in BLOGS]
    urls += [f'/{slug}/' for slug in material_support.POLICIES]
    entries = "\n".join(
        f"  <url><loc>{BASE_URL}{path}</loc><lastmod>{TODAY}</lastmod></url>"
        for path in sorted(urls)
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n"
        "</urlset>"
    )


def main() -> None:
    write(ROOT / "styles.css", STYLES)
    write(ROOT / "script.js", SCRIPT)
    write(ROOT / "index.html", render_homepage())
    write(ROOT / "blog" / "index.html", render_blog_index_page())
    for blog_post in BLOGS:
      write(ROOT / "blog" / blog_post["slug"] / "index.html", render_blog_post_page(blog_post))
    write(ROOT / "hear-from-ceo" / "index.html", render_ceo_page())
    write(ROOT / "export-markets" / "index.html", render_export_markets_page())
    write(ROOT / "industrial-minerals-exporter-india" / "index.html", render_exporter_profile_page())
    write(ROOT / "operations" / "index.html", material_support.render_operations_page(globals()))
    for policy_slug in material_support.POLICIES:
      write(ROOT / policy_slug / "index.html", material_support.render_policy_page(globals(), policy_slug))
    write(ROOT / "products" / "index.html", render_products_index())
    for product in PRODUCTS:
      write(ROOT / "products" / product["slug"] / "index.html", render_product_page(product))
    for legacy_path, target_path in LEGACY_REDIRECTS.items():
      write(ROOT / legacy_path / "index.html", render_redirect_page(legacy_path, target_path))
    write(ROOT / "robots.txt", render_robots())
    write(ROOT / "sitemap.xml", render_sitemap())


if __name__ == "__main__":
    main()
