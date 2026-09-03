#!/usr/bin/env python3
"""
build_analytics.py -- Demeter Tactical Investments, "Dual-Engine Quantitative Equity
Strategy" (Share Class B, live Jul 2012, data through Jun 2026).

Rebuilds every factsheet statistic from the transcribed monthly returns, derives a
TB3MS (3-month T-bill) proxy for the Sharpe calculation, and reconciles the results
against the factsheet's own stated statistics table.

Inputs (read only, never modified)
    data/monthly_returns.csv                         168 monthly returns, Jul 2012 .. Jun 2026
    data/stated_figures.json                         factsheet tables, transcribed
    model/data/raw/steelcerberus_us_market_data.csv  daily 3-month T-bill ("Risk Free Rate")

Outputs
    data/tb3ms_monthly.csv   monthly TB3MS proxy (calendar-month mean of the daily rate)
    analytics.json           series, windows, tables and the reconciliation report

Run:  python3 build_analytics.py        (pure pandas/numpy; deterministic)

Definitions that reproduce the factsheet (see META_DEFINITIONS below for the full list):
    * std dev, Sharpe            population std (ddof=0) -- sample std does NOT reproduce the table
    * Sharpe                     mean(monthly excess over cash) x 12 / (pop-std(excess) x sqrt(12))
    * Sortino                    annualised geometric return / (RMS(min(r,0)) x sqrt(12)); no cash term
    * Jensen alpha               (mean(r) - beta x mean(spy)) x 12, i.e. OLS intercept x 12, cash dropped
    * up/down capture            annualised compounded return of strategy in SPY up (down) months /
                                 annualised compounded return of SPY in the same months x 100
"""

import json
import math
import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RETURNS_CSV = os.path.join(HERE, "data", "monthly_returns.csv")
STATED_JSON = os.path.join(HERE, "data", "stated_figures.json")
RAW_RFR_CSV = os.path.join(HERE, "model", "data", "raw", "steelcerberus_us_market_data.csv")
TB3MS_CSV = os.path.join(HERE, "data", "tb3ms_monthly.csv")
OUT_JSON = os.path.join(HERE, "analytics.json")

SQ12 = math.sqrt(12.0)
STD_DDOF = 0  # population std reproduces the stated table; sample std does not

STATED_WINDOWS = {
    "since_inception": ("2012-07", "2026-06"),
    "rolling_12m": ("2025-07", "2026-06"),
    "rolling_60m": ("2021-07", "2026-06"),
    "rolling_120m": ("2016-07", "2026-06"),
}
EXTRA_WINDOWS = {
    "family_office": ("2012-07", "2023-07"),
    "commingled_fund": ("2023-08", "2026-06"),
}
STATED_METRICS = [
    "total_growth_pct", "annualized_return_pct", "annualized_std_dev", "max_drawdown_pct",
    "pct_positive_months", "sharpe", "sortino", "calmar", "correlation_to_spy", "beta_to_spy",
    "alpha_ann_jensen_pct", "up_capture_pct", "down_capture_pct", "growth_of_1000",
]
DIST_BIN_EDGES = [-15, -10, -5, -2.5, 0, 2.5, 5, 10, 15, 20, 30, 60]

