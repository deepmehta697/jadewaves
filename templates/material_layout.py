"""Shared Material Ledger navigation, contact brief, and footer."""

from html import escape
from textwrap import dedent


def _get(g, key, default=None):
    return g.get(key, default) if isinstance(g, dict) else getattr(g, key, default)


def render_nav(g) -> str:
    company = escape(_get(g, "CONTACT")["company"])
    links = """
        <a href="/products/">Materials</a>
        <a href="/#process">Export process</a>
        <a href="/hear-from-ceo/">Our company</a>
        <a href="/#contact">Contact</a>
    """
    return dedent(f"""
        <a class="skip-link" href="#main-content">Skip to content</a>
        <header class="site-header" data-header>
          <div class="site-header__inner shell">
            <a class="brand-mark" href="/" aria-label="{company} home">
              <img src="/assets/jade-waves-logo-transparent.png" alt="" width="612" height="408" />
              <span class="brand-lockup"><strong>Jade Waves</strong><em>Industrial Mineral Export</em></span>
            </a>
            <nav class="desktop-nav" aria-label="Primary">{links}</nav>
            <div class="header-actions">
              <a class="button button--dark button--compact" href="/#contact" data-set-request="TDS">Request a specification</a>
              <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open navigation" data-menu-toggle hidden>Menu</button>
            </div>
          </div>
          <div class="mobile-menu" id="mobile-menu" role="dialog" aria-modal="true" aria-labelledby="mobile-menu-title" tabindex="-1" data-mobile-menu hidden>
            <div class="mobile-menu__top">
              <p id="mobile-menu-title">Jade Waves</p>
              <button class="mobile-menu__close" type="button" data-menu-close aria-label="Close navigation">Close <span aria-hidden="true">×</span></button>
            </div>
            <nav class="mobile-menu__links" aria-label="Mobile primary">{links}<a href="/#contact" data-set-request="TDS">Request a specification →</a></nav>
            <p class="mobile-menu__note">Mineral supply from India.<br />Specification to shipment.</p>
          </div>
          <noscript><nav class="mobile-menu__fallback shell" aria-label="Primary">{links}</nav></noscript>
        </header>
    """).strip()


def render_footer(g) -> str:
    contact = _get(g, "CONTACT")
    return dedent(f"""
        <footer class="site-footer">
          <div class="shell site-footer__inner">
            <div class="site-footer__lead">
              <p class="footer-label">{escape(contact['company'])}</p>
              <p class="footer-copy">Mineral supply from India.<br />Specification to shipment.</p>
              <p class="footer-address">{escape(contact['address'])}</p>
            </div>
            <div class="footer-grid">
              <div>
                <p class="footer-heading">Export desk</p>
                <a href="mailto:{escape(contact['sales_email'])}">{escape(contact['sales_email'])}</a>
                <a href="tel:{escape(contact['phone'])}">{escape(contact['phone'])}</a>
                <p>{escape(contact['port'])} · Gujarat, India</p>
              </div>
              <nav aria-label="Footer">
                <p class="footer-heading">Explore</p>
                <a href="/products/">Material portfolio</a>
                <a href="/#process">Export process</a>
                <a href="/export-markets/">Export markets</a>
                <a href="/operations/">Operations</a>
                <a href="/hear-from-ceo/">Hear from our CEO</a>
                <a href="/blog/">Buyer notes</a>
              </nav>
            </div>
          </div>
          <div class="shell site-footer__meta">
            <p>© <span data-current-year>2026</span> {escape(contact['company'])}</p>
            <nav class="footer-legal" aria-label="Legal"><a href="/privacy-policy/">Privacy policy</a><a href="/terms-disclaimer/">Terms &amp; disclaimer</a></nav>
            <a href="/#contact" data-set-request="Quote">Talk to the export desk ↗</a>
          </div>
        </footer>
    """).strip()


