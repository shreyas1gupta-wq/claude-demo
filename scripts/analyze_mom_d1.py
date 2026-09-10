"""MOM-D1 — the stock-level lookback anatomy across regimes (US + India).
Registered 2026-09-10 BEFORE this run (ledger entry of record). Builds lookback
windows from RAW formation returns (not the panel's pre-baked Mom_* columns).
One-way rule frozen: EW no-delisting bias depresses momentum spreads on both
panels, so a POSITIVE spread is admissible evidence, a negative one is not.
Prints only; interpretation hand-appended to the ledger after."""
import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"


def dec(s, n=10):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


# ================= US: firm_panel, built from R1M_Usd pivot =================
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz",
                 usecols=["stock_id", "date", "R1M_Usd", "Mkt_Cap_12M_Usd"],
                 parse_dates=["date"])
r = fp.pivot_table(index="date", columns="stock_id", values="R1M_Usd")
lg = np.log1p(r)
sz = fp.pivot_table(index="date", columns="stock_id", values="Mkt_Cap_12M_Usd")


def window_sum(lgret, lo, hi):
    """rows t-hi .. t-lo (inclusive), as of row t (using rows already known at t,
    i.e. r at row t is the FORWARD return realized in month t+1 per vault AUTH,
    so 'formation ending last month' = sum of lg rows (t-hi+1)..(t-lo) shifted so
    the most recent included row is t-lo, with row t itself excluded)."""
    # lgret.shift(lo) drops the most recent `lo-1` rows before the sum window ends
    total = lgret.rolling(hi - lo + 1).sum().shift(lo)
    return total


WINDOWS = {"3-1": (1, 3), "6-1": (1, 6), "6-2": (2, 6), "12-2": (2, 12), "12-7": (7, 12)}
forms = {k: window_sum(lg, lo, hi) for k, (lo, hi) in WINDOWS.items()}

szq = sz.apply(lambda col: pd.Series(dec(col, 5), index=col.index) if col.notna().sum() else col, axis=1)
# szq built per-date instead (row-wise dec across columns at each date):
szq = sz.rank(axis=1, pct=True).apply(lambda row: np.ceil(row * 5), axis=1)

print("=" * 100)
print("MOM-D1 (US) — the lookback ladder, D10-D1 fwd-1m EW ann. %/yr (panel | large half):")
print("=" * 100)
L1 = {}
for k, f in forms.items():
    fst = f.stack()
    rst = r.stack()
    df = pd.DataFrame({"f": fst, "r": rst}).dropna()
    df["d"] = df.groupby(level=0).f.transform(dec)
    panel_spread = (df[df.d == 10].r.mean() - df[df.d == 1].r.mean()) * 1200
    szst = szq.stack().rename("sz")
    dfb = df.join(szst)
    big = dfb[dfb.sz == 5].copy()
    big["d2"] = big.groupby(level=0).f.transform(dec)
    large_spread = (big[big.d2 == 10].r.mean() - big[big.d2 == 1].r.mean()) * 1200
    L1[k] = (round(panel_spread, 2), round(large_spread, 2))
    print(f"  {k:>5}: panel {panel_spread:+7.2f} | large {large_spread:+7.2f}")

# ---- US market/vol regimes ----
p = pd.read_csv(f"{V}/factors/fff_monthly_us.csv", skiprows=3)
p.columns = [c.strip() for c in p.columns]
c0 = p.columns[0]
p = p[pd.to_numeric(p[c0], errors="coerce").notna()].copy()
p["ym"] = p[c0].astype(int)
p = p[(p.ym >= 192607) & (p.ym <= 202412)]
p.index = pd.to_datetime(p.ym, format="%Y%m") + pd.offsets.MonthEnd(0)
mkt = (p["Mkt-RF"].astype(float) + p["RF"].astype(float))
tr12 = (1 + mkt).rolling(12).apply(np.prod, raw=True) - 1
mkt_state = np.sign(tr12).shift(1)