META_DEFINITIONS = {
    "total_growth_pct": "prod(1+r) - 1, in percent.",
    "annualized_return_pct": "geometric: (1+total_growth)^(12/n) - 1.",
    "annualized_std_dev": "POPULATION std (ddof=0) of monthly returns x sqrt(12), as a decimal. "
                          "The factsheet's four windows round to the population figure; the sample "
                          "(ddof=1) figure is off by 0.001-0.006 and is reported under alt_definitions.",
    "max_drawdown_pct": "minimum of index/running-peak - 1 on the monthly cumulative index; the running "
                        "peak includes the level at the start of the window (=1.0).",
    "sharpe": "mean(monthly excess over cash) x 12 / (population std of monthly excess x sqrt(12)), "
              "cash = TB3MS_pct/100/12 (factsheet footnote). Sample-std and raw-return-std variants "
              "are in alt_definitions; the population-std-of-excess form is used because it matches the "
              "table's own std-dev convention and reconciles all eight Sharpes within 0.011.",
    "sortino": "annualised geometric return / (sqrt(mean(min(r,0)^2)) x sqrt(12)). Target = 0 and no "
               "cash term. This is the only form that reproduces the stated Sortinos (all eight within "
               "0.003); the textbook excess-return form gives values 15-40% lower (alt_definitions).",
    "calmar": "annualised return / |max drawdown|.",
    "beta_to_spy": "cov(r, spy) / var(spy) on monthly returns (population moments; ddof cancels).",
    "correlation_to_spy": "Pearson correlation of monthly returns.",
    "alpha_ann_jensen_pct": "(mean(r) - beta x mean(spy)) x 12 = OLS intercept x 12, i.e. Jensen alpha "
                            "with the cash term dropped. Matches the table within 0.01pp; the textbook "
                            "form (mean(r-cash) - beta x mean(spy-cash)) x 12 is 0.4-1.1pp lower and is "
                            "reported under alt_definitions.",
    "up_capture_pct": "[(prod(1+r_up))^(12/n_up) - 1] / [(prod(1+spy_up))^(12/n_up) - 1] x 100 over "
                      "SPY-up months (annualised compounded capture). Geometric-mean and arithmetic-mean "
                      "captures (alt_definitions) miss the table by 1-13pp.",
    "down_capture_pct": "same as up capture over SPY-down months.",
    "growth_of_1000": "1000 x prod(1+r).",
    "pct_positive_months": "share of months with r > 0, in percent.",
    "cash": "monthly cash return = TB3MS_pct/100/12 with TB3MS_pct the calendar-month mean of the daily "
            "3-month T-bill rate (see meta.tb3ms_source).",
    "drawdown_episode": "peak = month-end at which the high-water mark was set (a month before the "
                        "window start denotes the starting level); trough = lowest month-end; recovery = "
                        "first month-end back at/above the peak, null if not yet recovered; "
                        "length_months = peak to recovery (or to the last month if unrecovered).",
    "distribution_bins": "left-closed, right-open intervals [a,b) over DIST_BIN_EDGES; the last bin "
                         "is closed on both sides (numpy.histogram convention).",
}


# --------------------------------------------------------------------------- helpers
def prev_month(ym):
    p = pd.Period(ym, freq="M") - 1
    return p.strftime("%Y-%m")


def total_growth(r):
    return float(np.prod(1.0 + r) - 1.0)


def annualized(r):
    return float((1.0 + total_growth(r)) ** (12.0 / len(r)) - 1.0)


def ann_std(r, ddof=STD_DDOF):
    return float(np.std(r, ddof=ddof) * SQ12) if len(r) > ddof else float("nan")


def cum_index(r):
    """Cumulative index with the starting level 1.0 prepended."""
    return np.concatenate([[1.0], np.cumprod(1.0 + r)])


def drawdown_series(r):
    idx = cum_index(r)
    dd = idx / np.maximum.accumulate(idx) - 1.0
    return dd[1:]


def max_drawdown(r):
    return float(drawdown_series(r).min())


def sharpe(r, cash, ddof=STD_DDOF, std_of="excess"):
    ex = r - cash
    sd = np.std(ex if std_of == "excess" else r, ddof=ddof)
    return float(ex.mean() * 12.0 / (sd * SQ12)) if sd > 0 else float("nan")


def sortino(r):
    """Factsheet form: annualised geometric return over annualised downside RMS about zero."""
    dn = math.sqrt(np.mean(np.minimum(r, 0.0) ** 2))
    return float(annualized(r) / (dn * SQ12)) if dn > 0 else float("nan")


def sortino_textbook(r, cash):
    ex = r - cash
    dn = math.sqrt(np.mean(np.minimum(ex, 0.0) ** 2))
    return float(ex.mean() * 12.0 / (dn * SQ12)) if dn > 0 else float("nan")


def beta(r, m):
    v = np.var(m)
    return float(np.cov(r, m, ddof=0)[0, 1] / v) if v > 0 else float("nan")


def corr(r, m):
    if np.std(r) == 0 or np.std(m) == 0:
        return float("nan")
    return float(np.corrcoef(r, m)[0, 1])


def jensen_alpha(r, m):
    return float((r.mean() - beta(r, m) * m.mean()) * 12.0)


def jensen_alpha_with_rf(r, m, cash):
    return float(((r - cash).mean() - beta(r, m) * (m - cash).mean()) * 12.0)


