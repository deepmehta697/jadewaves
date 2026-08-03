const LOCAL_CACHE_KEY = "jade-waves-crm-cloud-cache-v1";
const API_STATE_ENDPOINT = "/api/state";
const GMAIL_SCOPE = "https://www.googleapis.com/auth/gmail.readonly";

const defaultState = {
  settings: {
    senderName: "Deep Mehta",
    senderCompany: "Jade Waves Enterprise",
    senderEmail: "",
    productLibrary: [
      "Silica Sand",
      "Quartz Sand",
      "Silica Flour",
      "Feldspar",
      "China Clay",
      "Bentonite",
      "Fly Ash",
      "Talc",
      "Copper Slag",
      "Salt",
    ],
  },
  gmail: {
    clientId: "",
    lastSyncAt: "",
  },
  companies: [],
};

const uiState = {
  filter: "all",
  search: "",
  selectedCompanyId: null,
  draftMode: "auto",
  storageStatusText: "Loading CRM data from secure cloud storage...",
  storageStatusTone: "saving",
};

const sessionState = {
  gmailToken: "",
  tokenClient: null,
  isSyncing: false,
};

const elements = {
  summaryStrip: document.querySelector("#summaryStrip"),
  companyTableBody: document.querySelector("#companyTableBody"),
  companyForm: document.querySelector("#companyForm"),
  formTitle: document.querySelector("#formTitle"),
  draftMode: document.querySelector("#draftMode"),
  draftSubject: document.querySelector("#draftSubject"),
  draftBody: document.querySelector("#draftBody"),
  draftSummaryText: document.querySelector("#draftSummaryText"),
  filterRow: document.querySelector("#filterRow"),
  searchInput: document.querySelector("#searchInput"),
  newCompanyButton: document.querySelector("#newCompanyButton"),
  deleteCompanyButton: document.querySelector("#deleteCompanyButton"),
  resetFormButton: document.querySelector("#resetFormButton"),
  syncAllButton: document.querySelector("#syncAllButton"),
  saveSettingsButton: document.querySelector("#saveSettingsButton"),
  exportDataButton: document.querySelector("#exportDataButton"),
  importFileInput: document.querySelector("#importFileInput"),
  settingsForm: document.querySelector("#settingsForm"),
  senderName: document.querySelector("#senderName"),
  senderCompany: document.querySelector("#senderCompany"),
  senderEmail: document.querySelector("#senderEmail"),
  productLibrary: document.querySelector("#productLibrary"),
  googleClientId: document.querySelector("#googleClientId"),
  gmailConnectButton: document.querySelector("#gmailConnectButton"),
  gmailRefreshButton: document.querySelector("#gmailRefreshButton"),
  gmailStatusText: document.querySelector("#gmailStatusText"),
  copySubjectButton: document.querySelector("#copySubjectButton"),
  copyBodyButton: document.querySelector("#copyBodyButton"),
  markSentButton: document.querySelector("#markSentButton"),
  markReplyButton: document.querySelector("#markReplyButton"),
  storageStatusText: document.querySelector("#storageStatusText"),
  logoutButton: document.querySelector("#logoutButton"),
};

let state = loadLocalCache();
let saveQueue = Promise.resolve();

function loadLocalCache() {
  try {
    const raw = window.localStorage.getItem(LOCAL_CACHE_KEY);
    if (!raw) return createInitialState();
    const parsed = JSON.parse(raw);
    return normalizeState(parsed);
  } catch (error) {
    console.warn("Unable to load CRM state", error);
    return createInitialState();
  }
}

function createInitialState() {
  return {
    settings: { ...defaultState.settings, productLibrary: [...defaultState.settings.productLibrary] },
    gmail: { ...defaultState.gmail },
    companies: [],
  };
}

function normalizeState(rawState) {
  const settings = rawState.settings || {};
  const gmail = rawState.gmail || {};
  const companies = Array.isArray(rawState.companies) ? rawState.companies.map(normalizeCompany) : [];

  return {
    settings: {
      senderName: settings.senderName || defaultState.settings.senderName,
      senderCompany: settings.senderCompany || defaultState.settings.senderCompany,
      senderEmail: settings.senderEmail || "",
      productLibrary: normalizeProducts(
        Array.isArray(settings.productLibrary) ? settings.productLibrary.join(",") : settings.productLibrary || defaultState.settings.productLibrary.join(",")
      ),
    },
    gmail: {
      clientId: gmail.clientId || "",
      lastSyncAt: gmail.lastSyncAt || "",
    },
    companies,
  };
}

function normalizeCompany(rawCompany) {
  return {
    id: rawCompany.id || generateId(),
    companyName: (rawCompany.companyName || rawCompany.company || "").trim(),
    contactName: (rawCompany.contactName || rawCompany.contact || "").trim(),
    contactEmail: (rawCompany.contactEmail || rawCompany.email || "").trim(),
    country: (rawCompany.country || "").trim(),
    industry: (rawCompany.industry || "").trim(),
    application: (rawCompany.application || "").trim(),
    products: normalizeProducts(rawCompany.products || rawCompany.productFocus || ""),
    website: (rawCompany.website || "").trim(),
    accountState: normalizeAccountState(rawCompany.accountState || rawCompany.status || "active"),
    lastOutboundAt: normalizeIsoString(rawCompany.lastOutboundAt),
    lastInboundAt: normalizeIsoString(rawCompany.lastInboundAt),
    followUpCount: Math.max(0, Number(rawCompany.followUpCount) || 0),
    ignoreFollowUps: Boolean(rawCompany.ignoreFollowUps),
    notes: (rawCompany.notes || "").trim(),
    gmailSyncedAt: normalizeIsoString(rawCompany.gmailSyncedAt),
  };
}

