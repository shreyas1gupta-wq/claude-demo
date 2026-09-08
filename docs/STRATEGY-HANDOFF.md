# The Cycle Program — Strategy Handoff Brief

**Date:** 2026-09-08 · **Principal:** gaurav@ionic.in · **Repo:** `claude-demo`, branch `claude/funny-faraday-r3v4aj`
**Purpose:** a self-contained brief of the FINAL STANDING STRATEGY — its composition, code
logic, the data and statistical conventions behind every number, everything we tested and
rejected (with mechanisms), and how to hand this program to another Claude session or
another quant without losing the discipline that makes the numbers trustworthy.

> **If you are a new Claude session:** read this file, then `CLAUDE.md` (session onboarding)
> and `research/CONTRACT.md` (the binding rules) BEFORE computing anything. The single most
> important rule: **pre-register bars/priors in `research/register/trial-ledger.md` before
> any number is computed; bars never move after a print; every computed cell enters
> `research/register/trial-count.md`** (running total at handoff: **1,013**).

---

## 1. The final strategy — the standing book (baseline SW2-A1, adopted 2026-09-08)

Three capital sleeves plus three option overlays plus two accounting legs. Everything below
is **rationale-frozen** — no parameter was fitted to the full sample, and the two
optimization attempts that tried (OP-D3b grid, OP-D7 grid) were both rejected by their own
pre-registered out-of-sample validation.

### 1.1 Capital sleeves (weights fixed 65 / 20 / 15)

| Sleeve | Weight | Rule (all signals lagged ≥1 day/month) |
|---|---|---|
| **Vol-managed NIFTY core** | 65% | Exposure = min(15% ÷ EWMA(λ=.94) realized vol, **1.5x cap**); halved when India-VIX expanding-percentile ≥ 0.90. Financing charged at 6%/yr on exposure above 1.0x; idle cash below 1.0x credited at 4%/yr (both R/252 day-count). |
| **Dual-momentum switcher** | 20% | Monthly: hold NIFTY or gold-in-INR, whichever has the higher trailing 12m return at the PRIOR month-end. Marks at the last trading day of each month, flat intra-month. |
| **Factor sleeve** | 15% | Vol-managed 50/50 WML+HML (IIMA monthly factors), 15% vol target on EWMA(.94) monthly vol, leverage cap 2x, one-month signal lag. Paper LONG-SHORT — academic gross returns; a standing 25–35% haircut applies to any forward claim. |

### 1.2 Option overlays (all Black-Scholes flat-sigma at India VIX, r = 6%, zero costs — paper)

| Overlay | Rule |
|---|---|
| **Permanent put ladder** | Buy 91-day 5%-OTM puts on the core's levered notional; roll when ≤30 days remain. Costs ~1.6%/yr net of roll recovery; paid +4.3pp in 2020. This is the structural tail hedge — reactive vol rules lag crash onsets by 72–74 vol points (booked), so the hedge must always be on. |
| **Covered calls** | When VIX-pct ≥ 0.60: sell 1-month calls at strike S×(1+σ√T) on 50% of core notional. Earns ~+1.05%/yr — **the calls finance the puts** (net structure cost ~0.3–0.5%/yr for ~6pp less drawdown). |
| **Condor sleeve** | Monthly symmetric iron condor, short ±1.0σ / long ±2.5σ wings (σ from VIX), entry only when VIX-pct ≥ 0.60, sizing f = min(0.15×s_t, 10% of book)/max-loss, delta-roll at \|Δ\|≥0.30 max 3, stand-down at pct ≥ 0.90 (re-arm below 0.60), day-stop −2.22% of book, Union-Budget window excluded. |