def capture(r, m, up=True, method="annualized"):
    mask = m > 0 if up else m < 0
    if mask.sum() == 0:
        return float("nan")
    rs, ms = r[mask], m[mask]
    if method == "annualized":
        a, b = annualized(rs), annualized(ms)
    elif method == "geomean":
        a, b = np.prod(1 + rs) ** (1 / len(rs)) - 1, np.prod(1 + ms) ** (1 / len(ms)) - 1
    elif method == "arithmetic":
        a, b = rs.mean(), ms.mean()
    else:  # compounded total
        a, b = total_growth(rs), total_growth(ms)
    return float(a / b * 100.0) if b != 0 else float("nan")


def longest_streak(r, positive=True):
    best = run = 0
    for x in r:
        hit = x > 0 if positive else x < 0
        run = run + 1 if hit else 0
        best = max(best, run)
    return int(best)


def drawdown_episodes(months, r):
    """Every peak-to-recovery episode, sorted deepest first."""
    idx = cum_index(r)
    labels = [prev_month(months[0])] + list(months)
    episodes, peak_i, trough_i, in_dd = [], 0, 0, False
    for i in range(1, len(idx)):
        if idx[i] >= idx[peak_i]:
            if in_dd:
                episodes.append((peak_i, trough_i, i))
            peak_i, in_dd = i, False
        else:
            if not in_dd:
                in_dd, trough_i = True, i
            elif idx[i] < idx[trough_i]:
                trough_i = i
    if in_dd:
        episodes.append((peak_i, trough_i, None))
    out = []
    for p, t, rec in episodes:
        end_i = rec if rec is not None else len(idx) - 1
        out.append({
            "peak": labels[p],
            "trough": labels[t],
            "recovery": labels[rec] if rec is not None else None,
            "depth_pct": float((idx[t] / idx[p] - 1.0) * 100.0),
            "length_months": int(end_i - p),
            "recovery_months": int(rec - t) if rec is not None else None,
            "recovered": rec is not None,
        })
    out.sort(key=lambda e: e["depth_pct"])
    return out


def window_metrics(months, r, m, cash):
    """The M block of the output contract for one series over one window."""
    n = len(r)
    tg, ann, mdd = total_growth(r), annualized(r), max_drawdown(r)
    ups, dns = r[r > 0], r[r < 0]
    eps = drawdown_episodes(months, r)
    worst = eps[0] if eps else None
    return {
        "total_growth_pct": tg * 100,
        "annualized_return_pct": ann * 100,
        "annualized_std_dev": ann_std(r),
        "max_drawdown_pct": mdd * 100,
        "pct_positive_months": float((r > 0).mean() * 100),
        "sharpe": sharpe(r, cash),
        "sortino": sortino(r),
        "calmar": float(ann / abs(mdd)) if mdd < 0 else float("nan"),
        "correlation_to_spy": corr(r, m),
        "beta_to_spy": beta(r, m),
        "alpha_ann_jensen_pct": jensen_alpha(r, m) * 100,
        "up_capture_pct": capture(r, m, up=True),
        "down_capture_pct": capture(r, m, up=False),
        "growth_of_1000": 1000.0 * (1.0 + tg),
        "best_month_pct": float(r.max() * 100),
        "worst_month_pct": float(r.min() * 100),
        "avg_month_pct": float(r.mean() * 100),
        "median_month_pct": float(np.median(r) * 100),
        "avg_up_month_pct": float(ups.mean() * 100) if len(ups) else None,
        "avg_down_month_pct": float(dns.mean() * 100) if len(dns) else None,
        "n_up_months": int((r > 0).sum()),
        "n_down_months": int((r < 0).sum()),
        "n_months": int(n),
        "longest_drawdown_months": max((e["length_months"] for e in eps), default=0),
        "max_dd_peak": worst["peak"] if worst else None,
        "max_dd_trough": worst["trough"] if worst else None,
        "max_dd_recovery": worst["recovery"] if worst else None,
        "avg_cash_rate_pct": float(cash.mean() * 12 * 100),
        "alt_definitions": {
            "annualized_std_dev_sample": ann_std(r, ddof=1),
            "sharpe_sample_std_of_excess": sharpe(r, cash, ddof=1),
            "sharpe_pop_std_of_returns": sharpe(r, cash, ddof=0, std_of="returns"),
            "sharpe_cash_zero": sharpe(r, np.zeros_like(r)),
            "sortino_textbook_excess": sortino_textbook(r, cash),
            "alpha_ann_jensen_with_rf_pct": jensen_alpha_with_rf(r, m, cash) * 100,
            "up_capture_geomean_pct": capture(r, m, True, "geomean"),
            "down_capture_geomean_pct": capture(r, m, False, "geomean"),
            "up_capture_arithmetic_pct": capture(r, m, True, "arithmetic"),
            "down_capture_arithmetic_pct": capture(r, m, False, "arithmetic"),
            "up_capture_total_compounded_pct": capture(r, m, True, "total"),
            "down_capture_total_compounded_pct": capture(r, m, False, "total"),
        },
    }


