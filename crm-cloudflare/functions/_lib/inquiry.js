const RECAPTCHA_VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify";
const DEFAULT_INQUIRY_EMAIL = "deep@jadewavesenterprise.com";
const REQUEST_TYPE_ALLOWLIST = new Set(["Quote", "Sample", "TDS", "General Inquiry"]);
const DEFAULT_ALLOWED_ORIGINS = [
  "https://jadewavesenterprise.com",
  "https://www.jadewavesenterprise.com",
  "http://127.0.0.1:4173",
  "http://127.0.0.1:4174",
  "http://127.0.0.1:4175",
  "http://localhost:4173",
  "http://localhost:4174",
  "http://localhost:4175",
];

const MAX_FIELD_LENGTHS = {
  request_type: 40,
  product: 120,
  name: 120,
  company: 160,
  email: 160,
  phone: 80,
  application: 160,
  volume: 120,
  destination: 160,
  packing_size: 120,
  notes: 4000,
  source_page: 320,
  page_title: 160,
};

const EMAIL_PATTERN = /^[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}$/i;

function stripHtml(value) {
  return String(value ?? "")
    .replace(/<[^>]*>/g, " ")
    .replace(/&nbsp;/gi, " ")
    .replace(/&amp;/gi, "&")
    .replace(/&lt;/gi, "<")
    .replace(/&gt;/gi, ">")
    .replace(/&quot;/gi, '"')
    .replace(/&#39;/gi, "'")
    .replace(/[\u0000-\u001F\u007F]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function sanitizeField(name, value) {
  const text = stripHtml(value);
  const maxLength = MAX_FIELD_LENGTHS[name] || 500;
  return text.slice(0, maxLength).trim();
}

export function sanitizeInquiryPayload(payload = {}) {
  const cleaned = Object.fromEntries(
    Object.keys(MAX_FIELD_LENGTHS).map((field) => [field, sanitizeField(field, payload[field] ?? "")])
  );

  cleaned.request_type = REQUEST_TYPE_ALLOWLIST.has(cleaned.request_type) ? cleaned.request_type : "General Inquiry";
  cleaned.email = cleaned.email.toLowerCase();
  return cleaned;
}

export function verifyInquiryPayload(payload) {
  if (!payload.name) {
    return [false, "Name is required."];
  }

  if (!payload.email || !EMAIL_PATTERN.test(payload.email)) {
    return [false, "A valid email address is required."];
  }

  return [true, ""];
}

function allowedOrigins(env) {
  const configured = String(env.INQUIRY_ALLOWED_ORIGINS || "")
    .split(",")
    .map((value) => value.trim())
    .filter(Boolean);

  return new Set(configured.length ? configured : DEFAULT_ALLOWED_ORIGINS);
}

export function resolveAllowedOrigin(request, env) {
  const origin = String(request.headers.get("Origin") || "").trim();
  if (!origin) {
    return "";
  }

  return allowedOrigins(env).has(origin) ? origin : null;
}

export function corsHeaders(origin = "") {
  const headers = {
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    Vary: "Origin",
  };

  if (origin) {
    headers["Access-Control-Allow-Origin"] = origin;
  }

  return headers;
}

export function inquiryJsonResponse(payload, status = 200, origin = "") {
  return new Response(JSON.stringify(payload), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
      "X-Content-Type-Options": "nosniff",
      "Referrer-Policy": "strict-origin-when-cross-origin",
      ...corsHeaders(origin),
    },
  });
}

function remoteIpFromRequest(request) {
  const cfIp = String(request.headers.get("CF-Connecting-IP") || "").trim();
  if (cfIp) {
    return cfIp;
  }

  const forwarded = String(request.headers.get("X-Forwarded-For") || "").trim();
  return forwarded.split(",")[0]?.trim() || "";
}

export async function verifyRecaptcha(token, request, env) {
  const secret = String(env.RECAPTCHA_SECRET_KEY || "").trim();
  if (!secret) {
    return [false, "reCAPTCHA secret key is not configured on the server."];
  }

  if (!token) {
    return [false, "Please complete the Google reCAPTCHA challenge."];
  }

  const body = new URLSearchParams({
    secret,
    response: String(token),
  });

  const remoteIp = remoteIpFromRequest(request);
  if (remoteIp) {
    body.set("remoteip", remoteIp);
  }

  let result = {};
  try {
    const response = await fetch(RECAPTCHA_VERIFY_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: body.toString(),
    });

    result = await response.json();
  } catch (error) {
    return [false, "Google reCAPTCHA verification could not be completed."];
  }

  if (result?.success === true) {
    return [true, ""];
  }

  return [false, "Google reCAPTCHA verification failed."];
}

