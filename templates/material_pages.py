"""Material Ledger page compositions for the static site generator.

The first argument is the generator namespace so shared contact, product data,
inquiry behaviour, and the document shell remain a single source of truth.
"""

from html import escape
import re


def _shell(g, title, description, path, content, schema, page_class):
    body = f'{g["nav_html"]()}<main class="ml-main" id="main-content">{content}</main>{g["footer_html"]()}'
    return g["page_shell"](title, description, path, body, schema, f"{page_class} page-ledger")


def _organization(g):
    contact = g["CONTACT"]
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": contact["company"],
        "url": g["BASE_URL"],
        "email": contact["sales_email"],
        "telephone": contact["phone"],
        "address": {"@type": "PostalAddress", "streetAddress": contact["address"], "addressCountry": "IN"},
    }


def _breadcrumbs(g, entries):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": index, "name": name, "item": g["BASE_URL"] + path}
            for index, (name, path) in enumerate([("Home", "")] + entries, start=1)
        ],
    }


def _product_list(g):
    return {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Jade Waves Enterprise Product Portfolio",
        "itemListElement": [
            {"@type": "ListItem", "position": index, "url": f'{g["BASE_URL"]}/products/{product["slug"]}/', "name": product["name"]}
            for index, product in enumerate(g["CATALOGUE_PRODUCTS"], start=1)
        ],
    }


def _visual(g, slug, kind="hero"):
    visual = g["PRODUCT_VISUALS"].get(slug, {})
    return visual.get(kind) or visual.get("hero") or "/assets/optimized/quarry-quartz.jpg", visual.get("alt", "Industrial mineral material")


def _actions(g, primary="Request a specification", href="#contact", secondary="View material portfolio", secondary_href="/products/", request="TDS"):
    return f'''<div class="ml-actions">
      <a class="button button--dark ml-button" href="{escape(href)}" data-set-request="{escape(request)}">{escape(primary)}</a>
      <a class="ml-text-link" href="{escape(secondary_href)}">{escape(secondary)} <span aria-hidden="true">↗</span></a>
    </div>'''


def _photo_hero(g, title, copy, image, alt, label, primary="Request a specification", secondary="View material portfolio", secondary_href="/products/", proof=None, material=False):
    facts = proof or ["Near Mundra Port", "50 kg / jumbo bags", "COA & TDS", "FCL export handling"]
    proof_markup = "".join(f'<span>{escape(fact)}</span>' for fact in facts)
    return f'''<section class="ml-hero{' ml-material-hero' if material else ''}" aria-labelledby="page-heading">
      <img class="ml-hero-media" src="{escape(image)}" alt="{escape(alt)}" loading="eager" fetchpriority="high" />
      <div class="ml-hero-overlay" aria-hidden="true"></div>
      <div class="ml-container ml-hero-content">
        <div class="ml-hero-copy" data-reveal>
          <p class="ml-eyebrow ml-brand-line">{escape(label)}</p>
          <h1 id="page-heading">{escape(title)}</h1>
          <p class="ml-hero-description">{escape(copy)}</p>
          {_actions(g, primary=primary, secondary=secondary, secondary_href=secondary_href)}
          <div class="ml-hero-proof" aria-label="Supply information">{proof_markup}</div>
        </div>
      </div>
      <p class="ml-hero-caption">{escape(alt)}</p>
    </section>'''


def _heading(g, label, title, copy="", link="", href=""):
    action = f'<a class="ml-text-link" href="{escape(href)}">{escape(link)} <span aria-hidden="true">↗</span></a>' if link else ""
    paragraph = f'<p>{escape(copy)}</p>' if copy else ""
    return f'<div class="ml-section-head" data-reveal><div><p class="ml-eyebrow">{escape(label)}</p><h2>{escape(title)}</h2>{paragraph}</div>{action}</div>'


def _ledger(g, rows):
    return '<div class="ml-ledger">' + "".join(
        f'<div class="ml-ledger-row" data-reveal><span class="ml-ledger-number">{index:02d}</span><h3 class="ml-ledger-label">{escape(label)}</h3><p class="ml-ledger-text">{escape(text)}</p></div>'
        for index, (label, text) in enumerate(rows, start=1)
    ) + '</div>'


