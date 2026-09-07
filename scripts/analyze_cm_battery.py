"""CM-D1..D6 — the commodity battery (century table, inflation hedge, dollar/growth,
ratios, spot momentum, oil->INR). Registered 2026-09-07 BEFORE this run. Prints only."""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo/ingest/vault"
j = pd.read_csv(f"{ROOT}/commodities/jacks_real_commodity_prices_1850_2015.csv")
j = j.set_index("Year").drop(columns=["Entity"])
BIG4 = ["Petroleum", "Gold", "Silver", "Copper"]
GROUPS = {
    "energy": ["Coal", "Natural gas", "Petroleum"],
    "metals": ["Aluminum", "Chromium", "Copper", "Lead", "Manganese", "Nickel", "Steel",
               "Tin", "Zinc", "Gold", "Platinum", "Silver"],
    "agri": ["Barley", "Corn", "Rice", "Rye", "Wheat", "Cocoa", "Coffee", "Cotton",
             "Palm oil", "Peanuts", "Rubber", "Sugar", "Tea", "Tobacco", "Beef", "Pork",
             "Lamb", "Wool"],
}

print("CM-D1 — REAL price CAGR 1900-2015 (Jacks, US-CPI-deflated):")
for c in BIG4:
    s = j[c].loc[1900:2015].dropna()
    g = 100 * (np.exp(np.log(s.iloc[-1] / s.iloc[0]) / (s.index[-1] - s.index[0])) - 1)
    print(f"  {c:10}: {g:+.2f}%/yr (n={len(s)}y)")
for gname, cols in GROUPS.items():
    gs = []
    for c in cols:
        s = j[c].loc[1900:2015].dropna()
        if len(s) >= 80:
            gs.append(100 * (np.exp(np.log(s.iloc[-1] / s.iloc[0]) / (s.index[-1] - s.index[0])) - 1))
    print(f"  {gname:10}: median {np.median(gs):+.2f}%/yr across {len(gs)} series")

