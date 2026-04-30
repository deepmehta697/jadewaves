from __future__ import annotations

import json
from datetime import date
from html import escape
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).parent
BASE_URL = "https://jadewavesenterprise.com"
PROJECT_PAGES_REPO = "jadewaves"
TODAY = date.today().isoformat()
CEO_LINKEDIN_URL = "https://www.linkedin.com/in/deep-mehta-034230226/"
GA4_MEASUREMENT_ID = "G-9BRL4JKNN6"

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
        "Quartz sand, feldspar, and silica sand for bodies, tiles, glaze systems, and ceramic process buying.",
    ),
    (
        "Construction",
        "Silica sand and quartz inputs for construction-linked and engineered-stone-adjacent mineral demand.",
    ),
    (
        "Chemicals",
        "Salt, silica, and selected mineral inputs for processing, treatment, and utility-led operations.",
    ),
    (
        "Drilling",
        "Bentonite grades for drilling programs that rely on stable swelling, viscosity, and moisture control.",
    ),
    (
        "Agriculture",
        "Selected minerals for carrier, absorbent, and process-linked agricultural use.",
    ),
    (
        "Foundry",
        "Silica sand for moulding systems that depend on repeatable sizing and dependable export handling.",
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
        "seo_title": "Quartz Supplier from India | Quartz Sand, Grits & Powder Exporter | Jade Waves Enterprise",
        "meta_description": "Quartz supplier from India for ceramics, glass, and engineered stone buyers needing quartz sand, quartz grits, and quartz powder supply across Vietnam, Thailand, Malaysia, UAE, and Saudi Arabia.",
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
]

PACKING_BY_SLUG = {
    "silica-sand": "50 Kg/Jumbo Bags",
    "silica-flour": "50 Kg/Jumbo Bags",
    "quartz-sand-for-ceramics": "Jumbo Bags",
    "bentonite": "50 Kg/Jumbo Bags",
    "kaolin--china-clay": "50 Kg/Jumbo Bags",
    "fly-ash": "Jumbo Bags",
    "copper-slag": "Jumbo Bags",
}

for product in PRODUCTS:
    packing = PACKING_BY_SLUG.get(product["slug"])
    if packing:
        product["packing"] = packing

PRODUCTS_BY_SLUG = {product["slug"]: product for product in PRODUCTS}

ACTIVE_PRODUCT_SLUGS = ["silica-sand", "quartz-sand-for-ceramics", "feldspar"]
REDIRECT_PRODUCT_TARGETS = {
    "bentonite": "/products/",
    "copper-slag": "/products/",
    "fly-ash": "/products/",
    "kaolin--china-clay": "/products/",
    "salt": "/products/",
    "silica-flour": "/products/silica-sand/",
    "talc": "/products/",
}
ACTIVE_PRODUCTS = [PRODUCTS_BY_SLUG[slug] for slug in ACTIVE_PRODUCT_SLUGS]
ACTIVE_PRODUCT_SLUG_SET = set(ACTIVE_PRODUCT_SLUGS)

PRODUCT_FAMILIES = [
    {
        "id": "silica-quartz-feldspar",
        "name": "Silica, Quartz & Feldspar",
        "copy": "Purity-led grades for glass, ceramics, filtration, and engineered stone.",
        "best_for": ["Glass", "Ceramics", "Filtration", "Engineered Stone"],
        "products": ACTIVE_PRODUCT_SLUGS,
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
                    "Current silica line is focused on silica sand supply for active buyer programs",
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

CURRENT_BLOG_SLUGS = [
    "quartz-sand-supplier-india-vietnam-buyers-guide",
    "potassium-vs-sodium-feldspar-import-buyer-guide",
    "silica-sand-import-checklist-glass-foundry-filtration",
    "potassium-feldspar-supplier-for-ceramic-tiles",
    "quartz-powder-supplier-for-engineered-stone",
    "silica-sand-exporter-from-india",
    "how-to-check-tds-and-sample-coa-before-mineral-import",
]

REDIRECT_BLOG_TARGETS = {
    "bentonite-grade-selection-guide-for-importers": "/blog/",
    "bentonite-supplier-india": "/blog/",
    "copper-slag-supplier-for-shipyard-blasting": "/blog/",
    "fly-ash-exporter-from-india-bulk-shipment": "/blog/",
    "industrial-salt-exporter": "/blog/",
    "industrial-salt-import-guide-gulf-buyers": "/blog/",
    "kaolin-supplier-for-paint-industry": "/blog/",
}


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def make_project_pages_safe(markup: str) -> str:
    return markup


def nav_html() -> str:
    return dedent(
        f"""
        <header class="site-header" data-header>
          <div class="site-header__inner">
            <a class="brand-mark" href="/" aria-label="{escape(CONTACT["company"])} home">
              <img src="/assets/jade-waves-logo-transparent.png" alt="{escape(CONTACT["company"])} logo" />
            </a>
            <nav class="desktop-nav" aria-label="Primary">
              <a href="/#about">About</a>
              <a href="/products/">Products</a>
              <a href="/operations/">Operations</a>
              <a href="/blog/">Blog</a>
              <a href="/export-markets/">Markets</a>
              <a href="/#contact">Contact</a>
            </nav>
            <div class="header-actions">
              <a class="button button--dark button--compact" href="/#contact" data-set-request="Quote">Request Quote</a>
              <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" data-menu-toggle>
                Menu
              </button>
            </div>
          </div>
          <div class="mobile-menu" id="mobile-menu" data-mobile-menu hidden>
            <a href="/#about">About</a>
            <a href="/products/">Products</a>
            <a href="/operations/">Operations</a>
            <a href="/blog/">Blog</a>
            <a href="/export-markets/">Markets</a>
            <a href="/#contact">Contact</a>
          </div>
        </header>
        """
    ).strip()


def footer_html() -> str:
    return dedent(
        f"""
        <footer class="site-footer">
          <div class="shell site-footer__inner">
            <div>
              <p class="footer-label">{escape(CONTACT["company"])}</p>
              <p class="footer-copy">Industrial minerals, supplied with more control.</p>
            </div>
            <div class="footer-grid">
              <div>
                <p class="footer-heading">Contact</p>
                <a href="tel:{escape(CONTACT["phone"])}">{escape(CONTACT["phone"])}</a>
                <a href="mailto:{escape(CONTACT["sales_email"])}">{escape(CONTACT["sales_email"])}</a>
              </div>
              <div>
                <p class="footer-heading">Navigate</p>
                <a href="/">Home</a>
                <a href="/products/">Products</a>
                <a href="/operations/">Operations</a>
                <a href="/blog/">Blog</a>
                <a href="/hear-from-ceo/">Hear from Our CEO</a>
                <a href="/export-markets/">Export Markets</a>
                <a href="/#contact">Contact</a>
              </div>
            </div>
          </div>
          <div class="shell site-footer__meta">
            <p>&copy; <span data-current-year>2026</span> {escape(CONTACT["company"])}. All rights reserved.</p>
          </div>
        </footer>
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


def page_shell(title: str, meta_description: str, path: str, body: str, schema: list[dict], body_class: str = "") -> str:
    page_url = f"{BASE_URL}{path}"
    schema_blob = json.dumps(schema, ensure_ascii=False)
    tracking_markup = analytics_snippet()
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
                <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
                <link rel="stylesheet" href="/styles.css" />
                {tracking_markup}
                <script type="application/ld+json">{schema_blob}</script>
                <script defer src="/script.js"></script>
              </head>
              <body class="antialiased {escape(body_class)}">
                {body}
              </body>
            </html>
            """
        ).strip()
    )


def render_redirect_page(title: str, description: str, from_path: str, to_path: str) -> str:
    target_url = f"{BASE_URL}{to_path}"
    return dedent(
        f"""
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>{escape(title)}</title>
            <meta name="description" content="{escape(description)}" />
            <meta name="robots" content="noindex,follow" />
            <link rel="canonical" href="{escape(target_url)}" />
            <meta http-equiv="refresh" content="0; url={escape(target_url)}" />
            <script>window.location.replace({json.dumps(target_url)});</script>
            <link rel="stylesheet" href="/styles.css" />
          </head>
          <body class="antialiased page-redirect">
            <main class="shell" style="padding: 6rem 1.5rem;">
              <p class="section-label">Redirecting</p>
              <h1>{escape(title)}</h1>
              <p>{escape(description)}</p>
              <p><a href="{escape(to_path)}">Continue to the current page</a></p>
            </main>
          </body>
        </html>
        """
    ).strip()


def form_block(product_name: str = "") -> str:
    product_field = (
        f'<input type="text" name="product" value="{escape(product_name)}" readonly />'
        if product_name
        else product_select()
    )
    return dedent(
        f"""
        <div class="contact-shell" id="contact">
          <div class="contact-copy" data-reveal>
            <p class="section-label">Contact</p>
            <h2>Start the inquiry.</h2>
            <p>
              Share the product, end use, destination, and expected volume. We’ll align fit, packing, and shipment terms from there.
            </p>
            <div class="contact-details">
              <a href="mailto:{escape(CONTACT["sales_email"])}">{escape(CONTACT["sales_email"])}</a>
              <a href="tel:{escape(CONTACT["phone"])}">{escape(CONTACT["phone"])}</a>
            </div>
          </div>
          <form class="inquiry-form" data-inquiry-form data-reveal>
            <div class="form-grid">
              <label>
                <span>Request Type</span>
                <select name="request_type">
                  <option>Quote</option>
                  <option>Sample</option>
                  <option>General Inquiry</option>
                </select>
              </label>
              <label>
                <span>Product</span>
                {product_field}
              </label>
              <label>
                <span>Name</span>
                <input type="text" name="name" placeholder="Your name" required />
              </label>
              <label>
                <span>Company</span>
                <input type="text" name="company" placeholder="Company name" />
              </label>
              <label>
                <span>Email</span>
                <input type="email" name="email" placeholder="you@company.com" required />
              </label>
              <label>
                <span>Phone</span>
                <input type="text" name="phone" placeholder="+91 / country code" />
              </label>
              <label>
                <span>Application</span>
                <input type="text" name="application" placeholder="End use or industry" />
              </label>
              <label>
                <span>Volume</span>
                <input type="text" name="volume" placeholder="Trial / monthly volume" />
              </label>
              <label>
                <span>Packing Size</span>
                <input type="text" name="packing_size" placeholder="50 Kg bags / Jumbo bags / bulk" />
              </label>
              <label class="form-grid__wide">
                <span>Requirement</span>
                <textarea name="notes" rows="4" placeholder="Share grade, packing, destination, or any spec points that matter."></textarea>
              </label>
            </div>
            <div class="form-actions">
              <button class="button button--dark" type="submit">Send Inquiry</button>
              <p class="form-note" data-form-note>Send the form directly. We'll review the requirement and respond by email.</p>
            </div>
          </form>
        </div>
        """
    ).strip()


def product_select() -> str:
    options = ['<option value="">Select product</option>']
    for product in ACTIVE_PRODUCTS:
        options.append(f'<option value="{escape(product["name"])}">{escape(product["name"])}</option>')
    return "<select name=\"product\">" + "".join(options) + "</select>"


def related_links(slugs: list[str]) -> str:
    links = []
    for slug in slugs:
        if slug not in ACTIVE_PRODUCT_SLUG_SET:
            continue
        product = PRODUCTS_BY_SLUG[slug]
        links.append(
            f'<a href="/products/{product["slug"]}/">{escape(product["name"])}</a>'
        )
    return "".join(links)


def natural_join(items: list[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return f"{', '.join(items[:-1])}, and {items[-1]}"


def compact_label(text: str, max_chars: int = 24) -> str:
    clean = " ".join(text.split())
    if len(clean) <= max_chars:
        return clean
    trimmed = clean[:max_chars].rsplit(" ", 1)[0].strip()
    return (trimmed or clean[:max_chars]).rstrip(",/") + "..."


def sentence_fragment(text: str) -> str:
    clean = " ".join(text.split())
    if not clean:
        return clean
    first_word = clean.split()[0].strip(",:;()/-")
    if any(ch.isdigit() for ch in first_word) or sum(ch.isupper() for ch in first_word) >= 2:
        return clean
    return clean[0].lower() + clean[1:]


def render_homepage() -> str:
    proof_items = [
        ("Port Access", CONTACT["port"]),
        ("Commercial Terms", "FOB / CIF / CNF"),
        ("Load Mode", "FCL"),
        ("Sampling", "Sample-first flow"),
    ]
    operating_points = [
        (
            "01",
            "Start with the spec",
            "Application, chemistry, sizing, moisture, and packing are aligned before pricing starts to drift.",
        ),
        (
            "02",
            "Align the commercials",
            "Shipment basis, sample flow, documents, and payment expectations are made clear early.",
        ),
        (
            "03",
            "Keep the flow visible",
            "Loading, documents, and shipment updates stay in view until the cargo moves.",
        ),
        (
            "04",
            "Built to be reordered",
            "The goal is simple: make the first order clear and the next one easier.",
        ),
    ]
    family_blocks = []
    for index, family in enumerate(PRODUCT_FAMILIES, start=1):
        family_count = len(family["products"])
        count_label = f"{family_count} product" if family_count == 1 else f"{family_count} products"
        family_products = "".join(
            f'''
            <a class="home-family-row__product" href="/products/{escape(slug)}/">
              <span>{escape(PRODUCTS_BY_SLUG[slug]["name"])}</span>
              <em aria-hidden="true">→</em>
            </a>
            '''
            for slug in family["products"]
        )
        family_blocks.append(
            dedent(
                f"""
                <article class="home-family-row" data-reveal>
                  <span class="home-family-row__index">{index:02d}</span>
                  <div class="home-family-row__main">
                    <p class="home-family-row__count">{escape(count_label)}</p>
                    <h3><a class="home-family-row__family-link" href="/products/#{escape(family["id"])}">{escape(family["name"])}</a></h3>
                    <p>{escape(family["copy"])}</p>
                    <div class="home-family-row__products">{family_products}</div>
                  </div>
                  <a class="home-family-row__cta" href="/products/#{escape(family["id"])}">View family</a>
                </article>
                """
            ).strip()
        )
    industry_blocks = []
    for name, copy in INDUSTRIES:
        industry_blocks.append(
            dedent(
                f"""
                <article class="industry-line" data-reveal>
                  <h3>{escape(name)}</h3>
                  <p>{escape(copy)}</p>
                </article>
                """
            ).strip()
        )
    process_steps = [
        ("01", "Inquiry", "Share the product, application, destination, and target volume."),
        ("02", "Quote or sample", "Pricing or sampling is aligned to the right grade, packing, and end use."),
        ("03", "Documentation", "Commercial terms, packing, and export documents are locked before loading."),
        ("04", "Dispatch", "Shipment updates continue through loading, vessel planning, and cargo movement."),
    ]
    process_markup = "".join(
        dedent(
            f"""
            <article class="process-step" data-reveal>
              <span>{number}</span>
              <div class="process-step__body">
                <h3>{escape(title)}</h3>
                <p>{escape(copy)}</p>
              </div>
            </article>
            """
        ).strip()
        for number, title, copy in process_steps
    )
    operating_markup = "".join(
        dedent(
            f"""
            <article class="home-ledger-row" data-reveal>
              <span>{escape(number)}</span>
              <div>
                <strong>{escape(title)}</strong>
                <p>{escape(copy)}</p>
              </div>
            </article>
            """
        ).strip()
        for number, title, copy in operating_points
    )
    guide_links_once = "".join(
        f'<a class="buyer-guide-pill" href="/blog/">{escape(post.get("marquee_title", post["title"]))}</a>'
        for post in BLOGS
        if post["slug"] in CURRENT_BLOG_SLUGS
    )
    guide_links_markup = guide_links_once + guide_links_once
    home_body = dedent(
        f"""
        {nav_html()}
        <main>
          <section class="hero hero--home">
            <div class="hero__strata" aria-hidden="true">
              <span class="strata strata--a"></span>
              <span class="strata strata--b"></span>
              <span class="strata strata--c"></span>
              <span class="route-line route-line--hero"></span>
            </div>
            <div class="shell home-hero">
              <div class="hero-copy hero-copy--home" data-reveal>
                <h1>Manufacturer-backed mineral<br />supply for global buyers.</h1>
                <p class="hero-text">
                  Industrial minerals exported from India with clear specs, direct communication, and visible dispatch.
                </p>
                <div class="hero-actions">
                  <a class="button button--light" href="/products/">Explore Portfolio</a>
                  <a class="button button--ghost" href="/#contact" data-set-request="Quote">Request Quote</a>
                  <a class="button button--ghost" href="/#contact" data-set-request="Sample">Request Sample</a>
                </div>
                <p class="hero-subline">Fast Response. Reliable Supply. No Surprises.</p>
              </div>
              <div class="home-poster" data-reveal data-parallax="0.14">
                <div class="home-poster__surface">
                  <span class="ore-slab ore-slab--a"></span>
                  <span class="ore-slab ore-slab--b"></span>
                  <span class="ore-slab ore-slab--c"></span>
                  <div class="home-poster__summary">
                    <p class="home-poster__eyebrow">At a glance</p>
                    <strong>Right material. Right detail. Ready to move.</strong>
                    <p>Specification-led supply with packing and shipment aligned before the cargo moves.</p>
                  </div>
                  <div class="home-poster__metrics">
                    <article class="home-metric">
                      <span>Specification Focus</span>
                      <strong>Chemistry, sizing, and packing</strong>
                    </article>
                    <article class="home-metric">
                      <span>Packing</span>
                      <strong>50 Kg/Jumbo Bags</strong>
                    </article>
                    <article class="home-metric">
                      <span>Shipment</span>
                      <strong>FCL</strong>
                    </article>
                  </div>
                  <span class="route-line route-line--visual"></span>
                </div>
              </div>
            </div>
            <div class="shell proof-strip" data-reveal>
              {"".join(
                  dedent(
                      f'''
                      <article class="proof-strip__item">
                        <span class="proof-strip__eyebrow">{escape(label)}</span>
                        <strong>{escape(value)}</strong>
                      </article>
                      '''
                  ).strip()
                  for label, value in proof_items
              )}
            </div>
          </section>

          <section class="section-block" id="about">
            <div class="shell section-shell">
              <div class="home-ledger">
                <div class="home-ledger__intro" data-reveal>
                  <p class="section-kicker">Clarity, end to end.</p>
                  <h2>The details are handled early.</h2>
                    <p>
                      The material, the spec, the packing, the documents, the shipment. The work is set up for import buyers across Southeast Asia, the Gulf, Mauritius, and Maldives to feel settled before cargo moves.
                    </p>
                </div>
                <div class="home-ledger__rows">
                  {operating_markup}
                </div>
              </div>
            </div>
          </section>

          <section class="section-block section-block--contrast">
            <div class="shell section-shell">
              <div class="section-topline section-topline--stack" data-reveal>
                <div class="section-topline__copy">
                  <p class="section-kicker">Material families</p>
                  <h2>Find the right family first.</h2>
                </div>
                <a class="section-link" href="/products/">Explore portfolio</a>
              </div>
              <div class="home-family-list">
                {''.join(family_blocks)}
              </div>
            </div>
          </section>

          <section class="section-block section-block--contrast" id="industries">
            <div class="shell section-shell">
              <div class="home-split home-split--stack">
                <article class="home-split__panel" data-reveal>
                  <p class="section-label">Industries</p>
                  <h2>Specified into the work that keeps moving.</h2>
                  <p>The range is built around glass, ceramics, construction, chemicals, drilling, agriculture, and foundry demand.</p>
                  <div class="industry-rail">
                    {''.join(industry_blocks)}
                  </div>
                </article>
                <article class="home-split__panel" id="process" data-reveal>
                  <p class="section-label">Process</p>
                  <h2>From inquiry to dispatch.</h2>
                  <p>Short steps. Clean documents. One visible export flow.</p>
                  <div class="home-process-list">
                    {process_markup}
                  </div>
                </article>
              </div>
            </div>
          </section>

          <section class="section-block" id="countries-served">
            <div class="shell section-shell">
              <div class="corridor-stage">
                <div class="corridor-stage__top" data-reveal>
                  <div class="corridor-stage__intro">
                    <p class="section-label">Countries Served</p>
                    <h2>Countries we are currently exporting to from India.</h2>
                    <p>These lanes group the countries where Jade Waves is already moving cargo and handling live export requirements from the same India origin point.</p>
                  </div>
                </div>
                <div class="corridor-stage__body">
                  <article class="corridor-stage__hub" data-reveal>
                    <p class="corridor-stage__eyebrow">Origin</p>
                    <div class="corridor-stage__hub-mark" aria-hidden="true">
                      <span class="corridor-stage__hub-ring corridor-stage__hub-ring--outer"></span>
                      <span class="corridor-stage__hub-ring corridor-stage__hub-ring--inner"></span>
                      <span class="corridor-stage__hub-core"></span>
                    </div>
                    <h3>India manufacturing hub</h3>
                    <p>Plant handling, packing, and dispatch flow outward from one origin before cargo splits into country groups.</p>
                  </article>
                  <div class="corridor-stage__lanes" data-corridor-stage>
                    <button class="corridor-lane is-active" type="button" data-corridor-item aria-pressed="true">
                      <span class="corridor-lane__rail" aria-hidden="true">
                        <span class="corridor-lane__track"></span>
                        <span class="corridor-lane__glow"></span>
                        <span class="corridor-lane__ship"></span>
                        <span class="corridor-lane__terminal"></span>
                      </span>
                      <span class="corridor-lane__card">
                        <span class="corridor-lane__meta">01 · Gulf</span>
                        <strong>Gulf</strong>
                        <span class="corridor-lane__countries">UAE, Saudi Arabia, Oman, Kuwait, Qatar</span>
                      </span>
                    </button>
                    <button class="corridor-lane" type="button" data-corridor-item aria-pressed="false">
                      <span class="corridor-lane__rail" aria-hidden="true">
                        <span class="corridor-lane__track"></span>
                        <span class="corridor-lane__glow"></span>
                        <span class="corridor-lane__ship"></span>
                        <span class="corridor-lane__terminal"></span>
                      </span>
                      <span class="corridor-lane__card">
                        <span class="corridor-lane__meta">02 · Southeast Asia</span>
                        <strong>Southeast Asia</strong>
                        <span class="corridor-lane__countries">Vietnam, Philippines, Indonesia, Malaysia</span>
                      </span>
                    </button>
                    <button class="corridor-lane" type="button" data-corridor-item aria-pressed="false">
                      <span class="corridor-lane__rail" aria-hidden="true">
                        <span class="corridor-lane__track"></span>
                        <span class="corridor-lane__glow"></span>
                        <span class="corridor-lane__ship"></span>
                        <span class="corridor-lane__terminal"></span>
                      </span>
                      <span class="corridor-lane__card">
                        <span class="corridor-lane__meta">03 · Island Cargo</span>
                        <strong>Island cargo</strong>
                        <span class="corridor-lane__countries">Maldives and Mauritius</span>
                      </span>
                    </button>
                    <button class="corridor-lane" type="button" data-corridor-item aria-pressed="false">
                      <span class="corridor-lane__rail" aria-hidden="true">
                        <span class="corridor-lane__track"></span>
                        <span class="corridor-lane__glow"></span>
                        <span class="corridor-lane__ship"></span>
                        <span class="corridor-lane__terminal"></span>
                      </span>
                      <span class="corridor-lane__card">
                        <span class="corridor-lane__meta">04 · East Africa</span>
                        <strong>East Africa</strong>
                        <span class="corridor-lane__countries">Kenya</span>
                      </span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <section class="section-block section-block--contrast">
            <div class="shell section-shell">
              <article class="relationship-band" data-reveal>
                <p class="section-label">Supply Relationships</p>
                <h2>Built for Long-Term Supply Relationships</h2>
                <p>We work with buyers who value consistency in quality, communication, and shipment execution across repeat orders.</p>
              </article>
            </div>
          </section>

          <section class="section-block section-block--contact">
            <div class="shell section-shell">
              {form_block()}
            </div>
          </section>
        </main>
        {footer_html()}
        """
    ).strip()
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": CONTACT["company"],
            "url": BASE_URL,
            "email": CONTACT["sales_email"],
            "telephone": CONTACT["phone"],
            "addressCountry": "IN",
        },
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "Jade Waves Enterprise Product Portfolio",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": index + 1,
                    "url": f"{BASE_URL}/products/{product['slug']}/",
                    "name": product["name"],
                }
                for index, product in enumerate(ACTIVE_PRODUCTS)
            ],
        },
    ]
    return page_shell(
        "Industrial Mineral Exporter from India | Supplier for Global Buyers | Jade Waves Enterprise",
        "Industrial mineral exporter from India supplying global buyers across Vietnam, Thailand, the Philippines, UAE, Oman, Qatar, Bahrain, Mauritius, Maldives, Malaysia, Singapore, and Saudi Arabia.",
        "/",
        home_body,
        schema,
        "page-home",
    )