def _family(g, family, index):
    image, alt = _visual(g, family["visual_slug"])
    by_slug = g["CATALOGUE_BY_SLUG"]
    links = "".join(
        f'<a href="/products/{escape(slug)}/"><span>{escape(by_slug[slug]["name"])}</span><span aria-hidden="true">↗</span></a>'
        for slug in family["products"] if slug in by_slug
    )
    return f'''<article class="ml-family" data-reveal>
      <a class="ml-family-media" href="/products/#{escape(family["id"])}" aria-label="Explore {escape(family["name"])}">
        <img src="{escape(image)}" alt="{escape(alt)}" loading="lazy" />
      </a>
      <div class="ml-family-content">
        <p class="ml-eyebrow">Material family / {index:02d}</p>
        <h3>{escape(family["name"])}</h3>
        <p>{escape(family["copy"])}</p>
        <div class="ml-family-links">{links}</div>
      </div>
    </article>'''


def _directory(g, products, detailed=False):
    rows = []
    for product in products:
        image, alt = _visual(g, product["slug"], "thumb")
        if detailed:
            tds = g["TDS_BY_SLUG"].get(product["slug"])
            document = f'<a class="ml-text-link ml-directory-document" href="{escape(tds)}" target="_blank" rel="noopener">TDS <span aria-hidden="true">↗</span></a>' if tds else f'<a class="ml-text-link ml-directory-document" href="/products/{escape(product["slug"])}/#contact" data-set-request="TDS">Request technical data <span aria-hidden="true">↗</span></a>'
            if product['slug'] == 'pebbles':
                document = '<a class="ml-text-link ml-directory-document" href="/products/pebbles/#collection">Explore colours &amp; sizes <span aria-hidden="true">↗</span></a>'
            rows.append(f'''<article class="ml-directory-row ml-directory-row--detailed" data-reveal>
              <a class="ml-directory-thumb" href="/products/{escape(product["slug"])}/" tabindex="-1" aria-hidden="true"><img class="ml-thumbnail" src="{escape(image)}" alt="" loading="lazy" /></a>
              <div class="ml-directory-name"><h3><a href="/products/{escape(product["slug"])}/">{escape(product["name"])}</a></h3><p>{escape(" · ".join(product["forms"]))}</p></div>
              <div class="ml-directory-detail"><p>{escape(" / ".join(product["applications"][:2]))}</p><span>{escape(product.get("summary_spec", product["specs"][0]))}</span></div>
              {document}
            </article>''')
        else:
            rows.append(f'''<a class="ml-directory-row" href="/products/{escape(product["slug"])}/" data-reveal>
              <span class="ml-directory-thumb"><img class="ml-thumbnail" src="{escape(image)}" alt="" loading="lazy" /></span>
              <span class="ml-directory-name">{escape(product["name"])}</span>
              <span class="ml-directory-detail">{escape(" / ".join(product["industries"][:2]))}</span>
              <span class="ml-directory-arrow" aria-hidden="true">↗</span>
            </a>''')
    return '<div class="ml-directory">' + ''.join(rows) + '</div>'


def _process(g, product=None):
    product_name = product["name"] if product else "material"
    steps = [
        ("Requirement", f"Share the {product_name.lower()}, application, destination, and expected volume."),
        ("Grade alignment", "Confirm chemistry, size range, and the form required by your process."),
        ("Sample / COA", "Review the sample and technical references for the discussed grade."),
        ("Packing & dispatch", "Approve packing, shipment basis, and documents before loading."),
    ]
    steps_markup = ''.join(
        f'<li class="ml-process-step" data-reveal><span>{index:02d}</span><h3>{escape(title)}</h3><p>{escape(text)}</p></li>'
        for index, (title, text) in enumerate(steps, start=1)
    )
    return f'''<section class="ml-section ml-section--process" id="process"><div class="ml-container">
      {_heading(g, "Supply route", "From specification to vessel.", "Four approvals that connect the material requirement to the loading plan.")}
      <ol class="ml-process">{steps_markup}</ol>
      <figure class="ml-process-image" data-reveal><img src="/assets/optimized/packing-area.jpg" alt="Industrial mineral packing area with material bags prepared for shipment" loading="lazy" /><figcaption>Packing preparation · Export supply from India</figcaption></figure>
    </div></section>'''


