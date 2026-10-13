"use strict";

// Offline DOM/fetch mocks execute the shared source without submitting an inquiry.
const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const { resolve } = require("node:path");
const { test } = require("node:test");
const vm = require("node:vm");
const source = readFileSync(resolve(__dirname, "../../templates/material-ledger.js"), "utf8");

function createHarness(options = {}) {
  const events = [];
  const calls = [];
  const button = { disabled: true, textContent: "Send requirement ↗" };
  const note = { textContent: "", dataset: {}, setAttribute() {} };
  const values = new Map(Object.entries({
    request_type: "Quote", product: "Silica Sand", company_website: "",
    name: "Private Buyer", email: "private@example.test", phone: "+15555550100",
    company: "Private Business", application: "Private application", notes: "Private free text",
    destination: "Private destination", volume: "Private volume", packing_size: "Private packing",
    "g-recaptcha-response": "private-captcha-token", ...options.values,
  }));
  let submit;
  let resets = 0;
  let captchaResets = 0;
  const attributes = new Map();
  const form = {
    dataset: { recaptchaConfigured: options.configured === false ? "false" : "true" },
    elements: { namedItem() { return null; } },
    querySelector(selector) { return selector === "[data-form-note]" ? note : button; },
    addEventListener(type, callback) { if (type === "submit") submit = callback; },
    reportValidity() { return options.valid !== false; },
    setAttribute(key, value) { attributes.set(key, value); },
    removeAttribute(key) { attributes.delete(key); },
    reset() { resets++; values.clear(); },
  };
  const document = {
    querySelector() { return null; },
    querySelectorAll(selector) { return selector === "[data-inquiry-form]" ? [form] : []; },
    getElementById() { return null; },
    documentElement: { classList: { remove() {} } },
    body: { classList: { add() {} } },
    title: "Private title must not enter analytics",
    createElement() {
      return { content: { textContent: "" }, set innerHTML(value) { this.content.textContent = value.replace(/<[^>]*>/g, ""); } };
    },
  };
  const location = {
    href: "https://jadewaves.com/products/silica-sand/?email=private@example.test#private",
    origin: "https://jadewaves.com", pathname: "/products/silica-sand/",
  };
  const window = {
    location,
    matchMedia() { return { matches: true, addEventListener() {} }; },
    grecaptcha: { reset() { captchaResets++; } },
  };
  if (options.analytics !== "absent") {
    window.gtag = (...args) => {
      if (options.analytics === "throws") throw new Error("Analytics unavailable");
      events.push(args);
    };
  }
  const fetch = async (...args) => {
    calls.push(args);
    if (options.fetch) return options.fetch(...args);
    if (options.networkError) throw new Error("Network unavailable");
    return {
      ok: options.ok !== false,
      json: async () => {
        if (options.invalidJson) throw new Error("Invalid JSON");
        return Object.hasOwn(options, "result") ? options.result : { success: true };
      },
    };
  };
  class MockFormData {
    constructor() { this.values = new Map(values); }
    get(key) { return this.values.get(key) ?? null; }
    forEach(callback) { this.values.forEach(callback); }
  }
  vm.runInNewContext(source, {
    window, document, location, fetch, FormData: MockFormData,
    sessionStorage: { getItem() { return null; } }, URL,
  }, { filename: "material-ledger.js" });
  return {
    events, calls, button, note, attributes,
    submit: () => submit({ preventDefault() {} }),
    get resets() { return resets; },
    get captchaResets() { return captchaResets; },
  };
}

test("confirmed success emits one bounded GA4 lead before reset, without personal data or URL query", async () => {
  const harness = createHarness();
  await harness.submit();
  assert.equal(harness.events.length, 1);
  assert.deepEqual(JSON.parse(JSON.stringify(harness.events[0])), ["event", "generate_lead", {
    request_type: "Quote", product: "Silica Sand",
    page_location: "https://jadewaves.com/products/silica-sand/",
    page_referrer: "", page_title: "Jade Waves inquiry",
  }]);
  assert.equal(harness.resets, 1);
  assert.equal(harness.captchaResets, 1);
  assert.equal(harness.note.dataset.state, "success");
  assert.equal(harness.button.disabled, false);
  assert.equal(harness.attributes.has("aria-busy"), false);
});

