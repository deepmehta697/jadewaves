import {
  corsHeaders,
  forwardInquiry,
  inquiryJsonResponse,
  resolveAllowedOrigin,
  sanitizeHoneypot,
  sanitizeInquiryPayload,
  storeInquiry,
  updateInquiryDeliveryStatus,
  verifyInquiryPayload,
  verifyRecaptcha,
} from "../_lib/inquiry.js";

function forbiddenOriginResponse() {
  return new Response(JSON.stringify({ success: false, message: "Origin not allowed." }), {
    status: 403,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
      "X-Content-Type-Options": "nosniff",
      Vary: "Origin",
    },
  });
}

export async function onRequestOptions(context) {
  const origin = resolveAllowedOrigin(context.request, context.env);
  if (context.request.headers.get("Origin") && !origin) {
    return forbiddenOriginResponse();
  }

  return new Response(null, {
    status: 204,
    headers: corsHeaders(origin || ""),
  });
}

export async function onRequestPost(context) {
  const requestedOrigin = String(context.request.headers.get("Origin") || "").trim();
  const allowedOrigin = resolveAllowedOrigin(context.request, context.env);

  if (requestedOrigin && !allowedOrigin) {
    return forbiddenOriginResponse();
  }

  let payload;
  try {
    payload = await context.request.json();
  } catch (error) {
    return inquiryJsonResponse({ success: false, message: "Invalid JSON payload." }, 400, allowedOrigin || "");
  }

  if (sanitizeHoneypot(payload?.company_website || "")) {
    return inquiryJsonResponse({ success: true, message: "Inquiry sent." }, 200, allowedOrigin || "");
  }

  const [captchaOk, captchaMessage] = await verifyRecaptcha(
    String(payload?.["g-recaptcha-response"] || "").trim(),
    context.request,
    context.env
  );
  if (!captchaOk) {
    return inquiryJsonResponse({ success: false, message: captchaMessage }, 400, allowedOrigin || "");
  }

  const cleaned = sanitizeInquiryPayload(payload || {});
  const [valid, validationMessage] = verifyInquiryPayload(cleaned);
  if (!valid) {
    return inquiryJsonResponse({ success: false, message: validationMessage }, 400, allowedOrigin || "");
  }

  const [stored, inquiryId] = await storeInquiry(cleaned, context.env);
  const [forwarded, forwardMessage] = await forwardInquiry(cleaned, context.env);
  if (forwarded) {
    await updateInquiryDeliveryStatus(inquiryId, "sent", "", context.env);
    return inquiryJsonResponse(
      { success: true, message: "Inquiry sent. Jade Waves will get back to you shortly." },
      200,
      allowedOrigin || ""
    );
  }

  if (stored && inquiryId) {
    await updateInquiryDeliveryStatus(inquiryId, "email_pending", forwardMessage, context.env);
    return inquiryJsonResponse(
      {
        success: true,
        message:
          "Inquiry received. The email notification is delayed, but your requirement has been recorded and Jade Waves will review it shortly.",
      },
      200,
      allowedOrigin || ""
    );
  }

  return inquiryJsonResponse({ success: false, message: forwardMessage }, 502, allowedOrigin || "");
}
