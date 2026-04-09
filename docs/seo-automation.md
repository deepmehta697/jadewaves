# SEO Automation Setup

This repo is a static site with checked-in HTML, CSS, JS, and a Python generator. The daily SEO operator workflow added here is built around that stack instead of assuming a Node app.

## What was added

- `config/seo.config.json`
  - Site-specific SEO automation config for this repo.
  - Safe to commit with shared property and reporting defaults.
- `config/seo.config.local.json`
  - Optional local-only override file for machine-specific secrets such as the Google service account key path.
  - This file is gitignored and loaded automatically when present.
- `scripts/seo/daily_runner.py`
  - Reuses `reports/seo/YYYY-MM-DD.md` when it already exists.
  - Otherwise generates a new report and refreshes `reports/seo/latest.md`.
- `scripts/seo/generate_report.py`
  - Audits the repo output, checks live site availability, and attempts Google Search Console and GA4 fetches when configured.
  - Stops cleanly with exact blockers and setup instructions when Google access is missing.
- `scripts/build_site.py`
  - Builds the production `_site/` artifact in the same shape as the GitHub Pages workflow.
- `package.json`
  - Provides stable `npm` script names for the automation even though the site itself is Python-first.

## Report path

- Daily report: `reports/seo/YYYY-MM-DD.md`
- Latest report copy: `reports/seo/latest.md`

## Commands

- `npm run seo:report`
  - Reuse today's report if it exists, otherwise generate it.
- `npm run seo:report:force`
  - Force-regenerate today's report.
- `npm run build`
  - Assemble the production `_site/` output from the checked-in static site.
- `npm run build:regen`
  - Regenerate site files with `generate_site.py` first, then assemble `_site/`.

## Values you still need to provide locally

Put these in `config/seo.config.local.json` or via environment variables from `.env.example`.

- `SEO_SEARCH_CONSOLE_PROPERTY`
  - For this site, `https://jadewavesenterprise.com/` is working now.
  - A domain property such as `sc-domain:jadewavesenterprise.com` is still preferred long term.
- `SEO_GA4_PROPERTY_ID`
  - This must be the numeric GA4 Property ID, not the `G-...` measurement ID.
- `SEO_GOOGLE_SERVICE_ACCOUNT_KEY_PATH`
  - Absolute path to the service account JSON key file on disk.
  - Best kept only in `config/seo.config.local.json`, not in the committed config.
- `SEO_GA4_MEASUREMENT_ID`
  - Optional for frontend tagging.
  - Leave blank if tagging has not been installed yet.

## How to get each Google value

### 1. Search Console property value

1. Open Google Search Console.
2. Add a new `Domain` property for `jadewavesenterprise.com`.
3. Verify the DNS TXT record in your DNS provider.
4. After verification, use this value in config:
   - `sc-domain:jadewavesenterprise.com`

### 2. GA4 property ID

1. Open Google Analytics.
2. Go to `Admin`.
3. Under the correct property, open `Property details`.
4. Copy the numeric `Property ID`.
5. Put that number into `SEO_GA4_PROPERTY_ID`.

### 3. Service account JSON key

1. Open Google Cloud Console.
2. Create or choose the project you want to use for SEO automation.
3. Enable these APIs:
   - `Search Console API`
   - `Google Analytics Data API`
4. Go to `IAM & Admin > Service Accounts`.
5. Create a service account for this automation.
6. Open that service account and create a new JSON key.
7. Download the JSON file and store it outside the repo.
8. Set `SEO_GOOGLE_SERVICE_ACCOUNT_KEY_PATH` to the absolute path of that file.

### 4. Required access levels

- Search Console:
  - Add the service account email from the JSON file as a `Full user` on the Search Console property.
  - `Owner` is recommended if you want broader property administration later.
- GA4:
  - Add the same service account email at the property level with `Viewer` or `Analyst` access.

## Current analytics state in this repo

- GA4 tagging is now installed in the shared page shell.
- Lead-form events are emitted on successful inquiry submission.
- The report currently verifies GA4 configuration and Search Console access from the local machine.

## How the daily operator should use this

1. Run `npm run seo:report`.
2. Read `reports/seo/latest.md`.
3. If the report contains only setup blockers, stop and use the checklist in the report.
4. If the report identifies safe shared-template fixes, apply them in shared sources first.
5. Run a production build.
6. If relevant website code changed and the build passed, commit and push.
7. Open a GitHub issue summary using the report plus the issue template below.

## GitHub issue summary template

Use the issue template at `.github/ISSUE_TEMPLATE/seo-operator-report.md` for daily summary issues.