def render_blog_index_page() -> str:
    current_posts = [post for post in BLOGS if post["slug"] in CURRENT_BLOG_SLUGS]
    post_cards = []
    for post in current_posts:
        product = PRODUCTS_BY_SLUG[post["product_slug"]]
        post_cards.append(
            dedent(
                f"""
                <article class="blog-card" data-reveal>
                  <p class="blog-card__eyebrow">{escape(post["eyebrow"])}</p>
                  <h3>{escape(post["title"])}</h3>
                  <p>{escape(post["summary"])}</p>
                  <div class="blog-card__actions">
                    <a class="blog-card__link" href="/blog/{escape(post["slug"])}/">Read guide</a>
                    <a class="blog-card__link blog-card__link--alt" href="/products/{escape(product["slug"])}/">{escape(product["name"])}</a>
                  </div>
                </article>
                """
            ).strip()
        )
    body = dedent(
        f"""
        {nav_html()}
        <main>
          <section class="hero hero--home">
            <div class="hero__strata" aria-hidden="true">
              <span class="strata strata--a"></span>
              <span class="strata strata--b"></span>
              <span class="strata strata--c"></span>
              <span class="route-line route-line--hero"></span>
            </div>
            <div class="shell home-hero">
              <div class="hero-copy hero-copy--home" data-reveal>
                <p class="hero-label">Buyer Guides</p>
                <h1>Buyer<br />guides.</h1>
                <p class="hero-text">
                  This section is being rebuilt around real buyer questions on specification, sampling, and export planning.
                </p>
                <div class="hero-actions">
                  <a class="button button--light" href="/#contact" data-set-request="Quote">Start Inquiry</a>
                  <a class="button button--ghost" href="/products/">Explore Products</a>
                </div>
              </div>
            </div>
            <div class="shell proof-strip" data-reveal>
              <article class="proof-strip__item">
                <span class="proof-strip__eyebrow">Who this is for</span>
                <strong>Importers and procurement teams</strong>
              </article>
              <article class="proof-strip__item">
                <span class="proof-strip__eyebrow">What you get</span>
                <strong>Clear RFQ and pre-dispatch checklists</strong>
              </article>
              <article class="proof-strip__item">
                <span class="proof-strip__eyebrow">Move faster</span>
                <strong>Product links and direct inquiry paths</strong>
              </article>
              <article class="proof-strip__item">
                <span class="proof-strip__eyebrow">Next step</span>
                <strong>Share spec, destination, and volume</strong>
              </article>
            </div>
          </section>

          <section class="section-block section-block--contrast">
            <div class="shell section-shell">
              <div class="section-topline section-topline--stack" data-reveal>
                <div class="section-topline__copy">
                  <p class="section-kicker">Current post</p>
                  <h2>Published buyer guides.</h2>
                </div>
                <a class="section-link" href="/#contact">Need a quote now?</a>
              </div>
              <div class="blog-grid">
                {"".join(post_cards)}
              </div>
            </div>
          </section>

          <section class="section-block">
            <div class="shell section-shell">
              <div class="home-ledger">
                <div class="home-ledger__intro" data-reveal>
                  <p class="section-kicker">Quick move</p>
                  <h2>Move from reading to buying without friction.</h2>
                  <p>Use these direct links to switch from guide content into technical and commercial discussion.</p>
                </div>
                <div class="home-ledger__rows">
                  <article class="home-ledger-row" data-reveal>
                    <span>01</span>
                    <div>
                      <strong><a href="/products/">Open product portfolio</a></strong>
                      <p>Compare grades, forms, and specification focus across all products.</p>
                    </div>
                  </article>
                  <article class="home-ledger-row" data-reveal>
                    <span>02</span>
                    <div>
                      <strong><a href="/operations/">Review operations</a></strong>
                      <p>See processing and dispatch visibility before confirming supply decisions.</p>
                    </div>
                  </article>
                  <article class="home-ledger-row" data-reveal>
                    <span>03</span>
                    <div>
                      <strong><a href="/#countries-served">See countries served</a></strong>
                      <p>View the current export lanes and country groups being handled from India.</p>
                    </div>
                  </article>
                  <article class="home-ledger-row" data-reveal>
                    <span>04</span>
                    <div>
                      <strong><a href="/#contact" data-set-request="Quote">Send inquiry</a></strong>
                      <p>Share product, destination, monthly volume, and packing basis for a clean quote.</p>
                    </div>
                  </article>
                </div>
              </div>
            </div>
          </section>
        </main>
        {footer_html()}
        """
    ).strip()
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "Buyer and Importer Blog",
            "url": f"{BASE_URL}/blog/",
            "description": "Buyer guide hub for import teams reviewing industrial mineral sourcing, specification checks, and export planning from India.",
        },
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "Published Buyer Guides",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": index + 1,
                    "url": f"{BASE_URL}/blog/{post['slug']}/",
                    "name": post["title"],
                }
                for index, post in enumerate(current_posts)
            ],
        },
    ]
    return page_shell(
        "Buyer Guides | Jade Waves Enterprise",
        "Buyer guide hub from Jade Waves Enterprise for import teams reviewing mineral sourcing, specification checks, and export planning.",
        "/blog/",
        body,
        schema,
        "page-blog",
    )


def render_blog_post_page(post: dict) -> str:
    product = PRODUCTS_BY_SLUG[post["product_slug"]]
    title_lines = post.get("display_title_lines")
    visible_title = "<br />".join(escape(line) for line in title_lines) if title_lines else escape(post["title"])
    section_markup = "".join(
        dedent(
            f"""
            <section class="blog-article-section" data-reveal>
              <h2>{escape(section["heading"])}</h2>
              <p>{escape(section["body"])}</p>
              <ul class="bullet-list">
                {"".join(f"<li>{escape(point)}</li>" for point in section["points"])}
              </ul>
            </section>
            """
        ).strip()
        for section in post["sections"]
    )
    questions_markup = "".join(f"<li>{escape(question)}</li>" for question in post["questions"])
    related_cards = []
    for related in BLOGS:
        if related["slug"] not in CURRENT_BLOG_SLUGS:
            continue
        if related["slug"] == post["slug"]:
            continue
        related_cards.append(
            dedent(
                f"""
                <a class="blog-card blog-card--compact" href="/blog/{escape(related["slug"])}/" data-reveal>
                  <p class="blog-card__eyebrow">{escape(related["eyebrow"])}</p>
                  <h3>{escape(related["title"])}</h3>
                  <p>{escape(related["summary"])}</p>
                </a>
                """
            ).strip()
        )
        if len(related_cards) == 3:
            break
    related_section = ""
    if related_cards:
        related_section = dedent(
            f"""
          <section class="section-block section-block--contrast">
            <div class="shell section-shell">
              <div class="section-topline section-topline--stack" data-reveal>
                <div class="section-topline__copy">
                  <p class="section-kicker">Related guides</p>
                  <h2>Continue with nearby buyer questions.</h2>
                </div>
                <a class="section-link" href="/blog/">Open all guides</a>
              </div>
              <div class="blog-grid blog-grid--compact">
                {"".join(related_cards)}
              </div>
            </div>
          </section>
            """
        ).strip()

    body = dedent(
        f"""
        {nav_html()}
        <main>
          <section class="hero hero--home">
            <div class="hero__strata" aria-hidden="true">
              <span class="strata strata--a"></span>
              <span class="strata strata--b"></span>
              <span class="strata strata--c"></span>
              <span class="route-line route-line--hero"></span>
            </div>
            <div class="shell home-hero">
              <div class="hero-copy hero-copy--home" data-reveal>
                <p class="hero-label">{escape(post["eyebrow"])}</p>
                <h1>{visible_title}</h1>
                <p class="hero-text">{escape(post["summary"])}</p>
                <div class="hero-actions">
                  <a class="button button--light" href="/products/{escape(product["slug"])}/">Open {escape(product["name"])}</a>
                  <a class="button button--ghost" href="/#contact" data-set-request="Quote">Request Quote</a>
                </div>
              </div>
            </div>
            <div class="shell proof-strip" data-reveal>
              <article class="proof-strip__item">
                <span class="proof-strip__eyebrow">From this guide</span>
                <strong>What to confirm before RFQ</strong>
              </article>
              <article class="proof-strip__item">
                <span class="proof-strip__eyebrow">Primary product</span>
                <strong>{escape(product["name"])}</strong>
              </article>
              <article class="proof-strip__item">
                <span class="proof-strip__eyebrow">Move to technicals</span>
                <strong><a href="/products/{escape(product["slug"])}/">Open product page</a></strong>
              </article>
              <article class="proof-strip__item">
                <span class="proof-strip__eyebrow">Move to inquiry</span>
                <strong><a href="/#contact" data-set-request="Quote">Send requirement</a></strong>
              </article>
            </div>
          </section>

          <section class="section-block">
            <div class="shell section-shell">
              <div class="blog-layout">
                <article class="blog-article">
                  {section_markup}
                </article>
                <aside class="blog-sidecard" data-reveal>
                  <p class="section-label">Buyer RFQ checklist</p>
                  <h2>Share these details in your first inquiry.</h2>
                  <ul class="bullet-list">
                    {questions_markup}
                  </ul>
                  <div class="related-links blog-sidecard__links">
                    <a href="/products/{escape(product["slug"])}/">Open {escape(product["name"])}</a>
                    <a href="/operations/">See operations</a>
                    <a href="/#contact" data-set-request="Quote">Send inquiry</a>
                  </div>
                </aside>
              </div>
            </div>
          </section>

          {related_section}
        </main>
        {footer_html()}
        """
    ).strip()
    post_url = f"{BASE_URL}/blog/{post['slug']}/"
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": post["title"],
            "description": post["meta_description"],
            "mainEntityOfPage": post_url,
            "url": post_url,
            "datePublished": TODAY,
            "dateModified": TODAY,
            "author": {"@type": "Organization", "name": CONTACT["company"]},
            "publisher": {
                "@type": "Organization",
                "name": CONTACT["company"],
                "logo": {
                    "@type": "ImageObject",
                    "url": f"{BASE_URL}/assets/jade-waves-logo-transparent.png",
                },
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE_URL}/blog/"},
                {"@type": "ListItem", "position": 3, "name": post["title"], "item": post_url},
            ],
        },
    ]
    return page_shell(
        post["seo_title"],
        post["meta_description"],
        f"/blog/{post['slug']}/",
        body,
        schema,
        "page-blog-post",
    )


def render_products_index() -> str:
    family_nav = []
    family_sections = []
    for index, family in enumerate(PRODUCT_FAMILIES, start=1):
        family_product_count = len(family["products"])
        count_label = f"{family_product_count} product" if family_product_count == 1 else f"{family_product_count} products"
        family_number = f"{index:02d}"
        family_focus = "".join(
            f'<span class="portfolio-stage__pill">{escape(item)}</span>' for item in family.get("best_for", [])
        )
        family_nav.append(
            f'<a class="portfolio-anchor" href="#{escape(family["id"])}">{escape(family["name"])}</a>'
        )
        rows = []
        for slug in family["products"]:
            product = PRODUCTS_BY_SLUG[slug]
            raw_selection_targets = product.get("portfolio_best_for", product["applications"][:2])
            selection_targets = [
                raw_selection_targets[0],
                *[sentence_fragment(item) for item in raw_selection_targets[1:]],
            ] if raw_selection_targets else []
            selection_copy = natural_join(selection_targets)
            rows.append(
                dedent(
                    f"""
                    <a class="portfolio-product" href="/products/{product["slug"]}/">
                      <div class="portfolio-product__main">
                        <p class="portfolio-product__eyebrow">{escape(product["eyebrow"])}</p>
                        <h3>{escape(product["name"])}</h3>
                        <p class="portfolio-product__fit"><span>Best for</span>{escape(selection_copy)}</p>
                      </div>
                      <span class="portfolio-product__arrow">View product</span>
                    </a>
                    """
                ).strip()
            )
        family_sections.append(
            dedent(
                f"""
                <section class="portfolio-stage" id="{escape(family["id"])}">
                  <div class="portfolio-stage__intro" data-reveal>
                    <p class="portfolio-stage__index">{family_number}</p>
                    <p class="portfolio-stage__count">{escape(count_label)}</p>
                    <h2>{escape(family["name"])}</h2>
                    <p>{escape(family["copy"])}</p>
                    <div class="portfolio-stage__focus">
                      <span class="portfolio-stage__focus-label">Best for</span>
                      {family_focus}
                    </div>
                  </div>
                  <div class="portfolio-stage__track" data-reveal>
                    {''.join(rows)}
                  </div>
                </section>
                """
            ).strip()
        )
    body = dedent(
        f"""
        {nav_html()}
        <main>
          <section class="hero hero--portfolio">
            <div class="hero__strata" aria-hidden="true">
              <span class="strata strata--a"></span>
              <span class="strata strata--b"></span>
              <span class="strata strata--c"></span>
              <span class="route-line route-line--hero"></span>
            </div>
            <div class="shell hero__inner hero__inner--single">
              <div class="hero-copy hero-copy--portfolio" data-reveal>
                <p class="hero-label">Portfolio</p>
                <h1>Browse by application first.</h1>
                <p class="hero-text">
                  Use the portfolio to find industrial minerals supplied and exported from India for import buyers in Southeast Asia, the Gulf, Mauritius, and Maldives.
                </p>
                <div class="hero-actions">
                  <a class="button button--light" href="/#contact" data-set-request="Quote">Request Quote</a>
                  <a class="button button--ghost" href="/">Back to Homepage</a>
                </div>
              </div>
            </div>
          </section>
          <section class="section-block">
            <div class="shell portfolio-anchor-rail" data-reveal>
              {''.join(family_nav)}
            </div>
          </section>
          <section class="section-block">
            <div class="shell portfolio-shell">
              {''.join(family_sections)}
            </div>
          </section>
        </main>
        {footer_html()}
        """
    ).strip()
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "Jade Waves Enterprise Product Portfolio",
            "url": f"{BASE_URL}/products/",
        },
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "Industrial Minerals",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": index + 1,
                    "url": f"{BASE_URL}/products/{product['slug']}/",
                    "name": product["name"],
                }
                for index, product in enumerate(ACTIVE_PRODUCTS)
            ],
        },
    ]
    return page_shell(
        "Industrial Minerals Supplier & Exporter from India | Jade Waves Enterprise",
        "Industrial minerals supplier and exporter from India for import buyers across Vietnam, Thailand, the Philippines, UAE, Oman, Qatar, Bahrain, Mauritius, Maldives, Malaysia, Singapore, and Saudi Arabia.",
        "/products/",
        body,
        schema,
        "page-portfolio",
    )


def render_export_markets_page() -> str:
    proof_items = [
        ("Markets in scope", "Gulf, Southeast Asia, Mauritius, Maldives"),
        ("Buyer focus", "Specification, packing, timing"),
        ("Typical flow", "Quote, sample, documents, dispatch"),
        ("Best fit", "Bulk import buyers and repeat programs"),
    ]
    proof_markup = "".join(
        dedent(
            f"""
            <article class="proof-strip__item">
              <span class="proof-strip__eyebrow">{escape(label)}</span>
              <strong>{escape(value)}</strong>
            </article>
            """
        ).strip()
        for label, value in proof_items
    )
    market_rows = [
        ("01", "Gulf buyers", "Gulf buyers usually want cleaner communication on specs, packing, and dispatch timing before the cargo is locked."),
        ("02", "Southeast Asia buyers", "Southeast Asia buyers often start with application fit, then narrow into chemistry, sizing, and shipment rhythm."),
        ("03", "Island cargo buyers", "Mauritius and Maldives buyers usually value consistency and dependable export handling over unnecessary range."),
    ]
    market_rows_markup = "".join(
        dedent(
            f"""
            <article class="home-ledger-row" data-reveal>
              <span>{escape(number)}</span>
              <div>
                <strong>{escape(title)}</strong>
                <p>{escape(copy)}</p>
              </div>
            </article>
            """
        ).strip()
        for number, title, copy in market_rows
    )
    process_steps = [
        ("01", "Share the requirement", "Tell us the product, application, destination, monthly volume, and preferred packing."),
        ("02", "Align the right grade", "We match the requirement to the right chemistry, size range, and commercial fit before quoting."),
        ("03", "Confirm shipment detail", "Packing, documentation, and dispatch timing are aligned before the order moves."),
        ("04", "Keep the export flow visible", "Updates continue through loading and onward cargo movement so the buyer is not chasing status."),
    ]
    process_markup = "".join(
        dedent(
            f"""
            <article class="process-step" data-reveal>
              <span>{escape(number)}</span>
              <div class="process-step__body">
                <h3>{escape(title)}</h3>
                <p>{escape(copy)}</p>
              </div>
            </article>
            """
        ).strip()
        for number, title, copy in process_steps
    )
    market_links = "".join(
        [
            '<a href="/products/silica-sand/">Silica sand for glass, filtration, and foundry buyers</a>',
            '<a href="/products/quartz-sand-for-ceramics/">Quartz sand, grits, and powder for ceramic and glass buyers</a>',
            '<a href="/products/feldspar/">Potash and soda feldspar for ceramic and sanitaryware buyers</a>',
        ]
    )
    body = dedent(
        f"""
        {nav_html()}
        <main>
          <section class="hero hero--home">
            <div class="hero__strata" aria-hidden="true">
              <span class="strata strata--a"></span>
              <span class="strata strata--b"></span>
              <span class="strata strata--c"></span>
              <span class="route-line route-line--hero"></span>
            </div>
            <div class="shell home-hero">
              <div class="hero-copy hero-copy--home" data-reveal>
                <p class="hero-label">Export markets</p>
                <h1>Industrial minerals, clearly supplied.</h1>
                <p class="hero-text">
                  Jade Waves supports import buyers across the Gulf, Southeast Asia, Mauritius, and Maldives with clear product fit, export handling, and communication that stays steady from inquiry to dispatch.
                </p>
                <div class="hero-actions">
                  <a class="button button--light" href="/products/">View Products</a>
                  <a class="button button--ghost" href="/#contact" data-set-request="Quote">Request Quote</a>
                </div>
              </div>
              <div class="home-poster" data-reveal data-parallax="0.14">
                <div class="home-poster__surface">
                  <div class="home-poster__summary">
                    <p class="home-poster__eyebrow">Buyer view</p>
                    <strong>Clear market fit. Fewer loose ends.</strong>
                    <p>Buyers usually want three things early: the right material, a clean export plan, and communication that stays reliable after the first reply.</p>
                  </div>
                  <div class="home-poster__metrics">
                    <article class="home-metric">
                      <span>Scope</span>
                      <strong>Bulk industrial mineral supply</strong>
                    </article>
                    <article class="home-metric">
                      <span>Packing</span>
                      <strong>25 Kg/50 Kg &amp; Jumbo Bags</strong>
                    </article>
                    <article class="home-metric">
                      <span>Shipment</span>
                      <strong>Export handling from India</strong>
                    </article>
                  </div>
                  <span class="route-line route-line--visual"></span>
                </div>
              </div>
            </div>
            <div class="shell proof-strip" data-reveal>
              {proof_markup}
            </div>
          </section>

          <section class="section-block">
            <div class="shell section-shell">
              <div class="home-ledger">
                <div class="home-ledger__intro" data-reveal>
                  <p class="section-kicker">Where buyers are coming from</p>
                  <h2>Different markets, similar buying logic.</h2>
                  <p>Product fit, document clarity, and dispatch discipline tend to matter more than broad claims. The market changes, but those priorities usually do not.</p>
                </div>
                <div class="home-ledger__rows">
                  {market_rows_markup}
                </div>
              </div>
            </div>
          </section>

          <section class="section-block section-block--contrast">
            <div class="shell section-shell">
              <div class="home-split">
                <article class="home-split__panel" data-reveal>
                  <p class="section-label">How product fit is handled</p>
                  <h2>Start with application, then align the mineral.</h2>
                  <p>Better buying decisions usually come from starting with end use, chemistry range, size requirement, and packing constraints rather than a generic product list.</p>
                  <div class="related-links">{market_links}</div>
                </article>
                <article class="home-split__panel" data-reveal>
                  <p class="section-label">How export handling is kept calm</p>
                  <h2>One visible track from inquiry to dispatch.</h2>
                  <p>Short steps and cleaner handoffs reduce the usual friction around export buying.</p>
                  <div class="home-process-list">
                    {process_markup}
                  </div>
                </article>
              </div>
            </div>
          </section>

          <section class="section-block section-block--contact">
            <div class="shell section-shell">
              {form_block("Export Markets")}
            </div>
          </section>
        </main>
        {footer_html()}
        """
    ).strip()
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "Export Markets",
            "description": "Industrial mineral supply from India for buyers across the Gulf, Southeast Asia, Mauritius, and Maldives.",
            "url": f"{BASE_URL}/export-markets/",
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
                {"@type": "ListItem", "position": 2, "name": "Export Markets", "item": f"{BASE_URL}/export-markets/"},
            ],
        },
    ]
    return page_shell(
        "Export Markets for Industrial Mineral Buyers | Jade Waves Enterprise",
        "Industrial mineral supply from India for buyers across the Gulf, Southeast Asia, Mauritius, and Maldives.",
        "/export-markets/",
        body,
        schema,
        "page-export-markets",
    )


def render_exporter_profile_page() -> str:
    proof_items = [
        ("Company focus", "Industrial mineral supply from India"),
        ("Buyer priority", "Specification clarity before dispatch"),
        ("Typical shipment", "FCL export programs"),
        ("Best fit", "Import buyers who need repeatable supply"),
    ]
    proof_markup = "".join(
        dedent(
            f"""
            <article class="proof-strip__item">
              <span class="proof-strip__eyebrow">{escape(label)}</span>
              <strong>{escape(value)}</strong>
            </article>
            """
        ).strip()
        for label, value in proof_items
    )
    buyer_rows = [
        ("01", "Clear specification handling", "The right conversation starts with chemistry, size, application, packing, and destination, not vague product labels."),
        ("02", "Export-ready communication", "Buyers need direct answers on documents, shipment planning, and what can realistically be delivered."),
        ("03", "Range with commercial focus", "The range covers ceramic, glass, drilling, foundry, water treatment, and process buyers without reading like a generic catalogue."),
    ]
    buyer_rows_markup = "".join(
        dedent(
            f"""
            <article class="home-ledger-row" data-reveal>
              <span>{escape(number)}</span>
              <div>
                <strong>{escape(title)}</strong>
                <p>{escape(copy)}</p>
              </div>
            </article>
            """
        ).strip()
        for number, title, copy in buyer_rows
    )
    product_links = "".join(
        [
            '<a href="/products/silica-sand/">Silica sand supplier and exporter</a>',
            '<a href="/products/quartz-sand-for-ceramics/">Quartz sand, grits, and powder supplier</a>',
            '<a href="/products/feldspar/">Potash and soda feldspar supplier</a>',
        ]
    )
    process_steps = [
        ("01", "Requirement review", "Product, application, country, volume, and packing preference are clarified first."),
        ("02", "Quote or sample alignment", "Commercial fit is matched to the right grade before a sample or quote is finalised."),
        ("03", "Commercial confirmation", "Packing, paperwork, and shipment timing are confirmed before loading begins."),
        ("04", "Dispatch follow-through", "The buyer continues getting updates instead of having to chase the shipment."),
    ]
    process_markup = "".join(
        dedent(
            f"""
            <article class="process-step" data-reveal>
              <span>{escape(number)}</span>
              <div class="process-step__body">
                <h3>{escape(title)}</h3>
                <p>{escape(copy)}</p>
              </div>
            </article>
            """
        ).strip()
        for number, title, copy in process_steps
    )
    body = dedent(
        f"""
        {nav_html()}
        <main>
          <section class="hero hero--home">
            <div class="hero__strata" aria-hidden="true">
              <span class="strata strata--a"></span>
              <span class="strata strata--b"></span>
              <span class="strata strata--c"></span>
              <span class="route-line route-line--hero"></span>
            </div>
            <div class="shell home-hero">
              <div class="hero-copy hero-copy--home" data-reveal>
                <p class="hero-label">Company profile</p>
                <h1>Industrial minerals exporter from India for buyers who want the details settled early.</h1>
                <p class="hero-text">
                  Jade Waves Enterprise supports import buyers with industrial mineral supply from India, handling product fit, packing, documents, and dispatch with a calmer, specification-led approach.
                </p>
                <div class="hero-actions">
                  <a class="button button--light" href="/products/">Explore Portfolio</a>
                  <a class="button button--ghost" href="/#contact" data-set-request="Quote">Request Quote</a>
                </div>
              </div>
              <div class="home-poster" data-reveal data-parallax="0.14">
                <div class="home-poster__surface">
                  <div class="home-poster__summary">
                    <p class="home-poster__eyebrow">Why buyers shortlist</p>
                    <strong>Less friction around the important details.</strong>
                    <p>For import buyers, the stronger signal is usually clearer specification handling, steadier export follow-through, and faster alignment on what can actually ship.</p>
                  </div>
                  <div class="home-poster__metrics">
                    <article class="home-metric">
                      <span>Range</span>
                      <strong>Silica sand, quartz sand, and feldspar</strong>
                    </article>
                    <article class="home-metric">
                      <span>Focus</span>
                      <strong>Bulk industrial and repeat buying programs</strong>
                    </article>
                    <article class="home-metric">
                      <span>Origin</span>
                      <strong>Export supply from India</strong>
                    </article>
                  </div>
                  <span class="route-line route-line--visual"></span>
                </div>
              </div>
            </div>
            <div class="shell proof-strip" data-reveal>
              {proof_markup}
            </div>
          </section>

          <section class="section-block">
            <div class="shell section-shell">
              <div class="home-ledger">
                <div class="home-ledger__intro" data-reveal>
                  <p class="section-kicker">Buyer perspective</p>
                  <h2>What import teams usually need to know first.</h2>
                  <p>This page answers the practical questions buyers usually ask before going deeper into specs, samples, or commercial terms.</p>
                </div>
                <div class="home-ledger__rows">
                  {buyer_rows_markup}
                </div>
              </div>
            </div>
          </section>

          <section class="section-block section-block--contrast">
            <div class="shell section-shell">
              <div class="home-split">
                <article class="home-split__panel" data-reveal>
                  <p class="section-label">Core export range</p>
                  <h2>Products buyers usually ask for first.</h2>
                      <p>These products usually matter most when the requirement is tied to ceramics, glass, filtration, and engineered stone buying programs.</p>
                  <div class="related-links">{product_links}</div>
                </article>
                <article class="home-split__panel" data-reveal>
                  <p class="section-label">Working style</p>
                  <h2>How the export process is kept straightforward.</h2>
                  <p>The goal is to remove avoidable confusion before pricing, loading, and document handling become time-sensitive.</p>
                  <div class="home-process-list">
                    {process_markup}
                  </div>
                </article>
              </div>
            </div>
          </section>

          <section class="section-block section-block--contact">
            <div class="shell section-shell">
              {form_block("Industrial Minerals Exporter India")}
            </div>
          </section>
        </main>
        {footer_html()}
        """
    ).strip()
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "AboutPage",
            "name": "Industrial Minerals Exporter India",
            "description": "Industrial mineral exporter from India with clear specification handling and dependable export follow-through.",
            "url": f"{BASE_URL}/industrial-minerals-exporter-india/",
        },
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": CONTACT["company"],
            "url": BASE_URL,
            "telephone": CONTACT["phone"],
            "email": CONTACT["sales_email"],
            "address": {
                "@type": "PostalAddress",
                "streetAddress": CONTACT["address"],
                "addressCountry": "IN",
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
                {"@type": "ListItem", "position": 2, "name": "Industrial Minerals Exporter India", "item": f"{BASE_URL}/industrial-minerals-exporter-india/"},
            ],
        },
    ]
    return page_shell(
        "Industrial Minerals Exporter from India | Jade Waves Enterprise",
        "Industrial mineral exporter from India with clear specification handling and dependable export follow-through.",
        "/industrial-minerals-exporter-india/",
        body,
        schema,
        "page-exporter-profile",
    )


