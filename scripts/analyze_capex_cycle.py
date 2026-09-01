#!/usr/bin/env python3
"""Atlas 1.6 (capex cycle, seat L11) — analogue real-data leg. Trials IN1-IN3, PRE-REGISTERED.

IN1: expanding capex state (Hamilton gap of iy, h=5,p=1 -> expanding percentile, min_obs 20)
vs FORWARD 5y cumulative real equity return, per country. Bar: >=70% of countries (>=40
overlapping years) negative.
IN2: post-peak repair — years for iy to regain each peak (extrema min_gap 8y; censored spells
counted at censoring value, stated). Bar: median >= 4y.
IN3: pooled forward-5y mean real equity return, top vs bottom capex-state quintile.
Measurement only (prior set) — records what the analogue panel says about the clamp.
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

OUT = ROOT / "research" / "cycles" / "capex-deep" / "capex-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/capex-charts.json")


def peaks_of(series: pd.Series, min_gap: int = 8):
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
    df = df[["country", "iso", "year", "iy"]].sort_values(["iso", "year"])
    rr = pd.read_csv(ROOT / "ingest/vault/debt/jst_real_returns.csv", comment="#")

    corrs, states_all, fwd_all, repair, paths = {}, [], [], [], {}
    for iso, d in df.groupby("iso"):
        d = d.set_index("year")
        iy = d.iy.astype(float)
        if iy.notna().sum() < 40:
            continue
        gap = pd.Series(hamilton_filter(iy.to_numpy(), h=5, p=1, mode="expanding"), index=d.index)
        state = pd.Series(expanding_percentile(gap.to_numpy(), min_obs=20), index=d.index)
        r = rr[rr.iso == iso].set_index("year").equity.astype(float)
        logr = np.log1p(r)
        fwd5 = pd.Series(
            [logr.reindex(range(y + 1, y + 6)).sum(min_count=5) for y in state.index],
            index=state.index)
        j = pd.concat([state, fwd5], axis=1, keys=["s", "f"]).dropna()
        if len(j) >= 40:
            corrs[iso] = float(j.corr().iloc[0, 1])
            states_all += j.s.tolist()
            fwd_all += j.f.tolist()
        # IN2 repair spells on the raw iy level
        for pk in peaks_of(iy.dropna()):
            level = iy.loc[pk]
            later = iy.loc[pk + 1:]
            reg = later[later >= level]
            if len(reg):
                repair.append((iso, pk, int(reg.index[0] - pk), False))
            elif len(later):
                repair.append((iso, pk, int(later.index[-1] - pk), True))
        if iso in ("IND",):  # no India in JST; kept explicit for the record
            pass
        if iso in ("USA", "JPN", "KOR", "ESP"):
            paths[iso] = [[int(y), None if np.isnan(v) else round(float(v), 3)]
                          for y, v in state.items()]

    neg_share = np.mean([v < 0 for v in corrs.values()])
    reps = [t for _, _, t, _ in repair]
    cens = sum(1 for *_, c in repair if c)
    med_rep = float(np.median(reps))

    s = np.array(states_all); f = np.array(fwd_all)
    q_hi, q_lo = np.quantile(s, 0.8), np.quantile(s, 0.2)
    top = float(np.mean(f[s >= q_hi])); bot = float(np.mean(f[s <= q_lo]))
    mid = float(np.mean(f[(s > q_lo) & (s < q_hi)]))

    res = [
        "# Atlas 1.6 — capex cycle (L11): analogue results, JST R6 (IN1-IN3, pre-registered)", "",
        "India official series are proxy-blocked here; per the atlas's own 'C→B via analogues'",
        "clause these trials run on the 18-country JST iy panel + vaulted real equity returns.",
        "Bars pre-registered; interpretation AFTER the print.", "",
        "## IN1 — capex state → forward 5y real equity return", "",
        "| Country | corr(state, fwd 5y log real return) |", "|---|---|",
        *[f"| {k} | {v:+.2f} |" for k, v in sorted(corrs.items())],
        "",
        f"- Sign-consistency: **{neg_share*100:.0f}% negative** of {len(corrs)} countries "
        f"(bar ≥70%): **{'PASS' if neg_share >= 0.7 else 'FAIL'}**.", "",
        "## IN2 — post-peak repair length (iy regaining its peak)", "",
        f"- {len(repair)} peak spells; median repair **{med_rep:.0f}y** "
        f"({cens} censored spells counted at censoring value, as pre-stated);",
        f"  IQR {np.percentile(reps,25):.0f}-{np.percentile(reps,75):.0f}y.",
        f"- Bar (median ≥ 4y): **{'PASS' if med_rep >= 4 else 'FAIL'}**.", "",
        "## IN3 — quintile asymmetry (measurement, prior set — informs the clamp)", "",
        f"- Pooled mean forward-5y log real return: top-quintile capex state **{top:+.3f}**,",
        f"  middle **{mid:+.3f}**, bottom-quintile **{bot:+.3f}** "
        f"(n = {int((s>=q_hi).sum())}/{int(((s>q_lo)&(s<q_hi)).sum())}/{int((s<=q_lo).sum())} country-years).", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "corrs": {k: round(v, 2) for k, v in corrs.items()},
        "repair": sorted(reps), "quintiles": {"top": round(top, 3), "mid": round(mid, 3),
                                              "bot": round(bot, 3)},
        "paths": paths}, separators=(",", ":")))
    print(f"IN1 {'PASS' if neg_share>=0.7 else 'FAIL'} ({neg_share*100:.0f}% neg of {len(corrs)}) | "
          f"IN2 {'PASS' if med_rep>=4 else 'FAIL'} (median {med_rep:.0f}y, {cens} censored) | "
          f"IN3 top {top:+.3f} vs bot {bot:+.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