function inquiryDestination(env) {
  return String(env.INQUIRY_FORWARD_EMAIL || DEFAULT_INQUIRY_EMAIL).trim();
}

function googleAppsScriptWebhookUrl(env) {
  return String(env.GOOGLE_APPS_SCRIPT_WEBHOOK_URL || "").trim();
}

function inquiryDb(env) {
  return env?.DB || null;
}

async function ensureInquiryTable(db) {
  await db.exec(
    "CREATE TABLE IF NOT EXISTS inquiries (" +
      "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
      "created_at TEXT NOT NULL, " +
      "updated_at TEXT NOT NULL, " +
      "request_type TEXT NOT NULL, " +
      "product TEXT NOT NULL DEFAULT '', " +
      "name TEXT NOT NULL, " +
      "company TEXT NOT NULL DEFAULT '', " +
      "email TEXT NOT NULL, " +
      "phone TEXT NOT NULL DEFAULT '', " +
      "application TEXT NOT NULL DEFAULT '', " +
      "volume TEXT NOT NULL DEFAULT '', " +
      "destination TEXT NOT NULL DEFAULT '', " +
      "packing_size TEXT NOT NULL DEFAULT '', " +
      "notes TEXT NOT NULL DEFAULT '', " +
      "source_page TEXT NOT NULL DEFAULT '', " +
      "page_title TEXT NOT NULL DEFAULT '', " +
      "email_status TEXT NOT NULL DEFAULT 'pending', " +
      "email_error TEXT NOT NULL DEFAULT ''" +
      ");"
  );
}

function nowIso() {
  return new Date().toISOString();
}

export async function storeInquiry(payload, env) {
  const db = inquiryDb(env);
  if (!db) {
    return [false, 0, "Inquiry storage is not configured."];
  }

  try {
    await ensureInquiryTable(db);
    const timestamp = nowIso();
    const result = await db
      .prepare(
        "INSERT INTO inquiries (" +
          "created_at, updated_at, request_type, product, name, company, email, phone, application, volume, destination, packing_size, notes, source_page, page_title, email_status, email_error" +
          ") VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11, ?12, ?13, ?14, ?15, ?16, ?17)"
      )
      .bind(
        timestamp,
        timestamp,
        payload.request_type,
        payload.product,
        payload.name,
        payload.company,
        payload.email,
        payload.phone,
        payload.application,
        payload.volume,
        payload.destination,
        payload.packing_size,
        payload.notes,
        payload.source_page,
        payload.page_title,
        "pending",
        ""
      )
      .run();

    return [true, Number(result?.meta?.last_row_id || 0), ""];
  } catch (error) {
    console.error("Unable to store inquiry in D1", error);
    return [false, 0, "Unable to store inquiry."];
  }
}

export async function updateInquiryDeliveryStatus(inquiryId, status, errorMessage, env) {
  const db = inquiryDb(env);
  if (!db || !inquiryId) {
    return;
  }

  try {
    await db
      .prepare("UPDATE inquiries SET updated_at = ?1, email_status = ?2, email_error = ?3 WHERE id = ?4")
      .bind(nowIso(), String(status || "pending"), String(errorMessage || ""), Number(inquiryId))
      .run();
  } catch (error) {
    console.error("Unable to update inquiry delivery status", error);
  }
}

function relaySource(payload) {
  const fallbackOrigin = DEFAULT_ALLOWED_ORIGINS[0];
  const rawSourcePage = String(payload?.source_page || "").trim();

  try {
    const url = new URL(rawSourcePage);
    return {
      origin: url.origin,
      referer: url.href,
    };
  } catch (error) {
    return {
      origin: fallbackOrigin,
      referer: `${fallbackOrigin}/`,
    };
  }
}

function formSubmitEndpoint(env) {
  const configured = String(env.FORMSUBMIT_ENDPOINT || "").trim();
  if (configured) {
    return configured;
  }

  return `https://formsubmit.co/ajax/${inquiryDestination(env)}`;
}