def render_ceo_page() -> str:
    proof_items = [
        ("Company base", "Ahmedabad, Gujarat, India"),
        ("Manufacturer-backed supply", "Silica sand, quartz sand, and feldspar"),
        ("Port linkage", CONTACT["port"]),
        ("Core export documents", "COA, COO, Packing List, B/L"),
    ]
    proof_markup = "".join(
        dedent(
            f"""
            <article class="proof-strip__item">
              <span class="proof-strip__eyebrow">{escape(label)}</span>
              <strong>{escape(value)}</strong>
            </article>
            """
        ).strip()
        for label, value in proof_items
    )
    commitment_rows = [
        ("01", "Requirement clarity before quote", "We align end use, chemistry, grain size, and packing basis before numbers are finalized."),
        ("02", "Technical references before confirmation", "TDS and sample COA are shared against the discussed grade so technical teams can evaluate clearly."),
        ("03", "Commercial and document alignment", "Shipment basis, packing plan, and document expectations are confirmed early with your team."),
        ("04", "Dispatch visibility", "Buyers receive direct loading and shipment updates from planning stage to cargo movement."),
        ("05", "Repeat-order consistency", "The same operating method is carried into repeat orders so quality and communication remain stable."),
    ]
    commitment_markup = "".join(
        dedent(
            f"""
            <article class="home-ledger-row" data-reveal>
              <span>{escape(number)}</span>
              <div>
                <strong>{escape(title)}</strong>
                <p>{escape(copy)}</p>
              </div>
            </article>
            """
        ).strip()
        for number, title, copy in commitment_rows
    )
    body = dedent(
        f"""
        {nav_html()}
        <main>
          <section class="hero hero--home">
            <div class="hero__strata" aria-hidden="true">
              <span class="strata strata--a"></span>
              <span class="strata strata--b"></span>
              <span class="strata strata--c"></span>
              <span class="route-line route-line--hero"></span>
            </div>
            <div class="shell home-hero">
              <div class="hero-copy hero-copy--home" data-reveal>
                <p class="hero-label">Hear from our CEO</p>
                <h1>A note<br />for buyers.</h1>
                <p class="hero-text">
                  This page explains how we work with import buyers in practical terms: agree the right specification first, share technical references early, and keep dispatch execution visible until cargo moves.
                </p>
                <div class="hero-actions">
                  <a class="button button--light" href="/#contact" data-set-request="Quote">Request Quote</a>
                  <a class="button button--ghost" href="{escape(CEO_LINKEDIN_URL)}" target="_blank" rel="noopener noreferrer">Connect on LinkedIn</a>
                </div>
              </div>
            </div>
            <div class="shell proof-strip" data-reveal>
              {proof_markup}
            </div>
          </section>

          <section class="section-block section-block--contrast">
            <div class="shell section-shell">
              <article class="ceo-spotlight" data-reveal>
                <div class="ceo-spotlight__grid">
                  <div class="ceo-spotlight__content">
                    <p class="section-label">CEO Note</p>
                    <h2>What buyers can expect when working with Jade Waves.</h2>
                    <p class="ceo-spotlight__quote">“Clarity before commitment. Discipline in execution. Communication that stays direct from inquiry to dispatch.”</p>
                    <div class="ceo-spotlight__body">
                      <p>
                        We do not treat export supply as only cargo movement. Our responsibility is to make sure your team receives the material aligned to your end use, with the right packing, document discipline, and commercial clarity.
                      </p>
                      <p>
                        We manufacture and export silica sand, quartz sand, and feldspar from India for buyers who value repeat-order reliability over one-time transactions.
                      </p>
                      <p>
                        You will have a directly reachable team member during inquiry, sampling, documentation, and dispatch. That keeps decisions faster, execution cleaner, and avoidable risk lower.
                      </p>
                    </div>
                    <p class="ceo-spotlight__meta"><span>Deep Mehta</span><span>CEO, Jade Waves Enterprise</span></p>
                    <div class="ceo-spotlight__actions">
                      <a class="button button--ghost button--compact" href="{escape(CEO_LINKEDIN_URL)}" target="_blank" rel="noopener noreferrer">Connect on LinkedIn</a>
                    </div>
                  </div>
                  <figure class="ceo-spotlight__media">
                    <img src="/assets/deep-mehta-ceo.jpg" alt="Deep Mehta, CEO of Jade Waves Enterprise" loading="lazy" />
                  </figure>
                </div>
              </article>
            </div>
          </section>

          <section class="section-block">
            <div class="shell section-shell">
              <div class="home-ledger">
                <div class="home-ledger__intro" data-reveal>
                  <p class="section-kicker">Commercial commitments</p>
                  <h2>How we keep buyer confidence stable across repeat orders.</h2>
                  <p>These are operating commitments buyers can verify during enquiry, trial, documentation, and dispatch.</p>
                </div>
                <div class="home-ledger__rows">
                  {commitment_markup}
                </div>
              </div>
            </div>
          </section>

          <section class="section-block section-block--contact">
            <div class="shell section-shell">
              {form_block("CEO Inquiry")}
            </div>
          </section>
        </main>
        {footer_html()}
        """
    ).strip()
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "AboutPage",
            "name": "Hear from our CEO",
            "description": "CEO message on manufacturer-led mineral supply, technical clarity, and dependable export execution for global buyers.",
            "url": f"{BASE_URL}/hear-from-ceo/",
        },
        {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": "Deep Mehta",
            "jobTitle": "CEO",
            "worksFor": {"@type": "Organization", "name": CONTACT["company"]},
            "url": CEO_LINKEDIN_URL,
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
                {"@type": "ListItem", "position": 2, "name": "Hear from our CEO", "item": f"{BASE_URL}/hear-from-ceo/"},
            ],
        },
    ]
    return page_shell(
        "A Note for Buyers | Jade Waves Enterprise",
        "CEO message from Jade Waves Enterprise on how we align technical fit, packing, and export execution for global mineral buyers.",
        "/hear-from-ceo/",
        body,
        schema,
        "page-ceo",
    )


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


def render_product_page(product: dict) -> str:
    booking_points = product.get("booking_points", product["specs"])
    application_lines = "".join(
        dedent(
            f"""
            <article class="product-line">
              <span>{index:02d}</span>
              <div>
                <strong>{escape(item)}</strong>
              </div>
            </article>
            """
        ).strip()
        for index, item in enumerate(product["applications"], start=1)
    )
    benefit_notes = "".join(
        dedent(
            f"""
            <article class="product-note">
              <span aria-hidden="true"></span>
              <p>{escape(item)}</p>
            </article>
            """
        ).strip()
        for item in product["benefits"]
    )
    booking_items = "".join(
        dedent(
            f"""
            <article class="product-line product-line--booking">
              <span>{index:02d}</span>
              <div>
                <strong>{escape(item)}</strong>
              </div>
            </article>
            """
        ).strip()
        for index, item in enumerate(booking_points, start=1)
    )
    form_pills = "".join(f'<span class="form-pill">{escape(item)}</span>' for item in product["forms"])
    size_pills = "".join(
        f'<span class="size-pill">{escape(item)}</span>' for item in product.get("size_options", [])
    )
    parameter_doc_links = "".join(
        f'<a class="button button--ghost button--compact" href="{escape(href)}" target="_blank" rel="noopener">{escape(label)}</a>'
        for label, href in product.get("parameter_docs", [])
    )
    parameter_doc_block = ""
    if parameter_doc_links:
        parameter_doc_block = dedent(
            f"""
              <div class="grade-sheet-block">
                <div class="grade-sheet-block__head">
                  <p class="grade-sheet-block__label">Parameter Sheets</p>
                  <p class="grade-sheet-block__copy">{escape(product.get("parameter_docs_copy", "Chemical and physical parameter files for active grades."))}</p>
                </div>
                <div class="grade-sheet-block__actions">
                  {parameter_doc_links}
                </div>
              </div>
            """
        ).strip()
    sizes_card = ""
    if product.get("size_options"):
        sizes_card = dedent(
            f"""
              <article class="product-sheet product-sheet--full" data-reveal>
                <p class="section-label">Sizes Available</p>
                <h2>Readily Available Sizes</h2>
                <div class="size-cloud">{size_pills}</div>
                {parameter_doc_block}
              </article>
            """
        ).strip()
    commercial_tags = "".join(f'<span>{escape(item)}</span>' for item in product["industries"])
    related = related_links(product["related"])
    faq_markup, faq_schema = render_faq(product)
    summary_spec = product.get("summary_spec")
    poster_metrics = [
        ("Primary Use", product["applications"][0]),
        ("Typical Spec" if summary_spec else "Specification", summary_spec or booking_points[0]),
        ("Packing", product["packing"]),
        ("Shipment", "FCL"),
    ]
    poster_metric_markup = "".join(
        dedent(
            f"""
            <article class="product-poster__metric">
              <span>{escape(label)}</span>
              <strong>{escape(value)}</strong>
            </article>
            """
        ).strip()
        for label, value in poster_metrics
    )
    supply_rows = "".join(
        dedent(
            f"""
            <article class="product-info-row">
              <span>{escape(label)}</span>
              <strong>{escape(value)}</strong>
            </article>
            """
        ).strip()
        for label, value in [
            ("Forms", natural_join(product["forms"][:3])),
            ("Packing", product["packing"]),
            ("Shipment", "FCL"),
        ]
    )
    hero_crosslink = ""
    if product["slug"] == "silica-sand":
        hero_crosslink = dedent(
            """
            <a class="hero-crosslink-card hero-crosslink-card--bridge" href="/products/quartz-sand-for-ceramics/">
              <strong>For higher-purity requirements</strong>
              <span>Quartz Sand: &gt;99% SiO2 and high whiteness</span>
            </a>
            """
        ).strip()
    bridge_row = ""
    if hero_crosslink:
        bridge_row = dedent(
            f"""
            <div class="shell product-bridge-row" data-reveal>
              <div class="product-bridge-row__spacer" aria-hidden="true"></div>
              {hero_crosslink}
            </div>
            """
        ).strip()
    product_body = dedent(
        f"""
        {nav_html()}
        <main>
          <section class="hero hero--product theme-{escape(product["theme"])}">
            <div class="hero__strata" aria-hidden="true">
              <span class="strata strata--a"></span>
              <span class="strata strata--b"></span>
              <span class="strata strata--c"></span>
              <span class="route-line route-line--hero"></span>
            </div>
            <div class="shell hero__inner hero__inner--product product-hero">
              <div class="hero-copy hero-copy--product" data-reveal>
                <div class="breadcrumb">
                  <a href="/">Home</a>
                  <span>/</span>
                  <a href="/products/">Products</a>
                  <span>/</span>
                  <strong>{escape(product["name"])}</strong>
                </div>
                <p class="hero-label">{escape(product["eyebrow"])}</p>
                <h1>{escape(product["name"])}</h1>
                <p class="hero-text">{escape(product["hero_copy"])}</p>
                <div class="hero-actions">
                  <a class="button button--light" href="#contact" data-set-request="Quote">Request Quote</a>
                  <a class="button button--ghost" href="#contact" data-set-request="Sample">Request Sample</a>
                </div>
              </div>
              <aside class="product-poster" data-reveal data-parallax="0.12">
                <div class="product-poster__surface">
                  <span class="ore-pillar ore-pillar--a"></span>
                  <span class="ore-pillar ore-pillar--b"></span>
                  <span class="ore-pillar ore-pillar--c"></span>
                  <p class="product-poster__eyebrow">At a glance</p>
                  <strong class="product-poster__title">{escape(product["name"])}</strong>
                  <p class="product-poster__copy">{escape(product["short_copy"])}</p>
                  <div class="product-poster__metrics">
                    {poster_metric_markup}
                  </div>
                  <div class="product-poster__caption">
                    <p>Sample, documents, and dispatch stay on one clear track.</p>
                  </div>
                  <span class="route-line route-line--snapshot"></span>
                </div>
              </aside>
            </div>
          </section>

          <section class="section-block">
            {bridge_row}
            <div class="shell product-ledger">
              <article class="product-sheet product-sheet--wide" data-reveal>
                <p class="section-label">Applications</p>
                <h2>Where it fits best.</h2>
                <p class="product-sheet__intro">Common end uses where grade, form, and delivery have to line up.</p>
                <div class="product-line-list">{application_lines}</div>
              </article>
              <article class="product-sheet" data-reveal>
                <p class="section-label">Supply Snapshot</p>
                <h2>Supply, packing, and shipment.</h2>
                <div class="product-info-list">{supply_rows}</div>
                <div class="form-cloud product-form-cloud">{form_pills}</div>
              </article>
              {sizes_card}
            </div>
          </section>

          <section class="section-block section-block--contrast">
            <div class="shell product-ledger">
              <article class="product-sheet product-sheet--wide" data-reveal>
                <p class="section-label">Specification Focus</p>
                <h2>What should be confirmed.</h2>
                <div class="product-line-list product-line-list--booking">{booking_items}</div>
              </article>
              <article class="product-sheet" data-reveal>
                <p class="section-label">Commercial Fit</p>
                <h2>Why buyers choose it.</h2>
                <p class="product-sheet__body">{escape(product["commercial_fit"])}</p>
                <div class="product-tag-cloud">{commercial_tags}</div>
                <div class="product-note-list">{benefit_notes}</div>
              </article>
            </div>
          </section>

          <section class="section-block">
            <div class="shell section-shell">
              <div class="section-intro" data-reveal>
                <p class="section-label">Also In The Portfolio</p>
                <h2>More from the range.</h2>
              </div>
              <div class="related-links" data-reveal>{related}</div>
            </div>
          </section>

          <section class="section-block section-block--contrast">
            <div class="shell section-shell">
              <div class="section-intro" data-reveal>
                <p class="section-label">FAQ</p>
                <h2>Questions that usually come first.</h2>
                <p>Direct answers before pricing, sampling, and dispatch.</p>
              </div>
              <div class="faq-shell">{faq_markup}</div>
            </div>
          </section>

          <section class="section-block section-block--contact">
            <div class="shell section-shell">
              {form_block(product["name"])}
            </div>
          </section>
        </main>
        {footer_html()}
        """
    ).strip()
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": product["name"],
            "description": product["meta_description"],
            "category": "Industrial Mineral",
            "brand": {"@type": "Brand", "name": CONTACT["company"]},
            "manufacturer": {"@type": "Organization", "name": CONTACT["company"]},
            "url": f"{BASE_URL}/products/{product['slug']}/",
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": BASE_URL,
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "Products",
                    "item": f"{BASE_URL}/products/",
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": product["name"],
                    "item": f"{BASE_URL}/products/{product['slug']}/",
                },
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_schema,
        },
    ]
    return page_shell(
        product["seo_title"],
        product["meta_description"],
        f"/products/{product['slug']}/",
        product_body,
        schema,
        "page-product",
    )


