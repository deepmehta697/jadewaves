"""Operations and policy pages in the shared Material Ledger system."""

from html import escape


def _schema(g, name, path):
    url = g['BASE_URL'] + path
    return [
        {'@context': 'https://schema.org', '@type': 'WebPage', 'name': name, 'url': url},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': g['BASE_URL']},
            {'@type': 'ListItem', 'position': 2, 'name': name, 'item': url},
        ]},
    ]


def render_operations_page(g):
    images = [
        ('/assets/optimized/quarry-quartz.jpg', 'Quartz quarry before sorting and processing.'),
        ('/assets/optimized/manual-sorting.jpg', 'Manual sorting before the sizing stage.'),
        ('/assets/optimized/processing-area.jpg', 'Material processing at the plant.'),
        ('/assets/optimized/packing-area.jpg', 'Bagging and packing area.'),
        ('/assets/optimized/jumbo-bags-1.jpg', 'Jumbo bags prepared for dispatch.'),
        ('/assets/optimized/loading-trucks.jpg', 'Truck loading before movement to port.'),
        ('/assets/container-1604.jpeg', 'Bagged cargo inside a loaded container.'),
        ('/assets/quality-control.png', 'Quality control before dispatch planning.'),
    ]
    gallery = ''.join(f'<figure data-reveal><img src="{src}" alt="{escape(caption)}" loading="lazy" /><figcaption>{i:02d} / {escape(caption)}</figcaption></figure>' for i, (src, caption) in enumerate(images, 1))
    videos = ''.join(f'<figure><video controls playsinline preload="none" poster="/assets/{poster}"><source src="/assets/{video}" type="video/mp4" />Your browser does not support video playback.</video><figcaption>{escape(caption)}</figcaption></figure>' for video, poster, caption in [
        ('jcb.mp4', 'jcb-poster.jpg', 'Loading activity during cargo preparation.'),
        ('loading.mp4', 'loading-poster.jpg', 'Bag loading in the dispatch yard.'),
        ('process-loading.mp4', 'process-loading-poster.png', 'Container movement during dispatch coordination.'),
    ])
    body = f'''{g['nav_html']()}<main>
      <section class="ml-page-intro shell"><p class="section-label">Operations / India</p><h1>From material<br />to loaded container.</h1><p>Sorting, processing, packing, and dispatch. A view of the work behind the shipment.</p><a class="ml-text-link" href="#operations-gallery">View the operation <span aria-hidden="true">↓</span></a></section>
      <section class="ml-section ml-section--chalk"><div class="shell"><div class="ml-section-head"><p class="section-label">At the plant</p><h2>Material handling, in sequence.</h2></div><div class="ml-evidence-grid" id="operations-gallery">{gallery}</div></div></section>
      <section class="ml-section"><div class="shell"><div class="ml-section-head"><p class="section-label">Dispatch footage</p><h2>Inside the loading yard.</h2><p>Play each clip to see cargo preparation and movement.</p></div><div class="ml-evidence-grid ml-evidence-grid--videos">{videos}</div></div></section>
      <section class="ml-section ml-section--chalk"><div class="shell"><div class="ml-section-head"><p class="section-label">Before loading</p><h2>Confirm the shipment basis.</h2></div><dl class="ml-spec-table"><div><dt>Packing</dt><dd>50 kg bags / jumbo bags, aligned to the material</dd></div><div><dt>Port access</dt><dd>Near Mundra Port</dd></div><div><dt>Shipment</dt><dd>FCL cargo planning</dd></div><div><dt>Terms</dt><dd>FOB / CIF / CNF, subject to quotation and order confirmation</dd></div><div><dt>Documents</dt><dd>Aligned to product, destination, and order basis</dd></div></dl></div></section>
      <section class="ml-section ml-brief"><div class="shell">{g['form_block']()}</div></section>
    </main>{g['footer_html']()}'''
    return g['page_shell']('Operations | Jade Waves Enterprise | Mineral Manufacturing, Packing & Dispatch', 'See how Jade Waves Enterprise handles mineral manufacturing, packing, yard movement, container loading, and dispatch planning from India for bulk buyers.', '/operations/', body, _schema(g, 'Operations', '/operations/'), 'page-operations')


