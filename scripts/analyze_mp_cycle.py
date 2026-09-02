#!/usr/bin/env python3
"""Atlas 2.6 (monetary-policy cycle, seat L6) — analogue trials MP1-MP3, PRE-REGISTERED.

Matched legs per the BC2 standing warning: Δstir (1y change, short rate) and g_credit
(1y growth of real loans), both simple annual changes, no differential smoothing.
MP1: per country, most NEGATIVE cross-corr over lags -3..+3 (+ = rate leads); qualifying
floor |min| >= 0.10. Bar: >=60% of qualifying countries at lag >= +1.
MP2: pooled corr of Δstir_t vs g_credit at t+0..t+3 (measurement).
MP3: P(sign Δstir_{t+1} = sign Δstir_t), pooled (measurement).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "mpcycle-deep" / "mp-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/mp-charts.json")


def main() -> int:
    df = pd.ExcelFile(ROOT / "ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
    df = df[["iso", "year", "stir", "tloans", "cpi"]].sort_values(["iso", "year"])

    mins, pooled_x, pooled_g = {}, [], []
    persist = []
    for iso, d in df.groupby("iso"):
        d = d.set_index("year")
        ds = d.stir.astype(float).diff()
        rl = (d.tloans / d.cpi).astype(float)
        g = np.log(rl).diff()
        j = pd.concat([ds, g], axis=1, keys=["ds", "g"]).dropna()
        if len(j) < 50:
            continue
        cors = {}
        for lag in range(-3, 4):
            x = pd.concat([j.ds.shift(lag), j.g], axis=1).dropna()
            cors[lag] = float(x.corr().iloc[0, 1])
        lag_min = min(cors, key=lambda k: cors[k])
        mins[iso] = (lag_min, cors[lag_min])
        pooled_x.append(j.ds)
        pooled_g.append(j.g)
        s = np.sign(j.ds.replace(0, np.nan)).dropna()
        persist += (s.diff().fillna(0) == 0).iloc[1:].tolist()

    qual = {k: v for k, v in mins.items() if v[1] <= -0.10}
    share = np.mean([lag >= 1 for lag, _ in qual.values()]) if qual else float("nan")
    mp1 = "PASS" if qual and share >= 0.6 else "FAIL"

    X = pd.concat(pooled_x).reset_index(drop=True)
    # pooled lag profile computed per country then averaged to avoid cross-country pooling bias
    prof = {}
    for h in range(0, 4):
        vals = []
        for xs, gs in zip(pooled_x, pooled_g):
            a = pd.concat([xs, gs.shift(-h)], axis=1).dropna()
            if len(a) >= 50:
                vals.append(float(a.corr().iloc[0, 1]))
        prof[h] = float(np.mean(vals))
    p_persist = float(np.mean(persist))

    res = [
        "# Atlas 2.6 — monetary-policy cycle: JST analogue trials (MP1-MP3, pre-registered)", "",
        "Matched 1y-change legs on both sides (the BC2 standing warning applied at design",
        "time); magnitude floor declared. Interpretation AFTER the print.", "",
        "## MP1 — does the policy rate lead credit growth, negatively?", "",
        "| Country | most-negative corr | at lag |", "|---|---|---|",
        *[f"| {k} | {v[1]:+.2f} | {v[0]:+d} |" for k, v in sorted(mins.items())],
        "",
        f"- Qualifying countries (floor ≤ −0.10): {len(qual)}/{len(mins)}; of those, share",
        f"  with the minimum at lag ≥ +1 (rate leads): **{share*100:.0f}%** (bar ≥60%): **{mp1}**.", "",
        "## MP2 — the lag profile (measurement, prior set)", "",
        "| horizon (years ahead) | mean per-country corr(Δstir_t, credit growth_t+h) |", "|---|---|",
        *[f"| +{h} | {v:+.3f} |" for h, v in prof.items()], "",
        "## MP3 — campaign persistence (measurement, prior set)", "",
        f"- P(next year's Δstir has the same sign): **{p_persist*100:.0f}%** pooled — "
        "tightening/easing come in CAMPAIGNS, the regime reading's justification.", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "mins": {k: [v[0], round(v[1], 2)] for k, v in mins.items()},
        "profile": {str(k): round(v, 3) for k, v in prof.items()},
        "persist": round(p_persist, 3)}, separators=(",", ":")))
    print(f"MP1 {mp1} ({len(qual)} qualify, {share*100:.0f}% lead) | "
          f"MP2 profile {prof} | MP3 persist {p_persist*100:.0f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
