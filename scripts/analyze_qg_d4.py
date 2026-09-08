"""QG-D4 — growth x horizon + ROExGROWTH / GROWTHxVOL / ROExVOL matrices at
12/36/60/120m. Registered 2026-09-08 BEFORE this run; QG-D3 method verbatim.
Prints + JSON append for the dashboard."""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
dm = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz",
                 usecols=["stock_id", "date", "Roe", "Eps_Basic_Gr", "Vol1Y_Usd",
                          "Mkt_Cap_12M_Usd", "R1M_Usd"], parse_dates=["date"])


def dec(s, n):
    return np.minimum((s * n).apply(np.ceil).clip(lower=1), n).astype(int)


dm["gr_d"] = dec(dm.Eps_Basic_Gr, 10)
dm["gr_q"] = dec(dm.Eps_Basic_Gr, 5)
dm["roe_q"] = dec(dm.Roe, 5)
dm["vol_q"] = dec(dm.Vol1Y_Usd, 5)
dm["size_q"] = dec(dm.Mkt_Cap_12M_Usd, 5)

wide = dm.pivot_table(index="date", columns="stock_id", values="R1M_Usd")
log1 = np.log1p(wide)
HOR = [12, 36, 60, 120]
J4 = {"g_all": {}, "g_big": {}, "roe_gr": {}, "gr_vol": {}, "roe_vol": {}, "corners60": {}}

for h in HOR:
    s = log1.rolling(h, min_periods=int(np.ceil(0.75 * h))).sum().shift(-(h - 1))
    ann = np.expm1(s * (12 / h))
    last_form = wide.index[-1] - pd.DateOffset(months=h - 1)
    long = ann.loc[:last_form].stack().rename("ann").reset_index()
    m = long.merge(dm[["date", "stock_id", "gr_d", "gr_q", "roe_q", "vol_q", "size_q"]],
                   on=["date", "stock_id"])
    J4["g_all"][h] = {int(k): round(100 * v, 2) for k, v in m.groupby("gr_d").ann.median().items()}
    big = m[m.size_q == 5]
    J4["g_big"][h] = {int(k): round(100 * v, 2) for k, v in big.groupby("gr_q").ann.median().items()}
    for key, qa, qb in [("roe_gr", "roe_q", "gr_q"), ("gr_vol", "gr_q", "vol_q"),
                         ("roe_vol", "roe_q", "vol_q")]:
        t = (m.groupby([qa, qb]).ann.median().unstack() * 100).round(2)
        J4[key][h] = t.values.tolist()
    if h == 60:
        for key, qa, qb in [("roe_gr", "roe_q", "gr_q"), ("gr_vol", "gr_q", "vol_q"),
                             ("roe_vol", "roe_q", "vol_q")]:
            tb = (big.groupby([qa, qb]).ann.median().unstack() * 100).round(1)
            J4["corners60"][key] = {"11": float(tb.loc[1, 1]), "15": float(tb.loc[1, 5]),
                                     "51": float(tb.loc[5, 1]), "55": float(tb.loc[5, 5])}

print("QG-D4 — growth & matrices x horizon, median annualized %/yr (overlap flagged, no-delisting upper bounds):")
print("\n  g1-g4 GROWTH deciles ALL-PANEL:")
print("  hor  " + " ".join(f"D{d:>2}" for d in range(1, 11)) + "  D10-D1")
for h in HOR:
    r = J4["g_all"][h]
    print(f"  {h:>3}m " + " ".join(f"{r[d]:5.1f}" for d in range(1, 11)) +
          f"  {r[10] - r[1]:+6.1f}")
print("\n  g5-g8 GROWTH quintiles LARGE-CAP ONLY:")
print("  hor    Q1    Q2    Q3    Q4    Q5   Q5-Q1")
for h in HOR:
    r = J4["g_big"][h]
    print(f"  {h:>3}m " + " ".join(f"{r[q]:5.1f}" for q in range(1, 6)) + f"  {r[5] - r[1]:+6.1f}")
for key, nm, rows, cols in [("roe_gr", "ROE x GROWTH", "ROE", "growth"),
                              ("gr_vol", "GROWTH x VOL", "growth", "vol"),
                              ("roe_vol", "ROE x VOL", "ROE", "vol")]:
    print(f"\n  {nm} 5x5 by horizon (rows={rows} Q1..Q5 top-to-bottom, cols={cols} Q1..Q5):")
    for h in HOR:
        a = np.array(J4[key][h])
        best = np.unravel_index(np.nanargmax(a), a.shape)
        worst = np.unravel_index(np.nanargmin(a), a.shape)
        print(f"  {h:>3}m best ({rows}Q{best[0] + 1},{cols}Q{best[1] + 1}) {a[best]:.1f} | "
              f"worst ({rows}Q{worst[0] + 1},{cols}Q{worst[1] + 1}) {a[worst]:.1f} | "
              f"corners 11/15/51/55: {a[0, 0]:.1f}/{a[0, 4]:.1f}/{a[4, 0]:.1f}/{a[4, 4]:.1f}")
print("\n  k1-k3 LARGE-CAP corner check at 60m (corners RxQ1C1/R1C5/R5C1/R5C5):")
for key, nm in [("roe_gr", "ROExGROWTH"), ("gr_vol", "GROWTHxVOL"), ("roe_vol", "ROExVOL")]:
    c = J4["corners60"][key]
    print(f"    {nm}: {c['11']:.1f} / {c['15']:.1f} / {c['51']:.1f} / {c['55']:.1f}")

J = json.load(open("/home/user/claude-demo/research/notes/qg_d2_stats.json"))
J["qg_d4"] = J4
json.dump(J, open("/home/user/claude-demo/research/notes/qg_d2_stats.json", "w"))
print("JSON updated.")