POLICIES = {
    'privacy-policy': {
        'name': 'Privacy Policy',
        'title': 'How enquiry information is handled.',
        'description': 'Privacy policy for Jade Waves Enterprise covering website enquiries, email contact, and commercial information handling.',
        'intro': 'If you contact Jade Waves through the website, email, phone, or WhatsApp, this page explains what information may be used and why.',
        'sections': [
            ('Commercial information shared through enquiries.', [
                ('Contact details', 'Name, company, email, phone number, and any details you share while making an enquiry.'),
                ('Requirement details', 'Product, application, packing size, destination, volume, and technical points such as chemistry, sizing, or document needs.'),
                ('Commercial follow-up', 'Messages shared through email, phone, or WhatsApp once the enquiry moves into sampling, quotation, or shipment planning.'),
            ]),
            ('How the website form works today.', [
                ('Website submission', 'The current website form sends enquiry details directly to Jade Waves for commercial follow-up.'),
                ('When data reaches Jade Waves', 'As soon as the website form is submitted or the buyer contacts Jade Waves directly.'),
                ('Use', 'Quote, sample, shipment planning, and document follow-up.'),
            ]),
            ('Only for enquiry, quotation, and supply handling.', [
                ('Product fit and quotation', 'To understand the requirement, share the right product direction, and prepare pricing or sample discussion.'),
                ('Packing and dispatch planning', 'To align bagging, destination, documents, and shipment basis to the enquiry.'),
                ('Commercial follow-up', 'To answer questions, share updates, and manage repeat order communication where relevant.'),
            ]),
            ('Basic privacy position.', [
                ('Sale of personal data', 'Not sold.'),
                ('Sharing', 'Only where needed for internal handling or commercial processing.'),
                ('Retention', 'Kept only as needed for enquiry and business records.'),
            ]),
        ],
        'contact': 'If you need a correction or want information removed from a commercial enquiry thread, contact Jade Waves directly.',
    },
    'terms-disclaimer': {
        'name': 'Terms & Disclaimer',
        'title': 'The basis for a supply discussion.',
        'description': 'Terms and disclaimer for Jade Waves Enterprise covering website use, indicative mineral specifications, packing, and shipment confirmation.',
        'intro': 'Use this website as a commercial reference. Confirm the current product, specification, and shipment basis directly before placing an order.',
        'sections': [
            ('Commercial reference, not automatic commitment.', [
                ('Reference purpose', 'This website is intended to explain products, applications, operations, and enquiry paths for Jade Waves Enterprise.'),
                ('No automatic acceptance', 'A page view, enquiry, or sample request does not create a binding supply commitment on its own.'),
                ('Commercial confirmation', 'Final supply terms should be based on direct communication, current quotation, sample approval where relevant, and confirmed order documents.'),
            ]),
            ('What should always be reconfirmed.', [
                ('Product grade', 'Confirm before order.'),
                ('Packing size', 'Confirm before loading.'),
                ('Shipment basis', 'Confirm in quotation and order documents.'),
            ]),
            ('Website specifications are indicative until aligned to the order.', [
                ('Application matters', 'Mesh, chemistry, brightness, color, Fe2O3, moisture, and other technical points depend on the actual use case and should be confirmed for that requirement.'),
                ('Lot-to-lot confirmation', 'Current lot data, sample approval, and final commercial confirmation matter more than any general website statement.'),
                ('Document reference', 'Any sample COA, TDS, or document shared for reference should be treated as indicative unless confirmed against the current lot or shipment.'),
            ]),
            ('Packing and dispatch depend on the confirmed job.', [
                ('Packing', 'Subject to product, route, and buyer requirement.'),
                ('Documents', 'Aligned to destination and order basis.'),
                ('Lead time', 'Depends on product readiness, packing, and shipment plan.'),
                ('Commercial terms', 'FOB / CIF / CNF or other terms only when confirmed.'),
            ]),
        ],
        'contact': 'If the requirement is active, ask directly for the current grade, packing, and shipment basis rather than rely on a general website line.',
    },
}


def render_policy_page(g, slug):
    policy = POLICIES[slug]
    sections = ''.join(f'<section><h2>{escape(heading)}</h2>{"".join(f"<h3>{escape(label)}</h3><p>{escape(copy)}</p>" for label, copy in paragraphs)}</section>' for heading, paragraphs in policy['sections'])
    body = f'''{g['nav_html']()}<main><section class="ml-page-intro shell"><p class="section-label">{escape(policy['name'])}</p><h1>{escape(policy['title'])}</h1><p>{escape(policy['intro'])}</p></section><div class="shell ml-reading">{sections}<section><h2>Contact</h2><p>{escape(policy['contact'])}</p><a href="mailto:{escape(g['CONTACT']['sales_email'])}">{escape(g['CONTACT']['sales_email'])}</a></section></div></main>{g['footer_html']()}'''
    return g['page_shell'](policy['name'] + ' | Jade Waves Enterprise', policy['description'], '/' + slug + '/', body, _schema(g, policy['name'], '/' + slug + '/'), 'page-policy')
