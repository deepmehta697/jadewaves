const DEFAULT_STATE = {
  settings: {
    senderName: "Deep Mehta",
    senderCompany: "Jade Waves Enterprise",
    senderEmail: "",
    productLibrary: [
      "Silica Sand",
      "Quartz Sand",
      "Silica Flour",
      "Feldspar",
      "China Clay",
      "Bentonite",
      "Fly Ash",
      "Talc",
      "Copper Slag",
      "Salt",
    ],
  },
  gmail: {
    clientId: "",
    lastSyncAt: "",
  },
  companies: [],
};

export function defaultState() {
  return JSON.parse(JSON.stringify(DEFAULT_STATE));
}

function normalizeProducts(value) {
  if (Array.isArray(value)) {
    return value.map((item) => String(item || "").trim()).filter(Boolean);
  }

  return String(value || "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function normalizeAccountState(value) {
  const normalized = String(value || "active").toLowerCase();
  if (["active", "interested", "on_hold", "closed"].includes(normalized)) return normalized;
  return "active";
}

function normalizeIsoString(value) {
  if (!value) return "";
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? "" : date.toISOString();
}

function normalizeCompany(rawCompany = {}) {
  return {
    id: String(rawCompany.id || ""),
    companyName: String(rawCompany.companyName || rawCompany.company || "").trim(),
    contactName: String(rawCompany.contactName || rawCompany.contact || "").trim(),
    contactEmail: String(rawCompany.contactEmail || rawCompany.email || "").trim(),
    country: String(rawCompany.country || "").trim(),
    industry: String(rawCompany.industry || "").trim(),
    application: String(rawCompany.application || "").trim(),
    products: normalizeProducts(rawCompany.products || rawCompany.productFocus || ""),
    website: String(rawCompany.website || "").trim(),
    accountState: normalizeAccountState(rawCompany.accountState || rawCompany.status || "active"),
    lastOutboundAt: normalizeIsoString(rawCompany.lastOutboundAt),
    lastInboundAt: normalizeIsoString(rawCompany.lastInboundAt),
    followUpCount: Math.max(0, Number(rawCompany.followUpCount) || 0),
    ignoreFollowUps: Boolean(rawCompany.ignoreFollowUps),
    notes: String(rawCompany.notes || "").trim(),
    gmailSyncedAt: normalizeIsoString(rawCompany.gmailSyncedAt),
  };
}

export function normalizeState(rawState = {}) {
  const settings = rawState.settings || {};
  const gmail = rawState.gmail || {};
  const companies = Array.isArray(rawState.companies) ? rawState.companies.map(normalizeCompany) : [];

  return {
    settings: {
      senderName: String(settings.senderName || DEFAULT_STATE.settings.senderName),
      senderCompany: String(settings.senderCompany || DEFAULT_STATE.settings.senderCompany),
      senderEmail: String(settings.senderEmail || ""),
      productLibrary: normalizeProducts(
        Array.isArray(settings.productLibrary)
          ? settings.productLibrary.join(",")
          : settings.productLibrary || DEFAULT_STATE.settings.productLibrary.join(",")
      ),
    },
    gmail: {
      clientId: String(gmail.clientId || ""),
      lastSyncAt: String(gmail.lastSyncAt || ""),
    },
    companies,
  };
}

async function ensureStateTable(db) {
  await db.exec(
    "CREATE TABLE IF NOT EXISTS app_state (" +
      "key TEXT PRIMARY KEY NOT NULL, " +
      "value TEXT NOT NULL, " +
      "updated_at TEXT NOT NULL" +
      ")"
  );
}

export async function readState(db) {
  if (!db) return defaultState();
  await ensureStateTable(db);
  const row = await db.prepare("SELECT value FROM app_state WHERE key = ?1").bind("crm").first();
  if (!row || !row.value) {
    return defaultState();
  }

  try {
    return normalizeState(JSON.parse(String(row.value)));
  } catch (error) {
    console.error("Unable to parse CRM state from D1", error);
    return defaultState();
  }
}

export async function writeState(db, rawState) {
  if (!db) {
    throw new Error("Missing D1 binding");
  }

  await ensureStateTable(db);
  const normalized = normalizeState(rawState);
  await db
    .prepare(
      "INSERT INTO app_state (key, value, updated_at) VALUES (?1, ?2, ?3) " +
        "ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at"
    )
    .bind("crm", JSON.stringify(normalized), new Date().toISOString())
    .run();

  return normalized;
}

export function jsonResponse(payload, status = 200) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
      "X-Content-Type-Options": "nosniff",
      "Referrer-Policy": "same-origin",
      "X-Frame-Options": "DENY",
      "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
    },
  });
}
