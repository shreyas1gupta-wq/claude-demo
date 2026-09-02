#!/usr/bin/env python3
"""Atlas 2.12 — OL1, PRE-REGISTERED: India's oil-shock asymmetry by shock flavor.

Oil-up years (annual real oil return > +10%, Brent annualized 1988+; Jacks Petroleum real
before): demand-flavored (pooled JST mean real equity return > 0) vs supply-flavored (< 0).
India leg: annual iima MF, 1994-2015. Bar: demand-mean minus supply-mean >= +10pp. n small,
stated; the world-equity-sign proxy conflates demand flavor with risk appetite (declared).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
V = ROOT / "ingest" / "vault"
OUT = ROOT / "research" / "cycles" / "oil-fold" / "oil-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/oil-charts.json")


def main() -> int:
    br = pd.read_csv(V / "commodities/brent_monthly_eia.csv", parse_dates=["Date"])
    br["Year"] = br.Date.dt.year
    oil_ann = br.groupby("Year").Price.mean()
    oil_ret = np.log(oil_ann).diff()

    rr = pd.read_csv(V / "debt/jst_real_returns.csv", comment="#")
    glob = rr.pivot(index="year", columns="iso", values="equity").astype(float).mean(axis=1)

    f = pd.read_csv(V / "factors/iima_monthly_factors.csv", na_values=["NA"])
    f["Year"] = f.Date.str[:4].astype(int)
    ind = f.groupby("Year").MF.apply(lambda x: float(np.expm1(np.log1p(x / 100).sum())))

    j = pd.concat([oil_ret, glob, ind], axis=1, keys=["oil", "glob", "ind"]).dropna()
    j = j.loc[1994:2015]
    up = j[j.oil > np.log(1.10)]
    demand = up[up.glob > 0]
    supply = up[up.glob <= 0]
    md, ms = float(demand.ind.mean()), float(supply.ind.mean())
    diff = md - ms
    ol1 = "PASS" if diff >= 0.10 else "FAIL"

    res = [
        "# Atlas 2.12 — oil fold: the shock-flavor asymmetry (OL1, pre-registered)", "",
        f"Oil-up years 1994-2015 (annual real oil return > +10%): n = {len(up)} "
        f"({len(demand)} demand-flavored, {len(supply)} supply-flavored — TINY, stated;",
        "the world-equity-sign proxy conflates demand flavor with risk appetite, declared).", "",
        "| Year | oil return | flavor (glob sign) | India return |", "|---|---|---|---|",
        *[f"| {int(y)} | {np.expm1(r.oil)*100:+.0f}% | {'demand' if r.glob>0 else 'supply'} "
          f"| {r.ind*100:+.1f}% |" for y, r in up.iterrows()],
        "",
        f"- Mean India return: demand-flavored **{md*100:+.1f}%**, supply-flavored "
        f"**{ms*100:+.1f}%**; difference **{diff*100:+.1f}pp** (bar ≥ +10pp): **{ol1}**.", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "rows": [[int(y), round(float(np.expm1(r.oil)), 3), "demand" if r.glob > 0 else "supply",
                  round(float(r.ind), 3)] for y, r in up.iterrows()],
        "means": {"demand": round(md, 3), "supply": round(ms, 3)}},
        separators=(",", ":")))
    print(f"OL1 {ol1} | n={len(up)} ({len(demand)}D/{len(supply)}S) | "
          f"demand {md*100:+.1f}% vs supply {ms*100:+.1f}% -> diff {diff*100:+.1f}pp")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
