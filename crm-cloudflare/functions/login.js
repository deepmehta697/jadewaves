import {
  authEnabled,
  credentialsMatch,
  isAuthenticated,
  loginSuccessResponse,
  normalizedNextPath,
  redirectToPath,
  renderLoginPage,
} from "./_lib/auth.js";

export async function onRequestGet(context) {
  const nextPath = normalizedNextPath(new URL(context.request.url).searchParams.get("next"));

  if (!authEnabled(context.env)) {
    return redirectToPath(context.request, nextPath);
  }

  if (await isAuthenticated(context.request, context.env)) {
    return redirectToPath(context.request, nextPath);
  }

  return renderLoginPage(nextPath);
}

export async function onRequestPost(context) {
  const formData = await context.request.formData();
  const username = String(formData.get("username") || "");
  const password = String(formData.get("password") || "");
  const nextPath = normalizedNextPath(String(formData.get("next") || "/"));

  if (!authEnabled(context.env)) {
    return redirectToPath(context.request, nextPath);
  }

  if (!credentialsMatch(username, password, context.env)) {
    return renderLoginPage(nextPath, "Incorrect username or password.");
  }

  return loginSuccessResponse(context.request, context.env, username, nextPath);
}
