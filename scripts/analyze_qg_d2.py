"""QG-D2 — the ROE/growth/quality decile-and-matrix battery. Registered 2026-09-08
BEFORE this run (30 cells, conventions frozen in the ledger). Sources: authenticated
firm_panel/data_ml (EW, rank sorts, fwd returns, survivorship-tilt declared) and
factors_us FF5/FF6/Q5. Prints + JSON for the dashboard. Zero costs, paper.
"""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
OUT = {}

dm = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", parse_dates=["date"])
J = {}


def dec(s, n=10):
    return np.minimum((s * n).apply(np.ceil).clip(lower=1), n).astype(int)


dm["roe_d"] = dec(dm.Roe)
dm["roce_d"] = dec(dm.Roce)
dm["gr_d"] = dec(dm.Eps_Basic_Gr)
dm["capex_d"] = dec(dm.Capex_Sales)
for c, q in [("Roe", "roe_q"), ("Eps_Basic_Gr", "gr_q"), ("Pb", "pb_q"),
             ("Mom_11M_Usd", "mom_q"), ("Mkt_Cap_12M_Usd", "size_q"),
             ("Debtequity", "lev_q"), ("Vol1Y_Usd", "vol_q")]:
    dm[q] = dec(dm[c], 5)
dm["qual"] = dec((dm.Roe + dm.Ocf_Ta + (1 - dm.Debtequity)) / 3)

yrs = 20.33  # 1998-11..2019-03 fwd months


def ladder(col, ret="R1M_Usd"):
    l_ = dm.groupby(col)[ret].mean() * (12 if ret == "R1M_Usd" else 1)
    return {int(k): round(100 * v, 2) for k, v in l_.items()}


def series_dec(col, d):
    m = dm[dm[col] == d].groupby("date").R1M_Usd.mean()
    return m


def stats(m):
    eq = (1 + m).cumprod()
    cagr = 100 * (eq.iloc[-1] ** (12 / len(m)) - 1)
    sh = m.mean() / m.std() * np.sqrt(12)
    dd = 100 * (eq / eq.cummax() - 1).min()
    return round(cagr, 2), round(sh, 2), round(dd, 1)


print("QG-D2 — decile/matrix battery (data_ml 1999-2019 EW fwd-1m, ann. x12; FF/Q factors):")
J["c1"] = ladder("roe_d")
print("  c1 ROE ladder %/yr:", J["c1"], "| D10-D1:", round(J["c1"][10] - J["c1"][1], 2))
d10, d1 = series_dec("roe_d", 10), series_dec("roe_d", 1)
s10, s1 = stats(d10), stats(d1)
tw = float(((1 + d10).prod()) / ((1 + d1).prod()))
J["c2"] = {"D10": s10, "D1": s1, "terminal_wealth_ratio": round(tw, 2)}
print(f"  c2 compounding: D10 CAGR {s10[0]}% Sharpe {s10[1]} maxDD {s10[2]}% | "
      f"D1 {s1[0]}%/{s1[1]}/{s1[2]}% | terminal wealth D10/D1 = {tw:.2f}x")
e1 = dm[dm.date <= "2008-12-31"]; e2 = dm[dm.date > "2008-12-31"]
J["c3"] = {"era1_D10_D1": round(12 * 100 * (e1[e1.roe_d == 10].R1M_Usd.mean() - e1[e1.roe_d == 1].R1M_Usd.mean()), 2),
           "era2_D10_D1": round(12 * 100 * (e2[e2.roe_d == 10].R1M_Usd.mean() - e2[e2.roe_d == 1].R1M_Usd.mean()), 2)}
print("  c3 D10-D1 by era (%/yr):", J["c3"])
J["c4"] = {"D10_vol": round(100 * d10.std() * np.sqrt(12), 1), "D1_vol": round(100 * d1.std() * np.sqrt(12), 1)}
print(f"  c4 vols: D10 {J['c4']['D10_vol']}% vs D1 {J['c4']['D1_vol']}% (Sharpe/DD in c2)")
J["c5"] = ladder("roce_d")
print("  c5 ROCE ladder:", {k: J["c5"][k] for k in (1, 5, 10)}, "| D10-D1:", round(J["c5"][10] - J["c5"][1], 2))
J["c6"] = ladder("gr_d")
print("  c6 EPS-GROWTH ladder:", J["c6"], "| D10-D1:", round(J["c6"][10] - J["c6"][1], 2))
J["c7"] = ladder("capex_d")
print("  c7 CAPEX/SALES ladder:", {k: J["c7"][k] for k in (1, 5, 10)}, "| D10-D1:", round(J["c7"][10] - J["c7"][1], 2))


