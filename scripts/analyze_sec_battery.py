"""SEC-D1..D4 — the sector battery (India partial, NIFTY500 survivor panel).

Registered 2026-09-07 BEFORE this run; baskets, episode windows, bars and the
survivorship/one-way declaration live in the ledger. Prints only.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
VAULT = "/home/user/claude-demo/ingest/vault"

BASKETS = {
    "IT": ["TCS", "INFY", "WIPRO", "HCLTECH", "TECHM", "MPHASIS", "MINDTREE", "BSOFT",
           "CYIENT", "LTI"],
    "PHARMA": ["SUNPHARMA", "DRREDDY", "CIPLA", "LUPIN", "AUROPHARMA", "DIVISLAB", "ALKEM",
               "BIOCON", "GLENMARK", "TORNTPHARM", "IPCALAB"],
    "FMCG": ["HINDUNILVR", "ITC", "BRITANNIA", "DABUR", "MARICO", "GODREJCP", "COLPAL",
             "EMAMILTD", "TATACONSUM", "VBL"],
    "PVTBANK": ["HDFCBANK", "ICICIBANK", "KOTAKBANK", "AXISBANK", "INDUSINDBK",
                "FEDERALBNK", "CUB", "RBLBANK", "IDFCFIRSTB", "BANDHANBNK"],
    "PSUBANK": ["SBIN", "BANKBARODA", "PNB", "CANBK", "BANKINDIA", "UNIONBANK",
                "CENTRALBK", "IOB", "MAHABANK", "INDIANB"],
    "NBFC": ["BAJFINANCE", "CHOLAFIN", "SRTRANSFIN", "LICHSGFIN", "MUTHOOTFIN",
             "MANAPPURAM", "PNBHOUSING", "CANFINHOME", "CREDITACC"],
    "AUTO": ["MARUTI", "TATAMOTORS", "BAJAJ-AUTO", "HEROMOTOCO", "EICHERMOT", "ASHOKLEY",
             "TVSMOTOR", "ESCORTS", "APOLLOTYRE", "CEATLTD"],
    "METALS": ["TATASTEEL", "JSWSTEEL", "HINDALCO", "VEDL", "SAIL", "NMDC", "JINDALSTEL",
               "NATIONALUM", "HINDZINC", "COALINDIA", "MOIL"],
    "ENERGY": ["RELIANCE", "ONGC", "OIL", "GAIL", "IOC", "BPCL", "HINDPETRO", "PETRONET",
               "CASTROLIND", "IGL", "MGL"],
    "CAPGOODS": ["LT", "SIEMENS", "ABB", "BHEL", "BEL", "CUMMINSIND", "THERMAX", "KEC",
                 "NCC", "ASHOKA", "ADANIPORTS", "CONCOR"],
    "REALTY": ["DLF", "GODREJPROP", "OBEROIRLTY", "PRESTIGE", "SOBHA", "BRIGADE",
               "PHOENIXLTD", "SUNTECK", "IBREALEST"],
    "CEMENT": ["ULTRACEMCO", "ACC", "AMBUJACEM", "SHREECEM", "RAMCOCEM", "JKCEMENT",
               "DALBHARAT", "BIRLACORPN", "INDIACEM"],
    "DURABLES": ["TITAN", "HAVELLS", "VOLTAS", "CROMPTON", "BLUESTARCO", "BATAINDIA",
                 "PAGEIND", "RELAXO", "WHIRLPOOL", "AMBER", "BAJAJELEC"],
    "UTILITIES": ["NTPC", "POWERGRID", "TATAPOWER", "CESC", "TORNTPOWER", "NHPC", "SJVN",
                  "ADANIPOWER", "JSWENERGY"],
}
EPISODES = [
    ("E1 TAPER (ccy)", "2013-05-22", "2013-09-03"),
    ("E2 DEMONET (gdp)", "2016-11-09", "2017-01-31"),
    ("E3 NBFC (credit)", "2018-09-04", "2019-02-07"),
    ("E4 COVID (crisis)", "2020-02-20", "2020-03-23"),
    ("E4b RECOVERY", "2020-03-24", "2020-12-31"),
    ("E5 INR+OIL (ccy)", "2018-04-02", "2018-10-09"),
    ("E6 EASING (rates)", "2019-02-07", "2019-12-31"),
]

px = pd.read_csv(f"{VAULT}/panel/n500_adjclose_2012_2022.csv.gz",
                 parse_dates=["Date"]).set_index("Date").sort_index()
ret = px.pct_change(fill_method=None)
mkt = ret.mean(axis=1)
rel = {}
for name, members in BASKETS.items():
    have = [t for t in members if t in ret.columns]
    rel[name] = (ret[have].mean(axis=1) - mkt).dropna()
print(f"panel {ret.shape[1]} tickers {ret.index[0].date()}..{ret.index[-1].date()}; "
      f"baskets: " + ", ".join(f"{k}({len([t for t in v if t in ret.columns])})"
                               for k, v in BASKETS.items()))

def cum_rel(name, a, b):
    w = rel[name].loc[a:b]
    return float((1 + w).prod() - 1) if len(w) else np.nan

print("\nSEC-D1 — EPISODE TABLES (cum REL vs panel, pp; unaffected = |rel| < 3pp):")
hdr = f"  {'episode':>18} " + " ".join(f"{k:>8}" for k in BASKETS)
print(hdr)
ep_rel = {}
for lab, a, b in EPISODES:
    row = {k: cum_rel(k, a, b) for k in BASKETS}
    ep_rel[lab] = row
    print(f"  {lab:>18} " + " ".join(f"{100*row[k]:>+8.1f}" for k in BASKETS))
for lab, a, b in EPISODES:
    row = ep_rel[lab]
    s = sorted(row.items(), key=lambda kv: kv[1])
    flat = [k for k, v in row.items() if abs(v) < 0.03]
    print(f"  {lab}: worst {s[0][0]} {100*s[0][1]:+.1f} / {s[1][0]} {100*s[1][1]:+.1f}; "
          f"best {s[-1][0]} {100*s[-1][1]:+.1f} / {s[-2][0]} {100*s[-2][1]:+.1f}; "
          f"unaffected: {','.join(flat) if flat else '-'}")

# ---- annual states ----
inr = pd.read_csv(f"{VAULT}/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"])
inr_y = inr.set_index("Date").INR_per_USD.resample("YE").last()
inr_y.index = inr_y.index.year
dep = np.log(inr_y).diff()
iima = pd.read_csv(f"{VAULT}/factors/iima_monthly_factors.csv")
iima["year"] = iima.Date.str[:4].astype(int)
rf_y = iima.groupby("year").apply(lambda g: np.expm1(np.log1p(g.RF / 100).sum()))
drf = rf_y.diff()

yr_rel = pd.DataFrame({k: (1 + rel[k]).groupby(rel[k].index.year).prod() - 1
                       for k in BASKETS})
yrs = [y for y in yr_rel.index if y in dep.index and not np.isnan(dep.get(y, np.nan))]
weak = [y for y in yrs if dep[y] >= 0.05]
othr = [y for y in yrs if dep[y] < 0.05]
print(f"\nSEC-D2 — CURRENCY-SECTOR MAP: weak-INR years (dep>=5%): {weak}")
print(f"  {'sector':>9} {'weak-yr REL':>12} {'other-yr REL':>13} {'diff':>7}")
diffs = {}
for k in BASKETS:
    w, o = yr_rel.loc[weak, k].mean(), yr_rel.loc[othr, k].mean()
    diffs[k] = w - o
    print(f"  {k:>9} {100*w:>+11.1f}% {100*o:>+12.1f}% {100*(w-o):>+6.1f}")
exp_w = np.mean([yr_rel.loc[weak, k].mean() for k in ("IT", "PHARMA")])
exp_o = np.mean([yr_rel.loc[othr, k].mean() for k in ("IT", "PHARMA")])
print(f"  (ii) EXPORTER HEDGE: IT+PHARMA REL weak {100*exp_w:+.1f}% vs other {100*exp_o:+.1f}% "
      f"-> diff {100*(exp_w-exp_o):+.1f}pp/yr (bar >= +5)")
rev = []
for y in weak:
    if y + 1 in yr_rel.index:
        rev.append(stats.spearmanr(yr_rel.loc[y], yr_rel.loc[y + 1])[0])
print(f"  (iii) next-year reversal rank-corr per weak year: "
      f"{[f'{y}:{r:+.2f}' for y, r in zip(weak, rev)]} -> mean {np.mean(rev):+.2f}")

ry = [y for y in yr_rel.index if y in drf.index and not np.isnan(drf.get(y, np.nan))]
up = [y for y in ry if drf[y] > 0]
dn = [y for y in ry if drf[y] <= 0]
print(f"\nSEC-D3 — RATE-SECTOR MAP: rising-RF years {up} / falling {dn}")
print(f"  {'sector':>9} {'rising REL':>11} {'falling REL':>12} {'diff':>7}")
for k in BASKETS:
    u, d = yr_rel.loc[up, k].mean(), yr_rel.loc[dn, k].mean()
    print(f"  {k:>9} {100*u:>+10.1f}% {100*d:>+11.1f}% {100*(u-d):>+6.1f}")
trio_u = np.mean([yr_rel.loc[up, k].mean() for k in ("NBFC", "REALTY", "PSUBANK")])
trio_d = np.mean([yr_rel.loc[dn, k].mean() for k in ("NBFC", "REALTY", "PSUBANK")])
print(f"  (ii) LEVERAGED TRIO rising-minus-falling: {100*(trio_u-trio_d):+.1f}pp/yr (bar <= -3); "
      f"IT diff {100*(yr_rel.loc[up,'IT'].mean()-yr_rel.loc[dn,'IT'].mean()):+.1f} / "
      f"FMCG diff {100*(yr_rel.loc[up,'FMCG'].mean()-yr_rel.loc[dn,'FMCG'].mean()):+.1f} (|bar| < 3)")

e3 = ep_rel["E3 NBFC (credit)"]
print(f"\nSEC-D4 — E3 SPECIFICITY: (i) ordering NBFC {100*e3['NBFC']:+.1f} < PSUBANK "
      f"{100*e3['PSUBANK']:+.1f} < PVTBANK {100*e3['PVTBANK']:+.1f} "
      f"-> {'PASS' if e3['NBFC'] < e3['PSUBANK'] < e3['PVTBANK'] else 'FAIL'}")
print(f"  (ii) REALTY E3 cum REL {100*e3['REALTY']:+.1f}pp (bar <= -8)")
