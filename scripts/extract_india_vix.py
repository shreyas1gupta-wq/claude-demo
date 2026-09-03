"""Extract the India VIX daily vault file from the raw TradingView export + run pass-2 anchors.

Extraction spec is FIXED in ingest/vault/vix/AUTHENTICATION.md (pass 1, committed before
this script ran): keep time/open/high/low/close, epoch sec -> IST calendar date, drop
indicator columns. Anchors A1-A6 are checked here exactly as barred; results are appended
to AUTHENTICATION.md by hand (pass 2), never by editing pass 1.
"""
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIX_DIR = ROOT / "ingest" / "vault" / "vix"
RAW = VIX_DIR / "india_vix_daily_2010_2023_raw.csv"
OUT = VIX_DIR / "india_vix_daily_2010_2023.csv"
CBOE = ROOT / "ingest" / "vault" / "globalvol" / "cboe_vix_daily_1990_2026.csv"

raw = pd.read_csv(RAW, usecols=["time", "open", "high", "low", "close"])
# epoch seconds at bar open -> IST calendar date
ts = pd.to_datetime(raw["time"], unit="s", utc=True).dt.tz_convert("Asia/Kolkata")
df = pd.DataFrame({"date": ts.dt.date.astype(str),
                   "open": raw["open"], "high": raw["high"],
                   "low": raw["low"], "close": raw["close"]})
df.to_csv(OUT, index=False)
d = pd.to_datetime(df["date"])
print(f"Extracted {len(df)} rows, {df['date'].iloc[0]} .. {df['date'].iloc[-1]}")

# ---- pass-2 anchors, exactly as barred ----
def flag(ok):
    return "PASS" if ok else "MISS"

s = pd.Series(df["close"].values, index=d)

# A1: 2020-03-24 close in [82,85] AND sample max
a1_val = s.get(pd.Timestamp("2020-03-24"))
a1 = a1_val is not None and 82 <= a1_val <= 85 and a1_val == s.max()
print(f"A1 {flag(a1)}: 2020-03-24 close = {a1_val}, sample max = {s.max():.4f} on {s.idxmax():%Y-%m-%d}")

# A2: 2015-08-24 close in [26,30]
a2_val = s.get(pd.Timestamp("2015-08-24"))
a2 = a2_val is not None and 26 <= a2_val <= 30
print(f"A2 {flag(a2)}: 2015-08-24 close = {a2_val}")

# A3: yearly rows 2011-2022 in [240,252]
counts = d.dt.year.value_counts()
bad = {y: int(counts.get(y, 0)) for y in range(2011, 2023) if not 240 <= counts.get(y, 0) <= 252}
print(f"A3 {flag(not bad)}: yearly rows 2011-2022 = "
      f"{ {y: int(counts[y]) for y in range(2011, 2023)} }"
      + (f" OUT OF BAND: {bad}" if bad else ""))

# A4: closes in (7,100), strictly increasing dates, no dupes
a4 = bool(((s > 7) & (s < 100)).all() and d.is_monotonic_increasing and not d.duplicated().any())
print(f"A4 {flag(a4)}: close range [{s.min():.2f}, {s.max():.2f}], monotone={d.is_monotonic_increasing}, dupes={int(d.duplicated().sum())}")

# A5: max close 2018-02-01..2018-02-15 in [17,23]
feb18 = s.loc["2018-02-01":"2018-02-15"]
a5 = len(feb18) > 0 and 17 <= feb18.max() <= 23
print(f"A5 {flag(a5)}: Feb-2018 window max close = {feb18.max():.2f} on {feb18.idxmax():%Y-%m-%d} (n={len(feb18)})")

# A6: monthly last-close Pearson corr with CBOE VIX vault >= 0.55 over overlap
cboe = pd.read_csv(CBOE)
dcol = [c for c in cboe.columns if c.lower() in ("date", "dates")][0]
ccol = [c for c in cboe.columns if "close" in c.lower() or c.upper() == "VIX"][0]
cb = pd.Series(cboe[ccol].values, index=pd.to_datetime(cboe[dcol])).dropna()
m_in = s.resample("ME").last()
m_cb = cb.resample("ME").last()
both = pd.concat([m_in, m_cb], axis=1, keys=["ivix", "cboe"]).dropna()
r = both["ivix"].corr(both["cboe"])
a6 = r >= 0.55
print(f"A6 {flag(a6)}: monthly level corr with CBOE VIX = {r:.3f} over {len(both)} months "
      f"({both.index.min():%Y-%m} .. {both.index.max():%Y-%m})")

# Special-session report (not barred)
for day in ("2015-02-28", "2020-02-01"):
    print(f"REPORT: Saturday budget session {day} present = {pd.Timestamp(day) in s.index}")
