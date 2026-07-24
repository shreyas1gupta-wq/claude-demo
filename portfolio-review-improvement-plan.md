# Portfolio Review Deck — Improvement Plan & Revised Blueprint

*Worked against the v8 review deck (57 slides) and the NIFTY-750 quant scorecard. Client name
withheld from this file for privacy; all figures are the deck's own. This doubles as the
reusable proposal **template** the review asked for — it is written to apply to any future
portfolio review, using v8 as the worked example.*

---

## 0. TL;DR — what to do, in order

**Lead change (the reviewers' most-repeated ask):** reorder the deck from *methodology-first* to
*decision-first*. New front-of-deck spine: **Cover → IPS → "Where you stand vs your policy"
(gaps up front) → Executive summary (each gap paired 1:1 with an action)**. Everything else
hangs off that spine.

**But lock two conventions BEFORE rewriting the front (or the rewrite ships today's errors):**

1. **Concentration denominator = the equity sleeve (₹2.33 Cr), not the whole book.** On the
   whole book the largest name is 6.0% — inside the <8% limit — which makes the headline "trim
   Titan toward the guideline" action *incoherent*. It only works on the equity-sleeve base
   (Titan ≈ 11.2%, Reliance ≈ 11.0%, Groww ≈ 8.7% of the sleeve). Pick the equity-sleeve lens
   for all single-name rows and **label the base on the slide**.
2. **Proceeds vocabulary (three distinct numbers, never interchangeable):**
   `₹0.59 Cr` = 19 equity Sells → `₹0.67 Cr` = **cash freed to redeploy** (adds the ₹0.08 Cr
   Titan trim) → `₹0.74 Cr` = **total value reorganised** (adds ₹0.06 Cr of fund actions, which
   recirculate *inside* the fund book). Stop calling ₹0.74 Cr "proceeds."

**One governing compliance rule (most serious risk — see §3):** this is a **non-discretionary
(NDPMS)** review — the model issues no Buy. The richer the deployment slide gets, the closer it
edges to a Buy solicitation. Deployment must be expressed as **asset-allocation *direction* for
freed cash, actioned only on client instruction, with no named instruments to buy**, and the
disclaimer repeated on that slide. The CoPilot cost pitch sits in the same risk family.

**3 quickest wins (pure text edits, zero data needed, all ship-blockers):**
1. Delete the **leaked draft prose on slide 22** and drop in the honest data-gap panel (§6.10).
   Internal scaffolding text ("*in the supplied the fund dataset dataset… our fund dataset and
   our fund dataset files*") is currently sitting in a client deck.
2. Global replace **"Asset X house view"** (slides 3/4/7/25) with the real name, split into
   "Allocation reference" vs "Scoring benchmark." It reads as an unfilled template token.
3. Fix slide 29's **duplicate title** ("Priority actions / Priority actions") and paste the
   **proceeds bridge** at the foot of slides 3/16/27.

**3 data pulls gate the flagship new slides (see §7) — sequence these now:**
the **MF/hybrid evaluation framework** needs the NAV feed refreshed (today only 4 of 17 funds
have a 3Y record; the alpha window is stale at Dec-2024); the **cost slide** needs the fee/TER
schedule; the **equity tax block** needs the demat trade file. Until they arrive these slides
ship as *defined-but-blank* frameworks, and the deck should say so rather than imply they're done.

---

## 1. Ship-blockers — fix before the deck goes to any client

These are correctness defects, not enhancements. Full register of 23 in §8; the load-bearing four:

| # | Slide | Defect | Fix |
|---|-------|--------|-----|
| B1 | 22 | Leaked draft/editorial prose; slide also self-contradicts (asserts "overlap is mild" while admitting **no** look-through data exists) | Replace whole body with the data-gap panel (§6.10) |
| B2 | 8 | "Names above 8% = 3" is impossible if the largest name is 6.0% — it silently switches to an equity-sleeve denominator mid-table | Put the whole table on **one** base (equity sleeve, per §0); label it |
| B3 | 3 | "two names sit above 11% each" / "trim the two >11% positions" — no name exceeds 6.05% whole-book; citation "(p.8)" unsupported | Reword to "the two largest names are ~11% of the equity sleeve (6.0% / 5.9% of the whole book)" |
| B4 | 3/16 vs 27/29 | Two unreconciled "proceeds" (₹0.59 Cr vs ₹0.74 Cr) with no bridge | Add the three-number bridge (§0, §6.9) |

---

## 2. The reconciliation decisions to lock first

The seven analysis streams agreed on substance but collided on three shared conventions. Resolve
these once, centrally, or the new slides re-introduce the very defects the QA pass removes.

**2a. Concentration denominator → equity sleeve.** Chosen because it is the only base on which
the Titan trim and the <8% single-name limit are meaningful. Show both where helpful
("11.2% of equity / 6.0% of book") but drive all limit-vs-actual logic off the sleeve.

**2b. Proceeds → the three-number convention** (§0). Apply verbatim on slides 3, 16, 27, 29.

**2c. Slide numbering → adopt the CORE map in §5 as canonical**, then rewrite every internal
"see p.X" cross-reference to match. (Today the cost/tax/deployment renumbering conflicts between
streams, and slide 29's "sequence sells tax-aware per p.26" points at the wrong slide once things
move.)

**2d. Slide 4 is overloaded — split it.** Don't cram mandate + client understanding + benchmark
+ core-satellite + scoring method onto one slide. Keep **slide 4 = Mandate & method** (scope,
NDPMS/no-Buy, benchmark defined, core-satellite explained); make **"How we score a stock" its own
slide** (§6.4).

**2e. Gap narration is over-instrumented — say each gap once per job.** The foreign-equity and
gold-silver gaps currently recur ~6× across the new slides. Assign each a single owner:
*named* in the IPS gap board (§6.2), *actioned* in the exec summary (§6.3), *closed with amounts*
on the deployment slide (§6.9). Everywhere else, reference — don't restate.

---

## 3. Compliance guardrail (NDPMS / no-Buy) — read before drafting deployment or cost

The current deck is deliberately vague on redeployment ("freed cash shown as cash until
redeployed, never assumed fully invested"; "step up via redeployment"). That vagueness is a
*feature*: it keeps a non-discretionary review clear of a Buy recommendation. Two of the
requested improvements pull directly against it:

- **Deployment with rationale + amounts** (₹40 L low-vol/value, ₹18 L foreign, ₹9 L new
  gold-silver sleeve) into sleeves the client barely owns is functionally a Buy.
- **CoPilot cost positioning** inside a non-discretionary review is a solicitation/suitability
  question — is CoPilot a discretionary product, and does pitching it belong here?

**Rule to adopt and print on the deployment slide:** *deployment is expressed as
asset-allocation **direction** for freed cash, sized to house-view sleeves, to be actioned
solely on the client's instruction; no specific security is recommended for purchase.* Keep the
Sell/Trim/Switch/Redeem/Exit actions (all on existing holdings — safe) crisp and specific; keep
new-sleeve *entry* directional. Route the CoPilot slide past compliance before it ships, and add
the suitability disclosure they require.

---

## 4. Feedback → resolution map (all items)

### Group A — new / restructured slides

| # | Feedback | Verdict | Where it lands |
|---|----------|---------|----------------|
| A1 | IPS at the beginning | **New — 2-part front block**: policy + gap board | New slide 3 (§6.1–6.2) |
| A2 | Exec summary = gaps + action points | **Rebuild** as a Gap→Action→Impact table | Slide 5 (§6.3) |
| A3 | Longer sell rationale (stocks) | **Keep slide 16 table**; add an "Analyst view" column; move full rationale to a per-name **sell annexure** (prose already exists on the holdings slides) | Slide 15 + appendix M5 (§6.5) |
| A4 | More nuanced MF exit rationale | **Enrich** the 3 action cards with framework language | Slide 22 (§6.8) |
| A5 | Standalone cost slide → CoPilot savings | **New**, split out of today's "Tax & cost"; honest (book is already ~99.5% direct) | Slide 25 (§6.11) |
| A6 | Deployment slide needs rationale | **Rebuild** with per-sleeve why (house-view · gap · risk) | Slide 27 (§6.9) |
| A7 | Tax-impact slide | **New**, split out; equity block flagged pending demat file | Slide 26 (§6.12) |
| A8 | Exec-summary formatting | KPI strip trimmed to 4 tiles + one full-width table | Slide 5 (§6.3) |

### Group B — clarity / methodology fixes

| # | Feedback | Verdict | Where |
|---|----------|---------|-------|
| B1 | Mandate & Method unclear; benchmark label | **Revise slide 4**; define benchmark, add client-understanding block | §6.4 |
| B2 | Explain "core-satellite" | **Add plain-language panel** | Slide 4 (§6.4) |
| B3 | IPS refine + risk-profile standard | **Standardised per-profile SAA template** | Slide 3 (§6.1) |
| B4 | Sector / market-cap data scope | **State scope in headline**; add blended (stocks+fund proxy) view; **merge slides 9+10** | Slide 9 (§6.6) |
| B5 | Present scoring method, don't over-harp | **New "How we score" slide** with an equal-billing human-overlay half | Slide 4-adjacent (§6.4) |
| B6 | MF equity eval framework | **New framework**: up/down capture + consistency; Flexi>Multi; Factor/Passive>Active-LC | Slide 19 (§6.7) |
| B7 | Hybrid eval | **New**: RAR + max drawdown + worst rolling-1Y | Slide 19 (§6.7) |
| B8 | Overlay eval on over/under allocation | **New 2×2** (fund quality × sleeve over/under) | Slide 21 (§6.7) |
| B9 | Fund overlap unclear | **Replace** broken slide with honest data-gap panel; real look-through spec for Q3 | Slide 22 (§6.10) |
| B10 | Beyond slide 30 = optional; best template | **Two-tier template**: CORE (~30) + optional analytical appendix | §5 |

---

## 5. The revised deck blueprint (two-tier template)

**Principle:** the CORE is a self-contained decision story that ends on the order sheet and
disclaimer and depends on **no** appendix slide. Analytical set-pieces and row-level detail
become **optional modules** the advisor toggles per client — this is the reviewer's
"beyond-30 = optional." The order sheet, buried at slide 29 of 57 today, now lands ~20 slides
earlier.

### Tier 1 — CORE PROPOSAL (always presented, ~30 slides)

| # | Section | Slide | Status |
|---|---------|-------|--------|
| 1 | Front | Cover | keep |
| 2 | Front | Contents (rewritten to two tiers) | revise |
| 3 | Foundations | **IPS** — objectives, standardised risk profile, horizon, constraints, target SAA, **gaps up front** | **new** |
| 4 | Foundations | **Mandate & method** — NDPMS scope, benchmark *defined*, core-satellite *explained* | revise |
| 4a| Foundations | **How we score a stock** — 5 pillars × 2 horizons + BS-gate, with a human-overlay half | **new** |
| 5 | Foundations | **Executive summary** — gap→action→impact table (reformatted) | revise |
| 6 | Portfolio | Divider | keep |
| 7 | Portfolio | Snapshot | keep |
| 8 | Portfolio | Concentration & risk (single base; fix "3 names >8%") | revise |
| 9 | Portfolio | **Sector & market-cap** (merged 9+10; data scope stated; blended view) | revise/merge |
| 10| Direct Equity | Divider | keep |
| 11| Direct Equity | The whole book, scored (histogram) | keep |
| 12| Direct Equity | The equity book (treemap) — *rename nav item, no "top ten" slide exists* | revise |
| 13| Direct Equity | Spotlight: Reliance | keep (align verb — see D7) |
| 14| Direct Equity | Spotlight: Titan | keep |
| 15| Direct Equity | The names we would sell — + "Analyst view" col, link to annexure | revise |
| 16| Direct Equity | What stays, and why (watchlist) | keep (fix definition — D13) |
| 17| Mutual Funds | Divider | keep |
| 18| Mutual Funds | The fund book | keep |
| 19| Mutual Funds | **How we evaluate funds** — equity + hybrid frameworks | **new** |
| 20| Mutual Funds | The three-year test (alpha, 4 seasoned funds) | keep (refresh window) |
| 21| Mutual Funds | Category & AMC concentration **+ over/under-allocation overlay** | revise |
| 22| Mutual Funds | Three fund actions (nuanced) **+ honest overlap note** | revise (absorbs 22) |
| 23| The Plan | Divider | keep |
| 24| The Plan | **House-view fit** (merge today's 7 + 25 into one table) | revise/merge |
| 25| The Plan | **Cost — what you pay today + CoPilot** | **new** |
| 26| The Plan | **Tax impact** | **new** |
| 27| The Plan | **Deployment — where the money moves, with rationale** | revise |
| 28| The Plan | Before & after (the *only* today-vs-target table) | revise |
| 29| The Plan | Priority actions — order sheet + sign-off | keep (fix title/bridge) |
| 30| Back | Disclaimer (moved up to close the standalone core) | keep |

### Tier 2 — ANALYTICAL APPENDIX (append on demand; core reads cleanly without any)

| Module | Was | Include when |
|--------|-----|--------------|
| M1 Efficient frontier | 30 | client wants the risk-return case |
| M2 Quality vs price | 31 | client challenges valuations |
| M3 Factor profile | 32 | factor-aware client (*fix "six pillars" → five/seven, D24*) |
| M4 Growth projection | 33 | goal-planning (needs real goal inputs) |
| M5 Holdings in detail (68) | 34–51 | line-by-line ask; **doubles as the sell-rationale annexure** |
| M6 Equity register | 53–54 | compliance / audit trail |
| M7 MF register | 55 | compliance / audit trail (fix stranded 17th row — D10) |
| M8 Methodology & basis | 56 | **default-on**; required whenever any quant module shows |

**Advisor rule:** ship CORE + M8 by default; add M1–M4 for an analytical client; add M5–M7 only
when a full audit trail is asked for. The 17-slide M5 block is never presented live — it's the
leave-behind the core's sell table and spotlights link into.

**Two core-vs-optional dependencies to resolve** (a core slide must not need an optional one):
the deployment slide (27) references the efficient frontier's "steps left toward the frontier"
story, and "How we score" (4a) leans on the factor profile. Fix by keeping a **one-line
self-contained summary** of each in the core slide, with "detail in appendix M1/M3" as a pointer —
not a dependency.

**Redundancies to collapse:** merge house-view tables (today's 7 + 25) into one; make the exec
summary qualitative and let Before-&-after be the sole today-vs-target table; scope slide 8 to
equity single-name only (AMC row lives on 21, sector row on 9); have M5 omit Reliance/Titan
prose (or reduce to a pointer) so the spotlight paragraphs aren't printed twice.

---

## 6. Drafted content library (paste-ready)

### 6.1 IPS — "Your Investment Policy" (new slide 3, part A)

Standardised, risk-profile-keyed. Client's column highlighted; the rest is the reusable template.

| Sleeve | Conservative | Moderate | **Aggressive (this client)** |
|--------|-------------|----------|------------------------------|
| Domestic equity | 25–35% | 45–55% | 55–70% |
| Foreign equity | 5–10% | 10–20% | ~25% of equity (60:40 DM:EM) |
| Gold & silver | 5–10% | 5–10% | 5–10% (75:25 gold:silver) |
| Debt / arbitrage / cash | 45–60% | 20–35% | 5–15% |
| Style tilt | low-vol / quality | low-vol + value | low-vol and value favoured |
| Single-name limit (equity sleeve) | <5% | <6% | **<8%** |
| Single-AMC limit (funds) | <25% | <25% | <25% |
| Single-sector limit (equity) | <25% | <30% | <30% |

Policy strip: Risk profile · Horizon (7+ yrs) · Objective (long-term wealth creation) ·
Mandate type: **Non-discretionary (NDPMS) — Sell/Trim/Switch/Redeem/Hold only, never Buy** ·
Construction: core-satellite · Review cadence: quarterly. *All Aggressive-column numbers reuse
the house-view targets already on today's slides 7/25 and the limits on slide 8 — no new numbers.*

### 6.2 "Where you stand vs your policy" — gap board up front (new slide 3, part B)

| Policy standard | Where you are today | Status |
|-----------------|---------------------|--------|
| Single-name <8% (equity sleeve) | Titan 11.2%, top-10 = 32.0% of book | **GAP** (top-10 breach) |
| Single-AMC <25% (funds) | HSBC 36.7% | **GAP** |
| Single-sector <30% (equity) | largest 31.2% | **GAP** |
| Foreign equity ~25% of equity | ~9.7% of equity (5.2% of book), DM-light | **GAP** |
| Gold & silver 5–10% sleeve | residual 0.6% ETF, no sized sleeve | **GAP** |
| Every holding scores ≥40 | 19 of 68 stocks score <40 (14% by value) | **GAP** |
| Funds beat benchmark over 3Y | all 4 seasoned funds beat benchmark | **STRENGTH** |

### 6.3 Executive summary — gap → action → impact (rebuild slide 5)

KPI strip (4 tiles): `₹[total]` reviewed · `68 / 17` stocks/schemes · `32.0%` top-10 (breach) ·
`19 of 68` rated Sell (14% by value).

| # | Gap | Action that closes it | Impact |
|---|-----|-----------------------|--------|
| 1 | Top-10 = 32%; Titan at the single-name limit | Trim Titan toward <8% (equity sleeve) | frees ₹7.9 L; largest name within limit |
| 2 | 19 stocks <40, incl. Reliance at 27 | Run the Sell programme | ₹0.59 Cr proceeds; Sell-weight 13.7% → 0% |
| 3 | Foreign equity ~9.7% vs ~25% | Redeploy toward foreign equity, 60:40 DM:EM *(direction, on instruction)* | steps toward 25% |
| 4 | No gold/silver sleeve | Open a small 75:25 sleeve *(direction)* | adds the missing diversifier |
| 5 | Fund book: HSBC 36.7%, a Regular dup, a sub-scale 2nd small-cap | Switch Nippon→flexi; redeem ICICI Regular; exit Bandhan | 17 → 15 schemes |

Strength line (not an action): *"The fund book is sound — every scheme with a 3-year record beats
its benchmark; the three fund actions are structural, not performance."*
Proceeds bridge footer: `₹0.59 Cr Sells + ₹0.08 Cr Titan trim = ₹0.67 Cr to redeploy; +₹0.06 Cr
fund actions = ₹0.74 Cr total reorganised (order sheet, p.29).` **Delete the old "two names above
11%" line.**

### 6.4 Mandate & method (revise slide 4) + core-satellite panel

Benchmark block — split the conflated label:

| | |
|---|---|
| Scoring benchmark | NIFTY-750 cross-sectional percentile (Ionic Quant Scorecard) |
| Allocation reference | [House-view owner], Dec 2025 *(replace "Asset X")* |

Client-understanding block (advisory team fills): who the family is, source of wealth, liquidity
events, constraints, ESG/sector exclusions if any — the "understanding" content the reviewers
said the advisory team can supply.

Core-satellite panel (plain language): *"**Core** (the majority) holds steady, low-turnover,
high-quality positions that anchor the portfolio. **Satellites** (smaller sleeves) take
deliberate tilts — a sector, a factor, a theme — sized to add return without moving the whole
book. We review whether each satellite still earns its place; the core changes rarely."*

### 6.4b How we score a stock (new slide 4a) — machine + human, equal billing

Left half — **the pillars** (5 families, read over 3-year and 1-year horizons; the growth and
price-trend pillars are horizon-split, which is why the scorecard shows seven scored columns —
**reconcile slide 32's "six quant pillars" label to match**):

| Pillar | Measures | Built from |
|--------|----------|-----------|
| Quality | business durability | ROE, ROCE, margins, accruals |
| Value | what you pay | P/E vs peers and vs the stock's own history |
| Growth (3Y / 1Y) | structural + recent fundamental growth | revenue/earnings trend, latest quarter |
| Price-trend / momentum (3Y / 1Y) | long and recent price behaviour vs market | — |
| Sector / macro | tailwind or headwind | house sector read (0–100) |

Combine strip: *"Each pillar is a 0–100 cross-sectional percentile across the NIFTY-750 universe
(751 names). Horizons blend **0.60 × 3-year + 0.40 × 1-year**. A name is a **Sell below 40** on
the binding (lower) horizon; 40+ is a Hold. **The model never issues Buy.**"*
BS-gate callout: *"Before scoring, every non-financial name passes a balance-sheet gate — GREEN
(clean, 531) / AMBER (watch, 50) / RED (stressed, 49); financials gated separately (121). A RED
gate caps quality regardless of other pillars."*

Right half — **the human overlay** (the anti-"score-worship" half the reviewers asked for):
*"A score starts the conversation; it doesn't end it. Every flagged name is read by an analyst
before it reaches this deck. The analyst may **argue a Sell up to a Hold — never a Hold down to a
Sell**. Scores are point-in-time and can be stale or wrong. Where the model has no coverage
(recent listings, ETFs, demerged entities) there is no score — the desk carries those on
judgement."* Sign the spotlight footers *"Reviewed by: [analyst] · Ionic Equity Desk."*

### 6.5 Sell rationale (revise slide 15 + build annexure)

Add an **"Analyst view"** one-liner column to the sell table (e.g. Reliance — *"Concur — size
risk, not quality; reduce, not zero"*; Jio Financial — *"Concur — growth real, profitability
isn't"*; VIP — *"Concur — loss-making, weakest name in book"*). Point the footer at a new
**per-name sell annexure** (appendix M5) using this 4-part template:

> **[Name] — [wt]% · score [X] · [sector]** — **1. The number** (binding horizon + weakest
> pillar[s]); **2. The fundamental** ("X does not justify Y" on ROE/PE/growth); **3. The
> judgement** (why the desk agrees, or the caveat); **4. The action** (exit vs reduce, and where
> the proceeds go).

The full prose already exists on today's holdings slides 35–51 — this is relocate-and-tighten,
not new writing. **Align the verb first (D8):** slide 16's 13.7% / ₹0.59 Cr assume *full* exits,
but the holdings notes say "reduce" for 7 names — pick one, or the proceeds are overstated.

### 6.6 Sector & market-cap scope (merge slides 9+10)

Standing caption (promote out of the source line): *"**Scope: direct equity only (₹2.33 Cr, 68
stocks).** The ₹2.00 Cr fund book (46% of the portfolio) is shown separately in the blended view;
stock-level fund constituents aren't available, so fund exposure is at category level (p.18)."*
Add a **blended (stocks + fund category proxy)** panel so the client sees true exposure — today's
"86.7% large-cap" is a direct-equity fact, but the fund book is small-cap-heavy (38.3%) and infra-
thematic, which pulls the *portfolio* mix down and toward industrials. Label the blend "indicative
proxy."

### 6.7 MF & hybrid evaluation framework (new slide 19 + overlay on 21)

**Equity funds** — three performance axes + a house-preference tier gate:

| Axis | Good | Fail |
|------|------|------|
| Upside capture (UCR) | ≥100 | materially <100 |
| Downside capture (DCR) | <100 (loses less than market) | ≥100 |
| Capture spread (UCR−DCR) | positive, wider better | ≤0 |
| Rolling consistency (% of 3Y/1Y windows beating benchmark) | ≥60% | <50% |

Tier gate (knowable today, no NAV needed): **Preferred** = Flexi Cap · Factor/Passive (value,
low-vol) · Index; **Neutral** = Mid/Small/Thematic sized deliberately; **Dis-preferred** =
**Multi Cap** (SEBI forces ≥25% each large/mid/small — removes manager cap-sizing) and **Active
Large Cap** (persistent alpha rare — prefer Factor/Passive). Rule on the slide: *PREFER if DCR<100,
spread positive, rolling-win ≥60%, Preferred tier; REPLACE if DCR≥100 OR rolling-win<50% OR
Dis-preferred with no capture edge.* The two house rules go live on the actual book: Nippon
(Multi Cap) is switched *despite* +9.4pp alpha; the value index funds are affirmatively kept
(value favoured) while the momentum index funds are held-but-WATCHED (momentum on hold).

**Hybrid funds** — judged on risk, not equity alpha:

| Axis | Good |
|------|------|
| RAR (Sharpe **and** Sortino) | above category median on both |
| Max drawdown | materially shallower than a pure-equity comparator; arbitrage ≈ 0 |
| Worst rolling-1Y | contained; arbitrage never negative |

Applied: ICICI Multi-Asset (Direct) = core diversifier, validate it cushions vs equity; Tata
Arbitrage = cash-plus, fails if any real drawdown appears; ICICI Multi-Asset (**Regular**) = risk
identical to Direct, so the only differentiator is the trail cost → redeem.

**Overlay on over/under-allocation (new 2×2 on slide 21):** read every fund's verdict *against*
whether its sleeve is over/under the house weight.

| | Sleeve UNDER-weight | Sleeve OVER-weight |
|---|---|---|
| **Fund strong** | **GROW** (top-up) — e.g. JM Flexicap | **KEEP as primary, trim sleeve** — HSBC small-cap |
| **Fund weak/flagged** | **UPGRADE** (re-select, don't just add) — International (under & under-3Y) | **CUT FIRST** — Bandhan (sub-scale, over), Nippon (dis-preferred) |

> All capture/consistency/Sharpe/drawdown cells read **"pending Q3 NAV pull"** until the feed is
> refreshed — the tiers, plan, scale and sleeve fit are decidable today; the performance numbers
> are not. Say so on the slide.

### 6.8 Three fund actions — enriched rationale (slide 22)

- **SWITCH Nippon Multi-Cap → flexi:** *passes on performance (+9.4pp); fails only on tier —
  Multi Cap's forced ≥25% each cap removes the cap-sizing the "Flexi > Multi" rule exists to keep.
  Overlay: moves a 0.6% stub toward the under-weight Preferred flexi sleeve. Not a performance sell.*
- **REDEEM ICICI Multi-Asset (Regular) → Direct:** *risk metrics identical to the Direct plan
  already held; the only difference is the Regular trail — a permanent negative carry with no risk
  offset. Cost cleanup, sleeve weight unchanged.* **(Net-of-tax check — see §6.12: this triggers a
  small STCG now; confirm the trail saving beats the STCG on ₹2.0 L before actioning.)**
- **EXIT Bandhan Small-Cap → HSBC carries the sleeve:** *also passes on performance (+8.0pp);
  fails on overlay — Small Cap is the single most over-weight sleeve (38.3%) and a ₹3.2 L second
  fund beside a ₹73.5 L primary adds cost and mechanical overlap. Caveat: HSBC is under-3Y and
  unscoreable, so keeping it is a **scale** call — re-test HSBC vs Bandhan on capture/consistency at
  Q3 before finalising the primary.*

### 6.9 Deployment with rationale (rebuild slide 27)

*"Every rupee freed has a destination, and every destination has a reason."* One row per sleeve;
amounts foot to the **₹0.67 Cr deployable**, not ₹0.74 Cr. Expressed as **direction on client
instruction** (§3), not named buys.

| Destination sleeve | Indicative ₹ L | Why — house view · gap closed · risk reduced |
|--------------------|----------------|----------------------------------------------|
| Low-vol / value domestic | ~40 | favoured tilt; book is value-light (p.32); replaces 19 sub-40 names → lowers quality risk |
| Foreign equity, 60:40 DM:EM | ~18 | the larger open gap (~9.7% vs 25%); cuts India-only concentration; first step, not a one-review close |
| Gold & silver, 75:25 | ~9 | no sized sleeve today; low-correlation diversifier; steps the book toward the frontier |
| Cash buffer (staged) | remainder | never assumed fully invested day one; staged for entry + tax timing |
| *Fund-book reshuffle (not new-sleeve cash)* | ~6.3 | Nippon→flexi, ICICI Regular→Direct, Bandhan→primary; internal, structural |

Proceeds bridge (top of slide): the three-number table from §0. **Fix the footnote** — stop
calling ₹0.74 Cr "proceeds"; call it total reorganised. Gap-tracker footer keyed to slide 24 so
each row visibly discharges a house-view gap. **Reconcile the frontier (D)** — slide 30 mentions a
"debt cushion" that appears in no deployment row: either add a debt/cash-cushion row or drop the
phrase from slide 30.

### 6.10 Fund overlap — replace the broken slide (slide 22 → honest panel)

> **Fund overlap — pending look-through data.** *We hold the analysis rather than force a number.*
> Stock-level holdings aren't yet available for any of the 14 equity schemes, so a name-by-name
> overlap grid can't be produced this quarter. Rather than substitute mismatched index constituent
> lists (which would misstate factor funds as broad-market baskets), we flag this as a data gap.
> **What we can already say:** the four passive index/factor funds overlap each other by
> construction — that's index mechanics, not duplicated conviction, and not a diversification
> failure. The redundancy worth removing is structural and already on the action list (p.22): the
> sub-scale second small-cap and the Regular-plan duplicate.
> **Next step:** pull each scheme's latest AMC factsheet / MFCentral & RTA holdings for a true
> look-through read at Q3.

*Q3 build spec:* pairwise overlap heatmap (weighted common-holding %), a **combined look-through
top-10 single stocks across the whole fund book** (links back to the direct-equity concentration
on slide 8 — the "do I own 7% Reliance across five funds?" number), and a mechanical-vs-conviction
label.

### 6.11 Cost — "What you pay today" + CoPilot (new slide 25)

*Honest framing: the book is already ~99.5% direct plans, so plan conversion is a small win (one
₹2.0 L line). The durable saving is consolidation (17→15 schemes) + one transparent fee.* Three
panels: (1) **recurring annual cost** — Direct-plan TERs `[to source]`, the one Regular trail,
self-held equity (nil ongoing), any PMS/advisory fee `[to source]`, all-in in ₹ and bps;
(2) **one-time execution cost** — STT (0.1% sell side on ₹67.3 L), brokerage/GST/stamp, impact
(minimal, large-cap), MF exit loads (likely nil); (3) **with CoPilot** — trail eliminated, fewer
schemes, single transparent fee. Footer sets the honest expectation. **Route past compliance (§3).**

### 6.12 Tax impact (new slide 26)

Rate strip (FY26-27; confirm with adviser): equity LTCG (>12m) **12.5%** above the **₹1.25 L**
annual exemption; STCG **20%**; switch = redemption for tax. **Block A** — fund actions (computed:
Nippon switch LTCG, ICICI Regular STCG, Bandhan LTCG; ₹6.3 L). **Block B** — equity sells
(₹67.3 L) **"not computable until demat lot dates/costs supplied."** Minimisation levers: use the
₹1.25 L exemption **every FY** (split the programme across 31 March to shield ~₹2.5 L); **harvest
losses** (VIP, Swiggy, Tata Motors PV, Jubilant — candidates, confirm from lots) against gains;
prefer LTCG lots over STCG. **Tax-aware sequence:** (1) this FY — harvest losses, then LTCG up to
₹1.25 L, then the highest-conviction Sells (Reliance) regardless of tax; (2) this FY — the two
small fund redemptions; (3) next FY — remaining LTCG sells + Titan trim on a fresh exemption; the
Nippon switch can wait (structural). Boxed ask: *"One file closes this gap — share the demat trade
file and the next review computes exact per-lot tax."* This makes slide 29's "sequence sells
tax-aware per p.26" actually point at a sequence.

---

## 7. Data dependencies & sequencing

Three flagship slides are **defined-but-blank** until data arrives. Say this to the reviewers
plainly rather than presenting skeletons as finished:

| Slide | Blocked on | Decidable now without it |
|-------|-----------|--------------------------|
| MF/hybrid framework (19) | NAV feed refresh (alpha window is stale at Dec-2024; only 4/17 funds have 3Y) | tier, plan, scale, sleeve fit, the 3 actions |
| Cost (25) | fee/TER schedule per scheme + any advisory fee | the structure, the honest "already direct" framing |
| Tax — equity block (26) | demat trade file (lot dates + costs) | fund-action tax, exemption/harvest/sequence logic |

**Ask order:** demat trade file (unblocks tax + confirms harvest set) → fee schedule (unblocks
cost) → NAV refresh at Q3 (unblocks fund performance columns + fund-overlap look-through).

---

## 8. Full QA defect register (23)

| # | Slide | Issue | Severity |
|---|-------|-------|----------|
| 1 | 22 | Leaked draft prose; self-contradicting overlap claim | **Critical** |
| 2 | 8 | "Names above 8% = 3" — undisclosed denominator switch (correct whole-book = 0; equity-sleeve = 3) | **Critical** |
| 3 | 3 | "two names above 11%" — no name >6.05% whole-book; unsupported "(p.8)" citation | **Critical** |
| 4 | 3/16/27/29 | Two unreconciled "proceeds" (₹0.59 vs ₹0.74 Cr) | **Critical** |
| 5 | 29 | Duplicate title "Priority actions / Priority actions" | High |
| 6 | 28 | "Largest name 6.0% → 8.0% guideline" reads as *raising* the top holding; mixes bases | High |
| 7 | 14/35 vs 16/29 | Reliance: "reduce toward market weight" (spotlight) vs "full exit" (order sheet) | High |
| 8 | 35–51 vs 16/29 | 7 sells say "reduce" (partial) but proceeds sum *full* weight — overstated | High |
| 9 | 12/13/17 | Hold-count conflict: 44 (treemap) vs 49 (watchlist intro) vs 63 scored + 5 unrated | High |
| 10 | 55 | 17th scheme (UTI Momentum 30) stranded below the source line, outside the table | High |
| 11 | 3/4/7/25 | "Asset X house view" reads as an unfilled placeholder | Medium |
| 12 | 15/35 | Titan "best growth in the book, 84" false — Groww 96, BSE 98, Kaynes 94 exceed it | Medium |
| 13 | 17 | Watchlist defined as "all 40–46 Holds" but lists 8 of ~15 | Medium |
| 14 | 55 | Momentum index funds mis-tagged "Flexi Cap" / "Large & MidCap" | Medium |
| 15 | 2/11 | Nav item "The top ten" points to slide 13, titled "The equity book"; no such slide | Medium |
| 16 | many | Systemic name/sector truncation ("Godrej Consumer Produc", "Information Technolo") | Medium |
| 17 | 7/28/25 | Foreign-equity gap compares ~25% *of equity* against ~5% *of book* (mixed base) | Medium |
| 18 | 22 | "NIFTY 500 … (749 names)" — 749 is the ~750 universe, not NIFTY 500 | Low |
| 19 | 7/40 | "No gold sleeve / GAP" vs slide 40's 0.57% Gold BeES ETF | Low |
| 20 | 29 | Action badges render detached from the ACTION column | Low |
| 21 | 20/56 | Alpha window Dec-2024 is ~19 months stale vs the Jul-2026 cover | Low |
| 22 | 21 | AMC/category charts omit small slices; neither foots to 100% | Low |
| 23 | 27/29 | "Total redeployed 73.6" labels internal fund actions as redeployable proceeds | Low |
| 24 | 32 | "six quant pillars" vs the five-family / seven-column scoring model | Low |

---

*Prepared as an improvement plan + reusable template. Next step available on request: build the
revised CORE deck (slides 1–30) as a working .pptx against your brand template, or draft the full
per-name sell annexure (M5) from the existing holdings prose.*
