import { logoutResponse } from "./_lib/auth.js";

export async function onRequestGet(context) {
  return logoutResponse(context.request);
}
