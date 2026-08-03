import { jsonResponse } from "./state.js";

const SESSION_COOKIE_NAME = "jade_waves_crm_session";
const DEFAULT_SESSION_MAX_AGE = 60 * 60 * 24 * 14;

export function authEnabled(env) {
  return Boolean(env.CRM_USERNAME && env.CRM_PASSWORD);
}

function sessionSecret(env) {
  return env.CRM_SESSION_SECRET || `${env.CRM_USERNAME || ""}:${env.CRM_PASSWORD || ""}:jade-waves-crm`;
}

function sessionMaxAge(env) {
  const parsed = Number(env.CRM_SESSION_MAX_AGE);
  if (!Number.isFinite(parsed)) return DEFAULT_SESSION_MAX_AGE;
  return Math.max(900, Math.floor(parsed));
}

function normalizeNextPath(nextPath) {
  if (!nextPath) return "/";
  if (!nextPath.startsWith("/")) return "/";
  if (nextPath.startsWith("//")) return "/";
  return nextPath;
}

function parseCookies(rawCookie) {
  const parsed = {};
  String(rawCookie || "")
    .split(";")
    .forEach((segment) => {
      const separatorIndex = segment.indexOf("=");
      if (separatorIndex === -1) return;
      const key = segment.slice(0, separatorIndex).trim();
      const value = segment.slice(separatorIndex + 1).trim();
      if (!key) return;
      parsed[key] = value;
    });
  return parsed;
}

function constantTimeEqual(left, right) {
  const leftValue = String(left || "");
  const rightValue = String(right || "");
  let mismatch = leftValue.length === rightValue.length ? 0 : 1;
  const maxLength = Math.max(leftValue.length, rightValue.length);

  for (let index = 0; index < maxLength; index += 1) {
    mismatch |= (leftValue.charCodeAt(index) || 0) ^ (rightValue.charCodeAt(index) || 0);
  }

  return mismatch === 0;
}

