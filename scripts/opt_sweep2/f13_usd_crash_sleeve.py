"""f13_usd_crash_sleeve — Strategy Sweep 2, agent f13.

PERMANENT USD-ASSET CRASH SLEEVE. CU-D7 booked: India coupling -0.69/-0.79 (weak-INR
years, local equities fine in INR while USD investors are crushed; the mirror direction —
USD assets in INR terms rally when INR crashes — is what this sleeve tries to harvest as a
diversifier). Carve a permanent 10% SPX-in-INR sleeve out of the STANDING BOOK core
(0.65/0.20/0.15 -> 0.55/0.20/0.15 + 0.10 USD), unhedged, no signal, no timing — a pure
structural allocation, so HARD RULE #1 (no lookahead) is satisfied trivially: there is no
predictive signal in this design at all, only a static weight.

Data: sp500_fut_adjusted_daily.csv (back-adjusted SPX futures, hourly-stamped) +
sp500_fut_multiple_daily.csv (unadjusted current-contract PRICE, for the diff/lag(unadj)
return convention declared in ingest/vault/us_index/AUTHENTICATION.md) x
fx/inr_usd_monthly_1973_2026.csv (INR_per_USD, MONTHLY — there is no daily FX series in
the vault, so this sleeve is necessarily built at MONTHLY frequency: SPX-in-INR monthly
return = (1+r_usd_monthly)*(1+r_fx_monthly)-1, placed on the LAST TRADING DAY of the month
via the book engine's own month_stream() (the E1 fix pattern already used for the
switcher/factor sleeves) so there is no double-counted or dropped month.

Reuses: scripts/analyze_op_d6b.py (book engine: run_book, stats_of, dates, D0, D1,
month_stream, n_me, S_) exec'd verbatim before its MAIN block, per house convention
(process note #6 — no inline re-implementation of the book engine).
"""
import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"

# ---- pull in the book engine (house pattern, see analyze_op_d7.py) ----
_src = open("/home/user/claude-demo/scripts/analyze_op_d6b.py").read()
_g = {}
exec(_src.split("# === MAIN ===")[0], _g)
run_book, stats_of, month_stream = _g["run_book"], _g["stats_of"], _g["month_stream"]
dates, D0, D1 = _g["dates"], _g["D0"], _g["D1"]
n_me, S_, r_, pct_s = _g["n_me"], _g["S_"], _g["r_"], _g["pct_s"]

CELLS = []  # (name, description) — every computed conditional mean/backtest config


def cell(name):
    CELLS.append(name)


# =====================================================================================
# 1) Build the SPX-in-INR monthly return series (no lookahead: static structural sleeve)
# =====================================================================================

def daily_price_series(path, col):
    """Vault convention (us_index/AUTHENTICATION.md): daily price = the 20:00 row when
    present for that calendar date, else the last (max-hour) row of that date.
    Weekend-stamped rows are dropped first: the Sunday-evening GLOBEX reopen (~22:00 UTC)
    lands on a Sunday calendar date under simple normalize() and would otherwise be
    mistaken for a distinct 'trading day' between Friday's close and Monday's — verified
    directly against 2020-03-13->03-16 (a spurious '2020-03-15' row breaks the lag-1
    return and corrupts the B5 sanity check below if left in)."""
    df = pd.read_csv(path, parse_dates=["DATETIME"])
    df = df[df["DATETIME"].dt.dayofweek < 5]  # Mon-Fri only
    df["date"] = df["DATETIME"].dt.normalize()
    df["hour"] = df["DATETIME"].dt.hour
    has20 = df[df["hour"] == 20].drop_duplicates("date", keep="last").set_index("date")[col]
    lastrow = df.sort_values("DATETIME").drop_duplicates("date", keep="last").set_index("date")[col]
    out = has20.reindex(lastrow.index)
    out = out.fillna(lastrow)
    return out.sort_index()


adj = daily_price_series(f"{V}/us_index/sp500_fut_adjusted_daily.csv", "price")
unadj = daily_price_series(f"{V}/us_index/sp500_fut_multiple_daily.csv", "PRICE")

