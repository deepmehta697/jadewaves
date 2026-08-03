import { jsonResponse, readState, writeState } from "../_lib/state.js";

export async function onRequestGet(context) {
  if (!context.env.DB) {
    return jsonResponse({ error: "Missing D1 binding" }, 500);
  }

  const state = await readState(context.env.DB);
  return jsonResponse(state);
}

export async function onRequestPut(context) {
  if (!context.env.DB) {
    return jsonResponse({ error: "Missing D1 binding" }, 500);
  }

  let payload;
  try {
    payload = await context.request.json();
  } catch (error) {
    return jsonResponse({ error: "Invalid JSON payload" }, 400);
  }

  const saved = await writeState(context.env.DB, payload || {});
  return jsonResponse(saved);
}