function isRateLimitMessage(message) {
  return /rate limit/i.test(String(message || ""));
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function sendViaGoogleAppsScript(payload, env) {
  const webhookUrl = googleAppsScriptWebhookUrl(env);
  if (!webhookUrl) {
    return [false, "Google Apps Script webhook is not configured."];
  }

  const requestBody = {
    destinationEmail: inquiryDestination(env),
    requestType: payload.request_type,
    product: payload.product || "Not specified",
    name: payload.name,
    company: payload.company || "Not specified",
    email: payload.email,
    phone: payload.phone || "Not provided",
    application: payload.application || "Not specified",
    volume: payload.volume || "Not specified",
    destination: payload.destination || "Not specified",
    packingSize: payload.packing_size || "Not specified",
    requirement: payload.notes || "Not provided",
    sourcePage: payload.source_page || "Not provided",
    pageTitle: payload.page_title || "Not provided",
    submittedAt: nowIso(),
  };

  async function parseAppsScriptResponse(response) {
    const contentType = String(response.headers.get("content-type") || "");
    return contentType.includes("application/json")
      ? await response.json().catch(() => ({}))
      : { message: (await response.text().catch(() => "")).trim() };
  }

  try {
    const response = await fetch(webhookUrl, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json; charset=utf-8",
      },
      body: JSON.stringify(requestBody),
      redirect: "manual",
    });

    if ([301, 302, 303, 307, 308].includes(response.status)) {
      const redirectUrl = String(response.headers.get("location") || "").trim();
      if (!redirectUrl) {
        return [false, "Google Apps Script mailer redirected without a response URL."];
      }

      const finalResponse = await fetch(redirectUrl, {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      });
      const finalResult = await parseAppsScriptResponse(finalResponse);

      if (finalResponse.ok && finalResult?.success !== false && finalResult?.success !== "false") {
        return [true, finalResult?.message || ""];
      }

      return [false, finalResult?.message || `Google Apps Script mailer returned ${finalResponse.status}.`];
    }

    const result = await parseAppsScriptResponse(response);

    if (response.ok && result?.success !== false && result?.success !== "false") {
      return [true, result?.message || ""];
    }

    return [false, result?.message || `Google Apps Script mailer returned ${response.status}.`];
  } catch (error) {
    return [false, "Google Apps Script mailer could not be reached."];
  }
}

export async function forwardInquiry(payload, env) {
  const destination = inquiryDestination(env);
  if (!destination) {
    return [false, "Inquiry destination email is not configured."];
  }

  if (googleAppsScriptWebhookUrl(env)) {
    return sendViaGoogleAppsScript(payload, env);
  }

  const relay = relaySource(payload);

  const forwardPayload = new URLSearchParams({
    _subject: `${payload.request_type} | ${payload.product || "Not specified"}`,
    _template: "table",
    _captcha: "false",
    _replyto: payload.email,
    "Request Type": payload.request_type,
    Product: payload.product || "Not specified",
    Name: payload.name,
    Company: payload.company || "Not specified",
    Email: payload.email,
    Phone: payload.phone || "Not provided",
    Application: payload.application || "Not specified",
    Volume: payload.volume || "Not specified",
    Destination: payload.destination || "Not specified",
    "Packing Size": payload.packing_size || "Not specified",
    Requirement: payload.notes || "Not provided",
    "Source Page": payload.source_page || "Not provided",
    "Page Title": payload.page_title || "Not provided",
  });

  const requestInit = {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
      "X-Requested-With": "XMLHttpRequest",
      Origin: relay.origin,
      Referer: relay.referer,
    },
    body: forwardPayload.toString(),
  };

  for (let attempt = 0; attempt < 3; attempt += 1) {
    try {
      const response = await fetch(formSubmitEndpoint(env), requestInit);
      const result = await response.json().catch(() => ({}));
      if (response.ok && (result?.success === true || result?.success === "true")) {
        return [true, ""];
      }

      const message = result?.message || "Mail relay rejected the inquiry.";
      if (response.status === 429 || isRateLimitMessage(message)) {
        if (attempt < 2) {
          await sleep(1200 * (attempt + 1));
          continue;
        }
        return [false, "The inquiry service is temporarily busy. Please try again in one or two minutes."];
      }
      if (attempt < 2) {
        await sleep(1200 * (attempt + 1));
        continue;
      }

      return [false, /<html|<body|authorization required/i.test(message) ? "The inquiry service rejected the submission. Please try again shortly." : message];
    } catch (error) {
      if (attempt < 2) {
        await sleep(1200 * (attempt + 1));
        continue;
      }
      return [false, "Forwarding inquiry to the mail relay failed."];
    }
  }

  return [false, "Mail relay rejected the inquiry."];
}

export function sanitizeHoneypot(value) {
  return sanitizeField("company_website", value);
}
