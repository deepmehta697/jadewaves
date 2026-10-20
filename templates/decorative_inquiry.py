"""Compact decorative enquiries using the existing protected submission handler."""
from html import escape
from urllib.parse import urlencode


def navigation(g):
    return (g['nav_html']().replace('href="/#contact"', 'href="#contact"')
            .replace('data-set-request="TDS"', 'data-set-request="Sample"')
            .replace('Request a specification', 'Request a sample'))


def render(g, product, selection, email_attribute, extra=''):
    contact = g['CONTACT']
    key = g['RECAPTCHA_SITE_KEY']
    email = 'mailto:' + contact['sales_email'] + '?' + urlencode({'subject': product + ' enquiry', 'body': selection})
    security = (f'<div class="g-recaptcha" data-sitekey="{escape(key, quote=True)}"></div><p class="form-security__hint">Protected by Google reCAPTCHA.</p>' if key else
                '<p>Online enquiry is unavailable. Please email the export desk.</p>')
    return f'''<section class="decorative-enquiry ml-section" id="contact" aria-labelledby="decorative-enquiry-title">
      <div class="ml-container decorative-enquiry-layout">
        <div class="decorative-enquiry-intro">
          <p class="ml-eyebrow">Your selection, taken further</p>
          <h2 id="decorative-enquiry-title" tabindex="-1">Request a sample.</h2>
          <p>Share your application and destination. We’ll confirm the selection, sample and packing with you.</p>
          {extra}
          <div class="decorative-enquiry-selection"><span>Selected material</span><p>{escape(product)}</p><p data-decorative-selection>{escape(selection)}</p></div>
          <div class="contact-details decorative-enquiry-fallback">
            <a href="{escape(email, quote=True)}" {email_attribute}>Prefer email? Discuss this selection ↗</a>
            <a href="tel:{escape(contact['phone'])}">{escape(contact['phone'])}</a>
          </div>
        </div>
        <form class="inquiry-form decorative-inquiry-form" method="post" data-inquiry-form data-decorative-form
          data-inquiry-endpoint="{escape(g['INQUIRY_ENDPOINT'], quote=True)}" data-recaptcha-configured="{str(bool(key)).lower()}">
          <input type="hidden" name="company_website" value="" autocomplete="off" tabindex="-1">
          <input type="hidden" name="product" value="{escape(product, quote=True)}">
          <input type="hidden" name="packing_size" value="">
          <input type="hidden" name="notes" value="{escape(selection, quote=True)}">
          <div class="form-grid">
            <label><span>Your name *</span><input name="name" autocomplete="name" maxlength="120" required></label>
            <label><span>Email *</span><input type="email" name="email" autocomplete="email" maxlength="160" required></label>
            <label><span>Request</span><select name="request_type"><option value="Sample">Sample</option><option value="Quote">Quote</option><option value="General Inquiry">General enquiry</option></select></label>
            <label><span>Company <small>(optional)</small></span><input name="company" autocomplete="organization" maxlength="160"></label>
            <label><span>Destination</span><input name="destination" placeholder="Country or discharge port" maxlength="160"></label>
            <label><span>Quantity</span><input name="volume" placeholder="Trial or order quantity" maxlength="120"></label>
            <label class="form-grid__wide"><span>Application / binder system</span><input name="application" placeholder="Your intended use" maxlength="160"></label>
            <label class="form-grid__wide"><span>Anything else? <small>(optional)</small></span><textarea rows="3" maxlength="3000" data-decorative-message placeholder="Target shade, packing or sample requirements"></textarea></label>
          </div>
          <div class="form-security">{security}</div>
          <div class="form-actions"><button class="button button--dark" type="submit" disabled>Send enquiry ↗</button>
            <p class="form-note" data-form-note role="status" aria-live="polite" aria-atomic="true">We’ll review your enquiry and respond by email.</p></div>
          <noscript><p>Please enable JavaScript to submit online, or email <a href="mailto:{escape(contact['sales_email'])}">{escape(contact['sales_email'])}</a>.</p></noscript>
        </form>
      </div>
    </section>'''


def add_assets(g, html):
    return html.replace('</head>',
        f'<link rel="stylesheet" href="assets/decorative-products/enquiry.css?v={g["BUILD_VERSION"]}">'
        f'<script defer src="assets/decorative-products/enquiry.js?v={g["BUILD_VERSION"]}"></script></head>')
