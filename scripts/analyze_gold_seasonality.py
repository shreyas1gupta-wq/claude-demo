"""Atlas 4.9 — GS1: gold festival-seasonality demonstration (pre-registered).

Ledger 2026-09-02. Float era only (1972-01 onward). Kruskal-Wallis of monthly log returns
across the 12 calendar months; interpretation rule pre-stated (CONTEXT verdict stands
regardless of print — see the ledger entry). September median reported descriptively.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "commodities"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

df = pd.read_csv(VAULT / "gold_monthly_1833_2026.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m")
df = df[df["Date"] >= "1972-01-01"].reset_index(drop=True)
df["ret"] = np.log(df["Price"]).diff() * 100
df = df.dropna(subset=["ret"])
df["month"] = df["Date"].dt.month
print(f"Float-era sample: {df['Date'].min():%Y-%m}..{df['Date'].max():%Y-%m} n={len(df)}")

med = df.groupby("month")["ret"].median()
rk = med.rank(ascending=False).astype(int)
print("\nMedian monthly log return (%) by calendar month:")
for m in range(1, 13):
    n = (df["month"] == m).sum()
    print(f"  {MONTHS[m-1]}: {med[m]:+.2f}  rank={rk[m]}  n={n}")

groups = [df.loc[df["month"] == m, "ret"].values for m in range(1, 13)]
h, p = stats.kruskal(*groups)
print(f"\nGS1: Kruskal-Wallis H={h:.2f}, p={p:.3f}")
print(f"September (the folk claim), descriptive: median {med[9]:+.2f}, rank {rk[9]}/12")
print("GS1 interpretation (pre-stated): 4.9 CONTEXT verdict stands regardless — "
      + ("print consistent with NO world-price festival structure" if p >= 0.05
         else "p<0.05 logged under the 12-way caution; no mechanism for festivals to move the world price"))
