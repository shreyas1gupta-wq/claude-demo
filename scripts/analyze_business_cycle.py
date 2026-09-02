#!/usr/bin/env python3
"""Atlas 2.3 (business cycle proper) — analogue trials BC1-BC3, PRE-REGISTERED.

BC1: growth-cycle spacing (state = expanding percentile of Hamilton gap of log rgdpmad,
h=2y, p=1; extrema min_gap 2y). Bar: pooled median spacing in [3,6]y AND >=50% in [3,7]y.
BC2: the imported "credit leads growth" direction — per country, peak cross-correlation lag
between the credit gap (h=5) and the GDP gap (h=2), lags -5..+5 (positive = credit leads).
Bar: >=60% of countries (>=60 overlapping years) peak at lag >= +1.
BC3: growth-state persistence P(same side of 0.5 next year), pooled. Measurement, no bar.
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

OUT = ROOT / "research" / "cycles" / "buscycle-deep" / "buscycle-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/buscycle-charts.json")


def extrema_peaks(series: pd.Series, min_gap: int = 2):
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
    df = df[["iso", "year", "rgdpmad", "tloans", "gdp"]].sort_values(["iso", "year"])

    spacings, lead_lags, stay = [], {}, []
    paths = {}
    for iso, d in df.groupby("iso"):
        d = d.set_index("year")
        lg = np.log(d.rgdpmad.astype(float))
        if lg.notna().sum() < 40:
            continue
        gdp_gap = pd.Series(hamilton_filter(lg.to_numpy(), h=2, p=1, mode="expanding"),
                            index=d.index)
        state = pd.Series(expanding_percentile(gdp_gap.to_numpy(), min_obs=20), index=d.index)
        pks = extrema_peaks(state.dropna())
        spacings += [b - a for a, b in zip(pks, pks[1:])]
        s = state.dropna()
        side = (s > 0.5).astype(int)
        stay += (side.diff().fillna(0) == 0).iloc[1:].tolist()
        # BC2: credit gap vs GDP gap cross-correlation
        ratio = (d.tloans / d.gdp).astype(float)
        cr_gap = pd.Series(hamilton_filter(ratio.to_numpy(), h=5, p=1, mode="expanding"),
                           index=d.index)
        j = pd.concat([cr_gap, gdp_gap], axis=1, keys=["c", "g"]).dropna()
        if len(j) >= 60:
            cors = {}
            for lag in range(-5, 6):
                x = pd.concat([j.c.shift(lag), j.g], axis=1).dropna()
                cors[lag] = float(x.corr().iloc[0, 1])
            lead_lags[iso] = max(cors, key=lambda k: cors[k])
        if iso in ("USA", "JPN", "DEU", "GBR"):
            paths[iso] = [[int(y), None if np.isnan(v) else round(float(v), 3)]
                          for y, v in state.items()]

    med = float(np.median(spacings))
    share37 = np.mean([3 <= x <= 7 for x in spacings])
    bc1 = "PASS" if (3 <= med <= 6 and share37 >= 0.5) else "FAIL"
    leads = [v for v in lead_lags.values()]
    share_lead = np.mean([v >= 1 for v in leads])
    bc2 = "PASS" if share_lead >= 0.6 else "FAIL"
    p_stay = float(np.mean(stay))

    res = [
        "# Atlas 2.3 — business cycle: JST analogue trials (BC1-BC3, pre-registered)", "",
        "State: expanding Hamilton gap of log real GDP per capita (h=2y — the short-cycle band's",
        "own h, declared at registration), expanding percentiles. Bars fixed before running;",
        "interpretation AFTER the print.", "",
        "## BC1 — growth-cycle spacing vs the 4-5y claim", "",
        f"- n = {len(spacings)} peak-to-peak spacings; median **{med:.0f}y**, "
        f"IQR {np.percentile(spacings,25):.0f}-{np.percentile(spacings,75):.0f}y; "
        f"share in [3,7]y: **{share37*100:.0f}%**.",
        f"- Bar (median in [3,6] AND ≥50% in [3,7]): **{bc1}**.", "",
        "## BC2 — does the credit gap LEAD the GDP gap on its home panel?", "",
        "| Country | peak cross-corr lag (+ = credit leads, years) |", "|---|---|",
        *[f"| {k} | {v:+d} |" for k, v in sorted(lead_lags.items())],
        "",
        f"- Share with peak lag ≥ +1y: **{share_lead*100:.0f}%** of {len(leads)} "
        f"(bar ≥60%): **{bc2}**.", "",
        "## BC3 — growth-state persistence (measurement, prior set)", "",
        f"- P(state stays on the same side of 0.5 next year), pooled: **{p_stay*100:.0f}%**.", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "spacings": sorted(spacings), "lead_lags": lead_lags,
        "p_stay": round(p_stay, 3), "paths": paths}, separators=(",", ":")))
    print(f"BC1 {bc1} (med {med:.0f}y, {share37*100:.0f}% in [3,7]) | "
          f"BC2 {bc2} ({share_lead*100:.0f}% lead) | BC3 stay {p_stay*100:.0f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