async function hmacHex(secret, payload) {
  const encoder = new TextEncoder();
  const cryptoKey = await crypto.subtle.importKey(
    "raw",
    encoder.encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const signature = await crypto.subtle.sign("HMAC", cryptoKey, encoder.encode(payload));
  return Array.from(new Uint8Array(signature))
    .map((value) => value.toString(16).padStart(2, "0"))
    .join("");
}

function base64UrlEncode(value) {
  const encoded = btoa(value);
  return encoded.replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

function base64UrlDecode(value) {
  const padded = `${value}${"=".repeat((4 - (value.length % 4 || 4)) % 4)}`;
  return atob(padded.replace(/-/g, "+").replace(/_/g, "/"));
}

async function createSessionCookieValue(env, username) {
  const expiresAt = String(Math.floor(Date.now() / 1000) + sessionMaxAge(env));
  const payload = `${username}:${expiresAt}`;
  const signature = await hmacHex(sessionSecret(env), payload);
  return base64UrlEncode(`${payload}:${signature}`);
}

async function verifySessionCookieValue(value, env) {
  try {
    const decoded = base64UrlDecode(value);
    const [username, expiresAt, signature] = decoded.split(":");
    if (!username || !expiresAt || !signature) return false;
    if (!constantTimeEqual(username, env.CRM_USERNAME || "")) return false;
    if (Number(expiresAt) <= Math.floor(Date.now() / 1000)) return false;
    const expected = await hmacHex(sessionSecret(env), `${username}:${expiresAt}`);
    return constantTimeEqual(signature, expected);
  } catch (error) {
    return false;
  }
}

function htmlEscape(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function loginPageMarkup(nextPath, errorMessage) {
  const safeNext = htmlEscape(normalizeNextPath(nextPath));
  const errorMarkup = errorMessage
    ? `<p style="margin:0;color:#b76439;font-size:0.92rem;">${htmlEscape(errorMessage)}</p>`
    : "";

  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Jade Waves CRM Login</title>
    <style>
      :root {
        --bg: #f2f0ea;
        --surface: #fbfaf7;
        --ink: #1f2320;
        --ink-soft: rgba(31, 35, 32, 0.72);
        --line: rgba(31, 35, 32, 0.12);
        --accent: #15745c;
      }
      * { box-sizing: border-box; }
      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        background: linear-gradient(180deg, rgba(232, 227, 215, 0.84), rgba(242, 240, 234, 0.94) 18rem), #f2f0ea;
        color: var(--ink);
        font-family: Manrope, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
      main {
        width: min(28rem, calc(100vw - 2rem));
        padding: 1.2rem;
        border-radius: 8px;
        border: 1px solid var(--line);
        background: rgba(251, 250, 247, 0.96);
        box-shadow: 0 24px 50px rgba(31, 35, 32, 0.08);
      }
      h1 { margin: 0 0 0.4rem; line-height: 1.05; }
      p { color: var(--ink-soft); line-height: 1.55; }
      form { display: grid; gap: 0.82rem; margin-top: 1rem; }
      label { display: grid; gap: 0.38rem; font-weight: 700; font-size: 0.92rem; }
      input {
        width: 100%;
        padding: 0.82rem 0.9rem;
        border: 1px solid var(--line);
        border-radius: 8px;
        font: inherit;
      }
      button {
        min-height: 2.9rem;
        border: 0;
        border-radius: 8px;
        background: var(--accent);
        color: #fffef9;
        font: inherit;
        font-weight: 700;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <main>
      <p style="margin:0 0 0.45rem;font-size:0.76rem;font-weight:800;text-transform:uppercase;color:#15745c;">Jade Waves CRM</p>
      <h1>Private login</h1>
      <p>Use your CRM credentials to view companies, draft follow-ups, and scan Gmail reply status.</p>
      ${errorMarkup}
      <form method="post" action="/login">
        <input type="hidden" name="next" value="${safeNext}">
        <label>
          <span>Username</span>
          <input type="text" name="username" autocomplete="username" required>
        </label>
        <label>
          <span>Password</span>
          <input type="password" name="password" autocomplete="current-password" required>
        </label>
        <button type="submit">Open CRM</button>
      </form>
    </main>
  </body>
</html>`;
}

export function renderLoginPage(nextPath, errorMessage = "") {
  return new Response(loginPageMarkup(nextPath, errorMessage), {
    status: 200,
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "no-store",
      "X-Content-Type-Options": "nosniff",
      "Referrer-Policy": "same-origin",
      "X-Frame-Options": "DENY",
      "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
    },
  });
}

export function credentialsMatch(username, password, env) {
  return constantTimeEqual(username, env.CRM_USERNAME || "") && constantTimeEqual(password, env.CRM_PASSWORD || "");
}

export async function isAuthenticated(request, env) {
  if (!authEnabled(env)) return true;
  const cookies = parseCookies(request.headers.get("Cookie") || "");
  const sessionValue = cookies[SESSION_COOKIE_NAME];
  if (!sessionValue) return false;
  return verifySessionCookieValue(sessionValue, env);
}

export function redirectToLogin(request) {
  const url = new URL(request.url);
  const nextPath = `${url.pathname}${url.search}`;
  return Response.redirect(`${url.origin}/login?next=${encodeURIComponent(nextPath)}`, 302);
}

export function redirectToPath(request, nextPath) {
  const url = new URL(request.url);
  return Response.redirect(`${url.origin}${normalizeNextPath(nextPath)}`, 302);
}

export function unauthorizedJson() {
  return jsonResponse({ error: "unauthorized" }, 401);
}

export async function loginSuccessResponse(request, env, username, nextPath) {
  const url = new URL(request.url);
  const headers = new Headers({
    Location: `${url.origin}${normalizeNextPath(nextPath)}`,
    "Cache-Control": "no-store",
  });
  headers.append(
    "Set-Cookie",
    `${SESSION_COOKIE_NAME}=${await createSessionCookieValue(env, username)}; Path=/; HttpOnly; SameSite=Strict; Secure; Max-Age=${sessionMaxAge(env)}`
  );
  return new Response(null, { status: 302, headers });
}

export function logoutResponse(request) {
  const url = new URL(request.url);
  const headers = new Headers({
    Location: `${url.origin}/login`,
    "Cache-Control": "no-store",
  });
  headers.append(
    "Set-Cookie",
    `${SESSION_COOKIE_NAME}=deleted; Path=/; HttpOnly; SameSite=Strict; Secure; Max-Age=0`
  );
  return new Response(null, { status: 302, headers });
}

export function normalizedNextPath(value) {
  return normalizeNextPath(value);
}