def rolling(values, window, fn):
    out = [None] * len(values)
    for i in range(window - 1, len(values)):
        out[i] = fn(slice(i - window + 1, i + 1))
    return out


def clean(o):
    """JSON-safe: numpy -> python, NaN/inf -> null, floats rounded to 6 dp."""
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple, np.ndarray)):
        return [clean(v) for v in o]
    if isinstance(o, (bool, np.bool_)):
        return bool(o)
    if isinstance(o, (int, np.integer)):
        return int(o)
    if isinstance(o, (float, np.floating)):
        f = float(o)
        return round(f, 6) if math.isfinite(f) else None
    return o


# --------------------------------------------------------------------------- T-bill proxy
def build_tb3ms(months):
    raw = pd.read_csv(RAW_RFR_CSV, usecols=["Date", "Risk Free Rate"])
    raw["Date"] = pd.to_datetime(raw["Date"])
    raw = raw[raw["Date"] >= "2012-01-01"].dropna(subset=["Risk Free Rate"])
    raw["month"] = raw["Date"].dt.strftime("%Y-%m")
    grp = raw.groupby("month")["Risk Free Rate"].agg(["mean", "count"])
    last_day = raw["Date"].max()
    last_month = last_day.strftime("%Y-%m")
    src_name = os.path.relpath(RAW_RFR_CSV, HERE)

    rows, last_val = [], None
    for ym in months:
        if ym in grp.index:
            last_val = round(float(grp.loc[ym, "mean"]), 4)
            note = f"calendar-month mean of {int(grp.loc[ym, 'count'])} daily observations"
            if ym == last_month and last_day.day < 28:
                note += f"; partial month (daily data end {last_day.date()})"
            rows.append((ym, last_val, "derived", note))
        else:
            rows.append((ym, last_val, "held_flat",
                         f"held_flat: no daily data after {last_day.date()}; {last_month} value carried forward"))
    tb = pd.DataFrame(rows, columns=["month", "tb3ms_pct", "source", "note"])
    tb.to_csv(TB3MS_CSV, index=False)
    meta = {
        "tb3ms_source": f"{src_name}: 'Risk Free Rate' (3-month T-bill, percent, daily) averaged by "
                        f"calendar month as a proxy for FRED TB3MS (FRED not reachable).",
        "tb3ms_note": f"Daily data end {last_day.date()}; {int((tb.source == 'held_flat').sum())} months "
                      f"({tb.loc[tb.source == 'held_flat', 'month'].min()}..{tb.loc[tb.source == 'held_flat', 'month'].max()}) "
                      f"held flat at the {last_month} value of {last_val:.4f}%. Monthly cash return = tb3ms_pct/100/12.",
    }
    return tb, meta


# --------------------------------------------------------------------------- reconciliation
def tolerance_for(metric, stated):
    if metric == "annualized_std_dev":
        return 0.002
    if metric in ("sharpe", "sortino", "calmar"):
        return 0.02
    if metric in ("correlation_to_spy", "beta_to_spy"):
        return 0.01
    if metric in ("up_capture_pct", "down_capture_pct"):
        return 1.0
    if metric == "growth_of_1000":
        return max(3.0, 0.002 * abs(stated))
    if metric == "total_growth_pct" and abs(stated) > 1000:
        return 0.30
    return 0.05


