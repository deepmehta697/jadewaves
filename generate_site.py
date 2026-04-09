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
        "Quartz, feldspar, kaolin, talc, and silica flour for bodies, tiles, and glaze-linked production.",
    ),
    (
        "Construction",
        "Fly ash, silica, and copper slag for concrete, infrastructure, and mineral-heavy site demand.",
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
        "Silica sand and bentonite for moulding systems that depend on repeatable sizing and binding strength.",
    ),
]

PRODUCTS = [
    {
        "slug": "silica-sand",
        "name": "Silica Sand",
        "family": "Silica, Quartz & Feldspar",
        "anchor": "silica-quartz-feldspar",
        "theme": "silica",
        "eyebrow": "Glass / Filtration / Foundry / Construction",
        "seo_title": "Silica Sand Supplier from India for Import Buyers | Jade Waves Enterprise",
        "meta_description": "Silica sand supplier from India for import buyers in Vietnam, Thailand, the Philippines, UAE, Saudi Arabia, Mauritius, and Maldives.",
        "hero_copy": "Silica sand for glass, filtration, foundry, and construction buyers who need clean chemistry, steady grain size, and export handling that stays under control.",
        "short_copy": "Silica sand supplied for glass, filtration, foundry, and construction use.",
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
        "meta_description": "Quartz sand supplier from India for import buyers in Vietnam, Thailand, the Philippines, Malaysia, UAE, and Saudi Arabia.",
        "hero_copy": "Quartz sand, grits, and powder for ceramics, glass, and engineered stone where purity, whiteness, and sizing shape the result.",
        "short_copy": "Quartz sand, grits, and powder for ceramics, glass, and engineered stone.",
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
        "seo_title": "Bentonite Supplier from India for Import Buyers | Jade Waves Enterprise",
        "meta_description": "Bulk bentonite supplier from India for import buyers in Vietnam, UAE, Oman, Qatar, Bahrain, Saudi Arabia, and Malaysia.",
        "hero_copy": "Bentonite for drilling, foundry, sealing, absorbent, and bleaching grades where swelling, viscosity, and moisture control need to stay dependable.",
        "short_copy": "Bentonite supplied for drilling, foundry, sealing, absorbent, and bleaching use.",
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
        "seo_title": "Feldspar Supplier from India for Import Buyers | Jade Waves Enterprise",
        "meta_description": "Potassium and sodium feldspar supplier from India for import buyers in Vietnam, Thailand, the Philippines, UAE, Malaysia, and Saudi Arabia.",
        "hero_copy": "Potassium and sodium feldspar supplied for ceramic, sanitaryware, tile, glass, and engineered stone production where flux behavior, melting control, and cleaner firing matter.",
        "short_copy": "Potassium and sodium feldspar for ceramics, sanitaryware, glass, and engineered stone production.",
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
        "seo_title": "Industrial Salt Supplier from India for Import Buyers | Jade Waves Enterprise",
        "meta_description": "Industrial salt supplier from India for import buyers in UAE, Oman, Qatar, Bahrain, Saudi Arabia, Mauritius, and Maldives.",
        "hero_copy": "Industrial and iodized salt grades for chemical processing, treatment systems, infrastructure, and food-linked demand, with flexible packing and dependable export flow.",
        "short_copy": "Iodized and non-iodized salt grades for chemical, utility, and food-linked supply.",
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

PRODUCT_FAMILIES = [
    {
        "id": "silica-quartz-feldspar",
        "name": "Silica, Quartz & Feldspar",
        "copy": "Purity-led grades for glass, ceramics, filtration, and engineered stone.",
        "best_for": ["Glass", "Ceramics", "Filtration", "Engineered Stone"],
        "products": ["silica-sand", "silica-flour", "quartz-sand-for-ceramics", "feldspar"],
    },
    {
        "id": "clays-fillers",
        "name": "Clays & Functional Fillers",
        "copy": "Functional minerals for drilling, coatings, absorbents, ceramics, and process use.",
        "best_for": ["Drilling", "Ceramics", "Coatings", "Absorbents"],
        "products": ["bentonite", "kaolin--china-clay", "talc"],
    },
    {
        "id": "salt-grades",
        "name": "Industrial Salt Grades",
        "copy": "Salt grades arranged for chemical processing, treatment systems, utilities, and volume buying.",
        "best_for": ["Chemical Processing", "Water Treatment", "Utilities", "Food Supply"],
        "products": ["salt"],
    },
    {
        "id": "construction-media",
        "name": "Construction & Industrial Media",
        "copy": "Media and mineral inputs for concrete, blasting, infrastructure, and site-led demand.",
        "best_for": ["Blasting", "Concrete", "Infrastructure", "Surface Preparation"],
        "products": ["fly-ash", "copper-slag"],
    },
]

HOME_FEATURED = ["silica-sand", "bentonite", "feldspar"]

BLOGS = [
    {
        "title": "Glass Grade Silica Sand",
        "url": "https://jadewavesenterprise.com/blogs/f/glass-grade-silica-sand",
        "eyebrow": "Silica Insights",
        "copy": "A focused topic for buyers evaluating silica grades for glass-oriented production.",
    },
    {
        "title": "Bentonite Suppliers in Saudi Arabia",
        "url": "https://jadewavesenterprise.com/blogs/f/bentonite-suppliers-in-saudi-arabia",
        "eyebrow": "Regional Supply",
        "copy": "A market-facing note for buyers sourcing bentonite into Saudi Arabia.",
    },
    {
        "title": "Kaolin / China Clay Suppliers in India",
        "url": "https://jadewavesenterprise.com/blogs/f/kaolin-china-clay-suppliers-in-india",
        "eyebrow": "Material Guides",
        "copy": "A practical read for ceramic, coating, paper, and filler buyers comparing kaolin sources.",
    },
]

EXPORT_MARKETS = [
    {
        "slug": "quartz-sand-vietnam",
        "title": "Quartz Sand Supplier from India for Vietnam Buyers",
        "meta_description": "Quartz sand supplier from India for Vietnam ceramic, glass, and engineered stone buyers comparing purity, sizing, packing, and dispatch reliability.",
        "eyebrow": "Vietnam / Ceramics / Glass",
        "headline": "Quartz sand from India for Vietnam ceramic and glass buyers.",
        "summary": "Use this route when the buying brief centers on quartz sand, grits, or powder for tile bodies, ceramic plants, glass batches, or engineered stone demand in Vietnam.",
        "product_slugs": ["quartz-sand-for-ceramics", "silica-sand", "feldspar"],
        "market_points": [
            "Quartz sand, grits, and powder options aligned to ceramic and glass use.",
            "Specification-first discussions on SiO2, whiteness, grain size, and packing.",
            "Useful for buyers comparing multiple India quartz suppliers before trial or volume orders.",
        ],
    },
    {
        "slug": "feldspar-vietnam",
        "title": "Feldspar Supplier from India for Vietnam Buyers",
        "meta_description": "Feldspar supplier from India for Vietnam ceramic, sanitaryware, and glass buyers sourcing potassium and sodium feldspar grades.",
        "eyebrow": "Vietnam / Feldspar / Ceramics",
        "headline": "Feldspar supply from India for Vietnam ceramic and glass production.",
        "summary": "Built for Vietnam buyers sourcing potassium feldspar or sodium feldspar for ceramic bodies, sanitaryware, glaze systems, and glass production.",
        "product_slugs": ["feldspar", "quartz-sand-for-ceramics", "kaolin--china-clay"],
        "market_points": [
            "Potassium and sodium feldspar grades matched to ceramic and glass use.",
            "Conversations start around K2O, Na2O, Fe2O3, mesh size, and packing.",
            "Designed for import buyers narrowing suppliers before sample approval.",
        ],
    },
    {
        "slug": "feldspar-thailand",
        "title": "Feldspar Supplier from India for Thailand Buyers",
        "meta_description": "Feldspar supplier from India for Thailand import buyers sourcing ceramic and glass grades with controlled K2O, Na2O, Fe2O3, and mesh size.",
        "eyebrow": "Thailand / Feldspar / Ceramics",
        "headline": "Feldspar from India for Thailand ceramic and glass buyers.",
        "summary": "For Thailand buyers who need potassium or sodium feldspar with cleaner chemistry discussions before pricing, sampling, and dispatch.",
        "product_slugs": ["feldspar", "quartz-sand-for-ceramics", "kaolin--china-clay"],
        "market_points": [
            "Feldspar grades suited to ceramic, sanitaryware, and glass production.",
            "Useful when comparing India feldspar suppliers for repeat import programs.",
            "Built around export handling, packing, and order-fit discussions.",
        ],
    },
    {
        "slug": "silica-sand-maldives",
        "title": "Silica Sand Supplier from India for Maldives Buyers",
        "meta_description": "Silica sand supplier from India for Maldives buyers sourcing filtration, construction, and industrial silica sand with export-ready packing.",
        "eyebrow": "Maldives / Silica Sand / Filtration",
        "headline": "Silica sand from India for Maldives import buyers.",
        "summary": "A focused entry page for Maldives buyers sourcing silica sand for filtration, construction, or related mineral demand where dispatch and packing matter.",
        "product_slugs": ["silica-sand", "silica-flour"],
        "market_points": [
            "Silica sand supply for filtration, foundry, and construction-linked demand.",
            "Useful for Maldives buyers comparing bulk silica sand imports from India.",
            "Clear discussions on chemistry, grain size, packing, and shipment basis.",
        ],
    },
    {
        "slug": "silica-sand-philippines",
        "title": "Silica Sand Supplier from India for Philippines Buyers",
        "meta_description": "Silica sand supplier from India for Philippines import buyers sourcing glass, filtration, foundry, and construction grades.",
        "eyebrow": "Philippines / Silica Sand / Glass",
        "headline": "Silica sand from India for Philippines glass and industrial buyers.",
        "summary": "For Philippines buyers comparing silica sand suppliers from India for glass manufacturing, filtration, foundry use, and construction demand.",
        "product_slugs": ["silica-sand", "silica-flour", "quartz-sand-for-ceramics"],
        "market_points": [
            "Glass, filtration, foundry, and construction silica grades.",
            "Structured around import-buyer questions on Fe2O3, SiO2, sizing, and packing.",
            "Supports trial, sample, and volume conversations with export context.",
        ],
    },
    {
        "slug": "bentonite-vietnam-gulf",
        "title": "Bentonite Supplier from India for Vietnam and Gulf Buyers",
        "meta_description": "Bentonite supplier from India for Vietnam, UAE, Oman, Qatar, Bahrain, and Saudi Arabia buyers sourcing drilling, foundry, and bleaching grades.",
        "eyebrow": "Vietnam + Gulf / Bentonite",
        "headline": "Bentonite from India for Vietnam and Gulf import buyers.",
        "summary": "A route for buyers sourcing sodium bentonite, calcium bentonite, or bleaching earth grades into Vietnam and the Gulf region.",
        "product_slugs": ["bentonite", "talc"],
        "market_points": [
            "Drilling, foundry, sealing, absorbent, and bleaching bentonite discussions.",
            "Useful for Gulf and Southeast Asia buyers comparing India bentonite sources.",
            "Built around viscosity, liquid limit, moisture, and packing clarity.",
        ],
    },
    {
        "slug": "bentonite-saudi-arabia",
        "title": "Bentonite Supplier from India for Saudi Arabia Buyers",
        "meta_description": "Bentonite supplier from India for Saudi Arabia import buyers sourcing drilling, foundry, civil, absorbent, and bleaching earth grades.",
        "eyebrow": "Saudi Arabia / Bentonite",
        "headline": "Bentonite from India for Saudi Arabia buyers.",
        "summary": "For Saudi Arabia buyers sourcing bentonite from India for drilling fluids, foundry systems, sealing work, absorbent applications, or bleaching earth use.",
        "product_slugs": ["bentonite"],
        "market_points": [
            "Application-led bentonite discussions before price comparisons begin.",
            "Useful for Saudi buyers evaluating India bentonite suppliers for repeated imports.",
            "Commercial fit built around grade, viscosity, moisture, and packing.",
        ],
    },
    {
        "slug": "industrial-salt-uae",
        "title": "Industrial Salt Supplier from India for UAE Buyers",
        "meta_description": "Industrial salt supplier from India for UAE import buyers sourcing bulk non-iodized and iodized salt for chemical, treatment, and utility demand.",
        "eyebrow": "UAE / Industrial Salt",
        "headline": "Industrial salt from India for UAE buyers.",
        "summary": "This page targets UAE buyers sourcing industrial salt or selected edible grades from India for chemical processing, water treatment, utilities, and related demand.",
        "product_slugs": ["salt"],
        "market_points": [
            "Industrial salt and selected iodized or non-iodized grades for import planning.",
            "Useful for UAE buyers comparing India salt suppliers on purity, grain size, and packing.",
            "Built for bulk and repeat-order discussions rather than one-off commodity listings.",
        ],
    },
    {
        "slug": "talc-malaysia",
        "title": "Talc Powder Supplier from India for Malaysia Buyers",
        "meta_description": "Talc powder supplier from India for Malaysia import buyers sourcing plastics, paint, rubber, ceramic, detergent, and filler grades.",
        "eyebrow": "Malaysia / Talc Powder",
        "headline": "Talc powder from India for Malaysia import buyers.",
        "summary": "For Malaysia buyers comparing talc powder suppliers from India for plastics, coatings, rubber, ceramics, detergents, and industrial fillers.",
        "product_slugs": ["talc", "kaolin--china-clay"],
        "market_points": [
            "High-whiteness talc powder routes for plastics, coatings, ceramics, and fillers.",
            "Useful for Malaysia import buyers comparing mesh size, whiteness, and packing options.",
            "Commercial conversations start with grade fit, not generic talc listings.",
        ],
    },
    {
        "slug": "quartz-feldspar-ceramic-glass",
        "title": "Quartz and Feldspar Supplier from India for Ceramic and Glass Buyers",
        "meta_description": "Quartz and feldspar supplier from India for ceramic and glass buyers in Vietnam, Thailand, Malaysia, UAE, and Saudi Arabia.",
        "eyebrow": "Ceramic + Glass / Export Markets",
        "headline": "Quartz and feldspar from India for ceramic and glass production.",
        "summary": "A broader route for buyers who source both quartz and feldspar into ceramic, tile, sanitaryware, glass, and engineered stone lines.",
        "product_slugs": ["quartz-sand-for-ceramics", "feldspar", "kaolin--china-clay"],
        "market_points": [
            "Useful when the buying brief spans multiple ceramic or glass minerals, not just one line item.",
            "Supports early comparison around chemistry, flux behavior, whiteness, and sizing.",
            "Internal links point directly to the exact product pages for deeper spec review.",
        ],
    },
]

EXPORT_MARKETS_BY_SLUG = {market["slug"]: market for market in EXPORT_MARKETS}
PRODUCT_MARKET_LINKS = {
    "silica-sand": ["silica-sand-philippines", "silica-sand-maldives", "quartz-sand-vietnam"],
    "silica-flour": ["silica-sand-philippines", "quartz-sand-vietnam"],
    "quartz-sand-for-ceramics": ["quartz-sand-vietnam", "quartz-feldspar-ceramic-glass", "feldspar-thailand"],
    "feldspar": ["feldspar-vietnam", "feldspar-thailand", "quartz-feldspar-ceramic-glass"],
    "bentonite": ["bentonite-saudi-arabia", "bentonite-vietnam-gulf"],
    "kaolin--china-clay": ["feldspar-thailand", "quartz-feldspar-ceramic-glass", "talc-malaysia"],
    "talc": ["talc-malaysia", "bentonite-vietnam-gulf"],
    "salt": ["industrial-salt-uae"],
    "fly-ash": ["industrial-salt-uae"],
    "copper-slag": ["industrial-salt-uae"],
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
        '<link rel="stylesheet" href="/styles.css" />',
        f"{base_bootstrap}\n            <link rel=\"stylesheet\" href=\"styles.css\" />",
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
    return safe_markup


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
    for product in PRODUCTS:
        options.append(f'<option value="{escape(product["name"])}">{escape(product["name"])}</option>')
    return "<select name=\"product\">" + "".join(options) + "</select>"


def related_links(slugs: list[str]) -> str:
    links = []
    for slug in slugs:
        product = PRODUCTS_BY_SLUG[slug]
        links.append(
            f'<a href="/products/{product["slug"]}/">{escape(product["name"])}</a>'
        )
    return "".join(links)


def market_links(slugs: list[str]) -> str:
    cards = []
    for slug in slugs:
        market = EXPORT_MARKETS_BY_SLUG[slug]
        cards.append(
            dedent(
                f"""
                <a class="market-card" href="/export-markets/{market["slug"]}/">
                  <p class="market-card__eyebrow">{escape(market["eyebrow"])}</p>
                  <h3>{escape(market["title"])}</h3>
                  <p>{escape(market["summary"])}</p>
                  <span class="market-card__cta">Open market page</span>
                </a>
                """
            ).strip()
        )
    return "".join(cards)


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


def render_export_markets_index() -> str:
    market_cards = market_links([market["slug"] for market in EXPORT_MARKETS])
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
                <p class="hero-label">Export Markets</p>
                <h1>Product routes for priority import markets.</h1>
                <p class="hero-text">
                  These pages are built for buyers searching by product plus country, especially when the buying intent is to import from India into Southeast Asia, the Gulf, Mauritius, and Maldives.
                </p>
              </div>
            </div>
          </section>
          <section class="section-block">
            <div class="shell section-shell">
              <div class="section-intro" data-reveal>
                <p class="section-label">Priority Markets</p>
                <h2>Country and region pages with direct product links.</h2>
                <p>Each route narrows to the products, specification cues, and import conversations most likely to matter in that market.</p>
              </div>
              <div class="market-grid">{market_cards}</div>
            </div>
          </section>
        </main>
        {footer_html()}
        """
    ).strip()
    schema = [
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Jade Waves Export Markets", "url": f"{BASE_URL}/export-markets/"},
    ]
    return page_shell(
        "Industrial Minerals Export Markets | Jade Waves Enterprise",
        "Country and region pages for import buyers sourcing industrial minerals from India into Southeast Asia, the Gulf, Mauritius, and Maldives.",
        "/export-markets/",
        body,
        schema,
        "page-portfolio",
    )


def render_export_market_page(market: dict) -> str:
    product_cards = "".join(
        dedent(
            f"""
            <a class="portfolio-product" href="/products/{product["slug"]}/">
              <div class="portfolio-product__main">
                <p class="portfolio-product__eyebrow">{escape(product["eyebrow"])}</p>
                <h3>{escape(product["name"])}</h3>
                <p class="portfolio-product__fit"><span>Best for</span>{escape(product["short_copy"])}</p>
              </div>
              <span class="portfolio-product__arrow">View product</span>
            </a>
            """
        ).strip()
        for product in (PRODUCTS_BY_SLUG[slug] for slug in market["product_slugs"])
    )
    market_points = "".join(
        dedent(
            f"""
            <article class="product-line">
              <span>{index:02d}</span>
              <div>
                <strong>{escape(point)}</strong>
              </div>
            </article>
            """
        ).strip()
        for index, point in enumerate(market["market_points"], start=1)
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
                <div class="breadcrumb">
                  <a href="/">Home</a>
                  <span>/</span>
                  <a href="/export-markets/">Export Markets</a>
                  <span>/</span>
                  <strong>{escape(market["title"])}</strong>
                </div>
                <p class="hero-label">{escape(market["eyebrow"])}</p>
                <h1>{escape(market["headline"])}</h1>
                <p class="hero-text">{escape(market["summary"])}</p>
                <div class="hero-actions">
                  <a class="button button--light" href="#contact" data-set-request="Quote">Request Quote</a>
                  <a class="button button--ghost" href="/products/">Browse Products</a>
                </div>
              </div>
            </div>
          </section>
          <section class="section-block">
            <div class="shell product-ledger">
              <article class="product-sheet product-sheet--wide" data-reveal>
                <p class="section-label">Market Fit</p>
                <h2>What this page is intended to capture.</h2>
                <div class="product-line-list">{market_points}</div>
              </article>
              <article class="product-sheet" data-reveal>
                <p class="section-label">Commercial Flow</p>
                <h2>How buyers usually start.</h2>
                <p class="product-sheet__body">Most import conversations begin with the application, chemistry, size, packing, target destination, and expected monthly volume. This page narrows those questions before product-level review starts.</p>
              </article>
            </div>
          </section>
          <section class="section-block section-block--contrast">
            <div class="shell section-shell">
              <div class="section-intro" data-reveal>
                <p class="section-label">Linked Products</p>
                <h2>Open the exact product pages next.</h2>
                <p>These are the product pages most relevant to this country or regional search route.</p>
              </div>
              <div class="portfolio-stage__track" data-reveal>
                {product_cards}
              </div>
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
        {"@context": "https://schema.org", "@type": "WebPage", "name": market["title"], "url": f"{BASE_URL}/export-markets/{market['slug']}/"},
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
                {"@type": "ListItem", "position": 2, "name": "Export Markets", "item": f"{BASE_URL}/export-markets/"},
                {"@type": "ListItem", "position": 3, "name": market["title"], "item": f"{BASE_URL}/export-markets/{market['slug']}/"},
            ],
        },
    ]
    return page_shell(
        market["title"] + " | Jade Waves Enterprise",
        market["meta_description"],
        f"/export-markets/{market['slug']}/",
        body,
        schema,
        "page-portfolio",
    )


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
    market_markup = market_links([
        "quartz-sand-vietnam",
        "feldspar-thailand",
        "silica-sand-philippines",
        "industrial-salt-uae",
        "bentonite-saudi-arabia",
        "talc-malaysia",
    ])
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
                <h1>A better way to buy industrial minerals.</h1>
                <p class="hero-text">
                  Industrial minerals exported from India for import buyers who need clearer specifications, cleaner communication, and shipment flow that stays visible.
                </p>
                <div class="hero-actions">
                  <a class="button button--light" href="/products/">Explore Portfolio</a>
                  <a class="button button--ghost" href="/#contact" data-set-request="Quote">Request Quote</a>
                  <a class="button button--ghost" href="/#contact" data-set-request="Sample">Request Sample</a>
                </div>
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

          <section class="section-block">
            <div class="shell section-shell">
              <div class="section-intro" data-reveal>
                <p class="section-label">Priority Export Markets</p>
                <h2>Country pages built around import intent.</h2>
                <p>These routes are designed to catch searches that combine your product with a country market and an India-origin supplier intent.</p>
              </div>
              <div class="market-grid">{market_markup}</div>
            </div>
          </section>

          <section class="section-block section-block--contrast" id="industries">
            <div class="shell section-shell">
              <div class="home-split">
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

          <section class="section-block section-block--contrast">
            <div class="shell section-shell">
              <article class="ceo-spotlight" data-reveal>
                <div class="ceo-spotlight__grid">
                  <div class="ceo-spotlight__content">
                    <p class="section-label">From Our CEO</p>
                    <h2>A simple standard.</h2>
                    <p class="ceo-spotlight__quote">“Be clear on what is possible. Be early on what could change. Stand behind the shipment.”</p>
                    <div class="ceo-spotlight__body">
                      <p>
                        Jade Waves was built around a simple idea: industrial sourcing should feel calmer when the right details are handled early.
                      </p>
                      <p>
                        That means clearer specifications, direct communication, and follow-through that holds from the first message to dispatch.
                      </p>
                    </div>
                    <p class="ceo-spotlight__meta"><span>Deep Mehta</span><span>CEO, Jade Waves Enterprise</span></p>
                    <div class="ceo-spotlight__actions">
                      <a class="button button--light button--compact" href="{escape(CEO_LINKEDIN_URL)}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                    </div>
                  </div>
                  <figure class="ceo-spotlight__media">
                    <img src="/assets/deep-mehta-ceo.jpg" alt="Deep Mehta, CEO of Jade Waves Enterprise" loading="lazy" />
                  </figure>
                </div>
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
                for index, product in enumerate(PRODUCTS)
            ],
        },
    ]
    return page_shell(
        "Industrial Mineral Exporter from India for Global Buyers | Jade Waves Enterprise",
        "Industrial mineral exporter from India serving import buyers in Vietnam, Thailand, the Philippines, UAE, Oman, Qatar, Bahrain, Mauritius, Maldives, Malaysia, Singapore, and Saudi Arabia.",
        "/",
        home_body,
        schema,
        "page-home",
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
                  Use the portfolio to find industrial minerals supplied from India for import buyers in Southeast Asia, the Gulf, Mauritius, and Maldives.
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
                for index, product in enumerate(PRODUCTS)
            ],
        },
    ]
    return page_shell(
        "Industrial Minerals Supplier from India | Jade Waves Enterprise",
        "Industrial minerals supplier from India for import buyers in Vietnam, Thailand, the Philippines, UAE, Oman, Qatar, Bahrain, Mauritius, Maldives, Malaysia, Singapore, and Saudi Arabia.",
        "/products/",
        body,
        schema,
        "page-portfolio",
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
    sizes_card = ""
    if product.get("size_options"):
        sizes_card = dedent(
            f"""
              <article class="product-sheet product-sheet--full" data-reveal>
                <p class="section-label">Sizes Available</p>
                <h2>Readily Available Sizes</h2>
                <div class="size-cloud">{size_pills}</div>
              </article>
            """
        ).strip()
    commercial_tags = "".join(f'<span>{escape(item)}</span>' for item in product["industries"])
    related = related_links(product["related"])
    market_section = ""
    market_slugs = PRODUCT_MARKET_LINKS.get(product["slug"], [])
    if market_slugs:
        market_section = dedent(
            f"""
            <section class="section-block">
              <div class="shell section-shell">
                <div class="section-intro" data-reveal>
                  <p class="section-label">Priority Markets</p>
                  <h2>Country pages linked to this product.</h2>
                  <p>These export-market pages help connect country-specific import searches to the right product route.</p>
                </div>
                <div class="market-grid" data-reveal>{market_links(market_slugs)}</div>
              </div>
            </section>
            """
        ).strip()
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

          {market_section}

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

    .market-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 1.1rem;
    }

    .market-card {
      display: grid;
      gap: 0.85rem;
      padding: 1.35rem;
      border-radius: 1.5rem;
      background: rgba(255, 255, 255, 0.88);
      border: 1px solid rgba(29, 29, 31, 0.08);
      box-shadow: 0 14px 34px rgba(29, 29, 31, 0.06);
      transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    }

    .market-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 20px 42px rgba(29, 29, 31, 0.09);
      border-color: rgba(0, 113, 227, 0.18);
    }

    .market-card__eyebrow {
      margin: 0;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      font-size: 0.7rem;
      font-weight: 800;
      color: rgba(29, 29, 31, 0.46);
    }

    .market-card h3 {
      margin: 0;
      line-height: 1.15;
      font-size: 1.18rem;
      letter-spacing: -0.04em;
    }

    .market-card p {
      margin: 0;
      color: rgba(29, 29, 31, 0.66);
      line-height: 1.65;
      font-size: 0.96rem;
    }

    .market-card__cta {
      font-weight: 700;
      color: var(--ore);
      font-size: 0.92rem;
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

    .industry-line h3 {
      margin: 0 0 0.45rem;
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
      .product-ledger {
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

      .home-poster {
        min-height: 28rem;
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

      .market-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
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

      .section-topline {
        flex-direction: column;
        align-items: flex-start;
      }

      .section-topline--stack {
        align-items: flex-start;
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

      .market-grid {
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
      menuToggle.addEventListener("click", () => {{
        const open = mobileMenu.hasAttribute("hidden");
        if (open) {{
          mobileMenu.removeAttribute("hidden");
        }} else {{
          mobileMenu.setAttribute("hidden", "");
        }}
        menuToggle.setAttribute("aria-expanded", String(open));
      }});

      mobileMenu.querySelectorAll("a").forEach((link) => {{
        link.addEventListener("click", () => {{
          mobileMenu.setAttribute("hidden", "");
          menuToggle.setAttribute("aria-expanded", "false");
        }});
      }});
    }}

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
    urls: list[str] = []
    for path in sorted(ROOT.rglob("index.html")):
        if "_site" in path.parts or ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        if rel.name != "index.html":
            continue
        parent = rel.parent.as_posix()
        url_path = "/" if parent == "." else f"/{parent}/"
        urls.append(url_path)
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
    write(ROOT / "export-markets" / "index.html", render_export_markets_index())
    for market in EXPORT_MARKETS:
        write(ROOT / "export-markets" / market["slug"] / "index.html", render_export_market_page(market))
    write(ROOT / "products" / "index.html", render_products_index())
    for product in PRODUCTS:
      write(ROOT / "products" / product["slug"] / "index.html", render_product_page(product))
    write(ROOT / "robots.txt", render_robots())
    write(ROOT / "sitemap.xml", render_sitemap())


if __name__ == "__main__":
    main()
