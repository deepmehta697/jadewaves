# Inquiry analytics

The shared `templates/material-ledger.js` source emits GA4's `generate_lead` event only when the inquiry endpoint returns both a successful HTTP status and JSON with `success: true` (the boolean). The existing submit-button guard prevents concurrent duplicate submissions. Failed, invalid, unconfirmed, and honeypot submissions never emit a lead, including the endpoint's intentional success acknowledgement for honeypot spam. A recorded inquiry with a delayed notification email is still a confirmed lead.

Tracking is optional: it uses an existing `window.gtag` function and does not install or configure GA4. If that function is absent or throws, the confirmed inquiry still resets normally and displays its success message. An ad blocker or consent restriction may therefore prevent analytics delivery without affecting the inquiry.

Event parameters are `request_type` (Quote, Sample, TDS, or General Inquiry) and `product` (a fixed catalogue label, or Unspecified). Unknown request values map to General Inquiry. No form names, email addresses, phone numbers, company names, application/destination/packing/volume/notes fields, captcha tokens, or response messages are passed to analytics. `page_location` contains only the page origin and path; `page_referrer` is empty and `page_title` is a fixed label to avoid inherited query strings, fragments, or arbitrary titles on this event. Separate GA4 page-view configuration and automatic events require their own privacy review; these event overrides apply to `generate_lead` only.

After regeneration, the source is emitted into the site's shared script. In GA4, designate `generate_lead` as a key event and register `request_type` and `product` as event-scoped custom dimensions if they should appear in reports. Measurement IDs and consent configuration belong in the site's existing analytics setup.

Offline verification (no browser, network calls, or live inquiry):

```sh
/Users/deepmehta/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node --test scripts/tests/inquiry_analytics.test.cjs
```

The Node tests execute the complete shared script with a mocked DOM, FormData, fetch, and analytics function. They cover confirmation semantics, bounded parameters, URL privacy, validation/captcha gates, failed or ambiguous responses, honeypot acknowledgements, absent/throwing analytics, concurrent duplicate submissions, and successful retry after failure.
