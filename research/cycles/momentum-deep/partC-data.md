# Part C — Data engineering: building Indian momentum from bhavcopy

v1.0 · 2026-09-01 · Extends `docs/masterplan/A-data-catalog.md` §2 blocks A (NSE/BSE core market
data), B (index data), C4 (corporate actions) — that appendix is the source of truth for access
paths, priorities, and the fixture-governance rules (WORM manifest, vintage tagging); this part
goes one level deeper on the two price-only ladder inputs that are this program's cleanest,
first-built signal book (`config/ladder.yaml L3_momentum_composite`, `L4_tsmom_index_gold`) and
the `config/sleeves.yaml momentum` construction it feeds: exact file/field names, the
corporate-action adjustment math a build script needs, the survivorship-reconstruction procedure,
and the construction-grade conventions `research/dossiers/01-momentum-reversal.md` (the theory/
evidence dossier) correctly left unspecified. Consumes: `config/ladder.yaml` L3/L4, `config/
sleeves.yaml momentum`, `config/costs.yaml`. Feeds: this program's momentum econometrics and
algo-extraction parts (construction inputs), `ingest/pull_nse_bhavcopy.py` and the ingest kit
generally (see the closing note on scripts this part shows are still missing). Everything below
was checked this pass by web search (snippet-level, per Contract prior #11) — **with one upgrade**:
`raw.githubusercontent.com` is confirmed open at this environment's egress proxy (per `research/
OPEN_QUESTIONS.md`'s 2026-09-01 mirror-authorization note), so one UDiFF bhavcopy file was fetched
and read directly rather than inferred from search snippets — that field table below is
fetched-and-verified, not snippet-verified, and is flagged as such. `nseindia.com`,
`niftyindices.com`, `faculty.iima.ac.in`/`web.iima.ac.in`, and `zenodo.org` were all re-confirmed
blocked at the proxy this pass. Anything not independently confirmed carries **[VERIFY]**.

---

## C.1 Price data — NSE bhavcopy, the UDiFF break, and the BSE cross-check

**The single governing fact**: NSE's daily cash-market file changed schema on **2024-07-08**
(old format ran in parallel through 2024-07-05, then was discontinued per **NSE Circular No.
62424, dated 2024-06-12**, "Standardization of Exchange to Member Interface files in Unified
Distilled File Formats"). `ingest/pull_nse_bhavcopy.py` already switches URL scheme correctly at
this boundary (`UDIFF_BOUNDARY = date(2024, 7, 8)`) — **but it only fetches raw files; it does
not parse or normalize columns**, and the two eras use genuinely different field names, not just
a different file path. That crosswalk does not exist anywhere in this repo yet; it is specified
here for the first time.

**How far back, per exchange (free, daily, machine-readable):**

| Exchange/segment | Free daily bhavcopy starts | Format-break date(s) |
|---|---|---|
| NSE cash (CM) | NSE cash trading launched **1994-11**; the archived CSV bhavcopy series is commonly cited as available from the mid-1990s, with several third-party tools defaulting a bulk pull to **1996-01-01** as the practical start — **[VERIFY exact earliest archived date; 1994 vs 1996 is not resolved this pass]** | legacy→UDiFF: **2024-07-08** |
| NSE F&O | index futures from **2000**, stock F&O from **2001** | same UDiFF boundary, same date |
| BSE cash | BSE's own historical-download archive commonly reaches back to **~1997** | BSE's production bhavcopy URL is itself now UDiFF-named — `bseindia.com/download/BhavCopy/Equity/BhavCopy_BSE_CM_0_0_0_{yyyymmdd}_F_0000.CSV` (confirmed this pass) — **[VERIFY] BSE's own legacy→UDiFF transition date**; the naming convention strongly suggests BSE underwent an analogous SEBI-driven standardization, not independently dated this pass. **This is new to the catalog**: A4 does not currently flag that BSE needs its own format-break handling, not just its own URL. |

**Field tables.** Legacy NSE CM bhavcopy (13 columns, comma-separated, confirmed by multiple
independent secondary descriptions this pass): `SYMBOL, SERIES, OPEN, HIGH, LOW, CLOSE, LAST,
PREVCLOSE, TOTTRDQTY, TOTTRDVAL, TIMESTAMP, TOTALTRADES, ISIN`.

UDiFF CM bhavcopy — **fetched directly** this pass (`nse-cm-bhavcopy-2024-07-25.csv`, a GitHub
mirror of NSE's own `BhavCopy_NSE_CM_..._F_0000.csv.zip`), confirming the exact header row and a
sample data row:

```
TradDt, BizDt, Sgmt, Src, FinInstrmTp, FinInstrmId, ISIN, TckrSymb, SctySrs, XpryDt,
FininstrmActlXpryDt, StrkPric, OptnTp, FinInstrmNm, OpnPric, HghPric, LwPric, ClsPric, LastPric,
PrvsClsgPric, UndrlygPric, SttlmPric, OpnIntrst, ChngInOpnIntrst, TtlTradgVol, TtlTrfVal,
TtlNbOfTxsExctd, SsnId, NewBrdLotQty, Rmks, Rsvd1, Rsvd2, Rsvd3, Rsvd4
```

Confirmed directly from the sample row (BASF India, `FinInstrmTp=STK`): for a cash-equity row,
`XpryDt`, `StrkPric`, `OptnTp`, `UndrlygPric`, `SttlmPric`, `OpnIntrst`, `ChngInOpnIntrst` are all
**blank** — UDiFF is one shared schema across CM/F&O/SLB segments, with the F&O-only fields left
empty on equity rows, not a CM-specific column set. This matters for parser design: a naive
`len(columns)` check cannot distinguish CM from F&O rows inside a mixed pull; key on `Sgmt`/
`FinInstrmTp` instead.

**Legacy → UDiFF field crosswalk** (the parser this Part specifies, not yet built):

| Concept | Legacy field | UDiFF field |
|---|---|---|
| Trade date | `TIMESTAMP` | `TradDt` |
| Symbol | `SYMBOL` | `TckrSymb` |
| Series | `SERIES` | `SctySrs` |
| ISIN | `ISIN` | `ISIN` |
| Open/High/Low/Close | `OPEN/HIGH/LOW/CLOSE` | `OpnPric/HghPric/LwPric/ClsPric` |
| Last traded price | `LAST` | `LastPric` |
| Previous close | `PREVCLOSE` | `PrvsClsgPric` |
| Total traded qty | `TOTTRDQTY` | `TtlTradgVol` |
| Total traded value | `TOTTRDVAL` | `TtlTrfVal` |
| Total trades | `TOTALTRADES` | `TtlNbOfTxsExctd` |
| *(no legacy equivalent)* | — | `FinInstrmTp`, `Sgmt`, `Src`, `SsnId`, `NewBrdLotQty` — new market-structure metadata, not price data |

Normalize both eras into one internal schema (`date, isin, symbol, series, open, high, low,
close, volume, value, trades`) before anything downstream (momentum ranks, ADV, corporate-action
adjustment) touches the data — a script built only against one era's column names silently
breaks, not loudly, across 2024-07-08.

**BSE as cross-check/fallback**: independent scrip-code system (numeric, not the NSE symbol),
so any NSE↔BSE join must run through ISIN, with a maintained NSE-symbol↔BSE-scrip-code↔ISIN
crosswalk (build once from a corporate-actions-fed process, per A4). Used for (a) coverage where
a name trades BSE-only, (b) an independent second read on a corporate-action-adjusted price
series (§C.2's TRI test is the *index-level* check; a same-day NSE-vs-BSE close comparison is a
cheap *name-level* check that costs nothing once both bhavcopy streams are pulled).

**The ISIN-vs-symbol keying problem.** NSE symbols are reused and reassigned across renames,
series-flag changes (`EQ` vs `BE`/`BZ` trade-for-trade, ASM-tightened series), and mergers — a
raw symbol-keyed panel silently splices two different companies' histories at a rename. ISIN is
the correct key for continuity **but is not itself perfectly stable across the full corporate-
action lifecycle**: a merger typically extinguishes the acquired entity's ISIN; a demerger issues
a **new** ISIN for the spun-off entity while the parent's ISIN continues. The only complete fix is
a maintained symbol↔ISIN↔corporate-action crosswalk built from the same C.2 corporate-actions
feed, keyed to remain valid across a rename event, not a static ISIN lookup pulled once.

---

## C.2 Corporate actions — the hard problem for momentum

**Where it lives (free).** NSE: `nseindia.com/companies-listing/corporate-filings-actions`
(confirmed reachable by search this pass; segment-filterable equity/SME/debt/MF; **blocked for
direct fetch in this environment**, so its exact CSV-export mechanics are unconfirmed —
**[VERIFY]** on first live contact). An unofficial but widely-used Python wrapper (`nse` /
`NseIndiaApi`) documents an `.actions(segment, symbol, from_date, to_date)` method hitting an
internal NSE JSON endpoint — confirms the *parameter shape* (segment/symbol/date-range filtering
is possible) but the **exact endpoint URL was not independently confirmed this pass**
**[VERIFY]**. BSE mirrors the same disclosures under its own corporate-actions page; the
production English-language URL was not pinned down this pass (only a Gujarati-language mirror
and a `mock.` test-environment page surfaced in search) — **[VERIFY exact production BSE corp-
action URL** on first contact, budgeting extra reconnaissance per the data catalog's existing
caution on C4].

**Event types that matter for return adjustment, and the exact math:**

| Event | Adjustment factor (applied to all pre-event prices, multiplicatively) | Notes |
|---|---|---|
| **Split** (old face value → new, e.g. ₹10→₹2) | `factor = new_face_value / old_face_value` — for a 1-old-share-becomes-5 split, `factor = 1/5 = 0.20` | Shares outstanding scale by the inverse; volumes scale up by the same ratio the price scales down |
| **Bonus** (ratio a:b, "a new shares per b held") | `factor = b / (a + b)` — 1:1 bonus → `factor = 1/2` | Same mechanism as a split, expressed as a distribution rather than a face-value change |
| **Rights** (ratio a:b at subscription price `P_s`, cum-rights close `P_c`) | Theoretical ex-rights price `TERP = (b·P_c + a·P_s) / (a+b)`; `factor = TERP / P_c` | Standard index-methodology construction (the same TERP logic NSE/BSE index providers use); shares outstanding scale by `(a+b)/b` |
| **Special/one-time large dividend** | `factor = (P_c − Div_special) / P_c`, applied as a discrete step exactly like a rights adjustment — ordinary dividends are **not** step-adjusted in a raw-price-continuity series (only reinvested inside TRI math) | The *materiality threshold* that makes a dividend "special" (vs. ordinary, no adjustment) is an index-provider convention, not a universal rule — **[VERIFY exact NSE Indices threshold**; pin down from the B8 methodology document rather than assuming a US-style convention transfers directly] |
| **Demerger/spinoff** | No closed-form factor. Requires the scheme-of-arrangement record-date allocation ratio (spinco shares per parent share) plus the spinco's first-traded price to establish a relative value split; the parent's continuing series is then adjusted by removing the spinco's imputed value share as of the record date | Confirmed the hardest event type in this catalog — matches the data catalog's own characterization of C4 as needing a dedicated, hand-built event registry, not a formula |
| **Delisting/liquidation** | Terminal — return series truncates at last-traded date; no adjustment factor, a **survivorship problem** (§C.3), not an adjustment problem | — |

**What cannot be recovered free.** Machine-readable corporate-action disclosure is patchy before
roughly 2000 (per the existing A-catalog C4 finding); for a name that delisted in the late-1990s
window, no clean free CA record may exist at all — reconstruction, if attempted, requires scanned
filings with no guarantee of completeness. **Honest error bound**: large, discrete adjustment
factors (splits, bonuses — typically simple fractions) produce an obvious multi-fold price
discontinuity in the raw series at the ex-date, and are cheaply caught by an automated outlier
scan (`|daily log return| ` far outside trailing vol, coincident with a filed ex-date). A missed
or mis-dated **rights** adjustment or **special dividend** (typically a 5–15% price effect, not a
multi-fold one) is the dangerous case: small enough to *not* trip an outlier flag, large enough to
bias a momentum rank that depends on cumulative return over exactly the window the miss falls in.
The honest bound on this construction is therefore: **splits/bonuses are self-auditing; rights/
special-dividend misses are silent** — the CA feed's own completeness (§C.8 step 4) matters far
more than any statistical patch for the second category. **[VERIFY: no primary base-rate figure
found this pass for how many CA events per listed name per year India's markets generate** —
treat as a data-phase-measurable quantity, not an assumed constant.]

**The standard test: reconstructed series vs NSE TRI.** NSE Total Return Index history (Nifty 50/
500/Total Market/Microcap 250 and the strategy indices) is free from `niftyindices.com/reports/
historical-data` and the documented (if unofficial) `Backpage.aspx/getTotalReturnIndexString`
endpoint (per data catalog B1–B4; exact internal index-name string required — spaced-uppercase for
broad-market indices, e.g. `"NIFTY 500"`, compact for strategy indices, e.g. `"NIFTY200 MOMENTUM
30"`). The test: for each rebalance date, reconstruct the constituent-weighted return from our own
adjusted-price + corporate-action database and compare against NSE's own published TRI return for
the identical window and weights. Near-zero (basis-point-level) tracking error validates the CA
feed; a **persistent** (not one-off) divergence, or a divergence dated to a specific ex-date,
flags a missed or mis-applied corporate action — this is the direct, mechanical validation gate
before any reconstructed series is trusted for momentum ranking.

---

## C.3 Survivorship — point-in-time universe, delisted names, the SME boundary

**Reconstructing point-in-time membership.** NSE Indices reconstitutes the whole broad-market
family (Nifty 50/100/200/500/Total Market/Microcap 250) **semi-annually, aligned**: review data
through end-January/end-July, replacements effective the **last trading day of March/September**,
with **four weeks' prior notice** via a dated press release (confirmed this pass; matches the
existing data catalog B1–B8/D3 finding). A forward-looking "Index Reconstitution Calendar" page
(`niftyindices.com/resources/index-rebalancing-schedule`) exists; the **backward** archive depth
of the press-release history itself (how many years of past reconstitution announcements are
still browsable, vs. requiring reconstruction from factsheet/news archives) was **not confirmed
this pass — [VERIFY]**. The B1–B4 caveat already on record bears directly on the aggressive
book's own stated universe and must not be re-litigated loosely here: **Nifty Total Market and
Microcap 250 history predating their actual launch (post-2023) is a back-computed construction,
not a point-in-time-published series** — any backtest using pre-launch history for either index
must be flagged non-PIT, exactly analogous to the fundamentals-restatement problem the whole
program is built to avoid on the price side.

