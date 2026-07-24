/* AZBY Family — Portfolio Review: tiered master template deck.
 * Ionic Wealth house style (extracted palette + logo). Dummy/illustrative data.
 * Tiers: RM CORE (green) · STANDARD (indigo) · UHNI family office (amber) · APPENDIX (slate).
 * Build: node build_deck.js  ->  AZBY_Portfolio_Review_Template.pptx
 */
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const D = JSON.parse(fs.readFileSync(path.join(__dirname, "azby_data.json")));
const C = D.palette;                       // hex strings, no '#'
const F = "Calibri";
const CH = (n) => path.join(__dirname, "assets", "charts", n + ".png");
const LOGO = path.join(__dirname, "assets", "ionic_logo.png");
const LOGO_W = path.join(__dirname, "assets", "ionic_logo_white.png");
const LOGO_AR = 68 / 391;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";               // 13.33 x 7.5 in
pres.author = "Ionic Wealth";
pres.company = "Ionic Wealth";

// derived numbers
const M = D.meta, PL = D.plan, CON = D.concentration;
const foreignBook = ((D.fund_cat["International"] || 0) / 100 * M.fund_l / M.book_l * 100);
const goldBook = ((D.fund_cat["Commodity-Gold FoF"] || 0) / 100 * M.fund_l / M.book_l * 100);
const foreignOfEq = foreignBook * M.book_l / M.equity_l; // rough: intl funds vs equity sleeve
let page = 0;

// ---------- helpers --------------------------------------------------------
const TIER = {
  RM:   { t: "RM · CORE",             fill: C.green,  col: "FFFFFF", w: 1.35 },
  STD:  { t: "STANDARD",              fill: C.indigo, col: "FFFFFF", w: 1.35 },
  UHNI: { t: "UHNI · FAMILY OFFICE",  fill: C.amber,  col: C.navy,   w: 2.15 },
  APX:  { t: "APPENDIX",              fill: C.slate,  col: "FFFFFF", w: 1.35 },
};
function chip(s, tier) {
  const c = TIER[tier];
  s.addText(c.t, { x: 12.78 - c.w, y: 0.42, w: c.w, h: 0.32, fontSize: 9.5, bold: true,
    color: c.col, fill: { color: c.fill }, align: "center", valign: "middle",
    shape: pres.ShapeType.roundRect, rectRadius: 0.16, fontFace: F, margin: 0, charSpacing: 1 });
}
function footer(s) {
  page += 1;
  s.addText(`${M.family} · illustrative template · Ionic Wealth`,
    { x: 0.55, y: 7.06, w: 8, h: 0.3, fontSize: 8, color: C.slate, fontFace: F, margin: 0 });
  s.addText("Private & Confidential", { x: 9.0, y: 7.06, w: 3.2, h: 0.3, fontSize: 8,
    color: C.slate, fontFace: F, align: "right", margin: 0 });
  s.addText(String(page), { x: 12.35, y: 7.06, w: 0.45, h: 0.3, fontSize: 8, color: C.slate,
    fontFace: F, align: "right", margin: 0 });
}
function head(title, sub, tier) {
  const s = pres.addSlide();
  s.background = { color: "FFFFFF" };
  s.addImage({ path: LOGO, x: 0.55, y: 0.36, w: 1.4, h: 1.4 * LOGO_AR });
  s.addText(title, { x: 0.55, y: 0.62, w: 9.6, h: 0.6, fontSize: 27, bold: true, color: C.navy,
    fontFace: F, margin: 0, valign: "middle" });
  if (sub) s.addText(sub, { x: 0.57, y: 1.2, w: 11.2, h: 0.38, fontSize: 14, color: C.slate,
    fontFace: F, margin: 0 });
  if (tier) chip(s, tier);
  footer(s);
  return s;
}
function chart(s, name, x, y, w, h) {
  s.addImage({ path: CH(name), x, y, sizing: { type: "contain", w, h } });
}
function kpi(s, x, y, w, value, label, color) {
  s.addText([
    { text: value + "\n", options: { fontSize: 23, bold: true, color: color || C.navy } },
    { text: label, options: { fontSize: 10.5, color: C.slate } },
  ], { x, y, w, h: 1.3, align: "center", valign: "middle", fontFace: F,
       fill: { color: C.near }, shape: pres.ShapeType.roundRect, rectRadius: 0.08, margin: 4, lineSpacingMultiple: 1.0 });
}
// simple styled table
function table(s, rows, x, y, w, colW, opts = {}) {
  const fs_ = opts.fontSize || 11;
  s.addTable(rows, {
    x, y, w, colW, fontFace: F, fontSize: fs_, color: C.navy, valign: "middle",
    border: { type: "solid", color: "FFFFFF", pt: opts.borderpt || 2 },
    rowH: opts.rowH || 0.3, autoPage: false, ...(opts.tableOpts || {}),
  });
}
function hcell(t, align = "left") {
  return { text: t, options: { bold: true, color: "FFFFFF", fill: { color: C.navy }, align, fontSize: 10.5 } };
}
function cell(t, o = {}) { return { text: t, options: { align: "left", ...o } }; }
function callBadge(call) {
  return { text: call, options: { bold: true, align: "center",
    color: call === "Sell" ? C.red : (call === "Hold" ? C.green : C.slate) } };
}
function bullets(items) {
  return items.map((t, i) => ({ text: t, options: { bullet: { code: "2022", indent: 14 },
    breakLine: true, paraSpaceAfter: 6, fontSize: 13, color: C.navy } }));
}
function zebra(rows, startFill = C.near) {
  rows.forEach((r, i) => { if (i === 0) return;
    const f = i % 2 ? "FFFFFF" : startFill;
    r.forEach(c => { c.options = c.options || {}; if (!c.options.fill) c.options.fill = { color: f }; });
  });
  return rows;
}

// ============================ SLIDES =======================================

// 1 — COVER -----------------------------------------------------------------
(() => {
  const s = pres.addSlide(); s.background = { color: C.navy };
  // amber ring motif (echoes the logo 'O'), large, top-right
  s.addShape(pres.ShapeType.donut, { x: 9.7, y: -1.1, w: 4.6, h: 4.6, fill: { color: C.amber, transparency: 82 }, line: { type: "none" } });
  s.addShape(pres.ShapeType.donut, { x: 11.0, y: 3.9, w: 3.2, h: 3.2, fill: { color: C.indigo2, transparency: 84 }, line: { type: "none" } });
  s.addImage({ path: LOGO_W, x: 0.7, y: 0.62, w: 1.9, h: 1.9 * LOGO_AR });
  s.addText("Co-founder in your journey of wealth creation", { x: 0.72, y: 1.02, w: 6, h: 0.3,
    fontSize: 11, color: C.indigo_t, fontFace: F, italic: true, margin: 0 });
  s.addText("Portfolio Review", { x: 0.7, y: 2.7, w: 11, h: 1.0, fontSize: 52, bold: true,
    color: "FFFFFF", fontFace: F, margin: 0 });
  s.addText("PREPARED FOR", { x: 0.72, y: 3.95, w: 6, h: 0.3, fontSize: 12, color: C.amber,
    fontFace: F, charSpacing: 3, margin: 0 });
  s.addText(M.family, { x: 0.7, y: 4.25, w: 9, h: 0.7, fontSize: 34, bold: true, color: "FFFFFF",
    fontFace: F, margin: 0 });
  s.addText(`₹${M.book_cr} Cr reviewed   ·   As of ${M.as_of}   ·   Ionic Wealth NDPMS Desk`,
    { x: 0.72, y: 5.15, w: 11, h: 0.4, fontSize: 14, color: C.indigo_t, fontFace: F, margin: 0 });
  s.addText("Illustrative template — AZBY Family is fictional; all holdings are dummy data for template design.",
    { x: 0.72, y: 6.7, w: 11.8, h: 0.3, fontSize: 9.5, color: C.slate, fontFace: F, margin: 0 });
})();

// 2 — CONTENTS --------------------------------------------------------------
(() => {
  const s = head("Contents", "A decision-first review, tiered for the audience in the room", null);
  const secs = [
    ["01", "Foundations", "IPS · gaps up front · mandate · how we score"],
    ["02", "The Portfolio", "snapshot · concentration · sector & cap"],
    ["03", "Direct Equity", "the book scored · spotlights · the sells · quality"],
    ["04", "Mutual Funds", "the fund book · how we evaluate · fund actions"],
    ["05", "The Plan", "house-view fit · cost · tax · deployment · order sheet"],
    ["06", "Growth & Frontier", "opportunity set · projection"],
    ["07", "Family Office", "consolidation · governance · goal funding"],
    ["A",  "Appendix", "chart library · registers · methodology"],
  ];
  let y = 1.85;
  secs.forEach(([n, t, d]) => {
    s.addText(n, { x: 0.6, y, w: 0.7, h: 0.5, fontSize: 20, bold: true, color: C.amber, fontFace: F, margin: 0, valign: "middle" });
    s.addText(t, { x: 1.35, y, w: 3.6, h: 0.5, fontSize: 16, bold: true, color: C.navy, fontFace: F, margin: 0, valign: "middle" });
    s.addText(d, { x: 5.0, y, w: 7.5, h: 0.5, fontSize: 12.5, color: C.slate, fontFace: F, margin: 0, valign: "middle" });
    y += 0.56;
  });
  // tier legend
  s.addShape(pres.ShapeType.rect, { x: 0.6, y: 6.45, w: 12.1, h: 0.02, fill: { color: C.grid }, line: { type: "none" } });
  const leg = [["RM · CORE", C.green], ["STANDARD", C.indigo], ["UHNI", C.amber], ["APPENDIX", C.slate]];
  let lx = 0.6;
  s.addText("Tiers →", { x: lx, y: 6.62, w: 0.9, h: 0.3, fontSize: 11, bold: true, color: C.navy, fontFace: F, margin: 0 });
  lx = 1.5;
  const legTxt = ["always show", "add analytics", "family office", "on demand"];
  leg.forEach(([t, c], i) => {
    s.addShape(pres.ShapeType.roundRect, { x: lx, y: 6.62, w: 0.28, h: 0.28, fill: { color: c }, line: { type: "none" }, rectRadius: 0.06 });
    s.addText(`${t} — ${legTxt[i]}`, { x: lx + 0.34, y: 6.6, w: 2.9, h: 0.32, fontSize: 10.5, color: C.slate, fontFace: F, margin: 0, valign: "middle" });
    lx += 2.85;
  });
})();

