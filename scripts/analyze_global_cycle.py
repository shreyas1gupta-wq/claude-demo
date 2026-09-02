#!/usr/bin/env python3
"""Atlas 2.8 (global financial cycle, seat L9) — trials GF1-GF3, PRE-REGISTERED.

GF1: median pairwise corr of annual real equity returns, pre-1990 (1900-1989) vs post-1990
(1990-2015). Bar: post exceeds pre by >= 0.10.
GF2: annual India MF (compounded iima monthly) vs equal-weight JST mean, 1994-2015 (n=22).
Bar: corr >= 0.30.
GF3: post-1950 global-down years (pooled mean < 0): median share of countries negative.
Bar: >= 75%.
"""
from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "globalcycle-deep" / "global-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/global-charts.json")


def med_pairwise(wide: pd.DataFrame) -> float:
    cors = []
    for a, b in combinations(wide.columns, 2):
        x = wide[[a, b]].dropna()
        if len(x) >= 20:
            cors.append(float(x.corr().iloc[0, 1]))
    return float(np.median(cors)), len(cors)


def main() -> int:
    rr = pd.read_csv(ROOT / "ingest/vault/debt/jst_real_returns.csv", comment="#")
    wide = rr.pivot(index="year", columns="iso", values="equity").astype(float)

    pre, n_pre = med_pairwise(wide.loc[1900:1989])
    post, n_post = med_pairwise(wide.loc[1990:2015])
    gf1 = "PASS" if post - pre >= 0.10 else "FAIL"

    f = pd.read_csv(ROOT / "ingest/vault/factors/iima_monthly_factors.csv",
                    na_values=["NA"])
    f["Year"] = f.Date.str[:4].astype(int)
    ind = f.groupby("Year").MF.apply(lambda x: float(np.expm1(np.log1p(x / 100).sum())))
    glob = wide.mean(axis=1)
    j = pd.concat([ind, glob], axis=1, keys=["ind", "glob"]).dropna().loc[1994:2015]
    gf2_corr = float(j.corr().iloc[0, 1])
    gf2 = "PASS" if gf2_corr >= 0.30 else "FAIL"

    g50 = wide.loc[1950:]
    downs = g50.index[g50.mean(axis=1) < 0]
    shares = [(g50.loc[y] < 0).mean() for y in downs]
    gf3_med = float(np.median(shares))
    gf3 = "PASS" if gf3_med >= 0.75 else "FAIL"

    res = [
        "# Atlas 2.8 — global financial cycle: GF1-GF3 (pre-registered)", "",
        "## GF1 — the factor's rise (pairwise co-movement, annual real equity)", "",
        f"- Pre-1990 median pairwise corr **{pre:+.2f}** ({n_pre} pairs); post-1990 "
        f"**{post:+.2f}** ({n_post} pairs); difference **{post-pre:+.2f}** (bar ≥ +0.10): **{gf1}**.", "",
        "## GF2 — India's loading (annual, 1994-2015, n=22)", "",
        f"- corr(India market factor, equal-weight JST mean) = **{gf2_corr:+.2f}** "
        f"(bar ≥ 0.30): **{gf2}**.", "",
        "## GF3 — breadth of global down-years (post-1950)", "",
        f"- {len(downs)} global-down years; median share of countries negative "
        f"**{gf3_med*100:.0f}%** (bar ≥ 75%): **{gf3}**.",
        f"- Down years: {[int(y) for y in downs]}", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "pre": round(pre, 2), "post": round(post, 2),
        "india_vs_global": [[int(y), round(r.ind, 3), round(r.glob, 3)]
                            for y, r in j.iterrows()],
        "gf2_corr": round(gf2_corr, 2),
        "down_years": {int(y): round(float(s), 2) for y, s in zip(downs, shares)}},
        separators=(",", ":")))
    print(f"GF1 {gf1} ({pre:+.2f}->{post:+.2f}) | GF2 {gf2} ({gf2_corr:+.2f}) | "
          f"GF3 {gf3} (median breadth {gf3_med*100:.0f}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
