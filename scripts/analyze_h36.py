"""H36-D1 — the 3-year horizon battery (ES/SC arc re-read at 36m forward).
Registered 2026-09-10 BEFORE this run. Parents' methods quoted verbatim:
QG-D3 fwd compounding (buy-and-hold forward R1M over h, >=75% coverage, ann.);
dec() per-date rank buckets; SC-D2/D3 rolling sums for time-series cells.
Prints only; interpretation hand-appended after."""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"

use = ["stock_id", "date", "Eps", "Pb", "Mom_11M_Usd", "Mkt_Cap_12M_Usd", "Roe",
       "Eps_Basic_Gr", "Vol1Y_Usd", "R1M_Usd"]
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", usecols=use, parse_dates=["date"])

# --- QG-D3 forward-compounding convention: fwd 36m/60m annualized, >=75% coverage ---
r = fp.pivot_table(index="date", columns="stock_id", values="R1M_Usd")
lg = np.log1p(r)


def fwd_ann(h):
    s = lg.rolling(h, min_periods=int(h * 0.75)).sum().shift(-(h - 1))
    return (np.exp(s * (12 / h)) - 1) * 100  # annualized %


f36 = fwd_ann(36).stack().rename("f36")
f60 = fwd_ann(60).stack().rename("f60")
eps = fp.pivot_table(index="date", columns="stock_id", values="Eps")
d3 = (eps - eps.shift(3)).stack().rename("d3")
fp = fp.set_index(["date", "stock_id"]).join(f36).join(f60).join(d3).reset_index()


def dec(s, n):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


fp["d3_d"] = fp.groupby("date").d3.transform(dec, n=10)
fp["sz"] = fp.groupby("date").Mkt_Cap_12M_Usd.transform(dec, n=5)
fp["pb_q"] = fp.groupby("date").Pb.transform(dec, n=5)

print("H36-D1 — the 3-year battery (fwd-36m annualized %, QG-D3 convention):")
lad = fp.groupby("d3_d").f36.median()
print(f"h1 d3(Eps) deciles, MEDIAN fwd-36m ann: D1 {lad[1]:+.1f} .. D10 {lad[10]:+.1f} | D10-D1 {lad[10]-lad[1]:+.2f}pp")
big = fp[fp.sz == 5].copy()
big["d3_q"] = big.groupby("date").d3.transform(dec, n=5)
lb = big.groupby("d3_q").f36.median()
print(f"   large-cap quintiles (median): Q1 {lb[1]:+.1f} .. Q5 {lb[5]:+.1f} | Q5-Q1 {lb[5]-lb[1]:+.2f}pp")

ci = fp[(fp.pb_q <= 2) & (fp.d3_d >= 8)].f36.mean()
ca = fp[fp.pb_q <= 2].f36.mean()
ed = fp[(fp.pb_q >= 4) & (fp.d3_d <= 3)].f36.mean()
cib = big[(big.pb_q <= 2) & (big.d3_q >= 4)].f36.mean()
cab = big[big.pb_q <= 2].f36.mean()
edb = big[(big.pb_q >= 4) & (big.d3_q <= 2)].f36.mean()
print(f"h2 corners fwd-36m EW ann: cheap+improving {ci:+.2f} | cheap-alone {ca:+.2f} (inc {ci-ca:+.2f}) | "
      f"exp+deteriorating {ed:+.2f}")
print(f"   large-cap: {cib:+.2f} | {cab:+.2f} (inc {cib-cab:+.2f}) | {edb:+.2f}")

sigs = {"Pb": ("Pb", -1), "Mom": ("Mom_11M_Usd", 1), "Vol": ("Vol1Y_Usd", -1),
        "Roe": ("Roe", 1), "Gr": ("Eps_Basic_Gr", 1), "d3": ("d3", 1)}
print("h3 within-size signal spreads, fwd-36m EW ann (Q1-Q5 for Pb/Vol; Q5-Q1 others):")
h3 = {}
for nm, (col, sign) in sigs.items():
    fp["q"] = fp.groupby(["date", "sz"])[col].transform(dec, n=5)
    row = []
    for s in range(1, 6):
        d = fp[fp.sz == s]
        sp = (d[d.q == 5].f36.mean() - d[d.q == 1].f36.mean()) * sign
        row.append(round(sp, 2))
    h3[nm] = row
    print(f"   {nm:>3}: " + " ".join(f"{x:+7.2f}" for x in row))

g = fp.groupby(["sz", "pb_q"]).f36.mean().unstack()
print("h4 size x Pb fwd-36m EW ann (rows size Q1..Q5, cols cheap..expensive):")
for i in range(1, 6):
    print("   " + " ".join(f"{g.loc[i, j]:+7.2f}" for j in range(1, 6)))
