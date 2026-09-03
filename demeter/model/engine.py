"""Dual-engine (levered long / cash) daily backtest engine.

Conventions
-----------
* One row per NYSE trading day, loaded from data/market_daily.csv.
* A *signal* is a function  f(df, **params) -> pd.Series  of target leverage L_t in [0, max_lev],
  indexed like df, computed using ONLY information available at the close of day t
  (rolling / shifted / expanding computations; never centered windows or full-sample statistics).
  This mirrors Demeter's 3:59 PM daily rebalance: the position chosen at the close of day t earns day t+1.
* Portfolio return:   r_p[t+1] = rf_daily[t+1] + L_t * x[t+1] - lev_fin[t+1] - cost[t+1]
      x = asset excess return over cash:
          asset='spx_tr' -> spx_tr_ret - rf_daily          (S&P 500 total return, synthetic futures; 1885-2026-02)
          asset='es'     -> es_ret                          (S&P 500 futures, back-adjusted; 1982-09..2024-03)
          asset='nq'     -> nq_ret                          (NASDAQ-100 futures, back-adjusted; 1999-12..2024-03)
      lev_fin = max(L_t - 1, 0) * financing_spread_bps/1e4/252   (extra financing over T-bill on the levered notional)
      cost    = |L_t - L_{t-1}| * cost_bps/1e4                    (commission + slippage per unit notional traded)
* Cash engine (L=0) earns the 3-month T-bill rate.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "market_daily.csv"
DEMETER_CSV = HERE.parent / "data" / "monthly_returns.csv"
MAX_LEV_DEFAULT = 3.0
TRADING_DAYS = 252


# ----------------------------------------------------------------------------- data
def load_market(path: Path | str = DATA, start=None, end=None) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"]).set_index("date").sort_index()
    if start is not None:
        df = df.loc[pd.Timestamp(start):]
    if end is not None:
        df = df.loc[:pd.Timestamp(end)]
    return df


def asset_excess(df: pd.DataFrame, asset: str) -> pd.Series:
    if asset == "spx_tr":
        return df["spx_tr_ret"] - df["rf_daily"]
    if asset == "es":
        return df["es_ret"]
    if asset == "nq":
        return df["nq_ret"]
    raise ValueError(f"unknown asset {asset!r}; use 'spx_tr', 'es' or 'nq'")


# ----------------------------------------------------------------------------- core
@dataclass
class Result:
    daily: pd.DataFrame            # index=date; columns: lev (position in effect that day), x, rf, ret, equity, mkt_tr_ret, cost
    asset: str
    cost_bps: float
    financing_spread_bps: float
    params: dict = field(default_factory=dict)
    name: str = "model"

    # --- convenience
    @property
    def ret(self) -> pd.Series:
        return self.daily["ret"]

    def monthly(self) -> pd.Series:
        return to_monthly(self.daily["ret"])

    def window(self, start=None, end=None) -> "Result":
        d = self.daily.loc[pd.Timestamp(start) if start else None: pd.Timestamp(end) if end else None].copy()
        d["equity"] = (1 + d["ret"]).cumprod()
        return Result(d, self.asset, self.cost_bps, self.financing_spread_bps, self.params, self.name)

    def metrics(self) -> dict:
        return metrics(self.daily)

    def compare_to_demeter(self, start="2012-07-01", end=None) -> dict:
        return compare_to_demeter(self, start=start, end=end)


def run(df: pd.DataFrame, lev: pd.Series, asset: str = "spx_tr", cost_bps: float = 2.0,
        financing_spread_bps: float = 0.0, max_lev: float = MAX_LEV_DEFAULT,
        start=None, end=None, name: str = "model", params: dict | None = None) -> Result:
    """Run the dual-engine backtest.  `lev` is the TARGET leverage decided at each close (see module doc)."""
    lev = lev.reindex(df.index).astype(float).clip(lower=0.0, upper=max_lev)
    x = asset_excess(df, asset)
    rf = df["rf_daily"]
    pos = lev.shift(1)                      # position in effect during day t (decided at close t-1)
    pos_prev = lev.shift(2)
    trade = (pos - pos_prev).abs()
    valid = x.notna() & pos.notna()
    d = pd.DataFrame(index=df.index)
    d["lev"] = pos
    d["x"] = x
    d["rf"] = rf
    d["mkt_tr_ret"] = df["spx_tr_ret"] if asset != "nq" else df["nq_ret"] + rf
    d["cost"] = trade.fillna(0.0) * cost_bps / 1e4
    d["lev_fin"] = (pos - 1.0).clip(lower=0.0).fillna(0.0) * financing_spread_bps / 1e4 / TRADING_DAYS
    d["ret"] = rf + pos * x - d["lev_fin"] - d["cost"]
    d = d[valid]
    if start is not None:
        d = d.loc[pd.Timestamp(start):]
    if end is not None:
        d = d.loc[:pd.Timestamp(end)]
    d = d.dropna(subset=["ret"])
    d["equity"] = (1 + d["ret"]).cumprod()
    return Result(d, asset, cost_bps, financing_spread_bps, params or {}, name)


# ----------------------------------------------------------------------------- statistics
def to_monthly(r: pd.Series) -> pd.Series:
    return (1 + r).resample("ME").prod() - 1


def drawdown(equity: pd.Series) -> pd.Series:
    return equity / equity.cummax() - 1


def monthly_stats(m: pd.Series, mkt_m: pd.Series | None = None, rf_m: pd.Series | None = None) -> dict:
    """Statistics from MONTHLY returns (decimal). Mirrors the Demeter factsheet definitions:
    Sharpe = mean(monthly excess over TB3MS) * 12 / (std(monthly excess) * sqrt(12)); std dev annualised from monthly."""
    m = m.dropna()
    n = len(m)
    if n == 0:
        return {}
    eq = (1 + m).cumprod()
    total = eq.iloc[-1] - 1
    yrs = n / 12.0
    cagr = eq.iloc[-1] ** (1 / yrs) - 1
    out = {
        "start": str(m.index[0].strftime("%Y-%m")), "end": str(m.index[-1].strftime("%Y-%m")), "n_months": n,
        "total_growth_pct": total * 100, "annualized_return_pct": cagr * 100,
        "annualized_std_dev": m.std(ddof=1) * np.sqrt(12),
        "max_drawdown_pct": drawdown(eq).min() * 100,
        "pct_positive_months": (m > 0).mean() * 100,
        "best_month_pct": m.max() * 100, "worst_month_pct": m.min() * 100,
        "avg_month_pct": m.mean() * 100, "median_month_pct": m.median() * 100,
        "growth_of_1000": eq.iloc[-1] * 1000,
        "calmar": (cagr / abs(drawdown(eq).min())) if drawdown(eq).min() < 0 else np.nan,
    }
    if rf_m is not None:
        rf_m = rf_m.reindex(m.index).fillna(0.0)
        ex = m - rf_m
        sd = ex.std(ddof=1)
        out["sharpe"] = ex.mean() * 12 / (sd * np.sqrt(12)) if sd > 0 else np.nan
        dn = np.sqrt(np.mean(np.minimum(ex, 0.0) ** 2)) * np.sqrt(12)
        out["sortino"] = ex.mean() * 12 / dn if dn > 0 else np.nan
    if mkt_m is not None:
        b = mkt_m.reindex(m.index)
        ok = b.notna()
        mm, bb = m[ok], b[ok]
        var = bb.var(ddof=1)
        beta = mm.cov(bb) / var if var > 0 else np.nan
        out["beta_to_spy"] = beta
        out["correlation_to_spy"] = mm.corr(bb)
        if rf_m is not None:
            rfx = rf_m.reindex(mm.index).fillna(0.0)
            out["alpha_ann_jensen_pct"] = ((mm - rfx).mean() - beta * (bb - rfx).mean()) * 12 * 100
        up, dn_ = bb > 0, bb < 0
        def geo(s):
            return (np.prod(1 + s) ** (1 / len(s)) - 1) if len(s) else np.nan
        out["up_capture_pct"] = geo(mm[up]) / geo(bb[up]) * 100 if up.sum() else np.nan
        out["down_capture_pct"] = geo(mm[dn_]) / geo(bb[dn_]) * 100 if dn_.sum() else np.nan
        out["n_spy_up_months"] = int(up.sum()); out["n_spy_down_months"] = int(dn_.sum())
        out["avg_in_spy_up_months_pct"] = mm[up].mean() * 100 if up.sum() else np.nan
        out["avg_in_spy_down_months_pct"] = mm[dn_].mean() * 100 if dn_.sum() else np.nan
        out["beat_spy_in_down_months_pct"] = (mm[dn_] > bb[dn_]).mean() * 100 if dn_.sum() else np.nan
        out["months_beat_spy_pct"] = (mm > bb).mean() * 100
    return out


def metrics(d: pd.DataFrame) -> dict:
    """Full metric set for a daily result frame (see Result.daily)."""
    r = d["ret"]
    if len(r) == 0:
        return {}
    m = to_monthly(r)
    mkt_m = to_monthly(d["mkt_tr_ret"])
    rf_m = to_monthly(d["rf"])
    out = monthly_stats(m, mkt_m, rf_m)
    eq = (1 + r).cumprod()
    out["start_date"] = str(r.index[0].date()); out["end_date"] = str(r.index[-1].date())
    out["n_days"] = int(len(r))
    out["daily_ann_vol"] = r.std(ddof=1) * np.sqrt(TRADING_DAYS)
    out["max_drawdown_daily_pct"] = drawdown(eq).min() * 100
    lev = d["lev"]
    out["pct_days_cash"] = (lev == 0).mean() * 100
    out["pct_days_invested"] = (lev > 0).mean() * 100
    out["pct_days_levered_gt1"] = (lev > 1.0).mean() * 100
    out["avg_leverage"] = lev.mean()
    out["avg_leverage_when_invested"] = lev[lev > 0].mean() if (lev > 0).any() else 0.0
    ch = lev.diff().fillna(0.0)
    yrs = len(r) / TRADING_DAYS
    out["n_position_changes"] = int((ch != 0).sum())
    out["n_entries_from_cash"] = int(((lev > 0) & (lev.shift(1) == 0)).sum())
    out["position_changes_per_year"] = (ch != 0).sum() / yrs
    out["turnover_notional_per_year"] = ch.abs().sum() / yrs
    out["total_cost_drag_pct_annual"] = d["cost"].mean() * TRADING_DAYS * 100
    holding = _run_lengths(lev > 0)
    out["avg_invested_spell_days"] = float(np.mean(holding)) if holding else 0.0
    out["median_invested_spell_days"] = float(np.median(holding)) if holding else 0.0
    q = quadrants(d)
    out.update({f"quad_{k}": v for k, v in q.items()})
    out["pct_days_positive_return"] = (r > 0).mean() * 100
    # market (buy-and-hold 1x) for reference
    bm = monthly_stats(mkt_m, mkt_m, rf_m)
    out["spy_annualized_return_pct"] = bm.get("annualized_return_pct")
    out["spy_max_drawdown_pct"] = bm.get("max_drawdown_pct")
    out["spy_sharpe"] = bm.get("sharpe")
    out["spy_annualized_std_dev"] = bm.get("annualized_std_dev")
    return out


def _run_lengths(mask: pd.Series) -> list:
    runs, cur = [], 0
    for v in mask.values:
        if v:
            cur += 1
        elif cur:
            runs.append(cur); cur = 0
    if cur:
        runs.append(cur)
    return runs


def quadrants(d: pd.DataFrame) -> dict:
    """Demeter's four daily scenarios, using the position in effect that day and the asset's excess return."""
    lev, x = d["lev"], d["x"]
    inv = lev > 0
    up, dn = x > 0, x < 0
    n = int(len(d))
    out = {
        "days": n,
        "loss_avoidance_days": int((~inv & dn).sum()), "gain_sacrifice_days": int((~inv & up).sum()),
        "amplified_gains_days": int((inv & up).sum()), "amplified_losses_days": int((inv & dn).sum()),
    }
    for k in list(out):
        if k.endswith("_days") and k != "days":
            out[k.replace("_days", "_pct")] = out[k] / n * 100 if n else np.nan
    return out


# ----------------------------------------------------------------------------- Demeter comparison
def load_demeter(path: Path | str = DEMETER_CSV) -> pd.DataFrame:
    dem = pd.read_csv(path)
    dem["date"] = pd.to_datetime(dem["date"]) + pd.offsets.MonthEnd(0)
    dem = dem.set_index("date")
    return dem[["strategy", "spy", "period"]]


def compare_to_demeter(res: Result, start="2012-07-01", end=None, demeter_path: Path | str = DEMETER_CSV) -> dict:
    dem = load_demeter(demeter_path)
    d = res.daily.loc[pd.Timestamp(start):(pd.Timestamp(end) if end else None)]
    # only keep FULL months of model data
    m = to_monthly(d["ret"])
    counts = d["ret"].resample("ME").count()
    full = counts >= 15
    m = m[full]
    mkt_m = to_monthly(d["mkt_tr_ret"])[full]
    rf_m = to_monthly(d["rf"])[full]
    dem_s = dem["strategy"].reindex(m.index) / 100
    dem_spy = dem["spy"].reindex(m.index) / 100
    ok = dem_s.notna()
    m, mkt_m, rf_m, dem_s, dem_spy = m[ok], mkt_m[ok], rf_m[ok], dem_s[ok], dem_spy[ok]
    out = {
        "window": {"start": str(m.index[0].strftime("%Y-%m")), "end": str(m.index[-1].strftime("%Y-%m")), "n_months": int(len(m))},
        "model": monthly_stats(m, mkt_m, rf_m),
        "demeter": monthly_stats(dem_s, dem_spy, rf_m),
        "spy_model_data": monthly_stats(mkt_m, mkt_m, rf_m),
        "spy_demeter_data": monthly_stats(dem_spy, dem_spy, rf_m),
        "monthly_corr_model_vs_demeter": float(m.corr(dem_s)),
        "monthly_rmse_pct": float(np.sqrt(np.mean((m - dem_s) ** 2)) * 100),
        "months_model_beats_demeter_pct": float((m > dem_s).mean() * 100),
        "same_sign_months_pct": float((np.sign(m) == np.sign(dem_s)).mean() * 100),
        "yearly": [],
        "monthly": [{"month": i.strftime("%Y-%m"), "model": float(a * 100), "demeter": float(b * 100), "spy": float(c * 100)}
                    for i, a, b, c in zip(m.index, m.values, dem_s.values, dem_spy.values)],
    }
    for y, g in pd.DataFrame({"model": m, "demeter": dem_s, "spy": dem_spy}).groupby(m.index.year):
        out["yearly"].append({"year": int(y), "n_months": int(len(g)),
                              "model": float((np.prod(1 + g.model) - 1) * 100),
                              "demeter": float((np.prod(1 + g.demeter) - 1) * 100),
                              "spy": float((np.prod(1 + g.spy) - 1) * 100)})
    return out


# ----------------------------------------------------------------------------- robustness helpers
def lookahead_check(signal_fn, df: pd.DataFrame, params: dict | None = None,
                    cutoffs=("2008-06-30", "2015-12-31", "2020-03-31", "2023-06-30"), atol=1e-9) -> dict:
    """Recompute the signal on data truncated at each cutoff; the pre-cutoff signal must be unchanged."""
    params = params or {}
    full = signal_fn(df, **params).reindex(df.index)
    worst, details = 0.0, []
    for c in cutoffs:
        c = pd.Timestamp(c)
        if c <= df.index[0] or c >= df.index[-1]:
            continue
        trunc = signal_fn(df.loc[:c], **params).reindex(df.loc[:c].index)
        a, b = full.loc[:c].astype(float), trunc.astype(float)
        both_nan = a.isna() & b.isna()
        diff = (a - b).abs().where(~both_nan, 0.0)
        nan_mismatch = int((a.isna() ^ b.isna()).sum())
        md = float(np.nanmax(diff.values)) if len(diff) else 0.0
        worst = max(worst, md)
        details.append({"cutoff": str(c.date()), "max_abs_diff": md, "nan_mismatches": nan_mismatch})
    ok = worst <= atol and all(x["nan_mismatches"] == 0 for x in details)
    return {"ok": bool(ok), "max_abs_diff": worst, "details": details}


def param_sensitivity(signal_fn, df: pd.DataFrame, base: dict, asset="spx_tr", cost_bps=2.0,
                      start=None, end=None, rel_steps=(-0.3, -0.15, 0.15, 0.3), keys=None) -> list:
    """Perturb each numeric parameter by the relative steps; report CAGR / Sharpe / maxDD / trades."""
    rows = []
    keys = keys or [k for k, v in base.items() if isinstance(v, (int, float)) and not isinstance(v, bool)]
    def one(p, label):
        r = run(df, signal_fn(df, **p), asset=asset, cost_bps=cost_bps, start=start, end=end)
        mt = r.metrics()
        return {"variant": label, "params": p, "cagr_pct": mt.get("annualized_return_pct"), "sharpe": mt.get("sharpe"),
                "max_dd_pct": mt.get("max_drawdown_pct"), "changes_per_year": mt.get("position_changes_per_year")}
    rows.append(one(dict(base), "base"))
    for k in keys:
        for s in rel_steps:
            p = dict(base)
            v = base[k] * (1 + s)
            p[k] = int(round(v)) if isinstance(base[k], int) else v
            if p[k] == base[k]:
                continue
            rows.append(one(p, f"{k}{s:+.0%}"))
    return rows


def sub_period_table(res: Result, periods=None) -> list:
    periods = periods or [("1950-01-01", "1989-12-31"), ("1990-01-01", "2011-12-31"), ("2012-07-01", "2019-12-31"),
                          ("2020-01-01", "2026-12-31"), ("2012-07-01", "2026-12-31")]
    rows = []
    for s, e in periods:
        w = res.window(s, e)
        if len(w.daily) < 60:
            continue
        mt = w.metrics()
        rows.append({"start": mt["start_date"], "end": mt["end_date"], "cagr_pct": mt["annualized_return_pct"],
                     "spy_cagr_pct": mt["spy_annualized_return_pct"], "sharpe": mt.get("sharpe"), "spy_sharpe": mt.get("spy_sharpe"),
                     "max_dd_pct": mt["max_drawdown_pct"], "spy_max_dd_pct": mt["spy_max_drawdown_pct"],
                     "pct_days_cash": mt["pct_days_cash"], "changes_per_year": mt["position_changes_per_year"]})
    return rows


def save_json(obj, path: Path | str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, indent=2, default=_json_default))


def _json_default(o):
    if isinstance(o, (np.floating, np.integer)):
        return None if (isinstance(o, np.floating) and np.isnan(o)) else o.item()
    if isinstance(o, (pd.Timestamp,)):
        return o.strftime("%Y-%m-%d")
    if isinstance(o, float) and np.isnan(o):
        return None
    if isinstance(o, (pd.Series, pd.Index, np.ndarray)):
        return list(o)
    return str(o)


# ----------------------------------------------------------------------------- reference signals
def buy_and_hold(df: pd.DataFrame, lev: float = 1.0) -> pd.Series:
    return pd.Series(lev, index=df.index)
