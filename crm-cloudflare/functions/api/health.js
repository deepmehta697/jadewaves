import { authEnabled } from "../_lib/auth.js";
import { jsonResponse } from "../_lib/state.js";

export async function onRequestGet(context) {
  return jsonResponse({
    ok: true,
    authEnabled: authEnabled(context.env),
    hasDatabase: Boolean(context.env.DB),
    service: "jadewaves-crm",
    timestamp: new Date().toISOString(),
  });
}