# sanity check vs the AUTHENTICATION B5 anchor before using this construction for anything
_r2020 = (adj.loc["2020-03-16"] - adj.shift(1).loc["2020-03-16"]) / unadj.shift(1).loc["2020-03-16"]
assert _r2020 <= -0.07, f"SPX daily-price construction failed the B5 sanity check: {_r2020:.4f}"

# monthly (last trading day of month), house diff(adjusted)/lag(unadjusted) convention
adj_me = adj.resample("ME").last()
unadj_me = unadj.resample("ME").last()
r_spx_usd_m = (adj_me.diff() / unadj_me.shift(1)).dropna()

fx = pd.read_csv(f"{V}/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"]).set_index("Date")["INR_per_USD"]
fx_me = fx.resample("ME").last().reindex(r_spx_usd_m.index, method="nearest")
r_fx_m = fx_me.pct_change()  # INR_per_USD rising = INR depreciating = USD asset gains in INR terms

r_spx_inr_m = ((1 + r_spx_usd_m) * (1 + r_fx_m) - 1).dropna()
r_spx_inr_m = r_spx_inr_m.loc[(r_spx_inr_m.index >= D0) & (r_spx_inr_m.index <= D1)]

# place on last trading day of each NIFTY month (book engine's own E1-fix placement)
usd_stream_full = month_stream(r_spx_inr_m, fix=True)  # book-relative daily stream, weight 1.0
cell("build SPX-in-INR monthly series + placement")

nifty_m = n_me.pct_change().reindex(r_spx_inr_m.index)

# =====================================================================================
# 2) Standalone diagnostics: what IS this sleeve, on its own
# =====================================================================================
eq_usd_alone = (1 + r_spx_inr_m).cumprod()
yrs = (eq_usd_alone.index[-1] - eq_usd_alone.index[0]).days / 365.25
cagr_usd = 100 * (eq_usd_alone.iloc[-1] ** (1 / yrs) - 1)
dd_usd = 100 * (eq_usd_alone / eq_usd_alone.cummax() - 1).min()
vol_usd = 100 * r_spx_inr_m.std() * np.sqrt(12)
cell("standalone SPX-in-INR CAGR/DD/vol")

corr_full = r_spx_inr_m.corr(nifty_m)
cell("full-sample monthly correlation vs NIFTY")

vixpct_m = pct_s.reindex(nifty_m.index, method="ffill")
hi = vixpct_m >= 0.90
lo = vixpct_m < 0.60
corr_hi = r_spx_inr_m[hi].corr(nifty_m[hi]) if hi.sum() >= 5 else np.nan
corr_lo = r_spx_inr_m[lo].corr(nifty_m[lo]) if lo.sum() >= 5 else np.nan
cell("correlation conditioned on VIX-pct>=0.90 (stress)")
cell("correlation conditioned on VIX-pct<0.60 (calm)")

crash_m = nifty_m <= -0.05
n_crash = int(crash_m.sum())
mean_usd_in_crash = r_spx_inr_m[crash_m].mean() if n_crash else np.nan
mean_usd_in_calm = r_spx_inr_m[~crash_m].mean()
cell("mean USD-sleeve return in NIFTY crash months (<=-5%) vs other months")

stress_months = list(nifty_m.index[hi])
worst5 = nifty_m.sort_values().head(5)
worst5_usd = r_spx_inr_m.reindex(worst5.index)
cell("worst-5 NIFTY months + USD-sleeve return in each (named-event check)")

# redundancy check vs the existing 20% NIFTY-vs-gold-INR switcher sleeve (both are
# INR-depreciation-linked overlays; do they double up on the same currency exposure?)
g_ret_m = _g["g_ret_m"]
corr_gold_usd = r_spx_inr_m.corr(g_ret_m.reindex(r_spx_inr_m.index))
cell("redundancy check: correlation vs gold-in-INR monthly returns")

# named era windows (descriptive, small-n — reported as such)
ERAS = {
    "2013 taper (May-Sep 2013)": ("2013-05-01", "2013-09-30"),
    "2018 INR/EM stress (Apr-Oct 2018)": ("2018-04-01", "2018-10-31"),
    "2020 COVID (Feb-Apr 2020)": ("2020-02-01", "2020-04-30"),
    "2022 Fed-hike/INR (Jan-Oct 2022)": ("2022-01-01", "2022-10-31"),
}
era_rows = {}
for label, (a, b) in ERAS.items():
    u = r_spx_inr_m.loc[a:b]
    n = nifty_m.loc[a:b]
    era_rows[label] = dict(
        n_months=int(len(u)),
        usd_cum=100 * ((1 + u).prod() - 1),
        nifty_cum=100 * ((1 + n.reindex(u.index).fillna(0)).prod() - 1),
    )
    cell(f"era window: {label}")