**Delisted/suspended names.** NSE's compulsory-delisting public-notice page (`nseindia.com/
static/regulations/public-notice`) and delisting list (`.../static/list/list-of-companies-
proposed-to-be-delisted`) are **current/forward lists only** — the same limitation already
documented for ASM/GSM (A7/A8): no confirmed bulk historical file with entry/exit dates. NSE's own
delisting SOP document confirms the mechanics feeding this list: compulsory-delisting candidates
are drawn from securities **suspended for more than 6 months**, and a compulsorily-delisted name
is barred from relisting for **10 years**. A third-party-compiled historical ISIN status database
("India ISIN Database") was located on Zenodo — **Zenodo is confirmed blocked at this
environment's egress proxy** (re-confirmed this pass, consistent with `research/OPEN_QUESTIONS.md`
2026-09-01 note), so its build methodology and coverage could not be checked; treat as a
principal's-machine candidate fixture, to be authenticated against an independent primary source
before use (per the mirror-authorization decision's own rule), not adopted uncritically.

**The SME/mainboard boundary.** SME issuers trade on a fully separate NSE Emerge / BSE SME tier,
already excluded outright from this program's NIFTY 750 universe (`sleeves.yaml
tail_neglect_sleeve.filters`, `ladder.yaml excluded: sme_ipos`). Mechanically, the boundary is
drawn two ways that should agree: (a) bhavcopy `SERIES`/`SctySrs` carries a distinct code for
SME-platform trades, separate from mainboard `EQ`/`BE` **[VERIFY exact SME series code(s)]**; (b)
trusting Nifty Total Market/Microcap 250 membership (both mainboard-only universes by NSE Indices
methodology) as the universe definition already excludes SME names by construction, provided the
membership is applied point-in-time (§ above). **Migration eligibility** (the threshold at which
an SME name could ever *become* a mainboard candidate, per NSE Circular No. NSE/CML/67671, dated
2025-04-24, effective 2025-05-01): paid-up equity ≥₹10cr, average market cap ≥₹100cr, revenue from
operations >₹100cr in the latest FY, positive EBITDA in ≥2 of the last 3 FYs, ≥3 years listed on
the SME platform, promoters retaining ≥50% of their original SME-listing shareholding, no material
regulatory action in the preceding 3 years.

**Bias direction for momentum specifically — losers delist more.** This is a distinct channel
from generic survivorship bias, and it runs in a specific, nameable direction for this program's
**long-only** construction (per mandate — no standalone short momentum leg outside the tactical
short sleeve). If a backtest applies today's Nifty 500/750 membership retroactively, it silently
removes exactly the names that were live candidates at some historical formation date but later
failed (delisted, not merely dropped from the index on size) before the position could be exited
in the ordinary course. Two effects compound in the same direction: (i) the **universe itself**
looks survivor-only, so the long-only book never had the chance to be caught holding a name that
subsequently collapsed between rebalances — this inflates the reconstructed book's realized
return; (ii) the failure-prone names are disproportionately concentrated in the **small/microcap
tail** (ranks 500–750), i.e. exactly the aggressive book's own stated extra territory beyond
ranks 1–500. Net: **survivorship bias on an India long-only momentum backtest is upward, and
larger for the aggressive book than for the moderate/conservative books**, because a genuine
long-short construction would have partially offset this via its short leg capturing some of the
same failures (the short leg is absent here by design). **[VERIFY: no India-specific quantified
magnitude for this effect was found this pass** — the general finance-literature direction
(survivorship inflates backtested returns) is well established (e.g., the mutual-fund survivorship
literature), but a momentum-specific India magnitude is a data-phase-measurable quantity, not yet
in hand.]

---

## C.4 The WML construction spec for India

**Universe filters** (quantile-based, per contract §6 — no fixed magic-number thresholds):
- Base universe: NIFTY 750 (aggressive) or ranks 1–500 (moderate/conservative), per the mandate.
- Price floor: not a standalone rupee threshold — a byproduct of the liquidity floor below (a
  name too illiquid to trade meaningfully is also, mechanically, usually a low-price name in the
  Indian small-cap tail; a separate price rule would be redundant with, and less principled than,
  the ADV-percentile rule).
- Liquidity floor: trailing-6-month ADV (computed as `TtlTradgVol × ClsPric`, i.e. turnover value,
  from the normalized bhavcopy panel — §C.1), ranked as an **expanding/rolling percentile within
  the relevant universe** at each rebalance date — reuse `costs.yaml`'s own rank-bucket boundaries
  (`r1_50, r51_150, r151_300, r301_500, r501_750`) rather than inventing a second bucket
  convention for the same underlying quantity.
- Exclusions (already frozen in `sleeves.yaml momentum.liquidity_rules`): circuit-band-lock ≥20%
  of recent trading days; ASM/GSM stage ≥2; no new entries into a live index-reconstitution price
  pop (fades 10–60 days, India-specific). F&O ban-list membership does **not** exclude a name from
  the cash-only momentum sleeve (the ban blocks new derivative positions only). Active insolvency/
  NCLT proceedings are not currently in any ladder/sleeve filter and have no confirmed free bulk
  source in the data catalog — **flagged here as a genuine gap**, with IBBI's public case list as
  an unconfirmed free candidate **[VERIFY]**.

**12-1 / 6-1 formation, skip-month.** At rebalance date `t`: 12-1 momentum = cumulative adjusted
total return over `[t-12m, t-1m]`; 6-1 = the same over `[t-6m, t-1m]`. The skip-month is not
optional decoration — `ladder.yaml L1_reversal_1m` is explicitly Tier-C, zero-return-budget,
reduce-only; the skip-month is the mechanism that keeps L3's construction clean of L1's excluded
signal by construction, not a redundant precaution. **[VERIFY]** whether formation should use the
single-day `ClsPric` at `t` and `t-12m`/`t-6m` or an averaged formation price over a few days
around the boundary (the standard Jegadeesh-Titman convention reduces microstructure noise this
way; whether AJV/Raju's India constructions do the same was not confirmed this pass) — a genuine,
checkable convention choice, not a magnitude question.

**52-week-high variant**: `ClsPric_t / max(ClsPric over trailing 252 trading days)`, per George &
Hwang (2004) — rank-blended with the 12-1/6-1 composite (`sleeves.yaml momentum.construct`), never
combined as a raw ratio average.

**Rebalance cadence.** Monthly re-rank with a hysteresis no-trade band (aggressive book), per the
dossier's own proposal — now with a direct, previously-unfound confirming citation: **Rajan Raju,
"Timing the Tide: The Impact of Rebalancing Periods in Momentum Investing in Indian Equities"**
(SSRN 4687044, 2024) tests 1/2/3/6-month rebalancing across 200/500/750-stock universes at
15/30/50 holdings and finds **shorter rebalancing periods capture the academic momentum effect
more effectively** — i.e., monthly is not simply "more turnover for the same signal" but plausibly
captures *more* signal per unit of turnover than quarterly/semi-annual, which cuts directly
against a fixed-N semi-annual mechanic like NSE's own Nifty200 Momentum 30. Moderate book:
momentum computed monthly, acted on only as a tiebreaker inside the slower factor-book turn
(frozen, Known Prior #10 — unchanged by this data layer). Conservative: quarterly-or-slower
composite input only.

**Decile vs tercile at Indian breadth:**

| Universe | Breadth (N) | Decile (top ~10%) | Tercile (top ~33%) | NSE product analog |
|---|---|---|---|---|
| NIFTY 750 (aggressive) | ~750 | ~75 names | ~250 names | none — no NSE product spans this breadth |
| Ranks 1–500 (moderate/conservative) | ~500 | ~50 names | ~167 names | Nifty200 Momentum 30 draws from top-200 only, fixed N=30 (~15% of *its* universe — between a decile and a quintile, not a clean analog to either) |

**Rajan Raju, "An Examination of Number of Holdings and Universe Size in Momentum Strategies:
Evidence from India"** (SSRN 4453680, 2023) tested 6 universes (top-200/325/500/625/750,
mid-small-cap-400) × 16 holding counts (5–80 in steps of 5) — 96 portfolios/month — and found
concentrated portfolios carry **superior factor exposure but higher idiosyncratic risk**, and **on
a risk-adjusted basis, highly concentrated portfolios do not outperform**. This argues against a
tight decile (or NSE's own fixed-30) at this book's scale, and toward a wider selection — closer
to a tercile than a decile — for the aggressive book specifically, since idiosyncratic name-level
blowups inside a small concentrated momentum decile are exactly a source of unwanted drawdown
against the contract's binding drawdown constraint. **Recommendation**: decile as the initial
academic-comparability default (matches AJV's own construction for the §C.6 benchmark test), with
a pre-registered decile/tercile/fixed-N sweep in the data phase — never tuned post-hoc, per
contract §9.

**Equal vs cap weighting:**

| Scheme | Effect | Crowding/cost interaction |
|---|---|---|
| Equal-weight within decile (academic convention: Jegadeesh-Titman, AJV) | More exposure to smaller, less-liquid names inside the decile | Lower overlap with NSE's own product holdings (Nifty200 Momentum 30 is free-float-cap-weighted) → lower crowding correlation with the ~₹46,000cr India smart-beta pool |
| Free-float-cap-weighted (NSE product convention) | Concentrates in the largest-cap momentum names | Directly overlaps NSE's own product → higher crowding correlation, a weaker "why does this survive being known" argument at scale |
| **Liquidity-tilted equal-weight (recommended default)** | Equal-weight, but only across names already surviving the ADV-percentile floor above — i.e. equal-weighting the liquid subset | Matches Chui, Ranganathan, Rohit & Veeraraghavan (2023)'s finding that Indian momentum lives in the liquid tercile only; balances impact cost against crowding |

**Turnover and cost at the statutory table.** Frozen caps: aggressive ≤200%/yr one-way
(`sleeves.yaml momentum.book_roles.aggressive`); moderate ≤~40%/yr one-way (1/5 of the 200%
annual budget, Known Prior #10). Statutory-only illustration using `costs.yaml`'s cash-delivery
round-trip range (24–32bps, Tier B):

| Book | Turnover cap (one-way/yr) | Statutory-floor cost (turnover × round-trip bps) |
|---|---|---|
| Aggressive | 200% | ~48–64bps NAV/yr |
| Moderate | 40% | ~10–13bps NAV/yr |

This is a **floor**, not the full cost — impact cost (`I = Y·σ_daily·√(Q/ADV)`) adds materially
more in the aggressive book's ranks 500–750 (thinnest ADV bucket, `r501_750: ₹1–4cr`,
**PROVISIONAL** in `costs.yaml`, pending the live-ADV recomputation already scheduled at data-
catalog runsheet step 15). Two external data points bound this from outside: (i) Raju's
"Implementing a Systematic Long-only Momentum Strategy" (SSRN 3510433, 2020) finds a NIFTY100
top-decile, **monthly-rebalanced** portfolio realizing **~32.1%/month mean turnover** (≈385%/yr
annualized — far above either of our caps) yet still outperforming the NIFTY100 index by +10.70pp/
yr gross, and explicitly states the outperformance "survives real-world implementation" given
discount-broker costs — a data point that our much tighter caps leave real headroom, not proof our
own net-of-cost number will match; (ii) NSE's own Nifty200 Momentum 30 semi-annual mechanical
reconstitution generates an estimated 130–140%/yr turnover from reconstitution alone (dossier01
§2) — a caution against copying that fixed-N mechanic, not a benchmark to match.

---

## C.5 Index/TSMOM data (L4)

**Equity TRI.** Nifty 50/500 TRI — free via `niftyindices.com/reports/historical-data` and the
`Backpage.aspx/getTotalReturnIndexString` endpoint (per B1–B4); exact internal index-name string
required per pull (spaced-uppercase for broad-market, compact for strategy indices).

**Gold INR series — three candidate sources, one frozen primary.**

| Source | What it is | Free depth | Role here |
|---|---|---|---|
| FRED `GOLDPMGBD228NLBM` × RBI reference rate (G10) | USD LBMA PM fix (free back to 1968, republished by FRED) × USD/INR | Full depth, both legs | **Primary**, per the already-frozen `sleeves.yaml gold.series_hygiene` rule: "INR gold = USD gold + USDINR, decomposed always" |
| MCX gold futures | India's own gold futures, contract from MCX's 2003-11 inception | Historical-data pages confirmed reachable this pass (`mcxindia.com/market-data/historical-data`, `.../reports-on-historical-data`, year/month filter) | Cross-check only, and the natural futures-leg data for basis/roll cost modeling — **not** the primary spot series |
| IBJA (India Bullion and Jewellers Association) AM/PM rate | Domestic reference physical-gold rate | Live-rate portals (`ibjarates.com`, `ibja.co`) confirmed; **no confirmed bulk historical download found this pass** — **[VERIFY]** | Forward-collection only (start daily snapshots now); not a deep-history source unlike the other two |

**This is worth stating plainly, matching the credit-deep dossier's "do not reach for CMIE out of
habit" framing**: MCX and IBJA are the *obvious* India-specific gold sources, but the design's own
frozen convention already routes around both as primaries — do not rebuild the gold sleeve on MCX/
IBJA out of habit; they are cross-checks.

**The futures-roll data question.** Continuous-futures construction (roll-date rule + price-
adjustment method across the roll) has no universal standard and materially affects backtest
results depending on the choice — confirmed this pass as a genuinely open, non-trivial data-
engineering problem for both MCX gold and NSE index futures. **The simplification worth stating
explicitly**: TSMOM's own signal (trailing 1–12 month sign/return, L4) needs only a *continuous
spot/TRI series* — which already exists free with no roll problem — not a stitched continuous
futures series. A continuous-futures build is only strictly required for the **execution** leg
(basis, cost-of-carry, funding), where expiry-level (not continuous) bhavcopy rows suffice because
the position is rolled monthly by design already. This avoids a real construction project that
this signal does not actually need.

---

## C.6 Validation fixtures — the external benchmark

**The Agarwalla-Jacob-Varma / IIMA data library is downloadable free.** Location:
`faculty.iima.ac.in/iffm/Indian-Fama-French-Momentum/` (mirror `web.iima.ac.in/~iffm/Indian-Fama-
French-Momentum/`); maintained by Agarwalla, Jacob & Varma, sourced from CMIE Prowess DX. **Update
cadence: three releases per year** (March, September, December), per this pass's search finding.
The archive page (`.../archive.php`) lists dated release files (2021-03, 2021-09, 2022-03,
2022-09, 2022-12, 2023-03, 2023-12 confirmed this pass) — **[VERIFY] whether the 2024–2026
releases are current on the live site**: a companion methodology paper, **Rajan Raju, "September
2024 Update on the Data Library: Fama-French Factors, Momentum, and Low-Risk Factors for the
Indian Market"** (SSRN 5008269), confirms the library was still being actively revised (expanded
universe, updated size classification) as of Sept-2024, but whether the stated 3x/year cadence has
been kept through 2025–2026 is the first thing to confirm on the principal's machine, not an
assumption to carry forward. **Programmatic access candidate**: the `indiafactorlibrary` PyPI
package (Apache-2.0), a pandas-datareader-style wrapper exposing `.get_available_datasets()` and
keyed DataFrame access, described as an "Invespar Factor Library for Indian equities" — **[VERIFY]
whether this wraps the IIMA/AJV series specifically or a separate, similarly-constructed library**;
treat as an ingestion shortcut to confirm and cross-check, not as confirmed-identical to the
primary IIMA files, per the mirror-authorization decision's own authentication requirement.

**This is THE external benchmark for our constructed WML**, exactly as the task frames it — no
other free India momentum-factor series has this combination of academic provenance, published
magnitude (WML 21.9%/yr, 1994–2014, survivorship-corrected, liquidity-screened — already the base-
case anchor in `sleeves.yaml momentum.haircut`), and a maintained update cadence.

**Acceptable tracking error before ours is trusted.** No literature value exists for this specific
comparison — it is a construction-validation choice, proposed here, and flagged as such (not a
sourced fact): reconstruct our own long-short decile WML (§C.4's spec) over AJV's own sample
window and require (i) monthly-return correlation with AJV's published/archived series **≥0.85**
(perfect correlation is neither expected nor the bar — universe screen, rebalance timing, and
weighting scheme genuinely differ), and (ii) our reconstructed **raw** (pre-haircut) annualized
mean WML within roughly **65–100% of AJV's 21.9%/yr** — i.e., a raw reconstruction landing *below*
the already-haircut ~14–16%/yr planning number in `sleeves.yaml` would mean the haircut is double-
counting a construction gap, not measuring further genuine decay, and must be investigated before
being read as evidence for a deeper haircut. **[DESIGN CHOICE, not a literature-sourced
threshold — flagged explicitly as such.]** Given AJV's own currency is unconfirmed past 2023–2024,
use **Rajan Raju's independent, more recent papers** (`Shades of Momentum`, Dec-2008–Sept-2024
sample, SSRN 4977717; `Implementing a Systematic Long-only Momentum Strategy`, SSRN 3510433) as a
**second, modern-regime benchmark** — these cover exactly the post-2015 window dossier01 §3
already flagged as the critical decay-test period ("if the post-2015 India momentum premium has
fallen materially below the 1994–2014 average, raise the haircut toward 58%"), which AJV's own
public data may not yet reach.

---

## C.7 Vintage / point-in-time discipline

Two dates mandatory everywhere per `ingest/manifest.py`'s existing WORM rule (a hash-mismatch
under an existing manifest entry is a hard failure — refreshes land as new vintage-named files,
never an overwrite):

| Series | Revision-prone? | Two dates that must never be conflated | Store first-print or latest? |
|---|---|---|---|
| NSE/BSE bhavcopy (A1/A2/A4) | Not revision-prone once published, but **[VERIFY] whether NSE ever reissues a same-date file under an unchanged filename** — if so, `manifest.py`'s hash-hard-fail is exactly the designed safety net | `pull_date` vs the file's own trading-date stamp | Latest; the manifest catches silent reissues |
| Corporate actions (C4) | Not revision-prone, but **two-date by nature**: announcement date (board approval) vs. effective ex-/record-date | Never adjust prices as of the announcement date — only from the ex-date forward; the announcement-to-effective gap is itself a state variable (`special_situations`) | Latest, append-only event log |
| Index membership (B1–B4/D3) | Scheduled, not revision-prone | Announced (4-weeks-prior press release) vs. effective (last trading day March/Sept) | Apply new membership only from the effective date; the drift between the two dates is itself the `index_inclusion_exclusion` signal, not noise to be collapsed |
| Delisting/suspension | Event-based | Suspension date (>6m triggers compulsory-delisting candidacy) vs. delisting order date vs. **last-traded date** — three distinct dates | Truncate a name's tradeable-universe membership only at its actual last-traded date, never earlier or later |
| AJV/IIMA factor library (C.6) | **Methodology-revision-prone** (per the Sept-2024 "expanded universe and updated size classification" update) | Release-vintage (2021-03, 2021-09, …) vs. pull date | **Every release kept as its own vintage, never only-latest** — identical discipline to credit-deep's WEO/FSR rows, for the identical reason (a benchmark whose own methodology moved must be traceable to which vintage validated which build) |
| MCX gold, FRED gold/USDINR (C.5) | Prices not restated | T+0/T+1 | Latest — no PIT problem, matches credit-deep's own "market-price complements" row |

---

## C.8 Construction pipeline — ordered, script-followable

1. **Registry load.** Validate `config/ladder.yaml` and `config/sleeves.yaml` against `config/
   validator.py` (0 errors) before any pull.
2. **Pull raw bhavcopy.** NSE cash + F&O via the existing `ingest/pull_nse_bhavcopy.py`
   (URL-scheme-complete already); BSE cash bhavcopy into `data/raw/bse/` — **no existing ingest
   script; this is a gap this Part surfaces**. Manifest every file immediately
   (`python ingest/manifest.py data/`).
3. **Build the legacy↔UDiFF field crosswalk parser** (§C.1's table) so both eras normalize into
   one internal schema before any downstream step runs — **new code, not yet in `ingest/`**.
4. **Pull/scrape corporate actions** (NSE corporate-filings-actions + BSE corp-action pages) into
   `data/raw/{nse,bse}/corp_actions/` — **no existing ingest script; a second gap**. Build the
   derived adjustment-factor table (§C.2's formulas), keyed by ISIN + ex-date, append-only.
5. **Apply adjustment factors** to the normalized price series, producing an adjusted daily
   return panel per ISIN; **run the TRI cross-check** (§C.2) against B1–B4's TRI series before
   trusting the adjusted output for anything downstream.
6. **Build point-in-time universe membership** (§C.3): archive NSE Indices reconstitution press
   releases into a membership-as-of-date table for Nifty 500/Total Market/Microcap 250; cross-
   reference delisting/suspension lists to truncate names correctly; tag the pre-launch Total
   Market/Microcap segment as back-computed, not PIT.
7. **Apply universe filters** (§C.4): ADV-percentile liquidity floor (reusing `costs.yaml`'s
   rank-bucket convention), ASM/GSM/circuit/ban-list exclusions, SME-series exclusion.
8. **Compute the momentum composite**: 12-1 and 6-1 total return plus 52-week-high proximity on
   the adjusted series, rank-blended per `sleeves.yaml momentum.construct`, skip-month applied,
   monthly per the aggressive-book default.
9. **Form deciles/terciles per book**, liquidity-tilted equal-weight default, hysteresis no-trade
   band; compute realized one-way turnover and compare against the frozen caps (200%/40%/
   quarterly-composite for aggressive/moderate/conservative).
10. **Apply the crash guard** (Barroso-Santa-Clara inverse-vol scaling + Daniel-Moskowitz
    bear-state cut, already specified in `sleeves.yaml momentum.crash_guard`) using the momentum
    spread's own trailing realized vol.
11. **Validate against AJV/IIMA** (§C.6): reconstruct the long-short decile factor over AJV's own
    sample window; compute correlation and mean-divergence against the published/archived AJV
    series; cross-check against Raju's independent modern-regime papers; log any divergence —
    never silently adopt an external number in place of a divergence finding.
12. **Compute the TSMOM leg** (L4): 1–12 month trailing sign/return on Nifty TRI/spot (not a
    stitched futures series, §C.5) and on the FRED-USD-gold × RBI-USDINR constructed INR gold
    series (not MCX/IBJA primary); feed the regime matrix only, never the equity-cross-section
    optimizer (respects the mandate's Stage-3 boundary).
13. **Manifest every derived fixture** (adjustment-factor table, membership table, momentum
    composite panel) as its own versioned, checksummed artifact; corrections append a new vintage
    row, never overwrite.
14. **Recalibration triggers.** Re-run whenever: (a) a new AJV/IIMA release lands — compare, log
    divergence; (b) a semi-annual index-reconstitution effective date passes; (c) book AUM moves
    ±50% (re-check the ADV floor/capacity per `costs.yaml`'s own recalibration trigger); (d) the
    data-phase purged-CV decile/tercile/weighting sweep (§C.4) completes and locks a construction
    choice — never re-tuned informally afterward, per contract §9.

---
*End of Part C. Cross-references: `docs/masterplan/A-data-catalog.md` §2 blocks A/B/C4 (access
paths, priorities, fixture governance), `research/dossiers/01-momentum-reversal.md` (the theory/
evidence/decay this part builds data for), `config/ladder.yaml` L3/L4, `config/sleeves.yaml
momentum`, `config/costs.yaml` (statutory rates, ADV rank buckets), `ingest/README.md` +
`ingest/manifest.py` (the WORM/manifest rule), `ingest/pull_nse_bhavcopy.py` (existing, URL-scheme-
complete, schema-crosswalk-incomplete), `research/OPEN_QUESTIONS.md` (Q1 benchmark decision;
2026-09-01 mirror-authorization note), `research/CONTRACT.md` §3 (free-source mandate), §6 (no
magic numbers), §9 (estimation standards).*