# US inflation regime from JST
us = pd.ExcelFile(f"{ROOT}/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
us = us[us.country == "USA"].set_index("year")
infl = us.cpi.pct_change()
in_pct = pd.Series(expanding_percentile(infl.to_numpy(), min_obs=20), index=us.index)
dinfl = infl.diff()
dlog = np.log(j).diff()

print("\nCM-D2 — SAME-YEAR REAL change by US inflation 2x2 (mean %/yr):")
print(f"  {'cell':>14} {'Petroleum':>10} {'Gold':>7} {'Silver':>7} {'Copper':>7} {'n':>4}")
for hi in (True, False):
    for ris in (True, False):
        yrs = [y for y in j.index if y in in_pct.index
               and not np.isnan(in_pct.get(y, np.nan)) and not np.isnan(dinfl.get(y, np.nan))
               and (in_pct[y] >= 0.8) == hi and (dinfl[y] > 0) == ris]
        lab = f"{'HIGH' if hi else 'low'}+{'rising' if ris else 'falling'}"
        vals = [100 * dlog[c].reindex(yrs).mean() for c in BIG4]
        print(f"  {lab:>14} " + " ".join(f"{v:>+7.1f}" for v in vals) + f"   {len(yrs):>4}")

# broad dollar (CU-D7 construction)
pan = pd.ExcelFile(f"{ROOT}/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
pan = pan[pan.country != "USA"]
usd = pan.pivot_table(index="year", columns="country", values="xrusd")
usd_chg = np.log(usd).diff().mean(axis=1)  # + = USD strengthening
strong = [y for y in j.index if usd_chg.get(y, np.nan) >= 0.05]
weak = [y for y in j.index if usd_chg.get(y, np.nan) <= -0.05]
all42 = [c for c in j.columns]
med_s = np.nanmedian([dlog[c].reindex(strong).mean() for c in all42])
med_w = np.nanmedian([dlog[c].reindex(weak).mean() for c in all42])
b4_s = np.nanmean([dlog[c].reindex(strong).mean() for c in BIG4])
b4_w = np.nanmean([dlog[c].reindex(weak).mean() for c in BIG4])
print(f"\nCM-D3(d1) dollar law: strong-USD years (n={len(strong)}): big4 mean {100*b4_s:+.1f}%, "
      f"all-42 median {100*med_s:+.1f}% || weak-USD (n={len(weak)}): big4 {100*b4_w:+.1f}%, "
      f"median {100*med_w:+.1f}%")
cg = np.log(j.Copper / j.Gold).diff()
g_us = np.log(us.rgdpmad).diff()
x = pd.concat([cg, g_us.shift(-1), g_us], axis=1, keys=["cg", "g_next", "g_same"]).dropna()
print(f"CM-D3(d2) Dr.Copper predictive: d(copper/gold)_t -> US growth_t+1 rho "
      f"{stats.spearmanr(x.cg, x.g_next)[0]:+.2f} (n={len(x)})")
print(f"CM-D3(d3) coincident: same-year rho {stats.spearmanr(x.cg, x.g_same)[0]:+.2f}")

print("\nCM-D4 — RATIOS:")
for num, den, tag, h in [("Gold", "Silver", "gold/silver", 5), ("Petroleum", "Gold", "oil/gold", 5)]:
    ratio = np.log(j[num] / j[den])
    pct = pd.Series(expanding_percentile(ratio.to_numpy(), min_obs=20), index=j.index)
    fwd_rel = (np.log(j[den]).diff(h).shift(-h) - np.log(j[num]).diff(h).shift(-h)) / h
    z = pd.concat([pct, fwd_rel], axis=1, keys=["p", "f"]).dropna()
    print(f"  {tag}: pct -> next-{h}y ({den} minus {num}) rho {stats.spearmanr(z.p, z.f)[0]:+.2f} "
          f"(n={len(z)}, overlap flagged); 2015 endpoint pct {pct.dropna().iloc[-1]:.2f}")

print("\nCM-D5 — SPOT MOMENTUM (IMF PCPS monthly 1980-2017, 12-1, EW terciles):")
m = pd.read_csv(f"{ROOT}/commodities/imf_pcps_monthly_1980_2017.csv", parse_dates=["Date"])
m = m.set_index("Date").sort_index()
drop = [c for c in m.columns if "Index" in c or "index" in c]
m = m.drop(columns=drop)
r = np.log(m).diff()
mom = np.log(m.shift(1) / m.shift(12))
ls = []
for t in range(13, len(m)):
    mm = mom.iloc[t].dropna()
    if len(mm) < 15:
        continue
    q = mm.rank(pct=True)
    top, bot = q[q >= 2 / 3].index, q[q <= 1 / 3].index
    ls.append((m.index[t], r.iloc[t][top].mean() - r.iloc[t][bot].mean()))
ls = pd.Series(dict(ls)).dropna()
ann = 100 * ls.mean() * 12
roll12 = 100 * ls.rolling(12).sum()
print(f"  d1 L/S annualized {ann:+.1f}%/yr over {len(ls)} months ({m.shape[1]} series); "
      f"vol {100*ls.std()*np.sqrt(12):.1f}% -> Sharpe-shape {ls.mean()/ls.std()*np.sqrt(12):.2f} (descriptive)")
print(f"  d2 worst rolling 12m: {roll12.min():+.1f}% ({roll12.idxmin().date()})")

wti = pd.read_csv(f"{ROOT}/commodities/wti_monthly_eia.csv", parse_dates=["Date"])
wti_y = wti.set_index("Date").Price.resample("YE").last()
wti_y.index = wti_y.index.year
inr = pd.read_csv(f"{ROOT}/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"])
inr_y = inr.set_index("Date").INR_per_USD.resample("YE").last()
inr_y.index = inr_y.index.year
z = pd.concat([np.log(wti_y).diff(), np.log(inr_y).diff()], axis=1, keys=["oil", "dep"]).dropna()
z = z[(z.index >= 1987) & (z.index <= 2025)]
print(f"\nCM-D6 — oil->INR: corr(WTI change, same-yr INR depreciation) 1987-2025 = "
      f"{stats.spearmanr(z.oil, z.dep)[0]:+.2f} (n={len(z)})")