def _gallery(g):
    images = [
        ("/assets/optimized/factory-view.jpg", "Mineral processing facility", "01 / Processing facility", "ml-evidence-wide"),
        ("/assets/optimized/manual-sorting.jpg", "Manual sorting of mineral material", "02 / Material sorting", ""),
        ("/assets/container-loading-wide.jpeg", "Bagged industrial minerals loaded in an export container", "03 / Container loading", "ml-evidence-tall"),
        ("/assets/silica-sand-coa-preview.png", "Preview of a silica sand certificate of analysis", "04 / Silica sand · COA reference", "ml-evidence-document"),
    ]
    figures = []
    for image, alt, caption, class_name in images:
        photograph = f'<img src="{escape(image)}" alt="{escape(alt)}" loading="lazy" />'
        if class_name == "ml-evidence-document":
            photograph = f'<a href="/assets/silica-sand-coa-premium-final.pdf" target="_blank" rel="noopener" aria-label="Open silica sand certificate of analysis PDF">{photograph}</a>'
        figures.append(f'<figure class="ml-evidence {class_name}" data-reveal>{photograph}<figcaption>{escape(caption)}</figcaption></figure>')
    return f'''<section class="ml-section ml-section--evidence"><div class="ml-container">
      {_heading(g, "Field evidence", "The material. The handling. The paperwork.", link="See operations", href="/operations/")}
      <div class="ml-gallery">{''.join(figures)}</div>
    </div></section>'''


def _brief(g, product_name=""):
    return f'<section class="ml-section ml-section--brief"><div class="ml-container ml-brief">{g["form_block"](product_name)}</div></section>'


def _editorial_hero(g, label, title, copy, image, alt, primary="Talk to the export desk", secondary="View material portfolio", secondary_href="/products/", contact=True):
    actions = _actions(g, primary=primary, request="Quote", secondary=secondary, secondary_href=secondary_href) if contact else f'<a class="ml-text-link" href="{escape(secondary_href)}">{escape(secondary)} <span aria-hidden="true">↗</span></a>'
    return f'''<section class="ml-editorial-hero"><div class="ml-container ml-editorial-layout">
      <div class="ml-editorial-copy" data-reveal><p class="ml-eyebrow">{escape(label)}</p><h1>{escape(title)}</h1><p class="ml-editorial-description">{escape(copy)}</p>{actions}</div>
      <figure class="ml-editorial-media" data-reveal><img src="{escape(image)}" alt="{escape(alt)}" loading="eager" fetchpriority="high" /><figcaption>{escape(alt)}</figcaption></figure>
    </div></section>'''


def render_homepage(g):
    featured_families = [family for family in g["PRODUCT_FAMILIES"] if family["id"] in {"silica-quartz-feldspar", "clays-functional-fillers", "industrial-media-pozzolans"}]
    proof = [
        ("Product fit", "Application, chemistry, and size range aligned to the requirement."),
        ("Sample & documents", "Sample COA and TDS shared for review before grade approval."),
        ("Packing", "50 kg and jumbo bag options matched to loading and unloading."),
        ("Export control", "Mundra access, FCL handling, documentation, and dispatch updates."),
    ]
    content = _photo_hero(g, "Industrial minerals from India.", "Chemistry, packing, and export handling aligned before your cargo moves.", "/assets/optimized/quarry-quartz.jpg", "Quartz quarry · India", "Jade Waves Enterprise / Industrial Mineral Export")
    content += f'''<section class="ml-section ml-section--ledger" id="about"><div class="ml-container">
      {_heading(g, "The supply brief", "Material clarity. Export discipline.", "Industrial mineral supply from India, with the buying details settled early.", "Company profile", "/industrial-minerals-exporter-india/")}
      {_ledger(g, proof)}
    </div></section>
    <section class="ml-section ml-section--families"><div class="ml-container">
      {_heading(g, "Material families", "Start with what your process needs.")}
      {''.join(_family(g, family, index) for index, family in enumerate(featured_families, start=1))}
    </div></section>
    <section class="ml-section ml-section--directory"><div class="ml-container">
      {_heading(g, "The complete directory", "Every material, in one place.", link="Compare the portfolio", href="/products/")}
      {_directory(g, g["CATALOGUE_PRODUCTS"])}
    </div></section>'''
    content += _process(g) + _gallery(g)
    content += f'''<section class="ml-section ml-section--markets" id="countries-served"><div class="ml-container ml-market-note" data-reveal>
      <div><p class="ml-eyebrow">Export markets</p><h2>From India to your discharge port.</h2></div>
      <div><p>Gulf · Southeast Asia · Mauritius · Maldives</p><a class="ml-text-link" href="/export-markets/">Read the destination brief <span aria-hidden="true">↗</span></a></div>
    </div></section>'''
    content += _brief(g)
    return _shell(g, "Industrial Mineral Exporter from India | Jade Waves Enterprise", "Industrial minerals from India for glass, ceramics, construction, and other industrial buyers. Review grades, technical references, packing, and export plans.", "/", content, [_organization(g), _product_list(g)], "page-home")


