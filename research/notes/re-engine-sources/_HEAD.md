# THE INDIA REAL-ESTATE EVIDENCE PACK
### Sources, literature and country patterns — the head start for the prediction-engine thread

**Written 2026-09-11 · The Cycle Program · principal gaurav@ionic.in · governed by
`research/CONTRACT.md` · ledger entry `RE-SOURCES` (zero run cells, census unchanged at 1,399)**

**What this is.** The companion to `research/register/handoff-prompt-india-realestate-engine.md`
(v3.1). The handoff prompt says *what to build and in what order*. This says **what is already
known** — the international forecasting literature and its honest failures, the country-by-country
data regimes and the four templates India could copy, the India source estate portal by portal, the
under-reporting econometrics, and the free geospatial stack. Read this first and you start at the
research frontier; skip it and you will spend a fortnight rediscovering that the 18-year property
cycle fails its own test and that Zillow lost money buying houses with its own model.

**What this is not.** Not a roadmap, not a plan, not a task list — those live in the handoff prompt
and in `research/frontier/india-property-plan.md`. Nothing here is a commitment to build anything.

---

## §0 — THE EVIDENCE STANDARD, AND HOW TO READ THE TAGS

**Binding, and identical to the standard the CN programme published under.** `WebFetch` is
EGRESS-BLOCKED for every domain in the environment this pack was assembled in. Only `WebSearch`
worked. **Every external claim in §§1-4 therefore rests on search-result snippets that could not be
checked against a primary page.** Thirty agents produced it: 22 wrote cited dossiers, 3 attacked
those dossiers adversarially, 4 synthesised, 1 asked what was missing.

| Tag | Means | How to treat it |
|---|---|---|
| `[DESK PRINT]` | Computed by this desk from a vaulted dataset, pre-registered, desk-verified. Carries a ledger entry ID. | **The only evidence-grade material in this document.** Citable as a print. |
| `[2-SOURCE]` | Two independent search results agreed. | Good enough to design on. Verify before publishing a number. |
| `[1-SOURCE]` | One source. | Treat as a lead, not a fact. |
| `[RECALL — unverified]` | From a model's memory; search did **not** confirm it. | **Assume it may not exist.** Chase it or drop it. Never cite it. |

**The pack carries its own corrections.** §6 is the audit scoreboard: claims the fact-checkers
refuted or downgraded, left visible rather than silently edited out, per the preservation rule.
Anything the auditors refuted has been removed from §§1-4 or corrected in place — but it stays
listed in §6 so a reader can see what the first draft got wrong.

**One structural warning about a pack like this.** The highest-probability error is not a wrong
number, it is a **citation that does not exist** — a plausible author-year-journal triple invented
by a language model and then repeated with confidence. That is why a third of the agent budget here
went to adversarial citation checking before a word of synthesis was written, and why §6 exists.

---

## §00 — WHAT THIS DESK ALREADY KNOWS ABOUT PROPERTY

**Read this section before the literature.** The desk has been working on property since the atlas
phase. Four on-desk documents outrank everything in §§1-4 because they are desk-grade rather than
snippet-grade, and one of them has already done most of the India data engineering.

### The documents of record, in reading order

1. **`research/cycles/fincycle-deep/partC-data.md`** (460 lines) — *"Data engineering: measuring
   India's property cycle, free."* **This is the single most valuable file in the repo for the new
   thread and it already exists.** It covers: RBI HPI provenance and the 2022-23/18-city rebase
   break sitting inside it now; NHB RESIDEX's two dated breaks and its **two structurally different
   price concepts** (an assessment-price leg that is a lender's number and a market-price leg that
   is not, which must never be blended with RBI HPI into one series); bank-plus-HFC housing credit;
   RERA and the supply side; registration counts and stamp duty as the transaction-side series; the
   circle-rate honesty note; a **vintage/point-in-time hazard table**; the L12 India pipeline; and
   §C.9, an explicit list of what cannot be measured free. Do not re-derive any of this.
2. **`docs/cycles/13-real-estate.md`** — the real-estate-cycle merge monograph. Kills the folk clock
   (see below), keeps the mechanism.
3. **`docs/cycles/12-financial-cycle.md`** (seat L12) — the credit-property cycle, seated, with the
   India degradation path designed and tested for a short HPI.
4. **`docs/learn/artifacts/india-property-atlas.html`** (README row 65) and
   **`china-property-crash-atlas.html`** (row 64), with their plans in `research/frontier/` and
   their dossiers in `research/notes/india-dossiers/` and `china-dossiers/`.

### The prints any new property work must not contradict or rediscover

Every row is `[DESK PRINT]` with its ledger entry. These are the desk's own numbers, computed from
vaulted data and desk-verified on a second code path.