**Margin model (principal's, frozen):** hedged structures 2.5% of notional; unhedged 10%;
long options = premium; pledge haircut 10%. Peak utilization 22.2% of book ex-factor;
23.7–28.2% including the factor sleeve's gross (bounds pending an SLB-margin convention).

### 1.3 Measured results (2011-07-01 … 2023-03-31, paper)

| Measure | Value |
|---|---|
| CAGR (price-only core) | **+11.46%/yr** (≈ **+12.76% with the +1.3pp TR adjustment**) |
| Max drawdown | **−11.36%** |
| Worst full year | **+0.4% (2013)** — no negative full year; 2023 is a Q1 stub at −2.3% |
| Worst month | −6.26% (Sep-2018); months positive 64%; monthly Sharpe ≈ 1.12 (paper, rf=0) |
| Era halves | +7.9%/yr (2011-16) · +14.7%/yr (2017-23) |
| At the −30% factor haircut | ~+10.3 (TR ~+11.6) / −11.9 — the conservative read |
| Yearly | 2012 +14.7 · 2013 +0.4 · 2014 +22.7 · 2015 +1.2 · 2016 +3.8 · 2017 +33.1 · 2018 +4.3 · 2019 +7.5 · 2020 **+22.3** · 2021 +27.7 · 2022 +3.4 |

**vs the principal's 15/15 target:** maxDD ≤ 15% is **beaten with ~3.6pp of room**
(even at the factor haircut). CAGR ≥ 15% TR **misses by ~2pp** — and five independent
attacks (two 15+-agent sweeps, an optimization grid, an MR battery, a leverage test)
established that this gap is **not closable from inside the current data**. See §5.

2020 is the design's signature: the put ladder flipped the COVID year from what would have
been a deep loss into **+22.3%** — structure, not timing.

---

## 2. Code logic — where everything lives and how it composes

```
scripts/analyze_op_d3.py    THE CONDOR STATE MACHINE: bs() pricing, make_legs/price_legs,
                            run(entry, wing, roll, d0, d1) -> equity curve. Other scripts
                            reuse it via: exec(src.split("BASE = ")[0], ns); ns["run"](...)
scripts/analyze_op_d6b.py   THE BOOK ENGINE (canonical): all data loading, core_stream(),
                            month_stream() (E1-fixed month marks), run_book(...), stats_of().
                            Designs exec the part before "# === MAIN ===" and compose.
scripts/analyze_sw2_a1.py   The adopted baseline print (idle-cash credit @4%) — run this
                            to reproduce the headline numbers bit-for-bit.
scripts/analyze_op_d7.py    The rejected optimization grid (kept as the honest record).
scripts/opt_sweep2/*.py     15 sweep-2 research scripts (+ research/opt_sweep2/*.json).
quant/                      Stage-1 machinery (regime assembler, walk-forward, stats, DSR).
config/ + config/validator.py  Registries; the validator gates every commit.
```

`run_book(core_w, sw_w, fac_w, cap, financing, overlays, fac_monthly, syn_margin,
extra_ret, extra_margin, fac_margin_rate)` is one daily loop: sleeve returns compound the
book; puts/calls are priced and marked daily in book units; margin is tracked against the
principal's model. New ideas plug in as **book-relative daily return streams** via
`extra_ret`/`extra_margin` — never re-implement the loop (process note #6).

**House statistical conventions (every booked number uses these):**
- Percentile ranks: `expanding_percentile(x, min_obs=252)` — never full-sample ranks.
- Vol: EWMA λ=0.94 = `ret.pow(2).ewm(alpha=0.06).mean().pow(0.5) × √252` (√12 monthly).
- All signals lag one bar (day/month). Monthly sleeves mark at the **last trading day**.
- Options: BS flat-sigma at India VIX, r=0.06, last-Thursday expiry, zero costs (declared).
- Sharpe-like claims must call `quant.stats.dsr.deflated_sharpe_ratio` with
  `n_trials ≥ census_n()` (mechanically parsed from trial-count.md).
- Train/test where used: train 2011-07..2016-12, test 2017-02..2023-03, **21-trading-day
  purge**, selection objective and acceptance rule frozen at registration.

---

## 3. Data used (the vault) — all free, sha256-manifested, two-pass authenticated

| Series | Span | Load-bearing caveat |
|---|---|---|
| NIFTY 50 daily OHLC | 2007–2026 | **Price-only** — +1.3pp/yr TR adjustment reported, never silently added |
| India VIX daily | 2010-07–**2023-04** | **No 2008 in sample; tail ends before the 2024-election/SEBI-curbs era** — every option number inherits this boundary |
| IIMA monthly factors (SMB/HML/WML/MF/RF) | 1993–2025 | Academic gross long-short construction → standing 25–35% haircut |
| Gold monthly × INR/USD monthly | 1833– / 1973– | Monthly resolution only |
| S&P futures daily / DJIA daily / Shiller monthly / CBOE VIX | 1982– / 1980–2012 / 1871– / 1990– | US legs; Shiller real columns valid only to 2023-09 |
| NIFTY500 survivor panel | 2012–2021 | **SURVIVORSHIP-BIASED — one-way uses only** (a negative kills, a positive only suggests); it has already produced one refuted claim |

What the vault does **not** contain (and therefore what no number here reflects): real
option chains/IV surfaces, point-in-time index membership, daily INR/USD, post-2023 India
VIX, funding-rate term structure. These are the Priority-1 principal-machine pulls.

---

## 4. The doctrine we USE (validated facts the design is built on)

1. **VRP is a state, not a constant:** mean +3.0 vol pts, 82% positive, monotone by VIX
   quintile (+1.9 → +5.9). Seller breach-edge exists **only post-spike** (top-quintile 21d
   breach 17% vs calm 32% ≈ Gaussian-neutral). Hence: sell only at VIX-pct ≥ 0.60.
2. **One event ≈ 21 months of premium** (Mar-2020 −64.5 on naive selling): tail safety must
   be **structural** (bought wings + permanent ladder), never reactive — EWMA/GARCH lag
   crash onsets by 72–74 vol points.
3. **Post-spike is a buyer's market at 6–12m horizons** (+18.2%/+32.4% fwd after VIX
   top-decile) — and seller/buyer proxies are +0.41 correlated (same state), so the
   stand-down and the fwd-return trade are one regime rule, not two systems.
4. **Vol-managed momentum works** (M5: WML Sharpe 0.77→1.29, maxDD 83→29%) and value hedges
   it (corr −0.37) — the factor sleeve is the 50/50 combination, vol-managed.
5. **Collar economics:** the covered calls pay for the put ladder almost exactly; ~6pp of
   drawdown was bought at near-zero net return cost. Risk is cheap; return is not.
6. **India monthly returns CONTINUE, they don't revert** (after a ≤−5% month: next month
   −0.24% vs +0.97% unconditional; −2.86% when VIX high). The only monthly bet in the book
   is momentum.
