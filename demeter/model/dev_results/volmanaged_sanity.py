"""Data sanity for volmanaged (DEV ONLY): columns, range, EWMA-vol distribution by era, implied raw-target quantiles."""
import sys
from pathlib import Path
import numpy as np, pandas as pd
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
import engine as E, features as F

df = E.load_market(end="2012-06-30")
print("rows", len(df), "range", df.index[0].date(), df.index[-1].date())
print("cols", list(df.columns))
print("spx_ret NaN", int(df["spx_ret"].isna().sum()), "first valid", df["spx_ret"].first_valid_index().date())
for hl in (5, 10, 20):
    s = F.ewma_vol(df["spx_ret"], halflife=hl)
    for era, (a, b) in {"1950-69": ("1950", "1969"), "1970-89": ("1970", "1989"), "1990-99": ("1990", "1999"), "2000-12": ("2000", "2012")}.items():
        q = s.loc[a:b].quantile([0.1, 0.25, 0.5, 0.75, 0.9, 0.99]).round(3).tolist()
        print(f"hl={hl:2d} {era}: EWMA vol q10/25/50/75/90/99 = {q}")
s = F.ewma_vol(df["spx_ret"], halflife=10)
for tv in (0.12, 0.15, 0.18, 0.21):
    for p in (1, 2):
        t = ((tv / s) ** p).clip(0, 3).loc["1990":]
        print(f"tv={tv} p={p}: mean L {t.mean():.2f}  share@3x {(t>=2.99).mean():.2f}  share<0.5 {(t<0.5).mean():.2f}  share<1 {(t<1).mean():.2f}")
# 1987 and Oct-2008 EWMA vol paths (hl 10) for the leverage-effect discussion
for a, b in (("1987-10-05", "1987-10-30"), ("2008-09-25", "2008-10-31")):
    sub = pd.DataFrame({"ret%": (df["spx_ret"] * 100).round(2), "ewma10%": (s * 100).round(1)}).loc[a:b]
    print(sub.to_string())