# =====================================================================================
# 3) Book-level test: baseline OP-D6b a5 (0.65/0.20/0.15) vs carved book (+10% USD)
# =====================================================================================
BASE_W = (0.65, 0.20, 0.15)
eq_base, pm_base = run_book(*BASE_W, cap=1.5, financing=True, syn_margin=True)
c_base, d_base, y_base = stats_of(eq_base)
cell("baseline book OP-D6b a5 (0.65/0.20/0.15)")


def carved_book(usd_w, core_w=None):
    cw = core_w if core_w is not None else BASE_W[0] - usd_w
    eq, pm = run_book(cw, BASE_W[1], BASE_W[2], cap=1.5, financing=True, syn_margin=True,
                       extra_ret=usd_w * usd_stream_full, extra_margin=None)
    return eq, pm


eq10, pm10 = carved_book(0.10)
c10, d10, y10 = stats_of(eq10)
cell("carved book 0.55/0.20/0.15 + 0.10 USD (PRIMARY design)")

# sensitivity: 5% and 15% carve sizes (same 0.65 core budget re-split)
eq05, pm05 = carved_book(0.05)
c05, d05, y05 = stats_of(eq05)
cell("carved book sensitivity: 0.05 USD carve")

eq15, pm15 = carved_book(0.15)
c15, d15, y15 = stats_of(eq15)
cell("carved book sensitivity: 0.15 USD carve")

# worst-year deltas
wy_base, wy10 = y_base.min(), y10.min()

print("=" * 90)
print("f13_usd_crash_sleeve — PERMANENT SPX-in-INR DIVERSIFIER SLEEVE")
print("=" * 90)
print(f"\n[data] SPX-in-INR monthly series: {r_spx_inr_m.index[0].date()} .. "
      f"{r_spx_inr_m.index[-1].date()}, n={len(r_spx_inr_m)} months (book window "
      f"{D0.date()}..{D1.date()}, India VIX ends 2023-04)")
print(f"[sanity] 2020-03-16 SPX futures daily return under declared convention: "
      f"{100*_r2020:.2f}% (AUTHENTICATION B5 bar: <=-7%, matches -8.8% anchor)")

print(f"\n--- Standalone sleeve (100% notional, unhedged, monthly) ---")
print(f"  CAGR {cagr_usd:+.2f}%/yr | maxDD {dd_usd:.2f}% | ann.vol {vol_usd:.2f}%")
print(f"  full-sample monthly corr vs NIFTY: {corr_full:+.3f}")
print(f"  corr | VIX-pct>=0.90 (stress, n={int(hi.sum())}): {corr_hi:+.3f}  "
      f"| VIX-pct<0.60 (calm, n={int(lo.sum())}): {corr_lo:+.3f}")
print(f"  mean monthly return | NIFTY crash months (<=-5%, n={n_crash}): "
      f"{100*mean_usd_in_crash:+.2f}%  | other months: {100*mean_usd_in_calm:+.2f}%")
print(f"  correlation vs gold-in-INR monthly returns (redundancy check vs the 20% "
      f"switcher sleeve): {corr_gold_usd:+.3f}")
print(f"  stress months (VIX-pct>=0.90, n={len(stress_months)}): "
      f"{[d.strftime('%Y-%m') for d in stress_months]}")
print(f"\n  worst 5 NIFTY months vs USD-sleeve return that same month:")
for d in worst5.index:
    print(f"    {d.strftime('%Y-%m')}: NIFTY {100*worst5[d]:+.2f}%  USD-sleeve "
          f"{100*worst5_usd[d]:+.2f}%" if not pd.isna(worst5_usd[d]) else
          f"    {d.strftime('%Y-%m')}: NIFTY {100*worst5[d]:+.2f}%  USD-sleeve n/a")