def matrix(qa, qb):
    t = dm.groupby([qa, qb]).R1M_Usd.mean().unstack() * 1200
    return t.round(2)


for cell, qa, qb, nm in [("c8", "roe_q", "gr_q", "ROE x EPS-GROWTH"),
                          ("c9", "roe_q", "pb_q", "ROE x P/B"),
                          ("c10", "roe_q", "mom_q", "ROE x MOMENTUM"),
                          ("c11", "roe_q", "size_q", "ROE x SIZE"),
                          ("c12", "roe_q", "lev_q", "ROE x LEVERAGE"),
                          ("c13", "roe_q", "vol_q", "ROE x VOL")]:
    t = matrix(qa, qb)
    J[cell] = t.values.tolist()
    best = t.stack().idxmax(); worst = t.stack().idxmin()
    print(f"  {cell} {nm} 5x5 (%/yr): best cell {best} {t.stack().max():.1f} | "
          f"worst {worst} {t.stack().min():.1f} | Q5 row: {list(t.loc[5].round(1))}")
J["c14"] = ladder("qual")
print("  c14 QUALITY COMPOSITE ladder:", {k: J["c14"][k] for k in (1, 5, 10)}, "| D10-D1:",
      round(J["c14"][10] - J["c14"][1], 2))
cheap = dm[dm.Pb <= 0.5]; exp_ = dm[dm.Pb > 0.5]
J["c15"] = {int(k): round(1200 * v, 2) for k, v in cheap.groupby("roe_d").R1M_Usd.mean().items()}
J["c16"] = {int(k): round(1200 * v, 2) for k, v in exp_.groupby("roe_d").R1M_Usd.mean().items()}
print("  c15 ROE ladder WITHIN CHEAP: D1", J["c15"][1], "D10", J["c15"][10], "spread", round(J["c15"][10]-J["c15"][1], 2))
print("  c16 within EXPENSIVE: D1", J["c16"][1], "D10", J["c16"][10], "spread", round(J["c16"][10]-J["c16"][1], 2))
hi = dm[dm.roe_d >= 8].copy()
hi["gt"] = dec(hi.Eps_Basic_Gr, 3)
J["c17"] = {int(k): round(1200 * v, 2) for k, v in hi.groupby("gt").R1M_Usd.mean().items()}
print("  c17 growth terciles WITHIN high-ROE:", J["c17"])
pv = dm.pivot_table(index="date", columns="stock_id", values="Roe")
ac = pv.rank(axis=1).apply(lambda r: r, axis=1).corrwith(pv.rank(axis=1).shift(12), axis=1).mean()
stay = (dm.sort_values(["stock_id", "date"]).groupby("stock_id").roe_d
        .apply(lambda s: (s == s.shift(12)).mean())).mean()
J["c18"] = {"rank_autocorr_12m": round(float(ac), 2), "same_decile_12m": round(float(stay), 2)}
print("  c18 ROE persistence: 12m rank-autocorr", J["c18"]["rank_autocorr_12m"],
      "| P(same decile after 12m)", J["c18"]["same_decile_12m"])