// ------- SECTION DIVIDER helper --------------------------------------------
function divider(num, title, tagline, items) {
  const s = pres.addSlide(); s.background = { color: C.navy };
  s.addImage({ path: LOGO_W, x: 0.6, y: 0.55, w: 1.5, h: 1.5 * LOGO_AR });
  s.addShape(pres.ShapeType.donut, { x: 10.8, y: 4.2, w: 3.4, h: 3.4, fill: { color: C.amber, transparency: 84 }, line: { type: "none" } });
  s.addText(`SECTION ${num}`, { x: 0.62, y: 2.5, w: 6, h: 0.4, fontSize: 14, color: C.amber, fontFace: F, charSpacing: 3, margin: 0 });
  s.addText(title, { x: 0.6, y: 2.9, w: 10, h: 1.0, fontSize: 44, bold: true, color: "FFFFFF", fontFace: F, margin: 0 });
  s.addText(tagline, { x: 0.62, y: 4.0, w: 9.5, h: 0.5, fontSize: 15, color: C.indigo_t, fontFace: F, italic: true, margin: 0 });
  if (items) s.addText(items.map((t) => ({ text: t, options: { breakLine: true, paraSpaceAfter: 4 } })),
    { x: 0.62, y: 4.8, w: 9, h: 1.6, fontSize: 12.5, color: "FFFFFF", fontFace: F, margin: 0 });
  footer(s);
}

// ============ SECTION 01 — FOUNDATIONS =====================================
divider("01", "Foundations", "Who the family is, the standard we hold the book to, and how we score.",
  ["Investment Policy Statement", "Where you stand vs your policy", "Mandate & method", "How we score a stock"]);

