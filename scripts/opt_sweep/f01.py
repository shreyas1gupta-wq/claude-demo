#!/usr/bin/env python3
"""OP-D2 family F01 — HMM 2-state daily (EM refit quarterly-expanding) vs VIX-pct baseline.

REGISTERED (trial-ledger Entry OP-D2, 2026-09-07, BEFORE running):
  F01 HMM 2-state daily (EM refit quarterly-expanding) vs VIX-pct baseline (4 cells)
  — prior: no material gain over the simple state (fwd-vol spread ratio <= 1.15x baseline's).

Operationalization declared in this header (per OP-D1 conventions; bars never move):
  - Data: vault only. NIFTY 50 daily Adj Close 2007-09..2026-04; India VIX close 2010-07..2023-04.
  - Returns: daily log returns of Adj Close.
  - HMM: 2-state Gaussian HMM on daily log returns, Baum-Welch EM (deterministic init:
    mu=[mean,mean], sigma=[0.5,2.0]x sample std, A diag 0.97, pi=[.5,.5]; warm-started refits).
    Refit schedule: first trading day of each calendar quarter, EXPANDING window using only
    returns strictly BEFORE the refit date; min_obs = 504 returns. Between refits the params
    are frozen; the state at day t is the FILTERED P(high-vol | r_1..r_t) > 0.5 (forward
    recursion over data <= t only — no smoothing, no lookahead). High-vol state = larger sigma.
  - Baseline: India VIX close expanding percentile (quant.ladder.credit_cycle.expanding_percentile,
    min_obs=252); high state = pct >= 0.5 (median split — the same 2-state granularity).
  - Forward vol: RV over the next 21 days = sqrt(252/21 * sum r_log^2 over t+1..t+21) * 100
    (annualized vol points; OP-D1 convention). Overlapping windows — flagged.
  - Common sample: days where HMM state, VIX pct, and fwd-21d RV are all defined.
CELLS (4):
  c1 hmm_fwd21_vol_spread      = mean fwdRV(HMM high) - mean fwdRV(HMM low)      DESCRIPTIVE
  c2 baseline_fwd21_vol_spread = mean fwdRV(VIXpct high) - mean fwdRV(VIXpct low) DESCRIPTIVE
  c3 spread_ratio = c1/c2  — THE REGISTERED BAR: <= 1.15x -> prior PASS (no material gain);
     > 1.15x -> MISS recorded (HMM adds material state information).
  c4 state_agreement = fraction of common days where the two high/low labels agree  DESCRIPTIVE

Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/f01.py
"""
import sys
sys.path.insert(0, "/home/user/claude-demo")
import numpy as np
import pandas as pd
from quant.ladder.credit_cycle import expanding_percentile

VAULT = "/home/user/claude-demo/ingest/vault"
MIN_OBS_HMM = 504
MIN_OBS_VIXPCT = 252
H = 21

# ---------- data ----------
nifty = pd.read_csv(f"{VAULT}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"])
nifty = nifty.sort_values("Date").reset_index(drop=True)
px = nifty["Adj Close"].astype(float).values
dates = nifty["Date"].values
r = np.diff(np.log(px))                      # log return on day i+1
rdates = dates[1:]                           # date of each return

vix = pd.read_csv(f"{VAULT}/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"])
vix = vix.sort_values("date").reset_index(drop=True)
vix_pct = expanding_percentile(vix["close"].astype(float).values, min_obs=MIN_OBS_VIXPCT)
vix_state = pd.Series(np.where(np.isnan(vix_pct), np.nan, (vix_pct >= 0.5).astype(float)),
                      index=vix["date"].values)

# ---------- 2-state Gaussian HMM (Baum-Welch, scaled) ----------
def gauss_pdf(x, mu, sig):
    return np.exp(-0.5 * ((x - mu) / sig) ** 2) / (sig * np.sqrt(2 * np.pi))

def forward_filtered(x, pi, A, mu, sig):
    """Scaled forward pass; returns filtered probs (n,2) and loglik. Uses only x[0..t] at row t."""
    n = len(x)
    B = np.column_stack([gauss_pdf(x, mu[k], sig[k]) for k in range(2)]) + 1e-300
    alpha = np.zeros((n, 2)); c = np.zeros(n)
    a = pi * B[0]; c[0] = a.sum(); alpha[0] = a / c[0]
    for t in range(1, n):
        a = (alpha[t - 1] @ A) * B[t]
        c[t] = a.sum(); alpha[t] = a / c[t]
    return alpha, np.log(c).sum()

