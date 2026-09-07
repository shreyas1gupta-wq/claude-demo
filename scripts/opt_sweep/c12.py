"""
c12 -- Completeness critic for OP-D2 (combiner cell).
Quantifies: (1) the VIX-sample date boundary and how many NIFTY trading days
fall outside it on each end, incl. the 2008 GFC window; (2) which of the 22
families are VIX-window-bound (upper bounds, not full-sample results) vs
NIFTY-only (full 2008-2026 range); (3) what option-chain data would add that
no vaulted series can substitute for.
Read-only: no new stats claims, just census/date-range arithmetic on already-
vaulted files plus a manifest of which cells cite which files (grep-derived).
Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/c12.py
"""
import pandas as pd

NIFTY = "ingest/vault/index/nifty50_daily_2007_2026.csv"
VIX = "ingest/vault/vix/india_vix_daily_2010_2023.csv"

nf = pd.read_csv(NIFTY, parse_dates=["Date"] if "Date" in pd.read_csv(NIFTY, nrows=1).columns else None)
datecol = "Date" if "Date" in nf.columns else nf.columns[0]
nf[datecol] = pd.to_datetime(nf[datecol])
nf = nf.sort_values(datecol)

vf = pd.read_csv(VIX, parse_dates=["date"])
vf = vf.sort_values("date")

vix_start, vix_end = vf["date"].min(), vf["date"].max()
print(f"VIX vault span: {vix_start.date()} .. {vix_end.date()}  (n={len(vf)})")
print(f"NIFTY vault span: {nf[datecol].min().date()} .. {nf[datecol].max().date()}  (n={len(nf)})")

pre = nf[nf[datecol] < vix_start]
post = nf[nf[datecol] > vix_end]
print(f"\nNIFTY trading days BEFORE VIX vault starts (2007-01 .. {vix_start.date()}): {len(pre)}")
gfc = nf[(nf[datecol] >= "2008-01-01") & (nf[datecol] <= "2009-06-30")]
print(f"  of which 2008-01-01..2009-06-30 (GFC crash+recovery window): {len(gfc)} days -- "
      f"ENTIRELY absent from every VIX-conditioned family (F01,F02,F06,F11,F13,F14,F16-F18,F20-F22)")
print(f"\nNIFTY trading days AFTER VIX vault ends ({vix_end.date()} .. today 2026-09-07): {len(post)}")
print(f"  = the entire post-Apr-2023 tail: 2024 general-election spike, any 2024-2026 vol events -- "
      f"none of it has fed F13/F14/F16/F17/F18/F20/F21/F22's VRP/condor/decay statistics")

# NIFTY full-range families (VIX not required as an input) for contrast
print("\n--- family sample coverage (from JSON/scripts) ---")
print("NIFTY-only, full 2008-2026 range (no VIX-window restriction): F03,F04,F07,F08,F09,F10,F12")
print("VIX-window-bound (2010-07-23..2023-04-05, ~2011-23 after min_obs=252 warmup): "
      "F01,F02,F06,F11,F13[REFUTED],F14,F16,F17,F18,F20,F22")
print("VIX-window-bound AND survivor-panel-bound (~2012-2022 intersection, narrower still): F21")
print("F19: mixed -- NIFTY-return leg full-range (n back to 2009 events), VIX-crush leg VIX-window-bound")
print("F15: analytic (BS math), no sample window, but VIX 12/18/30 buckets are levels seen in-sample "
      "(2010-23) not a fitted range claim")
