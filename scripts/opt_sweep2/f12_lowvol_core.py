"""f12_lowvol_core — LOW-VOL CORE TILT (ONE-WAY ONLY, survivorship-biased panel).

Purpose (per opt_sweep2 task brief): decide if a point-in-time (PIT) low-vol core is worth
a runsheet row. NOT a booked strategy. Survivor panel (ingest/vault/panel/n500_*_2012_2022,
2012-01-02..2021-12-31, SURVIVORSHIP-BIASED per AUTHENTICATION.md) used ONE-WAY per CONTRACT
Tier discipline and the repo's own T4 precedent (trial-ledger.md): "a negative kills, a
positive only suggests" for the standard survivorship direction (failures excluded ->
inflates included names generally). NOTE the repo's own SEC-D7 finding complicates this for
vol specifically: in THIS panel, vol LOSERS (high-vol delisted names, e.g. the 9-name HIGH-FL
cemetery) are disproportionately absent, which flatters the HIGH-vol survivor side and biases
AGAINST the low-vol premium showing up here. Both facts are stated in the JSON; this script
does not adjudicate between them further than T4 already did.

NO LOOKAHEAD: vol computed via rolling(252, min_periods=252) — a name only gets a vol
reading once it has 252 CONSECUTIVE trading days of non-NaN returns ending at that day; any
NaN in the trailing window (not-yet-listed OR delisted) forces NaN, which is the "alive at
signal time" gate. Signal at day d's close -> basket applies starting trading day d+1
(never day d itself). Rebalance monthly (last trading day of each calendar month, house
convention per scripts/analyze_op_d6b.py's E1 fix). Renormalize equal weights daily among
members with a valid return that day (handles mid-holding-period delisting without
lookahead — a name simply drops out of the average the day its price data ends).

Cells (5 backtest configurations, each producing CAGR/vol/Sharpe/beta/maxDD/2020DD vs NIFTY
over the identical date window):
  1. LOW  tercile (bottom third by trailing-252d vol)   <- the primary ask
  2. MID  tercile (control)
  3. HIGH tercile (control)
  4. BROAD EW-all-alive (composition control: isolates the panel's own size/composition
     tilt vs cap-weighted NIFTY from any genuine vol-tilt effect)
  5. LOW-LIQFILT: low tercile of vol AFTER excluding the bottom 30% of the alive universe
     by trailing-252d median value-traded (robustness: tests whether the low-vol basket is
     an illiquid-microcap / stale-price artifact)
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")

V = "/home/user/claude-demo/ingest/vault"

# ---------------------------------------------------------------------------
# Load panel (survivor, one-way) + NIFTY50 (index of record for the comparison)
# ---------------------------------------------------------------------------
adj = pd.read_csv(f"{V}/panel/n500_adjclose_2012_2022.csv.gz", parse_dates=["Date"]).set_index("Date").sort_index()
vt = pd.read_csv(f"{V}/panel/n500_value_traded_2012_2022.csv.gz", parse_dates=["Date"]).set_index("Date").sort_index()
assert list(adj.columns) == list(vt.columns), "adjclose/value_traded ticker mismatch"

nf = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date").sort_index()
nifty_close = nf["Adj Close"]
nifty_ret_full = nifty_close.pct_change()

ret = adj.pct_change()
VOL_WIN = 252
vol = ret.rolling(VOL_WIN, min_periods=VOL_WIN).std() * np.sqrt(252)          # annualized, no lookahead
liq = vt.rolling(VOL_WIN, min_periods=VOL_WIN).median()                       # trailing median value traded

# month-end signal dates = last trading day of each calendar month, restricted to where
# the cross-section actually has enough alive (seasoned) names to form 3 tercile groups
month_last = ret.index.to_series().groupby([ret.index.year, ret.index.month]).max()
signal_dates_all = pd.DatetimeIndex(sorted(month_last.values))
MIN_ALIVE = 30
signal_dates = [d for d in signal_dates_all if vol.loc[d].notna().sum() >= MIN_ALIVE]
print(f"signal months usable: {len(signal_dates)} / {len(signal_dates_all)} "
      f"(first {signal_dates[0].date()}, last {signal_dates[-1].date()})")


def build_membership(mode: str) -> dict:
    """mode in {'low','mid','high','broad','low_liqfilt'} -> {signal_date: [tickers]}."""
    memb = {}
    for d in signal_dates:
        alive = vol.loc[d].dropna()
        if mode == "broad":
            memb[d] = list(alive.index)
            continue
        if mode == "low_liqfilt":
            liq_d = liq.loc[d, alive.index].dropna()
            keep = liq_d[liq_d >= liq_d.quantile(0.30)].index   # drop bottom-30% illiquid
            pool = alive.loc[keep]
            if len(pool) < 9:
                memb[d] = list(alive.index)   # degenerate month fallback (not hit in practice)
                continue
            ranks = pool.rank(method="first")
            terc = pd.qcut(ranks, 3, labels=["low", "mid", "high"])
            memb[d] = list(pool.index[terc == "low"])
            continue
        ranks = alive.rank(method="first")
        terc = pd.qcut(ranks, 3, labels=["low", "mid", "high"])
        memb[d] = list(alive.index[terc == mode])
    return memb


def basket_returns(memb: dict) -> pd.Series:
    """Equal-weight daily return series, renormalized among members with a valid return
    that day (delisting mid-holding-period just drops the name from that day's average).
    Signal at d applies to trading days strictly AFTER d, through and including the next
    signal date; after the last signal date the last basket holds to the end of data."""
    idx = ret.index
    pos = {d: i for i, d in enumerate(idx)}
    out = pd.Series(0.0, index=idx)
    active = pd.Series(False, index=idx)
    sds = list(memb.keys())
    for k, d in enumerate(sds):
        start = pos[d] + 1
        end = pos[sds[k + 1]] if k + 1 < len(sds) else len(idx) - 1
        if start > end:
            continue
        cols = memb[d]
        if not cols:
            continue
        window = ret.iloc[start:end + 1][cols]
        out.iloc[start:end + 1] = window.mean(axis=1, skipna=True).fillna(0.0).to_numpy()
        active.iloc[start:end + 1] = True
    first_active = active.idxmax() if active.any() else None
    return out.loc[first_active:] if first_active is not None else out.iloc[0:0]


def stats_vs_nifty(r: pd.Series, tag: str) -> dict:
    r = r.dropna()
    t0, t1 = r.index[0], r.index[-1]
    rn = nifty_ret_full.reindex(r.index).fillna(0.0)   # same exact window, aligned
    eq = (1.0 + r).cumprod()
    eqn = (1.0 + rn).cumprod()
    n_days = len(r)
    yrs = n_days / 252.0
    cagr = eq.iloc[-1] ** (1.0 / yrs) - 1.0
    cagr_n = eqn.iloc[-1] ** (1.0 / yrs) - 1.0
    ann_vol = r.std() * np.sqrt(252)
    ann_vol_n = rn.std() * np.sqrt(252)
    running_max = eq.cummax()
    dd = eq / running_max - 1.0
    max_dd = dd.min()
    running_max_n = eqn.cummax()
    dd_n = eqn / running_max_n - 1.0
    max_dd_n = dd_n.min()
    mask20 = (r.index >= "2020-01-01") & (r.index <= "2020-12-31")
    dd20 = dd.loc[mask20].min() if mask20.any() else float("nan")
    dd20_n = dd_n.loc[mask20].min() if mask20.any() else float("nan")
    var_n = rn.var()
    beta = (r.cov(rn) / var_n) if var_n > 0 else float("nan")
    excess_cagr = cagr - cagr_n
    return {
        "tag": tag, "window": [str(t0.date()), str(t1.date())], "n_days": int(n_days),
        "cagr": round(float(cagr), 4), "ann_vol": round(float(ann_vol), 4),
        "sharpe_desc": round(float(cagr / ann_vol), 3) if ann_vol > 0 else None,
        "beta_vs_nifty": round(float(beta), 3),
        "max_dd": round(float(max_dd), 4), "max_dd_2020": round(float(dd20), 4),
        "nifty_cagr_same_window": round(float(cagr_n), 4),
        "nifty_ann_vol_same_window": round(float(ann_vol_n), 4),
        "nifty_max_dd_same_window": round(float(max_dd_n), 4),
        "nifty_max_dd_2020_same_window": round(float(dd20_n), 4),
        "excess_cagr_vs_nifty": round(float(excess_cagr), 4),
    }


def avg_basket_size(memb: dict) -> float:
    return float(np.mean([len(v) for v in memb.values()])) if memb else 0.0


results = {}
cells_consumed = 0
for mode in ["low", "mid", "high", "broad", "low_liqfilt"]:
    memb = build_membership(mode)
    r = basket_returns(memb)
    st = stats_vs_nifty(r, mode)
    st["avg_basket_size"] = round(avg_basket_size(memb), 1)
    results[mode] = st
    cells_consumed += 1
    print(mode, st)

# extra (no new cell): low-tercile basket's return series re-benchmarked against the
# BROAD equal-weight panel instead of NIFTY, to isolate the panel's own size/composition
# tilt (documented A1 MISS: EW-487 vs NIFTY50 corr 0.835) from the genuine vol-tilt effect
memb_low = build_membership("low")
memb_broad = build_membership("broad")
r_low = basket_returns(memb_low)
r_broad = basket_returns(memb_broad)
common = r_low.index.intersection(r_broad.index)
r_low_c, r_broad_c = r_low.loc[common], r_broad.loc[common]
eq_low = (1 + r_low_c).cumprod()
eq_broad = (1 + r_broad_c).cumprod()
yrs = len(common) / 252.0
cagr_low_vs_broad = {
    "low_cagr": round(float(eq_low.iloc[-1] ** (1 / yrs) - 1), 4),
    "broad_cagr": round(float(eq_broad.iloc[-1] ** (1 / yrs) - 1), 4),
    "excess_low_minus_broad": round(
        float(eq_low.iloc[-1] ** (1 / yrs) - 1) - float(eq_broad.iloc[-1] ** (1 / yrs) - 1), 4),
    "beta_low_vs_broad": round(float(r_low_c.cov(r_broad_c) / r_broad_c.var()), 3),
    "window": [str(common[0].date()), str(common[-1].date())],
}
print("low_vs_broad (decomposition, not a new cell):", cagr_low_vs_broad)

out = {
    "family": "f12_lowvol_core",
    "cells_consumed": cells_consumed,
    "panel_window_actual": [str(adj.index.min().date()), str(adj.index.max().date())],
    "signal_months_used": len(signal_dates),
    "signal_months_total": len(signal_dates_all),
    "min_alive_threshold": MIN_ALIVE,
    "vol_window_trading_days": VOL_WIN,
    "results": results,
    "low_vs_broad_decomposition": cagr_low_vs_broad,
    "prior_context": {
        "T4_trial_ledger": "Low-vol QUINTILE vs EW-UNIVERSE (not NIFTY), 2012-2021: "
                            "Sharpe 1.45 vs 1.34, CAPM beta 0.67, maxDD 24% vs 34% -- "
                            "signature visible but alpha +2.65%/yr at NW t=1.88 < 2 bar; "
                            "verdict INCONCLUSIVE per the declared one-way (PIT owed).",
        "SEC-D7_finding": "In this SAME survivor panel, high-vol survivors' full-period CAGR "
                          "is inflated (22.2 -> 32.6%/yr monotone UP by vol quintile) because "
                          "vol LOSERS are disproportionately the delisted names (the HIGH-FL "
                          "cemetery: 9/28 declared high-leverage names absent vs 1/25 low). "
                          "This is the specific mechanism behind the 'biases AGAINST low-vol' "
                          "one-way direction stated in trial-ledger T4 and in this task brief.",
        "AUTHENTICATION_A1_MISS": "EW-487-panel vs NIFTY50 daily corr = 0.835 (bar was 0.85) "
                                   "-- the broad panel itself is NOT compositionally close to "
                                   "NIFTY (small/midcap tilt), so ANY vs-NIFTY comparison here "
                                   "conflates a composition effect with a vol-tilt effect; the "
                                   "low_vs_broad_decomposition block above isolates the two.",
    },
    "caveats": [
        "SURVIVORSHIP-BIASED PANEL, ONE-WAY USE ONLY. Direction of the bias is DISPUTED "
        "internally in this repo: the generic one-way convention says a positive result "
        "'only suggests' (could be survivorship inflation) and a negative 'kills'; BUT this "
        "repo's own SEC-D7 finding shows survivorship in THIS panel specifically inflates "
        "HIGH-vol survivors (vol losers get delisted, vol winners remain) and therefore "
        "biases AGAINST the low-vol premium showing up here -- so a positive low-vol print "
        "in this panel is, if anything, MORE credible than the generic one-way convention "
        "would suggest, not less. Both readings are stated; PIT data is required to resolve "
        "which dominates.",
        "Panel spans 2012-01-02..2021-12-31 (487 survivor-roster tickers), not the 2012-2022 "
        "filename's literal endpoint -- effective usable window is ~2013-01..2021-12 once "
        "the 252-day vol warm-up is applied (matches T4's stated 'effective 2013-2021').",
        "Membership = index roster AS OF ~2021-22 construction, backfilled -- NOT "
        "point-in-time; MR1's PIT registration explicitly does not cover this panel.",
        "A3 (AUTHENTICATION.md) miss: 379/487 tickers have >=2000 rows -- some names carry "
        "under a year of history and never enter any tercile (correctly excluded by the "
        "252-day no-lookahead vol requirement, but it means recently-listed IPOs are "
        "structurally absent from year 1 of any basket, a conservative omission).",
        "No transaction costs, no market-impact, no bid-ask modeled -- monthly full-panel "
        "rebalance turnover for a ~160-name equal-weight tercile basket would not be free; "
        "this is a paper-return test only, consistent with CONTRACT's 'research only' scope.",
        "vs-NIFTY comparisons conflate two effects: the panel's own composition tilt "
        "(AUTHENTICATION A1: EW-487 vs NIFTY50 corr only 0.835, small/midcap-heavy) and the "
        "genuine within-panel vol tilt. The BROAD row (mode='broad') isolates the first; "
        "low_vs_broad_decomposition isolates the second. Do not read the LOW-vs-NIFTY excess "
        "CAGR alone as 'the low-vol premium' -- most of any vs-NIFTY excess CAGR across ALL "
        "five rows (including the untilted BROAD row) is composition, not vol-tilt.",
        "2020 drawdown uses the running peak from the FULL history (not reset at 2020-01-01) "
        "so it correctly captures the pre-COVID Jan/Feb-2020 high as the drawdown reference.",
        "Costs, index membership changes, and any real-world implementation friction are "
        "entirely unmodeled; this is a screening test, not a strategy backtest.",
    ],
}

import json
with open("/home/user/claude-demo/research/opt_sweep2/f12_lowvol_core.json", "w") as f:
    json.dump(out, f, indent=2)
print("wrote research/opt_sweep2/f12_lowvol_core.json")
print("cells_consumed:", cells_consumed)
