"""TS1 — L4 TSMOM calibration on the vaulted index + gold (pre-registered, DD-shaped bars).

Ledger 2026-09-02. Long if trailing k-month return > 0 else flat; k in {3,6,12}; monthly,
next-month application; costs 28bp/switch (NIFTY) / 10bp (gold, stated [A]).
"""
from pathlib import Path

import numpy as np
import pandas as pd

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault"


def monthly_from_daily(path, datecol, pricecol, start=None):
    df = pd.read_csv(path, parse_dates=[datecol]).sort_values(datecol)
    if start:
        df = df[df[datecol] >= start]
    s = df.set_index(datecol)[pricecol]
    return s.groupby(s.index.to_period("M")).last()


def run(name, m, cost):
    ret = m.pct_change().dropna()
    yrs = len(ret) / 12
    bh_cagr = (np.prod(1 + ret)) ** (1 / yrs) - 1
    lvl = np.cumprod(1 + ret.values)
    bh_dd = float((1 - lvl / np.maximum.accumulate(lvl)).max())
    print(f"\n{name}: {len(ret)} months; buy-hold CAGR {bh_cagr*100:.1f}%, maxDD {bh_dd*100:.0f}%")
    for k in (3, 6, 12):
        sig = (m / m.shift(k) - 1).shift(1).reindex(ret.index)  # decided at t-1 close
        pos = (sig > 0).astype(float)
        valid = sig.notna()
        pret = (pos * ret - pos.diff().abs().fillna(0) * cost)[valid]
        hits = float(((sig > 0) == (ret > 0))[valid].mean())
        yrs_v = len(pret) / 12
        cagr = (np.prod(1 + pret)) ** (1 / yrs_v) - 1
        lv = np.cumprod(1 + pret.values)
        dd = float((1 - lv / np.maximum.accumulate(lv)).max())
        bh_v = ret[valid]
        bh_cagr_v = (np.prod(1 + bh_v)) ** (1 / yrs_v) - 1
        lvb = np.cumprod(1 + bh_v.values)
        bh_dd_v = float((1 - lvb / np.maximum.accumulate(lvb)).max())
        sw = int(pos.diff().abs().sum())
        ok = (dd <= bh_dd_v - 0.10) and (cagr >= bh_cagr_v - 0.02)
        print(f"  k={k:2d}m: hit {hits:.0%} | net CAGR {cagr*100:+5.1f}% (bh {bh_cagr_v*100:+5.1f}) | "
              f"maxDD {dd*100:3.0f}% (bh {bh_dd_v*100:3.0f}) | switches {sw:3d} | "
              f"{'PASS' if ok else 'FAIL'}")


nifty = monthly_from_daily(VAULT / "index" / "nifty50_daily_2007_2026.csv", "Date", "Close")
run("NIFTY 50 (2007-2026)", nifty, 0.0028)

g = pd.read_csv(VAULT / "commodities" / "gold_monthly_1833_2026.csv")
g["Date"] = pd.to_datetime(g["Date"], format="%Y-%m")
g = g[g["Date"] >= "1972-01-01"].set_index("Date")["Price"]
g.index = g.index.to_period("M")
run("Gold float era (1972-2026)", g, 0.0010)
