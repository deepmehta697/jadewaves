const productData = {
  silica: {
    eyebrow: "Glass / Ceramics / Foundry",
    title: "Quartz / Silica Series",
    copy:
      "High-purity quartz, silica sand, and silica flour positioned for glass, ceramics, foundry, engineered surfaces, and industrial manufacturing where grain control and consistency matter.",
    tags: ["Glass grade", "Custom sizing", "Ceramics", "Foundry use"],
    notes: [
      "Consistency over commodity pricing.",
      "Prepared for industrial production lines.",
      "Quoted with export-ready clarity.",
    ],
    stageClass: "stage-silica",
  },
  bentonite: {
    eyebrow: "Absorbency / Refining / Drilling",
    title: "Bentonite / Activated Clay",
    copy:
      "Sodium bentonite and activated bleaching earth are positioned around absorbency, swelling behavior, drilling support, decolorizing performance, and refinery-linked applications.",
    tags: ["Montmorillonite", "Oil refining", "Water treatment", "Drilling use"],
    notes: [
      "Built around functional performance.",
      "Useful across treatment and refining contexts.",
      "Presented as a process-aware material line.",
    ],
    stageClass: "stage-bentonite",
  },
  cementitious: {
    eyebrow: "Concrete / Cement / Abrasives",
    title: "Fly Ash / Copper Slag",
    copy:
      "Class F fly ash and copper slag extend the portfolio into concrete systems, cement inputs, abrasive applications, lightweight aggregate, and partial river sand replacement use cases.",
    tags: ["Class F", "Concrete", "Abrasives", "Cement raw mix"],
    notes: [
      "Made for infrastructure-heavy buying decisions.",
      "Strong fit where substitution and performance matter.",
      "Commercially framed for large-volume export flow.",
    ],
    stageClass: "stage-cementitious",
  },
  process: {
    eyebrow: "Ceramics / Chemical / Process Minerals",
    title: "Kaolin / Salt",
    copy:
      "Kaolin, salt, and adjacent process minerals support ceramics, chemicals, fillers, and broad industrial use cases where cleaner handling and dependable shipment timing drive supplier choice.",
    tags: ["Ceramics", "Chemical use", "Industrial grade", "Export packed"],
    notes: [
      "Simple portfolio, broad industrial reach.",
      "Better framed around handling and reliability.",
      "Suitable for repeat export relationships.",
    ],
    stageClass: "stage-process",
  },
};

const header = document.querySelector(".site-header");
const revealElements = document.querySelectorAll(".reveal");
const heroStage = document.querySelector("[data-hero-stage]");
const heroFloats = document.querySelectorAll("[data-hero-float]");
const stage = document.getElementById("product-stage");
const selectorButtons = document.querySelectorAll(".selector-button");
const stageEyebrow = document.getElementById("stage-eyebrow");
const stageTitle = document.getElementById("stage-title");
const stageCopy = document.getElementById("stage-copy");
const stageTags = document.getElementById("stage-tags");
const stageNoteA = document.getElementById("stage-note-a");
const stageNoteB = document.getElementById("stage-note-b");
const stageNoteC = document.getElementById("stage-note-c");
const inquiryForm = document.getElementById("inquiry-form");
const formNote = document.getElementById("form-note");

const updateHeaderState = () => {
  if (!header) return;
  header.classList.toggle("is-scrolled", window.scrollY > 20);
};

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
      }
    });
  },
  { threshold: 0.14 }
);

revealElements.forEach((element) => {
  revealObserver.observe(element);
});

const setProduct = (key) => {
  const data = productData[key];

  if (
    !data ||
    !stage ||
    !stageEyebrow ||
    !stageTitle ||
    !stageCopy ||
    !stageTags ||
    !stageNoteA ||
    !stageNoteB ||
    !stageNoteC
  ) {
    return;
  }

  stageEyebrow.textContent = data.eyebrow;
  stageTitle.textContent = data.title;
  stageCopy.textContent = data.copy;
  stageNoteA.textContent = data.notes[0];
  stageNoteB.textContent = data.notes[1];
  stageNoteC.textContent = data.notes[2];

  Object.values(productData).forEach((product) => {
    stage.classList.remove(product.stageClass);
  });
  stage.classList.add(data.stageClass);

  stageTags.innerHTML = "";
  data.tags.forEach((tag) => {
    const pill = document.createElement("span");
    pill.className =
      "rounded-full border border-black/10 bg-white/60 px-4 py-2 text-sm font-medium text-black/70 backdrop-blur-md";
    pill.textContent = tag;
    stageTags.appendChild(pill);
  });

  selectorButtons.forEach((button) => {
    const isActive = button.dataset.product === key;
    button.classList.toggle("is-active", isActive);
    button.setAttribute("aria-selected", String(isActive));
  });
};

selectorButtons.forEach((button) => {
  const activate = () => setProduct(button.dataset.product);
  button.addEventListener("click", activate);
  button.addEventListener("mouseenter", activate);
  button.addEventListener("focus", activate);
});

const syncHeroMotion = () => {
  if (!heroStage) return;

  const rect = heroStage.getBoundingClientRect();
  const distance = Math.min(Math.max((window.innerHeight - rect.top) / window.innerHeight, 0), 1.4);
  const lift = distance * 22;

  heroFloats.forEach((element, index) => {
    const direction = index % 2 === 0 ? -1 : 1;
    element.style.transform = `translate3d(0, ${lift * direction}px, 0)`;
  });
};

if (inquiryForm && formNote) {
  inquiryForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(inquiryForm);
    const material = formData.get("material")?.toString().trim() || "Material";
    const application =
      formData.get("application")?.toString().trim() || "Industrial use";
    const volume = formData.get("volume")?.toString().trim() || "TBD";
    const incoterm = formData.get("incoterm")?.toString().trim() || "TBD";
    const name = formData.get("name")?.toString().trim() || "Buyer";
    const email = formData.get("email")?.toString().trim() || "Not provided";

    const subject = encodeURIComponent(`Inquiry for ${material}`);
    const body = encodeURIComponent(
      [
        "Hello Jade Waves Enterprise,",
        "",
        `I would like a quote for: ${material}`,
        `Application: ${application}`,
        `Volume: ${volume}`,
        `Preferred incoterm: ${incoterm}`,
        "",
        `Name: ${name}`,
        `Email: ${email}`,
      ].join("\n")
    );

    formNote.textContent =
      "Opening your mail client with a prepared inquiry draft.";
    window.location.href = `mailto:deep@jadewavesenterprise.com?subject=${subject}&body=${body}`;
  });
}

updateHeaderState();
setProduct("silica");
syncHeroMotion();

window.addEventListener("scroll", () => {
  updateHeaderState();
  syncHeroMotion();
});

window.addEventListener("resize", syncHeroMotion);