def implied_cash_note(r, cash, stated_sharpe):
    """How far the factsheet's T-bill average would have to sit from ours to hit the stated Sharpe."""
    ex = r - cash
    sd = np.std(ex, ddof=STD_DDOF)
    implied_ex_mean = stated_sharpe * sd * SQ12 / 12.0
    implied_rf = (r.mean() - implied_ex_mean) * 12 * 100
    ours = cash.mean() * 12 * 100
    return (f"stated Sharpe implies an average T-bill of {implied_rf:.2f}% vs {ours:.2f}% in our TB3MS proxy "
            f"({implied_rf - ours:+.2f}pp); the factsheet's FRED TB3MS series runs a few bp above our daily-average proxy")


def reconcile(df, stated, windows_out, ytd_computed):
    checks = []
    for wname, (a, b) in STATED_WINDOWS.items():
        g = df[(df.date >= a) & (df.date <= b)]
        cash = g.cash.values
        table = stated["statistics"][wname]
        for si, series in enumerate(["strategy", "spy"]):
            r = g[series].values / 100.0
            comp_block = windows_out[wname][series]
            for metric in STATED_METRICS:
                st_val = table[metric][si]
                if st_val is None:
                    continue
                comp = comp_block[metric]
                diff = comp - st_val if comp is not None and math.isfinite(comp) else None
                tol = tolerance_for(metric, st_val)
                ok = diff is not None and abs(diff) <= tol + 1e-9
                note = ""
                if metric == "sharpe":
                    note = "pop-std of monthly excess over TB3MS proxy; " + implied_cash_note(r, cash, st_val)
                elif metric == "sortino":
                    note = "factsheet form: annualised geometric return / (RMS(min(r,0)) x sqrt(12)), no cash term"
                elif metric == "alpha_ann_jensen_pct":
                    note = "OLS intercept x 12 (cash term dropped)"
                elif metric in ("up_capture_pct", "down_capture_pct"):
                    note = "annualised compounded capture"
                elif metric == "annualized_std_dev":
                    note = "population std (ddof=0)"
                if not ok:
                    if metric in ("total_growth_pct", "growth_of_1000", "annualized_return_pct"):
                        rel = abs(diff) / abs(st_val) * 100 if st_val else float("nan")
                        note = (f"{note + '; ' if note else ''}transcribed monthlies are rounded to 2 dp; compounding "
                                f"{len(r)} rounded months drifts the total by ~{abs(diff):.2f} ({rel:.3f}% relative), "
                                f"beyond the fixed tolerance; every underlying calendar-year YTD reconciles within 0.03pp")
                    elif metric == "sharpe":
                        note += "; residual due to T-bill series difference"
                checks.append({"window": wname, "series": series, "metric": metric, "stated": st_val,
                               "computed": comp, "diff": diff, "tolerance": tol, "ok": bool(ok), "note": note})
    # stated YTD / period figures
    for series, table in stated["period_ytd_stated"].items():
        for key, st_val in table.items():
            comp = ytd_computed[series][key]
            diff = comp - st_val
            ok = abs(diff) <= 0.03 + 1e-9
            checks.append({"window": key, "series": series, "metric": "period_return_pct", "stated": st_val,
                           "computed": comp, "diff": diff, "tolerance": 0.03, "ok": bool(ok),
                           "note": "" if ok else "compounded from 2-dp transcribed monthlies"})
    return checks


