(() => {
  "use strict";

  const header = document.querySelector("[data-header]");
  const menuToggle = document.querySelector("[data-menu-toggle]");
  const mobileMenu = document.querySelector("[data-mobile-menu]");
  const formTargets = [...document.querySelectorAll("[data-inquiry-form]")];
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const requestTypes = new Set(["Quote", "Sample", "TDS", "General Inquiry"]);
  const pendingRequestKey = "jade-waves-inquiry-request";
  let backgroundState = [];

  // Keep the page accessible when scripting or IntersectionObserver is unavailable.
  const reveals = [...document.querySelectorAll("[data-reveal]")];
  let revealObserver;
  const showAll = () => {
    reveals.forEach((node) => node.classList.add("is-visible"));
    revealObserver?.disconnect();
    document.documentElement.classList.remove("js-reveal-ready");
  };
  if (!reducedMotion.matches && "IntersectionObserver" in window) {
    try {
      revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          revealObserver.unobserve(entry.target);
        });
      }, { threshold: 0.08 });
      reveals.forEach((node) => {
        if (node.getBoundingClientRect().top < window.innerHeight) node.classList.add("is-visible");
        else revealObserver.observe(node);
      });
      document.documentElement.classList.add("js-reveal-ready");
    } catch (_) { showAll(); }
  } else { showAll(); }
  reducedMotion.addEventListener?.("change", (event) => { if (event.matches) showAll(); });

  // Give the shared skip link a target on both new and retained page shells.
  const main = document.querySelector("main");
  if (main && !document.getElementById("main-content")) main.id = "main-content";
  if (main && !main.hasAttribute("tabindex")) main.setAttribute("tabindex", "-1");
  document.querySelector(".skip-link")?.addEventListener("click", (event) => {
    if (!main) return;
    event.preventDefault();
    main.focus({ preventScroll: true });
    main.scrollIntoView({ behavior: reducedMotion.matches ? "instant" : "smooth" });
  });

  const menuFocusables = () => [...mobileMenu.querySelectorAll('a[href], button:not([disabled]), [tabindex="0"]')]
    .filter((node) => !node.hidden && node.getClientRects().length);
  const setBackgroundInert = () => {
    let branch = mobileMenu;
    while (branch && branch !== document.body) {
      [...branch.parentElement.children].forEach((node) => {
        if (node === branch || ["SCRIPT", "STYLE", "LINK"].includes(node.tagName)) return;
        backgroundState.push([node, node.inert]);
        node.inert = true;
      });
      branch = branch.parentElement;
    }
  };
  const closeMenu = (restoreFocus = true) => {
    if (!mobileMenu || mobileMenu.hidden) return;
    mobileMenu.hidden = true;
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation");
    document.body.classList.remove("menu-open");
    header?.classList.remove("is-menu-open");
    backgroundState.forEach(([node, wasInert]) => { node.inert = wasInert; });
    backgroundState = [];
    if (restoreFocus) {
      const focusTarget = menuToggle.getClientRects().length ? menuToggle : header?.querySelector(".brand-mark");
      focusTarget?.focus();
    }
  };
  const openMenu = () => {
    mobileMenu.hidden = false;
    menuToggle.setAttribute("aria-expanded", "true");
    menuToggle.setAttribute("aria-label", "Close navigation");
    document.body.classList.add("menu-open");
    header?.classList.add("is-menu-open");
    setBackgroundInert();
    (menuFocusables()[0] || mobileMenu).focus();
  };
  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener("click", () => { mobileMenu.hidden ? openMenu() : closeMenu(); });
    mobileMenu.querySelector("[data-menu-close]")?.addEventListener("click", () => closeMenu());
    document.addEventListener("keydown", (event) => {
      if (mobileMenu.hidden) return;
      if (event.key === "Escape") { event.preventDefault(); closeMenu(); return; }
      if (event.key !== "Tab") return;
      const targets = menuFocusables();
      const first = targets[0];
      const last = targets.at(-1);
      if (!first) { event.preventDefault(); mobileMenu.focus(); return; }
      if (event.shiftKey && (document.activeElement === first || document.activeElement === mobileMenu)) {
        event.preventDefault(); last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault(); first.focus();
      }
    });
    document.addEventListener("focusin", (event) => {
      if (!mobileMenu.hidden && !mobileMenu.contains(event.target)) (menuFocusables()[0] || mobileMenu).focus();
    });
    document.addEventListener("click", (event) => {
      if (!mobileMenu.hidden && !mobileMenu.contains(event.target) && !menuToggle.contains(event.target)) closeMenu();
    });
    mobileMenu.querySelectorAll("a[href]").forEach((link) => link.addEventListener("click", () => closeMenu()));
    window.matchMedia("(min-width: 961px)").addEventListener?.("change", (event) => { if (event.matches) closeMenu(); });
    menuToggle.hidden = false;
  }

  const setRequestType = (value) => {
    if (!requestTypes.has(value)) return;
    formTargets.forEach((form) => { const field = form.elements.namedItem("request_type"); if (field) field.value = value; });
  };
  const setProduct = (value) => {
    formTargets.forEach((form) => {
      const field = form.elements.namedItem("product");
      if (!field || field.readOnly) return;
      if (field.tagName !== "SELECT" || [...field.options].some((option) => option.value === value)) field.value = value;
    });
  };
  try {
    const pending = sessionStorage.getItem(pendingRequestKey);
    if (pending) { setRequestType(pending); sessionStorage.removeItem(pendingRequestKey); }
  } catch (_) { /* Forms work without storage. */ }
  document.querySelectorAll("[data-set-request], [data-set-product], [data-prefill-product]").forEach((link) => {
    link.addEventListener("click", () => {
      const request = link.dataset.setRequest;
      if (request) setRequestType(request);
      const product = link.dataset.setProduct || link.dataset.prefillProduct;
      if (product) setProduct(product);
      if (requestTypes.has(request) && link.href) {
        const target = new URL(link.href, document.baseURI);
        if (target.origin === location.origin && target.pathname !== location.pathname) {
          try { sessionStorage.setItem(pendingRequestKey, request); } catch (_) { /* Optional cross-page prefill. */ }
        }
      }
    });
  });

  const stripHtml = (value) => {
    const template = document.createElement("template");
    template.innerHTML = String(value ?? "");
    return (template.content.textContent || "").replace(/[\u0000-\u001F\u007F]+/g, " ").replace(/\s+/g, " ").trim();
  };
  const sanitizePayload = (data) => {
    const payload = {};
    data.forEach((value, key) => { payload[key] = key === "g-recaptcha-response" ? String(value || "").trim() : stripHtml(value); });
    payload.source_page = window.location.href;
    payload.page_title = document.title;
    return payload;
  };
  formTargets.forEach((form) => {
    const note = form.querySelector("[data-form-note]");
    const submitButton = form.querySelector('button[type="submit"]');
    const defaultLabel = submitButton?.textContent.trim() || "Send requirement ↗";
    const email = document.querySelector('.contact-details a[href^="mailto:"]')?.getAttribute("href").slice(7);
    const phone = document.querySelector('.contact-details a[href^="tel:"]')?.textContent.trim();
    const fallback = email ? `Please email ${email}${phone ? ` or call ${phone}` : ""}.` : "Please contact the export desk directly.";
    const setNote = (message, state) => {
      if (!note) return;
      note.textContent = message;
      note.dataset.state = state;
    };
    note?.setAttribute("aria-live", "polite");
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (!submitButton || submitButton.disabled || !form.reportValidity()) return;
      const data = new FormData(form);
      if (form.dataset.recaptchaConfigured !== "true") {
        setNote(`Online inquiry is currently unavailable. ${fallback}`, "error"); return;
      }
      if (!String(data.get("g-recaptcha-response") || "").trim()) {
        setNote("Please complete the Google reCAPTCHA check before submitting.", "error"); return;
      }
      submitButton.disabled = true;
      submitButton.textContent = "Sending…";
      form.setAttribute("aria-busy", "true");
      setNote("Sending your requirement. Please wait a moment.", "sending");
      try {
        const response = await fetch(form.dataset.inquiryEndpoint || "/api/inquiry", {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify(sanitizePayload(data)),
        });
        const result = await response.json().catch(() => null);
        if (!response.ok || result?.success !== true) throw new Error(result?.message || "Submission could not be confirmed. Please try again.");
        form.reset();
        if (window.grecaptcha) window.grecaptcha.reset();
        setNote(result?.message || "Inquiry sent. We will review your requirement and respond by email.", "success");
      } catch (error) {
        setNote(`${error?.message || "Submission did not go through."} ${fallback}`, "error");
      } finally {
        submitButton.disabled = false;
        submitButton.textContent = defaultLabel;
        form.removeAttribute("aria-busy");
      }
    });
    // Enable native controls only after the JSON submission handler is attached.
    if (submitButton) submitButton.disabled = false;
  });
  document.querySelectorAll("[data-current-year]").forEach((node) => { node.textContent = String(new Date().getFullYear()); });
  document.body.classList.add("is-ready");
})();
