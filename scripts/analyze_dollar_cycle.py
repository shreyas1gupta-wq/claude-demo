#!/usr/bin/env python3
"""Atlas 2.9/2.10 — DL1-DL3, PRE-REGISTERED: the dollar-swing clock, the India headwind,
and the Fed sub-face, on a REAL equal-weight dollar index built from JST xrusd + cpi
(chained mean of USD real appreciation vs the panel currencies, 1950-2015, USA excluded).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "dollar-fold" / "dollar-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/dollar-charts.json")


def peaks_of(series: pd.Series, min_gap: int = 4):
    s = series.rolling(3, center=True).mean().dropna()
    years, vals = s.index.to_numpy(), s.to_numpy()
    out = []
    for i in range(1, len(vals) - 1):
        if vals[i] >= vals[i - 1] and vals[i] > vals[i + 1]:
            if not out or years[i] - out[-1] >= min_gap:
                out.append(int(years[i]))
    return out


def main() -> int:
    df = pd.ExcelFile(ROOT / "ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
    df = df[["iso", "year", "xrusd", "cpi", "stir"]].sort_values(["iso", "year"])
    us = df[df.iso == "USA"].set_index("year")
    pi_us = np.log(us.cpi.astype(float)).diff()

    apps = {}
    for iso, d in df.groupby("iso"):
        if iso == "USA":
            continue
        d = d.set_index("year").loc[1950:2015]
        dx = np.log(d.xrusd.astype(float)).diff()
        pi = np.log(d.cpi.astype(float)).diff()
        apps[iso] = dx - pi + pi_us.reindex(d.index)
    A = pd.DataFrame(apps)
    dlog = A.mean(axis=1)
    index = dlog.fillna(0).cumsum()
    index.name = "real_usd"

    pks = peaks_of(index)
    sp = [b - a for a, b in zip(pks, pks[1:])]
    med = float(np.median(sp)) if sp else float("nan")
    share = np.mean([6 <= v <= 11 for v in sp]) if sp else float("nan")
    dl1 = "PASS" if sp and (7 <= med <= 10) and share >= 0.5 else "FAIL"

    f = pd.read_csv(ROOT / "ingest/vault/factors/iima_monthly_factors.csv", na_values=["NA"])
    f["Year"] = f.Date.str[:4].astype(int)
    ind = f.groupby("Year").MF.apply(lambda x: float(np.expm1(np.log1p(x / 100).sum())))
    j = pd.concat([dlog, ind], axis=1, keys=["dusd", "ind"]).dropna().loc[1994:2015]
    dl2_corr = float(j.corr().iloc[0, 1])
    dl2 = "PASS" if dl2_corr <= -0.30 else "FAIL"

    dstir = us.stir.astype(float).diff()
    k = pd.concat([dstir, dlog], axis=1, keys=["ds", "du"]).dropna()
    same = float(k.corr().iloc[0, 1])
    nxt = float(pd.concat([dstir, dlog.shift(-1)], axis=1).dropna().corr().iloc[0, 1])

    res = [
        "# Atlas 2.9/2.10 — dollar/Fed folds: DL1-DL3 (pre-registered)", "",
        "Real equal-weight dollar index vs the JST panel (chained, 1950-2015). Bars fixed",
        "before running; interpretation AFTER the print.", "",
        "## DL1 — the '7-10y dollar swing' as a clock claim", "",
        f"- Peaks: {pks}; spacings {sp}; median **{med:.0f}y**; share in [6,11]y "
        f"**{share*100:.0f}%**.",
        f"- Bar (median in [7,10] AND ≥50% in [6,11]): **{dl1}**.", "",
        "## DL2 — dollar-up = India equity headwind (1994-2015, n=22)", "",
        f"- corr(annual real-USD change, India market factor) = **{dl2_corr:+.2f}** "
        f"(bar ≤ −0.30): **{dl2}**.", "",
        "## DL3 — the Fed sub-face (measurement, prior set)", "",
        f"- corr(ΔUS short rate, real-USD change): same-year **{same:+.2f}**, "
        f"next-year **{nxt:+.2f}** (n={len(k)}).", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "index": [[int(y), round(float(v), 3)] for y, v in index.items()],
        "peaks": pks, "spacings": sp, "dl2": round(dl2_corr, 2),
        "scatter": [[int(y), round(r.dusd, 3), round(r.ind, 3)] for y, r in j.iterrows()]},
        separators=(",", ":")))
    print(f"DL1 {dl1} (peaks {pks}, med {med:.0f}y) | DL2 {dl2} ({dl2_corr:+.2f}) | "
          f"DL3 same {same:+.2f} next {nxt:+.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