def render_products_index(g):
    content = _photo_hero(g, "The industrial mineral portfolio.", "Compare materials by application, grade, and available form. Open the technical reference before you build the brief.", "/assets/optimized/quarry-quartz.jpg", "Quartz quarry · Mineral supply from India", "Jade Waves Enterprise / Material Portfolio", secondary="Browse materials", secondary_href="#material-directory", proof=[f'{len(g["PRODUCT_FAMILIES"])} material families', f'{len(g["CATALOGUE_PRODUCTS"])} products', "Technical references", "Sample-led approval"])
    anchors = ''.join(f'<a href="#{escape(family["id"])}">{escape(family["name"])}</a>' for family in g["PRODUCT_FAMILIES"])
    content += f'<div class="ml-container ml-family-nav" aria-label="Material families"><nav>{anchors}</nav></div><div id="material-directory">'
    for index, family in enumerate(g["PRODUCT_FAMILIES"], start=1):
        products = [g["CATALOGUE_BY_SLUG"][slug] for slug in family["products"] if slug in g["CATALOGUE_BY_SLUG"]]
        content += f'''<section class="ml-section ml-section--portfolio" id="{escape(family["id"])}"><div class="ml-container">
          {_heading(g, f"Family / {index:02d}", family["name"], family["copy"])}
          <p class="ml-family-applications">{' / '.join(escape(item) for item in family["best_for"])}</p>
          {_directory(g, products, detailed=True)}
        </div></section>'''
    content += '</div>' + _brief(g)
    schema = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Jade Waves Enterprise Product Portfolio", "url": g["BASE_URL"] + "/products/"}, _product_list(g)]
    return _shell(g, "Industrial Minerals Supplier from India | Jade Waves Enterprise", "Compare silica sand, quartz, feldspar, clays, salt, and other materials from India. Review applications, grades, technical references, and packing for export.", "/products/", content, schema, "page-portfolio")


def _specification_rows(g, product):
    rows = []
    for item in product["specs"]:
        if ":" in item:
            label, value = item.split(":", 1)
        else:
            match = re.search(r"\s+(?=[<>]?\d)", item)
            if match:
                label, value = item[:match.start()], item[match.end():]
            else:
                label, value = "Grade reference", item
        rows.append((label, value))
    rows.extend([
        ("Available forms", " · ".join(product["forms"])),
        ("Size options", " · ".join(product.get("size_options", [])) or "Confirm the required grain, mesh, or micron range with the export desk."),
        ("Packing", product["packing"]),
        ("Shipment basis", "FCL export handling from India; destination and commercial terms to be agreed."),
    ])
    return ''.join(f'<tr><th scope="row">{escape(label)}</th><td>{escape(value.strip())}</td></tr>' for label, value in rows)


def _documents(g, product):
    links = []
    tds = g["TDS_BY_SLUG"].get(product["slug"])
    if tds:
        links.append(("Technical data sheet", "TDS / PDF", tds))
    coa_names = {"quartz-sand-for-ceramics": "quartz-sand", "kaolin--china-clay": "china-clay"}
    if product["slug"] in g["TDS_BY_SLUG"]:
        coa_slug = coa_names.get(product["slug"], product["slug"])
        links.append(("Sample certificate of analysis", "COA / PDF", f"/assets/coas/{coa_slug}-sample-coa.pdf"))
    links.extend((label, "Parameter sheet / PDF", href) for label, href in product.get("parameter_docs", []))
    markup = ''.join(f'<a class="ml-document" href="{escape(href)}" target="_blank" rel="noopener"><span>{escape(kind)}</span><strong>{escape(label)}</strong><span aria-hidden="true">↗</span></a>' for label, kind, href in links)
    if not links:
        markup = '<a class="ml-document" href="#contact" data-set-request="TDS"><span>Technical reference</span><strong>Request grade and specification details</strong><span aria-hidden="true">↗</span></a>'
    return '<div class="ml-document-list">' + markup + '</div>'


