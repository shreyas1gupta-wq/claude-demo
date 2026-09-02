"""The first daily-resolution batch — CW-D1a / DW1 / F1a / F2a (pre-registered).

Ledger 2026-09-02. Data: ingest/vault/index/nifty50_daily_2007_2026.csv (mirror, 6/6
anchors). Budget dates and episode windows are public record, fixed below before any
trial ran (episode set verbatim from docs/cycles/02-fast-stress.md §3, in-span subset).
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import (drawdown_depth, fast_stress_composite,
                                      realized_vol)

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "index"

BUDGET_DAYS = [  # Union Budget presentation days (fulls + interims), 11am era, public record
    "2008-02-29", "2009-02-16", "2009-07-06", "2010-02-26", "2011-02-28", "2012-03-16",
    "2013-02-28", "2014-02-17", "2014-07-10", "2015-02-28", "2016-02-29", "2017-02-01",
    "2018-02-01", "2019-02-01", "2019-07-05", "2020-02-01", "2021-02-01", "2022-02-01",
    "2023-02-01", "2024-02-01", "2024-07-23", "2025-02-01", "2026-02-01",
]

EPISODES = [  # §3 pre-named stress episodes, in-span subset (12)
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
    ("INR/FII May-2026", "2026-05-01", "2026-06-30"),  # may exceed data end — checked below
]

df = pd.read_csv(VAULT / "nifty50_daily_2007_2026.csv", parse_dates=["Date"])
df = df.sort_values("Date").reset_index(drop=True)
df["ret"] = df["Close"].pct_change()
df = df.dropna(subset=["ret"]).reset_index(drop=True)
print(f"Sample: {df['Date'].min():%Y-%m-%d}..{df['Date'].max():%Y-%m-%d} n={len(df)}")

# ---------------- CW-D1a ----------------
bset = set(pd.to_datetime(BUDGET_DAYS))
in_span = [d for d in pd.to_datetime(BUDGET_DAYS) if df["Date"].min() <= d <= df["Date"].max()]
is_b = df["Date"].isin(bset)
on = df.loc[is_b, "ret"].abs() * 100
matched = sum(1 for d in in_span if (df["Date"] == d).any())
off = df.loc[~is_b, "ret"].abs() * 100
u, p1 = stats.mannwhitneyu(on, off, alternative="greater")
print(f"\nCW-D1a: {matched}/{len(in_span)} budget days matched to trading days")
print(f"  budget-day median |ret|={on.median():.2f}% (n={len(on)}) vs other days {off.median():.2f}%")
print(f"  MW one-sided p={p1:.4f} -> BAR p<0.05: {'PASS' if p1 < 0.05 else 'FAIL'}")
idx_b = df.index[is_b]
w = sorted(set(i + k for i in idx_b for k in (-1, 0, 1) if 0 <= i + k < len(df)))
onw = df.loc[w, "ret"].abs() * 100
offw = df.drop(index=w)["ret"].abs() * 100
u2, p2 = stats.mannwhitneyu(onw, offw, alternative="greater")
print(f"  secondary (±1 window, no bar): median {onw.median():.2f}% vs {offw.median():.2f}%, p={p2:.4f}")

# ---------------- DW1 ----------------
groups = [df.loc[df["Date"].dt.weekday == k, "ret"].values * 100 for k in range(5)]
h, p_dw = stats.kruskal(*groups)
meds = [f"{np.median(g):+.3f}" for g in groups]
print(f"\nDW1: weekday median returns (Mon..Fri) = {meds}")
print(f"  Kruskal-Wallis H={h:.2f}, p={p_dw:.3f} -> "
      + ("REJECT confirmed with evidence" if p_dw >= 0.05 else "p<0.05 logged; REJECT stands (rule pre-stated)"))

# ---------------- fast-stress composite (shared by F1a/F2a) ----------------
rv = realized_vol(df["ret"].values, window=21)
dd = drawdown_depth(df["ret"].values)
rv_p = expanding_percentile(rv, min_obs=252)
dd_p = expanding_percentile(dd, min_obs=252)
state = fast_stress_composite(rv_p, dd_p)
ok = ~np.isnan(state)

# F1a: AR(1) half-life + moving-block bootstrap CI
s = state[ok]


def ar1_halflife(x):
    x0, x1 = x[:-1] - x.mean(), x[1:] - x.mean()
    phi = float(np.dot(x0, x1) / np.dot(x0, x0))
    return np.log(0.5) / np.log(phi) if 0 < phi < 1 else np.inf


hl = ar1_halflife(s)
rng = np.random.default_rng(0)
B, block = 1000, 63
n = len(s)
hls = []
for _ in range(B):
    starts = rng.integers(0, n - block, size=n // block + 1)
    bs = np.concatenate([s[st:st + block] for st in starts])[:n]
    hls.append(ar1_halflife(bs))
lo, hi = np.percentile([h for h in hls if np.isfinite(h)], [2.5, 97.5])
print(f"\nF1a: tau_half = {hl:.0f} trading days (~{hl/21:.1f} months); "
      f"95% block-bootstrap CI [{lo:.0f}, {hi:.0f}]d (~[{lo/21:.1f}, {hi/21:.1f}]m); "
      f"registered ladder value [1,3] months")

# F2a: episode detection at state >= 0.3
print("\nF2a: episode detection (state >= 0.3 within [start-5bd, end+21bd]):")
dates = df["Date"].values
det, names_missed = 0, []
ep_mask = np.zeros(len(df), dtype=bool)
for name, s0, s1 in EPISODES:
    t0, t1 = np.datetime64(s0), np.datetime64(s1)
    if t0 > dates[-1]:
        print(f"  {name}: OUT OF SAMPLE (data ends {str(dates[-1])[:10]}) — excluded from denominator")
        continue
    i = np.where((dates >= t0) & (dates <= t1))[0]
    if len(i) == 0:
        print(f"  {name}: no trading days in window — excluded")
        continue
    w0, w1 = max(0, i[0] - 5), min(len(df) - 1, i[-1] + 21)
    seg = state[w0:w1 + 1]
    hitidx = np.where(seg >= 0.3)[0]
    m0 = max(0, i[0] - 42)
    m1 = min(len(df) - 1, i[-1] + 42)
    ep_mask[m0:m1 + 1] = True
    if len(hitidx) > 0:
        lag = int(hitidx[0] + w0 - i[0])
        det += 1
        print(f"  {name}: DETECTED (max state {np.nanmax(seg):+.2f}, lag {lag:+d}bd from start)")
    else:
        names_missed.append(name)
        print(f"  {name}: MISSED (max state {np.nanmax(seg):+.2f})")
denom = sum(1 for name, s0, s1 in EPISODES if np.datetime64(s0) <= dates[-1])
ff = int(np.nansum((state >= 0.3) & ~ep_mask & ok))
print(f"F2a: {det}/{denom} detected -> BAR >=8/{denom}: {'PASS' if det >= 8 else 'FAIL'}")
print(f"  false-fire days (>=0.3 outside episodes ±2m): {ff} of {int(ok.sum())} valid days "
      f"({100*ff/int(ok.sum()):.1f}%) [measurement, no bar]")
if names_missed:
    print(f"  misses to dissect: {names_missed}")
