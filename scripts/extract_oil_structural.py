"""Extract the Kilian index + Känzig oil-supply-news vault files and run pass-2 anchors.

Specs and bars are FIXED in ingest/vault/commodities/AUTHENTICATION.md (2026-09-03 section,
committed before this ran). Results are appended there by hand (pass 2).
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
COM = ROOT / "ingest" / "vault" / "commodities"


def flag(ok):
    return "PASS" if ok else "MISS"


# ---- File 1: Kilian index ----
d = pd.read_excel(COM / "kilian_replication_raw.xlsx", usecols=["Data", "Kilian_Index"])
d = d.rename(columns={"Data": "date", "Kilian_Index": "kilian_index"}).sort_values("date")
d.to_csv(COM / "kilian_index_monthly_1973_2019.csv", index=False)
s = pd.Series(d["kilian_index"].values, index=pd.to_datetime(d["date"]))
print(f"Kilian extracted: {len(s)} rows {s.index.min():%Y-%m}..{s.index.max():%Y-%m}")

k1 = pd.Timestamp("2007-01-01") <= s.idxmax() <= pd.Timestamp("2008-10-31")
print(f"K1 {flag(k1)}: sample max {s.max():.1f} on {s.idxmax():%Y-%m}")
dec10 = np.quantile(s, 0.10)
k2 = (s.loc["2008-10":"2009-12"] <= dec10).any()
print(f"K2 {flag(k2)}: min in 2008-10..2009-12 = {s.loc['2008-10':'2009-12'].min():.1f} vs 10th pct {dec10:.1f}")
q25 = np.quantile(s, 0.25)
k3 = (s.loc["1974-01":"1975-12"] <= q25).any()
print(f"K3 {flag(k3)}: min in 1974-75 = {s.loc['1974-01':'1975-12'].min():.1f} vs 25th pct {q25:.1f}")

p = pd.read_csv(COM / "imf_pcps_monthly_1980_2017.csv")
dcol = [c for c in p.columns if "date" in c.lower() or "month" in c.lower()][0]
acol = [c for c in p.columns if "all" in c.lower()][0]
pc = pd.Series(p[acol].values, index=pd.to_datetime(p[dcol])).dropna()
yoy = pc.pct_change(12) * 100
both = pd.concat([s, yoy], axis=1, keys=["k", "y"], sort=True).loc["1981-01":"2017-12"].dropna()
rho, _ = stats.spearmanr(both["k"], both["y"])
k4 = rho >= 0.25
print(f"K4 {flag(k4)}: Spearman(Kilian, PCPS All-Comm YoY) = {rho:.3f} over {len(both)} months")

months = pd.period_range(s.index.min(), s.index.max(), freq="M")
k5 = (len(s) == 558 and len(months) == 558 and (s > 0).any() and (s < 0).any()
      and (s.abs() <= 300).all())
print(f"K5 {flag(k5)}: 558 contiguous={len(months) == 558}, signs both={bool((s > 0).any() and (s < 0).any())}, max|v|={s.abs().max():.1f}")

# ---- File 2: Känzig shocks ----
xl = pd.ExcelFile(COM / "oil_supply_news_2025M12_raw.xlsx")
m = xl.parse("Monthly")
m.columns = ["date", "surprise", "news_shock"]
m.to_csv(COM / "oil_supply_news_monthly_1975_2025.csv", index=False)
day = xl.parse("Daily")
day.columns = ["date", "surprise"] if day.shape[1] == 2 else list(day.columns)
day["date"] = pd.to_datetime(day.iloc[:, 0])
ds = pd.Series(day.iloc[:, 1].values, index=day["date"])
print(f"\nKänzig: Monthly {len(m)} rows {m['date'].iloc[0]}..{m['date'].iloc[-1]}; Daily {len(ds)} rows")

for tag, dt, want_neg in (("Z1", "2014-11-27", True), ("Z2", "2016-11-30", False),
                          ("Z3", "2020-03-06", True)):
    v = ds.get(pd.Timestamp(dt))
    ok = v is not None and ((v < 0) if want_neg else (v > 0))
    print(f"{tag} {flag(bool(ok))}: {dt} daily surprise = {v}")

ns = pd.to_numeric(m["news_shock"], errors="coerce").dropna()
z4 = (len(m) == 612 and str(m['date'].iloc[0]) == "1975M01" and str(m['date'].iloc[-1]) == "2025M12"
      and abs(ns.mean()) < 0.5 * ns.std())
print(f"Z4 {flag(bool(z4))}: rows={len(m)}, span {m['date'].iloc[0]}..{m['date'].iloc[-1]}, "
      f"news-shock mean {ns.mean():+.4f} vs 0.5*std {0.5 * ns.std():.4f} (n non-NaN {len(ns)})")
