# Google Apps Script Inquiry Mailer

This small Apps Script web app sends Jade Waves website inquiries to `deep@jadewavesenterprise.com` through the existing Google Workspace mailbox.

## What it does

- receives sanitized inquiry JSON from the Cloudflare form backend
- sends an email notification from the Google account that deploys the script
- uses the buyer email as `replyTo`

## Local files

- `Code.gs` - the mailer logic
- `appsscript.json` - Apps Script manifest
- `.claspignore` - keeps non-script files out of the Google project

## Setup flow

1. Sign in with `clasp`
2. Create a standalone Apps Script project from this folder
3. Push the files
4. Open the project in Apps Script
5. Deploy as a Web App:
   - Execute as: `Me`
   - Who has access: `Anyone`
6. Copy the Web App URL
7. Save that URL into the Cloudflare Pages secret:
   - `GOOGLE_APPS_SCRIPT_WEBHOOK_URL`

## Notes

- This avoids DNS changes and uses the existing Google Workspace mailbox.
- The Cloudflare backend still handles reCAPTCHA, sanitization, and lead storage.
- If email delivery is slow or fails, the inquiry is still stored in D1.