def fit_hmm(x, init=None, max_iter=80, tol=1e-6):
    m, s = x.mean(), x.std()
    if init is None:
        mu = np.array([m, m]); sig = np.array([0.5 * s, 2.0 * s])
        A = np.array([[0.97, 0.03], [0.03, 0.97]]); pi = np.array([0.5, 0.5])
    else:
        pi, A, mu, sig = [v.copy() for v in init]
    n = len(x); prev_ll = -np.inf
    for _ in range(max_iter):
        B = np.column_stack([gauss_pdf(x, mu[k], sig[k]) for k in range(2)]) + 1e-300
        alpha = np.zeros((n, 2)); c = np.zeros(n)
        a = pi * B[0]; c[0] = a.sum(); alpha[0] = a / c[0]
        for t in range(1, n):
            a = (alpha[t - 1] @ A) * B[t]; c[t] = a.sum(); alpha[t] = a / c[t]
        beta = np.zeros((n, 2)); beta[-1] = 1.0
        for t in range(n - 2, -1, -1):
            beta[t] = (A @ (B[t + 1] * beta[t + 1])) / c[t + 1]
        gamma = alpha * beta; gamma /= gamma.sum(axis=1, keepdims=True)
        xi = np.zeros((2, 2))
        for t in range(n - 1):
            num = np.outer(alpha[t], B[t + 1] * beta[t + 1]) * A / c[t + 1]
            xi += num
        pi = gamma[0]
        A = xi / xi.sum(axis=1, keepdims=True)
        for k in range(2):
            w = gamma[:, k]; W = w.sum()
            mu[k] = (w * x).sum() / W
            sig[k] = max(np.sqrt((w * (x - mu[k]) ** 2).sum() / W), 1e-6)
        ll = np.log(c).sum()
        if abs(ll - prev_ll) < tol * abs(prev_ll):
            break
        prev_ll = ll
    if sig[0] > sig[1]:  # order: state 1 = high-vol
        mu, sig = mu[::-1].copy(), sig[::-1].copy()
        A = A[::-1, ::-1].copy(); pi = pi[::-1].copy()
    return pi, A, mu, sig

# refit dates: first trading return-date of each calendar quarter with >= MIN_OBS_HMM prior returns
rq = pd.PeriodIndex(pd.DatetimeIndex(rdates), freq="Q")
refit_idx = []
for q in rq.unique():
    i = int(np.argmax(rq == q))                # first return-day of quarter q
    if i >= MIN_OBS_HMM:
        refit_idx.append(i)
refit_idx = sorted(refit_idx)

hmm_state = np.full(len(r), np.nan)
params = None
for j, i0 in enumerate(refit_idx):
    params = fit_hmm(r[:i0], init=params, max_iter=200 if j == 0 else 80)
    i1 = refit_idx[j + 1] if j + 1 < len(refit_idx) else len(r)
    alpha, _ = forward_filtered(r[:i1], *params)   # filtered prob at t uses r[0..t] only
    hmm_state[i0:i1] = (alpha[i0:i1, 1] > 0.5).astype(float)
pi_f, A_f, mu_f, sig_f = params
print(f"HMM refits: {len(refit_idx)} (quarterly-expanding, min_obs={MIN_OBS_HMM}); "
      f"first state date {pd.Timestamp(rdates[refit_idx[0]]).date()}")
print(f"final-fit sigmas (ann vol pts): low {sig_f[0]*np.sqrt(252)*100:.1f}, "
      f"high {sig_f[1]*np.sqrt(252)*100:.1f}; A diag {A_f[0,0]:.3f}/{A_f[1,1]:.3f}")

# ---------- forward 21d RV ----------
fwd_rv = np.full(len(r), np.nan)
r2 = r ** 2
cs = np.concatenate([[0.0], np.cumsum(r2)])
for t in range(len(r) - H):
    fwd_rv[t] = np.sqrt(252.0 / H * (cs[t + 1 + H] - cs[t + 1])) * 100.0

# ---------- common sample ----------
df = pd.DataFrame({"date": rdates, "hmm": hmm_state, "fwd_rv": fwd_rv}).set_index("date")
df["vix_hi"] = vix_state.reindex(df.index)
df = df.dropna()
n = len(df)
print(f"common sample: {n} days, {df.index[0].date()}..{df.index[-1].date()} "
      f"(HMM-high share {df['hmm'].mean():.2%}, VIXpct-high share {df['vix_hi'].mean():.2%})")

hi_h, lo_h = df.loc[df.hmm == 1, "fwd_rv"], df.loc[df.hmm == 0, "fwd_rv"]
hi_b, lo_b = df.loc[df.vix_hi == 1, "fwd_rv"], df.loc[df.vix_hi == 0, "fwd_rv"]
c1 = hi_h.mean() - lo_h.mean()
c2 = hi_b.mean() - lo_b.mean()
c3 = c1 / c2
c4 = (df.hmm == df.vix_hi).mean()

print(f"c1 HMM fwd-21d vol spread: high {hi_h.mean():.2f} (n={len(hi_h)}) - low {lo_h.mean():.2f} "
      f"(n={len(lo_h)}) = {c1:.2f} vol pts")
print(f"c2 VIX-pct baseline spread: high {hi_b.mean():.2f} (n={len(hi_b)}) - low {lo_b.mean():.2f} "
      f"(n={len(lo_b)}) = {c2:.2f} vol pts")
print(f"c3 spread ratio HMM/baseline = {c3:.3f}  [REGISTERED BAR: <= 1.15 -> prior PASS]")
print(f"c4 state agreement = {c4:.2%}")
verdict = "PASS" if c3 <= 1.15 else "MISS"
print(f"VERDICT on the registered bar: {verdict}")
# transparency (not a cell): storm-day capture
storm = df.index[np.isin(df.index.values, rdates[np.abs(np.exp(r) - 1) >= 0.02])]
if len(storm):
    print(f"[info] storm days (|ret|>=2%) in sample: {len(storm)}; HMM-high on "
          f"{df.loc[storm,'hmm'].mean():.2%}, VIXpct-high on {df.loc[storm,'vix_hi'].mean():.2%}")
