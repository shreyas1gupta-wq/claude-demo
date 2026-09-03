#!/usr/bin/env python3
"""Assemble market_daily.csv (one row per NYSE trading day) from the raw source extracts in ./raw.

Sources (see PROVENANCE.md):
  * steelcerberus_us_market_data.csv  - S&P 500 price & total-return (SPY-like) index, 3-month T-bill rate, 1885-2025-12-19
  * fred_sp500_daily_2016_2026.csv    - FRED SP500 daily closes, used to extend the price series to 2026-02-11
  * cboe_vix_daily.csv                - CBOE VIX daily OHLC, 1990-01-02 onward
  * pysystemtrade_{SP500,NASDAQ,FED}_daily.csv - back-adjusted futures prices (daily last), 1982/1999/1990 .. 2024-03-28
  * arch_yahoo_nasdaq_composite_1999_2018.csv  - NASDAQ Composite closes (cross-check only)
Run:  python3 build_dataset.py
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"


def load_spx():
    u = pd.read_csv(RAW / "steelcerberus_us_market_data.csv", parse_dates=["Date"])
    u = u.rename(columns={"Date": "date", "Close": "spx_px", "Adjusted Close": "spx_tr",
                          "Risk Free Rate": "rf_pct", "Swap Rate": "swap_pct"})
    u = u[["date", "spx_px", "spx_tr", "rf_pct", "swap_pct"]].sort_values("date").reset_index(drop=True)
    u["spx_src"] = "steelcerberus"
    u["rf_src"] = "steelcerberus"
    f = pd.read_csv(RAW / "fred_sp500_daily_2016_2026.csv", parse_dates=["observation_date"])
    f = f.rename(columns={"observation_date": "date", "SP500": "fred_px"}).dropna().sort_values("date")
    ov = u.merge(f, on="date", how="inner")
    ru, rf_ = ov.spx_px.pct_change(), ov.fred_px.pct_change()
    checks = {
        "fred_overlap_days": int(len(ov)),
        "fred_overlap_daily_ret_corr": float(ru.corr(rf_)),
        "fred_overlap_mean_abs_diff_bps": float((ru - rf_).abs().mean() * 1e4),
    }
    last = u.iloc[-1]
    dy_daily = float((u.spx_tr.pct_change() - u.spx_px.pct_change()).tail(252).mean())
    checks["extension_dividend_yield_pct_annual"] = dy_daily * 252 * 100
    ext = f[f.date > last.date]
    prev = float(f[f.date <= last.date].fred_px.iloc[-1])
    px, tr = float(last.spx_px), float(last.spx_tr)
    rows = []
    for d, fp in zip(ext.date, ext.fred_px):
        r = fp / prev - 1.0
        prev = fp
        px *= 1 + r
        tr *= 1 + r + dy_daily
        rows.append({"date": d, "spx_px": px, "spx_tr": tr, "rf_pct": float(last.rf_pct), "swap_pct": float(last.swap_pct),
                     "spx_src": "fred_sp500_price_plus_trailing_div_yield", "rf_src": "held_at_last_observation"})
    u = pd.concat([u, pd.DataFrame(rows)], ignore_index=True)
    checks["extension_rows"] = len(rows)
    checks["extension_from"] = str(rows[0]["date"].date()) if rows else None
    checks["extension_to"] = str(rows[-1]["date"].date()) if rows else None
    return u.set_index("date"), checks


def load_future(sym, prefix, idx):
    p = pd.read_csv(RAW / f"pysystemtrade_{sym}_daily.csv", parse_dates=["date"]).set_index("date").sort_index()
    p = p.dropna(subset=["adj_price"])
    union = idx.union(p.index)
    adj = p["adj_price"].reindex(union).ffill().reindex(idx)
    px = p["price"].reindex(union).ffill().reindex(idx)
    mask = (idx < p.index.min()) | (idx > p.index.max())
    adj[mask] = np.nan
    px[mask] = np.nan
    ret = adj.diff() / px.shift(1)
    ret[mask] = np.nan
    return pd.DataFrame({f"{prefix}_adj": adj.values, f"{prefix}_px": px.values, f"{prefix}_ret": ret.values}, index=idx)


def main():
    m, checks = load_spx()
    m["spx_ret"] = m.spx_px.pct_change()
    m["spx_tr_ret"] = m.spx_tr.pct_change()
    m["rf_daily"] = m.rf_pct / 100.0 / 252.0
    m["spx_quality"] = np.where(m.index < pd.Timestamp("1927-12-30"), "dow_composite_proxy", "sp500")

    v = pd.read_csv(RAW / "cboe_vix_daily.csv", parse_dates=["DATE"]).set_index("DATE").sort_index()
    v.columns = ["vix_open", "vix_high", "vix_low", "vix_close"]
    m = m.join(v, how="left")

    idx = m.index
    es = load_future("SP500", "es", idx)
    nq = load_future("NASDAQ", "nq", idx)
    ff = load_future("FED", "ff", idx)
    m = m.join(es).join(nq)
    m["ff_implied_pct"] = 100.0 - ff["ff_px"]

    ix = pd.read_csv(RAW / "arch_yahoo_nasdaq_composite_1999_2018.csv", index_col=0, parse_dates=True)
    m = m.join(ix["Close"].rename("ixic_close"), how="left")

    # ---- validation ----
    # Futures (E-mini S&P) vs synthetic futures (S&P TR minus T-bill). The pysystemtrade snapshot is clean daily
    # settlement data until 2013-10 and sparse/irregular hourly bars afterwards, so the two eras are reported separately.
    for label, s0, s1 in [("daily_era_1990_2013", "1990-01-02", "2013-10-15"), ("hourly_era_2013_2024", "2013-10-16", "2024-03-28"),
                          ("demeter_window_2012_2024", "2012-07-02", "2024-03-28")]:
        w = m.loc[s0:s1]
        ex_es = w.es_ret
        ex_syn = w.spx_tr_ret - w.rf_daily
        wk_es = (1 + ex_es).resample("W").prod() - 1
        wk_syn = (1 + ex_syn).resample("W").prod() - 1
        mo_es = (1 + ex_es).resample("ME").prod() - 1
        mo_syn = (1 + ex_syn).resample("ME").prod() - 1
        checks[f"es_vs_synthetic_{label}"] = {
            "daily_corr": float(ex_es.corr(ex_syn)), "weekly_corr": float(wk_es.corr(wk_syn)), "monthly_corr": float(mo_es.corr(mo_syn)),
            "ann_mean_diff_pct": float((ex_es - ex_syn).mean() * 252 * 100),
            "es_ann_excess_pct": float(ex_es.mean() * 252 * 100), "syn_ann_excess_pct": float(ex_syn.mean() * 252 * 100),
        }
    w3 = m.loc["2000-01-03":"2018-12-31"]
    checks["nq_vs_ixic_2000_2018_corr"] = float(w3.nq_ret.corr(w3.ixic_close.pct_change()))
    w4 = m.loc["1990-03-13":"2024-03-28"]
    checks["rf_vs_fedfunds_implied_1990_2024_mean_diff_pct"] = float((w4.rf_pct - w4.ff_implied_pct).mean())
    cov = {}
    for c in ["spx_px", "spx_tr", "rf_pct", "vix_close", "es_ret", "nq_ret", "ixic_close", "ff_implied_pct"]:
        s = m[c].dropna()
        cov[c] = {"first": str(s.index.min().date()), "last": str(s.index.max().date()), "n": int(len(s))}
    checks["coverage"] = cov
    checks["rows"] = int(len(m))

    cols = ["spx_px", "spx_tr", "spx_ret", "spx_tr_ret", "rf_pct", "rf_daily", "swap_pct", "spx_quality", "spx_src", "rf_src",
            "vix_open", "vix_high", "vix_low", "vix_close", "es_adj", "es_px", "es_ret", "nq_adj", "nq_px", "nq_ret",
            "ff_implied_pct", "ixic_close"]
    m = m[cols]
    m.index.name = "date"
    m.to_csv(HERE / "market_daily.csv", float_format="%.10g")
    (HERE / "dataset_checks.json").write_text(json.dumps(checks, indent=2, default=str))
    print(json.dumps(checks, indent=2, default=str))


if __name__ == "__main__":
    main()
