"""F1b — corrected tau_half of the L2 two-leg composite (Track-R estimator).

Ledger 2026-09-02. Same composite as F1a/F2-index; quant/stats/tau_half.estimate_tau_half
(Kendall correction + parametric pivot CI, per MC1).
"""
from pathlib import Path

import numpy as np
import pandas as pd

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import drawdown_depth, fast_stress_composite, realized_vol
from quant.stats.tau_half import estimate_tau_half

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "index"

df = pd.read_csv(VAULT / "nifty50_daily_2007_2026.csv", parse_dates=["Date"]).sort_values("Date")
r = df["Close"].pct_change().dropna().values
rv_p = expanding_percentile(realized_vol(r, 21), min_obs=252)
dd_p = expanding_percentile(drawdown_depth(r), min_obs=252)
state = fast_stress_composite(rv_p, dd_p)
s = state[~np.isnan(state)]

res = estimate_tau_half(s, n_boot=400, ci=0.90, seed=0)
print(f"F1b: n={res.n_obs} daily obs")
print(f"  rho naive {res.rho_naive:.4f} -> Kendall-corrected {res.rho_corrected:.4f} "
      f"(near_unit_root: {res.near_unit_root})")
print(f"  tau_half corrected: {res.tau_half:.0f} trading days = {res.tau_half/21:.2f} months "
      f"(naive {res.tau_half_naive/21:.2f}m)")
print(f"  90% CI: [{res.ci_low:.0f}, {res.ci_high:.0f}] days = "
      f"[{res.ci_low/21:.2f}, {res.ci_high/21:.2f}] months; ladder registered [1, 3] months")
