"""QG-D3 — ROE x horizon ladder (fwd 12/36/60/120m). Registered 2026-09-08 BEFORE this
run; method frozen in the ledger (buy-and-hold compounding, >=75% coverage, median
annualized, all-panel + large-cap legs, overlap flagged). Prints + JSON append."""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
dm = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz",
                 usecols=["stock_id", "date", "Roe", "Mkt_Cap_12M_Usd", "R1M_Usd"],
                 parse_dates=["date"])


def dec(s, n):
    return np.minimum((s * n).apply(np.ceil).clip(lower=1), n).astype(int)


dm["roe_d"] = dec(dm.Roe, 10)
dm["roe_q"] = dec(dm.Roe, 5)
dm["size_q"] = dec(dm.Mkt_Cap_12M_Usd, 5)

wide = dm.pivot_table(index="date", columns="stock_id", values="R1M_Usd")
log1 = np.log1p(wide)

HOR = [12, 36, 60, 120]
res_all, res_big, att = {}, {}, {}
for h in HOR:
    s = log1.rolling(h, min_periods=int(np.ceil(0.75 * h))).sum().shift(-(h - 1))
    cnt = log1.notna().rolling(h, min_periods=1).count().shift(-(h - 1))
    ann = np.expm1(s * (12 / h))
    last_form = wide.index[-1] - pd.DateOffset(months=h - 1)
    long = ann.loc[:last_form].stack().rename("ann").reset_index()
    cov = (cnt.loc[:last_form].stack() / h).rename("cov").reset_index()
    long = long.merge(cov, on=["date", "stock_id"])
    m = long.merge(dm[["date", "stock_id", "roe_d", "roe_q", "size_q"]], on=["date", "stock_id"])
    full = m[m["cov"] >= 0.999]
    res_all[h] = (m.groupby("roe_d").ann.median() * 100).round(2)
    big = m[m.size_q == 5]
    res_big[h] = (big.groupby("roe_q").ann.median() * 100).round(2)
    a1 = full[full.roe_d == 1].shape[0] / max(m[m.roe_d == 1].shape[0], 1)
    a10 = full[full.roe_d == 10].shape[0] / max(m[m.roe_d == 10].shape[0], 1)
    att[h] = (round(100 * a1), round(100 * a10))

print("QG-D3 — ROE x horizon, median ANNUALIZED fwd return %/yr (overlapping formations, flagged):")
print("\n  h1-h4 ALL-PANEL deciles (EW; artifact-contaminated per QG-D2 — shown for the record):")
hdr = "  hor  " + " ".join(f"D{d:>2}" for d in range(1, 11)) + "   D10-D1"
print(hdr)
J3 = {"all": {}, "big": {}, "attrition": {}, "spread": {}}
for h in HOR:
    r = res_all[h]
    row = " ".join(f"{r.get(d, np.nan):5.1f}" for d in range(1, 11))
    sp = r.get(10, np.nan) - r.get(1, np.nan)
    print(f"  {h:>3}m {row}  {sp:+6.1f}")
    J3["all"][h] = {int(k): float(v) for k, v in r.items()}
    J3["spread"][h] = {"panel_D10_D1": round(float(sp), 2)}
print("\n  h5-h8 LARGE-CAP ONLY (size Q5), ROE quintiles:")
print("  hor    Q1    Q2    Q3    Q4    Q5   Q5-Q1")
for h in HOR:
    r = res_big[h]
    row = " ".join(f"{r.get(q, np.nan):5.1f}" for q in range(1, 6))
    sp = r.get(5, np.nan) - r.get(1, np.nan)
    print(f"  {h:>3}m {row}  {sp:+6.1f}")
    J3["big"][h] = {int(k): float(v) for k, v in r.items()}
    J3["spread"][h]["bigcap_Q5_Q1"] = round(float(sp), 2)
print("\n  h9 attrition (share of formation rows with FULL coverage, D1 junk vs D10 quality):")
for h in HOR:
    print(f"  {h:>3}m: D1 {att[h][0]}% vs D10 {att[h][1]}%")
    J3["attrition"][h] = {"D1_full_pct": att[h][0], "D10_full_pct": att[h][1]}
print("\n  h10 spreads by horizon:", {h: J3["spread"][h] for h in HOR})

J = json.load(open("/home/user/claude-demo/research/notes/qg_d2_stats.json"))
J["qg_d3"] = J3
json.dump(J, open("/home/user/claude-demo/research/notes/qg_d2_stats.json", "w"))
print("JSON updated.")