// 3 — IPS -------------------------------------------------------------------
(() => {
  const s = head("Investment Policy Statement", "The standard we hold this book to — standardised by risk profile", "RM");
  // left policy strip
  const pol = [
    ["Risk profile", "Aggressive"],
    ["Time horizon", "Long term (7+ years)"],
    ["Primary objective", "Long-term wealth creation"],
    ["Return objective", "Real growth above inflation"],
    ["Liquidity need", "Low near-term; buffer staged"],
    ["Mandate", "Non-discretionary (NDPMS)"],
    ["Construction", "Core–satellite"],
    ["Review cadence", "Quarterly refresh"],
  ];
  const prows = pol.map(([a, b]) => [
    { text: a, options: { color: C.slate, fontSize: 11 } },
    { text: b, options: { bold: true, color: C.navy, fontSize: 11, align: "right" } },
  ]);
  table(s, prows, 0.55, 1.85, 4.5, [2.5, 2.0], { rowH: 0.33, fontSize: 11 });
  s.addText("The mandate", { x: 0.55, y: 1.62, w: 4.5, h: 0.25, fontSize: 12, bold: true, color: C.indigo, fontFace: F, margin: 0 });

  // right — SAA template
  s.addText("Strategic asset allocation — by risk profile", { x: 5.4, y: 1.62, w: 7.3, h: 0.25, fontSize: 12, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  const saa = [
    [hcell("Sleeve"), hcell("Conservative", "center"), hcell("Moderate", "center"), hcell("Aggressive ▸", "center")],
    ...[
      ["Domestic equity", "25–35%", "45–55%", "55–70%"],
      ["Foreign equity", "5–10%", "10–20%", "~25% of eq"],
      ["Gold & silver", "5–10%", "5–10%", "5–10%"],
      ["Debt / arbitrage", "45–60%", "20–35%", "5–15%"],
      ["Style tilt", "low-vol", "low-vol+value", "low-vol+value"],
      ["Single-name limit", "<5%", "<6%", "<8% of eq"],
      ["Single-AMC limit", "<25%", "<25%", "<25%"],
      ["Single-sector limit", "<25%", "<30%", "<30%"],
    ].map((r) => [cell(r[0], { fontSize: 10.5 }), cell(r[1], { align: "center", color: C.slate, fontSize: 10.5 }),
      cell(r[2], { align: "center", color: C.slate, fontSize: 10.5 }),
      cell(r[3], { align: "center", bold: true, color: C.navy, fontSize: 10.5, fill: { color: C.tint_indigo } })]),
  ];
  table(s, saa, 5.4, 1.85, 7.3, [2.1, 1.7, 1.7, 1.8], { rowH: 0.34, fontSize: 10.5 });
  s.addText("The Aggressive column is this family's policy; limits reuse the house guidelines applied throughout this review.",
    { x: 5.4, y: 5.35, w: 7.3, h: 0.4, fontSize: 10, italic: true, color: C.slate, fontFace: F, margin: 0 });

  // understanding block
  s.addText("Our understanding of the family", { x: 0.55, y: 5.15, w: 4.5, h: 0.25, fontSize: 12, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText("First-generation promoter family; primary wealth from an operating business. Comfortable with equity risk and a long horizon, with a partial liquidity event anticipated. Priorities: compounding the core, reducing single-name risk, and building the diversifiers the book currently lacks.",
    { x: 0.55, y: 5.4, w: 4.6, h: 1.5, fontSize: 10.5, color: C.navy, fontFace: F, margin: 0 });
})();

// 4 — WHERE YOU STAND (gap board) -------------------------------------------
(() => {
  const s = head("Where you stand vs your policy", "Five gaps to close, one strength to keep — surfaced up front", "RM");
  const rows = [
    [hcell("Policy standard"), hcell("Where you are today"), hcell("Status", "center")],
    ...[
      [`Single-name < 8% of equity`, `${CON.largest_name} ${CON.largest_sleeve}%; top-10 ${CON.top10}% of book`, "GAP"],
      [`Single-AMC < 25% (funds)`, `Largest fund house ${CON.largest_amc}%`, "GAP"],
      [`Foreign equity ~25% of equity`, `~${foreignBook.toFixed(1)}% of book, developed-market light`, "GAP"],
      [`Gold & silver 5–10% sleeve`, `~${goldBook.toFixed(1)}% (a residual gold FoF), no sized sleeve`, "GAP"],
      [`Every holding scores ≥ 40`, `${D.below40} of ${M.n_stocks} stocks score < 40 (${CON.sell_wt}% by value)`, "GAP"],
      [`Funds beat benchmark over 3Y`, `Every seasoned fund beats its benchmark`, "STRENGTH"],
    ].map((r) => [cell(r[0], { fontSize: 12 }), cell(r[1], { fontSize: 12, color: C.navy }),
      { text: r[2], options: { align: "center", bold: true, color: r[2] === "STRENGTH" ? C.green : C.amber } }]),
  ];
  zebra(rows);
  table(s, rows, 0.55, 1.95, 12.2, [3.6, 6.6, 2.0], { rowH: 0.62, fontSize: 12 });
  s.addText("The executive summary attaches an action to each gap. Statuses use the house guidelines in the IPS.",
    { x: 0.55, y: 6.55, w: 12, h: 0.3, fontSize: 10.5, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 5 — EXECUTIVE SUMMARY ------------------------------------------------------
(() => {
  const s = head("Executive summary", "A sound core carrying avoidable concentration — five gaps, five actions", "RM");
  kpi(s, 0.55, 1.72, 2.85, `₹${M.book_cr} Cr`, "total reviewed", C.navy);
  kpi(s, 3.55, 1.72, 2.85, `${M.n_stocks} / ${M.n_funds}`, "stocks / schemes", C.navy);
  kpi(s, 6.55, 1.72, 2.85, `${CON.top10}%`, "top-10 weight", C.amber);
  kpi(s, 9.55, 1.72, 3.15, `${D.below40} of ${M.n_stocks}`, "rated Sell", C.red);
  const rows = [
    [hcell("Gap we found"), hcell("Action that closes it"), hcell("Impact")],
    ...[
      [`Top-10 ${CON.top10}%; ${CON.largest_name} at the single-name limit`, "Trim toward < 8% of equity", `frees ₹${PL.titan_trim_l} L; largest name within limit`],
      [`${D.below40} stocks score < 40, incl. ${D.spot_sell.name.split(" ")[0]} at ${D.spot_sell.score}`, "Run the Sell programme", `₹${PL.sells_cr} Cr proceeds; Sell-weight → 0%`],
      [`Foreign equity ~${foreignBook.toFixed(1)}% vs ~25% target`, "Redeploy toward foreign equity (direction)", "steps toward the target, 60:40 DM:EM"],
      [`No sized gold / silver sleeve`, "Open a small 75:25 sleeve (direction)", "adds the missing diversifier"],
      [`Funds: AMC ${CON.largest_amc}%, a Regular-plan duplicate, sub-scale 2nd small-cap`, "Switch / redeem / exit — 3 structural actions", `${M.n_funds} → ${M.n_funds - 2} schemes`],
    ].map((r) => [cell(r[0], { fontSize: 11.5 }), cell(r[1], { fontSize: 11.5, bold: true, color: C.navy }), cell(r[2], { fontSize: 11.5, color: C.slate })]),
  ];
  zebra(rows);
  table(s, rows, 0.55, 3.15, 12.2, [4.5, 4.0, 3.7], { rowH: 0.52, fontSize: 11.5 });
  s.addText([
    { text: "Strength — ", options: { bold: true, color: C.green } },
    { text: "the fund book is sound: every scheme with a 3-year record beats its benchmark; the three fund actions are structural, not performance.   ", options: { color: C.navy } },
    { text: `Proceeds bridge — ₹${PL.sells_cr} Cr Sells + ₹${(PL.titan_trim_l/100).toFixed(2)} Cr trim = ₹${PL.deployable_cr} Cr to redeploy; +₹${(PL.fund_actions_l/100).toFixed(2)} Cr fund actions = ₹${PL.total_reorg_cr} Cr reorganised.`, options: { italic: true, color: C.slate } },
  ], { x: 0.55, y: 6.35, w: 12.2, h: 0.7, fontSize: 10.5, fontFace: F, margin: 0, valign: "top" });
})();

// 6 — MANDATE & METHOD -------------------------------------------------------
(() => {
  const s = head("Mandate & method", "How to read this review", "RM");
  // left: mandate + core-satellite
  s.addText("The mandate", { x: 0.55, y: 1.75, w: 6, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText(bullets([
    "Non-discretionary (NDPMS): we recommend Sell, Trim, Switch, Redeem or Hold on holdings you already own. The model never issues a Buy.",
    "Scoring benchmark: the NIFTY-750 cross-sectional percentile (the Ionic Quant Scorecard).",
    "Allocation reference: the Ionic Wealth House View, Dec 2025 — the asset-mix we steer toward.",
  ]), { x: 0.55, y: 2.1, w: 6.1, h: 2.2, fontFace: F, margin: 0, valign: "top" });
  s.addText("What core–satellite means", { x: 0.55, y: 4.35, w: 6, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText("The core (the majority of the book) holds steady, high-quality positions that anchor returns and turn over rarely. Satellites are smaller, deliberate tilts — a sector, a factor, a theme — sized to add return without moving the whole book. Each quarter we test whether every satellite still earns its place; the core changes seldom.",
    { x: 0.55, y: 4.68, w: 6.1, h: 1.9, fontSize: 12, color: C.navy, fontFace: F, margin: 0 });
  // right: method box
  s.addShape(pres.ShapeType.roundRect, { x: 7.0, y: 1.75, w: 5.75, h: 4.9, fill: { color: C.near }, line: { color: C.grid, pt: 1 }, rectRadius: 0.1 });
  s.addText("The Ionic Score", { x: 7.35, y: 2.0, w: 5.1, h: 0.3, fontSize: 14, bold: true, color: C.navy, fontFace: F, margin: 0 });
  s.addText(bullets([
    "A 0–100 composite of quality, valuation, growth and momentum, refreshed each quarter on point-in-time data.",
    "Read over two horizons and blended 0.60 × 3-year + 0.40 × 1-year.",
    "A name is a Sell below 40; at 40+ it is a Hold. The model issues no Buy.",
    "An analyst may argue a Sell up to a Hold — never a Hold down to a Sell.",
  ]), { x: 7.35, y: 2.4, w: 5.1, h: 3.0, fontFace: F, margin: 0, valign: "top" });
  s.addShape(pres.ShapeType.roundRect, { x: 7.35, y: 5.55, w: 5.05, h: 0.85, fill: { color: C.navy }, line: { type: "none" }, rectRadius: 0.08 });
  s.addText([{ text: "The line every holding must clear\n", options: { fontSize: 11, color: C.indigo_t } },
    { text: "40  ·  on the binding horizon", options: { fontSize: 18, bold: true, color: "FFFFFF" } }],
    { x: 7.35, y: 5.55, w: 5.05, h: 0.85, align: "center", valign: "middle", fontFace: F, margin: 0, lineSpacingMultiple: 0.9 });
})();

// 7 — HOW WE SCORE A STOCK ---------------------------------------------------
(() => {
  const s = head("How we score a stock", "A model builds the number; an analyst signs it off", "STD");
  s.addText("The five pillars, over two horizons", { x: 0.55, y: 1.72, w: 6.5, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  const rows = [
    [hcell("Pillar"), hcell("What it measures"), hcell("Built from")],
    ...[
      ["Quality", "durability of the business", "ROE, ROCE, margins, accruals"],
      ["Value", "what you pay for it", "P/E vs peers and own history"],
      ["Growth", "structural + recent growth", "3Y & 1Y revenue / earnings"],
      ["Price-trend", "long & recent price behaviour", "3Y & 1Y vs the market"],
      ["Sector-macro", "the tailwind behind the name", "house sector read (0–100)"],
    ].map(r => [cell(r[0], { bold: true, fontSize: 11 }), cell(r[1], { fontSize: 11 }), cell(r[2], { fontSize: 11, color: C.slate })]),
  ];
  zebra(rows);
  table(s, rows, 0.55, 2.05, 6.7, [1.7, 2.7, 2.3], { rowH: 0.44, fontSize: 11 });
  s.addShape(pres.ShapeType.roundRect, { x: 0.55, y: 4.75, w: 6.7, h: 1.75, fill: { color: C.tint_indigo }, line: { type: "none" }, rectRadius: 0.08 });
  s.addText([
    { text: "How it combines.  ", options: { bold: true, color: C.navy } },
    { text: "Each pillar is a 0–100 percentile across the NIFTY-750 universe. Horizons blend 0.60×3Y + 0.40×1Y; a name is a Sell below 40 on the binding horizon.  ", options: { color: C.navy } },
    { text: "Balance-sheet gate: ", options: { bold: true, color: C.navy } },
    { text: "every non-financial name is first gated GREEN / AMBER / RED; a RED gate caps quality however strong the other pillars.", options: { color: C.navy } },
  ], { x: 0.75, y: 4.9, w: 6.3, h: 1.5, fontSize: 11, fontFace: F, margin: 0, valign: "top" });
  // right — human overlay
  s.addShape(pres.ShapeType.roundRect, { x: 7.5, y: 2.05, w: 5.25, h: 4.45, fill: { color: C.navy }, line: { type: "none" }, rectRadius: 0.1 });
  s.addText("The human overlay", { x: 7.8, y: 2.3, w: 4.7, h: 0.35, fontSize: 14, bold: true, color: C.amber, fontFace: F, margin: 0 });
  s.addText("A score starts the conversation; it does not end it.", { x: 7.8, y: 2.68, w: 4.7, h: 0.5, fontSize: 12.5, italic: true, color: "FFFFFF", fontFace: F, margin: 0 });
  s.addText([
    "Every flagged name is read by an analyst before it reaches this deck.",
    "The analyst can soften a Sell to a Hold on evidence — never harden a Hold to a Sell.",
    "Scores are point-in-time and can be stale or wrong; the desk is the check on that.",
    "Where the model has no coverage (recent listings, ETFs, demergers) there is no score — we carry those on judgement, not silence.",
  ].map(t => ({ text: t, options: { bullet: { code: "2022", indent: 14 }, breakLine: true, paraSpaceAfter: 8, color: "FFFFFF", fontSize: 12 } })),
    { x: 7.8, y: 3.25, w: 4.7, h: 3.1, fontFace: F, margin: 0, valign: "top" });
})();

// ============ SECTION 02 — THE PORTFOLIO ===================================
divider("02", "The Portfolio", "Where the money sits, and where it is over-concentrated.",
  ["Snapshot", "Concentration & risk", "Sector & market-cap positioning"]);

// 8 — SNAPSHOT ---------------------------------------------------------------
(() => {
  const s = head("Snapshot", `₹${M.book_cr} crore, split across direct equity and funds`, "RM");
  chart(s, "donut_split", 0.7, 1.85, 5.4, 4.7);
  const facts = [
    ["Direct equity", `₹${(M.equity_l/100).toFixed(2)} Cr · ${M.n_stocks} stocks`],
    ["Mutual funds", `₹${(M.fund_l/100).toFixed(2)} Cr · ${M.n_funds} schemes`],
    ["Largest position", `${CON.largest_book}% of book · ${CON.largest_name}`],
    ["Construction", "Core–satellite"],
    ["Stance", "Aggressive, long horizon"],
    ["Rated Sell", `${D.below40} stocks · ${CON.sell_wt}% by value`],
  ];
  let y = 2.05;
  facts.forEach(([a, b]) => {
    s.addText(a, { x: 6.6, y, w: 2.4, h: 0.5, fontSize: 12, color: C.slate, fontFace: F, margin: 0, valign: "middle" });
    s.addText(b, { x: 9.0, y, w: 3.7, h: 0.5, fontSize: 13.5, bold: true, color: C.navy, fontFace: F, margin: 0, valign: "middle" });
    s.addShape(pres.ShapeType.rect, { x: 6.6, y: y + 0.52, w: 6.1, h: 0.012, fill: { color: C.grid }, line: { type: "none" } });
    y += 0.72;
  });
})();

// 9 — CONCENTRATION ----------------------------------------------------------
(() => {
  const s = head("Concentration & risk", "The top ten names carry a third of the book", "RM");
  chart(s, "concentration_bubble", 6.4, 1.75, 6.5, 5.0);
  const rows = [
    [hcell("Metric"), hcell("Book", "center"), hcell("Guideline", "center"), hcell("Status", "center")],
    ...[
      ["Top-5 single names", `${CON.top5}%`, "< 25%", CON.top5 < 25 ? "WITHIN" : "BREACH"],
      ["Top-10 single names", `${CON.top10}%`, "< 30%", CON.top10 < 30 ? "WITHIN" : "BREACH"],
      [`Largest name (of equity)`, `${CON.largest_sleeve}%`, "< 8%", CON.largest_sleeve < 8 ? "WITHIN" : "BREACH"],
      [`Names > 8% of equity`, `${CON.names_over8_sleeve}`, "0", CON.names_over8_sleeve ? "WATCH" : "WITHIN"],
      ["Largest AMC (funds)", `${CON.largest_amc}%`, "< 25%", CON.largest_amc < 25 ? "WITHIN" : "BREACH"],
      ["Largest sector (equity)", `${CON.largest_sector}%`, "< 30%", CON.largest_sector < 30 ? "WITHIN" : "BREACH"],
    ].map(r => [cell(r[0], { fontSize: 11.5 }), cell(r[1], { align: "center", bold: true }),
      cell(r[2], { align: "center", color: C.slate }),
      { text: r[3], options: { align: "center", bold: true, color: r[3] === "BREACH" ? C.red : (r[3] === "WATCH" ? C.amber : C.green) } }]),
  ];
  zebra(rows);
  table(s, rows, 0.55, 2.05, 5.7, [2.7, 1.0, 1.1, 0.9], { rowH: 0.52, fontSize: 11.5 });
  s.addText("Single-name rows are measured on the equity sleeve (₹" + (M.equity_l/100).toFixed(2) + " Cr) — the base that drives the trim. Bubble: colour = call, size = position value.",
    { x: 0.55, y: 5.5, w: 5.7, h: 0.9, fontSize: 10, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 10 — SECTOR & MARKET CAP ---------------------------------------------------
(() => {
  const s = head("Sector & market-cap positioning", "A large-cap book; two sectors lead", "RM");
  s.addText("Sector exposure", { x: 0.55, y: 1.72, w: 6, h: 0.3, fontSize: 12.5, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  chart(s, "sector_bar", 0.35, 2.0, 6.7, 4.2);
  s.addText("Market-cap split", { x: 7.3, y: 1.72, w: 5, h: 0.3, fontSize: 12.5, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  chart(s, "mcap_bar", 7.1, 2.15, 5.7, 1.4);
  s.addShape(pres.ShapeType.roundRect, { x: 7.3, y: 3.9, w: 5.4, h: 2.5, fill: { color: C.near }, line: { color: C.grid, pt: 1 }, rectRadius: 0.08 });
  s.addText([
    { text: "Scope.  ", options: { bold: true, color: C.navy } },
    { text: `Direct equity only (₹${(M.equity_l/100).toFixed(2)} Cr, ${M.n_stocks} stocks). The ₹${(M.fund_l/100).toFixed(2)} Cr fund book (${M.fund_frac}% of the portfolio) is not in these charts; its stock-level constituents are not available, so fund exposure is read at category level (Section 04).`, options: { color: C.navy } },
  ], { x: 7.55, y: 4.1, w: 4.9, h: 1.3, fontSize: 11.5, fontFace: F, margin: 0, valign: "top" });
  s.addText("A large-cap core lowers volatility and liquidity risk; under 5% sits in mid/small, leaving room to add diversified SMID if more growth beta is wanted.",
    { x: 7.55, y: 5.35, w: 4.9, h: 0.95, fontSize: 11, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// ============ SECTION 03 — DIRECT EQUITY ===================================
divider("03", "Direct Equity", `${M.n_stocks} names, one bar to clear: a score of forty.`,
  ["The whole book, scored", "The equity book (treemap)", "Spotlights", "The names we would sell", "Quality vs price · factor profile"]);

// 11 — THE BOOK SCORED -------------------------------------------------------
(() => {
  const s = head("The whole book, scored", `${M.n_stocks} stocks; ${D.below40} fall below the line`, "RM");
  chart(s, "score_hist", 1.2, 1.95, 10.9, 4.3);
  s.addText(`${D.below40} of ${M.n_stocks} names score below 40 (${CON.sell_wt}% of the book by value). Bars left of the amber line are the Sell zone; the score shown is the binding, lower-horizon read.`,
    { x: 1.2, y: 6.35, w: 10.9, h: 0.4, fontSize: 11, italic: true, color: C.slate, fontFace: F, align: "center", margin: 0 });
})();

// 12 — TREEMAP ---------------------------------------------------------------
(() => {
  const s = head("The equity book", "Where every rupee sits, and what the scorecard says", "STD");
  chart(s, "treemap", 0.9, 1.85, 11.5, 4.8);
  s.addText("Tile area = share of the total portfolio; colour = call.", { x: 0.9, y: 6.65, w: 11.5, h: 0.3, fontSize: 10, italic: true, color: C.slate, fontFace: F, align: "center", margin: 0 });
})();

// 13 — SPOTLIGHTS ------------------------------------------------------------
(() => {
  const s = head("Spotlights", "The largest holding we keep, and the largest we would sell", "STD");
  const sh = D.spot_hold, ss = D.spot_sell;
  function spotlight(stock, chartName, callTxt, callColor, body, rx, tx, tw) {
    chart(s, chartName, rx, 2.35, 3.3, 3.6);
    s.addText(stock.name, { x: tx, y: 2.15, w: tw, h: 0.4, fontSize: 15, bold: true, color: C.navy, fontFace: F, margin: 0 });
    s.addText(callTxt, { x: tx, y: 2.55, w: 1.2, h: 0.32, fontSize: 12, bold: true, color: "FFFFFF", fill: { color: callColor }, align: "center", valign: "middle", shape: pres.ShapeType.roundRect, rectRadius: 0.14, fontFace: F, margin: 0 });
    s.addText(`${stock.weight}% of book · score ${stock.score}\nROE ${stock.roe}% · ${stock.pe}x P/E`, { x: tx, y: 2.98, w: tw, h: 0.6, fontSize: 10.5, color: C.slate, fontFace: F, margin: 0, lineSpacingMultiple: 1.0 });
    s.addText(body, { x: tx, y: 3.65, w: tw, h: 2.5, fontSize: 11, color: C.navy, fontFace: F, margin: 0 });
  }
  spotlight(sh, "radar_titan", "HOLD", C.green,
    "Highest-conviction core holding: quality and growth are among the best in the book. The one caution is valuation and sheer position size — so we watch the weight and trim toward the guideline rather than add.",
    0.35, 3.75, 2.55);
  spotlight(ss, "radar_reliance", "SELL", C.red,
    "The second-largest single holding, and the scorecard flags it a Sell: quality and price-trend are weak, and ROE is thin for a name this size. We would reduce toward a normal weight and redeploy into stronger core names.",
    6.6, 10.0, 2.75);
})();

// 14 — THE NAMES WE WOULD SELL ----------------------------------------------
(() => {
  const s = head("The names we would sell", `${D.below40} names below the line — about ₹${PL.sells_cr} Cr of proceeds`, "RM");
  const av = { "Reliance Industries": "concur — size risk, not quality; reduce", "Larsen & Toubro": "concur — sector headwind; exit",
    "Adani Enterprises": "concur — growth slowing vs price", "Wipro": "concur — cheap for a reason", "Tata Power": "concur — growth stalled",
    "GAIL India": "concur — growth not translating", "Godrej Consumer": "concur — quality gap at the price", "Max Financial Svcs": "concur — trend weak",
    "Tata Consumer": "concur — thin quality", "Jubilant Foodworks": "concur — QSR headwind", "Info Edge": "concur — quality vs multiple",
    "Swiggy": "concur — not yet profitable", "Jio Financial": "concur — growth real, profitability isn't", "Varun Beverages": "concur — trend soft",
    "VIP Industries": "concur — weakest name in book" };
  const rows = [
    [hcell("#", "center"), hcell("Name"), hcell("Wt", "center"), hcell("Score", "center"), hcell("Primary reason"), hcell("Analyst view")],
    ...D.sells.map((x, i) => [
      cell(String(i + 1), { align: "center", color: C.slate, fontSize: 10 }),
      cell(x.name, { fontSize: 10.5 }),
      cell(x.weight.toFixed(1) + "%", { align: "center", fontSize: 10.5 }),
      { text: String(x.score), options: { align: "center", bold: true, color: C.red, fontSize: 10.5 } },
      cell(x.reason, { fontSize: 10, color: C.slate }),
      cell(av[x.name] || "concur", { fontSize: 10, italic: true, color: C.navy }),
    ]),
  ];
  zebra(rows, C.tint_red);
  table(s, rows, 0.55, 1.9, 12.2, [0.5, 2.7, 0.8, 0.8, 4.0, 3.4], { rowH: 0.288, fontSize: 10.5 });
  s.addText(`${D.below40} names · ${CON.sell_wt}% of book · est. proceeds ₹${PL.sells_cr} Cr. Full per-name rationale in the holdings annexure (appendix).`,
    { x: 0.55, y: 6.65, w: 12, h: 0.3, fontSize: 10, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 15 — QUALITY VS PRICE ------------------------------------------------------
(() => {
  const s = head("Quality versus price", "Are we paying fair prices for the quality we own?", "STD");
  chart(s, "quality_price", 0.7, 1.85, 8.6, 5.0);
  s.addText("The four quadrants", { x: 9.4, y: 2.0, w: 3.3, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText("Every holding on quality (ROE) against valuation (P/E); bubble size is position value, colour is the call. The names to question sit bottom-right — expensive for the quality they deliver. Green Holds cluster top-left; red Sells lean expensive-and-mediocre.",
    { x: 9.4, y: 2.4, w: 3.35, h: 3.5, fontSize: 12, color: C.navy, fontFace: F, margin: 0 });
})();

// 16 — FACTOR PROFILE --------------------------------------------------------
(() => {
  const s = head("The book's factor profile", "How the equity book scores across the pillars", "STD");
  chart(s, "factor_radar", 0.9, 1.9, 5.2, 4.8);
  s.addText("What the profile says", { x: 6.6, y: 2.1, w: 6, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  const f = D.factor;
  s.addText(`Weighted across the equity book, the strongest pillar is quality (${f.Quality}) and the weakest is price-trend (${f["Price-trend"]}). A quality-led, trend-light profile is consistent with a large-cap growth book; it also explains why a stretch in price-trend is a common reason names fall below the line. The dashed ring marks the market average (50).`,
    { x: 6.6, y: 2.5, w: 6.1, h: 3.5, fontSize: 12.5, color: C.navy, fontFace: F, margin: 0 });
})();

// ============ SECTION 04 — MUTUAL FUNDS ====================================
divider("04", "Mutual Funds", `₹${(M.fund_l/100).toFixed(2)} crore across ${M.n_funds} schemes — judged on more than alpha.`,
  ["The fund book", "How we evaluate equity funds", "How we evaluate hybrids", "Evaluation × allocation", "Three fund actions"]);

// 17 — THE FUND BOOK ---------------------------------------------------------
(() => {
  const s = head("The fund book", `₹${(M.fund_l/100).toFixed(2)} crore across ${M.n_funds} schemes`, "RM");
  s.addText("By category", { x: 0.55, y: 1.72, w: 6, h: 0.3, fontSize: 12.5, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  const cats = Object.entries(D.fund_cat).slice(0, 9);
  const crows = cats.map(([k, v]) => [cell(k, { fontSize: 11 }), { text: v.toFixed(1) + "%", options: { align: "right", bold: true, fontSize: 11 } }]);
  table(s, crows, 0.55, 2.05, 5.5, [4.0, 1.5], { rowH: 0.42, fontSize: 11 });
  s.addText("By fund house", { x: 6.6, y: 1.72, w: 6, h: 0.3, fontSize: 12.5, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  const amcs = Object.entries(D.fund_amc).slice(0, 9);
  const arows = amcs.map(([k, v]) => [cell(k, { fontSize: 11 }),
    { text: v.toFixed(1) + "%", options: { align: "right", bold: true, fontSize: 11, color: v > 25 ? C.amber : C.navy } }]);
  table(s, arows, 6.6, 2.05, 5.5, [4.0, 1.5], { rowH: 0.42, fontSize: 11 });
  s.addText(`Largest fund house ${CON.largest_amc}% (guideline < 25%). Only the seasoned schemes carry a 3-year record; the rest are too young, passive, international or cash-like to score on alpha alone — so we judge them on the frameworks that follow.`,
    { x: 0.55, y: 6.2, w: 11.6, h: 0.6, fontSize: 11, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 18 — EVALUATE EQUITY FUNDS -------------------------------------------------
(() => {
  const s = head("How we evaluate equity funds", "Upside and downside capture, consistency — and the house category rules", "STD");
  chart(s, "capture_scatter", 0.4, 1.85, 7.4, 4.6);
  chart(s, "rolling_consistency", 0.4, 5.9, 7.6, 1.5); // placeholder; overwritten below with better layout
})();
// redo slide 18 cleanly (the above double-chart cramped) -> replace with two-panel
pres.slides.pop(); page -= 1;
(() => {
  const s = head("How we evaluate equity funds", "Capture + consistency, over the house category rules", "STD");
  chart(s, "capture_scatter", 0.35, 1.9, 7.2, 4.5);
  s.addText("The house rules", { x: 7.75, y: 1.95, w: 5, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText([
    { text: "Preferred:  ", options: { bold: true, color: C.green } }, { text: "Flexi cap · factor/passive (value, low-vol) · index.\n", options: {} },
    { text: "Dis-preferred:  ", options: { bold: true, color: C.red } }, { text: "Multi cap (forced cap quotas) and active large-cap (persistent alpha is rare — prefer factor/passive).\n\n", options: {} },
    { text: "A fund prefers if it loses less downside (capture < 100), beats its benchmark in ≥ 60% of rolling windows, and sits in a preferred category. It is replaced on the opposite.", options: { italic: true, color: C.slate } },
  ], { x: 7.75, y: 2.35, w: 5.0, h: 2.6, fontSize: 11.5, color: C.navy, fontFace: F, margin: 0, valign: "top" });
  chart(s, "rolling_consistency", 7.5, 4.75, 5.4, 2.0);
  s.addText("Live on the book: Nippon (Multi cap) is switched despite strong alpha; the value index funds are kept (value is house-favoured); momentum index funds are held but watched (momentum is on hold).",
    { x: 0.35, y: 6.5, w: 7.1, h: 0.4, fontSize: 10, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 19 — EVALUATE HYBRIDS ------------------------------------------------------
(() => {
  const s = head("How we evaluate hybrids", "Risk-adjusted return, drawdown, and the worst rolling year", "STD");
  chart(s, "hybrid_risk", 0.4, 1.95, 7.6, 4.4);
  s.addShape(pres.ShapeType.roundRect, { x: 8.2, y: 2.0, w: 4.55, h: 4.4, fill: { color: C.near }, line: { color: C.grid, pt: 1 }, rectRadius: 0.08 });
  s.addText("Why not alpha", { x: 8.45, y: 2.2, w: 4.1, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText([
    "Hybrids exist to shape risk, not to beat an equity benchmark on return. We judge them on:",
  ].concat([]).join(""), { x: 8.45, y: 2.55, w: 4.1, h: 0.7, fontSize: 12, color: C.navy, fontFace: F, margin: 0 });
  s.addText([
    "RAR — Sharpe and Sortino above the category median.",
    "Max drawdown — meaningfully shallower than pure equity; arbitrage ≈ 0.",
    "Worst rolling-1Y — contained; an arbitrage fund should never print negative.",
  ].map(t => ({ text: t, options: { bullet: { code: "2022", indent: 12 }, breakLine: true, paraSpaceAfter: 8, fontSize: 11.5, color: C.navy } })),
    { x: 8.45, y: 3.35, w: 4.1, h: 2.0, fontFace: F, margin: 0, valign: "top" });
  s.addText("The Regular-plan ICICI holding has risk identical to the Direct plan already held — so the only differentiator is the trail cost. That is a redeem, not a risk call.",
    { x: 8.45, y: 5.5, w: 4.1, h: 0.85, fontSize: 10.5, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 20 — EVALUATION x ALLOCATION -----------------------------------------------
(() => {
  const s = head("Evaluation × allocation", "A fund's quality is read against whether its sleeve is over- or under-weight", "STD");
  // 2x2 grid
  const gx = 0.9, gy = 2.3, gw = 5.4, gh = 3.9;
  const quads = [
    ["GROW — top up with redeployment", "JM Flexicap (flexi, under-weight)", C.tint_green, C.green],
    ["KEEP as primary, trim the sleeve", "HSBC carries a trimmed small-cap sleeve", C.tint_indigo, C.indigo],
    ["UPGRADE — re-select, don't just add", "International (under-weight & under-3Y)", C.tint_indigo, C.indigo],
    ["CUT FIRST — weak fund, over-weight sleeve", "Bandhan small-cap · Nippon multi-cap", C.tint_red, C.red],
  ];
  const pos = [[gx, gy], [gx + gw + 0.2, gy], [gx, gy + gh / 2 + 0.1], [gx + gw + 0.2, gy + gh / 2 + 0.1]];
  quads.forEach((q, i) => {
    const [x, y] = pos[i];
    s.addShape(pres.ShapeType.roundRect, { x, y, w: gw, h: gh / 2 - 0.1, fill: { color: q[2] }, line: { type: "none" }, rectRadius: 0.06 });
    s.addText([{ text: q[0] + "\n", options: { bold: true, fontSize: 13, color: q[3] } },
      { text: q[1], options: { fontSize: 11.5, color: C.navy } }], { x: x + 0.2, y: y + 0.15, w: gw - 0.4, h: gh / 2 - 0.4, fontFace: F, margin: 0, valign: "top", lineSpacingMultiple: 1.0 });
  });
  s.addText("Sleeve under-weight  ·  fund strong ▲ upper / weak ▼ lower", { x: gx, y: gy - 0.35, w: gw, h: 0.3, fontSize: 10.5, bold: true, color: C.slate, align: "center", fontFace: F, margin: 0 });
  s.addText("Sleeve over-weight", { x: gx + gw + 0.2, y: gy - 0.35, w: gw, h: 0.3, fontSize: 10.5, bold: true, color: C.slate, align: "center", fontFace: F, margin: 0 });
  s.addText("The exits are the bottom-right cell (weak funds in over-weight sleeves); the redeployment fills the under-weight sleeves — international, value, flexi, and the absent gold/silver.",
    { x: 0.9, y: 6.45, w: 11.5, h: 0.4, fontSize: 11, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 21 — THREE FUND ACTIONS ----------------------------------------------------
(() => {
  const s = head("Three fund actions", "Structural, not performance — each named against the framework", "RM");
  const cards = [
    ["SWITCH", C.indigo, "Nippon India Multi Cap → Flexi cap", "Passes on performance (+9.4pp alpha) but fails on category: multi-cap's forced cap quotas remove the manager's cap-sizing — the flexibility the Flexi > Multi rule keeps. Moves a stub toward an under-weight preferred sleeve."],
    ["REDEEM", C.amber, "ICICI Multi-Asset (Regular) → Direct", "Risk metrics are identical to the Direct plan already held; the only difference is the Regular-plan trail — a permanent cost with no risk offset. Pure cost cleanup; sleeve weight unchanged."],
    ["EXIT", C.red, "Bandhan Small Cap → HSBC carries it", "Also passes on performance; fails on overlay — small-cap is the most over-weight sleeve and a sub-scale second fund adds cost and mechanical overlap. Re-test HSBC vs Bandhan at Q3 before finalising the primary."],
  ];
  let x = 0.55;
  cards.forEach(([tag, col, title, body]) => {
    s.addShape(pres.ShapeType.roundRect, { x, y: 1.95, w: 3.95, h: 4.4, fill: { color: "FFFFFF" }, line: { color: C.grid, pt: 1.2 }, rectRadius: 0.1 });
    s.addText(tag, { x: x + 0.25, y: 2.2, w: 2.0, h: 0.4, fontSize: 13, bold: true, color: "FFFFFF", fill: { color: col }, align: "center", valign: "middle", shape: pres.ShapeType.roundRect, rectRadius: 0.1, fontFace: F, margin: 0 });
    s.addText(title, { x: x + 0.25, y: 2.8, w: 3.45, h: 0.7, fontSize: 13.5, bold: true, color: C.navy, fontFace: F, margin: 0 });
    s.addText(body, { x: x + 0.25, y: 3.55, w: 3.45, h: 2.6, fontSize: 11.5, color: C.navy, fontFace: F, margin: 0 });
    x += 4.15;
  });
  s.addText("Fund overlap — pending look-through: stock-level holdings are not yet available for the equity schemes, so we flag it as a data gap rather than force a grid from mismatched index lists. The redundancy worth removing is already above.",
    { x: 0.55, y: 6.5, w: 12.1, h: 0.5, fontSize: 10, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// ============ SECTION 05 — THE PLAN ========================================
divider("05", "The Plan", "The sells, the fund actions, the cost, the tax, and where the money goes.",
  ["House-view fit", "What you pay today", "Tax impact", "Deployment", "Before & after · order sheet"]);

// 22 — HOUSE-VIEW FIT --------------------------------------------------------
(() => {
  const s = head("House-view fit", "The plan closes the gaps against the house view", "RM");
  const rows = [
    [hcell("Dimension"), hcell("House view (Dec 2025)"), hcell("Today"), hcell("What the plan does"), hcell("Fit", "center")],
    ...[
      ["Domestic equity", "Incrementally positive", "Core, large-cap heavy", "Trim concentration", "ALIGNED"],
      ["Foreign equity", "~25% of equity, 60:40", `~${foreignBook.toFixed(1)}% of book`, "Step up via redeployment", "GAP"],
      ["Gold & silver", "Positive, 75:25", "No sized sleeve", "Add a small sleeve", "GAP"],
      ["Momentum factor", "On hold", "Held passively", "No new momentum adds", "ALIGNED"],
      ["Low-vol / value", "Favoured", "Value-light", "Redeploy Sell proceeds here", "ALIGNED"],
    ].map(r => [cell(r[0], { fontSize: 11.5, bold: true }), cell(r[1], { fontSize: 11.5, color: C.slate }),
      cell(r[2], { fontSize: 11.5 }), cell(r[3], { fontSize: 11.5, color: C.navy }),
      { text: r[4], options: { align: "center", bold: true, color: r[4] === "GAP" ? C.amber : C.green } }]),
  ];
  zebra(rows);
  table(s, rows, 0.55, 2.1, 12.2, [2.2, 3.0, 2.4, 3.0, 1.6], { rowH: 0.62, fontSize: 11.5 });
  s.addText("The redeployment plan (two slides on) fills the two GAP rows with sized, sequenced allocation direction.",
    { x: 0.55, y: 5.9, w: 12, h: 0.3, fontSize: 11, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 23 — COST ------------------------------------------------------------------
(() => {
  const s = head("What you pay today", "Most of the book is already low-cost; the saving is consolidation + one transparent fee", "RM");
  const rows = [
    [hcell("Cost line"), hcell("Base", "right"), hcell("Rate", "center"), hcell("Annual ₹", "right"), hcell("bps", "right")],
    ...[
      ["Fund TER — Direct plans (20 schemes)", `₹${((M.fund_l-2.2)/100).toFixed(2)} Cr`, "wtd [to source]", "[to source]", "[src]"],
      ["Fund TER — Regular-plan trail (1 scheme)", "₹0.05 Cr", "[to source]", "[to source]", "[src]"],
      ["Direct equity (self-held, 76 stocks)", `₹${(M.equity_l/100).toFixed(2)} Cr`, "nil ongoing", "₹0", "0"],
      ["Advisory / PMS fee (if any today)", `₹${M.book_cr} Cr`, "[to source]", "[to source]", "[src]"],
      ["Current all-in recurring", "", "", "[to source]", "[src]"],
    ].map((r, i) => [cell(r[0], { fontSize: 11, bold: i === 4 }), cell(r[1], { align: "right", fontSize: 11 }),
      cell(r[2], { align: "center", fontSize: 10.5, color: C.slate }), cell(r[3], { align: "right", fontSize: 11, bold: i === 4 }),
      cell(r[4], { align: "right", fontSize: 10.5, color: C.slate })]),
  ];
  zebra(rows);
  table(s, rows, 0.55, 2.0, 7.2, [3.4, 1.4, 1.4, 1.4, 0.9], { rowH: 0.46, fontSize: 11 });
  s.addShape(pres.ShapeType.roundRect, { x: 8.0, y: 2.0, w: 4.75, h: 3.2, fill: { color: C.navy }, line: { type: "none" }, rectRadius: 0.1 });
  s.addText("Where CoPilot saves", { x: 8.25, y: 2.25, w: 4.3, h: 0.3, fontSize: 13, bold: true, color: C.amber, fontFace: F, margin: 0 });
  s.addText([
    "The book is already ~99.5% direct plans — so plan conversion is a small win (one ₹0.05 Cr line).",
    "The durable saving is consolidating 21 → 19 schemes, removing duplicated exposure, and folding a fragmented fee base into one transparent CoPilot fee.",
  ].map(t => ({ text: t, options: { bullet: { code: "2022", indent: 12 }, breakLine: true, paraSpaceAfter: 8, color: "FFFFFF", fontSize: 12 } })),
    { x: 8.25, y: 2.62, w: 4.3, h: 2.4, fontFace: F, margin: 0, valign: "top" });
  s.addText("Every [to source] rate is confirmed against the latest factsheets and the CoPilot fee schedule before dealing. Cost and tax are shown on separate slides so neither double-counts the other.",
    { x: 0.55, y: 5.9, w: 12, h: 0.5, fontSize: 10.5, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 24 — TAX IMPACT ------------------------------------------------------------
(() => {
  const s = head("Tax impact of the plan", "What the actions trigger, how we minimise it, and the file that unlocks the equity estimate", "STD");
  s.addText("Rate framework (FY26-27; confirm with adviser): equity LTCG (>12m) 12.5% above the ₹1.25 L annual exemption; STCG 20%. A switch is a redemption for tax.",
    { x: 0.55, y: 1.72, w: 12.1, h: 0.4, fontSize: 11, italic: true, color: C.slate, fontFace: F, margin: 0 });
  const rows = [
    [hcell("Action"), hcell("₹ L", "right"), hcell("Holding"), hcell("Character"), hcell("Note")],
    ...[
      ["Nippon Multi-Cap (switch)", "1.7", "> 1y", "LTCG 12.5%", "switch = redemption for tax"],
      ["ICICI Multi-Asset Regular (redeem)", "2.4", "recent", "STCG 20%", "consolidate to Direct; check net-of-tax vs trail"],
      ["Bandhan Small-Cap (exit)", "3.7", "> 1y", "LTCG 12.5%", "small ticket, low tax drag"],
      ["Direct-equity Sells + Titan trim", `${(PL.deployable_l).toFixed(0)}`, "mixed lots", "pending", "not computable until demat trade file is shared"],
    ].map((r, i) => [cell(r[0], { fontSize: 11 }), cell(r[1], { align: "right", fontSize: 11 }),
      cell(r[2], { fontSize: 11, color: C.slate }), cell(r[3], { fontSize: 11, bold: true, color: i === 3 ? C.amber : C.navy }),
      cell(r[4], { fontSize: 10.5, color: C.slate })]),
  ];
  zebra(rows);
  table(s, rows, 0.55, 2.25, 7.6, [3.0, 0.8, 1.2, 1.3, 3.3], { rowH: 0.5, fontSize: 11 });
  s.addShape(pres.ShapeType.roundRect, { x: 8.35, y: 2.25, w: 4.4, h: 2.0, fill: { color: C.tint_indigo }, line: { type: "none" }, rectRadius: 0.08 });
  s.addText("Tax-aware sequence", { x: 8.6, y: 2.42, w: 4.0, h: 0.3, fontSize: 12.5, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText([
    "This FY: book losses first (harvest), then LTCG up to ₹1.25 L tax-free, then the high-conviction Sells regardless of tax.",
    "Next FY: remaining LTCG sells + the Titan trim, on a fresh exemption.",
  ].map(t => ({ text: t, options: { bullet: { code: "2022", indent: 12 }, breakLine: true, paraSpaceAfter: 6, fontSize: 11, color: C.navy } })),
    { x: 8.6, y: 2.78, w: 4.0, h: 1.4, fontFace: F, margin: 0, valign: "top" });
  s.addShape(pres.ShapeType.roundRect, { x: 8.35, y: 4.4, w: 4.4, h: 1.85, fill: { color: C.navy }, line: { type: "none" }, rectRadius: 0.08 });
  s.addText([{ text: "One file closes this gap.\n", options: { bold: true, color: C.amber, fontSize: 12.5 } },
    { text: "Share the demat trade file (acquisition dates + costs per lot) and the next review computes exact per-lot STCG/LTCG, finalises the harvest set, and locks the two-FY sequence. Until then the equity tax figure is intentionally blank, not guessed.", options: { color: "FFFFFF", fontSize: 11 } }],
    { x: 8.6, y: 4.55, w: 4.0, h: 1.55, fontFace: F, margin: 0, valign: "top" });
})();

// 25 — DEPLOYMENT ------------------------------------------------------------
(() => {
  const s = head("Deployment — where the money moves", "Every rupee freed has a destination, and every destination has a reason", "RM");
  chart(s, "sankey_deploy", 0.3, 1.85, 7.0, 4.8);
  const rows = [
    [hcell("Destination"), hcell("₹ L", "right"), hcell("Why")],
    ...PL.sleeves.map(sl => [cell(sl[0], { fontSize: 10.5, bold: true }), cell(sl[1].toFixed(0), { align: "right", fontSize: 10.5 }),
      cell(sl[2], { fontSize: 10, color: C.slate })]),
  ];
  zebra(rows);
  table(s, rows, 7.35, 1.95, 5.4, [2.5, 0.7, 2.2], { rowH: 0.62, fontSize: 10.5 });
  s.addText([{ text: "Proceeds bridge.  ", options: { bold: true, color: C.navy } },
    { text: `₹${PL.sells_cr} Cr Sells + ₹${(PL.titan_trim_l/100).toFixed(2)} Cr Titan trim = ₹${PL.deployable_cr} Cr cash to redeploy. The ₹${(PL.fund_actions_l/100).toFixed(2)} Cr of fund actions recirculates inside the fund book (not new-sleeve cash); total reorganised ₹${PL.total_reorg_cr} Cr.`, options: { color: C.slate } }],
    { x: 7.35, y: 5.0, w: 5.4, h: 1.0, fontSize: 10.5, italic: true, fontFace: F, margin: 0, valign: "top" });
  s.addText("Expressed as allocation direction for freed cash, actioned on your instruction — no specific security is recommended for purchase (non-discretionary mandate).",
    { x: 0.3, y: 6.75, w: 12.5, h: 0.3, fontSize: 9.5, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 26 — BEFORE & AFTER --------------------------------------------------------
(() => {
  const s = head("Before & after", "The book, before and after the plan", "RM");
  const rows = [
    [hcell("Measure"), hcell("Today", "center"), hcell("Proposed / target", "center")],
    ...[
      ["Largest single name (of equity)", `${CON.largest_sleeve}%`, "8.0% (guideline)"],
      ["Sell-rated weight", `${CON.sell_wt}%`, "0.0%"],
      ["Top-10 weight", `${CON.top10}%`, "toward < 30%"],
      ["Regular-plan fund", "one holding", "0"],
      ["Foreign-equity share", `~${foreignBook.toFixed(1)}%`, "toward 25% of equity"],
      ["Fund schemes", `${M.n_funds}`, `${M.n_funds - 2}`],
    ].map(r => [cell(r[0], { fontSize: 12.5 }), cell(r[1], { align: "center", fontSize: 13, bold: true, color: C.slate }),
      cell(r[2], { align: "center", fontSize: 13, bold: true, color: C.green })]),
  ];
  zebra(rows);
  table(s, rows, 1.6, 2.1, 10.1, [4.9, 2.6, 2.6], { rowH: 0.6, fontSize: 12.5 });
  s.addText("Proposed values are guidelines or house-view targets, not forecasts of return.",
    { x: 1.6, y: 6.1, w: 10, h: 0.3, fontSize: 11, italic: true, color: C.slate, fontFace: F, align: "center", margin: 0 });
})();

// 27 — PRIORITY ACTIONS ------------------------------------------------------
(() => {
  const s = head("Priority actions", "The order sheet — sequenced and tax-aware", "RM");
  const ss = D.spot_sell, sh = D.spot_hold;
  const rows = [
    [hcell("#", "center"), hcell("Action"), hcell("Instrument"), hcell("Instruction"), hcell("₹ L", "right"), hcell("Proceeds to")],
    ...[
      ["1", "TRIM", sh.name, "Toward the single-name guideline", `${PL.titan_trim_l}`, "Low-vol / value"],
      ["2", "SELL", ss.name, `Full exit, scored ${ss.score}`, `${ss.value_l.toFixed(0)}`, "Low-vol / value"],
      ["3", "SELL", `${D.below40 - 1} further Sell names`, "Scored below 40", `${(PL.sells_l - ss.value_l).toFixed(0)}`, "Redeploy per plan"],
      ["4", "SWITCH", "Nippon Multi-Cap", "Reshape to flexi-cap", "1.7", "Flexi-cap fund"],
      ["5", "REDEEM", "ICICI Multi-Asset (Regular)", "Duplicate, costlier plan", "2.4", "ICICI Direct plan"],
      ["6", "EXIT", "Bandhan Small-Cap", "Sub-scale duplicate", "3.7", "Primary small-cap"],
    ].map(r => [cell(r[0], { align: "center", color: C.slate }),
      { text: r[1], options: { bold: true, align: "center", color: r[1] === "SELL" || r[1] === "EXIT" ? C.red : (r[1] === "TRIM" ? C.amber : C.indigo) } },
      cell(r[2], { fontSize: 11, bold: true }), cell(r[3], { fontSize: 11, color: C.slate }),
      cell(r[4], { align: "right", fontSize: 11 }), cell(r[5], { fontSize: 11, color: C.navy })]),
  ];
  zebra(rows);
  table(s, rows, 0.55, 2.0, 12.2, [0.5, 1.2, 3.0, 3.4, 0.9, 3.2], { rowH: 0.5, fontSize: 11 });
  s.addText([{ text: `Total value reorganised  ₹${PL.total_reorg_l} L (₹${PL.total_reorg_cr} Cr).   `, options: { bold: true, color: C.navy } },
    { text: "Reviewed with client on  ____________________", options: { color: C.slate } }],
    { x: 0.55, y: 5.4, w: 12, h: 0.4, fontSize: 12, fontFace: F, margin: 0 });
  s.addText("Sequence sells tax-aware per the tax slide; amounts indicative pending dealing. Non-discretionary — actioned on your instruction.",
    { x: 0.55, y: 6.5, w: 12, h: 0.3, fontSize: 10, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// ============ SECTION 06 — GROWTH & FRONTIER ===============================
divider("06", "Growth & Frontier", "Where the book sits against the frontier, and where it could grow.",
  ["The opportunity set", "Growth projection"]);

// 28 — EFFICIENT FRONTIER ----------------------------------------------------
(() => {
  const s = head("The opportunity set", "Where the book sits against an efficient frontier", "STD");
  chart(s, "efficient_frontier", 0.6, 1.9, 8.0, 4.8);
  s.addText("Reading the map", { x: 8.8, y: 2.1, w: 3.9, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText("Each dot is a feasible asset-class mix; colour rises with reward-per-unit-risk, and the upper-left edge is the efficient frontier. Today (red) sits inside the frontier — too much single-basket equity risk for its return. The house-view target (green) steps left by adding international, gold and a debt cushion.",
    { x: 8.8, y: 2.5, w: 3.95, h: 3.8, fontSize: 12, color: C.navy, fontFace: F, margin: 0 });
  s.addText("Illustrative opportunity set from long-run capital-market assumptions, not a forecast.",
    { x: 8.8, y: 6.1, w: 3.95, h: 0.6, fontSize: 9.5, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 29 — GROWTH PROJECTION -----------------------------------------------------
(() => {
  const s = head("Growth projection", "Where this book could grow, and the goals it can fund", "STD");
  chart(s, "growth_cone", 0.6, 1.9, 8.2, 4.8);
  s.addText("Reading the cone", { x: 9.0, y: 2.1, w: 3.7, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText("At an assumed 11% return and 13% volatility, the book's central path roughly doubles in about seven years. The shaded band is the 10th–90th percentile of outcomes; real experience will vary. Dashed lines are illustrative goal corpora.",
    { x: 9.0, y: 2.5, w: 3.7, h: 3.5, fontSize: 12, color: C.navy, fontFace: F, margin: 0 });
  s.addText("Illustrative lognormal projection, not a forecast.", { x: 9.0, y: 5.9, w: 3.7, h: 0.4, fontSize: 9.5, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// ============ SECTION 07 — FAMILY OFFICE ===================================
divider("07", "Family Office", "For the UHNI family office: consolidation, governance and goal funding.",
  ["Consolidated view", "Governance & succession", "Goal funding"]);

// 30 — UHNI CONSOLIDATION ----------------------------------------------------
(() => {
  const U = D.uhni;
  const s = head("Consolidated view", `${U.name} — ₹${U.corpus_cr} Cr across five entities`, "UHNI");
  chart(s, "uhni_alloc", 0.5, 2.1, 5.0, 4.6);
  s.addText("By entity", { x: 6.0, y: 1.85, w: 6, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  const rows = [
    [hcell("Entity"), hcell("Mandate"), hcell("₹ Cr", "right")],
    ...U.entities.map(e => [cell(e[0], { fontSize: 11.5, bold: true }), cell(e[1], { fontSize: 10.5, color: C.slate }),
      { text: e[2].toFixed(1), options: { align: "right", bold: true, fontSize: 11.5 } }]),
  ];
  zebra(rows);
  table(s, rows, 6.0, 2.2, 6.7, [2.6, 2.9, 1.2], { rowH: 0.55, fontSize: 11 });
  s.addText("A family-office review consolidates every entity into one look-through — the same scorecard and house-view discipline applied across trust, HUF, treasury and individual demats, with entity-level tax and governance layered on top.",
    { x: 6.0, y: 5.5, w: 6.7, h: 1.0, fontSize: 11, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 31 — GOVERNANCE & SUCCESSION ----------------------------------------------
(() => {
  const s = head("Governance & succession", "The layer above the portfolio, for a multi-generational book", "UHNI");
  const cards = [
    ["Investment governance", "A written IPS per entity, an annual asset-allocation review, and a documented rebalancing policy so decisions survive any single decision-maker."],
    ["Succession & structure", "Trust and HUF structures aligned to the family's succession intent; beneficiary classes, trustee powers and a letter of wishes reviewed with counsel."],
    ["Liquidity & events", "A liquidity ladder for the anticipated promoter event, with reinvestment sequenced into the house-view sleeves rather than deployed at once."],
    ["Philanthropy & legacy", "An endowment sleeve with its own spending policy, ring-fenced from the family corpus and reported separately."],
  ];
  let x = 0.55, y = 1.95;
  cards.forEach((c, i) => {
    const cx = 0.55 + (i % 2) * 6.2, cy = 1.95 + Math.floor(i / 2) * 2.35;
    s.addShape(pres.ShapeType.roundRect, { x: cx, y: cy, w: 5.9, h: 2.1, fill: { color: C.near }, line: { color: C.grid, pt: 1 }, rectRadius: 0.1 });
    s.addText(c[0], { x: cx + 0.3, y: cy + 0.2, w: 5.3, h: 0.4, fontSize: 14, bold: true, color: C.indigo, fontFace: F, margin: 0 });
    s.addText(c[1], { x: cx + 0.3, y: cy + 0.7, w: 5.3, h: 1.3, fontSize: 12, color: C.navy, fontFace: F, margin: 0 });
  });
  chart(s, "uhni_goals", 0.6, 6.35, 12.1, 0.9);
})();

// 32 — GOAL FUNDING ----------------------------------------------------------
(() => {
  const s = head("Goal funding", "Probability the corpus funds the family's goals", "UHNI");
  chart(s, "montecarlo_fan", 0.6, 1.9, 8.2, 4.8);
  s.addText("Reading the fan", { x: 9.0, y: 2.1, w: 3.7, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText("Each faint line is one simulated path for the family corpus; the bold lines are the 10th, 50th and 90th percentiles. Against the illustrative goal, the probability of success is read where the paths clear the dashed line.",
    { x: 9.0, y: 2.5, w: 3.7, h: 3.5, fontSize: 12, color: C.navy, fontFace: F, margin: 0 });
  s.addText("Illustrative Monte-Carlo simulation on long-run assumptions; not a forecast or a guarantee.",
    { x: 9.0, y: 5.95, w: 3.7, h: 0.6, fontSize: 9.5, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// ============ APPENDIX ======================================================
divider("A", "Appendix", "A reusable chart library, the full registers, and the method.",
  ["Chart library (templates ready for any client)", "Direct-equity register", "Mutual-fund register", "Methodology & basis of preparation"]);

// 33 — CHART LIBRARY ---------------------------------------------------------
(() => {
  const s = head("Chart library", "Reusable analytics — ready for any client, shown here on AZBY data", "APX");
  const items = [["glidepath", "Allocation glidepath"], ["drawdown", "Drawdown / underwater"],
    ["corr_heatmap", "Asset-class correlation"], ["rolling_consistency", "Rolling-return consistency"]];
  const pos = [[0.55, 2.1], [6.7, 2.1], [0.55, 4.5], [6.7, 4.5]];
  items.forEach((it, i) => {
    const [x, y] = pos[i];
    s.addText(it[1], { x, y: y - 0.28, w: 5.8, h: 0.28, fontSize: 12, bold: true, color: C.indigo, fontFace: F, margin: 0 });
    chart(s, it[0], x, y, 5.9, 2.2);
  });
  s.addText("These are template charts wired to the same data model — an advisor can drop any of them into a client review without rebuilding.",
    { x: 0.55, y: 6.85, w: 12, h: 0.3, fontSize: 9.5, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 34/35 — EQUITY REGISTER ----------------------------------------------------
function registerSlide(part, subset) {
  const s = head("Direct-equity register", `Every holding, every score, every call · ${part} of 2`, "APX");
  const mk = (arr) => [
    [hcell("Name"), hcell("Wt", "center"), hcell("Score", "center"), hcell("Call", "center")],
    ...arr.map(x => [cell(x.name, { fontSize: 9.5 }), cell(x.weight.toFixed(1) + "%", { align: "center", fontSize: 9.5 }),
      { text: x.score == null ? "—" : String(x.score), options: { align: "center", fontSize: 9.5 } }, callBadge(x.call)]),
  ];
  const half = Math.ceil(subset.length / 2);
  const left = zebra(mk(subset.slice(0, half))), right = zebra(mk(subset.slice(half)));
  table(s, left, 0.55, 1.95, 6.0, [3.5, 1.0, 1.0, 0.9], { rowH: 0.238, fontSize: 9.5 });
  table(s, right, 6.75, 1.95, 6.0, [3.5, 1.0, 1.0, 0.9], { rowH: 0.238, fontSize: 9.5 });
  s.addText("Source: Ionic Quant Scorecard. Sorted by weight.", { x: 0.55, y: 6.95, w: 8, h: 0.25, fontSize: 9, italic: true, color: C.slate, fontFace: F, margin: 0 });
}
const byW = [...D.stocks].sort((a, b) => b.weight - a.weight);
registerSlide(1, byW.slice(0, 38));
registerSlide(2, byW.slice(38));

// 36 — MF REGISTER -----------------------------------------------------------
(() => {
  const s = head("Mutual-fund register", "Every scheme, category, plan and action", "APX");
  const rows = [
    [hcell("Scheme"), hcell("House"), hcell("Category"), hcell("Plan"), hcell("₹ L", "right"), hcell("3Y vs bench"), hcell("Action", "center")],
    ...D.funds.map(f => {
      const act = f.name.includes("Nippon India Multi") ? "SWITCH" : f.name.includes("(Reg)") ? "REDEEM" : f.name.includes("Bandhan") ? "EXIT" : "HOLD";
      return [cell(f.name, { fontSize: 9.5 }), cell(f.house, { fontSize: 9.5, color: C.slate }), cell(f.category, { fontSize: 9.5, color: C.slate }),
        cell(f.plan, { fontSize: 9.5 }), cell(f.aum_l.toFixed(1), { align: "right", fontSize: 9.5 }),
        cell(f.alpha ? `+${f.alpha}pp` : "under 3Y", { fontSize: 9.5, color: f.alpha ? C.green : C.slate }),
        { text: act, options: { align: "center", bold: true, fontSize: 9.5, color: act === "HOLD" ? C.slate : (act === "SWITCH" ? C.indigo : (act === "REDEEM" ? C.amber : C.red)) } }];
    }),
  ];
  zebra(rows);
  table(s, rows, 0.55, 1.95, 12.2, [3.2, 1.9, 2.4, 1.1, 0.9, 1.4, 1.3], { rowH: 0.225, fontSize: 9.5 });
  s.addText("Source: client statement; QFRA fund NAV feed. Capture, consistency and hybrid risk metrics refreshed each quarter.",
    { x: 0.55, y: 6.95, w: 10, h: 0.25, fontSize: 9, italic: true, color: C.slate, fontFace: F, margin: 0 });
})();

// 37 — METHODOLOGY -----------------------------------------------------------
(() => {
  const s = head("Methodology & basis of preparation", "How the numbers are built, and what they can and cannot say", "APX");
  s.addText("The Ionic Score", { x: 0.55, y: 1.8, w: 6, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText(bullets([
    "A 0–100 cross-sectional composite of quality, valuation, growth and momentum pillars.",
    "Blended 0.60 × 3-year + 0.40 × 1-year; a Sell triggers below 40, and the model never issues Buy.",
    "Refreshed each quarter on point-in-time data; a score can be stale or wrong, and is read alongside an analyst.",
  ]), { x: 0.55, y: 2.15, w: 6.0, h: 2.6, fontFace: F, margin: 0, valign: "top" });
  s.addText("Basis of preparation", { x: 6.8, y: 1.8, w: 6, h: 0.3, fontSize: 13, bold: true, color: C.indigo, fontFace: F, margin: 0 });
  s.addText(bullets([
    "All figures are illustrative template data for a fictional family; no real client is depicted.",
    "Fund capture, consistency and hybrid risk metrics are computed from the NAV feed at each quarterly refresh.",
    "Tax estimates cover the fund book until a demat trade file supplies equity acquisition lots and costs.",
    "Fund look-through (overlap) is pending each scheme's latest portfolio disclosure.",
  ]), { x: 6.8, y: 2.15, w: 6.0, h: 3.2, fontFace: F, margin: 0, valign: "top" });
})();

// 38 — DISCLAIMER ------------------------------------------------------------
(() => {
  const s = pres.addSlide(); s.background = { color: C.navy };
  s.addImage({ path: LOGO_W, x: 0.6, y: 0.6, w: 1.6, h: 1.6 * LOGO_AR });
  s.addText("DISCLAIMER", { x: 0.6, y: 1.7, w: 6, h: 0.4, fontSize: 14, color: C.amber, fontFace: F, charSpacing: 3, margin: 0 });
  s.addText("This is an illustrative template built on fictional data (the “AZBY Family”) to design a standard portfolio-review deck; it depicts no real client and is not investment advice. In a live review, recommendations are Sell (including full Exit or, for a fund, Redeem), Switch, Trim or Hold on holdings already owned; the model does not issue Buy calls. Scores are model output on point-in-time data and can be wrong or stale. Past performance is not indicative of future results. Mutual fund investments are subject to market risk; read all scheme-related documents carefully. Tax treatment depends on individual circumstances and may change; consult a tax adviser before dealing.",
    { x: 0.6, y: 2.2, w: 11.6, h: 3.2, fontSize: 13, color: "FFFFFF", fontFace: F, margin: 0, lineSpacingMultiple: 1.15 });
  s.addText("IONIC WEALTH", { x: 0.6, y: 5.9, w: 6, h: 0.4, fontSize: 16, bold: true, color: "FFFFFF", fontFace: F, margin: 0 });
  s.addText("Private & Confidential  ·  Illustrative template", { x: 0.6, y: 6.4, w: 8, h: 0.3, fontSize: 11, color: C.indigo_t, fontFace: F, margin: 0 });
})();

// ---------------------------------------------------------------------------
const OUT = path.join(__dirname, "AZBY_Portfolio_Review_Template.pptx");
pres.writeFile({ fileName: OUT }).then(() => console.log("wrote", OUT, "· slides:", pres.slides.length));