print(f"\n--- Era behavior (cumulative return over window, descriptive n small) ---")
for label, d in era_rows.items():
    print(f"  {label} (n={d['n_months']}mo): USD sleeve {d['usd_cum']:+.2f}% | "
          f"NIFTY {d['nifty_cum']:+.2f}%")

print(f"\n--- Book-level: baseline vs carved (full window {D0.date()}..{D1.date()}) ---")
print(f"  BASELINE  0.65/0.20/0.15         : CAGR {c_base:+.2f}%  maxDD {d_base:.2f}%  "
      f"worst-yr {100*wy_base:+.1f}%  peak-margin {100*pm_base:.1f}%")
print(f"  CARVED    0.55/0.20/0.15+10%USD  : CAGR {c10:+.2f}%  maxDD {d10:.2f}%  "
      f"worst-yr {100*y10.min():+.1f}%  peak-margin {100*pm10:.1f}%")
print(f"  DELTA                            : dCAGR {c10-c_base:+.2f}pp  dDD {d10-d_base:+.2f}pp "
      f" dWorstYr {100*(y10.min()-wy_base):+.1f}pp")
print(f"  sensitivity 5%  USD carve        : CAGR {c05:+.2f}%  maxDD {d05:.2f}%  "
      f"worst-yr {100*y05.min():+.1f}%")
print(f"  sensitivity 15% USD carve        : CAGR {c15:+.2f}%  maxDD {d15:.2f}%  "
      f"worst-yr {100*y15.min():+.1f}%")

print(f"\n--- Yearly, baseline vs carved (10%) ---")
yb = {d.year: f"{100*x:+.1f}" for d, x in y_base.items()}
yc = {d.year: f"{100*x:+.1f}" for d, x in y10.items()}
for yr in sorted(set(yb) | set(yc)):
    print(f"  {yr}: base {yb.get(yr,'  n/a')}%  carved {yc.get(yr,'  n/a')}%")

print(f"\nCELLS CONSUMED: {len(CELLS)}")
for i, c in enumerate(CELLS, 1):
    print(f"  {i}. {c}")

# =====================================================================================
# 4) Findings JSON
# =====================================================================================
import json  # noqa: E402

out = {
    "family": "f13_usd_crash_sleeve",
    "date": "2026-09-08",
    "data_span_used": f"{r_spx_inr_m.index[0].date()}..{r_spx_inr_m.index[-1].date()} "
                       f"({len(r_spx_inr_m)} months); book window {D0.date()}..{D1.date()}",
    "cells_consumed": len(CELLS),
    "cell_list": CELLS,
    "sanity_check_2020_03_16_return_pct": round(100 * float(_r2020), 2),
    "standalone_sleeve": {
        "cagr_pct": round(float(cagr_usd), 2),
        "maxdd_pct": round(float(dd_usd), 2),
        "ann_vol_pct": round(float(vol_usd), 2),
        "corr_vs_nifty_full": round(float(corr_full), 3),
        "corr_vs_nifty_stress_vixpct_ge_090": None if pd.isna(corr_hi) else round(float(corr_hi), 3),
        "corr_vs_nifty_calm_vixpct_lt_060": None if pd.isna(corr_lo) else round(float(corr_lo), 3),
        "n_months_stress": int(hi.sum()),
        "n_months_calm": int(lo.sum()),
        "mean_ret_nifty_crash_months_pct": None if n_crash == 0 else round(100 * float(mean_usd_in_crash), 2),
        "n_nifty_crash_months": n_crash,
        "mean_ret_other_months_pct": round(100 * float(mean_usd_in_calm), 2),
        "corr_vs_gold_in_inr_monthly": round(float(corr_gold_usd), 3),
        "stress_months_list": [d.strftime("%Y-%m") for d in stress_months],
        "worst5_nifty_months": {
            d.strftime("%Y-%m"): {"nifty_pct": round(100 * float(worst5[d]), 2),
                                   "usd_sleeve_pct": None if pd.isna(worst5_usd[d]) else round(100 * float(worst5_usd[d]), 2)}
            for d in worst5.index
        },
    },
    "era_behavior": {
        label: {"n_months": d["n_months"], "usd_sleeve_cum_pct": round(float(d["usd_cum"]), 2),
                "nifty_cum_pct": round(float(d["nifty_cum"]), 2)}
        for label, d in era_rows.items()
    },
    "book_level": {
        "baseline_0.65_0.20_0.15": {
            "cagr_pct": round(float(c_base), 2), "maxdd_pct": round(float(d_base), 2),
            "worst_year_pct": round(100 * float(wy_base), 2), "peak_margin_pct": round(100 * float(pm_base), 2),
        },
        "carved_0.55_0.20_0.15_plus_0.10_usd": {
            "cagr_pct": round(float(c10), 2), "maxdd_pct": round(float(d10), 2),
            "worst_year_pct": round(100 * float(y10.min()), 2), "peak_margin_pct": round(100 * float(pm10), 2),
        },
        "delta": {
            "d_cagr_pp": round(float(c10 - c_base), 2),
            "d_maxdd_pp": round(float(d10 - d_base), 2),
            "d_worst_year_pp": round(100 * float(y10.min() - wy_base), 2),
        },
        "sensitivity_0.05_usd": {"cagr_pct": round(float(c05), 2), "maxdd_pct": round(float(d05), 2),
                                  "worst_year_pct": round(100 * float(y05.min()), 2)},
        "sensitivity_0.15_usd": {"cagr_pct": round(float(c15), 2), "maxdd_pct": round(float(d15), 2),
                                  "worst_year_pct": round(100 * float(y15.min()), 2)},
    },
    "yearly_baseline_pct": {str(d.year): round(100 * float(x), 2) for d, x in y_base.items()},
    "yearly_carved10_pct": {str(d.year): round(100 * float(x), 2) for d, x in y10.items()},
}

