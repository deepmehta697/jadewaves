import { authEnabled, isAuthenticated, redirectToLogin, unauthorizedJson } from "./_lib/auth.js";

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const path = url.pathname;
  const publicPaths = new Set(["/api/inquiry"]);

  if (!authEnabled(context.env)) {
    return context.next();
  }

  if (publicPaths.has(path)) {
    return context.next();
  }

  if (path === "/login" || path === "/logout" || path === "/favicon.ico" || path.startsWith("/.well-known/")) {
    return context.next();
  }

  if (await isAuthenticated(context.request, context.env)) {
    return context.next();
  }

  if (path.startsWith("/api/")) {
    return unauthorizedJson();
  }

  return redirectToLogin(context.request);
}
