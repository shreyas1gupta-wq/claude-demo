#!/usr/bin/env python3
"""Atlas 2.4/2.5 — KJ1, PRE-REGISTERED: the ~40-month Kitchin clock on monthly commodity prices.

Cells: (a) gold, floating era 1968-01..2026-07; (b) IMF all-commodity index 1980-02..2017-06.
Construction: expanding Hamilton gap (h=24, p=4) -> expanding percentile (min_obs 36) ->
extrema, min_gap 18 months. Bar (both cells): median spacing in [30,50]m AND >=50% in [30,50].
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from quant.ladder import expanding_percentile  # noqa: E402
from quant.stats.hamilton import hamilton_filter  # noqa: E402

OUT = ROOT / "research" / "cycles" / "kitchin-juglar" / "kitchin-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/kitchin-charts.json")


def spacings_of(x: np.ndarray, min_gap: int = 18):
    gap = hamilton_filter(np.log(x), h=24, p=4, mode="expanding")
    state = expanding_percentile(gap, min_obs=36)
    s = pd.Series(state).rolling(3, center=True).mean().dropna()
    idx, vals = s.index.to_numpy(), s.to_numpy()
    pks = []
    for i in range(1, len(vals) - 1):
        if vals[i] >= vals[i - 1] and vals[i] > vals[i + 1]:
            if not pks or idx[i] - pks[-1] >= min_gap:
                pks.append(int(idx[i]))
    return [b - a for a, b in zip(pks, pks[1:])], state


def cell(name, x):
    sp, state = spacings_of(np.asarray(x, float))
    med = float(np.median(sp))
    share = np.mean([30 <= v <= 50 for v in sp])
    ok = (30 <= med <= 50) and share >= 0.5
    return {"name": name, "n": len(sp), "median": med, "share": share,
            "verdict": "PASS" if ok else "FAIL", "spacings": sorted(sp), "state": state}


def main() -> int:
    g = pd.read_csv(ROOT / "ingest/vault/commodities/gold_monthly_1833_2026.csv")
    g = g[g.Date >= "1968-01"].reset_index(drop=True)
    imf = pd.read_csv(ROOT / "ingest/vault/commodities/imf_pcps_monthly_1980_2017.csv")
    allc = imf["All Commodity Price Index"].astype(float).dropna().to_numpy()

    a = cell("gold floating era (1968-2026)", g.Price.to_numpy())
    b = cell("IMF all-commodity (1980-2017)", allc)

    res = [
        "# Atlas 2.4/2.5 — the Kitchin clock: monthly commodity prices (KJ1, pre-registered)", "",
        "Nominal series (stated at registration); h=24m/p=4 expanding gap, extrema min_gap 18m.",
        "Bar per cell: median in [30,50]m AND >=50% of spacings in [30,50]m.", "",
        "| Cell | n spacings | median | share in [30,50]m | verdict |",
        "|---|---|---|---|---|",
        *[f"| {c['name']} | {c['n']} | {c['median']:.0f}m | {c['share']*100:.0f}% "
          f"| **{c['verdict']}** |" for c in (a, b)],
        "",
        f"Gold spacings: {a['spacings']}", f"IMF spacings: {b['spacings']}", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "gold": {"spacings": a["spacings"], "median": a["median"]},
        "imf": {"spacings": b["spacings"], "median": b["median"]},
        "window": [30, 50]}, separators=(",", ":")))
    print(f"KJ1a {a['verdict']} (med {a['median']:.0f}m, {a['share']*100:.0f}%) | "
          f"KJ1b {b['verdict']} (med {b['median']:.0f}m, {b['share']*100:.0f}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
