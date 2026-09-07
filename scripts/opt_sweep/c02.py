#!/usr/bin/env python3
"""OP-D2 combiner C02 — the sizing stack: f18 DD-constrained base x f05 vol-target multiplier.

ONE formula (fraction of book posted as margin per structure, per entered cycle):

    f_t = f_DD(arm) * s_t,   s_t = min(target_vol_t / EWMA_vol_t(lambda=0.94), 2.0)

  - s_t is f05's registered vol-target multiplier VERBATIM (EWMA 0.94 init 63d pre-VIX,
    expanding-mean target, cap 2x, no-lookahead: state at t uses data <= t only).
  - f_DD(arm) is RE-DERIVED here on the VOL-SCALED F16 per-margin return distribution
    (r_scaled_t = s_t * r_t) with f18's own machinery verbatim (iid bootstrap, seed 42,
    20000 1y paths, largest f on 0.005 grid with P(book maxDD>10%) <= 1%/yr), so the
    combined stack respects the f18 DD budget as a system, not leg-by-leg.
  - Concrete numbers at VIX-pct 0.60 / 0.80 / 0.95: median s over common trading days
    with expanding VIX pct in bands [0.55,0.65) / [0.75,0.85) / [0.925,1.0].

DESCRIPTIVE sizing math on already-printed families (f05, f16, f18) — combiner cell,
no new bar registered, no promotion. Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/c02.py
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
sys.path.insert(0, "/home/user/claude-demo/scripts/opt_sweep")
import f16 as F16
import f18 as F18
from quant.ladder.credit_cycle import expanding_percentile

LAMBDA, EWMA_INIT_N, CAP = 0.94, 63, 2.0  # f05 registered spec, verbatim

# ---- f05 sizing signal, verbatim mechanics ----
nf = pd.read_csv(f"{F16.REPO}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                 parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
px = pd.to_numeric(nf["Adj Close"], errors="coerce")
nf = nf.loc[px.notna()].reset_index(drop=True)
px = px[px.notna()].values
r2 = np.diff(np.log(px)) ** 2
n = len(r2)
vol_pts = np.full(n, np.nan)
v = float(np.mean(r2[:EWMA_INIT_N]))
for t in range(EWMA_INIT_N, n):
    v = LAMBDA * v + (1.0 - LAMBDA) * r2[t]
    vol_pts[t] = np.sqrt(252.0 * v) * 100.0
target = np.full(n, np.nan)
csum, cnt = 0.0, 0
for t in range(EWMA_INIT_N, n):
    csum += vol_pts[t]; cnt += 1
    target[t] = csum / cnt
size_all = np.minimum(target / vol_pts, CAP)
sz = pd.Series(size_all, index=pd.Index(nf["Date"].values[1:]))

# ---- F16 monthly walk, f18.f16_margin_returns verbatim + entry date / s_t / pct ----
vx = pd.read_csv(f"{F16.REPO}/ingest/vault/vix/india_vix_daily_2010_2023.csv",
                 parse_dates=["date"]).set_index("date")["close"]
pxs = pd.read_csv(f"{F16.REPO}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                  parse_dates=["Date"]).set_index("Date")["Adj Close"]
df = pd.concat({"S": pxs, "vix": vx}, axis=1, join="inner").dropna().sort_index()
df["pct"] = expanding_percentile(df["vix"].values, min_obs=F16.MIN_OBS)
S, V, P = df["S"].values, df["vix"].values / 100.0, df["pct"].values
span = (df.index[-1] - df.index[F16.MIN_OBS - 1]).days / 365.25
rows = []
for t0 in range(F16.MIN_OBS - 1, len(df) - F16.TENOR, F16.TENOR):
    if np.isnan(P[t0]) or P[t0] < F16.ENTRY_PCT:
        continue
    S0, sig0 = S[t0], V[t0]
    T0 = F16.TENOR / 252.0
    K0 = F16.make_strikes(S0, sig0, T0)
    C0, _, _ = F16.condor_mark(S0, K0, T0, sig0)
    margin = max(K0["kc2"] - K0["kc1"], K0["kp1"] - K0["kp2"]) - C0
    stop_pnl, stopped = None, False
    for j in range(1, F16.TENOR + 1):
        Trem = (F16.TENOR - j) / 252.0
        cost, _, _ = F16.condor_mark(S[t0 + j], K0, Trem, V[t0 + j])
        if not stopped and cost >= F16.STOP_MULT * C0:
            stop_pnl, stopped = C0 - cost, True
    hold_pnl = C0 - cost
    if not stopped:
        stop_pnl = hold_pnl
    d = df.index[t0]
    rows.append((d, float(P[t0]), float(sz.loc[d]), hold_pnl / margin, stop_pnl / margin))
E = pd.DataFrame(rows, columns=["date", "pct", "s", "rh", "rs"])
print(f"F16 walk regenerated: n={len(E)} entries, span {span:.2f}y "
      f"({E['date'].min().date()}..{E['date'].max().date()})")
print(f"s_t at entries: mean {E['s'].mean():.3f}, min {E['s'].min():.3f}, "
      f"max {E['s'].max():.3f}, at-cap {(E['s'] >= CAP - 1e-9).sum()}/{len(E)}")

# ---- DD-constrained base f: unscaled (f18 anchor check) and vol-scaled ----
rate = len(E) / span
n_cyc = max(1, round(rate))
print(f"rate {rate:.2f} cycles/yr, bootstrap n_cyc={n_cyc}")
res = {}
for name, arr in [("hold-unscaled", E["rh"].values), ("stop2x-unscaled", E["rs"].values),
                  ("hold-volscaled", (E["s"] * E["rh"]).values),
                  ("stop2x-volscaled", (E["s"] * E["rs"]).values)]:
    rng = np.random.default_rng(42)
    idx = rng.integers(0, len(arr), size=(F18.NSIMS, n_cyc))
    fdd = F18.dd_constrained(arr, idx)
    g = F18.growth_yr(arr, fdd, rate)
    res[name] = fdd
    print(f"  [{name}] f_DD={fdd:.3f} (P(maxDD>10%)<=1%/yr), growth {g:+.1f}%/yr, "
          f"worst cycle {100*arr.min():+.1f}% of margin")

# ---- s(VIX-pct) mapping on all common days with valid pct + s ----
day = pd.DataFrame({"pct": df["pct"].values, "s": sz.reindex(df.index).values},
                   index=df.index).dropna()
bands = {0.60: (0.55, 0.65), 0.80: (0.75, 0.85), 0.95: (0.925, 1.0001)}
print("\ns_t by VIX expanding-percentile band (all common days, n=%d):" % len(day))
smed = {}
for k, (lo, hi) in bands.items():
    sub = day[(day["pct"] >= lo) & (day["pct"] < hi)]["s"]
    smed[k] = float(sub.median())
    print(f"  pct~{k:.2f} [{lo},{hi:.3f}): n={len(sub)}, median s={sub.median():.3f}, "
          f"IQR [{sub.quantile(.25):.3f},{sub.quantile(.75):.3f}]")

# ---- THE STACK: f_t = f_DD(volscaled arm) * s(pct) ----
print("\nCOMBINED SIZING (fraction of book as margin per structure, f_DD x median s):")
for arm in ["hold-volscaled", "stop2x-volscaled"]:
    base = res[arm]
    line = ", ".join(f"pct {k:.2f}: {base * smed[k]:.3f}" for k in bands)
    print(f"  {arm.replace('-volscaled','')}: base f_DD={base:.3f} -> {line}")
print("\nDESCRIPTIVE combiner math on printed families f05/f16/f18; iid bootstrap "
      "ignores clustering -> all f are UPPER bounds (f18 caveat); vol-target cannot "
      "see sudden onsets (f05 MISS, F04 lag) -> the DD budget, not s_t, is the "
      "protection against them.")
