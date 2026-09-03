"""H53a — the ToT->INR first link (pre-registered).

Ledger 2026-09-02. Non-overlapping Dec-to-Dec annual log changes, 1980-2017 overlap.
Primary: PCPS Fuel(Energy) vs INR/USD (positive = depreciation). Bar: Spearman rho>0,
one-sided p<0.10. Secondary (no bar): All-Commodity.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault"

pcps = pd.read_csv(VAULT / "commodities" / "imf_pcps_monthly_1980_2017.csv", parse_dates=["Date"]).set_index("Date")
inr = pd.read_csv(VAULT / "fx" / "inr_usd_monthly_1973_2026.csv", parse_dates=["Date"]).set_index("Date")["INR_per_USD"]

def dec_changes(s):
    dec = s[s.index.month == 12].dropna()
    return np.log(dec).diff().dropna()

d_inr = dec_changes(inr)
for name, col, is_primary in (("Fuel/Energy", "Fuel Energy Index", True),
                              ("All-Commodity", "All Commodity Price Index", False)):
    d_c = dec_changes(pcps[col])
    j = pd.concat([d_c.rename("c"), d_inr.rename("inr")], axis=1, join="inner").dropna()
    rho, p2 = stats.spearmanr(j["c"], j["inr"])
    p1 = p2 / 2 if rho > 0 else 1 - p2 / 2
    tag = "PRIMARY" if is_primary else "secondary (no bar)"
    print(f"H53a {tag}: {name} n={len(j)} ({j.index.min().year}-{j.index.max().year}) "
          f"Spearman rho={rho:+.3f}, one-sided p={p1:.3f}"
          + (f" -> BAR (rho>0, p<0.10): {'PASS' if rho > 0 and p1 < 0.10 else 'FAIL'}" if is_primary else ""))
