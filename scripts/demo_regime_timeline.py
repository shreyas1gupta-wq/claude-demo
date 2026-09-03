"""Stage-1 end-to-end DEMO on the vaulted index: L2 state -> regime R -> buckets.

MACHINERY DEMONSTRATION, not a trial (no bars): one block available (fast_stress), so R is
availability-weighted to L2 alone and every row carries n_blocks=1 — the honest label. The
point is the pipeline running end-to-end on real history: quant/ladder -> quant/regime.
"""
from pathlib import Path

import numpy as np
import pandas as pd

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import drawdown_depth, fast_stress_composite, realized_vol
from quant.regime import assemble_regime, bucket_path
from quant.registry.loader import load_registry

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "index"
LADDER = load_registry(validate=False)["ladder"]

df = pd.read_csv(VAULT / "nifty50_daily_2007_2026.csv", parse_dates=["Date"]).sort_values("Date")
r = df["Close"].pct_change().dropna().values
dates = df["Date"].iloc[1:].reset_index(drop=True)
st = fast_stress_composite(expanding_percentile(realized_vol(r, 21), min_obs=252),
                           expanding_percentile(drawdown_depth(r), min_obs=252))

scores = np.array([assemble_regime({"L2_fast_stress": s} if not np.isnan(s) else {}, LADDER).score
                   for s in st])
buckets = bucket_path(scores, grid=(0.5, 0.8, 0.95), min_obs=252)

ok = buckets > 0
print(f"Timeline: {dates.iloc[0]:%Y-%m-%d}..{dates.iloc[len(dates)-1]:%Y-%m-%d}; "
      f"{int(ok.sum())} bucketed days (n_blocks=1 throughout — L2 only, stated)")
for b, name in ((1, "R1 normal"), (2, "R2 watch"), (3, "R3 slow bear"), (4, "R4 crisis")):
    print(f"  {name}: {(buckets == b).sum():5d} days ({(buckets == b).sum()/ok.sum():5.1%})")

# R4 episodes: contiguous runs of bucket 4
runs, start = [], None
for i in range(len(buckets)):
    if buckets[i] == 4 and start is None:
        start = i
    elif buckets[i] != 4 and start is not None:
        runs.append((start, i - 1)); start = None
if start is not None:
    runs.append((start, len(buckets) - 1))
runs = [(a, b) for a, b in runs if b - a >= 2]   # >= 3 sessions to list
print(f"\nR4 (crisis-bucket) episodes of >= 3 sessions: {len(runs)}")
for a, b in runs:
    print(f"  {dates.iloc[a]:%Y-%m-%d} .. {dates.iloc[b]:%Y-%m-%d}  ({b-a+1} sessions)")
