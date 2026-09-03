"""F3a — vol-managed NIFTY (index partial), run exactly as registered (2026-09-03).

Three documentation cells with priors (no promotion bar, per the parent F3 rule):
  F3a-1 full-period Moreira-Muir replication (uncapped, vol-matched c)
  F3a-2 Cederburg real-time OOS (expanding c, 36m warm-up) with stationary-bootstrap CI
  F3a-3 desk-feasible capped-at-1, net of 16bps/unit-turnover (index_futures HI end)
"""
from pathlib import Path

import numpy as np
import pandas as pd

from quant.stats.bootstrap import max_drawdown, stationary_bootstrap

ROOT = Path(__file__).resolve().parents[1]

df = pd.read_csv(ROOT / "ingest/vault/index/nifty50_daily_2007_2026.csv",
                 parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
df["ret"] = df["Close"].pct_change()
df = df.dropna(subset=["ret"]).reset_index(drop=True)
df["ym"] = df["Date"].dt.to_period("M")

# monthly buy-hold returns and previous-month realized variance (annualized)
m_ret = df.groupby("ym")["ret"].apply(lambda x: float(np.expm1(np.log1p(x).sum())))
m_var = df.groupby("ym")["ret"].apply(lambda x: float(np.var(x, ddof=1) * 252))
months = m_ret.index
bh = m_ret.values
prev_var = m_var.shift(1).values
valid = ~np.isnan(prev_var)
bh, prev_var, months = bh[valid], prev_var[valid], months[valid]
n = len(bh)
print(f"F3a sample: {months[0]}..{months[-1]}  n={n} months")


def sharpe(x):
    return float(np.mean(x) / np.std(x, ddof=1) * np.sqrt(12))


def nw_alpha(y, x, lags=3):
    """Monthly alpha of y on x with Newey-West t-stat (manual, small and standard)."""
    X = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ beta
    XtX_inv = np.linalg.inv(X.T @ X)
    S = np.zeros((2, 2))
    for l in range(lags + 1):
        w = 1 - l / (lags + 1)
        for t in range(l, len(e)):
            u = X[t] * e[t]
            v = X[t - l] * e[t - l]
            S += w * (np.outer(u, v) + (np.outer(v, u) if l > 0 else 0))
    cov = XtX_inv @ S @ XtX_inv
    return beta[0], float(beta[0] / np.sqrt(cov[0, 0]))


# ---- F3a-1: full-period MM, uncapped, vol-matched c ----
raw_w = 1.0 / prev_var
c1 = np.std(bh, ddof=1) / np.std(raw_w * bh, ddof=1)
w1 = c1 * raw_w
mm = w1 * bh
alpha, t_alpha = nw_alpha(mm, bh)
print(f"\nF3a-1 (full-period MM, uncapped): c={c1:.4f}, weights [{w1.min():.2f},{w1.max():.2f}] "
      f"mean {w1.mean():.2f}")
print(f"  alpha {alpha*12*100:+.2f}%/yr (NW t={t_alpha:.2f}) | Sharpe {sharpe(mm):.2f} vs "
      f"buy-hold {sharpe(bh):.2f} | maxDD {max_drawdown(mm)*100:.0f}% vs {max_drawdown(bh)*100:.0f}%")

# ---- F3a-2: Cederburg real-time OOS (expanding c, 36m warm-up) ----
oos = np.full(n, np.nan)
for t in range(36, n):
    c_t = np.std(bh[:t], ddof=1) / np.std(raw_w[:t] * bh[:t], ddof=1)
    oos[t] = c_t * raw_w[t] * bh[t]
mask = ~np.isnan(oos)
d = oos[mask] - bh[mask]
sh_diff = sharpe(oos[mask]) - sharpe(bh[mask])
means = stationary_bootstrap(d, n_samples=2000, mean_block=6, seed=0).mean(axis=1)
lo, hi = np.quantile(means, [0.05, 0.95]) * 12 * 100
print(f"\nF3a-2 (real-time OOS, {mask.sum()} months): OOS Sharpe {sharpe(oos[mask]):.2f} vs "
      f"buy-hold {sharpe(bh[mask]):.2f} -> diff {sh_diff:+.2f}")
print(f"  mean return difference {np.mean(d)*12*100:+.2f}%/yr, 90% stationary-bootstrap CI "
      f"[{lo:+.2f}, {hi:+.2f}]%/yr (mean_block=6, n=2000, seed=0) -> "
      f"{'includes 0 (prior confirmed: no OOS improvement)' if lo <= 0 <= hi else 'EXCLUDES 0'}")

# ---- F3a-3: capped at 1, net of 16bps per unit turnover ----
w3 = np.minimum(w1, 1.0)
turn = np.abs(np.diff(np.concatenate([[0.0], w3])))
net = w3 * bh - turn * 0.0016
gross = w3 * bh
covid = [i for i, p in enumerate(months) if str(p) in ("2020-02", "2020-03", "2020-04")]
def window_dd(x, idx):
    path = np.cumprod(1 + x[min(idx):max(idx) + 1])
    return float(1 - (path / np.maximum.accumulate(path)).min())
print(f"\nF3a-3 (capped<=1, net of 16bps/turnover): mean weight {w3.mean():.2f}, "
      f"annual turnover {turn.sum() / (n / 12):.1f}x")
print(f"  maxDD {max_drawdown(net)*100:.0f}% vs buy-hold {max_drawdown(bh)*100:.0f}% | "
      f"net-vs-buy-hold drag {(np.mean(net) - np.mean(bh))*12*100:+.2f}%/yr "
      f"(gross {(np.mean(gross) - np.mean(bh))*12*100:+.2f}%/yr, costs "
      f"{np.mean(turn)*0.0016*12*100:.2f}%/yr)")
print(f"  COVID window (Feb-Apr 2020) DD: managed {window_dd(net, covid)*100:.0f}% vs "
      f"buy-hold {window_dd(bh, covid)*100:.0f}%")
