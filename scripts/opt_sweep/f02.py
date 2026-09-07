#!/usr/bin/env python3
"""OP-D2 family f02 — 3-state Gaussian HMM on NIFTY daily returns, SAME PROTOCOL as F01.

REGISTERED (trial-ledger.md, Entry OP-D2, 2026-09-07, BEFORE running):
  "F02 3-state HMM, same protocol (3) — prior: the 3rd state adds crash-onset
   separation or nothing; two-sided."
F01 protocol quoted verbatim (parent design, process note #5):
  "F01 HMM 2-state daily (EM refit quarterly-expanding) vs VIX-pct baseline (4) — prior:
   no material gain over the simple state (fwd-vol spread ratio <= 1.15x baseline's)."

Registered cells (3):
  c1 hmm3_fwdvol_spread_ratio_vs_vixpct — (3-state high/low fwd-21d vol ratio) divided by
     (VIX expanding-percentile top-vs-bottom-quintile fwd-21d vol ratio), overlap sample.
  c2 crash_onset_separation — lift of the 3rd (crash) state at t-1 before storm-cluster
     onsets vs its unconditional occupancy; compared with the 2-state high state's lift.
  c3 hmm3_vs_hmm2_spread — 3-state high/low fwd-vol ratio divided by 2-state high/low
     fwd-vol ratio (does the extra state widen forward-vol separation).

NO LOOKAHEAD: EM refit at each calendar-quarter start using returns strictly <= the last
trading day before the quarter start (expanding window, min_obs=504); states between
refits are causal FILTERED argmax probabilities under the frozen parameters (data <= t).
Conventions (OP-D1): fwd RV over h=21 days = sqrt(252/21 * sum sq daily log ret)*100;
storm day = |daily pct ret| >= 2%; VIX percentile = expanding percentile min_obs=252.
Vault data only. Seed fixed. All numbers below are printed by this script.
"""
import sys
sys.path.insert(0, '/home/user/claude-demo')
import numpy as np
import pandas as pd
from quant.ladder.credit_cycle import expanding_percentile

RNG = np.random.default_rng(20260907)
MIN_OBS = 504
VAR_FLOOR = 1e-10

# ---------- data ----------
px = pd.read_csv('/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv',
                 parse_dates=['Date']).sort_values('Date').set_index('Date')
adj = px['Adj Close'].astype(float)
ret_pct = adj.pct_change()
lr = np.log(adj).diff().dropna()          # daily log returns (HMM observable)
dates = lr.index
r = lr.values

vix = pd.read_csv('/home/user/claude-demo/ingest/vault/vix/india_vix_daily_2010_2023.csv',
                  parse_dates=['date']).sort_values('date').set_index('date')['close'].astype(float)
vix_pct = pd.Series(np.asarray(expanding_percentile(vix, min_obs=252)), index=vix.index)

# fwd 21d RV (annualized vol pts), t+1..t+21
h = 21
sq = pd.Series(r**2, index=dates)
fwd_sum = sq.shift(-h).rolling(h).sum().shift(h - 1)  # sum of sq lr over t+1..t+21
# simpler & verified: sum_{t+1..t+21} = reversed rolling
fwd_sum = sq[::-1].rolling(h).sum()[::-1].shift(-1)
fwd_rv = np.sqrt(252.0 / h * fwd_sum) * 100.0

# ---------- Gaussian HMM: EM + causal filter (own numpy impl; no hmmlearn in env) ----------
def em_fit(x, K, mu0=None, var0=None, A0=None, pi0=None, max_iter=60, tol=1e-7):
    n = len(x)
    if mu0 is None:
        qs = np.quantile(x, np.linspace(0.15, 0.85, K))
        mu0 = qs.copy()
        var0 = np.full(K, np.var(x)) * np.linspace(0.5, 2.0, K)
        A0 = np.full((K, K), 0.05 / max(K - 1, 1)); np.fill_diagonal(A0, 0.95)
        pi0 = np.full(K, 1.0 / K)
    mu, var, A, pi = mu0.copy(), np.maximum(var0, VAR_FLOOR), A0.copy(), pi0.copy()
    prev_ll = -np.inf
    for _ in range(max_iter):
        B = np.exp(-0.5 * (x[:, None] - mu[None, :])**2 / var[None, :]) / np.sqrt(2 * np.pi * var[None, :])
        B = np.maximum(B, 1e-300)
        # forward (scaled)
        alpha = np.zeros((n, K)); c = np.zeros(n)
        a = pi * B[0]; c[0] = a.sum(); alpha[0] = a / c[0]
        for t in range(1, n):
            a = (alpha[t - 1] @ A) * B[t]; c[t] = a.sum(); alpha[t] = a / c[t]
        ll = np.log(c).sum()
        # backward
        beta = np.zeros((n, K)); beta[-1] = 1.0
        for t in range(n - 2, -1, -1):
            beta[t] = (A @ (B[t + 1] * beta[t + 1])) / c[t + 1]
        g = alpha * beta; g /= g.sum(1, keepdims=True)
        xi_num = np.zeros((K, K))
        for t in range(n - 1):
            xi = (alpha[t][:, None] * A) * (B[t + 1] * beta[t + 1])[None, :]
            xi_num += xi / xi.sum()
        A = xi_num / xi_num.sum(1, keepdims=True)
        pi = g[0]
        w = g.sum(0)
        mu = (g * x[:, None]).sum(0) / w
        var = np.maximum((g * (x[:, None] - mu[None, :])**2).sum(0) / w, VAR_FLOOR)
        if abs(ll - prev_ll) < tol * max(1.0, abs(prev_ll)):
            break
        prev_ll = ll
    return mu, var, A, pi

