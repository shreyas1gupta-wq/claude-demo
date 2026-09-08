"""FUN-D1 — the global business-cycle phase atlas (fundamentals track opener).

Registered 2026-09-08 BEFORE this run. JST r4, 18 economies. Phase quadrants from
dlog(rgdppc) vs country EXPANDING median (min 10 obs) x rising/falling. Real-time
honest: phase in year t conditions returns in year t+1; contemporaneous = descriptive.
Real returns = (1+nominal)/(1+dCPI)-1. Prints only.
"""
import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
j = pd.read_csv(f"{V}/jst/jstdatasetr4.csv")
j = j.sort_values(["country", "year"])

frames = []
for c, g in j.groupby("country"):
    g = g.set_index("year")
    gr = np.log(g["rgdppc"]).diff()
    trend = gr.expanding(10).median().shift(1)  # trend known from PAST years only
    rising = gr > gr.shift(1)
    above = gr > trend
    phase = pd.Series(np.where(above & rising, "EXPANSION",
                      np.where(above & ~rising, "SLOWDOWN",
                      np.where(~above & rising, "RECOVERY", "CONTRACTION"))), index=g.index)
    phase[gr.isna() | trend.isna()] = np.nan
    infl = g["cpi"].pct_change()
    d = pd.DataFrame({"country": c, "phase": phase, "g": gr,
                      "crisis": g["crisisJST"],
                      "infl": infl,
                      "eq": (1 + g["eq_tr"]) / (1 + infl) - 1,
                      "bond": (1 + g["bond_tr"]) / (1 + infl) - 1,
                      "hous": (1 + g["housing_tr"]) / (1 + infl) - 1,
                      "bill": (1 + g["bill_rate"]) / (1 + infl) - 1})
    # expanding median inflation (lagged) for p9
    d["infl_hi"] = infl > infl.expanding(10).median().shift(1)
    for a in ["eq", "bond", "hous", "bill"]:
        d[f"f_{a}"] = d[a].shift(-1)  # NEXT-year return
    frames.append(d.reset_index())
D = pd.concat(frames, ignore_index=True).dropna(subset=["phase"])
PH = ["RECOVERY", "EXPANSION", "SLOWDOWN", "CONTRACTION"]

print(f"FUN-D1 — JST phase atlas: {D.country.nunique()} countries, "
      f"{len(D)} country-years with a phase, {D.year.min():.0f}-{D.year.max():.0f}")

# p1 frequencies + stickiness
freq = D.phase.value_counts(normalize=True)
same = (D.sort_values(['country', 'year']).groupby("country").phase
        .apply(lambda s: (s == s.shift(1)).mean()))
print("  p1 frequencies: " + " ".join(f"{p} {100*freq.get(p, 0):.0f}%" for p in PH)
      + f" | 1y phase persistence {100*same.mean():.0f}% (BC3 booked 77% for its def)")

# p2-p5 next-year real returns by phase
for a, nm in [("f_eq", "p2 equity"), ("f_bond", "p3 bonds"), ("f_hous", "p4 housing"),
              ("f_bill", "p5 bills")]:
    row = []
    for p in PH:
        d_ = D[D.phase == p][a].dropna()
        row.append(f"{p[:4]} {100*d_.median():+5.1f}% (n={len(d_)})")
    print(f"  {nm} NEXT-yr real median: " + " | ".join(row))

# p6 contemporaneous equity (descriptive)
row = [f"{p[:4]} {100*D.loc[D.phase == p, 'eq'].median():+5.1f}%" for p in PH]
print("  p6 SAME-yr equity (descriptive): " + " | ".join(row))

# p7 recovery vs expansion, within-country
agree = []
for c, g in D.groupby("country"):
    r_ = g[g.phase == "RECOVERY"].f_eq.dropna()
    e_ = g[g.phase == "EXPANSION"].f_eq.dropna()
    if len(r_) >= 5 and len(e_) >= 5:
        agree.append(r_.median() > e_.median())
rec = D[D.phase == "RECOVERY"].f_eq.dropna()
exp_ = D[D.phase == "EXPANSION"].f_eq.dropna()
print(f"  p7 RECOVERY vs EXPANSION next-yr equity: {100*rec.median():+.1f}% vs "
      f"{100*exp_.median():+.1f}% (gap {100*(rec.median()-exp_.median()):+.1f}pp); "
      f"recovery wins in {sum(agree)}/{len(agree)} countries")

# p8 contraction x crisis
con = D[D.phase == "CONTRACTION"]
cc = con[con.crisis == 1].f_eq.dropna()
cn = con[con.crisis == 0].f_eq.dropna()
print(f"  p8 CONTRACTION next-yr equity: with crisis {100*cc.median():+.1f}% (n={len(cc)}) "
      f"vs without {100*cn.median():+.1f}% (n={len(cn)})")

# p9 phase x inflation regime (next-yr equity)
row = []
for p in PH:
    hi = D[(D.phase == p) & (D.infl_hi == True)].f_eq.dropna()   # noqa: E712
    lo = D[(D.phase == p) & (D.infl_hi == False)].f_eq.dropna()  # noqa: E712
    row.append(f"{p[:4]} hi{100*hi.median():+5.1f}/lo{100*lo.median():+5.1f}")
print("  p9 next-yr equity, phase x inflation(hi/lo): " + " | ".join(row))

# p10 post-1950
D5 = D[D.year >= 1950]
row = [f"{p[:4]} {100*D5[D5.phase == p].f_eq.dropna().median():+5.1f}%" for p in PH]
print("  p10 post-1950 next-yr equity: " + " | ".join(row))