function normalizeAccountState(value) {
  const normalized = String(value || "active").toLowerCase();
  if (["active", "interested", "on_hold", "closed"].includes(normalized)) return normalized;
  return "active";
}

function normalizeIsoString(value) {
  if (!value) return "";
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? "" : date.toISOString();
}

function saveLocalCache() {
  window.localStorage.setItem(LOCAL_CACHE_KEY, JSON.stringify(state));
}

function hasMeaningfulData(candidateState) {
  return Boolean(
    candidateState &&
      ((Array.isArray(candidateState.companies) && candidateState.companies.length) ||
        (candidateState.settings && candidateState.settings.senderEmail))
  );
}

function saveState() {
  saveLocalCache();
  setStorageStatus("Saving CRM data to secure cloud storage...", "saving");

  const snapshot = JSON.parse(JSON.stringify(state));
  saveQueue = saveQueue
    .catch(() => undefined)
    .then(async () => {
      const response = await apiFetch(API_STATE_ENDPOINT, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(snapshot),
      });

      if (!response.ok) {
        throw new Error(`CRM save failed with ${response.status}`);
      }

      const savedState = normalizeState(await response.json());
      state = savedState;
      initSelection();
      saveLocalCache();
      render();
      setStorageStatus(`Saved to secure cloud storage at ${formatTimestamp(new Date().toISOString(), "just now")}.`, "saved");
      return savedState;
    })
    .catch((error) => {
      console.error(error);
      setStorageStatus("Cloud save failed. Working from browser backup until the app reconnects.", "warning");
      return snapshot;
    });

  return saveQueue;
}

async function fetchServerState() {
  const response = await apiFetch(`${API_STATE_ENDPOINT}?ts=${Date.now()}`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error(`CRM load failed with ${response.status}`);
  }

  return normalizeState(await response.json());
}

async function apiFetch(resource, options = {}) {
  const response = await fetch(resource, {
    credentials: "same-origin",
    ...options,
  });

  if (response.status === 401) {
    const nextPath = window.location.pathname + window.location.search;
    window.location.href = `/login?next=${encodeURIComponent(nextPath)}`;
    throw new Error("Unauthorized");
  }

  return response;
}

