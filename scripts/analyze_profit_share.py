#!/usr/bin/env python3
"""Atlas 2.15 — PS1-PS3, PRE-REGISTERED: capital-share (1 - labsh) reversion on PWT 10.0.

PS1: per country (>=50 obs), corr(level_t, next-10y change); bar >=70% negative.
PS2: pooled P(next-10y change < 0 | level in top quintile of own EXPANDING history) vs
unconditional; bar: conditional >= unconditional + 15pp.
PS3: India's path + 2019 own-history percentile (measurement).
Proxy caveat stated: macro capital share, broader than corporate profits/GDP.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "profitshare-deep" / "profitshare-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/profitshare-charts.json")


def main() -> int:
    d = pd.read_csv(ROOT / "ingest/vault/macro/pwt100.csv")
    lab = [c for c in d.columns if "labour compensation" in c][0]
    d["cap"] = 1.0 - d[lab].astype(float) / 100.0

    corrs, cond_hits, cond_n, unc_hits, unc_n = {}, 0, 0, 0, 0
    paths = {}
    for c, g in d.groupby("Entity"):
        s = g.set_index("Year")["cap"].dropna().sort_index()
        if len(s) < 50:
            continue
        chg10 = s.shift(-10) - s
        j = pd.concat([s, chg10], axis=1, keys=["lvl", "chg"]).dropna()
        if len(j) < 30:
            continue
        corrs[c] = float(j.corr().iloc[0, 1])
        # expanding top-quintile flag (min 20 ranks)
        ranks = s.expanding(min_periods=20).apply(
            lambda w: (w <= w.iloc[-1]).mean(), raw=False)
        top = ranks.reindex(j.index) >= 0.8
        unc_hits += int((j.chg < 0).sum()); unc_n += len(j)
        cond_hits += int((j.chg[top.fillna(False)] < 0).sum())
        cond_n += int(top.fillna(False).sum())
        if c in ("United States", "India", "Japan", "Germany"):
            paths[c] = [[int(y), round(float(v), 3)] for y, v in s.items()]

    neg_share = np.mean([v < 0 for v in corrs.values()])
    ps1 = "PASS" if neg_share >= 0.7 else "FAIL"
    p_cond = cond_hits / max(cond_n, 1)
    p_unc = unc_hits / max(unc_n, 1)
    ps2 = "PASS" if p_cond >= p_unc + 0.15 else "FAIL"

    ind = d[d.Entity == "India"].set_index("Year")["cap"].dropna().sort_index()
    ind_pct = float((ind <= ind.loc[2019]).mean())

    res = [
        "# Atlas 2.15 — profit-share cycle: PWT capital-share trials (PS1-PS3, pre-registered)", "",
        "Proxy: macro capital share (1 − labsh) — BROADER than corporate profits/GDP; the",
        "reversion question transfers partially, the level does not. Vault authenticated",
        "(PA1a/b pass; PA1c marginal miss recorded).", "",
        "## PS1 — level → next-decade change", "",
        f"- {len(corrs)} countries (≥50 obs): **{neg_share*100:.0f}% negative** "
        f"(bar ≥70%): **{ps1}**. Median corr {np.median(list(corrs.values())):+.2f}.", "",
        "## PS2 — the extremes condition", "",
        f"- P(next-10y change < 0): unconditional **{p_unc*100:.0f}%** (n={unc_n}); "
        f"top-quintile-of-own-history **{p_cond*100:.0f}%** (n={cond_n}).",
        f"- Bar (conditional ≥ unconditional + 15pp): **{ps2}**.", "",
        "## PS3 — India (measurement, prior set)", "",
        f"- India capital share 2019: **{ind.loc[2019]:.3f}**, its own-history percentile "
        f"**{ind_pct*100:.0f}th** (1950-2019). Path in the chart file. The 2019-24 listed-",
        "  corporate tripling is POST-sample and enters via the record, never spliced.", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "corrs": {k: round(v, 2) for k, v in sorted(corrs.items())},
        "p_unc": round(p_unc, 3), "p_cond": round(p_cond, 3),
        "paths": paths, "india_2019_pct": round(ind_pct, 2)},
        separators=(",", ":")))
    print(f"PS1 {ps1} ({neg_share*100:.0f}% neg of {len(corrs)}) | "
          f"PS2 {ps2} ({p_cond*100:.0f}% vs {p_unc*100:.0f}%) | "
          f"PS3 India 2019 cap {ind.loc[2019]:.3f} @ {ind_pct*100:.0f}th pct")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
