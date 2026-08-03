# Jade Waves CRM on Cloudflare

Private CRM deployment for `crm.jadewavesenterprise.com`.

## What this version does

- hosts the CRM on Cloudflare Pages
- stores CRM data in Cloudflare D1 instead of on your Mac
- protects the entire app behind a username and password
- keeps Gmail access read-only in the browser so it can detect who has replied and which follow-ups are pending
- leaves the public website on `jadewavesenterprise.com` untouched

## Folder layout

- `public/` static CRM files
- `functions/` Cloudflare Pages Functions for auth and state APIs
- `migrations/` D1 schema
- `wrangler.toml` Cloudflare config

## Zero-cost path

This setup is intended for the Cloudflare free tier:

- Pages Free for hosting
- Workers/Pages Functions Free for light API usage
- D1 Free for CRM storage within free limits

## Public inquiry API

This Cloudflare Pages project can also host the public inquiry endpoint for the main website:

- `POST /api/inquiry`
- verifies Google reCAPTCHA server-side
- strips HTML from incoming text fields
- forwards the inquiry to `deep@jadewavesenterprise.com`
- allows browser requests from `jadewavesenterprise.com` and local preview origins

That means the main site can stay static while the form submission is handled securely on Cloudflare.

## Deployment path

This repo can be deployed without keeping anything running on your Mac.

### 1. Push this repo to GitHub

Use the existing repository, or a dedicated branch if you want a clean rollout.

### 2. Create a Cloudflare Pages project

In Cloudflare:

1. Go to `Workers & Pages`
2. Create a new `Pages` project
3. Connect the GitHub repository
4. Set the project root directory to `crm-cloudflare`
5. Leave the build command empty
6. Set build output directory to `public`

### 3. Create a D1 database

Create a D1 database named `jadewaves-crm`.

Bind it to the Pages project as:

- binding name: `DB`

The app also auto-creates its `app_state` table on first use, so there is no fragile first-run step.

### 4. Add environment variables

In the Pages project settings, set:

- `CRM_USERNAME`
- `CRM_PASSWORD`
- `CRM_SESSION_SECRET`
- `RECAPTCHA_SECRET_KEY`

Use a long random value for `CRM_SESSION_SECRET`.

Optional variables:

- `INQUIRY_FORWARD_EMAIL` if you want a different destination than `deep@jadewavesenterprise.com`
- `INQUIRY_ALLOWED_ORIGINS` as a comma-separated list if you want to override the default allowed website origins
- `GOOGLE_APPS_SCRIPT_WEBHOOK_URL` if you want inquiries to send through Google Workspace
- `FORMSUBMIT_ENDPOINT` if you want to use a specific FormSubmit endpoint

### Google Workspace delivery path

Because `jadewavesenterprise.com` currently uses GoDaddy DNS and Google Workspace mail, the simplest reliable sender is a Google Apps Script Web App running under the existing mailbox.

The starter files live here:

- `../integrations/google-apps-script/inquiry-mailer/`

After you deploy that Apps Script Web App, save its URL into the Pages secret:

```bash
echo "https://script.google.com/macros/s/your-web-app-id/exec" | npx wrangler pages secret put GOOGLE_APPS_SCRIPT_WEBHOOK_URL --project-name jadewaves-crm
```

### 5. Attach the custom subdomain

Target:

- `crm.jadewavesenterprise.com`

Because your main site is currently on GitHub Pages, this subdomain setup will not disturb the live site.

Cloudflare Pages docs say a custom subdomain does not require moving the whole zone to Cloudflare, but you do need to:

1. add the custom domain inside the Pages dashboard first
2. then add a `CNAME` at your current DNS provider pointing `crm` to your Cloudflare `*.pages.dev` hostname

## Wire the public site to the API

When you build the public website for production, point the form to the Cloudflare endpoint:

```bash
INQUIRY_ENDPOINT=https://crm.jadewavesenterprise.com/api/inquiry python3 generate_site.py
python3 scripts/build_site.py
```

Keep `RECAPTCHA_SITE_KEY` in the public site's `.env.local`. Keep `RECAPTCHA_SECRET_KEY` only in the Cloudflare Pages environment variables.

### 6. Sign in and use the CRM

After login:

- add company records
- connect Gmail with a Google OAuth client ID
- scan reply status
- let the CRM tell you which follow-ups are pending

For the Google OAuth client, add authorized JavaScript origins for:

- `https://crm.jadewavesenterprise.com`
- your Cloudflare `https://<project>.pages.dev` URL during testing

## Privacy model

- the app is internet-accessible only behind login
- the data lives in Cloudflare D1, not on your Mac
- Gmail scanning is read-only
- your `pages.dev` URL may still exist, but it will also require login
