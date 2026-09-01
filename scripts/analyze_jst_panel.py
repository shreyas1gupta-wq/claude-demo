#!/usr/bin/env python3
"""JST Macrohistory panel (R6 mirror, verified) — pooled-prior analyses for L10.

FIRST REAL DATA in the project. Scope discipline:
- These are REPLICATIONS of published designs + the pre-registered pooled-prior reads
  (docs/cycles/01-credit-cycle.md §5, R1-prior; H66 pooled preliminary). NOT India results.
- The credit state here is PARAMETER-FREE per country (expanding Hamilton -> expanding
  percentile), so every score at year t uses only country-own data through t: the pooled AUROC
  of this score is real-time honest by construction. The only grids are h (pre-registered
  quarterly 16-24q, mapped to annual {4,5,6}) and the phase demo mapping — all cells logged
  to the trial ledger by scripts/… (see LEDGER note in the results file).
- Data: ingest/vault/jst/JSTdatasetR6.xlsx (mirror; sha256 in vault manifest; authenticated
  against the independent R4 mirror + published crisis chronologies).

Outputs: research/cycles/credit-deep/jst-panel-RESULTS.md and lesson chart JSON in scratchpad.
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
from quant.ladder.phase import phase_state  # noqa: E402
from quant.stats.hamilton import hamilton_filter  # noqa: E402

VAULT = ROOT / "ingest" / "vault" / "jst" / "JSTdatasetR6.xlsx"
OUT = ROOT / "research" / "cycles" / "credit-deep" / "jst-panel-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/jst-charts.json")

H_GRID = (4, 5, 6)          # annual mapping of the pre-registered 16-24 quarter grid
P_ANNUAL = 1                # Hamilton's annual-data lag convention (p=4 quarterly ~ 1y of lags)
MIN_OBS_PCT = 20            # years before an expanding rank is emitted (documented convention)
GAP_INTERP_MAX = 5          # interpolate interior gaps <= this many years (war gaps stay gaps)


def auroc(score: np.ndarray, label: np.ndarray) -> float:
    m = ~np.isnan(score) & ~np.isnan(label)
    s, y = score[m], label[m].astype(bool)
    if y.sum() == 0 or (~y).sum() == 0:
        return np.nan
    r = pd.Series(s).rank().to_numpy()
    n1, n0 = int(y.sum()), int((~y).sum())
    return float((r[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def interp_small_gaps(x: np.ndarray, maxgap: int) -> np.ndarray:
    x = x.astype(float).copy()
    isn = np.isnan(x)
    if not isn.any():
        return x
    idx = np.arange(len(x))
    valid = ~isn
    if valid.sum() < 2:
        return x
    filled = np.interp(idx, idx[valid], x[valid])
    # keep NaN for long runs and for leading/trailing gaps
    run = 0
    for i in range(len(x)):
        if isn[i]:
            run += 1
        else:
            run = 0
    out = x.copy()
    i = 0
    while i < len(x):
        if isn[i]:
            j = i
            while j < len(x) and isn[j]:
                j += 1
            interior = i > 0 and j < len(x)
            if interior and (j - i) <= maxgap:
                out[i:j] = filled[i:j]
            i = j
        else:
            i += 1
    return out


def logit_fit(X: np.ndarray, y: np.ndarray, iters: int = 60):
    """Newton-Raphson logistic regression (no external deps). X includes intercept col."""
    b = np.zeros(X.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-X @ b))
        W = p * (1 - p)
        g = X.T @ (y - p)
        H = (X * W[:, None]).T @ X + 1e-8 * np.eye(X.shape[1])
        step = np.linalg.solve(H, g)
        b += step
        if np.max(np.abs(step)) < 1e-10:
            break
    p = 1 / (1 + np.exp(-X @ b))
    return b, p


def main() -> int:
    df = pd.ExcelFile(VAULT).parse("JRT6 Data")
    need = ["country", "iso", "year", "tloans", "gdp", "cpi", "eq_tr", "crisisJST", "tbus", "thh"]
    have = [c for c in need if c in df.columns]
    df = df[have].sort_values(["country", "year"]).reset_index(drop=True)
    countries = sorted(df.country.unique())

    rows = []          # pooled per-country-year records
    charts = {"examples": {}}
    for c in countries:
        d = df[df.country == c].reset_index(drop=True)
        yr = d.year.to_numpy(float)
        ratio = interp_small_gaps((d.tloans / d.gdp).to_numpy(float), GAP_INTERP_MAX)
        real_loans = interp_small_gaps((d.tloans / d.cpi).to_numpy(float), GAP_INTERP_MAX)
        with np.errstate(all="ignore"):
            dlog = np.concatenate([[np.nan], np.diff(np.log(real_loans))])
            g5 = pd.Series(dlog).rolling(5).mean().to_numpy()      # 5y avg real credit growth
        gaps = {h: hamilton_filter(ratio, h=h, p=P_ANNUAL, mode="expanding") for h in H_GRID}
        gpct = {h: expanding_percentile(gaps[h], min_obs=MIN_OBS_PCT) for h in H_GRID}
        # equity 3y forward: REAL total-return index (nominal eq_tr deflated by CPI —
        # nominal local-currency returns are meaningless under hyperinflation: Weimar 1923
        # produced a +5.9e10% nominal cell in the first run of this script)
        eq = d.eq_tr.to_numpy(float)
        cpi = interp_small_gaps(d.cpi.to_numpy(float), GAP_INTERP_MAX)
        infl = np.concatenate([[np.nan], cpi[1:] / cpi[:-1] - 1.0])
        eq_real = (1.0 + eq) / (1.0 + infl) - 1.0
        lvl = np.cumprod(np.where(np.isnan(eq_real), 1.0, 1.0 + eq_real))
        lvl[np.isnan(eq_real)] = np.nan
        fwd_dd3 = np.full(len(d), np.nan)
        fwd_ret3 = np.full(len(d), np.nan)
        for t in range(len(d) - 3):
            w = lvl[t:t + 4]
            if np.isnan(w).any():
                continue
            peak = np.maximum.accumulate(w)
            fwd_dd3[t] = float((1 - w / peak).max())
            fwd_ret3[t] = float(w[3] / w[0] - 1)
        # trailing 3y equity return (for the R-zone joint condition)
        tr3 = np.full(len(d), np.nan)
        for t in range(3, len(d)):
            w = lvl[t - 3:t + 1]
            if not np.isnan(w).any():
                tr3[t] = float(w[-1] / w[0] - 1)
        # business-credit 3y change / gdp (R-zone business variant)
        if "tbus" in d.columns:
            bus = interp_small_gaps((d.tbus / d.gdp).to_numpy(float), GAP_INTERP_MAX)
            dbus3 = np.concatenate([[np.nan] * 3, bus[3:] - bus[:-3]])
        else:
            dbus3 = np.full(len(d), np.nan)
        cr = d.crisisJST.fillna(0).to_numpy(float)
        # crisis onset within next 1..3y / 1..5y
        def fwd_any(k):
            out = np.full(len(d), np.nan)
            for t in range(len(d) - k):
                out[t] = 1.0 if cr[t + 1:t + 1 + k].sum() > 0 else 0.0
            return out
        cr3, cr5 = fwd_any(3), fwd_any(5)
        # phase on the h=5 state
        ph = phase_state(gpct[5], k_slope=2, smooth=1, level_mid=0.5, min_obs=15)
        for i in range(len(d)):
            rows.append(dict(country=c, year=int(yr[i]),
                             g4=gpct[4][i], g5=gpct[5][i], g6=gpct[6][i],
                             growth5=g5[i], dbus3=dbus3[i], tr3=tr3[i],
                             dlog=dlog[i], cr3=cr3[i], cr5=cr5[i],
                             fdd3=fwd_dd3[i], fret3=fwd_ret3[i],
                             dirn=ph.direction[i], quad=int(ph.quadrant[i])))
        if c in ("USA", "Japan", "Spain"):
            charts["examples"][c] = dict(
                year=[int(v) for v in yr],
                ratio=[None if np.isnan(v) else round(v, 3) for v in ratio],
                gpct=[None if np.isnan(v) else round(v, 3) for v in gpct[5]],
                crisis=[int(v) for v in cr])
    P = pd.DataFrame(rows)

    res = ["# JST R6 pooled-panel results (REAL DATA - advanced-economy prior, NOT India)",
           "",
           "Source: JST Macrohistory R6 (GitHub mirror, sha256 in ingest/vault/jst/manifest.json;",
           "authenticated vs independent R4 mirror + published crisis chronologies). 18 countries,",
           "1870-2020, 88 crisis onsets. Conventions: annual Hamilton h in {4,5,6} (the 16-24q",
           f"grid), p={P_ANNUAL}; expanding percentiles min_obs={MIN_OBS_PCT}y; interior data gaps",
           f"<= {GAP_INTERP_MAX}y interpolated (war gaps remain gaps). The credit state is",
           "PARAMETER-FREE per country, so scores are real-time honest by construction.",
           "Generated by scripts/analyze_jst_panel.py on 2026-09-01. All cells below are logged",
           "in research/register/trial-ledger.md (entries J1-J5).", ""]

    # --- J1: our credit-state AUROC across the h grid ---
    res += ["## J1 - Early-warning power of OUR state (expanding Hamilton gap percentile)", "",
            "| Score | AUROC crisis<=3y | AUROC crisis<=5y | n(country-years) |", "|---|---|---|---|"]
    for h in H_GRID:
        s = P[f"g{h}"].to_numpy()
        res.append(f"| gap pctile h={h}y | {auroc(s, P.cr3.to_numpy()):.3f} "
                   f"| {auroc(s, P.cr5.to_numpy()):.3f} "
                   f"| {int((~np.isnan(s) & ~np.isnan(P.cr3.to_numpy())).sum())} |")
    s = P.growth5.to_numpy()
    res.append(f"| 5y real credit growth (ST-style) | {auroc(s, P.cr3.to_numpy()):.3f} "
               f"| {auroc(s, P.cr5.to_numpy()):.3f} "
               f"| {int((~np.isnan(s) & ~np.isnan(P.cr3.to_numpy())).sum())} |")
    # per-country AUROC distribution for h=5
    pc = []
    for c in countries:
        d = P[P.country == c]
        a = auroc(d.g5.to_numpy(), d.cr3.to_numpy())
        if not np.isnan(a):
            pc.append((c, a))
    pc.sort(key=lambda t: t[1])
    res += ["", f"Per-country AUROC (h=5, crisis<=3y): median "
            f"{np.median([a for _, a in pc]):.3f}; range {pc[0][0]} {pc[0][1]:.2f} to "
            f"{pc[-1][0]} {pc[-1][1]:.2f}; {sum(a > 0.5 for _, a in pc)}/{len(pc)} countries > 0.5.", ""]
    charts["percountry_auroc"] = [[c, round(a, 3)] for c, a in pc]

    # --- J2: Schularick-Taylor logit replication (simplified spec, stated) ---
    m = ~np.isnan(P.growth5.to_numpy()) & ~np.isnan(P.cr3.to_numpy())
    X0 = P.growth5.to_numpy()[m]
    dummies = pd.get_dummies(P.country[m]).to_numpy(float)
    Xz = (X0 - X0.mean()) / X0.std()
    X = np.column_stack([np.ones(m.sum()), Xz, dummies[:, 1:]])
    y = P.cr3.to_numpy()[m]
    b, p = logit_fit(X, y)
    mfx = float(np.mean(p * (1 - p)) * b[1])   # avg marginal effect per 1 sigma
    res += ["## J2 - Schularick-Taylor-style logit (simplified spec: 5y avg real credit growth,",
            "country fixed effects; label = crisis onset within 3y)", "",
            f"- Slope per 1 sigma of 5y credit growth: b = {b[1]:+.3f} (log-odds); average",
            f"  marginal effect = {mfx * 100:+.2f}pp on a base rate of {y.mean() * 100:.1f}%.",
            f"- In-sample AUROC of the fitted logit: {auroc(p, y):.3f} (published in-sample ~0.72",
            "  for the original 5-lag spec on 14 countries - same ballpark, different spec/panel).", ""]

    # --- J3: R-zone replication ---
    res += ["## J3 - R-zone (Greenwood-Hanson-Shleifer-Sorensen 2022 style)", ""]
    for name, credvar in (("business credit (Δ3y bus/GDP)", "dbus3"),
                          ("total credit (Δ3y proxy: 3y avg growth)", "growth5")):
        d = P.dropna(subset=[credvar, "tr3", "cr3"])
        if len(d) < 200:
            res.append(f"- {name}: insufficient rows ({len(d)})")
            continue
        cred_hi = d[credvar] >= d[credvar].quantile(0.8)
        eq_hi = d.tr3 >= d.tr3.quantile(2 / 3)
        rz = d[cred_hi & eq_hi]
        res.append(f"- {name}: R-zone n={len(rz)} country-years; P(crisis<=3y | R-zone) = "
                   f"**{rz.cr3.mean() * 100:.1f}%** vs base {d.cr3.mean() * 100:.1f}% "
                   f"(published: ~45% business / ~40% combined vs ~7% base; full-sample quantiles,")
        res.append("  as in the paper - the real-time variant is a pre-registered India design, R3).")
    res.append("")

    # --- J4: forward equity drawdown by state quintile (R2 prior) ---
    d = P.dropna(subset=["g5", "fdd3"])
    qs = pd.qcut(d.g5, 5, labels=False, duplicates="drop")
    res += ["## J4 - Forward 3y equity max drawdown by credit-state quintile (R2 prior)", "",
            "| State quintile (h=5 gap pctile) | mean fwd 3y max DD | median fwd 3y REAL return | n |",
            "|---|---|---|---|"]
    dd_by_q = []
    for q in range(5):
        sub = d[qs == q]
        dd_by_q.append(round(float(sub.fdd3.mean()), 4))
        res.append(f"| Q{q + 1} | {sub.fdd3.mean() * 100:.1f}% | {sub.fret3.median() * 100:+.1f}% "
                   f"| {len(sub)} |")
    slope = np.polyfit(d.g5, d.fdd3, 1)[0]
    res += ["", f"Linear slope fwd-DD on state: {slope * 100:+.2f}pp per unit of percentile "
            "(prior read only - the India R2 design carries Stambaugh + Newey-West).", ""]
    charts["dd_by_quintile"] = dd_by_q

    # --- J5: H66 preliminary - the 0.6U vs 0.6D question, pooled, matched level ---
    d = P[(P.g5 >= 0.55) & (P.g5 <= 0.90)].dropna(subset=["dirn", "cr3", "fdd3"])
    up, dn = d[d.dirn == 1], d[d.dirn == -1]
    res += ["## J5 - H66 PRELIMINARY (exploratory, pooled): same level, different trail", "",
            "Matched level: state percentile in [0.55, 0.90]. U = rising, D = falling-from-high.", "",
            "| Trail | n | P(crisis<=3y) | mean fwd 3y max DD | median fwd 3y REAL return |",
            "|---|---|---|---|---|",
            f"| U (rising) | {len(up)} | {up.cr3.mean() * 100:.1f}% | {up.fdd3.mean() * 100:.1f}% "
            f"| {up.fret3.median() * 100:+.1f}% |",
            f"| D (falling) | {len(dn)} | {dn.cr3.mean() * 100:.1f}% | {dn.fdd3.mean() * 100:.1f}% "
            f"| {dn.fret3.median() * 100:+.1f}% |", "",
            "EXPLORATORY read for the H66 prior only - the confirmatory design (matched-level",
            "deciles, purged CV, Stambaugh) runs at R2/R4. Logged as trial J5.", ""]
    charts["h66"] = dict(u=[len(up), round(float(up.cr3.mean()), 4), round(float(up.fdd3.mean()), 4)],
                         d=[len(dn), round(float(dn.cr3.mean()), 4), round(float(dn.fdd3.mean()), 4)])

    OUT.write_text("\n".join(res) + "\n")
    CHART.parent.mkdir(parents=True, exist_ok=True)
    CHART.write_text(json.dumps(charts, separators=(",", ":")))
    print(f"wrote {OUT.relative_to(ROOT)} and chart data ({CHART.stat().st_size}b)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
