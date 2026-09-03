"""T-CTRL1 — the BLL moving-average family, run exactly as registered (the control group).

10 rules: VMA (1,50),(1,150),(5,150),(1,200),(2,200) x bands {0%, 1%}. Long/flat, signal on
close t-1, held day t, costs 28bps/unit turnover. BAR per rule: net Sharpe > buy-hold AND
DSR p < 0.05 at n_trials = census_n() + 10. PRIOR: zero survivors.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm, skew, kurtosis

from quant.stats.dsr import census_n, deflated_sharpe_ratio

ROOT = Path(__file__).resolve().parents[1]
COST = 0.0028

df = pd.read_csv(ROOT / "ingest/vault/index/nifty50_daily_2007_2026.csv",
                 parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
df["ret"] = df["Close"].pct_change()
df = df.dropna(subset=["ret"]).reset_index(drop=True)
px = df["Close"]
r = df["ret"].to_numpy()

def sharpe_ann(x):
    return float(np.mean(x) / np.std(x, ddof=1) * np.sqrt(252))

bh_sharpe = sharpe_ann(r)
n_trials = census_n() + 10
rules = [(f, s, b) for (f, s) in [(1, 50), (1, 150), (5, 150), (1, 200), (2, 200)]
         for b in (0.0, 0.01)]
print(f"T-CTRL1: buy-hold Sharpe {bh_sharpe:.2f}; DSR n_trials = census {census_n()} + 10 "
      f"= {n_trials}; cost {COST*1e4:.0f}bps/unit turnover")

# pass 1: all rule returns (the cross-trial SR variance needs the full family first)
prets, srs = [], []
for fast, slow, band in rules:
    fma = px.rolling(fast).mean()
    sma = px.rolling(slow).mean()
    sig = (fma > sma * (1 + band)).astype(float).shift(1).fillna(0.0).to_numpy()
    turn = np.abs(np.diff(sig, prepend=0.0))
    pret = sig * r - turn * COST
    prets.append(pret)
    srs.append(sharpe_ann(pret))
sr_var_daily = float(np.var(np.asarray(srs) / np.sqrt(252), ddof=1))

survivors = 0
for (fast, slow, band), pret, sr in zip(rules, prets, srs):
    dsr_p = deflated_sharpe_ratio(sr / np.sqrt(252), len(pret), float(skew(pret)),
                                  float(kurtosis(pret, fisher=False)),
                                  n_trials=n_trials, sr_var_across_trials=sr_var_daily)
    beat = sr > bh_sharpe
    ok = beat and dsr_p > 0.95
    print(f"  VMA({fast},{slow}) band {band*100:.0f}%: net Sharpe {sr:+.2f} "
          f"(beats BH: {beat}), DSR prob {dsr_p:.3f} -> {'SURVIVES' if ok else 'dead'}")
    survivors += ok
print(f"\nT-CTRL1 VERDICT: {survivors}/10 survivors (prior: 0)")