def render_product_page(g, product):
    image, alt = _visual(g, product["slug"])
    content = _photo_hero(g, product["name"], product.get("short_copy", product["hero_copy"]), image, alt, "Jade Waves Enterprise / " + product["family"], secondary="Read specification", secondary_href="#specification", material=True, proof=[product.get("summary_spec", product["specs"][0]), product["packing"], "COA & TDS", "FCL export handling"])
    content += f'''<section class="ml-section" id="specification"><div class="ml-container ml-spec-layout">
      <div>{_heading(g, "Specification snapshot", "Read the grade before the quote.", "Published references are a starting point. Confirm the required grade and sample COA against your application.")}</div>
      <div class="ml-table-wrap" data-reveal><table class="ml-spec-table"><caption>{escape(product["name"])} · Grade, form, and supply reference</caption><tbody>{_specification_rows(g, product)}</tbody></table></div>
    </div></section>'''
    applications = [(item, "") for item in product["applications"]]
    checks = ''.join(f'<li>{escape(point)}</li>' for point in product.get("booking_points", product["specs"]))
    content += f'''<section class="ml-section ml-section--applications"><div class="ml-container ml-use-layout">
      <div>{_heading(g, "Application fit", "Where this material works.")}{_ledger(g, applications)}</div>
      <aside class="ml-buying-checks" data-reveal><p class="ml-eyebrow">Before ordering</p><h3>Build the technical brief.</h3><ul>{checks}</ul><p>{escape(product["commercial_fit"])}</p></aside>
    </div></section>
    <section class="ml-section ml-section--documents" id="technical-documents"><div class="ml-container ml-document-layout">
      <div>{_heading(g, "Technical evidence", "Documents for your review.", product.get("parameter_docs_copy", "TDS and sample COA references for the discussed material. Confirm the applicable grade before approval."))}{_documents(g, product)}</div>
      <figure class="ml-evidence" data-reveal><img src="/assets/optimized/packing-area.jpg" alt="Packing area for bagged industrial mineral shipments" loading="lazy" /><figcaption>Packing basis / {escape(product["packing"])}</figcaption></figure>
    </div></section>'''
    content += _process(g, product)
    faq_markup, faq_schema = g["render_faq"](product)
    faq_markup = faq_markup.replace('class="faq-item"', 'class="ml-faq"')
    content += f'<section class="ml-section"><div class="ml-container">{_heading(g, "Buyer questions", "Before you confirm supply.")}<div class="ml-faq-list">{faq_markup}</div></div></section>'
    guides = [post for post in _current_posts(g) if post["product_slug"] == product["slug"]]
    if guides:
        content += f'<section class="ml-section ml-section--guides"><div class="ml-container">{_heading(g, "Buyer guides", "Prepare your material brief.", "Review grade selection, sample checks, and the questions to include in your inquiry.")}{_journal_rows(g, guides)}</div></section>'
    related = [g["PRODUCTS_BY_SLUG"][slug] for slug in product["related"] if slug in g["PRODUCTS_BY_SLUG"]]
    if related:
        content += f'<section class="ml-section ml-section--related"><div class="ml-container">{_heading(g, "Related materials", "Continue your comparison.")}{_directory(g, related)}</div></section>'
    content += _brief(g, product["name"])
    path = f'/products/{product["slug"]}/'
    schema = [
        {"@context": "https://schema.org", "@type": "Product", "name": product["name"], "description": product["meta_description"], "category": product.get("category", "Industrial Mineral"), "brand": {"@type": "Brand", "name": g["CONTACT"]["company"]}, "manufacturer": {"@type": "Organization", "name": g["CONTACT"]["company"]}, "url": g["BASE_URL"] + path, "image": g["BASE_URL"] + image},
        _breadcrumbs(g, [("Products", "/products/"), (product["name"], path)]),
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_schema},
    ]
    return _shell(g, product["seo_title"], product["meta_description"], path, content, schema, "page-product")


