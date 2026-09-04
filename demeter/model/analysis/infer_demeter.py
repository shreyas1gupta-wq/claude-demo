#!/usr/bin/env python3
"""Infer what Demeter's daily dual-engine signal must have been doing, using ONLY the published monthly
returns (demeter/data/monthly_returns.csv) and our daily market data (model/data/market_daily.csv).

Writes results/demeter_inference.json and a set of markdown tables (scratch) used to assemble
results/demeter_inference.md.  Nothing here feeds a trading signal; it is descriptive inference only.
"""
from __future__ import annotations
import json, sys, itertools
from pathlib import Path
import numpy as np, pandas as pd

HERE = Path(__file__).resolve().parent.parent          # model/
sys.path.insert(0, str(HERE))
import engine as E                                     # noqa: E402

SCRATCH = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "results"
SCRATCH.mkdir(parents=True, exist_ok=True)
OUT_JSON = HERE / "results" / "demeter_inference.json"

df = E.load_market()
dem = E.load_demeter()                                 # index = month end; strategy, spy in percent
J: dict = {}
T: dict[str, str] = {}                                  # markdown tables


def md_table(frame: pd.DataFrame, floatfmt="{:.2f}", index=True) -> str:
    f = frame.copy()
    for c in f.columns:
        if pd.api.types.is_float_dtype(f[c]):
            f[c] = f[c].map(lambda v: "" if pd.isna(v) else floatfmt.format(v))
    if index:
        f = f.reset_index()
    cols = list(f.columns)
    lines = ["| " + " | ".join(str(c) for c in cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for _, r in f.iterrows():
        lines.append("| " + " | ".join(str(v) for v in r.values) + " |")
    return "\n".join(lines)


# --------------------------------------------------------------------------------------------- monthly frame
m = dem.copy()
m["strategy"] = m["strategy"].astype(float); m["spy"] = m["spy"].astype(float)
daily_ret = df["spx_tr_ret"]
m["spy_ours"] = (E.to_monthly(daily_ret) * 100).reindex(m.index)
_ndays = daily_ret.resample("ME").count().reindex(m.index)
m.loc[_ndays.fillna(0) < 15, "spy_ours"] = np.nan          # partial months (Feb-2026 has 8 days) are not usable
m["rf_m"] = (E.to_monthly(df["rf_daily"]) * 100).reindex(m.index)
vix = df["vix_close"].dropna()
m["vix_avg"] = vix.resample("ME").mean().reindex(m.index)
m["vix_start"] = vix.resample("ME").last().shift(1).reindex(m.index)     # VIX close on the last day of the prior month (known at the first decision)
m["vix_end"] = vix.resample("ME").last().reindex(m.index)
m["vix_max"] = vix.resample("ME").max().reindex(m.index)
m["vix_chg_pct"] = (m["vix_end"] / m["vix_start"] - 1) * 100
m["rv_ann"] = (daily_ret.resample("ME").std(ddof=1) * np.sqrt(252) * 100).reindex(m.index)
m["spy_prev"] = m["spy"].shift(1)
m["strat_prev"] = m["strategy"].shift(1)
m["exposure"] = np.where(m["spy"].abs() > 2.0, m["strategy"] / m["spy"], np.nan)
m["full_cash"] = m["strategy"] == 0.0
# compounding-consistent constant-leverage equivalent L* from daily data: prod(1 + L*x_d) = 1 + strat  (cash earns 0, as the 0.00 months imply)
x_daily = (df["spx_tr_ret"] - df["rf_daily"])


def const_lev_equiv(month_end: pd.Timestamp, target_pct: float, lo=-1.0, hi=6.0):
    xs = x_daily.loc[month_end.strftime("%Y-%m")].values
    if len(xs) < 15 or np.isnan(xs).any():
        return np.nan
    f = lambda L: np.prod(1 + L * xs) - 1 - target_pct / 100
    a, b = f(lo), f(hi)
    if a * b > 0:
        return np.nan
    for _ in range(80):
        mid = 0.5 * (lo + hi); fm = f(mid)
        if a * fm <= 0: hi, b = mid, fm
        else: lo, a = mid, fm
    return 0.5 * (lo + hi)


m["L_const"] = [const_lev_equiv(i, s) if not pd.isna(so) else np.nan for i, s, so in zip(m.index, m["strategy"], m["spy_ours"])]

# ------------------------------------------------------------------------------------------------- (a)
a_tab = m[["strategy", "spy", "exposure", "vix_avg", "full_cash"]].copy()
a_tab.index = a_tab.index.strftime("%Y-%m")
a_tab["flag"] = np.where(m["full_cash"].values, "FULL CASH (0.00)",
                np.where(m["exposure"].abs() < 0.25, "~0 (cash-dominated)",
                np.where(m["exposure"] > 1.5, ">1.5x", np.where(m["exposure"] < 0, "SIGN FLIP (intra-month timing)", ""))))
a_tab["flag"] = np.where(m["exposure"].isna() & ~m["full_cash"].values, "|SPY|<=2%: n/a", a_tab["flag"])
big = m["spy"].abs() > 2.0
J["a_implied_exposure"] = {
    "definition": "implied exposure = strategy / SPY monthly return, only where |SPY| > 2% (ratio unstable otherwise); L_const = constant daily leverage that reproduces the month's return from our daily data with cash earning 0",
    "n_months_total": int(len(m)), "n_months_abs_spy_gt_2": int(big.sum()),
    "full_cash_months": [i.strftime("%Y-%m") for i in m.index[m["full_cash"]]],
    "full_cash_months_spy": {i.strftime("%Y-%m"): float(m.loc[i, "spy"]) for i in m.index[m["full_cash"]]},
    "rows": [{"month": i.strftime("%Y-%m"), "strategy": float(r.strategy), "spy": float(r.spy),
              "exposure": None if pd.isna(r.exposure) else round(float(r.exposure), 3),
              "L_const": None if pd.isna(r.L_const) else round(float(r.L_const), 3),
              "vix_avg": None if pd.isna(r.vix_avg) else round(float(r.vix_avg), 2),
              "vix_start": None if pd.isna(r.vix_start) else round(float(r.vix_start), 2),
              "vix_chg_pct": None if pd.isna(r.vix_chg_pct) else round(float(r.vix_chg_pct), 1),
              "rv_ann": None if pd.isna(r.rv_ann) else round(float(r.rv_ann), 1),
              "full_cash": bool(r.full_cash)} for i, r in m.iterrows()],
}
T["a_full"] = md_table(a_tab.rename(columns={"strategy": "Demeter %", "spy": "SPY %", "exposure": "implied exp.", "vix_avg": "VIX avg"}).drop(columns=["full_cash"]))
# yearly summary of implied exposure
yr = m[big].groupby(m[big].index.year)["exposure"].agg(["count", "mean", "median", "min", "max"])
yr_all = m.groupby(m.index.year).apply(lambda g: pd.Series({"strat_yr": (np.prod(1 + g.strategy / 100) - 1) * 100, "spy_yr": (np.prod(1 + g.spy / 100) - 1) * 100,
                                                            "cash_months": int(g.full_cash.sum()), "vix_avg": g.vix_avg.mean()}))
yr_tab = yr_all.join(yr.rename(columns={"count": "n(|SPY|>2%)", "mean": "exp mean", "median": "exp median", "min": "exp min", "max": "exp max"}))
yr_tab.index.name = "year"
yr_tab[["cash_months", "n(|SPY|>2%)"]] = yr_tab[["cash_months", "n(|SPY|>2%)"]].fillna(0).astype(int)
T["a_yearly"] = md_table(yr_tab)
J["a_implied_exposure"]["yearly"] = {str(k): {c: (None if pd.isna(v) else round(float(v), 3)) for c, v in r.items()} for k, r in yr_tab.iterrows()}

# ------------------------------------------------------------------------------------------------- (b) rolling
def capture(s, b):
    up, dn = b > 0, b < 0
    geo = lambda z: (np.prod(1 + z / 100) ** (1 / len(z)) - 1) * 100 if len(z) else np.nan
    return (geo(s[up]) / geo(b[up]) * 100 if up.sum() else np.nan, geo(s[dn]) / geo(b[dn]) * 100 if dn.sum() else np.nan)


def rolling_stats(win):
    rows = []
    for i in range(win - 1, len(m)):
        g = m.iloc[i - win + 1:i + 1]
        s, b = g["strategy"], g["spy"]
        beta = s.cov(b) / b.var(ddof=1)
        up, dn = capture(s, b)
        rows.append({"month": g.index[-1].strftime("%Y-%m"), "beta": beta, "corr": s.corr(b), "up_capture": up, "down_capture": dn,
                     "strat_ann": ((np.prod(1 + s / 100)) ** (12 / win) - 1) * 100, "spy_ann": ((np.prod(1 + b / 100)) ** (12 / win) - 1) * 100,
                     "n_up": int((b > 0).sum()), "n_dn": int((b < 0).sum())})
    return pd.DataFrame(rows).set_index("month")


r12, r36 = rolling_stats(12), rolling_stats(36)
J["b_rolling"] = {"rolling_12m": [{"month": i, **{k: (None if pd.isna(v) else round(float(v), 3)) for k, v in r.items()}} for i, r in r12.iterrows()],
                  "rolling_36m": [{"month": i, **{k: (None if pd.isna(v) else round(float(v), 3)) for k, v in r.items()}} for i, r in r36.iterrows()],
                  "summary_12m": {"beta_min": float(r12.beta.min()), "beta_min_month": r12.beta.idxmin(), "beta_max": float(r12.beta.max()), "beta_max_month": r12.beta.idxmax(),
                                  "beta_median": float(r12.beta.median()), "pct_windows_beta_lt_0.5": float((r12.beta < 0.5).mean() * 100),
                                  "pct_windows_beta_gt_1": float((r12.beta > 1).mean() * 100), "pct_windows_beta_neg": float((r12.beta < 0).mean() * 100),
                                  "down_capture_median": float(r12.down_capture.median()), "up_capture_median": float(r12.up_capture.median())},
                  "summary_36m": {"beta_min": float(r36.beta.min()), "beta_min_month": r36.beta.idxmin(), "beta_max": float(r36.beta.max()), "beta_max_month": r36.beta.idxmax(),
                                  "beta_median": float(r36.beta.median()), "down_capture_median": float(r36.down_capture.median()), "up_capture_median": float(r36.up_capture.median())}}
sel12 = r12[r12.index.str.endswith(("-06", "-12"))]
T["b_r12"] = md_table(sel12[["beta", "corr", "up_capture", "down_capture", "strat_ann", "spy_ann"]].rename(columns={"strat_ann": "Demeter 12m %", "spy_ann": "SPY 12m %"}))
sel36 = r36[r36.index.str.endswith(("-06", "-12"))]
T["b_r36"] = md_table(sel36[["beta", "corr", "up_capture", "down_capture", "strat_ann", "spy_ann"]].rename(columns={"strat_ann": "Demeter 36m ann %", "spy_ann": "SPY 36m ann %"}))
# extremes
ext = pd.concat([r12.loc[[r12.beta.idxmin(), r12.beta.idxmax(), r12.down_capture.idxmin(), r12.down_capture.idxmax(), r12.up_capture.idxmax(), r12.up_capture.idxmin()]]])
ext["note"] = ["min 12m beta", "max 12m beta", "min 12m down-capture", "max 12m down-capture", "max 12m up-capture", "min 12m up-capture"]
T["b_ext"] = md_table(ext[["note", "beta", "corr", "up_capture", "down_capture", "strat_ann", "spy_ann"]])

# ------------------------------------------------------------------------------------------------- (c) down months & rebounds
dn_months = m[m["spy"] < -3.0].copy()
rows = []
for i in dn_months.index:
    pos = m.index.get_loc(i)
    nxt = m.iloc[pos + 1] if pos + 1 < len(m) else None
    nxt2 = m.iloc[pos + 2] if pos + 2 < len(m) else None
    # daily path of the month: return to the trough, day of trough (only where daily data cover the full month)
    ym = i.strftime("%Y-%m")
    if pd.isna(m.loc[i, "spy_ours"]):
        trough_day = pd.NaT; first_half = second_half = np.nan; path = pd.Series([np.nan])
    else:
        dd = df.loc[ym, "spx_tr"]
        px = df["spx_tr"]; prev_close_idx = px.index.get_loc(dd.index[0]) - 1
        path = dd / px.iloc[prev_close_idx] - 1
        trough_day = path.idxmin()
        first_half = (px.loc[dd.index[len(dd) // 2 - 1]] / px.iloc[prev_close_idx] - 1) * 100
        second_half = (px.loc[dd.index[-1]] / px.loc[dd.index[len(dd) // 2 - 1]] - 1) * 100
    rows.append({"month": i.strftime("%Y-%m"), "SPY": m.loc[i, "spy"], "Demeter": m.loc[i, "strategy"], "exposure": m.loc[i, "exposure"], "L_const": m.loc[i, "L_const"],
                 "SPY 1st half": first_half, "SPY 2nd half": second_half, "trough day": ("" if pd.isna(trough_day) else trough_day.strftime("%d")), "min path %": float(path.min() * 100),
                 "VIX start": m.loc[i, "vix_start"], "VIX max": m.loc[i, "vix_max"], "VIX end": m.loc[i, "vix_end"],
                 "next SPY": None if nxt is None else nxt.spy, "next Demeter": None if nxt is None else nxt.strategy, "next exp": None if nxt is None else nxt.exposure,
                 "next2 SPY": None if nxt2 is None else nxt2.spy, "next2 Demeter": None if nxt2 is None else nxt2.strategy, "next2 exp": None if nxt2 is None else nxt2.exposure})
c_tab = pd.DataFrame(rows).set_index("month")
T["c_down"] = md_table(c_tab[["SPY", "Demeter", "exposure", "L_const", "SPY 1st half", "SPY 2nd half", "trough day", "VIX start", "VIX max", "VIX end"]])
T["c_rebound"] = md_table(c_tab[["SPY", "Demeter", "next SPY", "next Demeter", "next exp", "next2 SPY", "next2 Demeter", "next2 exp"]])
J["c_down_months"] = {"threshold": "SPY < -3%", "rows": [{k: (None if (isinstance(v, float) and pd.isna(v)) or v is None else (round(float(v), 3) if isinstance(v, (float, np.floating)) else v)) for k, v in r.items()} for r in rows]}
J["c_down_months"]["summary"] = {
    "n": int(len(c_tab)), "mean_exposure": float(c_tab.exposure.mean()), "median_exposure": float(c_tab.exposure.median()),
    "n_beat_spy": int((c_tab.Demeter > c_tab.SPY).sum()), "n_positive": int((c_tab.Demeter > 0).sum()), "n_full_cash": int((c_tab.Demeter == 0).sum()),
    "n_exposure_gt_1": int((c_tab.exposure > 1).sum()), "months_exposure_gt_1": list(c_tab.index[c_tab.exposure > 1]),
    "next_month": {"mean_spy": float(c_tab["next SPY"].mean()), "mean_demeter": float(c_tab["next Demeter"].mean()),
                   "n_next_spy_up": int((c_tab["next SPY"] > 0).sum()), "mean_exp_when_next_spy_gt_2": float(c_tab.loc[c_tab["next SPY"] > 2, "next exp"].mean()),
                   "median_exp_when_next_spy_gt_2": float(c_tab.loc[c_tab["next SPY"] > 2, "next exp"].median())}}
# worst Demeter months and what SPY did
worst = m.nsmallest(12, "strategy")[["strategy", "spy", "exposure", "vix_start", "vix_avg", "vix_chg_pct", "rv_ann"]]
worst.index = worst.index.strftime("%Y-%m")
T["c_worst"] = md_table(worst.rename(columns={"strategy": "Demeter", "spy": "SPY", "vix_chg_pct": "VIX chg %", "rv_ann": "RV ann %"}))
J["c_down_months"]["worst_demeter_months"] = [{"month": i, **{k: (None if pd.isna(v) else round(float(v), 3)) for k, v in r.items()}} for i, r in worst.iterrows()]
bestm = m.nlargest(12, "strategy")[["strategy", "spy", "exposure", "vix_start", "vix_avg", "vix_chg_pct", "rv_ann"]]
bestm.index = bestm.index.strftime("%Y-%m")
T["c_best"] = md_table(bestm.rename(columns={"strategy": "Demeter", "spy": "SPY", "vix_chg_pct": "VIX chg %", "rv_ann": "RV ann %"}))
J["c_down_months"]["best_demeter_months"] = [{"month": i, **{k: (None if pd.isna(v) else round(float(v), 3)) for k, v in r.items()}} for i, r in bestm.iterrows()]

# ------------------------------------------------------------------------------------------------- (d) daily path inference
LEVELS = np.array([0.0, 1.0, 2.0, 3.0])


def month_x(ym):
    g = df.loc[ym]
    return g.index, (g["spx_tr_ret"] - g["rf_daily"]).values, g["spx_tr_ret"].values, g["vix_close"].values


def min_switch_paths(ym, target_pct, max_k=3, tol=None, levels=LEVELS, cost_bps=2.0):
    """Enumerate piecewise-constant leverage paths (levels in `levels`, at most max_k switches within the month,
    cash earning 0) whose compounded month return matches target within tol.  Returns dict by k."""
    idx, xs, tr, vx = month_x(ym)
    n = len(xs)
    tol = tol if tol is not None else max(0.25, 0.02 * abs(target_pct))
    logs = {L: np.concatenate([[0.0], np.cumsum(np.log1p(L * xs))]) for L in levels}   # cumulative log return per level
    out = {}
    for k in range(0, max_k + 1):
        sols = []
        for cuts in itertools.combinations(range(1, n), k):
            bounds = (0,) + cuts + (n,)
            for levs in itertools.product(levels, repeat=k + 1):
                if any(levs[j] == levs[j + 1] for j in range(k)):
                    continue
                lr = sum(logs[levs[j]][bounds[j + 1]] - logs[levs[j]][bounds[j]] for j in range(k + 1))
                cost = (abs(levs[0]) + sum(abs(levs[j + 1] - levs[j]) for j in range(k))) * cost_bps / 1e4  # entry from cash at month start counted (conservative)
                ret = (np.exp(lr) - 1 - cost) * 100
                if abs(ret - target_pct) <= tol:
                    lev_path = np.concatenate([np.full(bounds[j + 1] - bounds[j], levs[j]) for j in range(k + 1)])
                    sols.append({"levels": [float(v) for v in levs], "cuts": [idx[c].strftime("%m-%d") for c in cuts], "ret": ret,
                                 "days_3x": int((lev_path == 3).sum()), "days_2x": int((lev_path == 2).sum()), "days_1x": int((lev_path == 1).sum()), "days_cash": int((lev_path == 0).sum()),
                                 "path": lev_path})
        out[k] = sols
        if sols:
            break
    return out, idx, xs, tr, vx


def describe_paths(ym, target, max_k=3, tol=None):
    res, idx, xs, tr, vx = min_switch_paths(ym, target, max_k=max_k, tol=tol)
    k = next((kk for kk, s in res.items() if s), None)
    d = {"month": ym, "target": target, "spy": float((np.prod(1 + tr) - 1) * 100), "min_switches": k, "n_solutions": 0}
    if k is None:
        d["note"] = f"no path with <= {max_k} switches in levels {list(LEVELS)} matches"
        return d, None
    sols = res[k]
    d["n_solutions"] = len(sols)
    paths = np.array([s["path"] for s in sols])
    d["frac_solutions_invested_by_day"] = {idx[j].strftime("%m-%d"): round(float((paths[:, j] > 0).mean()), 2) for j in range(len(idx))}
    d["mean_lev_by_day"] = {idx[j].strftime("%m-%d"): round(float(paths[:, j].mean()), 2) for j in range(len(idx))}
    d["days_always_invested"] = [idx[j].strftime("%m-%d") for j in range(len(idx)) if (paths[:, j] > 0).all()]
    d["days_never_invested"] = [idx[j].strftime("%m-%d") for j in range(len(idx)) if (paths[:, j] == 0).all()]
    d["days_3x_range"] = [int(paths.__eq__(3).sum(1).min()), int(paths.__eq__(3).sum(1).max())]
    d["days_cash_range"] = [int(paths.__eq__(0).sum(1).min()), int(paths.__eq__(0).sum(1).max())]
    d["avg_lev_range"] = [round(float(paths.mean(1).min()), 2), round(float(paths.mean(1).max()), 2)]
    d["examples"] = [{kk: v for kk, v in s.items() if kk != "path"} for s in sorted(sols, key=lambda s: (s["days_3x"] + s["days_2x"], s["days_1x"]))[:4]] + \
                    [{kk: v for kk, v in s.items() if kk != "path"} for s in sorted(sols, key=lambda s: -(s["days_3x"]))[:3]]
    for e in d["examples"]:
        e["ret"] = round(float(e["ret"]), 2)
    return d, sols


def const_lev_table(ym):
    idx, xs, tr, vx = month_x(ym)
    return {f"{L:.0f}x": round(float((np.prod(1 + L * xs) - 1) * 100), 2) for L in LEVELS} | {
        "perfect_foresight_3x_up_days_only": round(float((np.prod(np.where(xs > 0, 1 + 3 * xs, 1.0)) - 1) * 100), 2),
        "3x_on_up_days_1x_on_down_days": round(float((np.prod(np.where(xs > 0, 1 + 3 * xs, 1 + xs)) - 1) * 100), 2),
        "n_days": int(len(xs)), "n_up": int((xs > 0).sum()), "n_down": int((xs < 0).sum()),
        "sum_up_pct": round(float(xs[xs > 0].sum() * 100), 2), "sum_down_pct": round(float(xs[xs < 0].sum() * 100), 2),
        "vix_first": round(float(vx[0]), 1), "vix_last": round(float(vx[-1]), 1), "vix_min": round(float(np.nanmin(vx)), 1), "vix_max": round(float(np.nanmax(vx)), 1),
        "rv_ann_pct": round(float(np.std(tr, ddof=1) * np.sqrt(252) * 100), 1)}


def daily_table(ym):
    g = df.loc[ym, ["spx_tr_ret", "vix_close"]].copy()
    g["SPY ret %"] = g["spx_tr_ret"] * 100
    g["cum SPY %"] = ((1 + g["spx_tr_ret"]).cumprod() - 1) * 100
    g["VIX"] = g["vix_close"]
    g["3x day ret %"] = 3 * (g["spx_tr_ret"] - df.loc[ym, "rf_daily"]) * 100
    g.index = g.index.strftime("%Y-%m-%d")
    return g[["SPY ret %", "cum SPY %", "VIX", "3x day ret %"]]


J["d_daily_inference"] = {"method": "For each month, enumerate every piecewise-constant leverage path with levels {0,1,2,3}, at most K switches inside the month "
                          "(position decided at the prior close, cash earns 0, 2 bp per unit notional traded), and keep the paths whose compounded return matches Demeter's "
                          "published month within tolerance (max(0.25%, 2% of |target|)). The smallest K with a solution is the minimum number of intra-month position changes "
                          "the record forces; the set of solutions shows which days MUST have been invested/in cash. Plus constant-leverage and perfect-foresight benchmarks.",
                          "months": {}}
key_months = ["2020-02", "2020-03", "2020-04", "2020-05", "2020-11", "2015-06", "2015-08", "2018-02", "2018-10", "2018-12", "2019-05", "2019-08", "2023-10", "2025-01", "2025-02", "2025-03", "2025-04"] + [f"2022-{mm:02d}" for mm in range(1, 13)]
for ym in key_months:
    tgt = float(dem.loc[pd.Timestamp(ym) + pd.offsets.MonthEnd(0), "strategy"])
    maxk = 4 if ym in ("2020-03",) else 3
    dsc, sols = describe_paths(ym, tgt, max_k=maxk)
    dsc["benchmarks"] = const_lev_table(ym)
    dsc["L_const"] = None if pd.isna(m.loc[pd.Timestamp(ym) + pd.offsets.MonthEnd(0), "L_const"]) else round(float(m.loc[pd.Timestamp(ym) + pd.offsets.MonthEnd(0), "L_const"]), 2)
    J["d_daily_inference"]["months"][ym] = dsc
    print(ym, "target", tgt, "min switches", dsc["min_switches"], "n sol", dsc["n_solutions"], "L_const", dsc["L_const"], "3x days range", dsc.get("days_3x_range"), "always inv", dsc.get("days_always_invested"), "never", dsc.get("days_never_invested"))

for ym in ["2020-02", "2020-03", "2020-04"]:
    T[f"d_daily_{ym}"] = md_table(daily_table(ym))

# Mar 2020 special scenarios
idx, xs, tr, vx = month_x("2020-03")
scen = {}
# (i) cash until close of day D, then 3x to month end
for j in range(len(idx)):
    scen[f"3x from {idx[j].strftime('%m-%d')} to month-end"] = round(float((np.prod(1 + 3 * xs[j:]) - 1) * 100), 2)
J["d_daily_inference"]["mar2020_enter_3x_and_hold"] = scen
# (ii) one-day mean reversion: long L after a down day, cash after an up day (decided at close, applied next day) - Feb, Mar, Apr 2020
def mr1(ym, L):
    g = df.loc[:ym]
    g = g.loc[g.index >= pd.Timestamp(ym) - pd.Timedelta(days=3)]
    x_all = (df["spx_tr_ret"] - df["rf_daily"])
    sig = (df["spx_tr_ret"] < 0).astype(float) * L           # decided at close t
    pos = sig.shift(1)
    r = (pos * x_all).loc[ym]
    return round(float((np.prod(1 + r) - 1) * 100), 2), int((pos.loc[ym] > 0).sum())
J["d_daily_inference"]["one_day_mean_reversion_after_down_day"] = {ym: {f"L={L:.0f}": mr1(ym, L) for L in (1, 2, 3)} for ym in ["2020-02", "2020-03", "2020-04", "2020-05"]}
# (iii) 3x on the day after a >=+3% up day (momentum/continuation) as contrast
def mom1(ym, L, thr=0.03):
    x_all = (df["spx_tr_ret"] - df["rf_daily"])
    pos = ((df["spx_tr_ret"] > thr).astype(float) * L).shift(1)
    r = (pos * x_all).loc[ym]
    return round(float((np.prod(1 + r) - 1) * 100), 2), int((pos.loc[ym] > 0).sum())
J["d_daily_inference"]["long_after_big_up_day_contrast"] = {ym: {f"L={L:.0f}": mom1(ym, L) for L in (1, 3)} for ym in ["2020-03", "2020-04"]}
# (iv) VIX-gated: cash when VIX > thr
def vixgate(ym, thr, L):
    x_all = (df["spx_tr_ret"] - df["rf_daily"])
    pos = ((df["vix_close"] < thr).astype(float) * L).shift(1)
    r = (pos * x_all).loc[ym]
    return round(float((np.prod(1 + r) - 1) * 100), 2), int((pos.loc[ym] > 0).sum())
J["d_daily_inference"]["vix_level_gate_contrast"] = {ym: {f"VIX<{t}, L=3": vixgate(ym, t, 3) for t in (20, 25, 30, 40, 50)} for ym in ["2020-03", "2020-04", "2022-07", "2022-10"]}
# (v) 200-day SMA trend filter contrast
sma200 = df["spx_px"].rolling(200).mean()
def trendgate(ym, L):
    x_all = (df["spx_tr_ret"] - df["rf_daily"])
    pos = ((df["spx_px"] > sma200).astype(float) * L).shift(1)
    r = (pos * x_all).loc[ym]
    return round(float((np.prod(1 + r) - 1) * 100), 2), int((pos.loc[ym] > 0).sum())
J["d_daily_inference"]["sma200_trend_gate_contrast"] = {ym: {"L=3": trendgate(ym, 3), "L=1": trendgate(ym, 1)} for ym in ["2020-03", "2020-04", "2020-05", "2022-03", "2022-07", "2022-10", "2022-11"]}
days_below_200 = {ym: int((df.loc[ym, "spx_px"] < sma200.loc[ym]).sum()) for ym in ["2020-03", "2020-04", "2020-05", "2022-07", "2022-10", "2022-11", "2023-01"]}
J["d_daily_inference"]["days_below_sma200"] = days_below_200

# 2022 month summary table
rows22 = []
for mm in range(1, 13):
    ym = f"2022-{mm:02d}"; me = pd.Timestamp(ym) + pd.offsets.MonthEnd(0)
    dsc = J["d_daily_inference"]["months"][ym]; b = dsc["benchmarks"]
    rows22.append({"month": ym, "SPY": m.loc[me, "spy"], "Demeter": m.loc[me, "strategy"], "exposure": m.loc[me, "exposure"], "L_const": m.loc[me, "L_const"],
                   "min switches": dsc["min_switches"], "n paths": dsc["n_solutions"], "3x days (min-max)": f"{dsc['days_3x_range'][0]}-{dsc['days_3x_range'][1]}" if dsc["min_switches"] is not None else "",
                   "cash days (min-max)": f"{dsc['days_cash_range'][0]}-{dsc['days_cash_range'][1]}" if dsc["min_switches"] is not None else "",
                   "1x all month": b["1x"], "3x all month": b["3x"], "VIX first": b["vix_first"], "VIX last": b["vix_last"], "RV %": b["rv_ann_pct"], "days<SMA200": int((df.loc[ym, "spx_px"] < sma200.loc[ym]).sum())})
t22 = pd.DataFrame(rows22).set_index("month")
T["d_2022"] = md_table(t22)
J["d_daily_inference"]["table_2022"] = [{k: (None if isinstance(v, float) and pd.isna(v) else (round(float(v), 3) if isinstance(v, (float, np.floating)) else (int(v) if isinstance(v, (np.integer,)) else v))) for k, v in r.items()} for r in rows22]
# 2020 table
rows20 = []
for ym in ["2020-01", "2020-02", "2020-03", "2020-04", "2020-05", "2020-06", "2020-09", "2020-10", "2020-11"]:
    me = pd.Timestamp(ym) + pd.offsets.MonthEnd(0)
    b = const_lev_table(ym)
    dsc = J["d_daily_inference"]["months"].get(ym)
    rows20.append({"month": ym, "SPY": m.loc[me, "spy"], "Demeter": m.loc[me, "strategy"], "exposure": m.loc[me, "exposure"], "L_const": m.loc[me, "L_const"],
                   "min switches": "" if dsc is None or dsc["min_switches"] is None else str(dsc["min_switches"]), "3x days (min-max)": "" if dsc is None or dsc["min_switches"] is None else f"{dsc['days_3x_range'][0]}-{dsc['days_3x_range'][1]}",
                   "1x": b["1x"], "2x": b["2x"], "3x": b["3x"], "3x up-days only": b["perfect_foresight_3x_up_days_only"], "VIX first": b["vix_first"], "VIX last": b["vix_last"], "RV %": b["rv_ann_pct"]})
T["d_2020"] = md_table(pd.DataFrame(rows20).set_index("month"))

# generic: min switches needed across all 163 months (K<=2 only, for speed)
allk = []
for me in m.index:
    if pd.isna(m.loc[me, "spy_ours"]):
        continue
    ym = me.strftime("%Y-%m"); tgt = float(m.loc[me, "strategy"])
    res, *_ = min_switch_paths(ym, tgt, max_k=2)
    k = next((kk for kk, s in res.items() if s), None)
    allk.append({"month": ym, "min_k": k, "n": 0 if k is None else len(res[k])})
allk = pd.DataFrame(allk).set_index("month")
J["d_daily_inference"]["min_switches_all_months"] = {"counts": {str(k): int(v) for k, v in allk["min_k"].value_counts(dropna=False).sort_index().items()},
                                                     "months_needing_ge_3_switches": list(allk.index[allk["min_k"].isna()]),
                                                     "months_k0_constant_level": list(allk.index[allk["min_k"] == 0]),
                                                     "note": "K is the minimum number of intra-month position changes among {0,1,2,3}-level paths that reproduce the month; "
                                                             "NaN = needs 3+ switches. K=0 months are reproducible by a constant level all month (includes the 0.00 cash months)."}
print(allk["min_k"].value_counts(dropna=False))

# ------------------------------------------------------------------------------------------------- (e) summary
bigm = m[big].copy()
e = {}
e["n_months_abs_spy_gt_2"] = int(len(bigm))
e["share_exposure_gt_1.5"] = float((bigm.exposure > 1.5).mean() * 100)
e["share_exposure_0.5_to_1.5"] = float(((bigm.exposure >= 0.5) & (bigm.exposure <= 1.5)).mean() * 100)
e["share_exposure_near_0"] = float((bigm.exposure.abs() < 0.25).mean() * 100)
e["share_exposure_0.25_to_0.5"] = float(((bigm.exposure.abs() >= 0.25) & (bigm.exposure < 0.5)).mean() * 100)
e["share_exposure_negative_lt_-0.25"] = float((bigm.exposure < -0.25).mean() * 100)
e["share_exposure_gt_2"] = float((bigm.exposure > 2).mean() * 100)
e["months_exposure_gt_1.5"] = [f"{i.strftime('%Y-%m')} ({r.exposure:.2f}x, SPY {r.spy:+.1f})" for i, r in bigm[bigm.exposure > 1.5].iterrows()]
e["months_exposure_negative"] = [f"{i.strftime('%Y-%m')} ({r.exposure:.2f}x, SPY {r.spy:+.1f}, Dem {r.strategy:+.2f})" for i, r in bigm[bigm.exposure < -0.25].iterrows()]
e["mean_exposure_all"] = float(bigm.exposure.mean()); e["median_exposure_all"] = float(bigm.exposure.median())
e["mean_exposure_trimmed_10pct"] = float(bigm.exposure.clip(bigm.exposure.quantile(0.1), bigm.exposure.quantile(0.9)).mean())
up, dn = bigm.spy > 2, bigm.spy < -2
e["exposure_in_up_months"] = {"n": int(up.sum()), "mean": float(bigm.exposure[up].mean()), "median": float(bigm.exposure[up].median()), "share_gt_1.5": float((bigm.exposure[up] > 1.5).mean() * 100), "share_lt_0.5": float((bigm.exposure[up] < 0.5).mean() * 100)}
e["exposure_in_down_months"] = {"n": int(dn.sum()), "mean": float(bigm.exposure[dn].mean()), "median": float(bigm.exposure[dn].median()), "share_gt_1": float((bigm.exposure[dn] > 1).mean() * 100), "share_lt_0.25": float((bigm.exposure[dn].abs() < 0.25).mean() * 100), "share_negative": float((bigm.exposure[dn] < 0).mean() * 100)}
# VIX splits (months with VIX data)
mv = m.dropna(subset=["vix_avg", "spy_ours"]).copy()   # full months with daily data only (Jul-2012..Jan-2026)
bv = mv[mv.spy.abs() > 2]
med = mv.vix_avg.median()
e["vix_split_median"] = {"median_vix_avg": float(med),
                         "low_vix": {"n_big_months": int((bv.vix_avg <= med).sum()), "mean_exposure": float(bv.exposure[bv.vix_avg <= med].mean()), "median_exposure": float(bv.exposure[bv.vix_avg <= med].median()),
                                     "mean_L_const": float(mv.L_const[mv.vix_avg <= med].mean()), "mean_demeter_ret": float(mv.strategy[mv.vix_avg <= med].mean()), "mean_spy_ret": float(mv.spy[mv.vix_avg <= med].mean()),
                                     "share_full_cash": float(mv.full_cash[mv.vix_avg <= med].mean() * 100)},
                         "high_vix": {"n_big_months": int((bv.vix_avg > med).sum()), "mean_exposure": float(bv.exposure[bv.vix_avg > med].mean()), "median_exposure": float(bv.exposure[bv.vix_avg > med].median()),
                                      "mean_L_const": float(mv.L_const[mv.vix_avg > med].mean()), "mean_demeter_ret": float(mv.strategy[mv.vix_avg > med].mean()), "mean_spy_ret": float(mv.spy[mv.vix_avg > med].mean()),
                                      "share_full_cash": float(mv.full_cash[mv.vix_avg > med].mean() * 100)}}
bins = [0, 13, 16, 20, 25, 30, 100]; labels = ["<13", "13-16", "16-20", "20-25", "25-30", ">30"]
mv["vix_bin"] = pd.cut(mv.vix_avg, bins, labels=labels)
vb = mv.groupby("vix_bin", observed=False).apply(lambda g: pd.Series({"n months": len(g), "n |SPY|>2%": int((g.spy.abs() > 2).sum()), "mean exposure": g.exposure.mean(), "median exposure": g.exposure.median(),
                                                                       "mean L_const": g.L_const.mean(), "median L_const": g.L_const.median(), "mean Demeter %": g.strategy.mean(), "mean SPY %": g.spy.mean(),
                                                                       "std Demeter %": g.strategy.std(), "std SPY %": g.spy.std(), "full-cash months": int(g.full_cash.sum())}))
vb[["n months", "n |SPY|>2%", "full-cash months"]] = vb[["n months", "n |SPY|>2%", "full-cash months"]].astype(int)
T["e_vixbins"] = md_table(vb)
e["vix_bins"] = {str(i): {k: (None if pd.isna(v) else round(float(v), 3)) for k, v in r.items()} for i, r in vb.iterrows()}
# same by VIX at start of month (causally known)
mv["vix_start_bin"] = pd.cut(mv.vix_start, bins, labels=labels)
vs = mv.groupby("vix_start_bin", observed=False).apply(lambda g: pd.Series({"n months": len(g), "n |SPY|>2%": int((g.spy.abs() > 2).sum()), "mean exposure": g.exposure.mean(), "median exposure": g.exposure.median(),
                                                                             "mean L_const": g.L_const.mean(), "mean Demeter %": g.strategy.mean(), "mean SPY %": g.spy.mean(), "full-cash months": int(g.full_cash.sum())}))
vs[["n months", "n |SPY|>2%", "full-cash months"]] = vs[["n months", "n |SPY|>2%", "full-cash months"]].astype(int)
T["e_vixstart"] = md_table(vs)
e["vix_start_bins"] = {str(i): {k: (None if pd.isna(v) else round(float(v), 3)) for k, v in r.items()} for i, r in vs.iterrows()}
# L_const distribution overall (all months with daily data)
lc = mv.L_const.dropna()
e["L_const_distribution"] = {"n": int(len(lc)), "mean": float(lc.mean()), "median": float(lc.median()), "share_lt_0.25": float((lc < 0.25).mean() * 100), "share_0.25_1.5": float(((lc >= 0.25) & (lc <= 1.5)).mean() * 100),
                             "share_gt_1.5": float((lc > 1.5).mean() * 100), "share_gt_3": float((lc > 3).mean() * 100), "share_negative": float((lc < 0).mean() * 100),
                             "note": "L_const>3 or <0 is impossible for a constant long-only position in [0,3]: those months PROVE intra-month timing (exposure varied with the path)."}
e["months_L_const_gt_3_or_negative"] = [f"{i.strftime('%Y-%m')} (L*={r.L_const:.2f}, SPY {r.spy:+.2f}, Dem {r.strategy:+.2f})" for i, r in mv[(mv.L_const > 3) | (mv.L_const < -0.05)].iterrows()]
e["months_L_const_unsolvable"] = [i.strftime("%Y-%m") for i, r in mv.iterrows() if pd.isna(r.L_const) and not pd.isna(r.spy_ours)]
# regressions: strategy on spy (linear, quadratic, up/down beta), with and without 2020-03
import statsmodels.api as sm
def regs(g):
    X = sm.add_constant(g.spy); lin = sm.OLS(g.strategy, X).fit()
    X2 = sm.add_constant(pd.DataFrame({"spy": g.spy, "spy2": g.spy ** 2})); quad = sm.OLS(g.strategy, X2).fit()
    X3 = sm.add_constant(pd.DataFrame({"up": g.spy.clip(lower=0), "dn": g.spy.clip(upper=0)})); pw = sm.OLS(g.strategy, X3).fit()
    return {"n": int(len(g)), "beta": float(lin.params.spy), "alpha_monthly_pct": float(lin.params.const), "r2": float(lin.rsquared),
            "quad_beta": float(quad.params.spy), "quad_convexity": float(quad.params.spy2), "quad_convexity_t": float(quad.tvalues.spy2),
            "up_beta": float(pw.params.up), "down_beta": float(pw.params.dn), "up_beta_t": float(pw.tvalues.up), "down_beta_t": float(pw.tvalues.dn),
            "skew_demeter": float(g.strategy.skew()), "skew_spy": float(g.spy.skew()), "kurt_demeter": float(g.strategy.kurt()), "kurt_spy": float(g.spy.kurt())}
e["regressions_all_months"] = regs(m)
e["regressions_ex_2020_02_to_04"] = regs(m.drop(pd.to_datetime(["2020-02-29", "2020-03-31", "2020-04-30"])))
# what predicts exposure? (contemporaneous reaction and causal predictors)
bb = mv[mv.spy.abs() > 2].dropna(subset=["exposure"])
def corr_sp(a, b_):
    ok = a.notna() & b_.notna()
    from scipy.stats import spearmanr
    return float(spearmanr(a[ok], b_[ok]).correlation)
e["exposure_correlates_spearman"] = {
    "vs_vix_avg_(contemporaneous)": corr_sp(bb.exposure, bb.vix_avg), "vs_vix_start_(causal)": corr_sp(bb.exposure, bb.vix_start),
    "vs_vix_change_within_month_(reaction)": corr_sp(bb.exposure, bb.vix_chg_pct), "vs_realised_vol_(contemporaneous)": corr_sp(bb.exposure, bb.rv_ann),
    "vs_prior_month_spy_(causal)": corr_sp(bb.exposure, bb.spy_prev), "vs_prior_month_demeter_(causal)": corr_sp(bb.exposure, bb.strat_prev), "vs_spy_same_month": corr_sp(bb.exposure, bb.spy),
    "up_months_only": {"vs_vix_start": corr_sp(bb.exposure[bb.spy > 2], bb.vix_start[bb.spy > 2]), "vs_vix_change": corr_sp(bb.exposure[bb.spy > 2], bb.vix_chg_pct[bb.spy > 2]),
                       "vs_vix_avg": corr_sp(bb.exposure[bb.spy > 2], bb.vix_avg[bb.spy > 2]), "vs_prior_spy": corr_sp(bb.exposure[bb.spy > 2], bb.spy_prev[bb.spy > 2]), "n": int((bb.spy > 2).sum())},
    "down_months_only": {"vs_vix_start": corr_sp(bb.exposure[bb.spy < -2], bb.vix_start[bb.spy < -2]), "vs_vix_change": corr_sp(bb.exposure[bb.spy < -2], bb.vix_chg_pct[bb.spy < -2]),
                         "vs_vix_avg": corr_sp(bb.exposure[bb.spy < -2], bb.vix_avg[bb.spy < -2]), "vs_prior_spy": corr_sp(bb.exposure[bb.spy < -2], bb.spy_prev[bb.spy < -2]), "n": int((bb.spy < -2).sum())}}
# exposure after a down month vs after an up month (mean reversion re-entry?)
e["exposure_after_prior_month"] = {"prior_spy_lt_-3": {"n": int((bb.spy_prev < -3).sum()), "mean_exp": float(bb.exposure[bb.spy_prev < -3].mean()), "median_exp": float(bb.exposure[bb.spy_prev < -3].median())},
                                   "prior_spy_-3_to_3": {"n": int(((bb.spy_prev >= -3) & (bb.spy_prev <= 3)).sum()), "mean_exp": float(bb.exposure[(bb.spy_prev >= -3) & (bb.spy_prev <= 3)].mean()), "median_exp": float(bb.exposure[(bb.spy_prev >= -3) & (bb.spy_prev <= 3)].median())},
                                   "prior_spy_gt_3": {"n": int((bb.spy_prev > 3).sum()), "mean_exp": float(bb.exposure[bb.spy_prev > 3].mean()), "median_exp": float(bb.exposure[bb.spy_prev > 3].median())}}
# strong rebound months: SPY > +5%
reb = m[m.spy > 5][["strategy", "spy", "exposure", "spy_prev", "vix_start", "vix_end", "vix_chg_pct"]]
reb.index = reb.index.strftime("%Y-%m")
T["e_strong_up"] = md_table(reb.rename(columns={"strategy": "Demeter", "spy": "SPY", "spy_prev": "prior SPY", "vix_chg_pct": "VIX chg %"}))
e["strong_up_months_spy_gt_5"] = {"n": int(len(reb)), "mean_exposure": float(reb.exposure.mean()), "median_exposure": float(reb.exposure.median()), "share_gt_1.5": float((reb.exposure > 1.5).mean() * 100),
                                   "rows": [{"month": i, **{k: (None if pd.isna(v) else round(float(v), 3)) for k, v in r.items()}} for i, r in reb.iterrows()]}
# vol-based estimate of leverage when invested
sd_s, sd_b = m.strategy.std(), m.spy.std()
mx = m.drop(pd.to_datetime(["2020-02-29", "2020-03-31", "2020-04-30"]))
e["vol_implied_leverage"] = {"monthly_std_demeter": float(sd_s), "monthly_std_spy": float(sd_b), "ratio": float(sd_s / sd_b),
                             "lev_when_invested_if_50pct_days_random": float(sd_s / sd_b / np.sqrt(0.5)),
                             "ex_2020_02_04": {"monthly_std_demeter": float(mx.strategy.std()), "monthly_std_spy": float(mx.spy.std()), "ratio": float(mx.strategy.std() / mx.spy.std()),
                                               "lev_when_invested_if_50pct_days_random": float(mx.strategy.std() / mx.spy.std() / np.sqrt(0.5))},
                             "note": "if the strategy is invested a random 50% of days at constant leverage L, its monthly std is about L*sqrt(0.5)*std(SPY); solving gives a rough L."}
# Demeter's daily quadrant counts vs our up/down day counts
oos = df.loc["2012-07-02":"2026-02-11"]
xo = oos["spx_tr_ret"] - oos["rf_daily"]
q = {"loss_avoidance": 804, "gain_sacrifice": 883, "amplified_gains": 1022, "amplified_losses": 768}
tot = sum(q.values())
e["quadrant_fingerprint"] = {"demeter_counts": q, "demeter_total_days": tot, "demeter_pct_cash": (q["loss_avoidance"] + q["gain_sacrifice"]) / tot * 100,
                             "P_market_up_given_invested": q["amplified_gains"] / (q["amplified_gains"] + q["amplified_losses"]) * 100,
                             "P_market_up_given_cash": q["gain_sacrifice"] / (q["gain_sacrifice"] + q["loss_avoidance"]) * 100,
                             "P_market_up_overall_demeter": (q["amplified_gains"] + q["gain_sacrifice"]) / tot * 100,
                             "P_invested_given_up_day": q["amplified_gains"] / (q["amplified_gains"] + q["gain_sacrifice"]) * 100,
                             "P_invested_given_down_day": q["amplified_losses"] / (q["amplified_losses"] + q["loss_avoidance"]) * 100,
                             "our_data_2012_07_to_2026_02": {"n_days": int(len(xo)), "pct_up": float((xo > 0).mean() * 100), "pct_up_tr": float((oos["spx_tr_ret"] > 0).mean() * 100),
                                                             "mean_abs_up_pct": float(xo[xo > 0].mean() * 100), "mean_abs_down_pct": float(xo[xo < 0].mean() * 100)},
                             "note": "Demeter's own counts imply only a ~4-5 point directional edge (market up 57% of invested days vs 52% of cash days): the return must come from "
                                     "magnitude (being levered on large up days, in cash on large down days), not from day-ahead direction.  Cash days had more up than down days "
                                     "(883 vs 804): cash spells persisted through rebounds."}
# daily magnitude check: in our data, days with |x| > 2% by regime
J["e_summary"] = e

# months with exposure sign flip: what did the path look like (first-half vs second-half SPY)
flip = m[(m.spy.abs() > 2) & (m.exposure < 0)]
fl_rows = []
for i in flip.index:
    ym = i.strftime("%Y-%m"); g = df.loc[ym, "spx_tr"]; prev = df["spx_tr"].iloc[df.index.get_loc(g.index[0]) - 1]
    mid = len(g) // 2
    fl_rows.append({"month": ym, "SPY": m.loc[i, "spy"], "Demeter": m.loc[i, "strategy"], "SPY 1st half %": (g.iloc[mid - 1] / prev - 1) * 100, "SPY 2nd half %": (g.iloc[-1] / g.iloc[mid - 1] - 1) * 100,
                    "VIX start": m.loc[i, "vix_start"], "VIX end": m.loc[i, "vix_end"]})
T["e_flip"] = md_table(pd.DataFrame(fl_rows).set_index("month"))
J["e_summary"]["sign_flip_months"] = fl_rows

# ------------------------------------------------------------------------------------------------- headline verification
w = m.loc["2012-07-31":"2026-01-31"]
rf_m = (E.to_monthly(df["rf_daily"])).reindex(w.index)
st = E.monthly_stats(w["strategy"] / 100, w["spy"] / 100, rf_m)
J["headline_verification_2012_07_2026_01"] = {k: float(v) for k, v in st.items() if isinstance(v, (int, float, np.floating, np.integer))}
J["headline_verification_2012_07_2026_01"]["spy_ours_vs_demeter_spy_corr"] = float(np.corrcoef(w.spy_ours, w.spy)[0, 1])
J["headline_verification_2012_07_2026_01"]["spy_ours_vs_demeter_spy_mad_pct"] = float((w.spy_ours - w.spy).abs().mean())
# T-bill in the 0.00 months (evidence cash is booked at 0)
J["cash_accounting"] = {i.strftime("%Y-%m"): {"tbill_month_pct": round(float(m.loc[i, "rf_m"]), 3), "published": 0.0} for i in m.index[m.full_cash]}


# ------------------------------------------------------------------------------------------------- extra: Feb-2020 exit scans, Apr-2020 entry scan
idx, xs, tr, vx = month_x("2020-02")
J["d_daily_inference"]["feb2020_3x_until_close_of_D_then_cash"] = {f"3x through {idx[j].strftime('%m-%d')}, cash after": round(float((np.prod(1 + 3 * xs[:j + 1]) - 1) * 100), 2) for j in range(len(idx))}
J["d_daily_inference"]["feb2020_3x_until_close_of_D_then_1x"] = {f"3x through {idx[j].strftime('%m-%d')}, 1x after": round(float((np.prod(1 + 3 * xs[:j + 1]) * np.prod(1 + xs[j + 1:]) - 1) * 100), 2) for j in range(len(idx))}
J["d_daily_inference"]["feb2020_2x_until_close_of_D_then_cash"] = {f"2x through {idx[j].strftime('%m-%d')}, cash after": round(float((np.prod(1 + 2 * xs[:j + 1]) - 1) * 100), 2) for j in range(len(idx))}
idx, xs, tr, vx = month_x("2020-04")
J["d_daily_inference"]["apr2020_cash_until_D_then_3x"] = {f"3x from {idx[j].strftime('%m-%d')} to month-end": round(float((np.prod(1 + 3 * xs[j:]) - 1) * 100), 2) for j in range(len(idx))}
# VIX path around the Mar-23 low (what a vol-dissipation trigger would have seen)
g = df.loc["2020-03-09":"2020-03-27", ["spx_tr_ret", "vix_close"]].copy()
g["vix_sma10"] = df["vix_close"].rolling(10).mean().loc[g.index]
g["vix_over_sma10"] = g["vix_close"] / g["vix_sma10"]
g["rv10_ann"] = (df["spx_tr_ret"].rolling(10).std(ddof=1) * np.sqrt(252) * 100).loc[g.index]
g["dd_from_high_pct"] = (df["spx_px"] / df["spx_px"].cummax() - 1).loc[g.index] * 100
g["rsi2"] = None
d_ = df["spx_px"].diff(); up_ = d_.clip(lower=0).ewm(alpha=1 / 2, min_periods=2, adjust=False).mean(); dn_ = (-d_.clip(upper=0)).ewm(alpha=1 / 2, min_periods=2, adjust=False).mean()
g["rsi2"] = (100 - 100 / (1 + up_ / dn_.replace(0, np.nan))).loc[g.index]
g["SPY ret %"] = g["spx_tr_ret"] * 100
g.index = g.index.strftime("%Y-%m-%d")
T["d_mar2020_vix_path"] = md_table(g[["SPY ret %", "vix_close", "vix_sma10", "vix_over_sma10", "rv10_ann", "dd_from_high_pct", "rsi2"]].rename(columns={"vix_close": "VIX", "vix_sma10": "VIX SMA10", "vix_over_sma10": "VIX/SMA10", "rv10_ann": "RV10 ann %", "dd_from_high_pct": "DD from high %", "rsi2": "RSI(2)"}))
J["d_daily_inference"]["mar2020_indicator_path"] = [{"date": i, **{k: (None if pd.isna(v) else round(float(v), 2)) for k, v in r.items()}} for i, r in g[["SPY ret %", "vix_close", "vix_sma10", "vix_over_sma10", "rv10_ann", "dd_from_high_pct", "rsi2"]].iterrows()]

# ------------------------------------------------------------------------------------------------- extra: archetype fingerprints (descriptive; NOT for tuning)
x_all = df["spx_tr_ret"] - df["rf_daily"]
rv21 = df["spx_tr_ret"].rolling(21).std(ddof=1) * np.sqrt(252)
vix_sma10 = df["vix_close"].rolling(10).mean()
arche = {
    "A. 3x buy-and-hold": pd.Series(3.0, index=df.index),
    "B. 1x buy-and-hold": pd.Series(1.0, index=df.index),
    "C. 1-day mean reversion: 3x after a down day, cash after an up day": (df["spx_tr_ret"] < 0).astype(float) * 3,
    "D. 1-day momentum: 3x after an up day, cash after a down day": (df["spx_tr_ret"] > 0).astype(float) * 3,
    "E. Realised-vol gate: 3x if RV21<15%, 1x if <25%, else cash": pd.Series(np.where(rv21 < 0.15, 3.0, np.where(rv21 < 0.25, 1.0, 0.0)), index=df.index),
    "F. VIX level gate: 3x if VIX<20 else cash": (df["vix_close"] < 20).astype(float) * 3,
    "G. VIX dissipation: 3x if VIX < its 10d SMA else cash": (df["vix_close"] < vix_sma10).astype(float) * 3,
    "H. 200d SMA trend: 3x above, cash below": (df["spx_px"] > sma200).astype(float) * 3,
    "I. Baseline volregime (trend AND vol): 3x RV<15 & trend, 1x RV<25 & trend": pd.Series(np.where((rv21 < 0.15) & (df["spx_px"] > sma200), 3.0, np.where((rv21 < 0.25) & (df["spx_px"] > sma200), 1.0, 0.0)), index=df.index),
}
rows = []
dm = m["strategy"].loc["2012-07-31":"2026-01-31"]
for name, lev in arche.items():
    r = E.run(df, lev, cost_bps=2.0, start="2012-07-01", end="2026-01-31")
    mm = (r.monthly() * 100).reindex(dm.index)
    mt = r.metrics()
    ok = mm.notna()
    sub = mm[ok]; dsub = dm[ok]
    ex = ~sub.index.isin(pd.to_datetime(["2020-02-29", "2020-03-31", "2020-04-30"]))
    rows.append({"archetype": name, "monthly corr with Demeter": float(sub.corr(dsub)), "corr ex Feb-Apr 2020": float(sub[ex].corr(dsub[ex])), "same-sign months %": float((np.sign(sub) == np.sign(dsub)).mean() * 100),
                 "RMSE %": float(np.sqrt(np.mean((sub - dsub) ** 2))), "CAGR %": mt["annualized_return_pct"], "Sharpe": mt.get("sharpe"), "maxDD %": mt["max_drawdown_pct"], "% cash days": mt["pct_days_cash"], "changes/yr": mt["position_changes_per_year"],
                 "Feb-20": float(sub.get(pd.Timestamp("2020-02-29"), np.nan)), "Mar-20": float(sub.get(pd.Timestamp("2020-03-31"), np.nan)), "Apr-20": float(sub.get(pd.Timestamp("2020-04-30"), np.nan)),
                 "2022 %": float((np.prod(1 + sub.loc["2022"] / 100) - 1) * 100)})
arch_tab = pd.DataFrame(rows).set_index("archetype")
T["f_archetypes"] = md_table(arch_tab)
J["f_archetype_fingerprints"] = {"note": "Descriptive fingerprint of coarse, un-tuned rule archetypes run through engine.run on 2012-07..2026-01 (2 bp costs). Used ONLY to say which family's monthly signature resembles the record; "
                                         "these numbers are in Demeter's live window and must not be used to tune model parameters.", "demeter_reference": {"CAGR %": 31.33, "Sharpe": 1.275, "maxDD %": -13.65, "Feb-20": -13.65, "Mar-20": 55.32, "Apr-20": 29.65, "2022 %": 19.24},
                                 "rows": [{"archetype": i, **{k: (None if pd.isna(v) else round(float(v), 3)) for k, v in r.items()}} for i, r in arch_tab.iterrows()]}
print(T["f_archetypes"])


# ------------------------------------------------------------------------------------------------- extra: named mild-down episodes (SPY between -1% and -3%)
named = ["2015-09", "2023-08", "2023-10", "2025-02", "2020-10", "2019-08", "2014-12", "2024-10"]
rows = []
for ym in named:
    me = pd.Timestamp(ym) + pd.offsets.MonthEnd(0)
    dsc = J["d_daily_inference"]["months"].get(ym)
    if dsc is None:
        dsc, _ = describe_paths(ym, float(m.loc[me, "strategy"]), max_k=3); dsc["benchmarks"] = const_lev_table(ym); J["d_daily_inference"]["months"][ym] = dsc
    b = dsc["benchmarks"]
    rows.append({"month": ym, "SPY": m.loc[me, "spy"], "Demeter": m.loc[me, "strategy"], "L_const": m.loc[me, "L_const"], "3x all month": b["3x"], "min switches": dsc["min_switches"],
                 "must be invested": ", ".join(dsc.get("days_always_invested", [])[:6]) + ("..." if len(dsc.get("days_always_invested", [])) > 6 else ""),
                 "must be cash": ", ".join(dsc.get("days_never_invested", [])[:6]) + ("..." if len(dsc.get("days_never_invested", [])) > 6 else ""),
                 "VIX start": m.loc[me, "vix_start"], "VIX end": m.loc[me, "vix_end"], "RV %": b["rv_ann_pct"]})
T["c_named_mild"] = md_table(pd.DataFrame(rows).set_index("month"))
J["c_down_months"]["named_mild_down_episodes"] = [{k: (None if isinstance(v, float) and pd.isna(v) else (round(float(v), 3) if isinstance(v, (float, np.floating)) else v)) for k, v in r.items()} for r in rows]

# save
E.save_json(J, OUT_JSON)
(SCRATCH / "tables.json").write_text(json.dumps(T, indent=1))
print("wrote", OUT_JSON, "and", SCRATCH / "tables.json")