| # | Print | Entry |
|---|---|---|
| 1 | **The 18-year property cycle FAILS its own pre-registered test.** 109 real house-price peak spacings across 17 JST countries: median **14y**, IQR 10-17y, full range 8-45y, and only **45%** land in the pre-declared [14,22]y window against a ≥50% bar — on a construction deliberately biased *toward* the claim. Kuznets 15-25y building swings fail cleanly too (investment/GDP spacings median 11y, 25% in-window). The slowness is real; the *clock* is not. | RE1, RE2 |
| 2 | **Credit-property amplification is the cleanest sign-consistency pass in the whole project** — 17/17 countries, median correlation **+0.40**. Cycle length lengthened 11y→13y post-1985. But crisis-at-peak *dating* is weak on a real-time construction (1.2-1.3x), which is the seat's own evidence for **states, never dates**. | FC1-FC3 |
| 3 | **A sustained 20%/yr real property boom has never happened in the modern era of the JST panel.** Post-1970: **0.00% of 884** five-year windows cleared 20%/yr real; 0.45% cleared 15%/yr. The post-1970 panel maximum is **Ireland 1999 at +17.25%/yr real** — and Ireland 2006 is the worst modern bust in the episode list at **-55.7%**. The fastest modern boom and the worst modern bust are the same country, seven years apart. | IN-D1 |
| 4 | **Hot markets stay hot at five years, which refuted the desk's own mean-reversion prior.** Next-5y real return after a ≥15%/yr real window: **+9.65%/yr**; after ≥20%/yr: **+11.16%/yr**. Those same windows carry roughly **2x** crash odds (2.02x at ≥10, 2.03x at ≥20; the ≥15 rung prints 1.03x on 45 windows and is recorded as a miss, not smoothed). Consumption: **ride-it-but-size-it, never in-or-out.** | IN-D1 |
| 5 | **Indian nominal property talk is mostly real, not money illusion** — the opposite of the registered prior. On hyperinflation-clean windows, 20%/yr nominal has typically meant about **+12%/yr real** (mean real +12.42 vs nominal +23.17%/yr; inflation supplied 46% of the headline; only **2.3%** of hot nominal windows were real-negative). | IN-D2 |
| 6 | **The base rate for a property crash: median -34.2% real over 6.5 years** across 48 episodes, 18 countries, 1870-2020; modern era **-32.0% over 5.5y**. | CN-D1 |
| 7 | **Busts are NOT slower than booms** — the registered "gentle deflation" bar missed. Velocity ratio **1.12x** full sample, **0.99x** modern. There is no slow-deflation discount. | CN-D1 |
| 8 | **A bigger boom buys SPEED, not depth.** Depth gap only **3.8pp** between big and small booms, but the unwind runs **3.5pp/yr faster**. So the *exit plan* matters more than the entry level. | CN-D4 |
| 9 | **Rental yield is the placement instrument.** It compresses **-0.83pp** into the peak and expands **+1.53pp** to the trough — which is how the desk placed tier-1 China at roughly a third of a crash when the price index alone was ambiguous. | CN-D2 |
| 10 | **The best-known credit early-warning indicator has an 87.2% false-alarm rate.** Mortgage-credit growth lifts 3-year crash odds **1.72x** — and cries wolf 87.2% of the time. Public-debt growth reads *backwards* (0.23x; it rises *after* busts). Anyone selling you a property-crash predictor is selling you this. | CN-D3 |
| 11 | **Equities lose -13.7pp excess real in the first year of a housing bust**, double if banks break, and are recovered by year five — reproducing CI-D5 on a different construction. Property busts are an equity-book event, not only a property-book event. | CN-D5, CI-D5 |
| 12 | **In the high-and-rising-inflation state, housing is the second-best asset and equities are the worst**: gold **+9.6** > housing **+6.8** >> equity **-3.0** > bonds **-5.6** (%/yr real). This is the one macro state where an Indian property overweight has desk support. | CI-D2 |
| 13 | **Announcement moves the price; completion merely confirms it.** Panvel **+76%** since 2021, mostly *before* the first flight at Navi Mumbai; the Jewar belt **+142-158%/5y**, mostly before flying; Delhi-Dehradun Expressway **+23% in the nine months before opening**; Samruddhi corridor land ≈**3.7x** pre-completion. Completed MMR infrastructure then yields only a smaller continuing **8-15%/yr** premium. **Corollary: every public, dated feature is already partly in the price.** | IN dossiers |
| 14 | **Every listed Indian REIT yields below the 10-year G-sec, and no residential REIT exists in India at all.** India's property carry is *more* negative than China's was at its peak. | IN dossiers |
| 15 | **The cost drag is the whole game.** Entry ~9% (stamp duty 5-7%, registration ~1%, brokerage 1-2%, diligence), exit ~1.5%, round trip **~10.5%**, holding ~2.2%/yr → **~21.5% over five years**. So: a locality doing 20% cumulative over five years nets **-0.30%/yr nominal, -4.60%/yr real**; break-even needs **21.5% gross**; matching the desk's own standing book (+11.46% CAGR) needs **93.5% gross**. Every forward distribution this project publishes must be shown **gross and net**. | handoff §1 |
| 16 | **Point forecasts are forbidden, and the desk's own results say why.** The ER-arc pooled expected-return equations failed out-of-sample at every horizon once purged and honestly benchmarked; single-country kitchen sinks exploded at **-389%**; Goyal-Welch binds fully. | ER-D4b, ER-D7 |

**How prints 3, 4 and 15 fit together, because together they are the project's actual thesis.** A
20%/yr five-year Indian property call is a *bubble-velocity* call, not a growth forecast — it has
never happened in the modern panel in real terms. A hot micro-market should nonetheless not be
dismissed on mean-reversion grounds, because at five years the base rate says it keeps running, at
roughly double the crash odds. And whatever it returns, the investor keeps it only after a ~21.5%
five-year cost wedge. **"Will prices rise?" is the wrong question. "Will prices rise enough to beat
21.5% plus the alternative?" is the question, and it has a much smaller yes-set.**

