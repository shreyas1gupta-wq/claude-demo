"""F1c — Andrews median-unbiased tau_half of the L2 composite (pre-registered)."""
from pathlib import Path

import numpy as np
import pandas as pd

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import drawdown_depth, fast_stress_composite, realized_vol
from quant.stats.andrews import median_unbiased_rho
from quant.stats.tau_half import ar1_ols

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "index"
df = pd.read_csv(VAULT / "nifty50_daily_2007_2026.csv", parse_dates=["Date"]).sort_values("Date")
r = df["Close"].pct_change().dropna().values
state = fast_stress_composite(expanding_percentile(realized_vol(r, 21), min_obs=252),
                              expanding_percentile(drawdown_depth(r), min_obs=252))
s = state[~np.isnan(state)]
hat = ar1_ols(s)
res = median_unbiased_rho(hat, len(s), n_sim=300, seed=0)
print(f"F1c: n={len(s)}; OLS rho {hat:.4f} -> median-unbiased {res.rho_mu:.4f} "
      f"(grid_edge: {res.grid_edge})")
print(f"  tau_half: {res.tau_half:.0f}d = {res.tau_half/21:.2f} months; "
      f"90% interval [{res.tau_ci_low/21:.2f}, {res.tau_ci_high/21:.2f}]m")
print(f"  context: ladder [1,3]m; F1b (Kendall) 3.18m CI [2.39,5.72]m")