ew = dm.groupby("date").R1M_Usd.mean()
up = ew[ew > 0].index; dn = ew[ew <= 0].index
sp = (series_dec("roe_d", 10) - series_dec("roe_d", 1))
J["c19"] = {"up": round(1200 * sp.reindex(up).mean(), 2), "down": round(1200 * sp.reindex(dn).mean(), 2)}
print("  c19 D10-D1 spread: up-months", J["c19"]["up"], "%/yr | down-months", J["c19"]["down"])
w = slice("2007-10-31", "2009-03-31")
g10 = 100 * ((1 + d10.loc[w]).prod() - 1); g1 = 100 * ((1 + d1.loc[w]).prod() - 1)
J["c20"] = {"D10": round(g10, 1), "D1": round(g1, 1)}
print(f"  c20 GFC (rows 2007-10..2009-03): D10 {g10:+.1f}% vs D1 {g1:+.1f}%")
l12 = dm.groupby("roe_d").R12M_Usd.mean() * 100
J["c21"] = {int(k): round(v, 2) for k, v in l12.items()}
print("  c21 fwd-12M ladder (OVERLAPPING, flagged): D1", J["c21"][1], "D10", J["c21"][10])

ff = pd.read_csv(f"{V}/factors_us/ff6_monthly_1963_2020.csv", parse_dates=["date"]).set_index("date")
q5 = pd.read_csv(f"{V}/factors_us/q5_monthly_1967_2019.csv", parse_dates=["date"]).set_index("date")


def fstats(s):
    eq = (1 + s).cumprod()
    return {"cagr": round(100 * (eq.iloc[-1] ** (12 / len(s)) - 1), 2),
            "sharpe": round(float(s.mean() / s.std() * np.sqrt(12)), 2),
            "maxdd": round(float(100 * (eq / eq.cummax() - 1).min()), 1)}


for cell, s, nm in [("c22", ff.RMW, "RMW 1963-2020"), ("c23", ff.CMA, "CMA"),
                     ("c24", q5.R_ROE, "q R_ROE 1967-2019"), ("c25", q5.R_EG, "q R_EG")]:
    J[cell] = fstats(s.dropna())
    print(f"  {cell} {nm}: {J[cell]}")
fac = pd.concat([ff[["MktRF", "SMB", "HML", "RMW", "CMA", "UMD"]],
                 q5[["R_ROE", "R_EG"]]], axis=1)
J["c26"] = fac.corr().round(2).to_dict()
print("  c26 corr: RMW-HML", J["c26"]["HML"]["RMW"], "| RMW-UMD", J["c26"]["UMD"]["RMW"],
      "| RMW-MktRF", J["c26"]["MktRF"]["RMW"], "| R_EG-RMW", J["c26"]["RMW"]["R_EG"])
dec_t = ff.RMW.groupby(ff.index.year // 10 * 10).mean() * 1200
J["c27"] = {int(k): round(v, 2) for k, v in dec_t.items()}
print("  c27 RMW by decade (%/yr):", J["c27"])
dn_m = ff[ff.MktRF <= 0]; up_m = ff[ff.MktRF > 0]
J["c28"] = {"RMW_down": round(1200 * dn_m.RMW.mean(), 2), "RMW_up": round(1200 * up_m.RMW.mean(), 2),
            "CMA_down": round(1200 * dn_m.CMA.mean(), 2), "CMA_up": round(1200 * up_m.CMA.mean(), 2)}
print("  c28 down/up months:", J["c28"])
bl = 0.5 * ff.HML + 0.5 * ff.RMW
J["c29"] = {"HML": round(float(ff.HML.mean() / ff.HML.std() * np.sqrt(12)), 2),
            "RMW": round(float(ff.RMW.mean() / ff.RMW.std() * np.sqrt(12)), 2),
            "blend": round(float(bl.mean() / bl.std() * np.sqrt(12)), 2)}
print("  c29 Sharpe: HML", J["c29"]["HML"], "RMW", J["c29"]["RMW"], "50/50 blend", J["c29"]["blend"])
pre = ff[ff.index < "2013-01-01"]; post = ff[ff.index >= "2013-01-01"]
J["c30"] = {"RMW_pre13": round(1200 * pre.RMW.mean(), 2), "RMW_post13": round(1200 * post.RMW.mean(), 2),
            "CMA_pre13": round(1200 * pre.CMA.mean(), 2), "CMA_post13": round(1200 * post.CMA.mean(), 2)}
print("  c30 pre/post-2013 (%/yr):", J["c30"])

with open("/home/user/claude-demo/research/notes/qg_d2_stats.json", "w") as f:
    json.dump(J, f)
print("JSON saved.")
