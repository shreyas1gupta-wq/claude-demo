"""FUN-D8 — the regime-identification battery (JST annual, 17 economies).

Registered 2026-09-08 BEFORE this run. Year-t states condition year t+1 real returns;
country expanding medians/terciles (min 10 obs); FUN-D1's frozen growth quadrants
reused verbatim. Prints only.
"""
import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
j = pd.read_csv(f"{V}/jst/jstdatasetr4.csv").sort_values(["country", "year"])

frames = []
for c, g in j.groupby("country"):
    g = g.set_index("year")
    gr = np.log(g["rgdppc"]).diff()
    trend = gr.expanding(10).median().shift(1)
    rising = gr > gr.shift(1)
    above = gr > trend
    phase = pd.Series(np.where(above & rising, "EXPANSION",
                      np.where(above & ~rising, "SLOWDOWN",
                      np.where(~above & rising, "RECOVERY", "CONTRACTION"))), index=g.index)
    phase[gr.isna() | trend.isna()] = np.nan
    infl = g["cpi"].pct_change()
    slope = g["ltrate"] - g["stir"]
    d = pd.DataFrame({
        "country": c, "phase": phase,
        "rate_up": g["stir"] > g["stir"].shift(1),
        "slope": slope,
        "realrate": g["stir"] / 100 - infl,
        "credit_acc": (g["tloans"] / g["gdp"]).diff(),
        "iy": g["iy"],
        "above": above,
        "eq": (1 + g["eq_tr"]) / (1 + infl) - 1,
        "bond": (1 + g["bond_tr"]) / (1 + infl) - 1,
        "hous": (1 + g["housing_tr"]) / (1 + infl) - 1,
    })
    for col in ["slope", "realrate"]:
        m = d[col].expanding(10)
        d[f"{col}_t"] = np.where(d[col] <= m.quantile(1 / 3).shift(1), "LO",
                        np.where(d[col] <= m.quantile(2 / 3).shift(1), "MID", "HI"))
        d.loc[d[col].isna(), f"{col}_t"] = np.nan
    d["credit_hi"] = d["credit_acc"] > d["credit_acc"].expanding(10).median().shift(1)
    d["iy_hi"] = d["iy"] > d["iy"].expanding(10).median().shift(1)
    for a in ["eq", "bond", "hous"]:
        d[f"f_{a}"] = d[a].shift(-1)
    d["f_contraction"] = (phase.shift(-1) == "CONTRACTION").astype(float)
    d.loc[phase.shift(-1).isna(), "f_contraction"] = np.nan
    frames.append(d.reset_index())
D = pd.concat(frames, ignore_index=True)

print(f"FUN-D8 — regime battery: {D.country.nunique()} countries, {D.year.min():.0f}-{D.year.max():.0f}")

# m1 rate direction
for a, nm in [("f_eq", "equity"), ("f_bond", "bonds")]:
    up = D[D.rate_up == True][a].dropna()   # noqa: E712
    dn = D[D.rate_up == False][a].dropna()  # noqa: E712
    print(f"  m1 {nm} next-yr real by SHORT-RATE direction: rising {100*up.median():+.1f}% "
          f"(n={len(up)}) vs falling {100*dn.median():+.1f}% (n={len(dn)})")

# m2 curve slope terciles
for a, nm in [("f_eq", "equity"), ("f_bond", "bonds")]:
    row = [f"{t} {100*D[D.slope_t == t][a].dropna().median():+.1f}%" for t in ["LO", "MID", "HI"]]
    print(f"  m2 {nm} next-yr real by CURVE-SLOPE tercile (LO=flat/inverted): " + " | ".join(row))
row = [f"{t} {100*D[D.slope_t == t].f_contraction.dropna().mean():.0f}%" for t in ["LO", "MID", "HI"]]
print("  m2 P(next-yr CONTRACTION phase) by slope tercile: " + " | ".join(row))

# m3 credit acceleration x growth (Borio joint)
tab = {}
for ch, gh in [(True, True), (True, False), (False, True), (False, False)]:
    d_ = D[(D.credit_hi == ch) & (D.above == gh)].f_eq.dropna()
    tab[(ch, gh)] = (100 * d_.median(), len(d_))
print(f"  m3 next-yr equity, CREDIT-ACC x GROWTH: boom-x-above {tab[(True, True)][0]:+.1f}% "
      f"(n={tab[(True, True)][1]}) | boom-x-below {tab[(True, False)][0]:+.1f}% | "
      f"calm-x-above {tab[(False, True)][0]:+.1f}% | CALM-x-BELOW {tab[(False, False)][0]:+.1f}% "
      f"(n={tab[(False, False)][1]})")
print(f"  m3 corner spread (calm-slump minus credit-boom-boom): "
      f"{tab[(False, False)][0] - tab[(True, True)][0]:+.1f}pp")

# m4 investment share
hi = D[D.iy_hi == True].f_eq.dropna()   # noqa: E712
lo = D[D.iy_hi == False].f_eq.dropna()  # noqa: E712
print(f"  m4 next-yr equity by INVESTMENT SHARE: high {100*hi.median():+.1f}% vs low {100*lo.median():+.1f}%")

# m7 real-rate terciles
for a, nm in [("f_eq", "equity"), ("f_bond", "bonds"), ("f_hous", "housing")]:
    row = [f"{t} {100*D[D.realrate_t == t][a].dropna().median():+.1f}%" for t in ["LO", "MID", "HI"]]
    print(f"  m7 {nm} next-yr real by REAL-RATE tercile: " + " | ".join(row))

# m5 joint seasons: phase x rate direction
PH = ["RECOVERY", "EXPANSION", "SLOWDOWN", "CONTRACTION"]


def seasons(D_):
    out = []
    for p in PH:
        for rd, tag in [(False, "cut"), (True, "hike")]:
            d_ = D_[(D_.phase == p) & (D_.rate_up == rd)].f_eq.dropna()
            out.append(f"{p[:4]}/{tag} {100*d_.median():+.1f}(n={len(d_)})")
    return " | ".join(out)


print("  m5 SEASONS (phase x rate dir, next-yr equity): " + seasons(D))
print("  m8 post-1950: " + seasons(D[D.year >= 1950]))
