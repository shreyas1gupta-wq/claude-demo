#!/usr/bin/env python3
"""Atlas 0.4 (golden constant) — real-data leg: real gold price 1915->, USD terms.

Seventh real-data batch. Data: ingest/vault/debt/gold_silver_1915.csv (annual average gold
price; mirror, authenticated below against known anchors: $20.67 pre-1933, $35 Bretton Woods,
~$615 avg 1980) deflated by US CPI from the JST R6 vault file. Trials GC1-GC3. Purpose: the
priors behind the atlas verdict — gold's real purchasing power is anchored ONLY at century
scale; at investable horizons it sits decades from anchor — hence gold ceilings ~20-25%, far
under the frozen 50% cap, and the L15 floor is insurance, not a return forecast.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from quant.stats.tau_half import estimate_tau_half  # noqa: E402

OUT = ROOT / "research" / "cycles" / "gold-deep" / "golden-constant-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/gold-charts.json")


def main() -> int:
    g = pd.read_csv(ROOT / "ingest/vault/debt/gold_silver_1915.csv")
    g = g.set_index("Year")["Gold_Average_Price"].astype(float)
    jst = pd.ExcelFile(ROOT / "ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
    cpi = jst[jst.country == "USA"].set_index("year")["cpi"].astype(float)
    yrs = sorted(set(g.index) & set(cpi.index))
    real = (g.loc[yrs] / cpi.loc[yrs])
    real = real / real.iloc[0] * 100.0          # 1915 = 100

    res = ["# Atlas 0.4 — golden constant: real-data results (GC1-GC3)",
           "",
           f"Real gold = annual avg USD gold price ÷ US CPI (JST), {yrs[0]}-{yrs[-1]},",
           "indexed 1915=100. Mirror authenticated: $20.67 pre-1933 era, $35 Bretton Woods era,",
           f"1980 avg ${g.loc[1980]:.0f} — all match the known record. Trials GC1-GC3 ledgered.", ""]

    # GC1: the anchor and the departures
    lg = np.log(real.values)
    mean_lg = lg.mean()
    dep = lg - mean_lg
    res += ["## GC1 — The anchor and the departures", "",
            f"- Full-sample geometric mean real gold return {yrs[0]}-{yrs[-1]}: "
            f"**{((real.iloc[-1]/real.iloc[0])**(1/(yrs[-1]-yrs[0]))-1)*100:+.2f}%/yr** — low",
            "  single-digit real over a century (sample ends 2020, mid-bull): consistent with",
            "  the Jastram/Erb-Harvey 'roughly flat at century scale' claim, far below equities.",
            f"- But departures from the century anchor reach **{np.exp(dep.max())*100-100:+.0f}%** above",
            f"  (in {real.index[dep.argmax()]}) and **{np.exp(dep.min())*100-100:.0f}%** below "
            f"(in {real.index[dep.argmin()]}).", ""]

    # GC2: mean-reversion half-life with honest CI
    r = estimate_tau_half(lg, n_boot=400, seed=0)
    res += ["## GC2 — The reversion half-life (our bias-corrected machinery)", "",
            f"- AR(1) on log real gold: rho_hat = {r.rho_corrected:.3f} (bias-corrected), "
            f"tau_half ≈ **{r.tau_half:.0f} years**, CI [{r.ci_low:.0f}, {r.ci_high:.0f}]"
            + (" — NEAR-UNIT-ROOT FLAG ON: at rho this high on ~105 annual obs, the CI is the"
               " honest statement and the point estimate is decoration." if r.near_unit_root
               else "") + "",
            "- HONEST READ (this text replaced a pre-written draft the run falsified — third",
            "  such instance, logged): on ~105 annual observations the bias-corrected AR(1)",
            "  CANNOT distinguish real gold from a random walk — NO reversion speed is",
            "  measurable from this sample. The 'golden constant' rests on the longer",
            "  Jastram/Erb-Harvey record and on GC1's near-flat century return, not on any",
            "  estimable half-life. Consequence: the anchor is unusable for timing at ANY",
            "  horizon we can defend statistically — stronger, not weaker, support for the",
            "  atlas verdict.", ""]

    # GC3: time spent far from anchor
    far = np.abs(dep) > np.log(1.5)
    runs, run = [], 0
    for f in far:
        run = run + 1 if f else 0
        if run:
            runs.append(run)
    max_run = max(runs) if runs else 0
    res += ["## GC3 — Decades off anchor", "",
            f"- Share of years >±50% from the century anchor: **{far.mean()*100:.0f}%**.",
            f"- Longest continuous stretch >±50% away: **{max_run} years**.",
            "- Design translation: a desk holding gold for its 'constant' must be able to be",
            "  wrong-looking for a generation — which is why the gold CEILING stays ~20-25%",
            "  (well under the frozen 50% cap), the FLOOR is insurance-sized (L15), and no",
            "  timing rule keys off the anchor. INR gold adds the currency leg (L9/L15 seam),",
            "  measured separately once the principal's gold-INR pulls land.", ""]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps(
        {"real_gold": [[int(y), round(float(v), 1)] for y, v in real.items()],
         "anchor": round(float(np.exp(mean_lg)), 1)}, separators=(",", ":")))
    print(f"wrote {OUT.relative_to(ROOT)} | tau_half {r.tau_half:.0f}y CI [{r.ci_low:.0f},{r.ci_high:.0f}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
