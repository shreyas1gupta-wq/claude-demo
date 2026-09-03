"""EN-D1a — onset-conditioned sectoral contrast (runnable partial of EN-D1).

Registered 2026-09-03 in research/register/trial-ledger.md BEFORE this run; definitions,
baskets, bars and the one-way declaration live there. This script prints; it decides nothing.
"""
import numpy as np
import pandas as pd

VAULT = "/home/user/claude-demo/ingest/vault"
TREATED = ["HINDUNILVR", "DABUR", "EMAMILTD", "GODREJCP", "BRITANNIA", "MARICO", "ITC",
           "HEROMOTOCO", "BAJAJ-AUTO", "ESCORTS", "UPL", "PIIND", "COROMANDEL",
           "CHAMBLFERT", "GNFC", "RALLIS", "KSCL", "JYOTHYLAB", "VBL"]
PLACEBO = ["TCS", "INFY", "WIPRO", "HCLTECH", "TECHM", "MPHASIS", "MINDTREE",
           "SUNPHARMA", "DRREDDY", "CIPLA", "LUPIN", "AUROPHARMA", "DIVISLAB"]
SEASON_END_MONTH = {"DJF": 2, "JFM": 3, "FMA": 4, "MAM": 5, "AMJ": 6, "MJJ": 7,
                    "JJA": 8, "JAS": 9, "ASO": 10, "SON": 11, "OND": 12, "NDJ": 1}

# --- onsets from the ONI file's own labels (rule in the registration) ---
oni = pd.read_csv(f"{VAULT}/climate/oni_seasonal_1950_2026.csv")
lab = (oni.oni == "el_nino").to_numpy()
onsets = []
for i in range(2, len(lab) - 2):
    if lab[i] and not lab[i - 1] and not lab[i - 2] and lab[i + 1] and lab[i + 2]:
        s, y = oni.season.iloc[i], int(oni.year.iloc[i])
        m = SEASON_END_MONTH[s]
        y_end = y + 1 if s == "NDJ" else y
        onsets.append((y, s, pd.Timestamp(y_end, m, 1) + pd.offsets.MonthEnd(0)))
print("onsets found (all-sample):", [(y, s) for y, s, _ in onsets])

# --- panel baskets ---
px = pd.read_csv(f"{VAULT}/panel/n500_adjclose_2012_2022.csv.gz",
                 parse_dates=["Date"]).set_index("Date").sort_index()
ret = px.pct_change(fill_method=None)
mkt = ret.mean(axis=1)


def rel_curve(names: list[str]) -> pd.Series:
    b = ret[[c for c in names if c in ret.columns]].mean(axis=1)
    return (b - mkt).dropna()


def zscore_of_window(rel: pd.Series, t0: pd.Timestamp, h: int):
    """Cum relative return over h td from first trading day after t0, z vs own rolling dist."""
    idx = rel.index[rel.index > t0]
    if len(idx) < h:
        return np.nan, np.nan
    win = rel.loc[idx[0]:idx[h - 1]]
    x = float((1 + win).prod() - 1)
    roll = (1 + rel).rolling(h).apply(np.prod, raw=True) - 1
    roll = roll.dropna()
    return x, float((x - roll.mean()) / roll.std(ddof=0))


for name, basket in [("TREATED", TREATED), ("PLACEBO", PLACEBO)]:
    rel = rel_curve(basket)
    print(f"\n{name} ({len([c for c in basket if c in ret.columns])} names, "
          f"panel span {rel.index[0].date()}..{rel.index[-1].date()})")
    for y, s, t0 in onsets:
        if t0 < rel.index[0] or t0 > rel.index[-1]:
            continue
        for h, tag in [(126, "6m"), (252, "12m")]:
            x, z = zscore_of_window(rel, t0, h)
            if np.isnan(x):
                print(f"  onset {y} {s}: {tag} window incomplete (panel ends)")
            else:
                print(f"  onset {y} {s} (event day after {t0.date()}): "
                      f"{tag} rel ret {100*x:+6.2f}%  z={z:+5.2f}")