def causal_filtered_states(x, mu, var, A, pi, t_from, t_to):
    """Filtered argmax state for t in [t_from, t_to) using data <= t under frozen params."""
    B = np.exp(-0.5 * (x[:t_to, None] - mu[None, :])**2 / var[None, :]) / np.sqrt(2 * np.pi * var[None, :])
    B = np.maximum(B, 1e-300)
    a = pi * B[0]; a /= a.sum()
    out = np.empty(t_to, dtype=int); out[0] = a.argmax()
    for t in range(1, t_to):
        a = (a @ A) * B[t]; a /= a.sum()
        out[t] = a.argmax()
    return out[t_from:t_to]

def run_hmm(K):
    qstarts = pd.date_range(dates[0], dates[-1], freq='QS')
    refits = [q for q in qstarts if (dates < q).sum() >= MIN_OBS]
    states = np.full(len(dates), -1, dtype=int)
    params = None
    n_refit = 0
    for i, q in enumerate(refits):
        n_tr = int((dates < q).sum())
        mu, var, A, pi = em_fit(r[:n_tr], K,
                                *(params if params else (None, None, None, None)))
        params = (mu, var, A, pi)
        n_refit += 1
        t_from = n_tr
        t_to = int((dates < refits[i + 1]).sum()) if i + 1 < len(refits) else len(dates)
        if t_to <= t_from:
            continue
        # relabel by sigma ascending so state K-1 is always the highest-vol state
        order = np.argsort(var)
        rank = np.empty(K, dtype=int); rank[order] = np.arange(K)
        raw = causal_filtered_states(r, mu, var, A, pi, t_from, t_to)
        states[t_from:t_to] = rank[raw]
    return pd.Series(states, index=dates), n_refit, params

print("== OP-D2 f02: 3-state HMM (same protocol as F01) ==")
print(f"NIFTY daily log returns {dates[0].date()}..{dates[-1].date()} n={len(r)}; "
      f"min_obs={MIN_OBS}; quarterly-expanding EM refits; causal filtered states.")

s2, nre2, p2 = run_hmm(2)
s3, nre3, p3 = run_hmm(3)
print(f"refits: K=2 {nre2}, K=3 {nre3}; first stated day: {dates[(s3.values >= 0).argmax()].date()}")
mu3, var3, A3, _ = p3
sig3 = np.sqrt(var3 * 252) * 100
order3 = np.argsort(var3)
print("final K=3 params (ann vol pts, sorted): "
      + ", ".join(f"state{k}: mu={mu3[o]*252*100:+.1f}%/yr ann_vol={sig3[o]:.1f} persist={A3[o,o]:.3f}"
                  for k, o in enumerate(order3)))
mu2, var2, A2, _ = p2
sig2 = np.sqrt(var2 * 252) * 100
order2 = np.argsort(var2)
print("final K=2 params (sorted): "
      + ", ".join(f"state{k}: mu={mu2[o]*252*100:+.1f}%/yr ann_vol={sig2[o]:.1f} persist={A2[o,o]:.3f}"
                  for k, o in enumerate(order2)))

valid3 = s3 >= 0
valid2 = s2 >= 0
occ3 = s3[valid3].value_counts(normalize=True).sort_index()
occ2 = s2[valid2].value_counts(normalize=True).sort_index()
print("occupancy K=3: " + ", ".join(f"s{k}={v:.3f}" for k, v in occ3.items()))
print("occupancy K=2: " + ", ".join(f"s{k}={v:.3f}" for k, v in occ2.items()))

# per-state fwd-21d RV (full stated sample where fwd RV exists)
df = pd.DataFrame({'s3': s3, 's2': s2, 'fwd': fwd_rv}).dropna()
df = df[(df.s3 >= 0) & (df.s2 >= 0)]
m3 = df.groupby('s3')['fwd'].agg(['mean', 'count'])
m2 = df.groupby('s2')['fwd'].agg(['mean', 'count'])
print("\nfwd-21d RV by K=3 state (mean vol pts / n): "
      + ", ".join(f"s{int(k)}={row['mean']:.2f}/{int(row['count'])}" for k, row in m3.iterrows()))
print("fwd-21d RV by K=2 state: "
      + ", ".join(f"s{int(k)}={row['mean']:.2f}/{int(row['count'])}" for k, row in m2.iterrows()))
r3 = m3['mean'].iloc[-1] / m3['mean'].iloc[0]
r2 = m2['mean'].iloc[-1] / m2['mean'].iloc[0]