# --------------------------------------------------------------------------- main build
def main():
    df = pd.read_csv(RETURNS_CSV)
    df = df.sort_values("date").reset_index(drop=True)
    assert len(df) == 168 and df.date.iloc[0] == "2012-07" and df.date.iloc[-1] == "2026-06"
    with open(STATED_JSON) as fh:
        stated = json.load(fh)

    months = list(df.date)
    tb, tb_meta = build_tb3ms(months)
    df["tb3ms_pct"] = tb.tb3ms_pct.values
    df["cash"] = df.tb3ms_pct / 100.0 / 12.0

    S = df.strategy.values / 100.0
    M = df.spy.values / 100.0
    C = df.cash.values
    n = len(df)

    # ---- series -----------------------------------------------------------------------
    def r12(arr):
        return rolling(arr, 12, lambda sl: total_growth(arr[sl]) * 100)

    roll12_s, roll12_m = r12(S), r12(M)
    series = {
        "months": months,
        "period": list(df.period),
        "strategy": list(df.strategy),
        "spy": list(df.spy),
        "tb3ms_pct": list(df.tb3ms_pct),
        "tb3ms_source": list(tb.source),
        "excess_vs_spy": list(df.strategy - df.spy),
        "growth_strategy": list(1000.0 * np.cumprod(1 + S)),
        "growth_spy": list(1000.0 * np.cumprod(1 + M)),
        "dd_strategy": list(drawdown_series(S) * 100),
        "dd_spy": list(drawdown_series(M) * 100),
        "rolling12_strategy": roll12_s,
        "rolling12_spy": roll12_m,
        "rolling12_excess": [None if a is None else a - b for a, b in zip(roll12_s, roll12_m)],
        "rolling36_sharpe_strategy": rolling(S, 36, lambda sl: sharpe(S[sl], C[sl])),
        "rolling36_sharpe_spy": rolling(M, 36, lambda sl: sharpe(M[sl], C[sl])),
        "rolling36_beta": rolling(S, 36, lambda sl: beta(S[sl], M[sl])),
        "rolling36_corr": rolling(S, 36, lambda sl: corr(S[sl], M[sl])),
        "rolling36_up_capture": rolling(S, 36, lambda sl: capture(S[sl], M[sl], True)),
        "rolling36_down_capture": rolling(S, 36, lambda sl: capture(S[sl], M[sl], False)),
        "rolling36_ann_strategy": rolling(S, 36, lambda sl: annualized(S[sl]) * 100),
        "rolling36_ann_spy": rolling(M, 36, lambda sl: annualized(M[sl]) * 100),
        "rolling60_ann_strategy": rolling(S, 60, lambda sl: annualized(S[sl]) * 100),
        "rolling60_ann_spy": rolling(M, 60, lambda sl: annualized(M[sl]) * 100),
    }

    # ---- windows ----------------------------------------------------------------------
    windows = {}
    for wname, (a, b) in {**STATED_WINDOWS, **EXTRA_WINDOWS}.items():
        mask = (df.date >= a) & (df.date <= b)
        g = df[mask]
        ws, wm, wc = g.strategy.values / 100, g.spy.values / 100, g.cash.values
        wmonths = list(g.date)
        W = {"start": a, "end": b, "n_months": int(len(g)),
             "strategy": window_metrics(wmonths, ws, wm, wc),
             "spy": window_metrics(wmonths, wm, wm, wc)}
        if wname in STATED_WINDOWS:
            tbl = stated["statistics"][wname]
            W["sp500_price_stated"] = {m: tbl[m][2] for m in STATED_METRICS}
            W["sp500_price_stated"]["note"] = "stated only: S&P 500 price index, no monthly data available"
        windows[wname] = W

    # ---- calendar years / monthly table / period split ----------------------------------
    calendar_years, monthly_table = [], []
    ytd_computed = {"strategy": {}, "spy": {}}
    for year, g in df.groupby("year"):
        ys, ym = g.strategy.values / 100, g.spy.values / 100
        sy, my = total_growth(ys) * 100, total_growth(ym) * 100
        calendar_years.append({
            "year": int(year), "n_months": int(len(g)), "partial": bool(len(g) < 12),
            "strategy_pct": sy, "spy_pct": my, "excess_pct": sy - my,
            "strategy_best_month_pct": float(g.strategy.max()), "strategy_worst_month_pct": float(g.strategy.min()),
            "spy_best_month_pct": float(g.spy.max()), "spy_worst_month_pct": float(g.spy.min()),
            "strategy_pos_months": int((g.strategy > 0).sum()), "spy_pos_months": int((g.spy > 0).sum()),
            "months_strategy_beat_spy": int((g.strategy > g.spy).sum()),
        })
        by_month = g.set_index("month")
        monthly_table.append({
            "year": int(year),
            "strategy": [float(by_month.strategy[m]) if m in by_month.index else None for m in range(1, 13)],
            "spy": [float(by_month.spy[m]) if m in by_month.index else None for m in range(1, 13)],
            "strategy_ytd_pct": sy, "spy_ytd_pct": my,
        })
        # key matching stated_figures.period_ytd_stated: "2013", "2026_jan_jun", ... (2023 is split below)
        if year != 2023:
            mon = lambda ym: pd.Period(ym).strftime("%b").lower()
            key = str(year) if len(g) == 12 or year == df.year.iloc[0] else f"{year}_{mon(g.date.iloc[0])}_{mon(g.date.iloc[-1])}"
            ytd_computed["strategy"][key] = sy
            ytd_computed["spy"][key] = my

    def span(a, b, col):
        g = df[(df.date >= a) & (df.date <= b)]
        return total_growth(g[col].values / 100) * 100

    period_split = {
        "family_office": {"start": "2012-07", "end": "2023-07",
                          "strategy_2023_jan_jul_pct": span("2023-01", "2023-07", "strategy"),
                          "spy_2023_jan_jul_pct": span("2023-01", "2023-07", "spy")},
        "commingled_fund": {"start": "2023-08", "end": "2026-06",
                            "strategy_2023_aug_dec_pct": span("2023-08", "2023-12", "strategy"),
                            "spy_2023_aug_dec_pct": span("2023-08", "2023-12", "spy")},
    }
    for series_name in ("strategy", "spy"):
        ytd_computed[series_name]["2023_jan_jul"] = span("2023-01", "2023-07", series_name)
        ytd_computed[series_name]["2023_aug_dec"] = span("2023-08", "2023-12", series_name)
    # sanity: every stated period key must have a computed counterpart
    for series_name, table in stated["period_ytd_stated"].items():
        missing = set(table) - set(ytd_computed[series_name])
        assert not missing, f"no computed value for stated period(s) {missing}"

    # ---- distribution -----------------------------------------------------------------
    edges = np.array(DIST_BIN_EDGES, dtype=float)
    s_counts, _ = np.histogram(df.strategy.values, bins=edges)
    m_counts, _ = np.histogram(df.spy.values, bins=edges)
    assert s_counts.sum() == n and m_counts.sum() == n, "monthly returns fall outside the histogram edges"
    distribution = {
        "bin_edges": DIST_BIN_EDGES,
        "bin_labels": [f"[{edges[i]:g}, {edges[i+1]:g})" for i in range(len(edges) - 1)],
        "strategy_counts": s_counts.tolist(), "spy_counts": m_counts.tolist(),
        "strategy_pct_of_months": list(s_counts / n * 100), "spy_pct_of_months": list(m_counts / n * 100),
    }

    # ---- scatter, up/down, best/worst -------------------------------------------------
    scatter = [{"month": d, "spy": float(m_), "strategy": float(s_), "period": p}
               for d, m_, s_, p in zip(df.date, df.spy, df.strategy, df.period)]

    up, dn = df.spy > 0, df.spy < 0
    beat = df.strategy > df.spy
    up_down = {
        "n_spy_up_months": int(up.sum()), "n_spy_down_months": int(dn.sum()),
        "strategy_avg_in_spy_up_pct": float(df.strategy[up].mean()),
        "strategy_avg_in_spy_down_pct": float(df.strategy[dn].mean()),
        "spy_avg_in_up_pct": float(df.spy[up].mean()), "spy_avg_in_down_pct": float(df.spy[dn].mean()),
        "strategy_beat_spy_in_down_months_pct": float(beat[dn].mean() * 100),
        "strategy_beat_spy_in_up_months_pct": float(beat[up].mean() * 100),
        "months_strategy_beat_spy": int(beat.sum()), "months_strategy_beat_spy_pct": float(beat.mean() * 100),
        "strategy_positive_when_spy_down_pct": float((df.strategy[dn] > 0).mean() * 100),
        "strategy_positive_when_spy_down_n": int((df.strategy[dn] > 0).sum()),
        "spy_down_months_table": [{"month": r.date, "spy": float(r.spy), "strategy": float(r.strategy),
                                   "excess": float(r.strategy - r.spy)} for r in df[dn].itertuples()],
    }

    def top(col, ascending, k=10):
        g = df.sort_values([col, "date"], ascending=[ascending, True]).head(k)
        return [{"month": r.date, "strategy": float(r.strategy), "spy": float(r.spy)} for r in g.itertuples()]

    best_worst = {"strategy_worst_10": top("strategy", True), "strategy_best_10": top("strategy", False),
                  "spy_worst_10": top("spy", True), "spy_best_10": top("spy", False)}

    drawdowns = {"strategy": drawdown_episodes(months, S)[:5], "spy": drawdown_episodes(months, M)[:5]}
    streaks = {"strategy_longest_win_months": longest_streak(S, True),
               "strategy_longest_loss_months": longest_streak(S, False),
               "spy_longest_win_months": longest_streak(M, True),
               "spy_longest_loss_months": longest_streak(M, False)}

    # ---- rolling-window statistics ----------------------------------------------------
    def roll_stats(strat_vals, spy_vals):
        sv = np.array([v for v in strat_vals if v is not None])
        pairs = [(a, b) for a, b in zip(strat_vals, spy_vals) if a is not None]
        return {"n_windows": int(len(sv)), "min": float(sv.min()), "max": float(sv.max()),
                "mean": float(sv.mean()), "median": float(np.median(sv)),
                "pct_positive": float((sv > 0).mean() * 100),
                "pct_beating_spy": float(np.mean([a > b for a, b in pairs]) * 100)}

    annual_rolling = {
        "rolling_12m_strategy_stats": roll_stats(series["rolling12_strategy"], series["rolling12_spy"]),
        "rolling_36m_ann_strategy_stats": roll_stats(series["rolling36_ann_strategy"], series["rolling36_ann_spy"]),
        "rolling_60m_ann_strategy_stats": roll_stats(series["rolling60_ann_strategy"], series["rolling60_ann_spy"]),
    }

    # ---- quadrants (daily; stated only) -----------------------------------------------
    q = dict(stated["quadrants_daily"])
    qkeys = ["loss_avoidance_days", "gain_sacrifice_days", "amplified_gains_days", "amplified_losses_days"]
    qsum = sum(q[k] for k in qkeys)
    q.update({
        "sum_of_quadrant_days": int(qsum),
        "pct_shares_using_sum": {k: q[k] / qsum * 100 for k in qkeys},
        "pct_positive_days_using_stated_total": q["amplified_gains_days"] / q["stated_total_days"] * 100,
        "pct_positive_days_using_sum": q["amplified_gains_days"] / qsum * 100,
        "pct_cash_days_using_sum": (q["loss_avoidance_days"] + q["gain_sacrifice_days"]) / qsum * 100,
        "note": f"source total {q['stated_total_days']:,} days disagrees with the quadrant sum {qsum:,}; both preserved",
    })

    # ---- reconciliation ---------------------------------------------------------------
    checks = reconcile(df, stated, windows, ytd_computed)
    fails = [c for c in checks if not c["ok"]]
    summary = {"n_checks": len(checks), "n_ok": len(checks) - len(fails), "n_fail": len(fails), "fails": fails}

    out = {
        "meta": {
            "as_of": "2026-06", "inception": "2012-07", "n_months": int(n), "generated_by": "build_analytics.py",
            "strategy": "Demeter Tactical Investments - Dual-Engine Quantitative Equity Strategy, Share Class B",
            "benchmark": "SPY (SPDR S&P 500 ETF Trust, total return)",
            "periods": {"family_office": "2012-07..2023-07", "commingled_fund": "2023-08..2026-06"},
            "units": "percentages in percent units; ratios unitless; annualized_std_dev as an annualised decimal",
            "tb3ms_source": tb_meta["tb3ms_source"], "tb3ms_note": tb_meta["tb3ms_note"],
            "definitions": META_DEFINITIONS,
            "sp500_price_note": "the factsheet's third column (S&P 500 price index) is carried as stated-only; "
                                "no monthly data are available for it",
        },
        "series": series, "windows": windows, "calendar_years": calendar_years, "monthly_table": monthly_table,
        "period_split": period_split, "distribution": distribution, "scatter": scatter,
        "up_down_analysis": up_down, "best_worst": best_worst, "drawdowns": drawdowns, "streaks": streaks,
        "annual_rolling": annual_rolling, "quadrants": q, "reconciliation": checks, "reconciliation_summary": summary,
    }
    out = clean(out)
    text = json.dumps(out, indent=1, allow_nan=False)
    json.loads(text)  # round-trip validation (allow_nan=False already rejects NaN/Infinity)
    with open(OUT_JSON, "w") as fh:
        fh.write(text + "\n")

    print(f"wrote {os.path.relpath(OUT_JSON, HERE)} and {os.path.relpath(TB3MS_CSV, HERE)}")
    print(f"reconciliation: {summary['n_ok']}/{summary['n_checks']} ok, {summary['n_fail']} fail")
    for c in fails:
        print(f"  FAIL {c['window']:16s} {c['series']:8s} {c['metric']:22s} stated {c['stated']:>10} "
              f"computed {c['computed']:>12.4f} diff {c['diff']:+.4f} tol {c['tolerance']}")


if __name__ == "__main__":
    main()