def render_export_markets_page(g):
    content = _editorial_hero(g, "Export markets", "A clear brief, for every destination.", "Industrial mineral supply from India for buyers across the Gulf, Southeast Asia, Mauritius, and Maldives.", "/assets/container-loading-wide.jpeg", "Bagged minerals · Container loading")
    regions = [
        ("Gulf", "UAE · Saudi Arabia · Oman · Qatar · Bahrain", "Confirm specification, packing, shipment basis, and the destination port before cargo planning.", ["Application and chemistry limits", "Bag size and unloading requirements", "Commercial terms and dispatch timing"]),
        ("Southeast Asia", "Vietnam · Thailand · Philippines · Malaysia · Singapore", "Start with the end use, then narrow the chemistry and sizing for your glass, ceramic, or industrial process.", ["Required grain or mesh range", "Sample and technical review", "Trial and repeat order volume"]),
        ("Indian Ocean", "Mauritius · Maldives", "Align the shipment quantity and packing with available storage, unloading, and vessel planning.", ["Discharge port and handling constraints", "Packing and container loading plan", "Document set and delivery window"]),
    ]
    content += f'<section class="ml-section"><div class="ml-container">{_heading(g, "Destination briefing", "Different ports. The same attention to detail.")}<div class="ml-regions">'
    for index, (region, countries, copy, checks) in enumerate(regions, start=1):
        content += f'<article class="ml-region" data-reveal><span class="ml-ledger-number">{index:02d}</span><div><h3>{escape(region)}</h3><p class="ml-region-countries">{escape(countries)}</p></div><div><p>{escape(copy)}</p><ul>{"".join(f"<li>{escape(item)}</li>" for item in checks)}</ul></div></article>'
    content += '</div></div></section>' + _process(g) + _brief(g)
    description = "Industrial mineral supply from India for buyers across the Gulf, Southeast Asia, Mauritius, and Maldives."
    schema = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Export Markets", "description": description, "url": g["BASE_URL"] + "/export-markets/"}, _breadcrumbs(g, [("Export Markets", "/export-markets/")])]
    return _shell(g, "Industrial Mineral Export Markets | Jade Waves Enterprise", description, "/export-markets/", content, schema, "page-export-markets")


def render_exporter_profile_page(g):
    content = _editorial_hero(g, "Company profile / India", "Jade Waves Enterprise.", "Industrial mineral supply, with specification, packing, and export execution considered together.", "/assets/optimized/factory-view.jpg", "Mineral processing facility · India")
    rows = [
        ("Company base", "Ahmedabad, Gujarat, India."),
        ("Core supply", "Silica sand, quartz sand, and feldspar, with clays, fillers, and industrial media in the portfolio."),
        ("Technical review", "Application, chemistry, grain or mesh size, sample COA, and TDS."),
        ("Export handling", "Packing, documents, and FCL dispatch planning near Mundra Port."),
    ]
    content += f'''<section class="ml-section"><div class="ml-container">
      {_heading(g, "Operating profile", "Close to the material. Clear on the requirement.", "Import teams need an explicit grade, a practical packing plan, and a contact who stays reachable through dispatch.")}
      {_ledger(g, rows)}
    </div></section>
    <section class="ml-section"><div class="ml-container ml-editorial-layout">
      <div class="ml-reading" data-reveal><p class="ml-eyebrow">How we work</p><h2>Settle the material decision early.</h2><p>We start with the end use and the parameters that matter to your production line. Chemistry alone is only part of the requirement: form, sizing, packing, and destination affect the supply plan too.</p><p>Technical references and sample discussions are linked to the proposed grade. Packing, shipment basis, and paperwork are agreed before loading becomes time-sensitive.</p><a class="ml-text-link" href="/hear-from-ceo/">A note from Deep Mehta <span aria-hidden="true">↗</span></a></div>
      <figure class="ml-editorial-media" data-reveal><img src="/assets/optimized/manual-sorting.jpg" alt="Sorting quartz material before processing" loading="lazy" /><figcaption>Material sorting / Grade preparation</figcaption></figure>
    </div></section>'''
    content += _process(g) + _brief(g)
    description = "Industrial mineral exporter from India with clear specification handling and dependable export follow-through."
    schema = [{"@context": "https://schema.org", "@type": "AboutPage", "name": "Industrial Minerals Exporter India", "description": description, "url": g["BASE_URL"] + "/industrial-minerals-exporter-india/"}, _organization(g), _breadcrumbs(g, [("Industrial Minerals Exporter India", "/industrial-minerals-exporter-india/")])]
    return _shell(g, "Industrial Minerals Exporter from India | Jade Waves Enterprise", description, "/industrial-minerals-exporter-india/", content, schema, "page-exporter-profile")