vix = pd.read_csv(f"{V}/globalvol/cboe_vix_daily_1990_2026.csv")
vcol = [c for c in vix.columns if "close" in c.lower() or "vix" in c.lower()]
vix.columns = [c.strip() for c in vix.columns]
dcol = [c for c in vix.columns if "date" in c.lower()][0]
vcol = [c for c in vix.columns if c != dcol][0]
vix[dcol] = pd.to_datetime(vix[dcol])
vix = vix.set_index(dcol)[vcol].astype(float)
vix_m = vix.resample("ME").mean()
vix_lo = vix_m.expanding(120).quantile(1 / 3).shift(1)
vix_hi = vix_m.expanding(120).quantile(2 / 3).shift(1)
vix_t = pd.Series(np.where(vix_m <= vix_lo, "LO", np.where(vix_m <= vix_hi, "MID", "HI")), index=vix_m.index)
vix_t[vix_lo.isna()] = np.nan


def spread_by_state(f, state_series, label_map=None):
    fst = f.stack()
    rst = r.stack()
    df = pd.DataFrame({"f": fst, "r": rst}).dropna()
    st = state_series.reindex(df.index.get_level_values(0))
    df["state"] = st.values
    out = {}
    for s in df.state.dropna().unique():
        d = df[df.state == s].copy()
        d["d"] = d.groupby(level=0).f.transform(dec)
        sp = (d[d.d == 10].r.mean() - d[d.d == 1].r.mean()) * 1200
        out[s] = round(sp, 2)
    return out


print("\nL2a — US 6-2 and 12-7 D10-D1 by market state (up=+1/down=-1), and the (12-7 - 6-2) diff per state:")
for k in ["6-2", "12-7"]:
    sb = spread_by_state(forms[k], mkt_state)
    print(f"  {k}: " + " | ".join(f"{s:+.0f}: {v:+.2f}" for s, v in sorted(sb.items())))
sb62 = spread_by_state(forms["6-2"], mkt_state)
sb127 = spread_by_state(forms["12-7"], mkt_state)
for s in sorted(set(sb62) & set(sb127)):
    print(f"  diff at state {s:+.0f}: {sb127[s]-sb62[s]:+.2f}")

print("\nL2b — US 6-2 and 12-7 D10-D1 by VIX tercile:")
for k in ["6-2", "12-7"]:
    sb = spread_by_state(forms[k], vix_t)
    print(f"  {k}: " + " | ".join(f"{s}: {v:+.2f}" for s, v in sorted(sb.items(), key=lambda x: {"LO": 0, "MID": 1, "HI": 2}.get(x[0], 9))))

print("\nL3a — era halves (1999-2009 / 2010-2019), 6-2 and 12-7 D10-D1:")
for era, (d0, d1) in [("1999-2009", ("1999", "2009")), ("2010-2019", ("2010", "2019"))]:
    for k in ["6-2", "12-7"]:
        f = forms[k].loc[d0:d1]
        rr = r.loc[d0:d1]
        fst = f.stack(); rst = rr.stack()
        df = pd.DataFrame({"f": fst, "r": rst}).dropna()
        df["d"] = df.groupby(level=0).f.transform(dec)
        sp = (df[df.d == 10].r.mean() - df[df.d == 1].r.mean()) * 1200
        print(f"  {era} {k}: {sp:+.2f}")

print("\nL3b — small-vs-large lookback ordering (panel-large gap per window):")
for k, (ps, ls) in L1.items():
    print(f"  {k}: panel {ps:+.2f} - large {ls:+.2f} = {ps-ls:+.2f}")

# ================= India: survivor panel, built from adjclose =================
px = pd.read_csv(f"{V}/panel/n500_adjclose_2012_2022.csv.gz", parse_dates=["Date"]).set_index("Date")
vt = pd.read_csv(f"{V}/panel/n500_value_traded_2012_2022.csv.gz", parse_dates=["Date"]).set_index("Date")
mret = px.resample("ME").last().pct_change()
mlg = np.log1p(mret)
adv = vt.rolling(252, min_periods=126).median().resample("ME").last()

iforms = {k: window_sum(mlg, lo, hi) for k, (lo, hi) in WINDOWS.items()}