def render_form(g, product_name: str = "") -> str:
    contact = _get(g, "CONTACT")
    site_key = _get(g, "RECAPTCHA_SITE_KEY", "")
    endpoint = escape(_get(g, "INQUIRY_ENDPOINT", "/api/inquiry"))
    if product_name:
        product_field = f'<input type="text" name="product" value="{escape(product_name)}" maxlength="120" readonly />'
    else:
        options = ['<option value="">Select a material</option>']
        for product in _get(g, "PRODUCTS", []):
            name = escape(product["name"])
            options.append(f'<option value="{name}">{name}</option>')
        product_field = '<select name="product">' + "".join(options) + '</select>'
    security = (
        f'<div class="form-security"><div class="g-recaptcha" data-sitekey="{escape(site_key)}"></div><p class="form-security__hint">Protected by Google reCAPTCHA.</p></div>'
        if site_key else
        '<div class="form-security form-security--warning"><p>Online inquiry is currently unavailable. Please contact the export desk directly.</p></div>'
    )
    return dedent(f"""
        <div class="contact-shell" id="contact">
          <div class="contact-copy" data-reveal>
            <p class="section-label">Export desk</p>
            <h2>Start with your<br />material requirement.</h2>
            <p>Share your application and destination. We’ll align the grade, documents and packing before dispatch.</p>
            <div class="contact-person">
              <p><strong>Deep Mehta</strong><br />CEO, Jade Waves Enterprise</p>
              <a class="text-link" href="/hear-from-ceo/">A note from our CEO ↗</a>
            </div>
            <div class="contact-details">
              <a href="mailto:{escape(contact['sales_email'])}">{escape(contact['sales_email'])}</a>
              <a href="tel:{escape(contact['phone'])}">{escape(contact['phone'])}</a>
              <p>{escape(contact['port'])} · Gujarat, India</p>
            </div>
            <p class="contact-footnote">COA &amp; TDS · 50 kg / jumbo bags · FCL handling</p>
          </div>
          <form class="inquiry-form" method="post" data-inquiry-form data-reveal data-inquiry-endpoint="{endpoint}" data-recaptcha-configured="{str(bool(site_key)).lower()}">
            <input type="hidden" name="company_website" value="" autocomplete="off" tabindex="-1" />
            <div class="form-grid">
              <label><span>Material</span>{product_field}</label>
              <label><span>Request</span><select name="request_type"><option value="Quote">Quote</option><option value="Sample">Sample</option><option value="TDS">Technical data sheet</option><option value="General Inquiry">General inquiry</option></select></label>
              <label><span>Application</span><input type="text" name="application" placeholder="End use or industry" maxlength="160" /></label>
              <label><span>Country / destination port</span><input type="text" name="destination" placeholder="Country or discharge port" maxlength="160" /></label>
              <label><span>Volume</span><input type="text" name="volume" placeholder="Trial or monthly tonnage" maxlength="120" /></label>
              <label><span>Preferred packing</span><input type="text" name="packing_size" placeholder="50 kg / jumbo bags / custom" maxlength="120" /></label>
              <label class="form-grid__wide"><span>Target specification / requirement</span><textarea name="notes" rows="3" placeholder="Chemistry, grain size or other specification points" maxlength="4000"></textarea></label>
              <label><span>Your name <span class="form-required" aria-hidden="true">*</span></span><input type="text" name="name" autocomplete="name" placeholder="Full name" maxlength="120" required /></label>
              <label><span>Company</span><input type="text" name="company" autocomplete="organization" placeholder="Company name" maxlength="160" /></label>
              <label><span>Email <span class="form-required" aria-hidden="true">*</span></span><input type="email" name="email" autocomplete="email" placeholder="you@company.com" maxlength="160" required /></label>
              <label><span>Phone / WhatsApp</span><input type="tel" name="phone" autocomplete="tel" placeholder="Country code and number" maxlength="80" /></label>
            </div>
            {security}
            <div class="form-actions">
              <button class="button button--dark" type="submit" disabled>Send requirement ↗</button>
              <p class="form-note" data-form-note role="status" aria-live="polite" aria-atomic="true">We’ll review your requirement and respond by email.</p>
            </div>
            <noscript><p class="form-note">Please send your requirement directly to <a href="mailto:{escape(contact['sales_email'])}">{escape(contact['sales_email'])}</a> or <a href="tel:{escape(contact['phone'])}">{escape(contact['phone'])}</a>.</p></noscript>
          </form>
        </div>
    """).strip()