sv = fp[(fp.sz <= 2) & (fp.pb_q <= 2)].f36.mean(); sg = fp[(fp.sz <= 2) & (fp.pb_q >= 4)].f36.mean()
lv = fp[(fp.sz >= 4) & (fp.pb_q <= 2)].f36.mean(); lgr = fp[(fp.sz >= 4) & (fp.pb_q >= 4)].f36.mean()
print(f"   corners: SV {sv:+.2f} | SG {sg:+.2f} | LV {lv:+.2f} | LG {lgr:+.2f} | gaps SV-SG {sv-sg:+.2f}, LV-LG {lv-lgr:+.2f}")
g60 = fp[fp.sz == 5].groupby("pb_q").f60.mean()
print(f"h5 szQ5 Pb row fwd-60m EW ann: " + " ".join(f"{g60[j]:+.2f}" for j in range(1, 6)) +
      f" | cheap-exp {g60[1]-g60[5]:+.2f}")

# --- time series: US + India SMB -> next-36m (annualized /3) ---
p = pd.read_csv(f"{V}/factors/fff_monthly_us.csv", skiprows=3)
p.columns = [c.strip() for c in p.columns]
c0 = p.columns[0]
p = p[pd.to_numeric(p[c0], errors="coerce").notna()].copy()
p["ym"] = p[c0].astype(int)
p = p[(p.ym >= 192607) & (p.ym <= 202412)]
p.index = pd.to_datetime(p.ym, format="%Y%m") + pd.offsets.MonthEnd(0)
smb = p["SMB"].astype(float); mkt = p["Mkt-RF"].astype(float) + p["RF"].astype(float)
ii = pd.read_csv(f"{V}/factors/iima_monthly_factors.csv", na_values="NA")
ii.index = pd.to_datetime(ii.Date, format="%Y-%m") + pd.offsets.MonthEnd(0)
ismb = ii.SMB.astype(float); imkt = (ii.MF + ii.RF).astype(float)


def ts36(s, mret, tag):
    tr12, tr36 = s.rolling(12).sum(), s.rolling(36).sum()
    nxt36 = s.rolling(36).sum().shift(-36) / 3  # ann %/yr
    pos, neg = nxt36[tr12 > 0], nxt36[tr12 < 0]
    print(f"{tag}-mom: next-36m ann after +12m years {pos.mean():+.2f} vs after - {neg.mean():+.2f} | spread {pos.mean()-neg.mean():+.2f}")
    lo = tr36.expanding(120).quantile(1/3).shift(1); hi = tr36.expanding(120).quantile(2/3).shift(1)
    t = pd.Series(np.where(tr36 <= lo, "LO", np.where(tr36 <= hi, "MID", "HI")), index=s.index)
    t[lo.isna()] = np.nan
    d = pd.DataFrame({"t": t, "f": nxt36}).dropna()
    rr = d.groupby("t").f.mean()
    print(f"{tag}-36m terciles -> next-36m ann: LO {rr.get('LO', np.nan):+.2f} | MID {rr.get('MID', np.nan):+.2f} | HI {rr.get('HI', np.nan):+.2f} (n={d.groupby('t').f.count().to_dict()})")
    m12 = mret.rolling(12).sum()
    dn, up = nxt36[m12 < 0], nxt36[m12 > 0]
    print(f"{tag}-post-bear: next-36m ann after DOWN market year {dn.mean():+.2f} (n={dn.count()}) vs up {up.mean():+.2f} | gap {dn.mean()-up.mean():+.2f}")


print("h6-h8 US SMB (1926-2024), next-36m annualized %/yr:")
ts36(smb, mkt, "  h US")
print("h9-h11 India SMB (IIMA 1993-2025), next-36m annualized %/yr (min-120 expanding terciles => short India window, n stated):")
ts36(ismb, imkt, "  h IN")

# --- h12/h13: SC-D1 spreads -> next-36m SL ---
fp["sz_q"] = np.ceil(fp.Mkt_Cap_12M_Usd * 5).clip(1, 5)
m = fp.groupby(["date", "sz_q"]).agg(pb=("Pb", "median"), gr=("Eps_Basic_Gr", "median"),
                                     r1=("R1M_Usd", "mean")).unstack()
V_t = m[("pb", 1.0)] - m[("pb", 5.0)]
G_t = m[("gr", 1.0)] - m[("gr", 5.0)]
sl = m[("r1", 1.0)] - m[("r1", 5.0)]
SL36 = sl.rolling(36).sum().shift(-36) / 3 * 100  # ann pp/yr
for nm, sig, cell in [("V_t(Pb)", V_t, "h12"), ("G_t", G_t, "h13")]:
    t = pd.qcut(sig, 3, labels=["T1", "T2", "T3"])
    d = pd.DataFrame({"t": t, "f": SL36}).dropna()
    rr = d.groupby("t", observed=True).f.mean()
    print(f"{cell} {nm} terciles (full-sample FLAGGED) -> next-36m S-L ann: T1 {rr['T1']:+.2f} | T2 {rr['T2']:+.2f} | T3 {rr['T3']:+.2f} (T1-T3 {rr['T1']-rr['T3']:+.2f}pp/yr; n={d.groupby('t', observed=True).f.count().to_dict()})")

json.dump({"h3_36m": h3, "h4_grid": [[round(g.loc[i, j], 2) for j in range(1, 6)] for i in range(1, 6)]},
          open("/home/user/claude-demo/research/notes/es_sc_matrices/h36.json", "w"), indent=1)
print("[written] research/notes/es_sc_matrices/h36.json")
