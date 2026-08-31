# FROZEN CONTRACT — Multi-Horizon "Cycle Stack" Portfolio Model (India)

Version 0.1 · 2026-08-31 · Owner: principal + Claude · Status: BINDING for the research phase.
Every research dossier, parameter proposal, and design decision must comply with this document.
Where a dossier wants to depart from it, the departure must be stated explicitly with the argument.

---

## 1. Mandate

Proprietary capital. Indian markets. Universe: NIFTY 750 equities (≈ Nifty Total Market index:
Nifty 500 + Nifty Microcap 250), gold, and a debt sleeve. Leverage and options permitted.
Three books — **different products, not one product dialled down**:

| Book | Capital (₹ cr) | Turnover cap (one-way/yr) | Equity universe |
|---|---|---|---|
| Aggressive | 100–250 | 600% | Full NIFTY 750 incl. mid/small tail (ranks 500–750) |
| Moderate | 1,000–2,500 | 200% | Roughly ranks 1–500 |
| Conservative | 10,000–25,000 | 100% | Roughly ranks 1–500 |

The model reads many cycles at once — multi-century currency/debt arc, 15–20y liquidity /
real-estate cycle, 7–11y credit cycle, business/monetary/flow cycles, down to 1-month reversal —
and turns that reading into (a) a target basket metric for alpha and (b) a regime matrix for risk.
Long cycles carry ±20% timing uncertainty (news/events can delay, accelerate, or compress them);
shorter lookbacks (12m/6m/3m momentum) have monthly-to-quarterly predictability with higher
confidence; fundamental/value signals have 3–5y realization horizons. Top-down and bottom-up.
Forward-looking judgement that cannot be backtested is in scope — but only inside Stage 2.

## 2. Architecture (FIXED)

- **Stage 1 — Cycles + Quant.** Must emit a COMPLETE portfolio on its own. Self-sufficiency is
  load-bearing: quant-only vs quant-plus-overlay is the only honest measure of Stage 2's value.