out["verdict"] = "PROMISING BUT NOT A CLEAN HEDGE — genuine diversifier, unreliable crash-hedge"
out["why"] = (
    "Real diversification exists (calm-regime corr +0.27, zero redundancy with the "
    "existing gold-INR switcher at +0.02, and in the worst 5 NIFTY months of the sample "
    "the sleeve NEVER compounded the loss — twice it was outright positive, 2011-11 and "
    "2016-02). But the mechanism is NOT a clean India-crisis hedge: conditioned on "
    "VIX-pct>=0.90 the correlation to NIFTY FLIPS to +0.82 (positive, n=9, 4 of 9 months "
    "one COVID episode) and the 2022 Fed-hiking window is a direct counterexample "
    "(USD sleeve -11.47% while NIFTY was flat/positive) — the sleeve tracks GLOBAL SPX "
    "risk more than India-specific stress, so it helps in India-idiosyncratic/EM-taper "
    "events (2013 taper: +24.1% vs NIFTY -3.3%, the cleanest confirmation of the CU-D7 "
    "mirror) and can hurt in globally-driven-but-India-resilient regimes (2022). The "
    "book-level in-sample dominance (CAGR +1.07pp AND maxDD +1.55pp AND worst-year "
    "+1.14pp, all simultaneously better) should NOT be read at face value: the "
    "standalone sleeve's +17.07%/yr CAGR is a secular USD-strength/SPX-bull-market "
    "artifact of this exact 2011-2023 window (INR depreciated ~45->82, a rare-magnitude "
    "multi-decade dollar cycle) and is very unlikely to repeat at that rate; the CAGR "
    "improvement should be haircut hard, the DD/worst-year improvement less so (it rests "
    "on genuine cross-asset decorrelation, not on the trend). SCOPE GATE: CONTRACT S1's "
    "asset universe is 'NIFTY 750 equities, gold, and a debt sleeve' — foreign (USD) "
    "equity exposure is not currently an authorized asset class; this design cannot be "
    "promoted without an explicit principal decision widening the mandate (OPEN_QUESTIONS "
    "candidate), independent of its statistical merit."
)
out["caveats"] = [
    "Era concentration: the whole 2011-2023 sample is one secular USD-strength / INR-"
    "depreciation cycle (INR ~44->82/USD) plus a historic US equity bull market; the "
    "standalone sleeve's +17.07%/yr CAGR is an upper bound unlikely to persist, and the "
    "book-level CAGR delta (+1.07pp) is suspect for the same reason.",
    "Stress correlation small-n: the VIX-pct>=0.90 bucket has only 9 months, 4 of which "
    "are one contiguous COVID episode (2020-03..06) — the +0.82 stress correlation is a "
    "COVID-dominated point estimate, not a robust regime statistic (same 'effective n' "
    "problem flagged for F20 in OP-D2).",
    "2022 is a clean counterexample to the hedge thesis: Fed-hiking global stress hurt "
    "the USD sleeve (-11.47%) while NIFTY itself was resilient (+3.79%) — the mechanism "
    "is regime-dependent (helps in India-specific/EM-taper stress, can hurt in global-"
    "equity-bear-but-India-resilient stress).",
    "FX data is MONTHLY ONLY in the vault (fx/inr_usd_monthly_1973_2026.csv) — there is "
    "no daily INR/USD series, so this entire analysis is monthly-resolution; it cannot "
    "speak to intraday/multi-day crash dynamics the way the option sleeves in OP-D2 can, "
    "and the monthly SPX return is built from the vault's declared "
    "diff(adjusted)/lag(unadjusted) futures convention, not a total-return SPX index (no "
    "dividends) — a small, structural understatement of true SPX total return.",
    "India VIX sample ends 2023-04 (same constraint as the rest of the book); the 743-day "
    "post-2023-04 tail (2024 election spike, SEBI derivatives curbs) is untested here, "
    "consistent with OP-D2's C12 caveats.",
    "CONTRACT SCOPE GATE (not a data or statistics caveat): CONTRACT.md S1's asset "
    "universe is NIFTY 750 + gold + debt; foreign equity is not currently authorized. "
    "This is a principal decision (OPEN_QUESTIONS candidate), not something this sweep "
    "can freeze on its own authority.",
    "No implementation costs modeled: real access to SPX exposure from an Indian PMS "
    "book (LRS-routed funds, GIFT City structures, or INR-denominated US-index feeder "
    "funds) carries FX-conversion spread, a materially higher TER (~1%/yr for feeder "
    "funds vs <0.1% domestic index) than assumed here (zero), and periodic SEBI/AMFI "
    "industry-wide caps on fresh overseas-fund subscriptions have intermittently frozen "
    "new inflows to US-linked funds (a 2022 precedent) — an access-continuity risk for a "
    "'permanent' always-on sleeve that this backtest does not price in. [UNVERIFIED for "
    "this book's actual execution vehicle — flagged, not backtested.]",
    "No redundancy with the existing 20% NIFTY-vs-gold-INR switcher (corr +0.02) — this "
    "is a genuinely distinct exposure, not double-counted currency risk.",
]
out["proposed_design"] = {
    "rule": "Carve 10pp from the core vol-managed sleeve (0.65->0.55) into a permanent, "
            "unhedged, unlevered allocation to SPX exposure marked in INR (S&P 500 "
            "futures-equivalent return x INR/USD), rebalanced monthly at each sleeve's "
            "existing month-end mark; no timing signal, no FX hedge, no leverage — a "
            "structural reallocation of existing capital, not incremental gross.",
    "frozen_params": "usd_w=0.10 (carved 1:1 from core_w: 0.65->0.55); sw_w=0.20 and "
                     "fac_w=0.15 unchanged; monthly cadence (house convention, and the "
                     "only cadence the vault's FX data supports); FX unhedged by "
                     "construction (hedging it would remove the exact mechanism being "
                     "tested); size fixed at 10% per this family's brief, not tuned "
                     "against backtest Sharpe — 5%/15% sensitivity checks show smooth, "
                     "monotonic CAGR/DD response rather than a fitted interior optimum.",
    "expected_cagr_add_pp": 0.3,
    "expected_dd_impact_pp": 1.0,
    "confidence": "low-medium: DD/worst-year direction is grounded in a real, low, "
                  "sometimes-negative calm-regime correlation and zero redundancy with "
                  "the existing gold sleeve, so directionally credible; the measured "
                  "CAGR add is a secular-trend artifact and heavily haircut here; the "
                  "stress-regime correlation is small-n and the 2022 window is a live "
                  "counterexample, so 'crash hedge' framing should not be oversold — call "
                  "it a diversifier with a scope gate (CONTRACT S1 does not currently "
                  "authorize foreign equity) still open.",
}
with open("/home/user/claude-demo/research/opt_sweep2/f13_usd_crash_sleeve.json", "w") as f:
    json.dump(out, f, indent=2)
print("\nwrote research/opt_sweep2/f13_usd_crash_sleeve.json")