for (const request_type of ["Quote", "Sample", "TDS", "General Inquiry"]) {
  test(`supported request ${request_type} is preserved`, async () => {
    const harness = createHarness({ values: { request_type, product: "Kaolin (China Clay)" } });
    await harness.submit();
    assert.equal(harness.events[0][2].request_type, request_type);
    assert.equal(harness.events[0][2].product, "Kaolin (China Clay)");
  });
}

test("unknown or personal request/product text is replaced with fixed labels", async () => {
  const harness = createHarness({ values: { request_type: "private@example.test", product: "Private free text" } });
  await harness.submit();
  assert.equal(harness.events[0][2].request_type, "General Inquiry");
  assert.equal(harness.events[0][2].product, "Unspecified");
});

for (const [name, options] of [
  ["invalid form", { valid: false }],
  ["captcha unavailable", { configured: false }],
  ["captcha missing", { values: { "g-recaptcha-response": "" } }],
]) {
  test(`${name} never submits or records a lead`, async () => {
    const harness = createHarness(options);
    await harness.submit();
    assert.equal(harness.calls.length, 0);
    assert.equal(harness.events.length, 0);
    assert.equal(harness.resets, 0);
  });
}

for (const [name, options] of [
  ["HTTP failure despite success body", { ok: false }],
  ["success false", { result: { success: false } }],
  ["success string", { result: { success: "true" } }],
  ["ambiguous empty response", { result: {} }],
  ["null response", { result: null }],
  ["invalid JSON", { invalidJson: true }],
  ["network failure", { networkError: true }],
]) {
  test(`${name} records no lead and restores the form`, async () => {
    const harness = createHarness(options);
    await harness.submit();
    assert.equal(harness.events.length, 0);
    assert.equal(harness.resets, 0);
    assert.equal(harness.note.dataset.state, "error");
    assert.equal(harness.button.disabled, false);
    assert.equal(harness.attributes.has("aria-busy"), false);
  });
}

test("honeypot acknowledgement is excluded even when endpoint returns success true", async () => {
  const harness = createHarness({ values: { company_website: "https://spam.example.test" } });
  await harness.submit();
  assert.equal(harness.calls.length, 1);
  assert.equal(harness.events.length, 0);
  assert.equal(harness.resets, 1);
  assert.equal(harness.note.dataset.state, "success");
});

for (const analytics of ["absent", "throws"]) {
  test(`analytics ${analytics} cannot interfere with confirmed form success`, async () => {
    const harness = createHarness({ analytics });
    await harness.submit();
    assert.equal(harness.events.length, 0);
    assert.equal(harness.resets, 1);
    assert.equal(harness.captchaResets, 1);
    assert.equal(harness.note.dataset.state, "success");
    assert.equal(harness.button.disabled, false);
  });
}

test("rapid duplicate submission sends once and records once after confirmation", async () => {
  let complete;
  const pending = new Promise((resolve) => { complete = resolve; });
  const harness = createHarness({ fetch: () => pending });
  const first = harness.submit();
  await harness.submit();
  assert.equal(harness.calls.length, 1);
  assert.equal(harness.events.length, 0);
  complete({ ok: true, json: async () => ({ success: true }) });
  await first;
  assert.equal(harness.events.length, 1);
  assert.equal(harness.resets, 1);
});

test("failed first attempt can be retried and records only the successful attempt", async () => {
  let attempts = 0;
  const harness = createHarness({ fetch: async () => {
    attempts++;
    return { ok: true, json: async () => ({ success: attempts > 1 }) };
  } });
  await harness.submit();
  assert.equal(harness.events.length, 0);
  await harness.submit();
  assert.equal(harness.calls.length, 2);
  assert.equal(harness.events.length, 1);
});