STYLES = dedent(
    """
    :root {
      --bg: #f5f5f7;
      --paper: #ffffff;
      --paper-strong: #fbfbfd;
      --ink: #1d1d1f;
      --ink-soft: rgba(29, 29, 31, 0.72);
      --line: rgba(29, 29, 31, 0.08);
      --line-strong: rgba(255, 255, 255, 0.68);
      --jade: #0071e3;
      --ore: #0071e3;
      --ore-soft: rgba(0, 113, 227, 0.1);
      --stone: #e8e8ed;
      --shadow: 0 18px 48px rgba(29, 29, 31, 0.06);
      --shadow-lg: 0 30px 80px rgba(29, 29, 31, 0.1);
      --radius-xl: 2.25rem;
      --radius-lg: 1.5rem;
      --max-width: 1200px;
    }

    * {
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      margin: 0;
      background:
        radial-gradient(circle at 18% 0%, rgba(0, 113, 227, 0.06), transparent 18%),
        radial-gradient(circle at 82% 8%, rgba(255, 255, 255, 0.84), transparent 18%),
        linear-gradient(180deg, #fbfbfd 0, #f7f7fa 32rem, var(--bg) 32rem, var(--bg) 100%);
      color: var(--ink);
      font-family: "Manrope", sans-serif;
    }

    body::before {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      background:
        linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.55), transparent),
        repeating-linear-gradient(180deg, rgba(255, 255, 255, 0.18) 0, rgba(255, 255, 255, 0.18) 1px, transparent 1px, transparent 12px);
      mix-blend-mode: lighten;
      opacity: 0.1;
      z-index: 0;
      animation: atmosphereDrift 26s ease-in-out infinite alternate;
    }

    body:not(.is-ready) .hero-copy > *,
    body:not(.is-ready) .home-poster__summary,
    body:not(.is-ready) .home-poster__metrics,
    body:not(.is-ready) .home-poster__family-grid,
    body:not(.is-ready) .home-poster__caption,
    body:not(.is-ready) .proof-strip__item,
    body:not(.is-ready) .product-poster__eyebrow,
    body:not(.is-ready) .product-poster__title,
    body:not(.is-ready) .product-poster__copy,
    body:not(.is-ready) .product-poster__metrics,
    body:not(.is-ready) .product-poster__caption {
      opacity: 0;
      transform: translateY(1rem);
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    img {
      display: block;
      max-width: 100%;
    }

    button,
    input,
    select,
    textarea {
      font: inherit;
    }

    ::selection {
      background: rgba(0, 113, 227, 0.16);
    }

    .shell {
      width: min(var(--max-width), calc(100vw - 2rem));
      margin: 0 auto;
    }

    .site-header {
      position: fixed;
      inset: 0 0 auto;
      z-index: 40;
      padding-top: 1rem;
    }

    .site-header__inner {
      width: min(var(--max-width), calc(100vw - 2rem));
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding: 0.95rem 1.2rem;
      border-radius: 999px;
      border: 1px solid transparent;
      transition: background-color 220ms ease, border-color 220ms ease, box-shadow 220ms ease, transform 220ms ease;
    }

    .site-header.is-scrolled .site-header__inner {
      background: rgba(255, 255, 255, 0.76);
      border-color: rgba(29, 29, 31, 0.08);
      box-shadow: 0 18px 48px rgba(29, 29, 31, 0.08);
      backdrop-filter: blur(18px);
    }

    .brand-mark {
      flex: 0 0 auto;
    }

    .brand-mark img {
      height: 2.9rem;
      width: auto;
    }

    .desktop-nav {
      display: flex;
      align-items: center;
      gap: 1.4rem;
      font-size: 0.95rem;
      color: rgba(29, 29, 31, 0.66);
    }

    .site-header.is-scrolled .desktop-nav {
      color: rgba(29, 29, 31, 0.66);
    }

    .desktop-nav a,
    .mobile-menu a {
      position: relative;
      transition: color 180ms ease;
    }

    .desktop-nav a::after,
    .mobile-menu a::after {
      content: "";
      position: absolute;
      left: 0;
      bottom: -0.25rem;
      width: 100%;
      height: 1px;
      background: currentColor;
      transform: scaleX(0);
      transform-origin: left center;
      transition: transform 180ms ease;
    }

    .desktop-nav a:hover::after,
    .mobile-menu a:hover::after {
      transform: scaleX(1);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .menu-toggle {
      display: none;
      border: 0;
      background: rgba(255, 255, 255, 0.9);
      color: var(--ink);
      padding: 0.8rem 1rem;
      border-radius: 999px;
      cursor: pointer;
      box-shadow: 0 10px 24px rgba(29, 29, 31, 0.06);
    }

    .site-header.is-scrolled .menu-toggle {
      background: rgba(255, 255, 255, 0.92);
      color: var(--ink);
    }

    .mobile-menu {
      width: min(var(--max-width), calc(100vw - 2rem));
      margin: 0.75rem auto 0;
      padding: 1rem 1.15rem;
      border-radius: 1.25rem;
      background: rgba(255, 255, 255, 0.96);
      border: 1px solid rgba(29, 29, 31, 0.08);
      box-shadow: var(--shadow);
      display: grid;
      gap: 0.7rem;
    }

    .mobile-menu[hidden] {
      display: none !important;
    }

    .button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      min-height: 3rem;
      padding: 0.8rem 1.3rem;
      border-radius: 999px;
      font-weight: 700;
      font-size: 0.95rem;
      transition: transform 180ms ease, box-shadow 180ms ease, background-color 180ms ease, border-color 180ms ease, color 180ms ease;
      cursor: pointer;
      border: 1px solid transparent;
    }

    .button:hover {
      transform: translateY(-1px);
    }

    .button--dark {
      color: white;
      background: var(--ore);
      box-shadow: 0 16px 40px rgba(0, 113, 227, 0.2);
    }

    .button--light {
      color: var(--ink);
      background: white;
      border-color: rgba(29, 29, 31, 0.08);
      box-shadow: 0 12px 30px rgba(29, 29, 31, 0.08);
    }

    .button--ghost {
      color: var(--ore);
      background: rgba(255, 255, 255, 0.78);
      border-color: rgba(29, 29, 31, 0.08);
      box-shadow: 0 10px 24px rgba(29, 29, 31, 0.06);
    }

    .button--compact {
      min-height: 2.75rem;
      padding-inline: 1.1rem;
    }

    .site-header.is-scrolled .button--ghost {
      color: var(--ore);
      background: rgba(255, 255, 255, 0.92);
      border-color: rgba(29, 29, 31, 0.08);
    }

    main {
      position: relative;
      z-index: 1;
    }

    .hero {
      position: relative;
      overflow: hidden;
      padding-top: 8.7rem;
      color: var(--ink);
    }

    .hero__inner {
      position: relative;
      z-index: 1;
      display: grid;
      grid-template-columns: minmax(0, 1.1fr) minmax(320px, 0.9fr);
      gap: 2.8rem;
      align-items: center;
      min-height: 78vh;
      padding-bottom: 4.25rem;
    }

    .hero__inner--single {
      grid-template-columns: minmax(0, 1fr);
      min-height: 62vh;
      max-width: 58rem;
    }

    .hero__inner--product {
      align-items: stretch;
      gap: 2.4rem;
      min-height: 68vh;
    }

    .hero-copy {
      max-width: 42rem;
    }

    .hero-label,
    .section-label,
    .product-snapshot__label,
    .footer-label,
    .family-label,
    .feature-row__eyebrow,
    .portfolio-row__eyebrow {
      margin: 0 0 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.18em;
      font-size: 0.72rem;
      font-weight: 800;
    }

    .hero-label {
      color: rgba(29, 29, 31, 0.48);
    }

    .hero h1,
    .section-intro h2,
    .product-panel h2,
    .contact-copy h2 {
      margin: 0;
      line-height: 0.96;
      letter-spacing: -0.06em;
      font-weight: 800;
    }

    .hero h1 {
      max-width: 11ch;
      font-size: clamp(3.4rem, 8.2vw, 7.1rem);
    }

    .hero-text,
    .section-intro p,
    .about-point p,
    .industry-item p,
    .process-step p,
    .contact-copy p,
    .panel-copy,
    .faq-item p,
    .footer-copy,
    .portfolio-row p,
    .feature-row p,
    .family-copy {
      margin: 0;
      line-height: 1.75;
      font-size: 1rem;
    }

    .hero-text {
      max-width: 34rem;
      margin-top: 1.4rem;
      color: rgba(29, 29, 31, 0.68);
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 0.85rem;
      margin-top: 2rem;
    }

    .hero-crosslink-card {
      margin-top: 1rem;
      display: inline-grid;
      gap: 0.22rem;
      padding: 0.68rem 0.92rem;
      border-radius: 0.95rem;
      border: 1px solid rgba(29, 29, 31, 0.1);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(246, 248, 252, 0.95)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.06), transparent 46%);
      color: var(--ink);
      text-decoration: none;
      box-shadow: 0 10px 24px rgba(29, 29, 31, 0.06);
      transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    }

    .hero-crosslink-card strong {
      font-size: 0.98rem;
      letter-spacing: -0.02em;
      line-height: 1.2;
    }

    .hero-crosslink-card span {
      font-size: 0.82rem;
      font-weight: 700;
      color: rgba(29, 29, 31, 0.62);
      line-height: 1.35;
    }

    .hero-crosslink-card:hover,
    .hero-crosslink-card:focus-visible {
      transform: translateY(-1px);
      border-color: rgba(0, 113, 227, 0.24);
      box-shadow: 0 14px 32px rgba(29, 29, 31, 0.08);
    }

    .hero-crosslink-card--bridge {
      width: fit-content;
      max-width: 100%;
      margin-top: 1rem;
      padding: 0.82rem 1.04rem;
      border-color: rgba(0, 113, 227, 0.26);
      box-shadow: 0 14px 32px rgba(29, 29, 31, 0.1);
      min-width: clamp(14rem, 28vw, 18.4rem);
      z-index: 4;
    }

    .product-bridge-row {
      display: grid;
      grid-template-columns: minmax(0, 1.08fr) minmax(320px, 0.92fr);
      gap: 1.4rem;
      align-items: start;
      margin-top: -1rem;
      margin-bottom: 1.15rem;
    }

    .product-bridge-row .hero-crosslink-card--bridge {
      margin-top: 0;
    }

    .hero-visual {
      position: relative;
      display: grid;
      align-self: center;
      min-height: 30rem;
      will-change: transform;
    }

    .hero-visual__specimen {
      position: relative;
      min-height: 27rem;
      border-radius: calc(var(--radius-xl) + 0.4rem);
      background:
        radial-gradient(circle at 25% 16%, rgba(255, 255, 255, 0.9), transparent 28%),
        linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(245, 245, 247, 0.92));
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow-lg);
      overflow: hidden;
      backdrop-filter: blur(14px);
    }

    .hero-visual__specimen::after,
    .product-snapshot__visual::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(120deg, transparent 24%, rgba(255, 255, 255, 0.48) 50%, transparent 72%);
      transform: translateX(-120%);
      animation: specimenSweep 12s cubic-bezier(0.22, 1, 0.36, 1) infinite;
      pointer-events: none;
    }

    .hero-spec-grid,
    .snapshot-visual-grid {
      position: relative;
      z-index: 2;
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 0.8rem;
      padding: 1.2rem;
    }

    .hero-spec-card,
    .snapshot-visual-card {
      padding: 0.85rem 0.9rem;
      border-radius: 1.25rem;
      background: rgba(255, 255, 255, 0.86);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: 0 10px 24px rgba(29, 29, 31, 0.06);
      animation: cardBreathe 8s ease-in-out infinite;
      min-width: 0;
    }

    .hero-spec-card:nth-child(2),
    .snapshot-visual-card:nth-child(2) {
      animation-delay: 0.7s;
    }

    .hero-spec-card:nth-child(3),
    .snapshot-visual-card:nth-child(3) {
      animation-delay: 1.4s;
    }

    .hero-spec-card span,
    .snapshot-visual-card span {
      display: block;
      margin-bottom: 0.35rem;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .hero-spec-card strong,
    .snapshot-visual-card strong {
      display: block;
      line-height: 1.32;
      font-size: 0.98rem;
      letter-spacing: -0.03em;
    }

    .hero-spec-caption,
    .snapshot-visual-caption {
      position: absolute;
      left: 1.2rem;
      right: 1.2rem;
      bottom: 1.1rem;
      z-index: 2;
      display: flex;
      align-items: center;
      gap: 0.7rem;
      padding: 0.9rem 1rem;
      border-radius: 1.2rem;
      background: rgba(255, 255, 255, 0.88);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: 0 10px 24px rgba(29, 29, 31, 0.06);
    }

    .hero-spec-caption p,
    .snapshot-visual-caption p {
      margin: 0;
      line-height: 1.5;
      font-size: 0.92rem;
      color: rgba(29, 29, 31, 0.62);
    }

    .hero-spec-caption__dot,
    .snapshot-visual-caption__dot {
      flex: 0 0 auto;
      width: 0.82rem;
      height: 0.82rem;
      border-radius: 50%;
      background: linear-gradient(180deg, #53a3ff, #0071e3);
      box-shadow: 0 0 0 0 rgba(0, 113, 227, 0.16);
      animation: beaconPulse 3.2s ease-in-out infinite;
    }

    .hero-visual__footer {
      display: none;
    }

    .hero-visual__footer span {
      display: none;
    }

    .hero-visual__footer span:nth-child(2) {
      animation-delay: 0.6s;
    }

    .hero-visual__footer span:nth-child(3) {
      animation-delay: 1.2s;
    }

    .ore-slab,
    .ore-pillar {
      position: absolute;
      border-radius: 2rem;
      overflow: hidden;
      transform-origin: center;
      animation: oreDrift 14s ease-in-out infinite alternate;
    }

    .ore-slab::before,
    .ore-pillar::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.22)),
        linear-gradient(120deg, rgba(224, 228, 236, 0.95), rgba(255, 255, 255, 0.8) 42%, rgba(214, 229, 255, 0.9));
    }

    .ore-slab::after,
    .ore-pillar::after {
      content: "";
      position: absolute;
      inset-inline: 10%;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(29, 29, 31, 0.1), transparent);
      top: 28%;
      box-shadow: 0 2.5rem 0 rgba(29, 29, 31, 0.06), 0 5rem 0 rgba(29, 29, 31, 0.04);
    }

    .ore-slab--a {
      left: 7%;
      top: 11%;
      width: 52%;
      height: 32%;
    }

    .ore-slab--b {
      right: 6%;
      top: 29%;
      width: 60%;
      height: 28%;
      animation-duration: 18s;
    }

    .ore-slab--c {
      left: 15%;
      bottom: 9%;
      width: 70%;
      height: 25%;
      animation-duration: 16s;
    }

    .hero-track,
    .product-snapshot {
      position: relative;
      align-self: center;
      padding: 2rem;
      border-radius: calc(var(--radius-xl) + 0.25rem);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.94), rgba(248, 248, 250, 0.92)),
        linear-gradient(140deg, rgba(0, 113, 227, 0.08), rgba(255, 255, 255, 0.5) 44%, rgba(255, 255, 255, 0.18));
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow-lg);
      backdrop-filter: blur(16px);
      overflow: hidden;
    }

    .hero-track::before,
    .product-snapshot::before {
      content: "";
      position: absolute;
      inset: auto -12% -30% auto;
      width: 18rem;
      height: 18rem;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(0, 113, 227, 0.12), transparent 65%);
      filter: blur(12px);
    }

    .hero-track {
      position: absolute;
      right: 1.2rem;
      bottom: 1.2rem;
      width: min(30rem, calc(100% - 2.4rem));
      z-index: 2;
    }

    .hero-signal {
      position: absolute;
      left: 1.2rem;
      top: 1.2rem;
      z-index: 2;
      width: min(16rem, 48%);
      padding: 1rem 1.1rem;
      border-radius: 1.35rem;
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid rgba(29, 29, 31, 0.06);
      backdrop-filter: blur(12px);
      box-shadow: 0 12px 32px rgba(29, 29, 31, 0.08);
    }

    .hero-signal p,
    .hero-signal strong {
      display: block;
      margin: 0;
    }

    .hero-signal p {
      font-size: 0.74rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .hero-signal strong {
      margin-top: 0.45rem;
      line-height: 1.45;
      font-size: 0.98rem;
    }

    .hero-track__label {
      margin: 0 0 1rem;
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.18em;
      color: rgba(29, 29, 31, 0.42);
    }

    .hero-track__rows {
      display: grid;
      gap: 0.85rem;
    }

    .hero-track__rows div,
    .snapshot-row {
      display: grid;
      grid-template-columns: 2.6rem minmax(0, 1fr);
      gap: 0.9rem;
      align-items: start;
      padding: 0.9rem 0;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
    }

    .hero-track__rows div:last-child,
    .snapshot-row:last-child {
      border-bottom: 0;
      padding-bottom: 0;
    }

    .hero-track__rows span {
      color: rgba(29, 29, 31, 0.42);
      font-size: 0.9rem;
      font-weight: 700;
    }

    .hero-track__rows strong,
    .snapshot-row strong {
      display: block;
      font-size: 1rem;
      line-height: 1.45;
    }

    .hero-track__rows em {
      display: block;
      margin-top: 0.22rem;
      font-style: normal;
      color: rgba(29, 29, 31, 0.56);
      font-size: 0.96rem;
    }

    .product-snapshot__label {
      color: rgba(29, 29, 31, 0.42);
    }

    .snapshot-row {
      grid-template-columns: minmax(0, 0.58fr) minmax(0, 1fr);
    }

    .snapshot-row span {
      color: rgba(29, 29, 31, 0.52);
      font-size: 0.94rem;
    }

    .hero__strata {
      position: absolute;
      inset: 0;
      overflow: hidden;
    }

    .strata {
      position: absolute;
      inset-inline: -8%;
      border-radius: 50%;
      opacity: 0.98;
      filter: blur(0.2px);
      transform-origin: center;
      animation: strataShift 10s ease-in-out infinite alternate;
    }

    .strata--a {
      inset-block-start: 14%;
      height: 32%;
      background: linear-gradient(90deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.3) 40%, rgba(0, 113, 227, 0.12));
    }

    .strata--b {
      inset-block-start: 42%;
      height: 26%;
      background: linear-gradient(90deg, rgba(0, 113, 227, 0.12), rgba(255, 255, 255, 0.16), rgba(255, 255, 255, 0));
      animation-duration: 19s;
    }

    .strata--c {
      inset-block-end: -8%;
      height: 34%;
      background: linear-gradient(90deg, rgba(229, 232, 238, 0.9), rgba(255, 255, 255, 0.36) 45%, rgba(214, 229, 255, 0.68));
      animation-duration: 22s;
    }

    .route-line {
      position: absolute;
      display: block;
      overflow: hidden;
    }

    .route-line::before,
    .route-line::after {
      content: "";
      position: absolute;
    }

    .route-line--hero {
      inset: auto 6% 8% 6%;
      height: 5rem;
    }

    .route-line--visual {
      inset: auto 8% 21% 8%;
      height: 2.8rem;
      z-index: 1;
    }

    .route-line--snapshot {
      inset: auto 12% 8% 12%;
      height: 2.2rem;
      z-index: 1;
    }

    .route-line--hero::before,
    .route-line--process::before,
    .route-line--visual::before,
    .route-line--snapshot::before {
      inset: 50% 0 auto;
      height: 1px;
      background: linear-gradient(90deg, rgba(29, 29, 31, 0), rgba(0, 113, 227, 0.26), rgba(29, 29, 31, 0));
      background-size: 180% 100%;
      animation: lineTravel 6.4s linear infinite;
      opacity: 0.7;
    }

    .route-line--hero::after,
    .route-line--process::after,
    .route-line--visual::after,
    .route-line--snapshot::after {
      display: none;
    }

    .proof-strip {
      position: relative;
      z-index: 1;
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 0;
      margin-bottom: 3.4rem;
      border-radius: 2rem;
      overflow: hidden;
      background: rgba(255, 255, 255, 0.82);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow);
      backdrop-filter: blur(12px);
    }

    .proof-strip::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, transparent 0, rgba(255, 255, 255, 0.34) 50%, transparent 100%);
      transform: translateX(-120%);
      animation: proofSweep 8.5s linear infinite;
      pointer-events: none;
    }

    .proof-strip__item {
      position: relative;
      padding: 1.15rem 1.2rem 1.2rem;
      min-width: 0;
    }

    .reveal.is-visible.proof-strip .proof-strip__item {
      animation: softLiftIn 760ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .reveal.is-visible.proof-strip .proof-strip__item:nth-child(2) {
      animation-delay: 0.08s;
    }

    .reveal.is-visible.proof-strip .proof-strip__item:nth-child(3) {
      animation-delay: 0.16s;
    }

    .reveal.is-visible.proof-strip .proof-strip__item:nth-child(4) {
      animation-delay: 0.24s;
    }

    .proof-strip__item:not(:last-child) {
      border-right: 1px solid rgba(29, 29, 31, 0.08);
    }

    .proof-strip__eyebrow {
      display: block;
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      font-weight: 800;
      color: rgba(29, 29, 31, 0.4);
    }

    .proof-strip__item strong {
      display: block;
      margin-top: 0.45rem;
      line-height: 1.35;
      font-size: 1rem;
      letter-spacing: -0.03em;
    }

    .section-cta {
      margin-top: 1.5rem;
    }

    .section-shell--premium {
      padding: 1.6rem;
      border: 1px solid rgba(29, 29, 31, 0.06);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.92), rgba(248, 248, 250, 0.82)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.035), transparent 42%, rgba(214, 229, 255, 0.14));
      box-shadow: var(--shadow);
    }

    .section-topline {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 1.35rem;
    }

    .section-topline .section-label {
      margin-bottom: 0;
    }

    .section-topline--tight {
      margin-bottom: 1.2rem;
    }

    .section-topline--stack {
      align-items: flex-start;
      gap: 1rem;
    }

    .section-topline__copy {
      display: grid;
      gap: 0.6rem;
      padding-top: 0.25rem;
    }

    .section-topline__copy h2 {
      margin: 0;
      font-size: clamp(2.4rem, 4.6vw, 4.8rem);
      line-height: 0.98;
      letter-spacing: -0.06em;
    }

    .section-kicker {
      display: block;
      margin: 0;
      padding-inline-start: 0.06em;
      font-size: 0.9rem;
      font-weight: 700;
      color: rgba(29, 29, 31, 0.5);
      line-height: 1.35;
    }

    .section-link {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ore);
    }

    .section-link::after {
      content: "->";
      transition: transform 180ms ease;
    }

    .section-link:hover::after {
      transform: translateX(0.18rem);
    }

    .section-block {
      padding: clamp(3.4rem, 6vw, 5.2rem) 0 0;
    }

    .section-shell,
    .contact-shell,
    .portfolio-group {
      position: relative;
      overflow: hidden;
      border-radius: 2.3rem;
    }

    .section-shell::before,
    .contact-shell::before {
      content: "";
      position: absolute;
      inset: auto auto -20% -12%;
      width: 38%;
      height: 70%;
      background: radial-gradient(circle, rgba(0, 113, 227, 0.1), rgba(255, 255, 255, 0) 72%);
      filter: blur(24px);
      opacity: 0.75;
      animation: ambientDrift 15s ease-in-out infinite alternate;
      pointer-events: none;
    }

    .section-shell > *,
    .contact-shell > * {
      position: relative;
      z-index: 1;
    }

    .section-shell {
      padding: 1.4rem 1.25rem 0;
    }

    .section-block--contrast .section-shell,
    .section-block--contact .section-shell {
      padding-top: 0;
    }

    .section-intro,
    .contact-copy,
    .portfolio-group__intro {
      max-width: 42rem;
      margin-bottom: 2rem;
    }

    .section-label,
    .footer-label,
    .family-label,
    .feature-row__eyebrow,
    .portfolio-row__eyebrow {
      color: rgba(29, 29, 31, 0.42);
    }

    .section-intro h2,
    .product-panel h2,
    .contact-copy h2 {
      max-width: 12ch;
      font-size: clamp(2.1rem, 5vw, 4.6rem);
      color: var(--ink);
    }

    .section-intro p,
    .contact-copy p,
    .portfolio-group__intro p {
      margin-top: 1rem;
      color: var(--ink-soft);
      max-width: 42rem;
    }

    .about-grid,
    .industry-grid,
    .product-overview,
    .product-specs,
    .footer-grid {
      display: grid;
      gap: 1rem;
    }

    .about-grid {
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }

    .home-hero {
      position: relative;
      z-index: 1;
      display: grid;
      gap: 2.2rem;
      min-height: 78vh;
      padding-bottom: 4rem;
    }

    .hero-copy--home {
      max-width: 54rem;
      margin: 0 auto;
      text-align: center;
    }

    .hero-copy--home h1,
    .hero-copy--home .hero-text {
      margin-inline: auto;
    }

    .hero-copy--home .hero-actions {
      justify-content: center;
    }

    body.is-ready .hero-copy > * {
      animation: softLiftIn 860ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    body.is-ready .hero-copy > *:nth-child(2) {
      animation-delay: 0.08s;
    }

    body.is-ready .hero-copy > *:nth-child(3) {
      animation-delay: 0.16s;
    }

    body.is-ready .hero-copy > *:nth-child(4) {
      animation-delay: 0.24s;
    }

    body.is-ready .hero-copy > *:nth-child(5) {
      animation-delay: 0.32s;
    }

    .home-poster {
      position: relative;
      display: grid;
      min-height: 28rem;
      will-change: transform;
      animation: surfaceFloat 9s ease-in-out infinite;
    }

    .home-poster__surface {
      position: relative;
      min-height: 28rem;
      padding: 1.55rem;
      border-radius: calc(var(--radius-xl) + 0.45rem);
      background:
        radial-gradient(circle at 18% 12%, rgba(255, 255, 255, 0.96), transparent 26%),
        linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(246, 246, 248, 0.92));
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow-lg);
      overflow: hidden;
      backdrop-filter: blur(16px);
    }

    .home-poster__surface::before,
    .product-poster__surface::before {
      content: "";
      position: absolute;
      inset: -20% -12%;
      background:
        radial-gradient(circle at 18% 24%, rgba(0, 113, 227, 0.1), transparent 24%),
        radial-gradient(circle at 76% 68%, rgba(0, 113, 227, 0.08), transparent 28%),
        linear-gradient(120deg, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.34) 45%, rgba(255, 255, 255, 0) 75%);
      opacity: 0.9;
      transform: translate3d(-3%, 0, 0);
      animation: ambientSweep 12s cubic-bezier(0.22, 1, 0.36, 1) infinite alternate;
      pointer-events: none;
    }

    .home-poster__surface::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(120deg, transparent 24%, rgba(255, 255, 255, 0.48) 50%, transparent 72%);
      transform: translateX(-120%);
      animation: specimenSweep 7.5s cubic-bezier(0.22, 1, 0.36, 1) infinite;
      pointer-events: none;
    }

    .home-poster__summary,
    .home-poster__metrics {
      position: relative;
      z-index: 2;
    }

    .home-poster__summary {
      max-width: 30rem;
      padding: 1.2rem 0 0;
    }

    .home-poster__eyebrow {
      margin: 0;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .home-poster__summary strong {
      display: block;
      margin-top: 0.65rem;
      max-width: 12ch;
      font-size: clamp(2.2rem, 3.4vw, 3.3rem);
      line-height: 0.94;
      letter-spacing: -0.06em;
    }

    .home-poster__summary p:last-child {
      margin: 0.95rem 0 0;
      max-width: 28rem;
      color: rgba(29, 29, 31, 0.62);
      line-height: 1.66;
      font-size: 1rem;
    }

    .home-poster__metrics {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 0;
      margin-top: 7.1rem;
      padding-top: 1.2rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .home-metric {
      padding: 0 1.05rem;
      min-width: 0;
      animation: none;
    }

    .home-metric:first-child {
      padding-left: 0;
    }

    .home-metric:not(:last-child) {
      border-right: 1px solid rgba(29, 29, 31, 0.08);
    }

    .home-metric span {
      display: block;
      margin-bottom: 0.38rem;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .home-metric strong {
      display: block;
      max-width: 18ch;
      line-height: 1.35;
      font-size: 1.04rem;
      letter-spacing: -0.03em;
    }

    body.is-ready .home-poster__summary {
      animation: softLiftIn 900ms cubic-bezier(0.22, 1, 0.36, 1) 0.18s both;
    }

    body.is-ready .home-poster__metrics {
      animation: softLiftIn 900ms cubic-bezier(0.22, 1, 0.36, 1) 0.28s both;
    }

    .home-ledger {
      display: grid;
      grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
      gap: 2.4rem;
      align-items: start;
      padding-top: 1rem;
    }

    .home-ledger__intro {
      max-width: 34rem;
    }

    .home-ledger__intro h2 {
      margin: 0;
      font-size: clamp(2.6rem, 5vw, 5rem);
      line-height: 0.98;
      letter-spacing: -0.06em;
    }

    .home-ledger__intro p {
      margin: 1.1rem 0 0;
      line-height: 1.78;
      color: var(--ink-soft);
    }

    .home-ledger__rows {
      display: grid;
      gap: 0;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .home-ledger-row {
      display: grid;
      grid-template-columns: 2.6rem minmax(0, 1fr);
      gap: 1rem;
      padding: 1.25rem 0;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
    }

    .home-ledger-row span {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 2.3rem;
      height: 2.3rem;
      border-radius: 999px;
      background: rgba(0, 113, 227, 0.08);
      color: var(--ore);
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.08em;
    }

    .home-ledger-row strong {
      display: block;
      margin: 0 0 0.32rem;
      font-size: 1.08rem;
      line-height: 1.35;
      letter-spacing: -0.03em;
    }

    .home-ledger-row p {
      margin: 0;
      line-height: 1.72;
      color: var(--ink-soft);
    }

    .reveal.is-visible.home-ledger-row {
      animation: softLiftIn 780ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .home-family-list {
      display: grid;
      gap: 0;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .home-family-row {
      position: relative;
      display: grid;
      grid-template-columns: 4.2rem minmax(0, 1fr) auto;
      gap: 1.5rem;
      align-items: center;
      padding: 1.7rem 0;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
      transition: transform 200ms ease, border-color 200ms ease;
    }

    .home-family-row::after {
      content: "";
      position: absolute;
      left: 0;
      right: 22%;
      bottom: -1px;
      height: 1px;
      background: linear-gradient(90deg, rgba(0, 113, 227, 0.72), rgba(0, 113, 227, 0));
      background-size: 180% 100%;
      transform: scaleX(0.22);
      transform-origin: left center;
      transition: transform 700ms cubic-bezier(0.22, 1, 0.36, 1);
      animation: lineTravel 4.8s linear infinite;
      opacity: 0.42;
    }

    .home-family-row:hover,
    .home-family-row:focus-visible {
      transform: translateX(0.22rem);
    }

    .home-family-row:hover::after,
    .home-family-row:focus-visible::after {
      transform: scaleX(1);
      opacity: 0.9;
    }

    .home-family-row__index {
      display: block;
      font-size: clamp(2rem, 4vw, 3rem);
      line-height: 0.9;
      letter-spacing: -0.08em;
      font-weight: 800;
      color: rgba(29, 29, 31, 0.14);
    }

    .home-family-row__count {
      margin: 0 0 0.45rem;
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .home-family-row__main h3 {
      margin: 0;
      font-size: clamp(2rem, 3.4vw, 3.2rem);
      line-height: 0.95;
      letter-spacing: -0.07em;
    }

    .home-family-row__main p {
      margin: 0.8rem 0 0;
      max-width: 38rem;
      color: var(--ink-soft);
      line-height: 1.72;
    }

    .home-family-row__products {
      display: flex;
      flex-wrap: wrap;
      gap: 0.7rem;
      margin-top: 1rem;
    }

    .home-family-row__product {
      display: inline-flex;
      align-items: center;
      gap: 0.72rem;
      min-height: 2.65rem;
      padding: 0.64rem 0.78rem 0.64rem 0.96rem;
      border-radius: 999px;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background: rgba(255, 255, 255, 0.9);
      color: rgba(29, 29, 31, 0.76);
      font-size: 0.9rem;
      font-weight: 700;
      box-shadow: 0 12px 24px rgba(29, 29, 31, 0.05);
      transition: transform 180ms ease, background-color 180ms ease, border-color 180ms ease, box-shadow 180ms ease, color 180ms ease;
    }

    .home-family-row__product span {
      line-height: 1.2;
    }

    .home-family-row__product em {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 2rem;
      height: 2rem;
      border-radius: 999px;
      background: rgba(0, 113, 227, 0.08);
      color: var(--ore);
      font-style: normal;
      font-size: 1rem;
      font-weight: 800;
      line-height: 1;
      transition: transform 180ms ease, background-color 180ms ease, color 180ms ease;
    }

    .home-family-row__product:hover,
    .home-family-row__product:focus-visible {
      transform: translateY(-1px);
      background: white;
      border-color: rgba(0, 113, 227, 0.16);
      box-shadow: 0 16px 32px rgba(29, 29, 31, 0.08);
      color: var(--ink);
    }

    .home-family-row__product:hover em,
    .home-family-row__product:focus-visible em {
      transform: translateX(0.08rem);
      background: rgba(0, 113, 227, 0.12);
    }

    .home-family-row__cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 8rem;
      min-height: 2.95rem;
      padding: 0.7rem 1rem;
      border-radius: 999px;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background: rgba(255, 255, 255, 0.9);
      color: var(--ore);
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      transition: transform 180ms ease, background-color 180ms ease, color 180ms ease, border-color 180ms ease;
    }

    .home-family-row:hover .home-family-row__cta,
    .home-family-row:focus-visible .home-family-row__cta {
      transform: translateX(0.16rem);
      background: var(--ore);
      border-color: transparent;
      color: white;
    }

    .reveal.is-visible.home-family-row {
      animation: softLiftIn 820ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .home-split {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 3rem;
      align-items: start;
      padding-top: 1rem;
    }

    .home-split--stack {
      grid-template-columns: 1fr;
      gap: 2.1rem;
      max-width: 72rem;
    }

    .home-split__panel {
      padding-top: 1.2rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .home-split__panel h2 {
      margin: 0;
      max-width: 10ch;
      font-size: clamp(2.4rem, 4.5vw, 4.6rem);
      line-height: 0.96;
      letter-spacing: -0.06em;
    }

    .home-split__panel > p:last-of-type {
      margin: 1rem 0 0;
      color: var(--ink-soft);
      line-height: 1.72;
    }

    .home-process-list {
      display: grid;
      gap: 0;
      margin-top: 1.4rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .home-process-list .process-step {
      display: grid;
      grid-template-columns: 2.6rem minmax(0, 1fr);
      gap: 1rem;
      padding: 1.1rem 0;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
      background: transparent;
      box-shadow: none;
      border-radius: 0;
      border-left: 0;
      border-right: 0;
      border-top: 0;
      min-height: 0;
    }

    .home-process-list .process-step span {
      margin-bottom: 0;
    }

    .home-process-list .process-step__body {
      min-width: 0;
    }

    .home-process-list .process-step h3 {
      margin: 0 0 0.35rem;
      font-size: 1.06rem;
      line-height: 1.35;
      letter-spacing: -0.03em;
    }

    .home-process-list .process-step p {
      margin: 0;
    }

    .reveal.is-visible.process-step {
      animation: softLiftIn 780ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .reveal.is-visible.process-step:nth-child(2) {
      animation-delay: 0.08s;
    }

    .reveal.is-visible.process-step:nth-child(3) {
      animation-delay: 0.16s;
    }

    .reveal.is-visible.process-step:nth-child(4) {
      animation-delay: 0.24s;
    }

    .corridor-stage {
      position: relative;
      overflow: hidden;
      padding: 1.35rem;
      border-radius: calc(var(--radius-xl) + 0.25rem);
      background:
        radial-gradient(circle at 16% 18%, rgba(96, 157, 233, 0.2), transparent 24%),
        radial-gradient(circle at 86% 72%, rgba(78, 134, 218, 0.18), transparent 24%),
        linear-gradient(180deg, #0e2039 0%, #102746 54%, #143055 100%);
      border: 1px solid rgba(255, 255, 255, 0.08);
      box-shadow: 0 28px 56px rgba(5, 13, 24, 0.22);
    }

    .corridor-stage::before,
    .corridor-stage::after {
      content: "";
      position: absolute;
      inset: 0;
      pointer-events: none;
    }

    .corridor-stage::before {
      background:
        linear-gradient(90deg, rgba(255, 255, 255, 0.04) 1px, transparent 1px),
        linear-gradient(180deg, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
      background-size: 7.5rem 7.5rem;
      mask-image: linear-gradient(180deg, rgba(0, 0, 0, 0.34), rgba(0, 0, 0, 0.08));
    }

    .corridor-stage::after {
      background:
        radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.1), transparent 18%),
        radial-gradient(circle at 72% 24%, rgba(255, 255, 255, 0.08), transparent 16%);
      opacity: 0.75;
    }

    .corridor-stage__top,
    .corridor-stage__body {
      position: relative;
      z-index: 1;
    }

    .corridor-stage__top {
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 1.5rem;
      padding-bottom: 1.2rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    }

    .corridor-stage__intro {
      max-width: 44rem;
    }

    .corridor-stage__top .section-label {
      margin: 0;
      color: rgba(225, 236, 252, 0.62);
    }

    .corridor-stage__top h2 {
      margin: 0;
      max-width: 12ch;
      color: rgba(255, 255, 255, 0.98);
      font-size: clamp(2.4rem, 4.6vw, 4.8rem);
      line-height: 0.95;
      letter-spacing: -0.07em;
    }

    .corridor-stage__top p:last-child {
      margin: 1rem 0 0;
      color: rgba(226, 235, 247, 0.76);
      line-height: 1.74;
    }

    .corridor-stage__body {
      display: grid;
      grid-template-columns: minmax(0, 0.4fr) minmax(0, 0.6fr);
      gap: 2rem;
      align-items: start;
      padding-top: 1.4rem;
    }

    .corridor-stage__hub {
      position: relative;
      min-height: 100%;
      padding: 1.45rem;
      border-radius: 1.6rem;
      border: 1px solid rgba(255, 255, 255, 0.1);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.03)),
        radial-gradient(circle at 24% 18%, rgba(150, 198, 255, 0.16), transparent 34%);
      box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08);
    }

    .corridor-stage__eyebrow {
      margin: 0 0 1rem;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(229, 237, 249, 0.56);
    }

    .corridor-stage__hub-mark {
      position: relative;
      width: 8.8rem;
      aspect-ratio: 1;
      margin-bottom: 1.35rem;
      display: grid;
      place-items: center;
    }

    .corridor-stage__hub-ring,
    .corridor-stage__hub-core {
      position: absolute;
      border-radius: 50%;
    }

    .corridor-stage__hub-ring--outer {
      inset: 0;
      border: 1px solid rgba(190, 222, 255, 0.18);
      animation: corridorHubOrbit 7.6s linear infinite;
    }

    .corridor-stage__hub-ring--inner {
      inset: 18%;
      border: 1px solid rgba(221, 236, 255, 0.3);
      animation: corridorHubPulse 3.1s ease-in-out infinite;
    }

    .corridor-stage__hub-core {
      inset: 35%;
      background:
        radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 1), rgba(218, 235, 255, 0.98) 54%, rgba(110, 168, 244, 0.96) 100%);
      box-shadow:
        0 0 0 0.55rem rgba(142, 193, 255, 0.12),
        0 0 2.5rem rgba(148, 201, 255, 0.24);
    }

    .corridor-stage__hub h3 {
      margin: 0;
      color: rgba(255, 255, 255, 0.98);
      font-size: clamp(1.5rem, 2.4vw, 2rem);
      line-height: 1.02;
      letter-spacing: -0.05em;
    }

    .corridor-stage__hub p:last-child {
      margin: 0.8rem 0 0;
      max-width: 22rem;
      color: rgba(228, 236, 247, 0.72);
      line-height: 1.72;
    }

    .corridor-stage__lanes {
      display: grid;
      gap: 0.9rem;
    }

    .corridor-lane {
      width: 100%;
      padding: 0;
      border: 0;
      background: transparent;
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(14rem, 18.5rem);
      align-items: center;
      gap: 1rem;
      color: inherit;
      text-align: left;
      cursor: pointer;
    }

    .corridor-lane__rail {
      position: relative;
      display: block;
      min-width: 0;
      height: 3.4rem;
    }

    .corridor-lane__track,
    .corridor-lane__glow {
      position: absolute;
      left: 0;
      right: 0.25rem;
      top: 50%;
      height: 2px;
      border-radius: 999px;
      transform: translateY(-50%);
    }

    .corridor-lane__track {
      background: linear-gradient(90deg, rgba(190, 219, 255, 0.14), rgba(190, 219, 255, 0.26) 54%, rgba(190, 219, 255, 0.1));
    }

    .corridor-lane__glow {
      background: linear-gradient(90deg, rgba(255, 255, 255, 0), rgba(204, 230, 255, 0.92) 36%, rgba(204, 230, 255, 0));
      transform: translateY(-50%) scaleX(0.18);
      transform-origin: left center;
      opacity: 0;
      transition: transform 520ms cubic-bezier(0.22, 1, 0.36, 1), opacity 320ms ease;
    }

    .corridor-lane__terminal {
      position: absolute;
      right: 0;
      top: 50%;
      width: 0.8rem;
      height: 0.8rem;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.92);
      box-shadow: 0 0 0 0.32rem rgba(191, 224, 255, 0.1);
      transform: translateY(-50%);
    }

    .corridor-lane__ship {
      position: absolute;
      top: 50%;
      left: 0;
      width: 2.05rem;
      height: 1.35rem;
      transform: translate(-0.15rem, -50%);
      opacity: 0;
    }

    .corridor-lane__ship::before,
    .corridor-lane__ship::after {
      content: "";
      position: absolute;
    }

    .corridor-lane__ship::before {
      inset: auto 0 0 0;
      height: 0.68rem;
      background: rgba(255, 255, 255, 0.96);
      clip-path: polygon(0 35%, 76% 35%, 100% 58%, 88% 100%, 14% 100%);
      filter: drop-shadow(0 8px 12px rgba(3, 8, 15, 0.28));
    }

    .corridor-lane__ship::after {
      left: 0.76rem;
      top: 0.04rem;
      width: 0.42rem;
      height: 0.52rem;
      border-radius: 0.16rem 0.16rem 0 0;
      background: rgba(255, 255, 255, 0.96);
      box-shadow: 0.48rem 0.12rem 0 -0.08rem rgba(191, 223, 255, 0.94);
    }

    .corridor-lane__card {
      display: grid;
      gap: 0.18rem;
      padding: 0.95rem 1rem;
      border-radius: 1.35rem;
      border: 1px solid rgba(255, 255, 255, 0.09);
      background: rgba(255, 255, 255, 0.05);
      box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
      transition: background-color 220ms ease, border-color 220ms ease, transform 220ms ease, box-shadow 220ms ease;
    }

    .corridor-lane__meta {
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(226, 236, 250, 0.56);
    }

    .corridor-lane__card strong {
      font-size: 1.1rem;
      line-height: 1.15;
      letter-spacing: -0.03em;
      color: rgba(255, 255, 255, 0.98);
    }

    .corridor-lane__countries {
      color: rgba(224, 234, 247, 0.72);
      line-height: 1.55;
    }

    .corridor-lane:hover .corridor-lane__card,
    .corridor-lane:focus-visible .corridor-lane__card {
      transform: translateY(-1px);
      border-color: rgba(196, 225, 255, 0.22);
    }

    .corridor-lane:focus-visible {
      outline: none;
    }

    .corridor-lane.is-active .corridor-lane__glow {
      opacity: 1;
      transform: translateY(-50%) scaleX(1);
    }

    .corridor-lane.is-active .corridor-lane__ship {
      opacity: 1;
      animation: corridorShipTravel 3.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) infinite;
    }

    .corridor-lane.is-active .corridor-lane__terminal {
      animation: corridorTerminalPulse 2.4s ease-out infinite;
    }

    .corridor-lane.is-active .corridor-lane__card {
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.14), rgba(255, 255, 255, 0.08)),
        radial-gradient(circle at 12% 16%, rgba(152, 205, 255, 0.14), transparent 34%);
      border-color: rgba(204, 231, 255, 0.2);
      box-shadow:
        inset 0 1px 0 rgba(255, 255, 255, 0.08),
        0 18px 28px rgba(6, 16, 29, 0.18);
    }

    .relationship-band {
      max-width: 62rem;
      padding: 1.4rem 0 0.2rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .relationship-band h2 {
      margin: 0;
      font-size: clamp(2rem, 4.2vw, 3.8rem);
      line-height: 0.97;
      letter-spacing: -0.05em;
    }

    .relationship-band p {
      margin: 0.95rem 0 0;
      color: var(--ink-soft);
      max-width: 44rem;
      line-height: 1.72;
    }

    .ceo-spotlight {
      max-width: 68rem;
      padding-top: 1rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .ceo-spotlight__grid {
      display: grid;
      grid-template-columns: minmax(0, 1.08fr) minmax(19rem, 0.72fr);
      gap: 2.2rem;
      align-items: start;
    }

    .ceo-spotlight__content {
      min-width: 0;
    }

    .ceo-spotlight h2 {
      margin: 0;
      max-width: 13ch;
      font-size: clamp(2.4rem, 4.8vw, 4.8rem);
      line-height: 0.96;
      letter-spacing: -0.06em;
    }

    .ceo-spotlight__quote {
      margin: 1.2rem 0 0;
      font-size: clamp(1.7rem, 3.5vw, 3rem);
      line-height: 1.02;
      letter-spacing: -0.05em;
      font-weight: 800;
      color: var(--ink);
    }

    .ceo-spotlight__body {
      display: grid;
      gap: 1rem;
      margin-top: 1.2rem;
      max-width: 46rem;
    }

    .ceo-spotlight__body p {
      margin: 0;
      line-height: 1.75;
      color: var(--ink-soft);
    }

    .ceo-spotlight__meta {
      margin: 1.35rem 0 0;
      color: rgba(29, 29, 31, 0.92);
      font-weight: 700;
      line-height: 1.55;
      display: grid;
      gap: 0.08rem;
      padding-inline-start: 0.04em;
    }

    .ceo-spotlight__actions {
      margin-top: 1.15rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .ceo-spotlight__media {
      position: relative;
      margin: 0;
      border-radius: calc(var(--radius-lg) + 0.1rem);
      overflow: hidden;
      border: 1px solid rgba(29, 29, 31, 0.06);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(243, 245, 248, 0.9)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.05), transparent 46%);
      box-shadow: var(--shadow-lg);
      aspect-ratio: 4 / 4.3;
    }

    .ceo-spotlight__media::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(120deg, transparent 24%, rgba(255, 255, 255, 0.34) 50%, transparent 74%);
      transform: translateX(-120%);
      animation: specimenSweep 8.5s cubic-bezier(0.22, 1, 0.36, 1) infinite;
      pointer-events: none;
    }

    .ceo-spotlight__media img {
      width: 100%;
      height: 100%;
      display: block;
      object-fit: cover;
      object-position: center top;
      transform: scale(1.01);
    }

    .reveal.is-visible.ceo-spotlight__grid > * {
      animation: softLiftIn 820ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .reveal.is-visible.ceo-spotlight__grid > *:nth-child(2) {
      animation-delay: 0.08s;
    }

    .operating-stage {
      display: grid;
      grid-template-columns: minmax(0, 0.86fr) minmax(0, 1.14fr);
      gap: 2rem;
      align-items: start;
    }

    .operating-stage__intro {
      max-width: 34rem;
    }

    .operating-stage__intro h2 {
      margin: 0;
      font-size: clamp(2.6rem, 5vw, 5rem);
      line-height: 0.98;
      letter-spacing: -0.06em;
    }

    .operating-stage__intro p {
      margin: 1.15rem 0 0;
      line-height: 1.78;
      color: var(--ink-soft);
      max-width: 33rem;
    }

    .operating-stage__cards {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 1rem;
    }

    .operating-card {
      position: relative;
      min-height: 13rem;
      padding: 1.45rem;
      border-radius: calc(var(--radius-lg) + 0.1rem);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.88), rgba(250, 250, 252, 0.78)),
        linear-gradient(140deg, rgba(0, 113, 227, 0.04), transparent 45%);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow);
      overflow: hidden;
      transition: transform 220ms ease, box-shadow 220ms ease;
    }

    .operating-card::after {
      content: "";
      position: absolute;
      inset: auto -20% -34% auto;
      width: 11rem;
      height: 11rem;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(0, 113, 227, 0.08), transparent 66%);
      filter: blur(6px);
    }

    .operating-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 24px 70px rgba(29, 29, 31, 0.1);
    }

    .operating-card__index {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 2.2rem;
      height: 2.2rem;
      border-radius: 999px;
      background: rgba(0, 113, 227, 0.08);
      color: var(--ore);
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.1em;
    }

    .operating-card h3,
    .split-stage__panel h2 {
      margin: 1rem 0 0.7rem;
      font-size: 1.34rem;
      line-height: 1.18;
      letter-spacing: -0.04em;
    }

    .operating-card p {
      margin: 0;
      line-height: 1.72;
      color: var(--ink-soft);
    }

    .about-point,
    .industry-item,
    .product-panel,
    .process-step,
    .portfolio-row,
    .feature-row,
    .contact-shell,
    .faq-item,
    .portfolio-group {
      background: rgba(255, 255, 255, 0.86);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow);
    }

    .about-point,
    .industry-item,
    .product-panel,
    .process-step,
    .portfolio-group {
      padding: 1.5rem;
      border-radius: var(--radius-lg);
    }

    .about-point h3,
    .industry-item h3,
    .process-step h3,
    .feature-row h3,
    .portfolio-row h3 {
      margin: 0 0 0.7rem;
      font-size: 1.22rem;
      line-height: 1.3;
      letter-spacing: -0.04em;
    }

    .about-point p,
    .industry-item p,
    .process-step p {
      color: var(--ink-soft);
    }

    .ceo-note {
      display: grid;
      grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
      gap: 2rem;
      align-items: start;
      padding: 1.8rem;
      border-radius: calc(var(--radius-xl) + 0.15rem);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.9), rgba(248, 248, 250, 0.82)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.04), transparent 40%, rgba(214, 229, 255, 0.18));
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
    }

    .ceo-note::after {
      content: "";
      position: absolute;
      inset: auto -8% -28% auto;
      width: 18rem;
      height: 18rem;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(0, 113, 227, 0.08), transparent 66%);
      filter: blur(8px);
    }

    .ceo-note__lead,
    .ceo-note__body {
      position: relative;
      z-index: 1;
    }

    .ceo-note__quote {
      margin: 1.4rem 0 0;
      font-size: clamp(1.5rem, 3.2vw, 2.5rem);
      line-height: 1.05;
      letter-spacing: -0.05em;
      font-weight: 800;
      color: var(--ink);
    }

    .ceo-note__body {
      display: grid;
      gap: 1rem;
    }

    .ceo-note__body p {
      margin: 0;
      line-height: 1.75;
      color: var(--ink-soft);
    }

    .ceo-note__meta {
      padding-top: 0.8rem;
      color: rgba(29, 29, 31, 0.92) !important;
      font-weight: 700;
    }

    .family-bands {
      display: grid;
      gap: 1rem;
    }

    .family-band {
      display: grid;
      grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr);
      gap: 1.25rem;
      align-items: center;
      padding: 1.7rem 1.7rem 2.35rem;
      border-radius: calc(var(--radius-lg) + 0.25rem);
      border: 1px solid rgba(29, 29, 31, 0.06);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.84), rgba(250, 250, 252, 0.78)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.04), transparent 42%, rgba(214, 229, 255, 0.18));
      box-shadow: var(--shadow);
      transition: transform 180ms ease, box-shadow 180ms ease;
      position: relative;
      overflow: hidden;
    }

    .family-band::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(110deg, transparent 30%, rgba(255, 255, 255, 0.52) 48%, transparent 66%);
      transform: translateX(-120%);
      transition: transform 700ms cubic-bezier(0.22, 1, 0.36, 1);
      pointer-events: none;
    }

    .family-band:hover,
    .portfolio-row:hover,
    .feature-row:hover {
      transform: translateY(-2px);
      box-shadow: 0 24px 70px rgba(29, 29, 31, 0.1);
    }

    .family-band:hover::after {
      transform: translateX(120%);
    }

    .family-band__head h3 {
      margin: 0 0 0.7rem;
      font-size: 1.95rem;
      line-height: 1.05;
      letter-spacing: -0.05em;
    }

    .family-band__head {
      display: grid;
      gap: 0.75rem;
    }

    .family-copy {
      color: var(--ink-soft);
      max-width: 30rem;
    }

    .family-band__meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding-top: 0.15rem;
    }

    .family-band__meta span {
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.4);
    }

    .family-band__cta {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      width: fit-content;
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--ore);
    }

    .family-band__cta::after {
      content: "->";
      transition: transform 180ms ease;
    }

    .family-band:hover .family-band__cta::after {
      transform: translateX(0.16rem);
    }

    .family-band__beam {
      position: absolute;
      left: 1.7rem;
      right: 1.7rem;
      bottom: 1rem;
      height: 1px;
      background: linear-gradient(90deg, rgba(0, 113, 227, 0.32), rgba(29, 29, 31, 0.04));
      overflow: hidden;
    }

    .family-band__beam::after {
      content: "";
      position: absolute;
      top: -0.35rem;
      left: 0;
      width: 0.72rem;
      height: 0.72rem;
      border-radius: 50%;
      background: linear-gradient(180deg, #53a3ff, #0071e3);
      box-shadow: 0 0 0 0 rgba(0, 113, 227, 0.18);
      animation: bandRoute 5.8s linear infinite;
    }

    .family-band__links,
    .related-links {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      align-items: center;
    }

    .product-link,
    .related-links a {
      position: relative;
      display: inline-flex;
      align-items: center;
      gap: 0.7rem;
      min-height: 3.5rem;
      padding: 0.85rem 1.05rem 0.85rem 1.15rem;
      border-radius: 999px;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background: rgba(255, 255, 255, 0.74);
      font-size: 0.95rem;
      font-weight: 700;
      transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease, background-color 180ms ease;
      overflow: hidden;
    }

    .product-link::before {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(110deg, transparent 20%, rgba(255, 255, 255, 0.55) 50%, transparent 80%);
      transform: translateX(-130%);
      transition: transform 720ms cubic-bezier(0.22, 1, 0.36, 1);
      pointer-events: none;
    }

    .product-link:hover,
    .product-link:focus-visible,
    .related-links a:hover,
    .related-links a:focus-visible {
      transform: translateY(-2px);
      box-shadow: 0 16px 38px rgba(29, 29, 31, 0.08);
      border-color: rgba(0, 113, 227, 0.18);
      background: rgba(255, 255, 255, 0.96);
    }

    .product-link:hover::before,
    .product-link:focus-visible::before {
      transform: translateX(130%);
    }

    .product-link__name,
    .product-link__arrow {
      position: relative;
      z-index: 1;
    }

    .product-link__arrow {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 1.9rem;
      height: 1.9rem;
      border-radius: 999px;
      background: rgba(0, 113, 227, 0.08);
      color: var(--ore);
      font-size: 0.88rem;
      line-height: 1;
      transition: transform 180ms ease, background-color 180ms ease, color 180ms ease;
      animation: arrowDrift 3.8s ease-in-out infinite;
    }

    .product-link:hover .product-link__arrow,
    .product-link:focus-visible .product-link__arrow {
      transform: translateX(0.2rem);
      background: var(--ore);
      color: white;
    }

    .grade-sheet-block {
      display: grid;
      gap: 0.85rem;
      margin-top: 1.25rem;
      padding-top: 1.15rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .grade-sheet-block__head {
      display: grid;
      gap: 0.35rem;
    }

    .grade-sheet-block__label,
    .grade-sheet-block__copy {
      margin: 0;
    }

    .grade-sheet-block__label {
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .grade-sheet-block__copy {
      max-width: 42rem;
      line-height: 1.6;
      color: var(--ink-soft);
    }

    .grade-sheet-block__actions {
      display: flex;
      flex-wrap: wrap;
      gap: 0.72rem;
    }

    .grade-sheet-block__actions .button {
      text-decoration: none;
    }

    .buyer-guides-holder {
      display: flex;
      justify-content: flex-end;
      align-items: flex-start;
      padding-right: clamp(0rem, 2.6vw, 1.2rem);
    }

    .buyer-guides-strip {
      position: relative;
      width: min(18.5rem, 100%);
      aspect-ratio: 1 / 1;
      padding: 1rem;
      border-radius: 1.6rem;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(247, 248, 251, 0.92)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.04), transparent 42%);
      box-shadow: var(--shadow);
      display: grid;
      grid-template-rows: auto 1fr;
    }

    .buyer-guides-strip__head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.9rem;
      margin-bottom: 0.72rem;
    }

    .buyer-guides-strip__head .section-kicker {
      margin: 0;
    }

    .buyer-guides-marquee {
      position: relative;
      overflow: hidden;
      border-radius: 1.1rem;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background: rgba(255, 255, 255, 0.74);
      padding: 0.5rem 0;
      align-self: stretch;
      display: flex;
      align-items: center;
    }

    .buyer-guides-marquee::before,
    .buyer-guides-marquee::after {
      content: "";
      position: absolute;
      top: 0;
      bottom: 0;
      width: 4rem;
      z-index: 2;
      pointer-events: none;
    }

    .buyer-guides-marquee::before {
      left: 0;
      background: linear-gradient(90deg, rgba(255, 255, 255, 0.96), rgba(255, 255, 255, 0));
    }

    .buyer-guides-marquee::after {
      right: 0;
      background: linear-gradient(270deg, rgba(255, 255, 255, 0.96), rgba(255, 255, 255, 0));
    }

    .buyer-guides-marquee__track {
      width: max-content;
      display: flex;
      align-items: center;
      gap: 0.62rem;
      padding: 0 0.6rem;
      animation: buyerGuidesScroll 84s linear infinite;
    }

    .buyer-guides-marquee:hover .buyer-guides-marquee__track {
      animation-play-state: paused;
    }

    .buyer-guide-pill {
      display: inline-flex;
      align-items: center;
      min-height: 2.2rem;
      padding: 0.45rem 0.9rem;
      border-radius: 999px;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background: rgba(255, 255, 255, 0.92);
      color: var(--ink);
      font-size: 0.84rem;
      font-weight: 700;
      line-height: 1.25;
      white-space: nowrap;
      text-decoration: none;
      transition: transform 180ms ease, border-color 180ms ease, color 180ms ease, background-color 180ms ease;
    }

    .buyer-guide-pill:hover,
    .buyer-guide-pill:focus-visible {
      transform: translateY(-1px);
      border-color: rgba(0, 113, 227, 0.24);
      color: var(--ore);
      background: rgba(245, 250, 255, 0.94);
    }

    .blog-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 1rem;
      align-items: start;
    }

    .blog-grid--compact .blog-card {
      min-height: auto;
    }

    .blog-card {
      position: relative;
      display: grid;
      gap: 0.75rem;
      min-height: 100%;
      padding: 1.25rem 1.2rem;
      border-radius: 1.4rem;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(247, 248, 251, 0.92)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.05), transparent 42%);
      box-shadow: 0 12px 28px rgba(29, 29, 31, 0.06);
      transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    }

    .blog-card:hover,
    .blog-card:focus-visible {
      transform: translateY(-2px);
      box-shadow: 0 18px 34px rgba(29, 29, 31, 0.08);
      border-color: rgba(0, 113, 227, 0.2);
    }

    a.blog-card {
      color: var(--ink);
      text-decoration: none;
    }

    .blog-card__eyebrow {
      margin: 0;
      font-size: 0.66rem;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      font-weight: 800;
      color: rgba(29, 29, 31, 0.44);
    }

    .blog-card h3 {
      margin: 0;
      line-height: 1.16;
      letter-spacing: -0.03em;
      font-size: clamp(1.15rem, 1.55vw, 1.42rem);
    }

    .blog-card p {
      margin: 0;
      color: var(--ink-soft);
      line-height: 1.66;
    }

    .blog-card__actions {
      margin-top: 0.35rem;
      display: flex;
      flex-wrap: wrap;
      gap: 0.55rem;
    }

    .blog-card__link {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 2.4rem;
      padding: 0.5rem 0.9rem;
      border-radius: 999px;
      font-size: 0.84rem;
      font-weight: 800;
      color: var(--ore);
      border: 1px solid rgba(0, 113, 227, 0.2);
      background: rgba(240, 246, 255, 0.78);
      text-decoration: none;
      transition: transform 180ms ease, border-color 180ms ease, background-color 180ms ease;
    }

    .blog-card__link--alt {
      color: rgba(29, 29, 31, 0.72);
      border-color: rgba(29, 29, 31, 0.12);
      background: rgba(255, 255, 255, 0.92);
    }

    .blog-card__link:hover,
    .blog-card__link:focus-visible {
      transform: translateY(-1px);
      border-color: rgba(0, 113, 227, 0.32);
      background: rgba(240, 246, 255, 1);
    }

    .blog-layout {
      display: grid;
      grid-template-columns: minmax(0, 1.35fr) minmax(0, 0.85fr);
      gap: 1rem;
      align-items: start;
    }

    .blog-article,
    .blog-sidecard {
      position: relative;
      padding: 1.3rem;
      border-radius: 1.55rem;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(247, 248, 251, 0.92)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.05), transparent 42%);
      box-shadow: var(--shadow);
    }

    .blog-article-section + .blog-article-section {
      margin-top: 1.4rem;
      padding-top: 1.35rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .blog-article-section h2 {
      margin: 0 0 0.6rem;
      font-size: clamp(1.4rem, 2.2vw, 2rem);
      letter-spacing: -0.04em;
      line-height: 1.08;
    }

    .blog-article-section p {
      margin: 0;
      line-height: 1.72;
      color: var(--ink-soft);
    }

    .blog-sidecard {
      top: 6.2rem;
      position: sticky;
    }

    .blog-sidecard h2 {
      margin: 0 0 0.85rem;
      font-size: clamp(1.4rem, 2.1vw, 2rem);
      letter-spacing: -0.04em;
      line-height: 1.08;
    }

    .blog-sidecard__links {
      margin-top: 1rem;
    }

    .process-media-grid {
      display: grid;
      gap: 1rem;
      margin-top: 1.5rem;
      align-items: start;
    }

    .process-media-grid--dispatch {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .process-media-grid--operations {
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }

    .process-media-card {
      min-width: 0;
      display: grid;
      grid-template-rows: auto 1fr;
      border-radius: calc(var(--radius-lg) + 0.1rem);
      overflow: hidden;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(247, 248, 251, 0.92)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.04), transparent 46%);
      box-shadow: var(--shadow);
    }

    .process-media-card img,
    .process-media-card video {
      display: block;
      width: 100%;
      height: 100%;
      background: #edf1f6;
      object-fit: cover;
    }

    .process-media-card > img,
    .process-media-card > video {
      aspect-ratio: 4 / 3;
    }

    .process-media-card--video > video {
      aspect-ratio: 16 / 10;
    }

    .process-media-card--lead {
      grid-column: span 2;
    }

    .process-media-card--lead > video {
      aspect-ratio: 16 / 9;
    }

    .process-media-card--wide-view {
      grid-column: 1 / -1;
    }

    .process-media-card--wide-view > img {
      aspect-ratio: 16 / 9;
      object-position: center 44%;
    }

    .process-media-card--quarry > img {
      object-position: center 42%;
    }

    .process-media-card figcaption {
      padding: 0.9rem 1rem 1rem;
      border-top: 1px solid rgba(29, 29, 31, 0.06);
      font-size: 0.92rem;
      line-height: 1.55;
      color: var(--ink-soft);
    }

    .process-media-card figcaption::before {
      content: "";
      display: block;
      width: 2.1rem;
      height: 1px;
      margin-bottom: 0.7rem;
      background: linear-gradient(90deg, rgba(0, 113, 227, 0.42), rgba(0, 113, 227, 0));
    }

    .reveal.is-visible .product-link {
      animation: chipEnter 620ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .reveal.is-visible .product-link:nth-child(2) {
      animation-delay: 0.08s;
    }

    .reveal.is-visible .product-link:nth-child(3) {
      animation-delay: 0.16s;
    }

    .reveal.is-visible .product-link:nth-child(4) {
      animation-delay: 0.24s;
    }

    .split-stage {
      display: grid;
      grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
      gap: 1.1rem;
    }

    .split-stage__panel {
      position: relative;
      padding: 1.6rem;
      border-radius: calc(var(--radius-lg) + 0.15rem);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.88), rgba(249, 249, 251, 0.8)),
        linear-gradient(140deg, rgba(0, 113, 227, 0.035), transparent 44%);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow);
      overflow: hidden;
    }

    .split-stage__panel::after {
      content: "";
      position: absolute;
      inset: auto -14% -30% auto;
      width: 15rem;
      height: 15rem;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(0, 113, 227, 0.06), transparent 68%);
      filter: blur(8px);
    }

    .split-stage__panel > * {
      position: relative;
      z-index: 1;
    }

    .split-stage__panel h2 {
      margin-top: 0;
      font-size: clamp(2rem, 4vw, 3.7rem);
      line-height: 1;
      letter-spacing: -0.05em;
    }

    .split-stage__panel p {
      margin: 1rem 0 0;
      color: var(--ink-soft);
      line-height: 1.72;
    }

    .split-stage__panel .industry-rail {
      margin-top: 1.45rem;
    }

    .split-stage__panel--process {
      display: grid;
      align-content: start;
    }

    .process-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 1rem;
      margin-top: 1.45rem;
    }

    .feature-stack,
    .portfolio-list {
      display: grid;
      gap: 1rem;
    }

    .feature-row,
    .portfolio-row {
      display: grid;
      grid-template-columns: minmax(0, 0.75fr) minmax(0, 1.25fr);
      gap: 1.2rem;
      align-items: start;
      padding: 1.4rem 1.5rem;
      border-radius: var(--radius-lg);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(250, 250, 252, 0.9)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.04), transparent 42%);
      transition: transform 180ms ease, box-shadow 180ms ease;
    }

    .feature-row p,
    .portfolio-row p {
      color: var(--ink-soft);
    }

    .about-frame {
      display: grid;
      grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr);
      gap: 2rem;
      align-items: start;
    }

    .principle-stack {
      display: grid;
      gap: 0;
      padding-top: 0.2rem;
    }

    .principle-line {
      padding: 1.2rem 0;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
    }

    .principle-line:first-child {
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .principle-line strong {
      display: block;
      margin: 0 0 0.45rem;
      font-size: 1.08rem;
      letter-spacing: -0.03em;
    }

    .principle-line p {
      margin: 0;
      line-height: 1.7;
      color: var(--ink-soft);
    }

    .industry-rail {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 1.1rem 2rem;
    }

    .industry-line {
      position: relative;
      padding: 0.1rem 0 1rem;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
      transition: transform 180ms ease;
    }

    .industry-line::after {
      content: "";
      position: absolute;
      left: 0;
      right: 22%;
      bottom: -1px;
      height: 1px;
      background: linear-gradient(90deg, rgba(0, 113, 227, 0.65), rgba(0, 113, 227, 0));
      background-size: 170% 100%;
      transform: scaleX(0.2);
      transform-origin: left center;
      transition: transform 820ms cubic-bezier(0.22, 1, 0.36, 1);
      animation: lineTravel 5.6s linear infinite;
      opacity: 0.4;
    }

    .reveal.is-visible.industry-line::after {
      transform: scaleX(1);
      opacity: 0.82;
    }

    .industry-line:hover {
      transform: translateX(0.15rem);
    }

    .industry-line__title {
      display: flex;
      align-items: center;
      gap: 0.58rem;
      margin: 0 0 0.45rem;
    }

    .industry-line__icon {
      width: 1.55rem;
      height: 1.55rem;
      border-radius: 0.48rem;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: rgba(0, 113, 227, 0.74);
      background: rgba(0, 113, 227, 0.08);
      border: 1px solid rgba(0, 113, 227, 0.18);
      flex: 0 0 auto;
    }

    .industry-line__icon svg {
      width: 0.95rem;
      height: 0.95rem;
      stroke: currentColor;
      fill: none;
      stroke-width: 1.7;
      stroke-linecap: round;
      stroke-linejoin: round;
    }

    .industry-line__icon svg rect,
    .industry-line__icon svg circle {
      fill: none;
    }

    .industry-line h3 {
      margin: 0;
      font-size: 1.2rem;
      line-height: 1.25;
      letter-spacing: -0.04em;
    }

    .industry-line p {
      margin: 0;
      line-height: 1.7;
      color: var(--ink-soft);
    }

    .process-shell {
      position: relative;
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 1rem;
      padding-top: 0.8rem;
    }

    .route-line--process {
      inset: 0 0 auto;
      height: 2rem;
    }

    .route-line--process::after {
      animation-duration: 7.8s;
    }

    .process-step {
      padding-top: 3rem;
    }

    .process-grid .process-step {
      min-height: 11.5rem;
      padding-top: 1.35rem;
    }

    .process-step span {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 2.4rem;
      height: 2.4rem;
      border-radius: 50%;
      background: var(--ink);
      color: white;
      font-weight: 800;
      font-size: 0.88rem;
      margin-bottom: 1rem;
    }

    .contact-shell {
      display: grid;
      grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
      gap: 1.4rem;
      padding: 1.5rem;
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(250, 250, 252, 0.9)),
        linear-gradient(110deg, rgba(0, 113, 227, 0.04), transparent 48%);
    }

    .contact-details {
      display: grid;
      gap: 0.55rem;
      margin-top: 1.2rem;
      color: var(--ink-soft);
    }

    .contact-details a {
      font-weight: 700;
      color: var(--ink);
    }

    .inquiry-form {
      padding: 1.4rem;
      border-radius: var(--radius-lg);
      background: rgba(255, 255, 255, 0.98);
      color: var(--ink);
      position: relative;
      overflow: hidden;
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow);
    }

    .inquiry-form::before {
      content: "";
      position: absolute;
      inset: auto -10% -22% auto;
      width: 14rem;
      height: 14rem;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(0, 113, 227, 0.1), transparent 68%);
    }

    .form-grid {
      position: relative;
      z-index: 1;
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 1rem;
    }

    .form-grid label {
      display: grid;
      gap: 0.55rem;
    }

    .form-grid label span {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      font-weight: 800;
      color: rgba(29, 29, 31, 0.46);
    }

    .form-grid input,
    .form-grid select,
    .form-grid textarea {
      width: 100%;
      border-radius: 1rem;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background: rgba(245, 245, 247, 0.92);
      padding: 0.95rem 1rem;
      color: var(--ink);
      outline: none;
      transition: border-color 180ms ease, background-color 180ms ease;
    }

    .form-grid input[readonly] {
      color: rgba(29, 29, 31, 0.72);
    }

    .form-grid textarea {
      resize: vertical;
      min-height: 7rem;
    }

    .form-grid input:focus,
    .form-grid select:focus,
    .form-grid textarea:focus {
      border-color: rgba(0, 113, 227, 0.34);
      background: white;
    }

    .form-grid__wide {
      grid-column: 1 / -1;
    }

    .form-actions {
      position: relative;
      z-index: 1;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 0.8rem;
      margin-top: 1.3rem;
    }

    .form-note {
      color: rgba(29, 29, 31, 0.5);
      font-size: 0.9rem;
      margin: 0;
      max-width: 20rem;
    }

    .bullet-list {
      margin: 1.1rem 0 0;
      padding: 0;
      list-style: none;
      display: grid;
      gap: 0.85rem;
    }

    .bullet-list li {
      position: relative;
      padding-left: 1.4rem;
      line-height: 1.7;
      color: var(--ink-soft);
    }

    .bullet-list li::before {
      content: "";
      position: absolute;
      left: 0;
      top: 0.72rem;
      width: 0.45rem;
      height: 0.45rem;
      border-radius: 50%;
      background: linear-gradient(180deg, var(--jade), var(--ore));
    }

    .product-hero {
      gap: 3rem;
      align-items: center;
    }

    .hero-copy--product {
      max-width: 34rem;
    }

    .product-poster {
      position: relative;
      display: grid;
      align-self: stretch;
      min-width: 0;
      animation: surfaceFloat 8.5s ease-in-out infinite;
    }

    .product-poster__surface {
      position: relative;
      min-height: 33rem;
      padding: 1.5rem;
      border-radius: calc(var(--radius-xl) + 0.2rem);
      background:
        radial-gradient(circle at 18% 12%, rgba(255, 255, 255, 0.98), transparent 24%),
        linear-gradient(180deg, rgba(247, 247, 249, 0.96), rgba(241, 243, 247, 0.92));
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow-lg);
      overflow: hidden;
    }

    .product-poster__surface::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(120deg, transparent 24%, rgba(255, 255, 255, 0.48) 50%, transparent 72%);
      transform: translateX(-120%);
      animation: specimenSweep 7.6s cubic-bezier(0.22, 1, 0.36, 1) infinite;
      pointer-events: none;
    }

    .product-poster__eyebrow,
    .product-poster__metrics,
    .product-poster__caption,
    .product-poster__title,
    .product-poster__copy {
      position: relative;
      z-index: 2;
    }

    .product-poster__eyebrow {
      margin: 0;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .product-poster__title {
      display: block;
      margin-top: 0.7rem;
      max-width: 10ch;
      font-size: clamp(2.8rem, 5.6vw, 5rem);
      line-height: 0.9;
      letter-spacing: -0.08em;
      color: var(--ink);
    }

    .product-poster__copy {
      margin: 1rem 0 0;
      max-width: 28rem;
      color: var(--ink-soft);
      line-height: 1.72;
    }

    .product-poster__metrics {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 0.85rem;
      margin-top: 1.25rem;
    }

    .product-poster__metric {
      padding: 0.92rem 1rem;
      border-radius: 1.25rem;
      background: rgba(255, 255, 255, 0.88);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: 0 8px 20px rgba(29, 29, 31, 0.04);
      animation: cardBreathe 6.4s ease-in-out infinite;
      min-width: 0;
    }

    .product-poster__metric:nth-child(2) {
      animation-delay: 0.6s;
    }

    .product-poster__metric:nth-child(3) {
      animation-delay: 1.2s;
    }

    .product-poster__metric:nth-child(4) {
      animation-delay: 1.8s;
    }

    .product-poster__metric span {
      display: block;
      margin-bottom: 0.35rem;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .product-poster__metric strong {
      display: block;
      line-height: 1.45;
      font-size: 0.98rem;
      letter-spacing: -0.03em;
    }

    .product-poster__caption {
      position: relative;
      left: auto;
      right: auto;
      bottom: auto;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-top: 1rem;
      padding: 0.95rem 1rem;
      border-radius: 1.2rem;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: 0 10px 24px rgba(29, 29, 31, 0.06);
    }

    .product-poster__caption p {
      margin: 0;
      line-height: 1.55;
      font-size: 0.93rem;
      color: rgba(29, 29, 31, 0.62);
    }

    body.is-ready .product-poster__eyebrow {
      animation: softLiftIn 820ms cubic-bezier(0.22, 1, 0.36, 1) 0.18s both;
    }

    body.is-ready .product-poster__title {
      animation: softLiftIn 860ms cubic-bezier(0.22, 1, 0.36, 1) 0.26s both;
    }

    body.is-ready .product-poster__copy {
      animation: softLiftIn 900ms cubic-bezier(0.22, 1, 0.36, 1) 0.34s both;
    }

    body.is-ready .product-poster__metrics {
      animation: softLiftIn 940ms cubic-bezier(0.22, 1, 0.36, 1) 0.42s both;
    }

    body.is-ready .product-poster__caption {
      animation: softLiftIn 980ms cubic-bezier(0.22, 1, 0.36, 1) 0.5s both;
    }

    .product-poster .route-line--snapshot {
      display: none;
    }

    .product-ledger {
      display: grid;
      grid-template-columns: minmax(0, 1.08fr) minmax(320px, 0.92fr);
      gap: 1.4rem;
      align-items: start;
    }

    .product-sheet {
      position: relative;
      overflow: hidden;
      padding: 1.75rem;
      border-radius: calc(var(--radius-lg) + 0.15rem);
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.92), rgba(249, 249, 251, 0.88)),
        linear-gradient(140deg, rgba(0, 113, 227, 0.03), transparent 46%);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: var(--shadow);
    }

    .product-sheet--full {
      grid-column: 1 / -1;
    }

    .product-sheet::after {
      content: "";
      position: absolute;
      inset: auto -18% -34% auto;
      width: 12rem;
      height: 12rem;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(0, 113, 227, 0.08), transparent 68%);
      filter: blur(8px);
      pointer-events: none;
    }

    .product-sheet > * {
      position: relative;
      z-index: 1;
    }

    .reveal.is-visible.product-sheet .product-line,
    .reveal.is-visible.product-sheet .product-info-row,
    .reveal.is-visible.product-sheet .product-note,
    .reveal.is-visible.product-sheet .form-pill,
    .reveal.is-visible.product-sheet .product-tag-cloud span {
      animation: softLiftIn 700ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .reveal.is-visible.product-sheet .product-line:nth-child(2),
    .reveal.is-visible.product-sheet .product-info-row:nth-child(2),
    .reveal.is-visible.product-sheet .product-note:nth-child(2),
    .reveal.is-visible.product-sheet .form-pill:nth-child(2),
    .reveal.is-visible.product-sheet .product-tag-cloud span:nth-child(2) {
      animation-delay: 0.08s;
    }

    .reveal.is-visible.product-sheet .product-line:nth-child(3),
    .reveal.is-visible.product-sheet .product-info-row:nth-child(3),
    .reveal.is-visible.product-sheet .product-note:nth-child(3),
    .reveal.is-visible.product-sheet .form-pill:nth-child(3),
    .reveal.is-visible.product-sheet .product-tag-cloud span:nth-child(3) {
      animation-delay: 0.16s;
    }

    .reveal.is-visible.product-sheet .product-line:nth-child(4),
    .reveal.is-visible.product-sheet .product-info-row:nth-child(4),
    .reveal.is-visible.product-sheet .product-note:nth-child(4),
    .reveal.is-visible.product-sheet .form-pill:nth-child(4),
    .reveal.is-visible.product-sheet .product-tag-cloud span:nth-child(4) {
      animation-delay: 0.24s;
    }

    .product-sheet h2 {
      margin: 0;
      max-width: 14ch;
      font-size: clamp(1.95rem, 3vw, 3rem);
      line-height: 0.98;
      letter-spacing: -0.06em;
      color: var(--ink);
    }

    .product-sheet__intro,
    .product-sheet__body {
      margin-top: 0.95rem;
      max-width: 34rem;
      color: var(--ink-soft);
      line-height: 1.75;
    }

    .product-line-list,
    .product-info-list {
      display: grid;
      gap: 0;
      margin-top: 1.35rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .product-line {
      display: grid;
      grid-template-columns: 2.25rem minmax(0, 1fr);
      gap: 1rem;
      align-items: start;
      padding: 1rem 0;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
    }

    .product-line span {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 2.25rem;
      height: 2.25rem;
      border-radius: 999px;
      background: rgba(0, 113, 227, 0.08);
      color: var(--ore);
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.08em;
    }

    .product-line strong {
      display: block;
      padding-top: 0.14rem;
      line-height: 1.45;
      font-size: 1.04rem;
      letter-spacing: -0.03em;
    }

    .product-info-row {
      display: grid;
      grid-template-columns: minmax(0, 0.42fr) minmax(0, 0.58fr);
      gap: 1rem;
      align-items: start;
      padding: 1rem 0;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
    }

    .product-info-row span {
      color: rgba(29, 29, 31, 0.46);
      font-size: 0.84rem;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }

    .product-info-row strong {
      display: block;
      line-height: 1.6;
      font-size: 0.98rem;
      letter-spacing: -0.02em;
    }

    .product-form-cloud {
      margin-top: 1.25rem;
    }

    .product-tag-cloud {
      display: flex;
      flex-wrap: wrap;
      gap: 0.7rem;
      margin-top: 1.2rem;
    }

    .product-tag-cloud span {
      display: inline-flex;
      align-items: center;
      min-height: 2.65rem;
      padding: 0.68rem 0.92rem;
      border-radius: 999px;
      background: rgba(0, 113, 227, 0.08);
      border: 1px solid rgba(0, 113, 227, 0.12);
      color: var(--ore);
      font-size: 0.86rem;
      font-weight: 700;
    }

    .product-note-list {
      display: grid;
      gap: 0.9rem;
      margin-top: 1.35rem;
    }

    .product-note {
      display: grid;
      grid-template-columns: 0.72rem minmax(0, 1fr);
      gap: 0.85rem;
      align-items: start;
    }

    .product-note span {
      width: 0.72rem;
      height: 0.72rem;
      margin-top: 0.5rem;
      border-radius: 50%;
      background: linear-gradient(180deg, #53a3ff, #0071e3);
      box-shadow: 0 0 0 0 rgba(0, 113, 227, 0.12);
      animation: beaconPulse 3.4s ease-in-out infinite;
    }

    .product-note p {
      margin: 0;
      line-height: 1.72;
      color: var(--ink-soft);
    }

    .product-stage,
    .product-commercial {
      display: grid;
      gap: 1rem;
    }

    .product-stage {
      grid-template-columns: minmax(0, 1.08fr) minmax(320px, 0.92fr);
      align-items: start;
    }

    .product-commercial {
      grid-template-columns: minmax(0, 1.08fr) minmax(320px, 0.92fr);
      align-items: start;
    }

    .product-commercial__main {
      display: grid;
      gap: 1rem;
    }

    .product-panel {
      position: relative;
      overflow: hidden;
    }

    .product-panel::after {
      content: "";
      position: absolute;
      inset: auto -18% -34% auto;
      width: 12rem;
      height: 12rem;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(0, 113, 227, 0.08), transparent 68%);
      filter: blur(8px);
      pointer-events: none;
    }

    .product-panel > * {
      position: relative;
      z-index: 1;
    }

    .product-panel h2 {
      max-width: 14ch;
      font-size: clamp(1.7rem, 2.8vw, 2.7rem);
      line-height: 1.02;
      letter-spacing: -0.05em;
      color: var(--ink);
    }

    .product-panel__intro,
    .product-panel__meta {
      margin-top: 0.95rem;
      color: var(--ink-soft);
      line-height: 1.72;
      max-width: 34rem;
    }

    .application-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 0.9rem;
      margin-top: 1.35rem;
    }

    .application-card {
      min-height: 8.25rem;
      padding: 1rem 1.05rem;
      border-radius: 1.3rem;
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(249, 249, 251, 0.9)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.04), transparent 44%);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: 0 14px 34px rgba(29, 29, 31, 0.06);
    }

    .application-card span {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 2rem;
      height: 2rem;
      border-radius: 999px;
      background: rgba(0, 113, 227, 0.08);
      color: var(--ore);
      font-size: 0.76rem;
      font-weight: 800;
      letter-spacing: 0.08em;
    }

    .application-card strong {
      display: block;
      margin-top: 1rem;
      line-height: 1.35;
      font-size: 1rem;
      letter-spacing: -0.03em;
    }

    .benefit-stack,
    .booking-list {
      display: grid;
      gap: 0.85rem;
      margin-top: 1.3rem;
    }

    .benefit-item {
      display: grid;
      grid-template-columns: 0.72rem minmax(0, 1fr);
      gap: 0.8rem;
      align-items: start;
      padding: 0.95rem 0;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
    }

    .benefit-item:last-child {
      border-bottom: 0;
      padding-bottom: 0;
    }

    .benefit-item span {
      width: 0.72rem;
      height: 0.72rem;
      margin-top: 0.48rem;
      border-radius: 50%;
      background: linear-gradient(180deg, #53a3ff, #0071e3);
      box-shadow: 0 0 0 0 rgba(0, 113, 227, 0.12);
      animation: beaconPulse 3.4s ease-in-out infinite;
    }

    .benefit-item p {
      margin: 0;
      line-height: 1.72;
      color: var(--ink-soft);
    }

    .booking-item {
      display: grid;
      grid-template-columns: 2.2rem minmax(0, 1fr);
      gap: 0.9rem;
      align-items: start;
      padding: 0.95rem 1rem;
      border-radius: 1.25rem;
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(249, 249, 251, 0.9)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.035), transparent 44%);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: 0 12px 30px rgba(29, 29, 31, 0.05);
    }

    .booking-item span {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 2.2rem;
      height: 2.2rem;
      border-radius: 999px;
      background: var(--ink);
      color: white;
      font-size: 0.76rem;
      font-weight: 800;
      letter-spacing: 0.08em;
    }

    .booking-item strong {
      display: block;
      padding-top: 0.1rem;
      line-height: 1.45;
      font-size: 1rem;
      letter-spacing: -0.03em;
    }

    .form-cloud,
    .commercial-fit__tags,
    .snapshot-stage__tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.7rem;
    }

    .form-cloud {
      margin-top: 1.3rem;
    }

    .size-cloud {
      display: flex;
      flex-wrap: wrap;
      gap: 0.8rem;
      margin-top: 1.35rem;
    }

    .form-pill,
    .size-pill,
    .commercial-fit__tags span,
    .snapshot-stage__tags span {
      display: inline-flex;
      align-items: center;
      min-height: 2.8rem;
      padding: 0.72rem 0.95rem;
      border-radius: 999px;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background: rgba(255, 255, 255, 0.92);
      box-shadow: 0 12px 28px rgba(29, 29, 31, 0.05);
      font-size: 0.92rem;
      font-weight: 700;
      line-height: 1.3;
    }

    .size-pill {
      min-height: 3rem;
      padding-inline: 1rem;
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(248, 250, 253, 0.92)),
        linear-gradient(120deg, rgba(0, 113, 227, 0.05), transparent 46%);
      border-color: rgba(0, 113, 227, 0.12);
      color: rgba(29, 29, 31, 0.86);
      box-shadow: 0 14px 30px rgba(29, 29, 31, 0.06);
      letter-spacing: -0.01em;
    }

    .commercial-fit__tags {
      margin-top: 1.1rem;
    }

    .commercial-fit__tags span,
    .snapshot-stage__tags span {
      background: rgba(0, 113, 227, 0.08);
      border-color: rgba(0, 113, 227, 0.12);
      color: var(--ore);
      box-shadow: none;
      font-size: 0.86rem;
    }

    .panel-copy--comfortable {
      margin-top: 1.1rem;
      max-width: 28rem;
      color: var(--ink-soft);
      line-height: 1.8;
    }

    .product-panel--commercial {
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(248, 248, 250, 0.92)),
        linear-gradient(145deg, rgba(0, 113, 227, 0.08), rgba(255, 255, 255, 0.42) 42%);
    }

    .product-panel--commercial h2 {
      max-width: 8ch;
      font-size: clamp(1.45rem, 2.4vw, 2.1rem);
    }

    .commercial-fit__note {
      display: grid;
      gap: 0.42rem;
      margin-top: 1rem;
      padding-top: 1rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .commercial-fit__note span {
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      font-weight: 800;
      color: rgba(29, 29, 31, 0.42);
    }

    .commercial-fit__note strong {
      line-height: 1.6;
      font-size: 0.98rem;
      letter-spacing: -0.02em;
    }

    .product-snapshot__visual {
      position: relative;
      display: grid;
      align-content: start;
      gap: 0.9rem;
      min-height: 0;
      margin-bottom: 1.2rem;
      border-radius: 1.7rem;
      overflow: hidden;
      background:
        radial-gradient(circle at 18% 16%, rgba(255, 255, 255, 0.98), transparent 28%),
        linear-gradient(180deg, rgba(245, 245, 247, 0.96), rgba(239, 241, 246, 0.92));
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: 0 18px 48px rgba(29, 29, 31, 0.08);
      padding: 1.15rem;
    }

    .snapshot-stage {
      position: relative;
      z-index: 2;
      padding: 1.15rem 1.2rem 1.2rem;
      border-radius: 1.35rem;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: 0 14px 36px rgba(29, 29, 31, 0.06);
    }

    .snapshot-stage__eyebrow {
      margin: 0;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .snapshot-stage__title {
      display: block;
      margin-top: 0.65rem;
      font-size: clamp(1.9rem, 3vw, 2.8rem);
      line-height: 0.98;
      letter-spacing: -0.06em;
    }

    .snapshot-stage__copy {
      margin: 0.8rem 0 0;
      max-width: 22rem;
      line-height: 1.62;
      color: var(--ink-soft);
    }

    .snapshot-stage__tags {
      margin-top: 1rem;
    }

    .product-snapshot .snapshot-visual-grid {
      position: relative;
      z-index: 2;
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 0.8rem;
      padding: 0;
    }

    .product-snapshot .snapshot-visual-card {
      min-height: 6rem;
      padding: 0.95rem 1rem;
      animation-duration: 10s;
    }

    .product-snapshot .snapshot-visual-card strong {
      font-size: 0.98rem;
      line-height: 1.35;
    }

    .product-snapshot .snapshot-visual-caption {
      position: relative;
      left: auto;
      right: auto;
      bottom: auto;
      margin-top: 0.1rem;
    }

    .product-snapshot .route-line--snapshot {
      display: none;
    }

    .ore-pillar--a {
      left: 9%;
      top: 14%;
      width: 24%;
      height: 62%;
    }

    .ore-pillar--b {
      left: 39%;
      top: 6%;
      width: 22%;
      height: 72%;
      animation-duration: 18s;
    }

    .ore-pillar--c {
      right: 10%;
      top: 20%;
      width: 27%;
      height: 56%;
      animation-duration: 16s;
    }

    .breadcrumb {
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem;
      align-items: center;
      margin-bottom: 1rem;
      font-size: 0.9rem;
      color: rgba(29, 29, 31, 0.46);
    }

    .breadcrumb strong {
      color: var(--ink);
    }

    .related-links a {
      transition: transform 180ms ease, box-shadow 180ms ease;
    }

    .related-links a:hover {
      transform: translateY(-1px);
      box-shadow: 0 12px 30px rgba(29, 29, 31, 0.08);
    }

    .faq-shell {
      display: grid;
      gap: 0.9rem;
    }

    .faq-item {
      padding: 0;
      overflow: hidden;
      border-radius: var(--radius-lg);
      background: rgba(255, 255, 255, 0.92);
    }

    .faq-item summary {
      list-style: none;
      cursor: pointer;
      padding: 1.25rem 1.3rem;
      font-weight: 700;
      position: relative;
      padding-right: 3.2rem;
    }

    .faq-item summary::-webkit-details-marker {
      display: none;
    }

    .faq-item summary::after {
      content: "+";
      position: absolute;
      right: 1.3rem;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.2rem;
      color: rgba(29, 29, 31, 0.46);
    }

    .faq-item[open] summary::after {
      content: "−";
    }

    .faq-item p {
      padding: 0 1.3rem 1.25rem;
      color: var(--ink-soft);
    }

    .reveal.is-visible.faq-item {
      animation: softLiftIn 720ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .reveal.is-visible.faq-item:nth-child(2),
    .reveal.is-visible .related-links a:nth-child(2) {
      animation-delay: 0.08s;
    }

    .reveal.is-visible.faq-item:nth-child(3),
    .reveal.is-visible .related-links a:nth-child(3) {
      animation-delay: 0.16s;
    }

    .reveal.is-visible.faq-item:nth-child(4),
    .reveal.is-visible .related-links a:nth-child(4) {
      animation-delay: 0.24s;
    }

    .reveal.is-visible .related-links a {
      animation: softLiftIn 720ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .hero-copy--portfolio {
      max-width: 56rem;
      margin: 0 auto;
      text-align: center;
    }

    .hero-copy--portfolio h1,
    .hero-copy--portfolio .hero-text {
      margin-inline: auto;
    }

    .hero-copy--portfolio h1 {
      max-width: 10.5ch;
    }

    .hero-copy--portfolio .hero-text {
      max-width: 42rem;
    }

    .hero-copy--portfolio .hero-actions {
      justify-content: center;
    }

    .portfolio-hero-meta {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.7rem;
      margin-top: 1.8rem;
    }

    .portfolio-hero-meta span {
      display: inline-flex;
      align-items: center;
      min-height: 2.75rem;
      padding: 0.68rem 1rem;
      border-radius: 999px;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background: rgba(255, 255, 255, 0.84);
      color: rgba(29, 29, 31, 0.72);
      font-size: 0.92rem;
      font-weight: 700;
      box-shadow: 0 12px 24px rgba(29, 29, 31, 0.05);
      animation: floatLift 7s ease-in-out infinite;
    }

    .portfolio-hero-meta span:nth-child(2) {
      animation-delay: 0.4s;
    }

    .portfolio-hero-meta span:nth-child(3) {
      animation-delay: 0.8s;
    }

    .portfolio-shell {
      display: grid;
      gap: 4.5rem;
    }

    .portfolio-anchor-rail {
      position: sticky;
      top: 5.8rem;
      z-index: 8;
      display: flex;
      gap: 0.7rem;
      padding: 0.7rem;
      margin-bottom: 0.2rem;
      overflow-x: auto;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.82);
      border: 1px solid rgba(29, 29, 31, 0.06);
      box-shadow: 0 16px 40px rgba(29, 29, 31, 0.06);
      backdrop-filter: blur(14px);
      scrollbar-width: none;
      animation: surfaceFloat 10s ease-in-out infinite;
    }

    .portfolio-anchor-rail::-webkit-scrollbar {
      display: none;
    }

    .portfolio-anchor {
      display: inline-flex;
      flex: 0 0 auto;
      align-items: center;
      min-height: 2.9rem;
      padding: 0.72rem 1rem;
      white-space: nowrap;
      border-radius: 999px;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background: rgba(255, 255, 255, 0.9);
      color: rgba(29, 29, 31, 0.72);
      font-size: 0.92rem;
      font-weight: 700;
      transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease, background-color 180ms ease, color 180ms ease;
    }

    .reveal.is-visible.portfolio-anchor-rail .portfolio-anchor {
      animation: softLiftIn 680ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .reveal.is-visible.portfolio-anchor-rail .portfolio-anchor:nth-child(2) {
      animation-delay: 0.06s;
    }

    .reveal.is-visible.portfolio-anchor-rail .portfolio-anchor:nth-child(3) {
      animation-delay: 0.12s;
    }

    .reveal.is-visible.portfolio-anchor-rail .portfolio-anchor:nth-child(4) {
      animation-delay: 0.18s;
    }

    .portfolio-anchor:hover,
    .portfolio-anchor:focus-visible {
      transform: translateY(-1px);
      border-color: rgba(0, 113, 227, 0.18);
      box-shadow: 0 12px 28px rgba(29, 29, 31, 0.06);
    }

    .portfolio-anchor.is-active {
      background: var(--ore);
      border-color: transparent;
      color: white;
      box-shadow: 0 18px 38px rgba(0, 113, 227, 0.2);
    }

    .portfolio-stage {
      position: relative;
      display: grid;
      grid-template-columns: minmax(0, 0.82fr) minmax(0, 1.18fr);
      gap: 3rem;
      align-items: start;
      padding-top: 2.2rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
      overflow: hidden;
    }

    .portfolio-stage::after {
      content: "";
      position: absolute;
      top: 0;
      left: -14rem;
      width: 16rem;
      height: 2px;
      background: linear-gradient(90deg, transparent, rgba(0, 113, 227, 0.36), transparent);
      animation: proofSweep 7.8s linear infinite;
    }

    .portfolio-stage__intro {
      position: sticky;
      top: 7.8rem;
      align-self: start;
      max-width: 30rem;
      padding-right: 1rem;
    }

    .portfolio-stage__index {
      margin: 0;
      font-size: clamp(4.2rem, 9vw, 7.5rem);
      line-height: 0.82;
      letter-spacing: -0.09em;
      font-weight: 800;
      color: rgba(29, 29, 31, 0.12);
    }

    .portfolio-stage__count {
      margin: 0.65rem 0 1rem;
      font-size: 0.74rem;
      font-weight: 800;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .portfolio-stage__intro h2 {
      margin: 0;
      font-size: clamp(3rem, 5.5vw, 6rem);
      line-height: 0.9;
      letter-spacing: -0.08em;
      color: var(--ink);
    }

    .portfolio-stage__intro p {
      margin: 1rem 0 0;
      color: var(--ink-soft);
      line-height: 1.76;
      max-width: 28rem;
    }

    .portfolio-stage__summary {
      color: rgba(29, 29, 31, 0.58);
      font-size: 0.98rem;
    }

    .portfolio-stage__focus {
      display: flex;
      flex-wrap: wrap;
      gap: 0.7rem;
      align-items: center;
      margin-top: 1.15rem;
    }

    .portfolio-stage__focus-label {
      color: rgba(29, 29, 31, 0.42);
      font-size: 0.74rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
    }

    .portfolio-stage__pill {
      display: inline-flex;
      align-items: center;
      min-height: 2.35rem;
      padding: 0.6rem 0.9rem;
      border-radius: 999px;
      background: rgba(0, 113, 227, 0.08);
      border: 1px solid rgba(0, 113, 227, 0.12);
      color: var(--ore);
      font-size: 0.86rem;
      font-weight: 700;
      letter-spacing: -0.02em;
    }

    .portfolio-stage__track {
      display: grid;
      gap: 0;
      min-width: 0;
      padding-top: 0.85rem;
    }

    .portfolio-product {
      position: relative;
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 1.35rem;
      align-items: center;
      padding: 1.7rem 0;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
      transition: transform 220ms ease, border-color 220ms ease;
    }

    .portfolio-product::before {
      content: "";
      position: absolute;
      inset: 0 auto 0 0;
      width: 0;
      background: linear-gradient(90deg, rgba(0, 113, 227, 0.06), transparent 72%);
      opacity: 0;
      transition: width 220ms ease, opacity 220ms ease;
      pointer-events: none;
    }

    .portfolio-product:first-child {
      padding-top: 0;
    }

    .portfolio-product:last-child {
      border-bottom: 0;
      padding-bottom: 0;
    }

    .portfolio-product:hover,
    .portfolio-product:focus-visible {
      transform: translateX(0.26rem);
      border-color: rgba(0, 113, 227, 0.18);
    }

    .portfolio-product:hover::before,
    .portfolio-product:focus-visible::before {
      width: 100%;
      opacity: 1;
    }

    .portfolio-product__main {
      display: grid;
      gap: 0.6rem;
      min-width: 0;
    }

    .portfolio-product__eyebrow {
      margin: 0;
      font-size: 0.74rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(29, 29, 31, 0.42);
    }

    .portfolio-product h3 {
      margin: 0;
      font-size: clamp(2rem, 3.4vw, 3.35rem);
      line-height: 0.95;
      letter-spacing: -0.07em;
      color: var(--ink);
    }

    .portfolio-product__copy {
      margin: 0;
      max-width: 35rem;
      color: var(--ink-soft);
      line-height: 1.74;
      font-size: 1.02rem;
    }

    .portfolio-product__fit {
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem;
      align-items: center;
      margin: 0;
      color: rgba(29, 29, 31, 0.68);
      line-height: 1.55;
      font-size: 0.96rem;
      letter-spacing: -0.02em;
    }

    .portfolio-product__fit span {
      color: rgba(29, 29, 31, 0.46);
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
    }

    .portfolio-product__arrow {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 8.6rem;
      min-height: 3rem;
      padding: 0.75rem 1.1rem;
      border-radius: 999px;
      border: 1px solid rgba(29, 29, 31, 0.08);
      background: rgba(255, 255, 255, 0.9);
      color: var(--ore);
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      transition: transform 180ms ease, background-color 180ms ease, color 180ms ease, border-color 180ms ease;
    }

    .portfolio-product:hover .portfolio-product__arrow,
    .portfolio-product:focus-visible .portfolio-product__arrow {
      transform: translateX(0.18rem);
      background: var(--ore);
      border-color: transparent;
      color: white;
    }

    .reveal.is-visible.portfolio-stage__track .portfolio-product {
      animation: softLiftIn 780ms cubic-bezier(0.22, 1, 0.36, 1) both;
    }

    .reveal.is-visible.portfolio-stage__track .portfolio-product:nth-child(2) {
      animation-delay: 0.08s;
    }

    .reveal.is-visible.portfolio-stage__track .portfolio-product:nth-child(3) {
      animation-delay: 0.16s;
    }

    .reveal.is-visible.portfolio-stage__track .portfolio-product:nth-child(4) {
      animation-delay: 0.24s;
    }

    .site-footer {
      padding: 3rem 0 2rem;
      background: #f5f5f7;
      color: rgba(29, 29, 31, 0.72);
      margin-top: 3.5rem;
      border-top: 1px solid rgba(29, 29, 31, 0.08);
    }

    .site-footer__inner {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.6rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid rgba(29, 29, 31, 0.08);
    }

    .site-footer__inner > * {
      min-width: 0;
    }

    .footer-copy {
      color: rgba(29, 29, 31, 0.56);
      max-width: 34rem;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 1.2rem;
    }

    .footer-grid > div {
      min-width: 0;
    }

    .footer-heading {
      margin: 0 0 0.75rem;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      font-weight: 800;
      color: rgba(29, 29, 31, 0.42);
    }

    .footer-grid a,
    .footer-grid p {
      display: block;
      margin: 0.3rem 0;
      color: rgba(29, 29, 31, 0.72);
      line-height: 1.6;
      overflow-wrap: anywhere;
    }

    .site-footer__meta {
      padding-top: 1rem;
      color: rgba(29, 29, 31, 0.48);
      font-size: 0.92rem;
    }

    .theme-silica .strata--a,
    .theme-quartz .strata--a {
      background: linear-gradient(90deg, rgba(255, 255, 255, 0.92), rgba(214, 229, 255, 0.72), rgba(255, 255, 255, 0.16));
    }

    .theme-clay .strata--a,
    .theme-kaolin .strata--a,
    .theme-talc .strata--a {
      background: linear-gradient(90deg, rgba(235, 237, 241, 0.92), rgba(255, 255, 255, 0.72), rgba(214, 229, 255, 0.18));
    }

    .theme-feldspar .strata--a,
    .theme-salt .strata--a {
      background: linear-gradient(90deg, rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.54), rgba(0, 113, 227, 0.14));
    }

    .theme-copper .strata--a,
    .theme-ash .strata--a {
      background: linear-gradient(90deg, rgba(228, 232, 238, 0.92), rgba(255, 255, 255, 0.5), rgba(214, 229, 255, 0.2));
    }

    .reveal {
      opacity: 0;
      transform: translateY(34px) scale(0.988);
      filter: blur(10px);
      transition:
        opacity 760ms cubic-bezier(0.22, 1, 0.36, 1),
        transform 760ms cubic-bezier(0.22, 1, 0.36, 1),
        filter 760ms cubic-bezier(0.22, 1, 0.36, 1);
    }

    .reveal.is-visible {
      opacity: 1;
      transform: translateY(0) scale(1);
      filter: blur(0);
    }

    @keyframes atmosphereDrift {
      from {
        transform: translate3d(0, 0, 0);
      }
      to {
        transform: translate3d(1.2%, -1%, 0);
      }
    }

    @keyframes ambientDrift {
      from {
        transform: translate3d(0, 0, 0) scale(1);
      }
      to {
        transform: translate3d(8%, -6%, 0) scale(1.08);
      }
    }

    @keyframes ambientSweep {
      from {
        transform: translate3d(-5%, 0, 0) scale(1);
      }
      to {
        transform: translate3d(6%, -4%, 0) scale(1.06);
      }
    }

    @keyframes softLiftIn {
      from {
        opacity: 0;
        transform: translate3d(0, 1rem, 0) scale(0.985);
      }
      to {
        opacity: 1;
        transform: translate3d(0, 0, 0) scale(1);
      }
    }

    @keyframes strataShift {
      from {
        transform: translate3d(-1%, 0, 0) scaleX(1.02);
      }
      to {
        transform: translate3d(2%, -1.5%, 0) scaleX(0.98);
      }
    }

    @keyframes oreDrift {
      from {
        transform: translate3d(-0.35rem, 0.3rem, 0) rotate(-2.2deg) scale(1);
      }
      to {
        transform: translate3d(0.65rem, -1.2rem, 0) rotate(2.2deg) scale(1.04);
      }
    }

    @keyframes surfaceFloat {
      0%, 100% {
        transform: translate3d(0, 0, 0);
      }
      50% {
        transform: translate3d(0, -0.55rem, 0);
      }
    }

    @keyframes floatLift {
      0%, 100% {
        transform: translateY(0);
      }
      50% {
        transform: translateY(-0.24rem);
      }
    }

    @keyframes specimenSweep {
      0%,
      64% {
        transform: translateX(-120%);
      }
      100% {
        transform: translateX(120%);
      }
    }

    @keyframes routePulse {
      from {
        transform: translateX(0);
        box-shadow: 0 0 0 0 rgba(0, 113, 227, 0.24);
      }
      30% {
        box-shadow: 0 0 0 0.55rem rgba(0, 113, 227, 0.08);
      }
      to {
        transform: translateX(calc(100% - 0.8rem));
        box-shadow: 0 0 0 0 rgba(0, 113, 227, 0);
      }
    }

    @keyframes cardBreathe {
      0%, 100% {
        transform: translateY(0);
      }
      50% {
        transform: translateY(-0.42rem);
      }
    }

    @keyframes chipEnter {
      from {
        opacity: 0;
        transform: translateY(0.65rem) scale(0.98);
      }
      to {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }

    @keyframes arrowDrift {
      0%, 100% {
        transform: translateX(0);
      }
      50% {
        transform: translateX(0.12rem);
      }
    }

    @keyframes bandRoute {
      from {
        transform: translateX(0);
        box-shadow: 0 0 0 0 rgba(0, 113, 227, 0.22);
      }
      35% {
        box-shadow: 0 0 0 0.45rem rgba(0, 113, 227, 0.08);
      }
      to {
        transform: translateX(calc(100% - 0.72rem));
        box-shadow: 0 0 0 0 rgba(0, 113, 227, 0);
      }
    }

    @keyframes beaconPulse {
      0%, 100% {
        box-shadow: 0 0 0 0 rgba(0, 113, 227, 0.14);
      }
      50% {
        box-shadow: 0 0 0 0.45rem rgba(0, 113, 227, 0.06);
      }
    }

    @keyframes proofSweep {
      from {
        transform: translateX(-120%);
      }
      to {
        transform: translateX(120%);
      }
    }

    @keyframes lineTravel {
      from {
        background-position: 0% 0;
      }
      to {
        background-position: 180% 0;
      }
    }

    @keyframes corridorHubOrbit {
      from {
        transform: rotate(0deg);
      }
      to {
        transform: rotate(360deg);
      }
    }

    @keyframes corridorHubPulse {
      0%,
      100% {
        transform: scale(0.94);
        opacity: 0.66;
      }
      50% {
        transform: scale(1.03);
        opacity: 1;
      }
    }

    @keyframes corridorShipTravel {
      0% {
        left: 0;
        transform: translate(-0.15rem, -50%) scale(0.94);
        opacity: 0;
      }
      12% {
        opacity: 1;
      }
      84% {
        opacity: 1;
      }
      100% {
        left: calc(100% - 2.05rem);
        transform: translate(0, -50%) scale(1);
        opacity: 0;
      }
    }

    @keyframes corridorTerminalPulse {
      0% {
        box-shadow: 0 0 0 0 rgba(191, 224, 255, 0.34);
      }
      100% {
        box-shadow: 0 0 0 0.8rem rgba(191, 224, 255, 0);
      }
    }

    @keyframes buyerGuidesScroll {
      from {
        transform: translateX(0);
      }
      to {
        transform: translateX(-50%);
      }
    }

    @media (max-width: 1100px) {
      .hero__inner,
      .home-ledger,
      .home-split,
      .about-frame,
      .operating-stage,
      .split-stage,
      .contact-shell,
      .site-footer__inner,
      .ceo-note,
      .product-ledger,
      .product-bridge-row {
        grid-template-columns: 1fr;
      }

      .process-shell {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }

      .route-line--process {
        display: none;
      }

      .hero-visual {
        min-height: 28rem;
      }

      .product-hero {
        gap: 2rem;
      }

      .product-bridge-row {
        margin-top: 0;
      }

      .home-poster {
        min-height: 28rem;
      }

      .blog-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }

      .blog-layout {
        grid-template-columns: 1fr;
      }

      .blog-sidecard {
        position: relative;
        top: auto;
      }

      .process-media-grid--operations {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }

      .portfolio-stage {
        grid-template-columns: 1fr;
        gap: 1.9rem;
      }

      .portfolio-stage__intro {
        position: static;
        max-width: none;
        padding-right: 0;
      }

      .portfolio-stage__track {
        padding-top: 0;
      }

      .corridor-stage__body {
        grid-template-columns: 1fr;
      }

      .corridor-stage__hub {
        max-width: 34rem;
      }
    }

    @media (max-width: 900px) {
      .desktop-nav,
      .header-actions .button--compact {
        display: none;
      }

      .header-actions {
        gap: 0.55rem;
      }

      .menu-toggle {
        display: inline-flex;
        align-items: center;
        justify-content: center;
      }

      .hero {
        padding-top: 7.5rem;
      }

      .proof-strip,
      .home-poster__metrics,
      .blog-grid,
      .industry-rail,
      .operating-stage__cards,
      .process-grid,
      .product-overview,
      .product-specs,
      .product-poster__metrics,
      .product-stage,
      .product-commercial,
      .product-commercial__main,
      .application-grid,
      .footer-grid,
      .ceo-spotlight__grid {
        grid-template-columns: 1fr;
      }

      .process-media-grid--dispatch {
        grid-template-columns: 1fr;
      }

      .process-media-card--lead,
      .process-media-card--wide-view {
        grid-column: auto;
      }

      .section-topline {
        flex-direction: column;
        align-items: flex-start;
      }

      .section-topline--stack {
        align-items: flex-start;
      }

      .buyer-guides-strip__head {
        flex-direction: column;
        align-items: flex-start;
      }

      .buyer-guides-holder {
        justify-content: flex-start;
        padding-right: 0;
      }

      .buyer-guides-strip {
        width: min(19rem, 100%);
        aspect-ratio: auto;
        min-height: 12rem;
      }

      .corridor-stage__top {
        align-items: flex-start;
      }

      .corridor-lane {
        grid-template-columns: minmax(0, 1fr);
        gap: 0.5rem;
      }

      .corridor-lane__rail {
        height: 2.7rem;
      }

      .family-band__meta {
        flex-direction: column;
        align-items: flex-start;
      }

      .proof-strip {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }

      .proof-strip__item:nth-child(2) {
        border-right: 0;
      }

      .proof-strip__item:nth-child(-n + 2) {
        border-bottom: 1px solid rgba(29, 29, 31, 0.08);
      }

      .family-band,
      .feature-row,
      .portfolio-row,
      .portfolio-product,
      .home-family-row {
        grid-template-columns: 1fr;
      }

      .hero-spec-grid {
        grid-template-columns: 1fr;
      }

      .home-family-row {
        gap: 1rem;
      }

      .home-family-row__cta {
        width: fit-content;
      }

      .product-info-row {
        grid-template-columns: 1fr;
        gap: 0.35rem;
      }

      .product-poster .route-line--snapshot {
        inset-inline: 12%;
      }

      .portfolio-anchor-rail {
        top: 4.9rem;
      }

      .portfolio-product {
        align-items: start;
      }

      .portfolio-product__arrow {
        width: fit-content;
      }
    }

    @media (max-width: 720px) {
      body {
        background:
          radial-gradient(circle at 22% 0%, rgba(0, 113, 227, 0.08), transparent 20%),
          linear-gradient(180deg, #fbfbfd 0, #f7f7fa 22rem, var(--bg) 22rem, var(--bg) 100%);
      }

      .shell {
        width: min(var(--max-width), calc(100vw - 1.25rem));
      }

      .site-header__inner {
        width: min(var(--max-width), calc(100vw - 1.25rem));
        padding-inline: 1rem;
      }

      .menu-toggle {
        min-height: 2.65rem;
        padding-inline: 0.88rem;
      }

      .section-shell {
        padding-inline: 0.95rem;
      }

      .brand-mark img {
        height: 2.5rem;
      }

      .hero__inner,
      .hero__inner--product,
      .hero__inner--single {
        min-height: auto;
        padding-bottom: 2.5rem;
        grid-template-columns: 1fr;
      }

      .home-hero {
        min-height: auto;
        padding-bottom: 2.5rem;
      }

      .hero h1 {
        max-width: 12ch;
        font-size: clamp(2.5rem, 12vw, 4.4rem);
      }

      .hero-track,
      .product-snapshot,
      .about-point,
      .industry-item,
      .product-panel,
      .process-step,
      .portfolio-group,
      .contact-shell {
        border-radius: 1.5rem;
      }

      .hero-copy--portfolio h1 {
        max-width: 11ch;
      }

      .hero-copy--home h1 {
        max-width: 11ch;
      }

      .portfolio-hero-meta {
        justify-content: flex-start;
      }

      .home-poster__metrics,
      .product-poster__metrics {
        grid-template-columns: 1fr;
      }

      .home-poster__surface {
        min-height: 25rem;
        padding: 1.25rem;
      }

      .product-poster__surface {
        min-height: 29rem;
        padding: 1.25rem;
      }

      .home-poster__metrics {
        margin-top: 2rem;
        padding-top: 1rem;
      }

      .home-metric {
        padding: 0.85rem 0 0;
      }

      .home-metric:not(:last-child) {
        border-right: 0;
        border-bottom: 1px solid rgba(29, 29, 31, 0.08);
        padding-bottom: 0.85rem;
      }

      .product-poster__caption {
        position: relative;
        left: auto;
        right: auto;
        bottom: auto;
        margin-top: 1rem;
      }

      .product-poster .route-line--snapshot {
        inset: auto 10% 8.2rem 10%;
      }

      .home-family-row__index {
        font-size: clamp(1.9rem, 12vw, 3rem);
      }

      .home-family-row__main h3 {
        font-size: clamp(2rem, 11vw, 3rem);
      }

      .home-split__panel h2 {
        font-size: clamp(2.1rem, 10vw, 3.4rem);
      }

      .ceo-spotlight__media {
        max-width: 26rem;
      }

      .portfolio-anchor-rail {
        padding: 0.45rem;
      }

      .portfolio-anchor {
        min-height: 2.65rem;
        padding: 0.64rem 0.88rem;
      }

      .portfolio-stage {
        gap: 1.4rem;
        padding-top: 1.6rem;
      }

      .portfolio-stage__index {
        font-size: clamp(3rem, 18vw, 5rem);
      }

      .portfolio-stage__intro h2 {
        font-size: clamp(2.4rem, 12vw, 4rem);
      }

      .portfolio-product {
        padding: 1.35rem 0;
      }

      .portfolio-product h3 {
        font-size: clamp(1.8rem, 8vw, 2.35rem);
      }

      .hero-visual {
        min-height: 24rem;
      }

      .hero-visual__specimen {
        min-height: 21rem;
      }

      .home-poster {
        min-height: 24rem;
      }

      .blog-card {
        padding: 1.1rem 1rem;
      }

      .process-media-grid--operations {
        grid-template-columns: 1fr;
      }

      .buyer-guides-strip {
        padding: 0.9rem 0.82rem;
        min-height: 11.4rem;
      }

      .buyer-guides-marquee::before,
      .buyer-guides-marquee::after {
        width: 2.5rem;
      }

      .product-snapshot__visual {
        min-height: 31rem;
      }

      .product-snapshot .snapshot-visual-grid {
        grid-template-columns: 1fr;
        bottom: 4.6rem;
      }

      .proof-strip {
        grid-template-columns: 1fr;
        margin-bottom: 2.4rem;
      }

      .proof-strip__item {
        border-right: 0 !important;
      }

      .proof-strip__item:not(:last-child) {
        border-bottom: 1px solid rgba(29, 29, 31, 0.08);
      }

      .form-grid {
        grid-template-columns: 1fr;
      }

      .site-footer {
        margin-top: 2.5rem;
      }
    }

    @media (prefers-reduced-motion: reduce) {
      html {
        scroll-behavior: auto;
      }

      *,
      *::before,
      *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
    """
).strip()