- **Stage 2 — AI + human forward views and checks.** SWITCHABLE OFF at any time.
- **Stage 3 — Optimizer.** Final construction. Optimizes ONLY the equity cross-section; the
  asset mix comes from a policy portfolio set by construction (see Known Priors #5).

## 3. Frozen constraints

- Returns measured **net of costs, pre-tax**.
- **Drawdown is binding**: max drawdown below the Nifty 50's over the same window, measured on
  episodes where the index itself fell >20%, with flash-crash-and-immediate-reversal episodes
  excluded — the exclusion must be defined testably, not by judgement. Absolute ceiling 30–35%.
- Debt ≤70% · gold ≤50% · gross leverage ≤1.5x.
- Name entry 5–6% · drift cap 10% · in-progress (staged-entry) positions ≤20% aggregate.
- Options notional ≤50% directional, ≤75% tail. Hedge ratio is a swept config parameter
  (0/25/50/75/100/125/150%) **jointly** with the regime that selects it — never independently.
- Sector exposure: fully active (no sector neutrality requirement).
- Debt sleeve: flat 10% return assumption — no credit model, no duration overlay.
- Gold via ETF and futures only.
- Rebalance weekly permitted; bi-weekly to monthly preferred (cadence may differ per sleeve).
- Special situations in scope, including recently listed IPOs.
- Data (when the data phase begins): free sources only — NSE/BSE bhavcopy, RBI DBIE, MOSPI,
  CCIL, BIS, IMF, FRED, World Bank, AMFI, NSDL, World Gold Council, exchange filings,
  Kaggle/HuggingFace; scraping allowed; no paid feeds.
- Team: principal + Claude. Timeline: 3–6 months.

## 4. Evidence tiers and cycle authority

- Cycles have **persistence, not periodicity**. Anything without ≥4 observed complete periods
  (clock test) is a **state variable**, not a cycle. Order the ladder by `tau_half` — the
  autocorrelation half-life in months, estimable from overlapping windows with zero complete cycles.
- Tier **A**: ≥30 independent observations of the effect; may be fitted with purged CV.
- Tier **B**: 4–30 observations, or n<4 with ≥10 cross-country analogues; parameters FROZEN at inception.
- Tier **C**: <4 observations; narrative. **Tier-C signals may only REDUCE risk** — never add.
- Consequence already accepted: a 200-year debt cycle moves the book by ~1.5pp; the long-wave
  view lives in a structural gold floor and tail hedges, not in cycle influence.

## 5. Governing principle: assume your alpha decays

- McLean & Pontiff (2016): published anomalies decay ~26% out-of-sample, ~58% post-publication.
- Chordia, Subrahmanyam & Tong: attenuation as arbitrage capital arrives.
- Arnott et al.: much of reported factor return was valuation (multiple) expansion, not premium.
- For every signal, answer IN WRITING: *why does this survive being known?* Acceptable answers:
  (i) structural/behavioural mechanism persistent under crowding, (ii) capacity limit that keeps
  large capital out, (iii) genuine risk premium someone must be paid to bear, (iv) institutional
  constraint. Unacceptable: "it backtests well."
- Signals with no survival argument get a **stated numeric decay haircut** before sizing.
- The strategy must still work after every edge is haircut by its historical decay rate.
- We are not slaves to the literature: we may reject published results with argument, and build
  forward-looking constructs for 2026–2036 (and beyond) — but every rejection and every new
  construct carries its own written argument and provenance.

## 6. No magic numbers

No fixed thresholds of the "20%, 10%, 200-DMA" variety presented as truth. Broad, sensitivity-
robust rules are acceptable ("3-month return > 0 → equity else cash" is the flavor: sign tests,
quantile ranks, long-anchor scalings). Every constant in the final design must trace to a source:
a paper, a cross-country panel, documented practitioner experience, or an explicit economic
argument — recorded in the research register with confidence and decay assumption.

## 7. Known priors from the prior design pass

Items marked (data-derived) were computed on Indian data and are **provisional priors to be
re-argued from literature in this phase** — not settled facts.

1. Of 32 cycle candidates, five survived the clock test (three calendar-anchored). Everything
   else is a state variable ordered by `tau_half`.
2. Authority tracks evidence (the tier system above).
3. The cycle stack is the RISK system; name selection is the RETURN system. Cycle-driven
   allocation contributes only ~100–300bps/yr; cycles buy permission to run concentrated and
   levered without breaching the drawdown ceiling. (data-derived)
4. Standing 1.25x leverage is incompatible with the 30–35% ceiling (2008 at 1.25x ≈ −58%;
   Mar-2020 ≈ −36%). Leverage must be state-contingent permission; compatible averages
   ~1.10–1.15x aggressive, ~1.05x moderate. (data-derived)
5. A flat 10% debt return breaks every optimizer (MVO corners 70% debt; risk parity 67%).
   Therefore: asset mix from a policy portfolio set by construction; optimize only the equity
   cross-section; state the implied override explicitly (~400bps/yr markdown to debt).
6. Turnover costs ~3.9% of NAV/yr at 500% one-way (~0.6% at 100%), so the high-churn book's
   incremental hurdle is ~3.3pp/yr of extra gross alpha. (data-derived — re-derive the cost
   stack from first principles and check it)
7. Free Indian fundamentals are restated with no knowledge date → backtests biased upward
   150–450bps/yr, plus survivorship. Against a 3.3pp hurdle that is decisive: a price-only,
   genuinely point-in-time factor book is the only instrument that can answer the central
   question. Design it now; build it first. (data-derived)
8. Fast crashes cannot be met by cycles. Slow bears yes; a five-week 38% fall with no prior
   signal, no. Fast vol/funding triggers plus options cut Mar-2020 to ≈ −20% portfolio, with
   8–12% irreducible. Do not claim otherwise.
9. Honest targets: ~22–28% CAGR / 25–30% maxDD (aggressive); 15–19% / 20–25% (moderate).
   Higher is a stretch case (high nominal growth + wide value spread + early credit cycle),
   not a design target.
10. The moderate book's engine is the FACTOR book, not momentum — value/quality run ~5×
    momentum's half-life, so cost ~1/5 the turnover per unit of authority.
11. This remote environment has no market-data network access (NSE, RBI, FRED, Kaggle 403 at
    the proxy; web search works). Data phase: ingestion on principal's machine; every indicator
    resolves against a committed fixture; every module testable with zero live data.

## 8. Traps (forbidden moves)

- Do NOT optimize the asset mix.
- Do NOT tune thresholds against backtest Sharpe.
- Do NOT use neural nets for return prediction on ~25 years of lag-approximated data.
- Do NOT include Elliott Wave, Gann, or fixed-period calendar cycles.
- Do NOT treat 500–600% turnover as a target; it is a ceiling to be earned.
- Do NOT admit a signal with no free data source or no decay-survival argument.
- Do NOT report a fundamental backtest without its price-only counterpart.
- Do NOT use the HP filter anywhere (endpoint revisions); use Hamilton's (2018) regression filter.
- Do NOT fit regime-switching models without ≥10 observed transitions.

## 9. Estimation standards (for the data phase; the design must be written to them)

- Pool on the Jordà–Schularick–Taylor panel where India alone offers <2 cycles.
- Correct Stambaugh bias on persistent predictors.
- Out-of-sample R² judged against the historical-mean benchmark, never in-sample.
- Purged and embargoed cross-validation; embargo scaled to signal half-life.
- Pre-register every hypothesis before running it; never re-test a rejected idea with tweaked
  parameters.
- Deflated Sharpe with the TRUE trial count (all sweeps counted, including the 7-point hedge
  sweep × regime grid).

## 10. Working conventions (updated with principal's decisions, 2026-08-31)

- **Turnover** = one-way: min(buys, sells) / average NAV per year.
- **Options in leverage accounting**: delta-adjusted exposure counts toward the 1.5x gross cap;
  the notional caps (≤50% directional / ≤75% tail) are separate hard caps.
- **Drawdown** measured on daily NAV, close-to-close.
- **Benchmark**: Nifty 500 TRI for alpha/signal research (all books); Nifty 50 TRI only for the
  frozen drawdown constraint.
- **Drawdown violation (testable form)**: the relative constraint applies only when portfolio
  MDD > 20%; violation = portfolio drawdown exceeds Nifty 50 drawdown by more than a margin ε
  for more than K consecutive trading days (K ≈ 10–20; ε, K derived with sensitivity analysis).
  Absolute ceiling 30–35% unchanged. This replaces episode exclusion: flash crashes produce
  only transient excursions and are handled automatically.
- **Leverage instrument**: margin funding on cash names. `funding_rate` is a first-class config
  parameter; the leverage-state function must clear expected-return > funding-rate; margin-call
  dynamics in stress must be modeled (leverage permission tightens earlier than a futures
  overlay would require).
- **Hedging**: de-grossing first (cut stocks/margin); option BUYING is rare, budgeted, and
  rule-triggered for tail regimes only. The fast-crash floor must be re-derived under this.
- **Short side**: base hedge-only via index derivatives, plus a tactical single-name short
  sleeve (Nifty 100 names only; single-stock futures, put spreads, defined-risk combos)
  capped at ~25% of the total short-side sleeve.
- **Stage 2**: advisory-only (shadow book + scored ledger) until a pre-registered paired test
  passes at a high bar. LLM channels: structured scorer, red team, tactical thesis/buy calls —
  all human-vetoed, logged, Brier-scored.
- **Re-entry rules**: per-sleeve (calendar / hysteresis / vol-target families), derived in
  research with equal precision to exits. Rebalance cadence is also per-sleeve.
- **Special situations**: capped Tier-B satellite sleeve, aggressive book only, rules frozen
  at inception.
- Books are evaluated net of costs, pre-tax; cost model must be stated per book.
- All parameters land in a versioned `config/` registry with provenance (`research/register/`),
  validated in CI: evidence-tier caps, tier-C reduce-only, per-bucket budget containment,
  3σ aggregation inside mandate caps, turnover caps, DAG acyclicity. A registry violating its
  own budget must fail to load.

## 11. Design decisions record

See `research/OPEN_QUESTIONS.md` — batch 1 (ten questions) was answered by the principal on
2026-08-31; that file is the decision record and lists the new research questions each
decision opened.

## 12. Rules for research agents (this phase)

- RESEARCH ONLY: no data acquisition, no ingestion code, no backtests, no model code.
- Read this file and `research/OPEN_QUESTIONS.md` from disk before starting. Do not guess.
- Use web search heavily. NEVER fabricate a citation: verify author/title/venue/year by search;
  if unverifiable, keep the finding and tag it `[VERIFY: <best description of source>]`.
- Prefer Indian evidence; where only US/global evidence exists, say so and mark it a
  cross-country prior (Tier B at best).
- Every proposed indicator must name its free data source or be flagged unavailable.
- Do not spawn subagents (a maximum of three agents run concurrently across the whole program).
- Dossiers go to `research/dossiers/`; dense prose, no filler, provenance tables included.
