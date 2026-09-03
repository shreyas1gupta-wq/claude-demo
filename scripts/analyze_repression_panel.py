"""Post-WWII financial-repression panel: real asset returns 1950-1980 from the JST vault.

CONTEXT NOTE computation (descriptive; no hypothesis, no bars, no census consumption).
Per country: real geometric CAGR of equities (eq_tr), housing (housing_tr), government
bonds (bond_tr), bills (bill_rate), plus avg CPI inflation and the debt/GDP descent
1945->1980. Gold (USD, deflated by US CPI) from the commodities vault. Medians across the
18-economy panel and across assets. Real return_t = (1+nom_t)/(1+infl_t) - 1.
"""
import numpy as np
import pandas as pd

VAULT = "/home/user/claude-demo/ingest/vault"
Y0, Y1 = 1951, 1980          # returns for the 1950->1980 holding period
MIN_YEARS = 26               # of 30; else mark partial

jst = pd.read_csv(f"{VAULT}/jst/jstdatasetr4.csv",
                  usecols=["year", "iso", "cpi", "eq_tr", "housing_tr", "bond_tr",
                           "bill_rate", "debtgdp"])
jst = jst.sort_values(["iso", "year"])
jst["infl"] = jst.groupby("iso")["cpi"].pct_change()

def real_cagr(g: pd.DataFrame, col: str) -> tuple[float, int]:
    w = g[(g.year >= Y0) & (g.year <= Y1)][[col, "infl"]].dropna()
    if len(w) == 0:
        return np.nan, 0
    real = (1 + w[col]) / (1 + w["infl"]) - 1
    return float(np.exp(np.log1p(real).mean()) - 1), len(w)

rows = []
for iso, g in jst.groupby("iso"):
    eq, n_eq = real_cagr(g, "eq_tr")
    hs, n_hs = real_cagr(g, "housing_tr")
    bd, n_bd = real_cagr(g, "bond_tr")
    bl, n_bl = real_cagr(g, "bill_rate")
    w = g[(g.year >= Y0) & (g.year <= Y1)]["infl"].dropna()
    infl = float(np.exp(np.log1p(w).mean()) - 1) if len(w) else np.nan
    d45 = g.loc[g.year == 1945, "debtgdp"]
    d80 = g.loc[g.year == 1980, "debtgdp"]
    rows.append(dict(iso=iso, eqty=eq, n_eq=n_eq, housing=hs, n_hs=n_hs, bond=bd,
                     n_bd=n_bd, bill=bl, n_bl=n_bl, infl=infl,
                     debt45=float(d45.iloc[0]) if len(d45) and pd.notna(d45.iloc[0]) else np.nan,
                     debt80=float(d80.iloc[0]) if len(d80) and pd.notna(d80.iloc[0]) else np.nan))
df = pd.DataFrame(rows).set_index("iso")

print(f"REAL GEOMETRIC CAGR {Y0-1}->{Y1} (percent/yr); * = <{MIN_YEARS} yrs of data")
print(f"{'iso':4} {'equity':>8} {'housing':>8} {'bond':>8} {'bill':>8} {'infl':>6}"
      f" {'debt/GDP 45->80':>16}")
for iso, r in df.sort_values("eqty", ascending=False).iterrows():
    def f(v, n):
        return ("   n/a  " if pd.isna(v) else f"{100*v:7.1f}{'*' if n < MIN_YEARS else ' '}")
    dbt = ("" if pd.isna(r.debt45) or pd.isna(r.debt80)
           else f"{100*r.debt45:6.0f} -> {100*r.debt80:4.0f}")
    print(f"{iso:4} {f(r.eqty, r.n_eq)} {f(r.housing, r.n_hs)} {f(r.bond, r.n_bd)}"
          f" {f(r.bill, r.n_bl)} {100*r.infl:5.1f}  {dbt:>16}")

med = df[["eqty", "housing", "bond", "bill", "infl"]].median()
print("\nPANEL MEDIANS (18 economies):")
for k, label in [("eqty", "equities"), ("housing", "housing"), ("bond", "govt bonds"),
                 ("bill", "bills/cash"), ("infl", "inflation")]:
    print(f"  {label:11}: {100*med[k]:+6.1f} %/yr real")

# gold in USD, deflated by US CPI, 1950->1980 and the 1971 split
gold = pd.read_csv(f"{VAULT}/commodities/gold_monthly_1833_2026.csv")
gold.columns = [c.strip().lower() for c in gold.columns]
dcol = [c for c in gold.columns if "date" in c or "month" in c or "year" in c][0]
pcol = [c for c in gold.columns if c != dcol][0]
gold["year"] = pd.to_datetime(gold[dcol]).dt.year
gy = gold.groupby("year")[pcol].last()
uscpi = jst[jst.iso == "USA"].set_index("year")["cpi"]
for a, b in [(1950, 1980), (1950, 1970), (1970, 1980)]:
    nom = (gy[b] / gy[a]) ** (1 / (b - a)) - 1
    infl = (uscpi[b] / uscpi[a]) ** (1 / (b - a)) - 1
    real = (1 + nom) / (1 + infl) - 1
    print(f"  gold {a}->{b}: {100*real:+6.1f} %/yr real  (${gy[a]:.0f} -> ${gy[b]:.0f})")

# equity sub-periods: the golden age vs the 1970s
print("\nEQUITY REAL CAGR SUB-PERIODS (median across panel):")
for a, b in [(1950, 1968), (1968, 1980)]:
    sub = []
    for iso, g in jst.groupby("iso"):
        w = g[(g.year > a) & (g.year <= b)][["eq_tr", "infl"]].dropna()
        if len(w) >= (b - a) - 2:
            sub.append(np.exp(np.log1p((1 + w.eq_tr) / (1 + w.infl) - 1).mean()) - 1)
    print(f"  {a}->{b}: median {100*np.median(sub):+5.1f} %/yr real  (n={len(sub)})")