print("\n" + "=" * 100)
print("MOM-D1 (India) — the lookback ladder, D10-D1 fwd-1m EW ann. %/yr (full | top-ADV tercile):")
print("=" * 100)
L4 = {}
adv_t = adv.rank(axis=1, pct=True)
adv_long = adv_t.stack().rename("adv").reset_index()
adv_long.columns = ["date", "ticker", "adv"]
adv_long["ticker"] = adv_long["ticker"].astype(str)
for k, f in iforms.items():
    fst = f.stack().rename("f").reset_index()
    fst.columns = ["date", "ticker", "f"]
    fst["ticker"] = fst["ticker"].astype(str)
    rst = mret.stack().rename("r").reset_index()
    rst.columns = ["date", "ticker", "r"]
    rst["ticker"] = rst["ticker"].astype(str)
    df = fst.merge(rst, on=["date", "ticker"]).dropna()
    df["d"] = df.groupby("date").f.transform(lambda s: dec(s, n=5))
    full_spread = (df[df.d == 5].r.mean() - df[df.d == 1].r.mean()) * 1200
    dfa = df.merge(adv_long, on=["date", "ticker"], how="left")
    top = dfa[dfa.adv > 2 / 3].copy()
    top["d2"] = top.groupby("date").f.transform(lambda s: dec(s, n=5))
    top_spread = (top[top.d2 == 5].r.mean() - top[top.d2 == 1].r.mean()) * 1200
    L4[k] = (round(full_spread, 2), round(top_spread, 2))
    print(f"  {k:>5}: full {full_spread:+7.2f} | top-ADV {top_spread:+7.2f}")

nifty = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
ncol = [c for c in nifty.columns if "Adj" in c][0]
nm = nifty[ncol].resample("ME").last().pct_change()
ntr12 = (1 + nm).rolling(12).apply(np.prod, raw=True) - 1
n_state = np.sign(ntr12).shift(1)


def spread_by_state_india(f, state_series, ntile=5):
    fst = f.stack(); rst = mret.stack()
    df = pd.DataFrame({"f": fst, "r": rst}).dropna()
    st = state_series.reindex(df.index.get_level_values(0))
    df["state"] = st.values
    out = {}
    for s in df.state.dropna().unique():
        d = df[df.state == s].copy()
        d["d"] = d.groupby(level=0).f.transform(lambda x: dec(x, n=ntile))
        sp = (d[d.d == ntile].r.mean() - d[d.d == 1].r.mean()) * 1200
        out[s] = round(sp, 2)
    return out


print("\nL5a — India 6-2 and 12-7 D10-D1 by NIFTY market state:")
for k in ["6-2", "12-7"]:
    sb = spread_by_state_india(iforms[k], n_state)
    print(f"  {k}: " + " | ".join(f"{s:+.0f}: {v:+.2f}" for s, v in sorted(sb.items())))

ivix = pd.read_csv(f"{V}/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"]).set_index("date")
ivix_m = ivix["close"].resample("ME").mean()
ivix_med = ivix_m.median()
ivix_t = pd.Series(np.where(ivix_m <= ivix_m.quantile(1 / 3), "LO",
                            np.where(ivix_m <= ivix_m.quantile(2 / 3), "MID", "HI")), index=ivix_m.index)
print("\nL5b — India 6-2 and 12-7 D10-D1 by India-VIX tercile (2010-2021, FULL-SAMPLE cut, FLAGGED):")
for k in ["6-2", "12-7"]:
    sb = spread_by_state_india(iforms[k], ivix_t)
    print(f"  {k}: " + " | ".join(f"{s}: {v:+.2f}" for s, v in sorted(sb.items(), key=lambda x: {"LO": 0, "MID": 1, "HI": 2}.get(x[0], 9))))

print("\nL6 — verdict: best lookback (full-sample, positive spreads only admissible) per market:")
print("  US panel:", max(L1.items(), key=lambda kv: kv[1][0]))
print("  US large:", max(L1.items(), key=lambda kv: kv[1][1]))
print("  India full:", max(L4.items(), key=lambda kv: kv[1][0]))
print("  India top-ADV:", max(L4.items(), key=lambda kv: kv[1][1]))