7. **Financed leverage at Indian rates doesn't pay:** the incremental calm-period equity
   premium over 6% funding is ≈ 0 (negative in all 12 tested pairs). DD headroom cannot be
   spent on levered beta unless the true funding rate is well below 6%.
8. **Cash accounting is symmetric:** charge financing above 1x AND credit idle cash below
   1x (44% of days; 47% of book idle in COVID). Worth +0.33pp at a conservative 4%.

---

## 5. The graveyard — what we tested and REJECTED (read before proposing "new" ideas)

Every entry is booked in `research/register/trial-ledger.md` with the mechanism named.
The census cost of learning all this honestly: **1,013 cells**.

| Rejected idea | Why it died |
|---|---|
| **Overnight-only core** (gross +26.3%/−5.5%!) | Cost mirage: breakeven one-way cost only 2–4bp; also loses 4.3× more on zero-warning shocks (2016 demonetization) |
| **Weekly option selling, always-on** | In-sample ruin at full margin |
| **Weekly condor, post-spike only** | Won on train (+2.3pp), FLAT on test — era-concentrated; rejected by the frozen purged validation |
| **Synthetic-futures leverage (cap 1.5→2.0x)** | Negative in all 12 train pairs at 6% financing (doctrine #7) |
| **Mean reversion — daily/weekly/monthly** | Dead at every frequency; after 3 down days next-day is −2.3bp vs +4.5 unconditional |
| **IV−RV condor gate** (tried TWICE) | 1st: lookahead leak (grouped stats). 2nd (clean, lagged): a trade-more-often frequency confound — loses to frequency-matched VIX-pct controls |
| **VRP-quintile condor sizing** | Vacuous: reduces to a naive cap raise breaching the 10%-DD invariant; Q5 fires 3/33 times |
| **Condor parameter grid** (entry/wing/roll) | Train winner failed test validation — baseline stands |
| **Weight re-optimization** (6-point simplex × 2 × 2) | Train winner (50/25/25+weekly) lost on test by 0.2pp — baseline stands |
| **Put-ladder re-tuning** (tenor/strike/roll frontier) | REFUTED: the "protection" axis silently measured Feb-2016, not 2020 — the frontier ranking was invalid; current cell frozen pending real chains |
| **Covered-call grid** | REFUTED: its OOS bar was computationally vacuous (a stats-slicing bug); true test edge +0.55pp with flat-worse DD, likely eaten by 2.5× more writing costs |
| **Drawdown governor on the book** | Trades 1.5–5pp of scarce CAGR for DD headroom the book doesn't need |
| **Gold sleeve upgrades** (vol-managed/trend-gated/60-40) | All flat-to-negative vs the binary switcher at book level |
| **Factor sleeve extensions** (add SMB / risk-parity / other targets) | SMB ~doubles maxDD (2018 smallcap unwind); nothing beat 50/50 at its bars |
| **Factor rotation timing** (WML↔HML switching) | Destroys the −0.37 diversification benefit; ~doubles maxDD |
| **Faster VIX stand-downs** (ΔVIX, MA-ratio, 2-day spike) | Rarer AND worse DD than pct ≥ 0.90; the one attractive cell reverses across eras |
| **Turn-of-month overlay** | Era fingerprint flips sign under a small window shift; principal's no-trade cap on the TOM prints stands |
| **Low-vol core** (+9.8pp excess!) | REFUTED twice: survivorship panel positive-claim + undisclosed 2013-16 era concentration |
| **September effect, Dr. Copper, daily-skew trades, Kondratieff, earnings-revision, hegemonic-cycle timing…** | Atlas/battery graveyards — see the ledger and `docs/cycles/38-atlas-close.md` |

**Parked (verified clean, awaiting a principal decision):**
- **10% SPX-in-INR carve** (f13): +1.07pp CAGR/+1.55pp DD in-sample, honest ~+0.3pp net of
  feeder TER and the secular-USD-window haircut. Blocked on CONTRACT S1 scope
  (foreign equity) — OPEN_QUESTIONS **B4-4**. Mutually exclusive with:
- **Tri-asset 12-1 switcher** (f04): adds NO CAGR (−0.12pp) but +1.8pp DD headroom —
  stored DD budget, same USD/INR bet as f13.

---

## 6. Errors found and corrected (a checklist for the next Claude)

These were REAL bugs found by directed audit — each is exactly the class of error to check
for in any new script:

1. **E1 month-drop:** monthly sleeves marked at *calendar* month-ends → 31% of months
   silently zeroed when month-end wasn't a trading day. Fix: mark at last trading day.
2. **E2 free leverage:** core ran >1x on 57% of days with no financing charged.
3. **stats_of slicing trap:** its d0/d1 args set the year-count but didn't slice the
   equity curve — one sweep agent's "out-of-sample" bar was thereby vacuous. Fixed; a
   shared sliced-stats helper is owed to `quant/stats/`.
4. **Missing factor margin line** in the engine's peak-margin (long-short gross carried
   zero margin). Now a declared bounds read (23.7–28.2%).