def render_ceo_page(g):
    content = _editorial_hero(g, "Hear from our CEO", "A note for buyers.", "Agree the specification first, review the technical references early, and keep the export plan visible until cargo moves.", "/assets/deep-mehta-ceo.jpg", "Deep Mehta · CEO, Jade Waves Enterprise", secondary="Connect on LinkedIn", secondary_href=g["CEO_LINKEDIN_URL"])
    content += f'''<section class="ml-section"><div class="ml-container ml-ceo-note">
      <p class="ml-eyebrow" data-reveal>From Deep Mehta</p>
      <div class="ml-reading" data-reveal><blockquote>“Clarity before commitment. Discipline in execution. Communication that stays direct from inquiry to dispatch.”</blockquote><p>We do not treat export supply as only cargo movement. Our responsibility is to make sure your team receives material aligned to your end use, with the right packing, document discipline, and commercial clarity.</p><p>We manufacture and export silica sand, quartz sand, and feldspar from India for buyers who value repeat-order reliability.</p><p>You will have a directly reachable team member during inquiry, sampling, documentation, and dispatch.</p><p class="ml-signature"><strong>Deep Mehta</strong><span>CEO, Jade Waves Enterprise</span></p></div>
    </div></section>'''
    rows = [
        ("Requirement clarity", "End use, chemistry, grain size, and packing basis aligned before the quote."),
        ("Technical references", "TDS and sample COA shared for evaluation against the discussed grade."),
        ("Commercial agreement", "Shipment basis, packing plan, and document expectations confirmed early."),
        ("Dispatch visibility", "Direct loading and shipment updates from planning to cargo movement."),
        ("Repeat orders", "The agreed grade and operating method carried into the next supply program."),
    ]
    content += f'<section class="ml-section"><div class="ml-container">{_heading(g, "Working commitments", "What your team can expect.")}{_ledger(g, rows)}</div></section>' + _brief(g)
    schema = [
        {"@context": "https://schema.org", "@type": "AboutPage", "name": "Hear from our CEO", "description": "CEO message on manufacturer-led mineral supply, technical clarity, and dependable export execution for global buyers.", "url": g["BASE_URL"] + "/hear-from-ceo/"},
        {"@context": "https://schema.org", "@type": "Person", "name": "Deep Mehta", "jobTitle": "CEO", "worksFor": {"@type": "Organization", "name": g["CONTACT"]["company"]}, "url": g["CEO_LINKEDIN_URL"], "image": g["BASE_URL"] + "/assets/deep-mehta-ceo.jpg"},
        _breadcrumbs(g, [("Hear from our CEO", "/hear-from-ceo/")]),
    ]
    return _shell(g, "A Note for Buyers | Jade Waves Enterprise", "CEO message from Jade Waves Enterprise on how we align technical fit, packing, and export execution for global mineral buyers.", "/hear-from-ceo/", content, schema, "page-ceo")


def _current_posts(g):
    return [post for post in g["BLOGS"] if post["slug"] in g.get("CURRENT_BLOG_SLUGS", {post["slug"] for post in g["BLOGS"]})]


def _journal_rows(g, posts):
    return '<div class="ml-journal-list">' + ''.join(
        f'<article class="ml-journal-row" data-reveal><p class="ml-eyebrow">{escape(post["eyebrow"])}</p><div><h3><a href="/blog/{escape(post["slug"])}/">{escape(post["title"])}</a></h3><p>{escape(post["summary"])}</p></div><a class="ml-text-link" href="/blog/{escape(post["slug"])}/" aria-label="Read {escape(post["title"])}">Read guide <span aria-hidden="true">↗</span></a></article>'
        for post in posts
    ) + '</div>'


def render_blog_index_page(g):
    posts = _current_posts(g)
    content = _editorial_hero(g, "The buyer journal", "Industrial mineral buyer guides.", "Practical guides for import teams reviewing mineral grades, technical references, and export requirements.", "/assets/silica-sand-samples.png", "Silica sand samples · Grain-size comparison", contact=False, secondary="Browse material portfolio", secondary_href="/products/")
    content += f'<section class="ml-section"><div class="ml-container">{_heading(g, "Buyer guides", "Before you prepare the RFQ.")}{_journal_rows(g, posts)}</div></section>'
    content += _brief(g)
    schema = [
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Buyer and Importer Blog", "url": g["BASE_URL"] + "/blog/", "description": "Buyer guide hub for import teams reviewing industrial mineral sourcing, specification checks, and export planning from India."},
        {"@context": "https://schema.org", "@type": "ItemList", "name": "Published Buyer Guides", "itemListElement": [{"@type": "ListItem", "position": index, "url": f'{g["BASE_URL"]}/blog/{post["slug"]}/', "name": post["title"]} for index, post in enumerate(posts, start=1)]},
    ]
    return _shell(g, "Industrial Mineral Buyer Guides | Jade Waves Enterprise", "Buyer guides for 11 materials, from silica and feldspar to clays, salt, and industrial media. Review grade selection, sample evidence, and export requirements.", "/blog/", content, schema, "page-blog")


