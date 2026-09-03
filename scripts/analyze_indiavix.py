"""CW-D1v + F5a — the India VIX vault's two registered partials, run exactly as registered.

Registrations (trial-ledger.md, 2026-09-03, committed BEFORE this ran):
- CW-D1v: |Δlog VIX| on budget-day ±1 window days vs all other days, one-sided
  Mann-Whitney (elevated), p < 0.05. Events = canonical BUDGET_DAYS ∩ vault span (15).
  Secondary (descriptive, no bar): signed mean Δlog VIX by day −1 / 0 / +1.
- F5a: REDUNDANCY bar Spearman(IV pctile, RV pctile) ≥ 0.80; ADDS bar
  AUROC(IV→episodes) ≥ AUROC(RV→episodes) + 0.03 on joint days; episodes = frozen §3
  in-span ∩ joint span. VRP proxy descriptive only: IV² − 252·(21d daily std)²
  = (close/100)² − realized_vol(r,21)² (realized_vol is annualized, so the two forms
  are identical).
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import realized_vol
from quant.stats.metrics import auroc

ROOT = Path(__file__).resolve().parents[1]

# canonical list copied verbatim from scripts/analyze_nifty_daily.py (single source of record)
BUDGET_DAYS = [
    "2008-02-29", "2009-02-16", "2009-07-06", "2010-02-26", "2011-02-28", "2012-03-16",
    "2013-02-28", "2014-02-17", "2014-07-10", "2015-02-28", "2016-02-29", "2017-02-01",
    "2018-02-01", "2019-02-01", "2019-07-05", "2020-02-01", "2021-02-01", "2022-02-01",
    "2023-02-01", "2024-02-01", "2024-07-23", "2025-02-01", "2026-02-01",
]

EPISODES = [  # frozen §3 in-span subset, copied verbatim from scripts/analyze_nifty_daily.py
    ("Jan-2008 crash", "2008-01-01", "2008-02-15"),
    ("GFC core", "2008-09-01", "2008-11-30"),
    ("EU/downgrade 2011", "2011-08-01", "2011-11-30"),
    ("Taper tantrum", "2013-05-01", "2013-09-30"),
    ("China deval 2015", "2015-08-01", "2015-09-30"),
    ("Demonetization", "2016-11-08", "2016-11-30"),
    ("Feb-2018 vol+LTCG", "2018-02-01", "2018-03-31"),
    ("IL&FS", "2018-09-01", "2018-10-31"),
    ("COVID crash", "2020-02-20", "2020-04-30"),
    ("Russia 2022", "2022-02-01", "2022-03-31"),
    ("Election day 2024", "2024-06-04", "2024-06-10"),
    ("INR/FII May-2026", "2026-05-01", "2026-06-30"),
]

vix = pd.read_csv(ROOT / "ingest/vault/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"])
vix = vix.sort_values("date").reset_index(drop=True)
vix["dlv"] = np.log(vix["close"]).diff()
print(f"India VIX: {vix['date'].min():%Y-%m-%d}..{vix['date'].max():%Y-%m-%d} n={len(vix)}")

# ---------------- CW-D1v ----------------
in_span = [d for d in pd.to_datetime(BUDGET_DAYS)
           if vix["date"].min() <= d <= vix["date"].max()]
print(f"\nCW-D1v: budget events in span = {len(in_span)} "
      f"({in_span[0]:%Y-%m-%d} .. {in_span[-1]:%Y-%m-%d})")

idx_of = {d: i for i, d in enumerate(vix["date"])}
win_idx: set[int] = set()
day_groups = {-1: [], 0: [], +1: []}
for b in in_span:
    if b not in idx_of:
        print(f"  NOTE: {b:%Y-%m-%d} not a trading row — skipped (unexpected; Saturdays present)")
        continue
    i = idx_of[b]
    for off in (-1, 0, +1):
        j = i + off
        if 1 <= j < len(vix):          # j>=1 so dlv exists
            win_idx.add(j)
            day_groups[off].append(vix["dlv"].iloc[j])

dlv = vix["dlv"].to_numpy()
mask_win = np.zeros(len(vix), bool)
mask_win[list(win_idx)] = True
on = np.abs(dlv[mask_win])
off_ = np.abs(dlv[~mask_win & ~np.isnan(dlv)])
u, p = stats.mannwhitneyu(on, off_, alternative="greater")
print(f"CW-D1v PRIMARY: |dlogVIX| budget±1 (n={len(on)}) median {np.median(on):.4f} vs "
      f"other days (n={len(off_)}) median {np.median(off_):.4f}; one-sided MW p = {p:.4f} "
      f"-> {'PASS' if p < 0.05 else 'FAIL'} (bar p<0.05)")
for off in (-1, 0, +1):
    g = np.array(day_groups[off])
    print(f"  descriptive day {off:+d}: mean dlogVIX {np.nanmean(g):+.4f}, "
          f"median {np.nanmedian(g):+.4f} (n={len(g)})")

# ---------------- F5a ----------------
nifty = pd.read_csv(ROOT / "ingest/vault/index/nifty50_daily_2007_2026.csv",
                    parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
nifty["ret"] = nifty["Close"].pct_change()
nifty = nifty.dropna(subset=["ret"]).reset_index(drop=True)   # house convention: realized_vol
rv = realized_vol(nifty["ret"].to_numpy(), 21)          # takes a clean return series
rv_p = expanding_percentile(rv, min_obs=252)            # full NIFTY history, as registered
iv_p = expanding_percentile(vix["close"].to_numpy(), min_obs=252)

a = pd.DataFrame({"date": nifty["Date"], "rv": rv, "rv_p": rv_p})
b = pd.DataFrame({"date": vix["date"], "iv": vix["close"], "iv_p": iv_p})
j = a.merge(b, on="date", how="inner").dropna(subset=["rv_p", "iv_p"]).reset_index(drop=True)
print(f"\nF5a: joint days with both percentiles = {len(j)} "
      f"({j['date'].min():%Y-%m-%d} .. {j['date'].max():%Y-%m-%d})")

rho, _ = stats.spearmanr(j["iv_p"], j["rv_p"])
print(f"F5a REDUNDANCY: Spearman(iv_p, rv_p) = {rho:.3f} "
      f"-> {'REDUNDANT (bar >= 0.80 fired)' if rho >= 0.80 else 'not redundant by rank corr'}")

label = np.zeros(len(j))
covered = []
for name, s0, s1 in EPISODES:
    m = (j["date"] >= s0) & (j["date"] <= s1)
    if m.any():
        label[m.to_numpy()] = 1
        covered.append(f"{name} ({int(m.sum())}d)")
print(f"F5a episodes covered on joint days: {covered}")
auc_iv = auroc(j["iv_p"].to_numpy(), label)
auc_rv = auroc(j["rv_p"].to_numpy(), label)
adds = auc_iv >= auc_rv + 0.03
print(f"F5a ADDS: AUROC(IV)={auc_iv:.3f} vs AUROC(RV)={auc_rv:.3f} "
      f"(bar: IV >= RV + 0.03) -> {'ADDS' if adds else 'does not add'}")

# VRP proxy — descriptive only, no consumption without its own registration
vrp = (j["iv"] / 100.0) ** 2 - j["rv"] ** 2
qs = np.percentile(vrp, [25, 50, 75])
print(f"F5a VRP proxy (annualized variance units): mean {vrp.mean():+.4f}, "
      f"quartiles [{qs[0]:+.4f}, {qs[1]:+.4f}, {qs[2]:+.4f}], "
      f"positive {100 * (vrp > 0).mean():.1f}% of days (descriptive only)")