5. **F13 lookahead** (grouped IV−HV stats) and **winsorization lookahead / missing purge /
   benchmark mislabel** (the 2026-09-05 audit, process note #8) — the reasons every OOS
   claim now must state its purge rule, information set, windows, and benchmark.

Corrections are booked as dated entries (ER-D4b protocol); superseded numbers stay visible;
**bars are never retro-fitted to pass.**

---

## 7. Where the remaining return must come from (the honest frontier)

The DD side of 15/15 is done. The ~2pp CAGR gap is **data- and decision-gated**, not
engineering-gated. In priority order:

1. **Real NSE option chains / IV surfaces** — the ladder, calls, and condor are all priced
   at flat sigma; real skew changes their economics in both directions. (Priority-1 pull.)
2. **Point-in-time bhavcopy / index membership** — cross-sectional stock selection is the
   return system the program's priors always pointed to; the low-vol engine (alive-gate,
   tercile machinery) is built and waiting in `scripts/opt_sweep2/f12_lowvol_core.py`.
3. **funding_rate config** (validator warns on every run) — if the desk's true rate is
   materially below 6%, both the leverage verdict and the cash credit rescale linearly.
4. **Post-2023-04 India VIX + daily INR** — break the sample boundary every option number
   leans on.
5. **Decisions:** OPEN_QUESTIONS batches 3+4 and **B4-4** (foreign-equity scope → unlocks
   the verified +0.3pp USD sleeve).

---

## 8. Caveats that must travel with every headline number

Paper backtest; zero transaction costs; BS flat-sigma options (no skew, no spreads); NIFTY
price-only core (+1.3pp TR adjustment stated, not compounded in); factor sleeve is academic
gross long-short (25–35% haircut standing); no 2008 in the VIX sample and no post-2023-04
VIX; funding at a declared 6% pending the real rate; single-country, single-regime-era
sample (2011–2023). The program treats these as **bounds to be tightened by named data
pulls**, not as footnotes to be dropped.

## 9. Handing this to another Claude — the working rules

1. Read `research/CONTRACT.md` from disk first. It outranks everything including this file.
2. **Pre-register before running** (ledger entry with bars, priors, cell count) — then
   compute — then hand-write the interpretation. Never the other order.
3. Bars never move. Misses are recorded, not fixed. Optimization needs the frozen purged
   train/test protocol and an acceptance rule written BEFORE the grid runs.
4. Update the census (`trial-count.md`) with every consumed cell; it's parsed mechanically.
5. Gated commits: pytest + `config/validator.py` must pass (enforced by `.githooks/
   pre-commit` — install via `git config core.hooksPath .githooks`). Commit and push
   everything to the designated branch.
6. New sleeves plug into `run_book` via `extra_ret`/`extra_margin`; never fork the loop.
7. Sweep findings are exploratory until adversarially verified (refute-by-default) and
   re-registered as one-shots — three of five "promising" sweep-2 findings died in audit.
8. Reproduce before extending: `PYTHONPATH=<repo> python3 scripts/analyze_sw2_a1.py` must
   print CAGR +11.456 / maxDD −11.364 before you trust your environment.
