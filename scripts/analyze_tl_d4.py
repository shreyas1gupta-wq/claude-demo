"""TL-D4 — the sigma ledger at three speeds (weekly/monthly, NIFTY + smallcaps + US).

Registered 2026-09-07 BEFORE this run. Prints + appends key d4 to tl_atlas_stats.json.
"""
import json
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
ROOT = "/home/user/claude-demo"
V = f"{ROOT}/ingest/vault"


def agg(r, freq):
    return np.log1p(r).resample(freq).sum().pipe(np.expm1).replace(0, np.nan).dropna()


def ledger(r, name, freq):
    z = (r - r.mean()) / r.std()
    n = len(r)
    row = dict(name=name, freq=freq, n=n, sd=float(r.std()),
               ek=float(stats.kurtosis(r)), t=[])
    print(f"  {name:16} {freq:>7} n={n:>5} 1σ={100*r.std():5.2f}% "
          f"2σ={200*r.std():5.1f}% 3σ={300*r.std():5.1f}% 6σ={600*r.std():5.1f}%  | ", end="")
    for k in (1, 2, 3, 4, 6):
        obs = int((z.abs() >= k).sum())
        gauss = 2 * stats.norm.sf(k) * n
        row["t"].append([k, obs, round(gauss, 3)])
        print(f"{k}σ:{obs}/{gauss:.2f} ", end="")
    w = r.min()
    row["worst"] = [str(r.idxmin().date()), round(100*w, 1), round(float((w-r.mean())/r.std()), 1)]
    print(f"| worst {100*w:.1f}% ({row['worst'][2]}σ, {row['worst'][0]})")
    return row


# daily sources
nf = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
rn = nf["Adj Close"].pct_change().dropna()

px = pd.read_csv(f"{V}/panel/n500_adjclose_2012_2022.csv.gz", parse_dates=["Date"]).set_index("Date").sort_index()
vt = pd.read_csv(f"{V}/panel/n500_value_traded_2012_2022.csv.gz", parse_dates=["Date"]).set_index("Date").sort_index()
ret = px.pct_change(fill_method=None)
parts = []
for y in range(2013, 2022):
    med = vt.loc[f"{y-1}-01-01":f"{y-1}-12-31"].median()
    med = med[med > 0].dropna()
    parts.append(ret.loc[f"{y}-01-01":f"{y}-12-31", med[med.rank(pct=True) <= 1/3].index].mean(axis=1))
rsm = pd.concat(parts).sort_index().dropna()

adj = pd.read_csv(f"{V}/us_index/sp500_fut_adjusted_daily.csv", parse_dates=["DATETIME"])
mul = pd.read_csv(f"{V}/us_index/sp500_fut_multiple_daily.csv", parse_dates=["DATETIME"])
def daily(df, col):
    s = df.set_index("DATETIME")[col]
    def pick(g):
        h20 = g[g.index.hour == 20]
        return h20.iloc[-1] if len(h20) else g.iloc[-1]
    out = s.groupby(s.index.date).apply(pick)
    out.index = pd.to_datetime(out.index)
    return out
a, u = daily(adj, "price"), daily(mul, "PRICE")
rsp = (a.diff() / u.shift(1)).dropna()
rsp = rsp[rsp != 0]

dj = pd.read_csv(f"{V}/us_index/djia_daily_1980_2012.csv", parse_dates=["rownames"]).set_index("rownames")["dat"]
rdj = dj.pct_change().dropna()
rdj = rdj[rdj != 0]

rows = []
print("TL-D4 — WEEKLY ledgers (W-FRI log-sum):")
rows.append(ledger(agg(rn, "W-FRI"), "NIFTY 50", "weekly"))
rows.append(ledger(agg(rsm, "W-FRI"), "India small*", "weekly"))
rows.append(ledger(agg(rsp, "W-FRI"), "S&P futures", "weekly"))
rows.append(ledger(agg(rdj, "W-FRI"), "Dow Jones", "weekly"))
print("MONTHLY ledgers (new: NIFTY; the rest cited from TL-D2 and recomputed for the display table):")
rows.append(ledger(agg(rn, "ME"), "NIFTY 50", "monthly"))
rows.append(ledger(agg(rsm, "ME"), "India small*", "monthly"))
rows.append(ledger(agg(rsp, "ME"), "S&P futures", "monthly"))
rows.append(ledger(agg(rdj, "ME"), "Dow Jones", "monthly"))
# cited monthly series recomputed only to render the unified table (booked in TL-D2)
ff = pd.read_csv(f"{V}/factors/fff_monthly_us.csv", skiprows=3)
ff.columns = ["ym"] + [c.strip() for c in ff.columns[1:]]
ff = ff[ff.ym.astype(str).str.match(r"^\s*\d{6}\s*$", na=False)].astype(float)
ff.index = pd.to_datetime(ff.ym.astype(int).astype(str), format="%Y%m")
mkt = (ff["Mkt-RF"] + ff.RF) / 100
sml = mkt + ff.SMB / 100
im = pd.read_csv(f"{V}/factors/iima_monthly_factors.csv")
im.index = pd.to_datetime(im.Date, format="%Y-%m")
imkt = ((im.MF + im.RF) / 100).dropna()
isml = (imkt + im.SMB / 100).dropna()
sh = pd.read_csv(f"{V}/us_index/sp500_shiller_monthly_1871.csv", parse_dates=["Date"]).set_index("Date")
spxm = sh.SP500.pct_change().dropna()
print("cited (TL-D2) monthly, with the x1 |z|>=1 completion row:")
rows.append(ledger(mkt, "US market 1926-", "monthly"))
rows.append(ledger(sml, "US small 1926-*", "monthly"))
rows.append(ledger(imkt, "India mkt 1993-", "monthly"))
rows.append(ledger(isml, "India small'93-*", "monthly"))
rows.append(ledger(spxm, "S&P 1871- (avg)", "monthly"))

# daily reference ratios for the decay claim
def ratio(r, k):
    z = (r - r.mean()) / r.std()
    return float((z.abs() >= k).sum() / (2 * stats.norm.sf(k) * len(r)))
print("\naggregation-decay check (3σ / 4σ failure ratios):")
for nm, d, w, m in [("NIFTY", rn, agg(rn, "W-FRI"), agg(rn, "ME")),
                    ("SPX", rsp, agg(rsp, "W-FRI"), agg(rsp, "ME"))]:
    print(f"  {nm}: 3σ {ratio(d,3):.1f}x -> {ratio(w,3):.1f}x -> {ratio(m,3):.1f}x | "
          f"4σ {ratio(d,4):.0f}x -> {ratio(w,4):.0f}x -> {ratio(m,4):.0f}x")

with open(f"{ROOT}/research/notes/tl_atlas_stats.json") as f:
    D = json.load(f)
D["d4"] = rows
with open(f"{ROOT}/research/notes/tl_atlas_stats.json", "w") as f:
    json.dump(D, f)
print("d4 appended")