def render_blog_post_page(g, post):
    product = g["PRODUCTS_BY_SLUG"][post["product_slug"]]
    image, alt = _visual(g, product["slug"])
    title_lines = post.get("display_title_lines")
    visible_title = "<br />".join(escape(line) for line in title_lines) if title_lines else escape(post["title"])
    dates = g["article_dates"](post)
    date_markup = ''.join(
        f'<span>{label} <time datetime="{escape(dates[key])}">{escape(dates[key])}</time></span>'
        for key, label in (("datePublished", "Published"), ("dateModified", "Updated"))
        if key in dates and (key != "dateModified" or dates[key] != dates.get("datePublished"))
    )
    content = f'''<header class="ml-article-header"><div class="ml-container">
      <nav class="ml-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/blog/">Buyer guides</a></nav>
      <p class="ml-eyebrow" data-reveal>{escape(post["eyebrow"])}</p><h1 data-reveal>{visible_title}</h1><p class="ml-article-summary" data-reveal>{escape(post["summary"])}</p>
      <div class="ml-article-meta"><span>Jade Waves Enterprise / Buyer guide</span>{date_markup}<a class="ml-text-link" href="/products/{escape(product["slug"])}/">{escape(product["name"])} technical reference <span aria-hidden="true">↗</span></a></div>
    </div></header>
    <section class="ml-section ml-section--article"><div class="ml-container ml-article-layout"><article class="ml-reading ml-article">'''
    for section in post["sections"]:
        points = ''.join(f'<li>{escape(point)}</li>' for point in section.get("points", []))
        content += f'<section class="ml-reading-section" data-reveal><h2>{escape(section["heading"])}</h2><p>{escape(section["body"])}</p><ul>{points}</ul></section>'
    questions = ''.join(f'<li>{escape(question)}</li>' for question in post["questions"])
    content += f'''</article><aside class="ml-article-aside"><figure class="ml-evidence"><img src="{escape(image)}" alt="{escape(alt)}" loading="lazy" /><figcaption>{escape(product["name"])} / Material reference</figcaption></figure><div class="ml-buying-checks" data-reveal><p class="ml-eyebrow">RFQ checklist</p><h2>Questions for your first inquiry.</h2><ul>{questions}</ul><a class="ml-text-link" href="#contact" data-set-request="Quote">Send your requirement <span aria-hidden="true">↗</span></a></div></aside></div></section>'''
    related = sorted(
        (item for item in _current_posts(g) if item["slug"] != post["slug"]),
        key=lambda item: (
            item["product_slug"] != post["product_slug"],
            g["PRODUCTS_BY_SLUG"][item["product_slug"]]["family"] != product["family"],
        ),
    )[:3]
    if related:
        content += f'<section class="ml-section"><div class="ml-container">{_heading(g, "Further reading", "Continue the technical review.", link="All buyer guides", href="/blog/")}{_journal_rows(g, related)}</div></section>'
    content += _brief(g, product["name"])
    path = f'/blog/{post["slug"]}/'
    schema = [
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": post["title"], "description": post["meta_description"], "mainEntityOfPage": g["BASE_URL"] + path, "url": g["BASE_URL"] + path, "image": g["BASE_URL"] + image, **dates, "author": {"@type": "Organization", "name": g["CONTACT"]["company"]}, "publisher": {"@type": "Organization", "name": g["CONTACT"]["company"], "logo": {"@type": "ImageObject", "url": g["BASE_URL"] + "/assets/jade-waves-logo-transparent.png"}}},
        _breadcrumbs(g, [("Blog", "/blog/"), (post["title"], path)]),
    ]
    return _shell(g, post["seo_title"], post["meta_description"], path, content, schema, "page-blog-post")
