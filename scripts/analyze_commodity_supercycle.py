#!/usr/bin/env python3
"""Atlas 1.3 (commodity supercycle) — real-data leg on Jacks 1850-2015 + Clio/USGS production.

Twelfth real-data batch. Trials CS1/CS1b-CS4, PRE-REGISTERED in research/register/trial-ledger.md
before this ran (two-pass rule per verification-log near-miss #4). Groups (the file's natural
grouping, fixed here before running): energy = {Coal, Natural gas, Petroleum}; metals_minerals =
{Aluminum, Chromium, Copper, Lead, Manganese, Nickel, Steel, Tin, Zinc, Bauxite, Iron ore, Gold,
Platinum, Silver, Phosphate, Potash, Sulfur}; agriculture = the rest. CS3/CS4 matched metals:
the 11 with both a Jacks price and a Clio/USGS World production column.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

V = ROOT / "ingest" / "vault" / "commodities"
OUT = ROOT / "research" / "cycles" / "commodity-deep" / "commodities-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/commodity-charts.json")

ENERGY = ["Coal", "Natural gas", "Petroleum"]
METALS = ["Aluminum", "Chromium", "Copper", "Lead", "Manganese", "Nickel", "Steel", "Tin",
          "Zinc", "Bauxite", "Iron ore", "Phosphate", "Potash", "Sulfur", "Gold", "Platinum",
          "Silver"]
MATCH = {"Nickel": "Nickel", "Zinc": "Zinc", "Silver": "Silver", "Bauxite": "Bauxite",
         "Iron ore": "Iron Ore", "Gold": "Gold", "Tin": "Tin", "Lead": "Lead",
         "Copper": "Copper", "Aluminum": "Aluminium", "Manganese": "Manganese"}


def extrema(series: pd.Series, min_gap: int = 15):
    """Local minima AND maxima of the 3y-centered-smoothed level (positional, RE1 machinery)."""
    s = series.rolling(3, center=True).mean().dropna()
    years, vals = s.index.to_numpy(), s.to_numpy()
    peaks, troughs = [], []
    for i in range(1, len(vals) - 1):
        if vals[i] >= vals[i - 1] and vals[i] > vals[i + 1]:
            if not peaks or years[i] - peaks[-1] >= min_gap:
                peaks.append(int(years[i]))
        if vals[i] <= vals[i - 1] and vals[i] < vals[i + 1]:
            if not troughs or years[i] - troughs[-1] >= min_gap:
                troughs.append(int(years[i]))
    return peaks, troughs


def main() -> int:
    j = pd.read_csv(V / "jacks_real_commodity_prices_1850_2015.csv").set_index("Year")
    j = j.drop(columns=["Entity"])
    logs = np.log(j)

    # CS1: plain equal-weight mean of available log prices
    idx_plain = logs.mean(axis=1)
    # CS1b: chained mean-of-Δlog (composition-robust)
    dl = logs.diff()
    chain = dl.mean(axis=1).fillna(0).cumsum()
    chain.name = "chained"

    def cs1(index: pd.Series, label: str):
        pks, trs = extrema(index.loc[1870:])
        sp = [b - a for a, b in zip(trs, trs[1:])]
        ok = (3 <= len(trs) <= 5) and (len(sp) > 0 and 25 <= float(np.median(sp)) <= 45)
        return {"label": label, "peaks": pks, "troughs": trs, "spacings": sp,
                "median": float(np.median(sp)) if sp else float("nan"),
                "verdict": "PASS" if ok else "FAIL"}

    r1, r1b = cs1(idx_plain, "plain"), cs1(chain, "chained")

    # CS2: 10y dlog corr within vs across groups
    d10 = logs - logs.shift(10)
    groups = {c: ("energy" if c in ENERGY else "metals" if c in METALS else "ag")
              for c in logs.columns}
    within, across = [], []
    cols = [c for c in logs.columns if d10[c].notna().sum() > 40]
    for i, a in enumerate(cols):
        for b in cols[i + 1:]:
            x = pd.concat([d10[a], d10[b]], axis=1).dropna()
            if len(x) < 40:
                continue
            r = float(x.corr().iloc[0, 1])
            (within if groups[a] == groups[b] else across).append(r)
    cs2_ok = np.median(across) > 0 and np.mean([r > 0 for r in across]) >= 0.5

    # CS3/CS4: price vs World production, decade lead/lag
    m = pd.read_csv(V / "metal_production_clio_usgs.csv")
    w = m[m.Entity == "World"].set_index("Year")
    cs3, cs4 = {}, {}
    for price_col, prod_stub in MATCH.items():
        prod = w[[c for c in w.columns if c.startswith(prod_stub + " ")][0]].astype(float)
        lp, lq = np.log(j[price_col]), np.log(prod.replace(0, np.nan))
        dp, dq = (lp - lp.shift(10)), (lq - lq.shift(10))
        a = pd.concat([dp, dq.shift(-10)], axis=1).dropna()   # price change -> NEXT decade prod
        b = pd.concat([dq, dp.shift(-10)], axis=1).dropna()   # prod change -> NEXT decade price
        if len(a) > 40:
            cs3[price_col] = float(a.corr().iloc[0, 1])
        if len(b) > 40:
            cs4[price_col] = float(b.corr().iloc[0, 1])
    cs3_share = np.mean([v > 0 for v in cs3.values()])
    cs4_share = np.mean([v < 0 for v in cs4.values()])

    res = [
        "# Atlas 1.3 — commodity supercycle: Jacks 1850-2015 + Clio/USGS World production",
        "",
        "Trials CS1/CS1b-CS4 pre-registered (constructions, groups, bars) before this ran;",
        "interpretation written AFTER the print. Vault authenticated (A1-A5, all pass).", "",
        "## CS1 / CS1b — existence and shape (claim: 3-4 supercycles, trough-to-trough 30-40y)", "",
        "| Index | troughs (min_gap 15y, from 1870) | spacings | median | bar (3-5 troughs AND median in [25,45]) |",
        "|---|---|---|---|---|",
        f"| plain | {r1['troughs']} | {r1['spacings']} | {r1['median']:.0f}y | **{r1['verdict']}** |",
        f"| chained | {r1b['troughs']} | {r1b['spacings']} | {r1b['median']:.0f}y | **{r1b['verdict']}** |",
        "",
        f"Peaks for the record: plain {r1['peaks']}, chained {r1b['peaks']}.", "",
        "## CS2 — breadth (supercycles claimed BROAD, cross-group)", "",
        f"- {len(within)} within-group pairs: median corr(10y Δlog) **{np.median(within):+.2f}**;",
        f"  {len(across)} across-group pairs: median **{np.median(across):+.2f}**, "
        f"{np.mean([r > 0 for r in across])*100:.0f}% positive.",
        f"- Bar (across-group median > 0 AND ≥50% positive): **{'PASS' if cs2_ok else 'FAIL'}**.", "",
        "## CS3 — mechanism leg 1: price boom → NEXT decade's capacity", "",
        "| Metal | corr(10y Δlog price, next-10y Δlog World production) |", "|---|---|",
        *[f"| {k} | {v:+.2f} |" for k, v in sorted(cs3.items())],
        f"", f"- Sign-consistency: **{cs3_share*100:.0f}% positive** (bar ≥70%): "
        f"**{'PASS' if cs3_share >= 0.7 else 'FAIL'}**.", "",
        "## CS4 — mechanism leg 2: capacity surge → NEXT decade's price", "",
        "| Metal | corr(10y Δlog production, next-10y Δlog real price) |", "|---|---|",
        *[f"| {k} | {v:+.2f} |" for k, v in sorted(cs4.items())],
        f"", f"- Sign-consistency: **{cs4_share*100:.0f}% negative** (bar ≥70%): "
        f"**{'PASS' if cs4_share >= 0.7 else 'FAIL'}**.", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")

    CHART.write_text(json.dumps({
        "index_plain": [[int(y), round(float(v), 4)] for y, v in idx_plain.dropna().items()],
        "index_chained": [[int(y), round(float(v), 4)] for y, v in chain.dropna().items()],
        "troughs": r1b["troughs"], "peaks": r1b["peaks"],
        "cs3": {k: round(v, 2) for k, v in cs3.items()},
        "cs4": {k: round(v, 2) for k, v in cs4.items()},
        "petroleum": [[int(y), round(float(v), 2)] for y, v in j["Petroleum"].dropna().items()],
        "copper": [[int(y), round(float(v), 2)] for y, v in j["Copper"].dropna().items()],
    }, separators=(",", ":")))
    print(f"CS1 {r1['verdict']} (med {r1['median']:.0f}y, n_troughs {len(r1['troughs'])}) | "
          f"CS1b {r1b['verdict']} (med {r1b['median']:.0f}y, n {len(r1b['troughs'])}) | "
          f"CS2 {'PASS' if cs2_ok else 'FAIL'} (across med {np.median(across):+.2f}) | "
          f"CS3 {cs3_share*100:.0f}%+ | CS4 {cs4_share*100:.0f}%-")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
