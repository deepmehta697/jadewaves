var DESTINATION_EMAIL = "deep@jadewavesenterprise.com";
var SENDER_NAME = "Jade Waves Enterprise Website";

var MAX_FIELD_LENGTHS = {
  requestType: 40,
  product: 120,
  name: 120,
  company: 160,
  email: 160,
  phone: 80,
  application: 160,
  volume: 120,
  destination: 160,
  packingSize: 120,
  requirement: 4000,
  sourcePage: 320,
  pageTitle: 160,
  submittedAt: 80,
  destinationEmail: 160,
};

function doGet() {
  return ContentService.createTextOutput("Jade Waves inquiry mailer is live.");
}

function doPost(e) {
  try {
    if (!e || !e.postData || !e.postData.contents) {
      return jsonResponse_({ success: false, message: "Missing request body." });
    }

    var payload = sanitizePayload_(JSON.parse(e.postData.contents));
    if (!payload.name || !payload.email) {
      return jsonResponse_({ success: false, message: "Name and email are required." });
    }

    MailApp.sendEmail({
      to: payload.destinationEmail || DESTINATION_EMAIL,
      subject: buildSubject_(payload),
      body: buildPlainBody_(payload),
      htmlBody: buildHtmlBody_(payload),
      replyTo: payload.email,
      name: SENDER_NAME,
    });

    return jsonResponse_({
      success: true,
      message: "Inquiry sent. Jade Waves will get back to you shortly.",
    });
  } catch (error) {
    return jsonResponse_({
      success: false,
      message: "Google mailer could not send the inquiry.",
      error: String(error && error.message ? error.message : error),
    });
  }
}

function sanitizePayload_(input) {
  var payload = input || {};
  var result = {};

  Object.keys(MAX_FIELD_LENGTHS).forEach(function (field) {
    var text = stripHtml_(payload[field] || "");
    result[field] = text.slice(0, MAX_FIELD_LENGTHS[field]).trim();
  });

  result.email = result.email.toLowerCase();
  return result;
}

function stripHtml_(value) {
  return String(value || "")
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

function escapeHtml_(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function buildSubject_(payload) {
  return [payload.requestType || "General Inquiry", payload.product || "Not specified"].join(" | ");
}

function buildPlainBody_(payload) {
  return [
    "New website inquiry",
    "",
    "Request Type: " + (payload.requestType || "General Inquiry"),
    "Product: " + (payload.product || "Not specified"),
    "Name: " + payload.name,
    "Company: " + (payload.company || "Not specified"),
    "Email: " + payload.email,
    "Phone: " + (payload.phone || "Not provided"),
    "Application: " + (payload.application || "Not specified"),
    "Volume: " + (payload.volume || "Not specified"),
    "Destination: " + (payload.destination || "Not specified"),
    "Packing Size: " + (payload.packingSize || "Not specified"),
    "Requirement: " + (payload.requirement || "Not provided"),
    "Source Page: " + (payload.sourcePage || "Not provided"),
    "Page Title: " + (payload.pageTitle || "Not provided"),
    "Submitted At: " + (payload.submittedAt || new Date().toISOString()),
  ].join("\n");
}

function buildHtmlBody_(payload) {
  var rows = [
    ["Request Type", payload.requestType || "General Inquiry"],
    ["Product", payload.product || "Not specified"],
    ["Name", payload.name],
    ["Company", payload.company || "Not specified"],
    ["Email", payload.email],
    ["Phone", payload.phone || "Not provided"],
    ["Application", payload.application || "Not specified"],
    ["Volume", payload.volume || "Not specified"],
    ["Destination", payload.destination || "Not specified"],
    ["Packing Size", payload.packingSize || "Not specified"],
    ["Requirement", payload.requirement || "Not provided"],
    ["Source Page", payload.sourcePage || "Not provided"],
    ["Page Title", payload.pageTitle || "Not provided"],
    ["Submitted At", payload.submittedAt || new Date().toISOString()],
  ];

  var htmlRows = rows
    .map(function (row) {
      return (
        "<tr>" +
        "<td style=\"padding:10px 12px;border:1px solid #d7dce5;font-weight:600;background:#f5f7fb;vertical-align:top;\">" +
        escapeHtml_(row[0]) +
        "</td>" +
        "<td style=\"padding:10px 12px;border:1px solid #d7dce5;vertical-align:top;\">" +
        escapeHtml_(row[1]) +
        "</td>" +
        "</tr>"
      );
    })
    .join("");

  return (
    "<div style=\"font-family:Arial,sans-serif;color:#111827;\">" +
    "<h2 style=\"margin:0 0 16px;\">New website inquiry</h2>" +
    "<table style=\"border-collapse:collapse;width:100%;max-width:760px;\">" +
    htmlRows +
    "</table>" +
    "</div>"
  );
}

function jsonResponse_(payload) {
  return ContentService.createTextOutput(JSON.stringify(payload)).setMimeType(ContentService.MimeType.JSON);
}
