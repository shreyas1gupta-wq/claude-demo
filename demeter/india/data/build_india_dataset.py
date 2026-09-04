#!/usr/bin/env python3
"""Assemble india_daily.csv (one row per NSE trading day) from the raw index extracts in ./raw.

Source: github.com/BennyThadikaran/eod2_data (NSE end-of-day index files), snapshot 2026-08-31.
Run:  python3 build_india_dataset.py
"""
import json
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"

FILES = {
    "mcs": "nifty_midcap_select",      # MIDCPNIFTY - the F&O underlying (from 2021-09)
    "mc50": "nifty_midcap_50",         # long midcap proxy (from 2012-02)
    "mc100": "nifty_midcap_100",
    "mc150": "nifty_midcap_150",
    "nifty": "nifty_50",
    "n500": "nifty_500",
    "bank": "nifty_bank",
    "vix": "india_vix",
    "rate1d": "nifty_1d_rate_index",       # overnight TREPS rate index -> the cash engine
    "futidx": "nifty_50_futures_index",    # rolling long Nifty futures, price only
    "futtri": "nifty_50_futures_tr_index", # same plus collateral interest
    "arb": "nifty_50_arbitrage",
}


def load(stem):
    d = pd.read_csv(RAW / f"{stem}.csv", parse_dates=["Date"]).set_index("Date").sort_index()
    return d[~d.index.duplicated(keep="last")]


def main():
    parts, checks = {}, {}
    for key, stem in FILES.items():
        d = load(stem)
        parts[key] = d["Close"].rename(key)
        if key == "vix":
            parts["vix_high"] = d["High"].rename("vix_high")
            parts["vix_low"] = d["Low"].rename("vix_low")
        if key in ("mcs", "mc50", "nifty"):
            parts[f"{key}_open"] = d["Open"].rename(f"{key}_open")
            parts[f"{key}_high"] = d["High"].rename(f"{key}_high")
            parts[f"{key}_low"] = d["Low"].rename(f"{key}_low")
        if key in ("mcs", "mc50", "nifty") and "P/E" in d:
            parts[f"{key}_pe"] = d["P/E"].rename(f"{key}_pe")

    m = pd.concat(parts.values(), axis=1).sort_index()
    m = m[m.index >= "2012-02-21"]

    # ---- cash engine: Nifty 1D Rate Index (overnight TREPS, total return index) ----
    m["cash_ret"] = m["rate1d"].pct_change()
    m["cash_ann_pct"] = m["cash_ret"] * 252 * 100
    # before the 1D rate index starts (2016-06), hold the first observed 21-day average rate
    first_rate = m["cash_ret"].dropna().iloc[:21].mean()
    m["cash_src"] = np.where(m["cash_ret"].notna(), "nifty_1d_rate_index", "held_at_first_observation")
    m["cash_ret"] = m["cash_ret"].fillna(first_rate)

    # ---- price returns ----
    for k in ["mcs", "mc50", "mc100", "mc150", "nifty", "n500", "bank"]:
        m[f"{k}_ret"] = m[k].pct_change()

    # ---- what a rolling long FUTURES position actually earns, measured not assumed ----
    # NSE's Nifty 50 Futures Index tracks a rolling long futures position (price only), so its
    # return IS the excess return over cash that a futures holder receives.
    m["fut_ret"] = m["futidx"].pct_change()
    m["futtri_ret"] = m["futtri"].pct_change().replace([np.inf, -np.inf], np.nan)
    w = m.loc["2016-06-24":].dropna(subset=["fut_ret", "nifty_ret", "cash_ret", "futtri_ret"])
    basis_drag = (w["fut_ret"] - (w["nifty_ret"] - w["cash_ret"])).mean() * 252 * 100
    checks["nifty_futures_index"] = {
        "start": str(w.index.min().date()), "end": str(w.index.max().date()), "n": int(len(w)),
        "corr_fut_vs_price": float(w["fut_ret"].corr(w["nifty_ret"])),
        "fut_ann_pct": float(w["fut_ret"].mean() * 252 * 100),
        "price_minus_cash_ann_pct": float((w["nifty_ret"] - w["cash_ret"]).mean() * 252 * 100),
        "basis_drag_ann_pct": float(basis_drag),
        "note": "futures return minus (price return - cash) = net carry the futures holder gives up or gains, i.e. (dividend yield - basis premium)",
        "futtri_minus_fut_ann_pct": float(np.nanmean((w["futtri_ret"] - w["fut_ret"]).replace([np.inf, -np.inf], np.nan)) * 252 * 100),
        "cash_ann_pct": float(w["cash_ret"].mean() * 252 * 100),
    }
    # Excess (futures-equivalent) return for each index: price return - cash + measured net carry.
    # For Nifty we can use the futures index directly; for the midcap indices we apply the same
    # measured carry adjustment, which is the assumption to challenge (see PROVENANCE.md).
    carry = basis_drag / 100 / 252
    for k in ["mcs", "mc50", "mc100", "mc150", "nifty", "bank"]:
        m[f"{k}_x"] = m[f"{k}_ret"] - m["cash_ret"] + carry
    m["nifty_x_measured"] = m["fut_ret"]

    checks["carry_applied_ann_pct"] = float(basis_drag)
    checks["coverage"] = {k: {"first": str(m[k].dropna().index.min().date()), "last": str(m[k].dropna().index.max().date()), "n": int(m[k].notna().sum())} for k in ["mcs", "mc50", "nifty", "vix", "rate1d", "futidx"]}
    checks["rows"] = int(len(m))
    # correlation of the midcap proxies with the actual F&O underlying, where they overlap
    ov = m.dropna(subset=["mcs_ret", "mc50_ret", "mc100_ret", "mc150_ret"])
    checks["midcap_proxy_corr_vs_mcs"] = {k: float(ov[f"{k}_ret"].corr(ov["mcs_ret"])) for k in ["mc50", "mc100", "mc150"]}
    checks["midcap_proxy_overlap"] = {"start": str(ov.index.min().date()), "end": str(ov.index.max().date()), "n": int(len(ov))}
    ann = lambda s: (np.prod(1 + s.dropna()) ** (252 / max(1, s.notna().sum())) - 1) * 100
    checks["annualised_price_return_pct"] = {k: float(ann(m[f"{k}_ret"])) for k in ["mcs", "mc50", "nifty"]}
    checks["annualised_vol_pct"] = {k: float(m[f"{k}_ret"].std() * np.sqrt(252) * 100) for k in ["mcs", "mc50", "nifty"]}

    m.index.name = "date"
    m.to_csv(HERE / "india_daily.csv", float_format="%.10g")
    (HERE / "india_checks.json").write_text(json.dumps(checks, indent=2))
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    main()
