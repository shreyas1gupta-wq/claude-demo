"""Atlas 4.1/4.2/4.11 — the calendar-as-signal trials (CW1-CW3).

Pre-registered in research/register/trial-ledger.md (2026-09-02) BEFORE running.
Data: ingest/vault/factors/iima_monthly_factors.csv (IIMA India factors, monthly).

CW1: Budget-month vol — February |MF| rank among 12 months + one-sided Mann-Whitney.
CW2: FY-end small-cap reversal — April SMB rank + median>0 + one-sided Mann-Whitney.
CW3: month-of-year omnibus — Kruskal-Wallis across 12 months (demonstration; the
     4.11 REJECT stands regardless of print, per the pre-stated interpretation rule).
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "factors"

df = pd.read_csv(VAULT / "iima_monthly_factors.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m")
df["month"] = df["Date"].dt.month
mf = df.dropna(subset=["MF"]).copy()
smb = df.dropna(subset=["SMB"]).copy()
print(f"MF sample: {mf['Date'].min():%Y-%m}..{mf['Date'].max():%Y-%m} n={len(mf)}")
print(f"SMB sample: {smb['Date'].min():%Y-%m}..{smb['Date'].max():%Y-%m} n={len(smb)}")

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# ---------------- CW1: February |MF| ----------------
mf["absMF"] = mf["MF"].abs()
med_by_month = mf.groupby("month")["absMF"].median()
ranks = med_by_month.rank(ascending=False).astype(int)  # 1 = highest median |MF|
print("\nCW1 — median |MF| by month (rank 1 = most volatile):")
for m in range(1, 13):
    n = (mf["month"] == m).sum()
    print(f"  {MONTHS[m-1]}: median|MF|={med_by_month[m]:.2f}  rank={ranks[m]}  n={n}")
feb = mf.loc[mf["month"] == 2, "absMF"]
nonfeb = mf.loc[mf["month"] != 2, "absMF"]
u, p_cw1 = stats.mannwhitneyu(feb, nonfeb, alternative="greater")
feb_rank = ranks[2]
cw1_pass = (feb_rank <= 3) and (p_cw1 < 0.10)
print(f"CW1: Feb median|MF|={feb.median():.2f} vs non-Feb {nonfeb.median():.2f}; "
      f"rank={feb_rank}/12; MW one-sided p={p_cw1:.3f}")
print(f"CW1 BAR (rank<=3 AND p<0.10): {'PASS' if cw1_pass else 'FAIL'}")

# ---------------- CW2: April SMB ----------------
smb_med = smb.groupby("month")["SMB"].median()
smb_ranks = smb_med.rank(ascending=False).astype(int)  # 1 = highest median SMB
print("\nCW2 — median SMB by month (rank 1 = highest):")
for m in range(1, 13):
    print(f"  {MONTHS[m-1]}: medianSMB={smb_med[m]:+.2f}  rank={smb_ranks[m]}")
apr = smb.loc[smb["month"] == 4, "SMB"]
nonapr = smb.loc[smb["month"] != 4, "SMB"]
u2, p_cw2 = stats.mannwhitneyu(apr, nonapr, alternative="greater")
apr_rank = smb_ranks[4]
cw2_pass = (apr_rank <= 2) and (apr.median() > 0) and (p_cw2 < 0.10)
print(f"CW2: Apr median SMB={apr.median():+.2f} (n={len(apr)}); rank={apr_rank}/12; "
      f"MW one-sided p={p_cw2:.3f}")
print(f"CW2 BAR (rank<=2 AND median>0 AND p<0.10): {'PASS' if cw2_pass else 'FAIL'}")

# ---------------- CW3: omnibus (demonstration) ----------------
groups = [mf.loc[mf["month"] == m, "MF"].values for m in range(1, 13)]
h, p_cw3 = stats.kruskal(*groups)
print(f"\nCW3: Kruskal-Wallis MF across 12 months: H={h:.2f}, p={p_cw3:.3f}")
best = mf.groupby("month")["MF"].median().rank(ascending=False).astype(int)
top_m = int(best[best == 1].index[0])
print(f"  (highest median-MF month, logged not promoted: {MONTHS[top_m-1]})")
print("CW3 interpretation (pre-stated): REJECT of 4.11 stands regardless — "
      + ("print consistent with NO calendar structure" if p_cw3 >= 0.05
         else "p<0.05 logged as expected false-positive risk under 12-way comparison; NOT promoted"))