function normalizeProducts(value) {
  if (Array.isArray(value)) {
    return value
      .map((item) => String(item || "").trim())
      .filter(Boolean);
  }

  return String(value || "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function render() {
  renderSettings();
  renderSummary();
  renderTable();
  renderCompanyForm();
  renderDraft();
  renderGmailStatus();
  renderStorageStatus();
}

function renderSettings() {
  elements.senderName.value = state.settings.senderName;
  elements.senderCompany.value = state.settings.senderCompany;
  elements.senderEmail.value = state.settings.senderEmail;
  elements.productLibrary.value = state.settings.productLibrary.join(", ");
  elements.googleClientId.value = state.gmail.clientId;
  elements.draftMode.value = uiState.draftMode;
  elements.searchInput.value = uiState.search;

  Array.from(elements.filterRow.querySelectorAll("[data-filter]")).forEach((button) => {
    button.classList.toggle("is-active", button.dataset.filter === uiState.filter);
  });
}

function renderSummary() {
  const allCompanies = state.companies;
  const counts = {
    total: allCompanies.length,
    ready: allCompanies.filter((company) => getWorkflowStatus(company).key === "ready").length,
    due: allCompanies.filter((company) => getWorkflowStatus(company).key === "due").length,
    waiting: allCompanies.filter((company) => getWorkflowStatus(company).key === "waiting").length,
    replied: allCompanies.filter((company) => getWorkflowStatus(company).key === "replied").length,
  };

  const cards = [
    { label: "Total companies", value: counts.total },
    { label: "Ready for first touch", value: counts.ready },
    { label: "Follow-ups due", value: counts.due },
    { label: "Waiting on timer", value: counts.waiting },
    { label: "Replies received", value: counts.replied },
  ];

  elements.summaryStrip.innerHTML = cards
    .map(
      (card) => `
        <article class="summary-card">
          <p class="summary-card__label">${escapeHtml(card.label)}</p>
          <p class="summary-card__value">${card.value}</p>
        </article>
      `
    )
    .join("");
}

function renderTable() {
  const visibleCompanies = getVisibleCompanies();

  if (!visibleCompanies.length) {
    elements.companyTableBody.innerHTML = `
      <tr>
        <td colspan="5">
          <div class="empty-state">
            <strong>No companies in this view yet.</strong>
            Add a company, import a CSV, or switch filters to see more.
          </div>
        </td>
      </tr>
    `;
    return;
  }

  elements.companyTableBody.innerHTML = visibleCompanies
    .map((company) => {
      const workflow = getWorkflowStatus(company);
      const isSelected = company.id === uiState.selectedCompanyId;
      const productsMarkup = company.products.length
        ? `<div class="tag-list">${company.products.slice(0, 3).map((product) => `<span class="tag">${escapeHtml(product)}</span>`).join("")}</div>`
        : `<span class="muted">No product focus yet</span>`;

      return `
        <tr data-company-id="${company.id}" class="${isSelected ? "is-selected" : ""}">
          <td>
            <div class="company-meta">
              <strong>${escapeHtml(company.companyName || "Untitled company")}</strong>
              <span>${escapeHtml(company.contactEmail || "No email saved")}</span>
              <span>${escapeHtml([company.country, company.industry].filter(Boolean).join(" · ") || "Add country or industry")}</span>
            </div>
          </td>
          <td>${productsMarkup}</td>
          <td>
            <span class="status-badge status-badge--${workflow.key}">${escapeHtml(workflow.label)}</span>
          </td>
          <td>${escapeHtml(formatTimestamp(company.lastOutboundAt || company.lastInboundAt, "No activity yet"))}</td>
          <td>${escapeHtml(workflow.nextActionText)}</td>
        </tr>
      `;
    })
    .join("");
}

function renderCompanyForm() {
  const company = getSelectedCompany();
  const isExisting = Boolean(company);
  const record = company || createBlankCompany();

  elements.formTitle.textContent = isExisting ? record.companyName || "Selected company" : "Add a company";

  setFieldValue("companyId", record.id || "");
  setFieldValue("companyName", record.companyName);
  setFieldValue("contactName", record.contactName);
  setFieldValue("contactEmail", record.contactEmail);
  setFieldValue("country", record.country);
  setFieldValue("industry", record.industry);
  setFieldValue("application", record.application);
  setFieldValue("products", record.products.join(", "));
  setFieldValue("website", record.website);
  setFieldValue("accountState", record.accountState);
  setFieldValue("lastOutboundAt", toDatetimeLocalValue(record.lastOutboundAt));
  setFieldValue("lastInboundAt", toDatetimeLocalValue(record.lastInboundAt));
  setFieldValue("followUpCount", String(record.followUpCount || 0));
  setCheckboxValue("ignoreFollowUps", record.ignoreFollowUps);
  setFieldValue("notes", record.notes);

  elements.deleteCompanyButton.disabled = !isExisting;
}

function renderDraft() {
  const company = getSelectedCompany();
  if (!company) {
    elements.draftSummaryText.textContent = "Select a company to generate the next email based on reply status and follow-up timing.";
    elements.draftSubject.value = "";
    elements.draftBody.value = "";
    toggleDraftButtons(false);
    return;
  }

  const draft = buildDraft(company, uiState.draftMode);
  elements.draftSummaryText.textContent = draft.summary;
  elements.draftSubject.value = draft.subject;
  elements.draftBody.value = draft.body;
  toggleDraftButtons(Boolean(draft.subject || draft.body));
}

function renderGmailStatus(message) {
  if (message) {
    elements.gmailStatusText.textContent = message;
    return;
  }

  if (sessionState.isSyncing) {
    return;
  }

  if (state.gmail.lastSyncAt) {
    elements.gmailStatusText.textContent = `Last Gmail scan: ${formatTimestamp(state.gmail.lastSyncAt, "Not synced yet")}.`;
    return;
  }

  elements.gmailStatusText.textContent =
    "Add a Google web client ID, connect Gmail, then the app will read sent and reply timestamps for saved contacts. It never sends email automatically.";
}

function setStorageStatus(text, tone) {
  uiState.storageStatusText = text;
  uiState.storageStatusTone = tone || "saved";
  renderStorageStatus();
}

function renderStorageStatus() {
  if (!elements.storageStatusText) return;
  elements.storageStatusText.textContent = uiState.storageStatusText;
  elements.storageStatusText.className = `storage-indicator storage-indicator--${uiState.storageStatusTone}`;
}

function toggleDraftButtons(enabled) {
  elements.copySubjectButton.disabled = !enabled;
  elements.copyBodyButton.disabled = !enabled;
  elements.markSentButton.disabled = !enabled;
  elements.markReplyButton.disabled = !enabled;
}

function getSelectedCompany() {
  return state.companies.find((company) => company.id === uiState.selectedCompanyId) || null;
}

function createBlankCompany() {
  return {
    id: "",
    companyName: "",
    contactName: "",
    contactEmail: "",
    country: "",
    industry: "",
    application: "",
    products: [],
    website: "",
    accountState: "active",
    lastOutboundAt: "",
    lastInboundAt: "",
    followUpCount: 0,
    ignoreFollowUps: false,
    notes: "",
    gmailSyncedAt: "",
  };
}

function getVisibleCompanies() {
  const searchTerm = uiState.search.trim().toLowerCase();
  return [...state.companies]
    .filter((company) => {
      if (!matchesFilter(company, uiState.filter)) return false;
      if (!searchTerm) return true;
      const haystack = [
        company.companyName,
        company.contactName,
        company.contactEmail,
        company.country,
        company.industry,
        company.application,
        company.notes,
        company.products.join(" "),
      ]
        .join(" ")
        .toLowerCase();
      return haystack.includes(searchTerm);
    })
    .sort(sortCompanies);
}

function matchesFilter(company, filter) {
  if (filter === "all") return true;
  return getWorkflowStatus(company).key === filter;
}

function sortCompanies(a, b) {
  const statusPriority = {
    due: 0,
    ready: 1,
    waiting: 2,
    replied: 3,
    ignored: 4,
  };

  const workflowA = getWorkflowStatus(a);
  const workflowB = getWorkflowStatus(b);
  const priorityDelta = statusPriority[workflowA.key] - statusPriority[workflowB.key];
  if (priorityDelta !== 0) return priorityDelta;

  const dueA = workflowA.nextActionAt ? new Date(workflowA.nextActionAt).getTime() : Number.MAX_SAFE_INTEGER;
  const dueB = workflowB.nextActionAt ? new Date(workflowB.nextActionAt).getTime() : Number.MAX_SAFE_INTEGER;
  if (dueA !== dueB) return dueA - dueB;

  return (a.companyName || "").localeCompare(b.companyName || "");
}

function getWorkflowStatus(company) {
  const lastOutboundAt = company.lastOutboundAt ? new Date(company.lastOutboundAt) : null;
  const lastInboundAt = company.lastInboundAt ? new Date(company.lastInboundAt) : null;
  const hasReply = lastInboundAt && (!lastOutboundAt || lastInboundAt > lastOutboundAt);

  if (company.ignoreFollowUps || company.accountState === "closed" || company.accountState === "on_hold") {
    return {
      key: "ignored",
      label: company.accountState === "closed" ? "Closed" : company.accountState === "on_hold" ? "On hold" : "Ignored",
      nextActionText: "No follow-up scheduled",
      nextActionAt: "",
    };
  }

  if (hasReply || company.accountState === "interested") {
    return {
      key: "replied",
      label: company.accountState === "interested" ? "Interested" : "Replied",
      nextActionText: "Review reply and answer manually",
      nextActionAt: company.lastInboundAt,
    };
  }

  if (!lastOutboundAt) {
    return {
      key: "ready",
      label: "Ready",
      nextActionText: "Send first-touch email",
      nextActionAt: "",
    };
  }

  const waitDays = 3 + (Math.max(0, Number(company.followUpCount) || 0) * 2);
  const nextActionAt = addDays(lastOutboundAt, waitDays);
  const due = nextActionAt.getTime() <= Date.now();
  const nextFollowUpNumber = Math.max(1, Number(company.followUpCount) + 1);

  return {
    key: due ? "due" : "waiting",
    label: due ? `Follow-up ${nextFollowUpNumber} due` : "Waiting",
    nextActionText: due
      ? `Send follow-up ${nextFollowUpNumber}`
      : `Follow-up ${nextFollowUpNumber} on ${formatTimestamp(nextActionAt.toISOString(), "Pending")}`,
    nextActionAt: nextActionAt.toISOString(),
  };
}

function addDays(date, days) {
  const nextDate = new Date(date);
  nextDate.setDate(nextDate.getDate() + days);
  return nextDate;
}

function formatTimestamp(value, fallback = "") {
  if (!value) return fallback;
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return fallback;

  return new Intl.DateTimeFormat("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  }).format(date);
}

function toDatetimeLocalValue(value) {
  if (!value) return "";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "";

  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  const hours = String(date.getHours()).padStart(2, "0");
  const minutes = String(date.getMinutes()).padStart(2, "0");
  return `${year}-${month}-${day}T${hours}:${minutes}`;
}

function setFieldValue(id, value) {
  const field = document.querySelector(`#${id}`);
  if (field) field.value = value || "";
}

function setCheckboxValue(id, value) {
  const field = document.querySelector(`#${id}`);
  if (field) field.checked = Boolean(value);
}

function buildDraft(company, draftMode) {
  const workflow = getWorkflowStatus(company);
  const resolvedMode = draftMode === "auto" ? getAutoDraftMode(company) : draftMode;

  if (workflow.key === "ignored") {
    return {
      summary: `${company.companyName} is ignored for follow-ups. Turn off ignore or move the account back to active to resume drafts.`,
      subject: "",
      body: "",
    };
  }

  if (workflow.key === "replied" && draftMode === "auto") {
    return {
      summary: `${company.companyName} already replied. This company is out of the automatic follow-up queue until you decide the next manual step.`,
      subject: "",
      body: "",
    };
  }

  const firstName = getFirstName(company.contactName);
  const greeting = firstName ? `Hi ${firstName},` : `Hi ${company.companyName || "team"},`;
  const primaryProduct = company.products[0] || "industrial minerals";
  const productLine = joinList(company.products) || primaryProduct;
  const useCase = company.application || company.industry || "your production needs";
  const contextLine = buildContextLine(company);
  const valueCue = buildValueCue(company);
  const signature = buildSignature();
  const closeLine = company.contactName
    ? "Happy to send the closest grade suggestion if you share your current requirement."
    : "Happy to send the closest grade suggestion if this should go to another buyer on your team.";

  const templates = {
    first_touch: {
      summary: `${company.companyName} has not been contacted yet, so this draft is a first-touch email focused on ${productLine}.`,
      subject: `${primaryProduct} supply for ${useCase}`,
      body: [
        greeting,
        "",
        `I am reaching out from ${state.settings.senderCompany}. We support buyers looking for ${productLine.toLowerCase()} with ${valueCue}.`,
        contextLine,
        `If ${primaryProduct.toLowerCase()} is on your sourcing list, I can share available grades, packing options, and shipment support based on your current requirement.`,
        closeLine,
        "",
        signature,
      ].join("\n"),
    },
    follow_up_1: {
      summary: `${company.companyName} has an earlier outbound email and no reply yet. This is follow-up 1, timed 3 days after the last email.`,
      subject: `Following up on ${primaryProduct} for ${useCase}`,
      body: [
        greeting,
        "",
        `Just following up on my earlier note about ${productLine.toLowerCase()}.`,
        `We usually help buyers narrow the right fit around ${useCase.toLowerCase()}, especially when they need ${valueCue}.`,
        `If this is relevant, I can send a short spec match and packing overview for a quick review.`,
        "",
        signature,
      ].join("\n"),
    },
    follow_up_2: {
      summary: `${company.companyName} still shows no reply, so this is follow-up 2 with a 5 day gap from the last touch.`,
      subject: `Checking timing on ${primaryProduct} requirement`,
      body: [
        greeting,
        "",
        `Sharing a quick second follow-up in case my earlier email got buried.`,
        `For ${useCase.toLowerCase()}, we generally support buyers who want ${valueCue} and reliable export coordination.`,
        `If the timing is not right, feel free to tell me when to reconnect and I will work around your schedule.`,
        "",
        signature,
      ].join("\n"),
    },
    follow_up_3: {
      summary: `${company.companyName} is due for follow-up 3, which this workflow places 7 days after the latest outbound email.`,
      subject: `Can I send specs for ${primaryProduct}?`,
      body: [
        greeting,
        "",
        `I wanted to try once more regarding ${productLine.toLowerCase()} for ${useCase.toLowerCase()}.`,
        `If useful, I can send a concise note with grade range, packing format, and shipment support so you can check fit quickly.`,
        `If another colleague handles this category, I would appreciate being pointed in the right direction.`,
        "",
        signature,
      ].join("\n"),
    },
    follow_up_4: {
      summary: `${company.companyName} is due for follow-up 4, which this workflow places 9 days after the last email.`,
      subject: `Still relevant for ${primaryProduct}?`,
      body: [
        greeting,
        "",
        `One more follow-up from my side regarding ${productLine.toLowerCase()}.`,
        `If you are reviewing suppliers for ${useCase.toLowerCase()}, I can send a short requirement-fit note instead of a long introduction.`,
        `If this is not relevant right now, no issue at all. A quick note back will help me time future follow-ups better.`,
        "",
        signature,
      ].join("\n"),
    },
    nudge_close: {
      summary: `${company.companyName} is beyond follow-up 4, so this version is a clean final nudge.`,
      subject: `Closing the loop on ${primaryProduct}`,
      body: [
        greeting,
        "",
        `I will close the loop after this note.`,
        `If ${productLine.toLowerCase()} becomes relevant later for ${useCase.toLowerCase()}, I would be glad to reconnect with a tailored offer and shipment plan.`,
        `If someone else handles this internally, a short redirect would help.`,
        "",
        signature,
      ].join("\n"),
    },
  };

  return templates[resolvedMode] || templates.first_touch;
}

function getAutoDraftMode(company) {
  const workflow = getWorkflowStatus(company);
  if (workflow.key === "ready") return "first_touch";
  if (workflow.key === "ignored") return "nudge_close";
  if (workflow.key === "replied") return "nudge_close";

  const nextFollowUp = Math.max(1, Number(company.followUpCount) + 1);
  if (nextFollowUp === 1) return "follow_up_1";
  if (nextFollowUp === 2) return "follow_up_2";
  if (nextFollowUp === 3) return "follow_up_3";
  if (nextFollowUp === 4) return "follow_up_4";
  return "nudge_close";
}

function buildContextLine(company) {
  const parts = [];
  if (company.companyName) parts.push(`${company.companyName}`);
  if (company.industry) parts.push(`works in ${company.industry.toLowerCase()}`);
  if (company.country) parts.push(`in ${company.country}`);
  const joined = parts.join(" ");
  if (joined) {
    return `Your profile suggests ${joined}, which is why I thought this could be relevant.`;
  }
  return "I thought there could be a fit based on your trade activity and product profile.";
}

function buildValueCue(company) {
  const haystack = [company.industry, company.application, company.products.join(" ")].join(" ").toLowerCase();

  if (haystack.includes("ceramic")) {
    return "consistent particle sizing, low contamination, and steady kiln performance";
  }
  if (haystack.includes("construction")) {
    return "bulk availability, dependable gradation, and shipment planning";
  }
  if (haystack.includes("glass")) {
    return "high silica options, low iron focus, and export-ready lots";
  }
  if (haystack.includes("foundry")) {
    return "grain distribution control, low moisture, and stable bulk supply";
  }
  if (haystack.includes("paint")) {
    return "stable whiteness, controlled fineness, and predictable packing";
  }
  return "consistent specs, packing flexibility, and dependable export handling";
}

function buildSignature() {
  const lines = [state.settings.senderName || "Deep Mehta", state.settings.senderCompany || "Jade Waves Enterprise"];
  if (state.settings.senderEmail) lines.push(state.settings.senderEmail);
  return lines.join("\n");
}

function getFirstName(name) {
  return String(name || "")
    .trim()
    .split(/\s+/)
    .filter(Boolean)[0] || "";
}

function joinList(items) {
  if (!items || !items.length) return "";
  if (items.length === 1) return items[0];
  if (items.length === 2) return `${items[0]} and ${items[1]}`;
  return `${items.slice(0, -1).join(", ")}, and ${items[items.length - 1]}`;
}

function escapeHtml(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function handleCompanySubmit(event) {
  event.preventDefault();
  const formData = new FormData(elements.companyForm);
  const selectedCompany = getSelectedCompany();
  const company = normalizeCompany({
    id: formData.get("companyId") || generateId(),
    companyName: formData.get("companyName"),
    contactName: formData.get("contactName"),
    contactEmail: formData.get("contactEmail"),
    country: formData.get("country"),
    industry: formData.get("industry"),
    application: formData.get("application"),
    products: formData.get("products"),
    website: formData.get("website"),
    accountState: formData.get("accountState"),
    lastOutboundAt: datetimeLocalToIso(formData.get("lastOutboundAt")),
    lastInboundAt: datetimeLocalToIso(formData.get("lastInboundAt")),
    followUpCount: formData.get("followUpCount"),
    ignoreFollowUps: formData.get("ignoreFollowUps") === "on",
    notes: formData.get("notes"),
    gmailSyncedAt: selectedCompany ? selectedCompany.gmailSyncedAt : "",
  });

  const existingIndex = state.companies.findIndex((item) => item.id === company.id);
  if (existingIndex >= 0) {
    state.companies.splice(existingIndex, 1, company);
  } else {
    state.companies.push(company);
  }

  uiState.selectedCompanyId = company.id;
  saveState();
  render();
  showToast(`${company.companyName || "Company"} saved.`);
}

function datetimeLocalToIso(value) {
  if (!value) return "";
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? "" : date.toISOString();
}

function handleSettingsSubmit(event) {
  event.preventDefault();
  state.settings.senderName = elements.senderName.value.trim() || defaultState.settings.senderName;
  state.settings.senderCompany = elements.senderCompany.value.trim() || defaultState.settings.senderCompany;
  state.settings.senderEmail = elements.senderEmail.value.trim();
  state.settings.productLibrary = normalizeProducts(elements.productLibrary.value);
  state.gmail.clientId = elements.googleClientId.value.trim();
  saveState();
  render();
  showToast("Workspace settings saved.");
}

function startNewCompany() {
  uiState.selectedCompanyId = null;
  render();
  document.querySelector("#companyName").focus();
}

function resetSelectedForm() {
  render();
}

function deleteSelectedCompany() {
  const company = getSelectedCompany();
  if (!company) return;
  const confirmed = window.confirm(`Delete ${company.companyName || "this company"} from the CRM?`);
  if (!confirmed) return;

  state.companies = state.companies.filter((item) => item.id !== company.id);
  uiState.selectedCompanyId = null;
  saveState();
  render();
  showToast("Company deleted.");
}

function selectCompany(id) {
  uiState.selectedCompanyId = id;
  render();
}

function handleTableClick(event) {
  const row = event.target.closest("[data-company-id]");
  if (!row) return;
  selectCompany(row.dataset.companyId);
}

function handleFilterClick(event) {
  const button = event.target.closest("[data-filter]");
  if (!button) return;
  uiState.filter = button.dataset.filter;
  render();
}

function handleSearchInput(event) {
  uiState.search = event.target.value;
  renderTable();
}

function handleDraftModeChange(event) {
  uiState.draftMode = event.target.value;
  renderDraft();
}

async function copyToClipboard(value, successMessage) {
  if (!value) return;
  try {
    await navigator.clipboard.writeText(value);
    showToast(successMessage);
  } catch (error) {
    console.error(error);
    showToast("Clipboard access failed.");
  }
}

function markDraftSentNow() {
  const company = getSelectedCompany();
  if (!company) return;

  const workflow = getWorkflowStatus(company);
  const now = new Date().toISOString();

  if (workflow.key === "ready" || !company.lastOutboundAt) {
    company.followUpCount = 0;
  } else if (workflow.key === "replied") {
    company.followUpCount = 0;
  } else {
    company.followUpCount = Math.max(0, Number(company.followUpCount) || 0) + 1;
  }

  company.lastOutboundAt = now;
  company.gmailSyncedAt = "";
  saveState();
  render();
  showToast("Outbound touch marked as sent.");
}

function markReplyReceivedNow() {
  const company = getSelectedCompany();
  if (!company) return;

  company.lastInboundAt = new Date().toISOString();
  saveState();
  render();
  showToast("Reply marked as received.");
}

function exportData() {
  const payload = JSON.stringify(state, null, 2);
  downloadFile("jade-waves-crm-export.json", payload, "application/json");
  showToast("CRM export ready.");
}

function downloadFile(filename, content, mimeType) {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

function handleImportFile(event) {
  const [file] = event.target.files || [];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = () => {
    try {
      const importedCompanies = file.name.toLowerCase().endsWith(".json")
        ? parseJsonImport(String(reader.result || ""))
        : parseCsvImport(String(reader.result || ""));
      mergeImportedCompanies(importedCompanies);
      saveState();
      render();
      showToast(`${importedCompanies.length} companies imported.`);
    } catch (error) {
      console.error(error);
      showToast("Import failed. Check the file format.");
    } finally {
      elements.importFileInput.value = "";
    }
  };
  reader.readAsText(file);
}

function parseJsonImport(text) {
  const parsed = JSON.parse(text);
  const records = Array.isArray(parsed) ? parsed : parsed.companies || [];
  return records.map(normalizeCompany);
}

function parseCsvImport(text) {
  const rows = parseCsv(text);
  if (!rows.length) return [];
  const header = rows[0].map((value) => normalizeHeader(value));
  return rows.slice(1).filter((row) => row.some((value) => String(value || "").trim())).map((row) => {
    const record = {};
    header.forEach((key, index) => {
      record[key] = row[index] || "";
    });

    return normalizeCompany({
      companyName: record.company || record.companyname,
      contactName: record.contact || record.contactname,
      contactEmail: record.email || record.contactemail,
      country: record.country,
      industry: record.industry,
      application: record.application,
      products: record.products || record.productfocus,
      website: record.website,
      accountState: record.accountstate,
      notes: record.notes,
      followUpCount: record.followupcount,
      lastOutboundAt: record.lastoutboundat,
      lastInboundAt: record.lastinboundat,
      ignoreFollowUps: ["true", "yes", "1"].includes(String(record.ignorefollowups || "").toLowerCase()),
    });
  });
}

function normalizeHeader(value) {
  return String(value || "")
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "");
}

function mergeImportedCompanies(companies) {
  companies.forEach((company) => {
    const existingIndex = state.companies.findIndex((item) => {
      const emailMatch =
        item.contactEmail && company.contactEmail && item.contactEmail.toLowerCase() === company.contactEmail.toLowerCase();
      const companyMatch =
        item.companyName && company.companyName && item.companyName.toLowerCase() === company.companyName.toLowerCase();
      return emailMatch || companyMatch;
    });

    if (existingIndex >= 0) {
      state.companies.splice(existingIndex, 1, { ...state.companies[existingIndex], ...company, id: state.companies[existingIndex].id });
    } else {
      state.companies.push(company);
    }
  });

  if (!uiState.selectedCompanyId && state.companies[0]) {
    uiState.selectedCompanyId = state.companies[0].id;
  }
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;

  for (let index = 0; index < text.length; index += 1) {
    const char = text[index];
    const next = text[index + 1];

    if (char === '"') {
      if (inQuotes && next === '"') {
        field += '"';
        index += 1;
      } else {
        inQuotes = !inQuotes;
      }
      continue;
    }

    if (char === "," && !inQuotes) {
      row.push(field);
      field = "";
      continue;
    }

    if ((char === "\n" || char === "\r") && !inQuotes) {
      if (char === "\r" && next === "\n") index += 1;
      row.push(field);
      rows.push(row);
      row = [];
      field = "";
      continue;
    }

    field += char;
  }

  if (field.length || row.length) {
    row.push(field);
    rows.push(row);
  }

  return rows;
}

async function connectGmail() {
  state.gmail.clientId = elements.googleClientId.value.trim();
  if (!state.gmail.clientId) {
    showToast("Add your Google OAuth client ID first.");
    return;
  }

  saveState();
  try {
    await ensureGmailToken(true);
    renderGmailStatus("Gmail connected. You can now scan saved emails.");
    showToast("Gmail connected.");
  } catch (error) {
    console.error(error);
    renderGmailStatus("Gmail connection failed. Recheck the client ID and authorized origin.");
    showToast("Unable to connect Gmail.");
  }
}

async function refreshInboxScan() {
  const companiesWithEmails = state.companies.filter((company) => company.contactEmail);
  if (!companiesWithEmails.length) {
    showToast("Add at least one company with an email first.");
    return;
  }

  try {
    sessionState.isSyncing = true;
    renderGmailStatus("Connecting to Gmail...");
    await ensureGmailToken(false);

    for (let index = 0; index < companiesWithEmails.length; index += 1) {
      const company = companiesWithEmails[index];
      renderGmailStatus(`Scanning ${index + 1} of ${companiesWithEmails.length}: ${company.companyName || company.contactEmail}`);
      await syncCompanyWithGmail(company);
      saveLocalCache();
    }

    state.gmail.lastSyncAt = new Date().toISOString();
    saveState();
    render();
    showToast("Inbox scan complete.");
  } catch (error) {
    console.error(error);
    renderGmailStatus("Inbox scan failed. Reconnect Gmail and try again.");
    showToast("Unable to scan Gmail.");
  } finally {
    sessionState.isSyncing = false;
    render();
  }
}

function ensureGmailToken(forceConsent) {
  if (sessionState.gmailToken && !forceConsent) {
    return Promise.resolve(sessionState.gmailToken);
  }

  if (!state.gmail.clientId) {
    return Promise.reject(new Error("Missing Google client ID"));
  }

  if (!window.google || !window.google.accounts || !window.google.accounts.oauth2) {
    return Promise.reject(new Error("Google Identity Services not loaded"));
  }

  return new Promise((resolve, reject) => {
    sessionState.tokenClient = window.google.accounts.oauth2.initTokenClient({
      client_id: state.gmail.clientId,
      scope: GMAIL_SCOPE,
      callback: (response) => {
        if (response.error) {
          reject(new Error(response.error));
          return;
        }

        sessionState.gmailToken = response.access_token;
        resolve(response.access_token);
      },
    });

    sessionState.tokenClient.requestAccessToken({ prompt: forceConsent || !sessionState.gmailToken ? "consent" : "" });
  });
}

async function syncCompanyWithGmail(company) {
  const sentSummary = await gmailMessageSummary(`in:sent to:"${company.contactEmail}"`);
  const inboundSummary = await gmailMessageSummary(`from:"${company.contactEmail}"`);

  if (sentSummary.latestAt) {
    company.lastOutboundAt = sentSummary.latestAt;
    company.followUpCount = Math.max(0, sentSummary.count - 1);
  }

  if (inboundSummary.latestAt) {
    company.lastInboundAt = inboundSummary.latestAt;
  }

  company.gmailSyncedAt = new Date().toISOString();
}

async function gmailMessageSummary(query) {
  const list = await gmailFetch(`/gmail/v1/users/me/messages?q=${encodeURIComponent(query)}&maxResults=5`);
  const messages = Array.isArray(list.messages) ? list.messages : [];
  if (!messages.length) {
    return {
      count: 0,
      latestAt: "",
    };
  }

  const details = await Promise.all(
    messages.map((message) => gmailFetch(`/gmail/v1/users/me/messages/${message.id}?format=metadata`))
  );
  const timestamps = details.map((detail) => Number(detail.internalDate || 0)).filter(Boolean);

  return {
    count: Number(list.resultSizeEstimate) || messages.length,
    latestAt: timestamps.length ? new Date(Math.max(...timestamps)).toISOString() : "",
  };
}

async function gmailFetch(path) {
  const response = await fetch(`https://gmail.googleapis.com${path}`, {
    headers: {
      Authorization: `Bearer ${sessionState.gmailToken}`,
    },
  });

  if (response.status === 401) {
    sessionState.gmailToken = "";
    throw new Error("Unauthorized Gmail token");
  }

  if (!response.ok) {
    throw new Error(`Gmail request failed with ${response.status}`);
  }

  return response.json();
}

function showToast(message) {
  const existingToast = document.querySelector(".toast");
  if (existingToast) existingToast.remove();

  const toast = document.createElement("div");
  toast.className = "toast";
  toast.textContent = message;
  document.body.appendChild(toast);
  window.setTimeout(() => toast.remove(), 2400);
}

function generateId() {
  if (window.crypto && typeof window.crypto.randomUUID === "function") {
    return window.crypto.randomUUID();
  }
  return `crm-${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function wireEvents() {
  elements.companyForm.addEventListener("submit", handleCompanySubmit);
  elements.settingsForm.addEventListener("submit", handleSettingsSubmit);
  elements.companyTableBody.addEventListener("click", handleTableClick);
  elements.filterRow.addEventListener("click", handleFilterClick);
  elements.searchInput.addEventListener("input", handleSearchInput);
  elements.newCompanyButton.addEventListener("click", startNewCompany);
  elements.deleteCompanyButton.addEventListener("click", deleteSelectedCompany);
  elements.resetFormButton.addEventListener("click", resetSelectedForm);
  elements.syncAllButton.addEventListener("click", refreshInboxScan);
  elements.gmailConnectButton.addEventListener("click", connectGmail);
  elements.gmailRefreshButton.addEventListener("click", refreshInboxScan);
  elements.importFileInput.addEventListener("change", handleImportFile);
  elements.exportDataButton.addEventListener("click", exportData);
  elements.draftMode.addEventListener("change", handleDraftModeChange);
  elements.copySubjectButton.addEventListener("click", () => copyToClipboard(elements.draftSubject.value, "Subject copied."));
  elements.copyBodyButton.addEventListener("click", () => copyToClipboard(elements.draftBody.value, "Email copied."));
  elements.markSentButton.addEventListener("click", markDraftSentNow);
  elements.markReplyButton.addEventListener("click", markReplyReceivedNow);
}

function initSelection() {
  if (!state.companies.length) {
    uiState.selectedCompanyId = null;
    return;
  }
  if (!uiState.selectedCompanyId || !state.companies.some((company) => company.id === uiState.selectedCompanyId)) {
    uiState.selectedCompanyId = state.companies[0].id;
  }
}

async function bootApp() {
  const cachedState = normalizeState(state);
  initSelection();
  render();

  try {
    const serverState = await fetchServerState();
    const serverHasData = hasMeaningfulData(serverState);
    const cachedHasData = hasMeaningfulData(cachedState);

    if (!serverHasData && cachedHasData) {
      state = cachedState;
      initSelection();
      render();
      setStorageStatus("Loaded browser backup. Saving it to secure cloud storage now...", "saving");
      await saveState();
      return;
    }

    state = serverState;
    initSelection();
    saveLocalCache();
    render();
    setStorageStatus("CRM connected. Data now loads and saves from secure cloud storage automatically.", "saved");
  } catch (error) {
    console.error(error);
    state = cachedState;
    initSelection();
    render();

    if (hasMeaningfulData(cachedState)) {
      setStorageStatus("Cloud sync is offline. Using the browser backup until secure storage is back.", "warning");
    } else {
      setStorageStatus("Cloud sync is offline. Sign in again once the hosted app is reachable.", "warning");
    }
  }
}

wireEvents();
bootApp();