SCRIPT = dedent(
    f"""
    const header = document.querySelector("[data-header]");
    const reveals = document.querySelectorAll("[data-reveal]");
    const menuToggle = document.querySelector("[data-menu-toggle]");
    const mobileMenu = document.querySelector("[data-mobile-menu]");
    const requestLinks = document.querySelectorAll("[data-set-request]");
    const formTargets = document.querySelectorAll("[data-inquiry-form]");
    const yearTargets = document.querySelectorAll("[data-current-year]");
    const parallaxNodes = document.querySelectorAll("[data-parallax]");
    const routeNetworks = document.querySelectorAll("[data-route-network]");
    const portfolioAnchors = document.querySelectorAll(".portfolio-anchor");
    const portfolioStages = document.querySelectorAll(".portfolio-stage[id]");
    const corridorStages = document.querySelectorAll("[data-corridor-stage]");
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    requestAnimationFrame(() => {{
      document.body.classList.add("is-ready");
    }});

    const syncHeader = () => {{
      if (!header) return;
      header.classList.toggle("is-scrolled", window.scrollY > 24);
    }};

    const syncParallax = () => {{
      if (!parallaxNodes.length || prefersReducedMotion.matches) return;

      parallaxNodes.forEach((node) => {{
        const speed = Number(node.dataset.parallax || 0.14);
        const rect = node.getBoundingClientRect();
        const midpoint = rect.top + rect.height / 2;
        const viewportMid = window.innerHeight / 2;
        const offset = (midpoint - viewportMid) * speed * -0.12;
        node.style.transform = `translate3d(0, ${{offset.toFixed(2)}}px, 0)`;
      }});
    }};

    const initRouteNetwork = (canvas) => {{
      const ctx = canvas.getContext("2d");
      if (!ctx) return null;

      let width = 0;
      let height = 0;
      let dpr = Math.min(window.devicePixelRatio || 1, 2);
      let frameId = 0;
      let nodes = [];
      let lanes = [];
      let contours = [];

      const density = Number(canvas.dataset.networkDensity || 18);
      const theme = canvas.dataset.networkTheme || "home";
      const mode = canvas.dataset.motionMode || "harbor";
      const palettes = {{
        home: {{ line: "92, 121, 164", glow: "205, 223, 248", node: "255, 255, 255", contour: "110, 140, 184" }},
        portfolio: {{ line: "104, 126, 164", glow: "216, 229, 247", node: "255, 255, 255", contour: "118, 143, 181" }},
        silica: {{ line: "109, 139, 186", glow: "220, 233, 248", node: "255, 255, 255", contour: "115, 149, 198" }},
        quartz: {{ line: "118, 145, 190", glow: "224, 235, 249", node: "255, 255, 255", contour: "125, 154, 197" }},
        clay: {{ line: "124, 138, 168", glow: "225, 231, 239", node: "255, 255, 255", contour: "128, 142, 172" }},
        kaolin: {{ line: "132, 145, 176", glow: "228, 234, 243", node: "255, 255, 255", contour: "138, 151, 183" }},
        talc: {{ line: "128, 143, 179", glow: "226, 233, 243", node: "255, 255, 255", contour: "132, 148, 184" }},
        feldspar: {{ line: "120, 142, 180", glow: "223, 234, 247", node: "255, 255, 255", contour: "128, 150, 191" }},
        salt: {{ line: "132, 150, 184", glow: "231, 238, 247", node: "255, 255, 255", contour: "138, 159, 194" }},
        ash: {{ line: "126, 138, 164", glow: "226, 232, 238", node: "255, 255, 255", contour: "132, 143, 171" }},
        copper: {{ line: "116, 132, 165", glow: "220, 229, 239", node: "255, 255, 255", contour: "122, 138, 171" }},
      }};
      const palette = palettes[theme] || palettes.home;

      const roundRect = (x, y, w, h, r) => {{
        const radius = Math.min(r, w / 2, h / 2);
        ctx.beginPath();
        ctx.moveTo(x + radius, y);
        ctx.lineTo(x + w - radius, y);
        ctx.quadraticCurveTo(x + w, y, x + w, y + radius);
        ctx.lineTo(x + w, y + h - radius);
        ctx.quadraticCurveTo(x + w, y + h, x + w - radius, y + h);
        ctx.lineTo(x + radius, y + h);
        ctx.quadraticCurveTo(x, y + h, x, y + h - radius);
        ctx.lineTo(x, y + radius);
        ctx.quadraticCurveTo(x, y, x + radius, y);
        ctx.closePath();
      }};

      const buildHarbor = () => {{
        nodes = [];
        lanes = [];

        const columns = width > 920 ? [0.14, 0.36, 0.62, 0.84] : [0.18, 0.5, 0.82];
        const kinds = columns.length === 4
          ? ["packing", "spec", "port", "shipment"]
          : ["packing", "port", "shipment"];

        columns.forEach((ratio, columnIndex) => {{
          const count = Math.max(3, Math.min(6, Math.round(height / density) + (columnIndex % 2)));
          const spread = height / (count + 1);

          for (let row = 0; row < count; row += 1) {{
            nodes.push({{
              id: `${{columnIndex}}-${{row}}`,
              column: columnIndex,
              kind: kinds[columnIndex] || "shipment",
              x: width * ratio + (Math.random() - 0.5) * width * 0.03,
              y: spread * (row + 1) + (Math.random() - 0.5) * spread * 0.22,
              rangeX: 5 + Math.random() * 10,
              rangeY: 4 + Math.random() * 8,
              phase: Math.random() * Math.PI * 2,
              size: 2.4 + Math.random() * 1.6,
            }});
          }}
        }});

        const columnMap = Array.from({{ length: columns.length }}, () => []);
        nodes.forEach((node) => columnMap[node.column].push(node));
        columnMap.forEach((group) => group.sort((a, b) => a.y - b.y));

        columnMap.forEach((group) => {{
          for (let index = 0; index < group.length - 1; index += 1) {{
            lanes.push({{ a: group[index], b: group[index + 1], emphasis: 0.24 }});
          }}
        }});

        for (let columnIndex = 0; columnIndex < columnMap.length - 1; columnIndex += 1) {{
          columnMap[columnIndex].forEach((node, nodeIndex) => {{
            const targetGroup = columnMap[columnIndex + 1];
            const connections = [...targetGroup]
              .sort((a, b) => Math.abs(a.y - node.y) - Math.abs(b.y - node.y))
              .slice(0, columnIndex === columnMap.length - 2 ? 2 : 1 + (nodeIndex % 2));

            connections.forEach((target) => {{
              lanes.push({{
                a: node,
                b: target,
                emphasis: columnIndex === columnMap.length - 2 ? 0.4 : 0.3,
              }});
            }});
          }});
        }}

        const deduped = [];
        const seen = new Set();
        lanes.forEach((lane) => {{
          const key = [lane.a.id, lane.b.id].sort().join(":");
          if (seen.has(key)) return;
          seen.add(key);
          deduped.push({{
            ...lane,
            glowPhase: Math.random() * Math.PI * 2,
          }});
        }});
        lanes = deduped;
      }};

      const buildContour = () => {{
        contours = Array.from({{ length: Math.max(7, Math.min(12, Math.round(height / 68))) }}, (_, index) => ({{
          baseY: height * 0.14 + (height * 0.72 / Math.max(6, Math.min(11, Math.round(height / 68)))) * index,
          amp: 8 + (index % 4) * 2.8 + Math.random() * 3.2,
          freq: 0.007 + Math.random() * 0.004,
          phase: Math.random() * Math.PI * 2,
          speed: 0.5 + Math.random() * 0.45,
          drift: 5 + Math.random() * 8,
          alpha: 0.08 + (index % 3) * 0.025,
          width: 0.9 + (index % 4) * 0.18,
        }}));
      }};

      const pointFor = (node, time) => ({{
        x: node.x + Math.sin(time * 0.00042 + node.phase) * node.rangeX,
        y: node.y + Math.cos(time * 0.00036 + node.phase) * node.rangeY,
      }});

      const drawNode = (node, point) => {{
        ctx.save();
        ctx.translate(point.x, point.y);
        ctx.fillStyle = "rgba(" + palette.node + ", 0.88)";
        ctx.strokeStyle = "rgba(" + palette.line + ", 0.14)";
        ctx.lineWidth = 0.8;

        if (node.kind === "packing") {{
          roundRect(-4.8, -3.3, 9.6, 6.6, 2.3);
          ctx.fill();
          ctx.stroke();
        }} else if (node.kind === "port") {{
          ctx.rotate(Math.PI / 4);
          roundRect(-3.5, -3.5, 7, 7, 1.8);
          ctx.fill();
          ctx.stroke();
        }} else if (node.kind === "shipment") {{
          roundRect(-5.3, -2.8, 10.6, 5.6, 2.8);
          ctx.fill();
          ctx.stroke();
        }} else {{
          ctx.beginPath();
          ctx.arc(0, 0, node.size, 0, Math.PI * 2);
          ctx.fill();
          ctx.stroke();
        }}

        ctx.restore();
      }};

      const drawHarbor = (time = 0) => {{
        if (!width || !height) return;
        ctx.clearRect(0, 0, width, height);

        const points = new Map();
        nodes.forEach((node) => points.set(node.id, pointFor(node, time)));

        [
          {{ x: width * 0.16, y: height * 0.22, r: Math.min(width, height) * 0.18, alpha: 0.055 }},
          {{ x: width * 0.78, y: height * 0.72, r: Math.min(width, height) * 0.22, alpha: 0.045 }},
        ].forEach((glow) => {{
          const gradient = ctx.createRadialGradient(glow.x, glow.y, 0, glow.x, glow.y, glow.r);
          gradient.addColorStop(0, "rgba(" + palette.glow + ", " + glow.alpha + ")");
          gradient.addColorStop(1, "rgba(255, 255, 255, 0)");
          ctx.fillStyle = gradient;
          ctx.beginPath();
          ctx.arc(glow.x, glow.y, glow.r, 0, Math.PI * 2);
          ctx.fill();
        }});

        lanes.forEach((lane) => {{
          const a = points.get(lane.a.id);
          const b = points.get(lane.b.id);
          const shimmer = prefersReducedMotion.matches ? 0.5 : (Math.sin(time * 0.00026 + lane.glowPhase) + 1) / 2;
          const gradient = ctx.createLinearGradient(a.x, a.y, b.x, b.y);
          gradient.addColorStop(0, "rgba(" + palette.line + ", 0.025)");
          gradient.addColorStop(0.5, "rgba(" + palette.line + ", " + (0.08 + lane.emphasis * 0.18 + shimmer * 0.08).toFixed(3) + ")");
          gradient.addColorStop(1, "rgba(" + palette.line + ", 0.03)");
          ctx.strokeStyle = gradient;
          ctx.lineWidth = lane.emphasis > 0.35 ? 1.15 : 0.9;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }});

        nodes.forEach((node) => {{
          const point = points.get(node.id);
          const halo = ctx.createRadialGradient(point.x, point.y, 0, point.x, point.y, 12);
          halo.addColorStop(0, "rgba(" + palette.glow + ", 0.1)");
          halo.addColorStop(1, "rgba(255, 255, 255, 0)");
          ctx.fillStyle = halo;
          ctx.beginPath();
          ctx.arc(point.x, point.y, 12, 0, Math.PI * 2);
          ctx.fill();
          drawNode(node, point);
        }});
      }};

      const drawContour = (time = 0) => {{
        if (!width || !height) return;
        ctx.clearRect(0, 0, width, height);

        const driftTime = prefersReducedMotion.matches ? 0 : time * 0.00022;

        [
          {{ x: width * 0.2, y: height * 0.26, r: Math.min(width, height) * 0.2, alpha: 0.045 }},
          {{ x: width * 0.74, y: height * 0.7, r: Math.min(width, height) * 0.24, alpha: 0.05 }},
        ].forEach((glow) => {{
          const gradient = ctx.createRadialGradient(glow.x, glow.y, 0, glow.x, glow.y, glow.r);
          gradient.addColorStop(0, "rgba(" + palette.glow + ", " + glow.alpha + ")");
          gradient.addColorStop(1, "rgba(255, 255, 255, 0)");
          ctx.fillStyle = gradient;
          ctx.beginPath();
          ctx.arc(glow.x, glow.y, glow.r, 0, Math.PI * 2);
          ctx.fill();
        }});

        contours.forEach((contour, index) => {{
          ctx.beginPath();
          const steps = Math.max(26, Math.round(width / 18));
          for (let step = 0; step <= steps; step += 1) {{
            const x = (width / steps) * step;
            const waveA = Math.sin(x * contour.freq + driftTime * contour.speed + contour.phase) * contour.amp;
            const waveB = Math.cos(x * contour.freq * 0.52 - driftTime * contour.speed * 0.78 + contour.phase * 1.2) * contour.amp * 0.56;
            const lift = Math.sin(driftTime * 0.8 + contour.phase) * contour.drift;
            const y = contour.baseY + waveA + waveB + lift;
            if (step === 0) {{
              ctx.moveTo(x, y);
            }} else {{
              ctx.lineTo(x, y);
            }}
          }}
          ctx.strokeStyle = "rgba(" + palette.contour + ", " + contour.alpha + ")";
          ctx.lineWidth = contour.width;
          ctx.stroke();

          if (index % 3 === 0) {{
            ctx.beginPath();
            for (let step = 0; step <= steps; step += 1) {{
              const x = (width / steps) * step;
              const waveA = Math.sin(x * contour.freq + driftTime * contour.speed + contour.phase + 0.16) * (contour.amp * 0.92);
              const waveB = Math.cos(x * contour.freq * 0.52 - driftTime * contour.speed * 0.78 + contour.phase * 1.2) * contour.amp * 0.42;
              const lift = Math.sin(driftTime * 0.8 + contour.phase) * contour.drift;
              const y = contour.baseY + waveA + waveB + lift + 5.5;
              if (step === 0) {{
                ctx.moveTo(x, y);
              }} else {{
                ctx.lineTo(x, y);
              }}
            }}
            ctx.strokeStyle = "rgba(" + palette.glow + ", 0.09)";
            ctx.lineWidth = 0.9;
            ctx.stroke();
          }}
        }});
      }};

      const draw = (time = 0) => {{
        if (mode === "contour") {{
          drawContour(time);
        }} else {{
          drawHarbor(time);
        }}
      }};

      const resize = () => {{
        const rect = canvas.getBoundingClientRect();
        width = Math.max(260, Math.round(rect.width));
        height = Math.max(180, Math.round(rect.height));
        dpr = Math.min(window.devicePixelRatio || 1, 2);
        canvas.width = width * dpr;
        canvas.height = height * dpr;
        canvas.style.width = width + "px";
        canvas.style.height = height + "px";
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        if (mode === "contour") {{
          buildContour();
        }} else {{
          buildHarbor();
        }}
        draw(performance.now());
      }};

      const loop = (time) => {{
        draw(time);
        if (!prefersReducedMotion.matches) {{
          frameId = window.requestAnimationFrame(loop);
        }}
      }};

      resize();
      if (!prefersReducedMotion.matches) {{
        frameId = window.requestAnimationFrame(loop);
      }}

      const onResize = () => resize();
      window.addEventListener("resize", onResize);

      return () => {{
        if (frameId) window.cancelAnimationFrame(frameId);
        window.removeEventListener("resize", onResize);
      }};
    }};

    if (reveals.length) {{
      const observer = new IntersectionObserver(
        (entries) => {{
          entries.forEach((entry) => {{
            if (entry.isIntersecting) {{
              entry.target.classList.add("reveal", "is-visible");
            }}
          }});
        }},
        {{ threshold: 0.14 }}
      );

      reveals.forEach((element) => {{
        element.classList.add("reveal");
        observer.observe(element);
      }});
    }}

    if (menuToggle && mobileMenu) {{
      const mobileBreakpoint = window.matchMedia("(max-width: 900px)");
      const closeMobileMenu = () => {{
        mobileMenu.setAttribute("hidden", "");
        menuToggle.setAttribute("aria-expanded", "false");
      }};

      const syncMobileMenuState = () => {{
        if (!mobileBreakpoint.matches) {{
          closeMobileMenu();
        }}
      }};

      closeMobileMenu();

      menuToggle.addEventListener("click", () => {{
        if (!mobileBreakpoint.matches) {{
          closeMobileMenu();
          return;
        }}
        const open = mobileMenu.hasAttribute("hidden");
        if (open) {{
          mobileMenu.removeAttribute("hidden");
        }} else {{
          closeMobileMenu();
        }}
        menuToggle.setAttribute("aria-expanded", String(open));
      }});

      mobileMenu.querySelectorAll("a").forEach((link) => {{
        link.addEventListener("click", () => {{
          closeMobileMenu();
        }});
      }});

      document.addEventListener("click", (event) => {{
        if (mobileMenu.hasAttribute("hidden")) return;
        const target = event.target;
        if (!(target instanceof Node)) return;
        if (mobileMenu.contains(target) || menuToggle.contains(target)) return;
        closeMobileMenu();
      }});

      document.addEventListener("keydown", (event) => {{
        if (event.key === "Escape") {{
          closeMobileMenu();
        }}
      }});

      if (mobileBreakpoint.addEventListener) {{
        mobileBreakpoint.addEventListener("change", syncMobileMenuState);
      }} else if (mobileBreakpoint.addListener) {{
        mobileBreakpoint.addListener(syncMobileMenuState);
      }}
      window.addEventListener("resize", syncMobileMenuState);
    }}

    const initCorridorStage = (stage) => {{
      const items = Array.from(stage.querySelectorAll("[data-corridor-item]"));
      if (!items.length) {{
        return;
      }}

      let activeIndex = items.findIndex((item) => item.classList.contains("is-active"));
      let timerId = 0;

      if (activeIndex < 0) {{
        activeIndex = 0;
      }}

      const update = (nextIndex) => {{
        activeIndex = (nextIndex + items.length) % items.length;

        items.forEach((item, index) => {{
          const isActive = index === activeIndex;
          item.classList.toggle("is-active", isActive);
          item.setAttribute("aria-pressed", String(isActive));
        }});
      }};

      const stopAutoplay = () => {{
        if (!timerId) return;
        window.clearInterval(timerId);
        timerId = 0;
      }};

      const startAutoplay = () => {{
        if (prefersReducedMotion.matches || items.length < 2) return;
        stopAutoplay();
        timerId = window.setInterval(() => {{
          update(activeIndex + 1);
        }}, 3600);
      }};

      items.forEach((item, index) => {{
        item.addEventListener("click", () => {{
          update(index);
          startAutoplay();
        }});
      }});

      stage.addEventListener("mouseenter", stopAutoplay);
      stage.addEventListener("mouseleave", startAutoplay);
      stage.addEventListener("focusin", stopAutoplay);
      stage.addEventListener("focusout", startAutoplay);

      update(activeIndex);
      startAutoplay();
    }};

    const inquiryEndpoint = "https://formsubmit.co/ajax/{CONTACT["sales_email"]}";

    const setRequestType = (requestType) => {{
      formTargets.forEach((form) => {{
        const select = form.querySelector('[name="request_type"]');
        if (select) {{
          select.value = requestType;
        }}
      }});
    }};

    requestLinks.forEach((link) => {{
      link.addEventListener("click", () => {{
        const requestType = link.dataset.setRequest;
        if (requestType) {{
          setRequestType(requestType);
        }}
      }});
    }});

    formTargets.forEach((form) => {{
      const note = form.querySelector("[data-form-note]");
      const submitButton = form.querySelector('button[type="submit"]');
      note?.setAttribute("aria-live", "polite");

      if (submitButton) {{
        submitButton.dataset.defaultLabel = submitButton.textContent.trim();
      }}

      form.addEventListener("submit", async (event) => {{
        event.preventDefault();
        if (!submitButton) return;

        const data = new FormData(form);
        const requestType = data.get("request_type")?.toString().trim() || "Inquiry";
        const product = data.get("product")?.toString().trim() || "Not specified";
        const email = data.get("email")?.toString().trim() || "Not provided";

        data.append("_subject", `${{requestType}} | ${{product}}`);
        data.append("_template", "table");
        data.append("_captcha", "false");
        data.append("_replyto", email);
        data.append("Source Page", window.location.href);
        data.append("Page Title", document.title);

        submitButton.disabled = true;
        submitButton.textContent = "Sending...";

        if (note) {{
          note.textContent = "Sending the inquiry directly. Please wait a moment.";
        }}

        try {{
          const response = await fetch(inquiryEndpoint, {{
            method: "POST",
            body: data,
            headers: {{
              Accept: "application/json",
            }},
          }});

          const result = await response.json().catch(() => null);
          if (!response.ok || result?.success === false || result?.success === "false") {{
            throw new Error(result?.message || "Submission failed");
          }}

          form.reset();
          if (note) {{
            note.textContent = "Inquiry sent. We will review the requirement and respond by email.";
          }}
        }} catch (error) {{
          if (note) {{
            note.textContent = "Submission did not go through. Please email {CONTACT["sales_email"]} or call {CONTACT["phone"]}.";
          }}
        }} finally {{
          submitButton.disabled = false;
          submitButton.textContent = submitButton.dataset.defaultLabel || "Send Inquiry";
        }}
      }});
    }});

    yearTargets.forEach((target) => {{
      target.textContent = String(new Date().getFullYear());
    }});

    if (portfolioAnchors.length && portfolioStages.length) {{
      const anchorMap = new Map(
        Array.from(portfolioAnchors).map((anchor) => [anchor.getAttribute("href"), anchor])
      );

      const setActiveAnchor = (id) => {{
        anchorMap.forEach((anchor, href) => {{
          anchor.classList.toggle("is-active", href === `#${{id}}`);
        }});
      }};

      const stageObserver = new IntersectionObserver(
        (entries) => {{
          const visibleEntry = entries
            .filter((entry) => entry.isIntersecting)
            .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

          if (visibleEntry?.target?.id) {{
            setActiveAnchor(visibleEntry.target.id);
          }}
        }},
        {{
          rootMargin: "-20% 0px -55% 0px",
          threshold: [0.2, 0.45, 0.7],
        }}
      );

      portfolioStages.forEach((stage) => stageObserver.observe(stage));

      const firstStage = portfolioStages[0];
      if (firstStage?.id) {{
        setActiveAnchor(firstStage.id);
      }}
    }}

    routeNetworks.forEach((canvas) => {{
      initRouteNetwork(canvas);
    }});

    corridorStages.forEach((stage) => {{
      initCorridorStage(stage);
    }});

    syncHeader();
    syncParallax();
    window.addEventListener("scroll", syncHeader, {{ passive: true }});
    window.addEventListener("scroll", syncParallax, {{ passive: true }});
    window.addEventListener("resize", syncParallax);
    """
).strip()


