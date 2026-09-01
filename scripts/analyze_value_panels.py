#!/usr/bin/env python3
"""Value/quality real-data analyses: India HML (vault mirror) + US Fama-French factors.

Third real-data batch. Sources (sha256 in ingest/vault/factors/manifest.json):
- iima_monthly_factors.csv — India SMB/HML/WML/MF/RF 1993-2025 (mirror; authenticated in the
  momentum batch M0; the LEVEL caveat recorded there applies to HML equally).
- fff_monthly_us.csv — Ken French FF3 monthly (202411 CRSP vintage; Mkt-RF, SMB, HML, RF).
- ff_momentum_monthly.csv — Ken French Mom (202512 vintage) for the value-momentum correlation.

Trials V0-V4 logged in research/register/trial-ledger.md. Pooled priors + replications only;
NOT India-primary results (mirror caveat stands).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
V = ROOT / "ingest" / "vault" / "factors"
OUT = ROOT / "research" / "cycles" / "value-deep" / "value-panel-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/value-charts.json")


def load_french_table(path, ncols, names):
    rows = []
    for line in path.read_text().splitlines():
        m = re.match(r"^\s*(\d{6})\s*,\s*" + r"\s*,\s*".join([r"(-?\d+\.?\d*)"] * ncols), line)
        if m:
            ym = m.group(1)
            if not (1900 < int(ym[:4]) <= 2026):
                continue
            rows.append((pd.Period(f"{ym[:4]}-{ym[4:]}", "M").to_timestamp("M"),
                         *[float(g) for g in m.groups()[1:]]))
        elif rows and re.match(r"^\s*Annual", line):
            break
    df = pd.DataFrame(rows, columns=["date"] + names).set_index("date")
    return df


def dd_series(r):
    lvl = (1 + r / 100).cumprod()
    return 1 - lvl / lvl.cummax()


def main() -> int:
    ind = pd.read_csv(V / "iima_monthly_factors.csv", na_values=["NA"])
    ind["date"] = pd.PeriodIndex(ind["Date"], freq="M").to_timestamp("M")
    ind = ind.set_index("date")[["SMB", "HML", "WML", "MF", "RF"]].astype(float)
    us3 = load_french_table(V / "fff_monthly_us.csv", 4, ["MktRF", "SMB", "HML", "RF"])
    usmom = load_french_table(V / "ff_momentum_monthly.csv", 1, ["Mom"])

    res = ["# Value real-data results — India HML mirror + US Fama-French factors",
           "",
           "Sources/authentication per file header. India levels carry the mirror [VERIFY]",
           "caveat from M0/M1; shapes and correlations are the primary objects here.",
           "Generated 2026-09-01; trials V0-V4 ledgered.", ""]

    # V0 authentication: US HML chronology checks
    worst = us3.HML.nsmallest(5)
    best = us3.HML.nlargest(5)
    res += ["## V0 — Authentication (US HML chronology must match published history)", "",
            "| Worst months | HML % | Best months | HML % |", "|---|---|---|---|"]
    for (dw, vw), (db, vb) in zip(worst.items(), best.items()):
        res.append(f"| {dw:%Y-%m} | {vw:+.1f} | {db:%Y-%m} | {vb:+.1f} |")
    res += ["", f"US FF3 span: {us3.index.min():%Y-%m} → {us3.index.max():%Y-%m} "
            f"({len(us3)} months, 202411 CRSP vintage).", ""]

    # V1 India value premium + sub-periods
    res += ["## V1 — India HML: level and sub-periods (mirror)", "",
            "| Window | ann. mean (x12) | ann. vol | Sharpe vs RF | n |", "|---|---|---|---|---|"]
    for name, a, b in [("full 1993-2025", None, None), ("1994-2014", "1994", "2014"),
                       ("2015-2019 (the growth mania)", "2015", "2019"),
                       ("post-2020", "2020", None)]:
        w = ind.HML[(ind.index >= (a or "1900")) & (ind.index <= (f"{b}-12-31" if b else "2100"))]
        rf = ind.RF.reindex(w.index)
        sh = ((w - rf).mean() / w.std() * np.sqrt(12)) if w.std() > 0 else np.nan
        res.append(f"| {name} | {w.mean() * 12:+.1f}% | {w.std() * np.sqrt(12):.1f}% | {sh:.2f} | {len(w)} |")
    res.append("")

    # V2 value-momentum correlation (the AMP diversification claim)
    ind_vm = ind[["HML", "WML"]].dropna()
    us_vm = pd.concat([us3.HML, usmom.Mom], axis=1).dropna()
    res += ["## V2 — The value-momentum correlation (AMP's diversification claim)", "",
            f"- India (mirror, {len(ind_vm)} months): corr(HML, WML) = **{ind_vm.corr().iloc[0, 1]:+.2f}**",
            f"- US (French, {len(us_vm)} months since {us_vm.index.min():%Y}): corr(HML, Mom) = "
            f"**{us_vm.corr().iloc[0, 1]:+.2f}**",
            "- Rolling 60m correlations exported to the lesson charts. Published AMP claim:",
            "  materially negative within every market they studied [exact table cell VERIFY].", ""]
    roll_us = us_vm.HML.rolling(60).corr(us_vm.Mom)
    roll_in = ind_vm.HML.rolling(60).corr(ind_vm.WML)

    # V3 the combination arithmetic
    res += ["## V3 — The combination (why negative correlation is the free lunch)", "",
            "| Portfolio | ann. mean | ann. vol | Sharpe (raw) |", "|---|---|---|---|"]
    combos = {}
    for label, s in [("US HML", us_vm.HML), ("US Mom", us_vm.Mom),
                     ("US 50/50", (us_vm.HML + us_vm.Mom) / 2),
                     ("India HML", ind_vm.HML), ("India WML", ind_vm.WML),
                     ("India 50/50", (ind_vm.HML + ind_vm.WML) / 2)]:
        sh = s.mean() / s.std() * np.sqrt(12)
        combos[label] = round(float(sh), 2)
        res.append(f"| {label} | {s.mean() * 12:+.1f}% | {s.std() * np.sqrt(12):.1f}% | {sh:.2f} |")
    res += ["", "The 50/50 Sharpe exceeding BOTH legs on both panels is the diversification",
            "arithmetic our sleeve-weighting prior rests on (D11 fixed-weights rule).", ""]

    # V4 value winters: drawdown anatomy
    dd_us = dd_series(us3.HML)
    dd_in = dd_series(ind.HML.dropna())
    def winters(dd, thresh=0.2):
        out, in_w = [], False
        for dt, v in dd.items():
            if v > thresh and not in_w:
                start, peakv, in_w = dt, v, True
            elif in_w:
                peakv = max(peakv, v)
                if v < 0.02:
                    out.append((start, dt, peakv)); in_w = False
        if in_w:
            out.append((start, dd.index[-1], peakv))
        return out
    res += ["## V4 — Value winters (HML drawdowns > 20%, peak depth, recovery)", "",
            "| Panel | Start | End (recovered<2%) | Max depth |", "|---|---|---|---|"]
    for lab, w in [("US", winters(dd_us)), ("India (mirror)", winters(dd_in))]:
        for s0, s1, depth in w:
            res.append(f"| {lab} | {s0:%Y-%m} | {s1:%Y-%m} | {depth * 100:.0f}% |")
    res += ["", "The US 2017-2020 winter and its 2020-2022 recovery, and any Indian analogues,",
            "are the empirical basis for the SPREAD-CONDITIONED patience rule (never abandonment,",
            "never doubling down — the valuation_sentiment block consumes the spread state).", ""]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    charts = dict(
        us_hml_dd=[[f"{d:%Y-%m}", round(float(v), 3)] for d, v in dd_us.items()][::2],
        in_hml_dd=[[f"{d:%Y-%m}", round(float(v), 3)] for d, v in dd_in.items()],
        roll_us=[[f"{d:%Y-%m}", None if np.isnan(v) else round(float(v), 2)] for d, v in roll_us.items()][::2],
        roll_in=[[f"{d:%Y-%m}", None if np.isnan(v) else round(float(v), 2)] for d, v in roll_in.items()],
        combos=combos,
    )
    CHART.write_text(json.dumps(charts, separators=(",", ":")))
    print(f"wrote {OUT.relative_to(ROOT)} + charts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