# ---- c1: vs VIX-pct baseline on the overlap sample ----
ov = pd.DataFrame({'s3': s3, 'vp': vix_pct.reindex(dates), 'fwd': fwd_rv}).dropna()
ov = ov[ov.s3 >= 0]
ov['q'] = np.minimum((ov.vp * 5).astype(int), 4)
b = ov.groupby('q')['fwd'].mean()
base_ratio = b.loc[4] / b.loc[0]
m3o = ov.groupby('s3')['fwd'].mean()
hmm3_ratio_ov = m3o.iloc[-1] / m3o.iloc[0]
c1 = hmm3_ratio_ov / base_ratio
print(f"\n[c1] overlap sample {ov.index[0].date()}..{ov.index[-1].date()} n={len(ov)}")
print(f"[c1] VIX-pct quintile fwd-vol Q5/Q1 = {b.loc[4]:.2f}/{b.loc[0]:.2f} = {base_ratio:.3f}x")
print(f"[c1] HMM3 high/low fwd-vol (overlap) = {m3o.iloc[-1]:.2f}/{m3o.iloc[0]:.2f} = {hmm3_ratio_ov:.3f}x")
print(f"[c1] hmm3_fwdvol_spread_ratio_vs_vixpct = {c1:.3f}x  (F01 materiality anchor: 1.15x)")

# ---- c2: crash-onset separation ----
storm = (ret_pct.abs() >= 0.02).reindex(dates).fillna(False)
storm_arr = storm.values
onset = np.zeros(len(dates), dtype=bool)
for i in range(21, len(dates)):
    if storm_arr[i] and not storm_arr[i - 21:i].any():
        onset[i] = True
ok = valid3.values & valid2.values
on_idx = np.where(onset & ok)[0]
on_idx = on_idx[on_idx >= 1]
n_on = len(on_idx)
p3_on = float(np.mean(s3.values[on_idx - 1] == 2))
p2_on = float(np.mean(s2.values[on_idx - 1] == 1))
occ3h = float((s3[valid3] == 2).mean())
occ2h = float((s2[valid2] == 1).mean())
lift3 = p3_on / occ3h
lift2 = p2_on / occ2h
print(f"\n[c2] storm-cluster onsets (|ret|>=2%, none in prior 21d), stated sample: n={n_on}")
print(f"[c2] P(K=3 crash state at t-1 | onset) = {p3_on:.3f} vs occupancy {occ3h:.3f} -> lift {lift3:.2f}x")
print(f"[c2] P(K=2 high state at t-1 | onset)  = {p2_on:.3f} vs occupancy {occ2h:.3f} -> lift {lift2:.2f}x")
sep = lift3 / lift2 if lift2 > 0 else float('nan')
print(f"[c2] crash_onset_separation (lift3/lift2) = {sep:.3f}" if lift2 > 0 else
      "[c2] crash_onset_separation (lift3/lift2) = undefined (both lifts zero: neither model anticipates onsets)")
# reaction speed: state at the onset day t and within t..t+5
p3_t0 = float(np.mean(s3.values[on_idx] == 2))
p2_t0 = float(np.mean(s2.values[on_idx] == 1))
w3 = float(np.mean([(s3.values[i:i + 6] == 2).any() for i in on_idx]))
w2 = float(np.mean([(s2.values[i:i + 6] == 1).any() for i in on_idx]))
print(f"[c2] reaction: P(crash/high state AT onset day) K3={p3_t0:.3f} K2={p2_t0:.3f}; "
      f"within t..t+5: K3={w3:.3f} K2={w2:.3f}")
# storm-day (not just onset) capture for context
st_idx = np.where(storm_arr & ok)[0]; st_idx = st_idx[st_idx >= 1]
cap3 = float(np.mean(s3.values[st_idx - 1] == 2)); cap2 = float(np.mean(s2.values[st_idx - 1] == 1))
print(f"[c2] context: all storm days n={len(st_idx)}: crash-state t-1 capture K3={cap3:.3f} (lift {cap3/occ3h:.2f}x), "
      f"K2 high={cap2:.3f} (lift {cap2/occ2h:.2f}x)")

# ---- c3: 3-state vs 2-state fwd-vol separation ----
c3 = r3 / r2
print(f"\n[c3] full stated sample n={len(df)}: HMM3 high/low fwd-vol = {r3:.3f}x, HMM2 = {r2:.3f}x")
print(f"[c3] hmm3_vs_hmm2_spread = {c3:.3f}x; crash-state occupancy = {occ3.iloc[-1]:.3f} "
      f"({int(occ3.iloc[-1]*len(s3[valid3]))} days)")
mid_gap = m3['mean'].iloc[-1] - m3['mean'].iloc[1] if len(m3) == 3 else float('nan')
print(f"[c3] crash-vs-mid fwd-vol gap = {mid_gap:.2f} vol pts (distinctness of the 3rd state)")

print("\nSUMMARY c1={:.3f} c2_lift3={:.2f} c2_lift2={:.2f} c3={:.3f}".format(c1, lift3, lift2, c3))