def render_robots() -> str:
    return dedent(
        f"""
        User-agent: *
        Allow: /

        Sitemap: {BASE_URL}/sitemap.xml
        """
    ).strip()


def render_sitemap() -> str:
    urls = [
        "/",
        "/blog/",
        "/hear-from-ceo/",
        "/export-markets/",
        "/industrial-minerals-exporter-india/",
        "/operations/",
        "/privacy-policy/",
        "/products/",
        "/terms-disclaimer/",
        *[f"/blog/{post['slug']}/" for post in BLOGS if post["slug"] in CURRENT_BLOG_SLUGS],
        *[f"/products/{product['slug']}/" for product in ACTIVE_PRODUCTS],
    ]
    entries = "\n".join(
        f"  <url><loc>{BASE_URL}{path}</loc><lastmod>{TODAY}</lastmod></url>"
        for path in urls
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
      if blog_post["slug"] in CURRENT_BLOG_SLUGS:
        write(ROOT / "blog" / blog_post["slug"] / "index.html", render_blog_post_page(blog_post))
    for slug, target in REDIRECT_BLOG_TARGETS.items():
      write(
          ROOT / "blog" / slug / "index.html",
          render_redirect_page(
              "Blog Redirect | Jade Waves Enterprise",
              "This article has been consolidated into the current Jade Waves content hub.",
              f"/blog/{slug}/",
              target,
          ),
      )
    write(ROOT / "hear-from-ceo" / "index.html", render_ceo_page())
    write(ROOT / "export-markets" / "index.html", render_export_markets_page())
    write(ROOT / "industrial-minerals-exporter-india" / "index.html", render_exporter_profile_page())
    write(ROOT / "products" / "index.html", render_products_index())
    for product in ACTIVE_PRODUCTS:
      write(ROOT / "products" / product["slug"] / "index.html", render_product_page(product))
    for slug, target in REDIRECT_PRODUCT_TARGETS.items():
      product_name = slug.replace("-", " ").replace("--", " ")
      write(
          ROOT / "products" / slug / "index.html",
          render_redirect_page(
              f"{product_name.title()} Redirect | Jade Waves Enterprise",
              "This product page has been consolidated into the current Jade Waves portfolio.",
              f"/products/{slug}/",
              target,
          ),
      )
    write(ROOT / "robots.txt", render_robots())
    write(ROOT / "sitemap.xml", render_sitemap())


if __name__ == "__main__":
    main()
