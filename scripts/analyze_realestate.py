#!/usr/bin/env python3
"""Atlas 1.2 (real-estate cycle, merge entry) — real-data leg on JST R6.

Eleventh real-data batch. Trials RE1-RE2, PRE-REGISTERED in research/register/trial-ledger.md
BEFORE this script ran (constructions and pass bars declared there; nothing else was tried).
RE1: the folk 18-year claim — peak-to-peak spacings of REAL house prices (3y centered smooth,
local max, min_gap 8y). Pass bar: pooled median in [14,22]y AND >=50% of spacings in [14,22]y.
RE2: the Kuznets 15-25y swing — same construction on investment/GDP (iy). Pass bar: pooled
median in [15,25]y AND >=50% in [15,25]y; pre/post-1950 split reported direction-only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

OUT = ROOT / "research" / "cycles" / "realestate-merge" / "jst-realestate-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/realestate-charts.json")


def level_peaks(series: pd.Series, min_gap: int = 8):
    """Local maxima of the 3y-centered-smoothed LEVEL, min spacing in years (positional)."""
    s = series.rolling(3, center=True).mean().dropna()
    years, vals = s.index.to_numpy(), s.to_numpy()
    idx = []
    for i in range(1, len(vals) - 1):
        if vals[i] >= vals[i - 1] and vals[i] > vals[i + 1]:
            if not idx or years[i] - idx[-1] >= min_gap:
                idx.append(int(years[i]))
    return idx


def spacing_test(df: pd.DataFrame, col_fn, window: tuple[int, int], min_obs: int = 40):
    spacings, per_country, all_peaks = [], {}, {}
    for c, d in df.groupby("country"):
        d = d.set_index("year")
        s = col_fn(d)
        if s.notna().sum() < min_obs:
            continue
        pks = level_peaks(s.dropna())
        all_peaks[c] = pks
        sp = [b - a for a, b in zip(pks, pks[1:])]
        spacings += [(c, x, pks[i + 1]) for i, x in enumerate(sp)]
        if sp:
            per_country[c] = float(np.median(sp))
    vals = [x for _, x, _ in spacings]
    lo, hi = window
    in_win = [x for x in vals if lo <= x <= hi]
    return {"spacings": spacings, "vals": vals, "median": float(np.median(vals)),
            "share_in": len(in_win) / len(vals), "per_country": per_country,
            "peaks": all_peaks, "n": len(vals)}


def main() -> int:
    df = pd.ExcelFile(ROOT / "ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
    df = df[["country", "year", "hpnom", "cpi", "iy"]].sort_values(["country", "year"])

    re1 = spacing_test(df, lambda d: (d.hpnom / d.cpi).astype(float), (14, 22))
    re2 = spacing_test(df, lambda d: d.iy.astype(float), (15, 25))
    re2_pre = [x for _, x, y in re2["spacings"] if y < 1950]
    re2_post = [x for _, x, y in re2["spacings"] if y >= 1950]

    def verdict(r, lo, hi):
        a = lo <= r["median"] <= hi
        b = r["share_in"] >= 0.5
        return a, b, ("PASS" if a and b else "FAIL")

    a1, b1, v1 = verdict(re1, 14, 22)
    a2, b2, v2 = verdict(re2, 15, 25)

    q = lambda v, p: float(np.percentile(v, p))
    res = [
        "# Atlas 1.2 — real-estate cycle: JST R6 results (RE1-RE2)", "",
        "Constructions and pass bars PRE-REGISTERED in the trial ledger before this ran; the",
        "interpretation below was written AFTER the print (standing rule). Peaks = local maxima",
        "of the 3y-centered-smoothed level, min_gap 8y, per country; spacings pooled.", "",
        "## RE1 — the folk 18-year claim (real house prices)", "",
        f"- n = {re1['n']} spacings across {len(re1['per_country'])} countries.",
        f"- Pooled spacing: median **{re1['median']:.0f}y**, IQR {q(re1['vals'],25):.0f}-"
        f"{q(re1['vals'],75):.0f}y, full range {min(re1['vals'])}-{max(re1['vals'])}y.",
        f"- Share in the claimed [14, 22]y window: **{re1['share_in']*100:.0f}%** (bar: >=50%).",
        f"- Pre-registered bar: median in [14,22] -> {a1}; share >=50% -> {b1}. **{v1}**.", "",
        "Per-country median spacings (y): " + ", ".join(
            f"{c} {m:.0f}" for c, m in sorted(re1["per_country"].items())), "",
        "## RE2 — the Kuznets 15-25y swing (investment/GDP)", "",
        f"- n = {re2['n']} spacings across {len(re2['per_country'])} countries.",
        f"- Pooled spacing: median **{re2['median']:.0f}y**, IQR {q(re2['vals'],25):.0f}-"
        f"{q(re2['vals'],75):.0f}y.",
        f"- Share in the claimed [15, 25]y window: **{re2['share_in']*100:.0f}%** (bar: >=50%).",
        f"- Pre-registered bar: median in [15,25] -> {a2}; share >=50% -> {b2}. **{v2}**.",
        f"- Pre/post-1950 split (direction only, no bar): median {np.median(re2_pre):.0f}y "
        f"(n={len(re2_pre)}) vs {np.median(re2_post):.0f}y (n={len(re2_post)}).", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "re1_spacings": sorted(re1["vals"]), "re2_spacings": sorted(re2["vals"]),
        "re1_window": [14, 22], "re2_window": [15, 25],
        "peaks_sample": {c: re1["peaks"][c] for c in ("USA", "UK", "Japan", "Germany")
                         if c in re1["peaks"]}}, separators=(",", ":")))
    print(f"RE1 median {re1['median']:.0f}y share {re1['share_in']*100:.0f}% -> {v1} | "
          f"RE2 median {re2['median']:.0f}y share {re2['share_in']*100:.0f}% -> {v2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
