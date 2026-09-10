"""EQ-D1 — the earnings-quality / accrual-divergence battery.
Registered 2026-09-10 BEFORE this run (ledger entry of record). All constructions
are RANK-DIVERGENCE PROXIES (the panel's fields are already per-date uniformized
to (0,1]) — never the literal dollar-value Sloan/Beneish formulas.
Prints only; interpretation hand-appended to the ledger after."""
import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"

use = ["stock_id", "date", "Ni", "Ocf", "Ta", "Op_Margin", "Ocf_Margin", "Net_Margin",
       "Debtequity", "Pb", "Mkt_Cap_12M_Usd", "R1M_Usd", "R12M_Usd"]
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", usecols=use, parse_dates=["date"])


def dec(s, n=10):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


r = fp.pivot_table(index="date", columns="stock_id", values="R1M_Usd")
lg = np.log1p(r)
f36 = ((np.exp(lg.rolling(36, min_periods=27).sum().shift(-35) * (12 / 36)) - 1) * 100).stack().rename("f36")

op_m = fp.pivot_table(index="date", columns="stock_id", values="Op_Margin")
margin_decline = (op_m.shift(12) - op_m).stack().rename("margin_decline")
de = fp.pivot_table(index="date", columns="stock_id", values="Debtequity")
lev_increase = (de - de.shift(12)).stack().rename("lev_increase")

fp = fp.set_index(["date", "stock_id"])
fp["tata_proxy"] = fp.Ni - fp.Ocf  # both already per-date ranks in (0,1]
fp["cash_conv_proxy"] = fp.Ocf_Margin - fp.Net_Margin
fp = fp.join(f36).join(margin_decline).join(lev_increase)
fp = fp.reset_index()
fp["sz"] = fp.groupby("date").Mkt_Cap_12M_Usd.transform(dec, n=5)
fp["pb_q"] = fp.groupby("date").Pb.transform(dec, n=5)

print("=" * 100)
print("EQ-D1 — earnings-quality / accrual-divergence battery (rank-divergence proxies)")
print("=" * 100)


def ladder(df, col, n=10):
    df = df.copy()
    df["d"] = df.groupby("date")[col].transform(dec, n=n)
    s1 = (df[df.d == n].R1M_Usd.mean() - df[df.d == 1].R1M_Usd.mean()) * 1200
    s12 = (df[df.d == n].R12M_Usd.mean() - df[df.d == 1].R12M_Usd.mean()) * 100
    s36 = df[df.d == n].f36.mean() - df[df.d == 1].f36.mean()
    return s1, s12, s36


s1, s12, s36 = ladder(fp, "tata_proxy")
print(f"e1 TATA_proxy (Ni_rank - Ocf_rank) D10-D1, panel: 1m {s1:+.2f} | 12m {s12:+.2f} | 36m {s36:+.2f}")
big = fp[fp.sz == 5]
b1, b12, b36 = ladder(big, "tata_proxy")
print(f"   large-cap (szQ5): 1m {b1:+.2f} | 12m {b12:+.2f} | 36m {b36:+.2f}")

_, e2_12, _ = ladder(fp.dropna(subset=["margin_decline"]), "margin_decline")
print(f"e2 margin_decline (Op_Margin t-12 minus t) D10-D1, fwd-12m: {e2_12:+.2f}")

_, e3_12, _ = ladder(fp.dropna(subset=["lev_increase"]), "lev_increase")
print(f"e3 leverage_increase (Debtequity t minus t-12) D10-D1, fwd-12m: {e3_12:+.2f}")

_, e4_12, _ = ladder(fp, "cash_conv_proxy")
print(f"e4 cash_conversion_proxy (Ocf_Margin - Net_Margin) D10-D1, fwd-12m: {e4_12:+.2f} (mirror-check of e1)")

comp_df = fp.dropna(subset=["margin_decline", "lev_increase"]).copy()
for c in ["tata_proxy", "margin_decline", "lev_increase"]:
    comp_df[c + "_r"] = comp_df.groupby("date")[c].transform(lambda x: x.rank(pct=True))
comp_df["composite"] = comp_df[["tata_proxy_r", "margin_decline_r", "lev_increase_r"]].mean(axis=1)
c1, c12, c36 = ladder(comp_df, "composite")
print(f"e5 COMPOSITE (mean rank of tata+margin_decline+lev_increase) D10-D1, panel: "
      f"1m {c1:+.2f} | 12m {c12:+.2f} | 36m {c36:+.2f}")
bigc = comp_df[comp_df.sz == 5]
bc1, bc12, bc36 = ladder(bigc, "composite")
print(f"   large-cap (szQ5): 1m {bc1:+.2f} | 12m {bc12:+.2f} | 36m {bc36:+.2f}")

cheap = comp_df[comp_df.pb_q <= 2].copy()
med = cheap.groupby("date").composite.transform("median")
good = cheap.composite <= med  # low red-flag score = "good" cheap
g12 = (cheap[good].R12M_Usd.mean() - cheap[~good].R12M_Usd.mean()) * 100
g36 = cheap[good].f36.mean() - cheap[~good].f36.mean()
print(f"e6 VALUE-TRAP CROSS — among cheap (Pb Q1-2), low-redflag minus high-redflag half: "
      f"12m {g12:+.2f} | 36m {g36:+.2f}")

for era, (d0, d1) in [("1999-2009", ("1999", "2009")), ("2010-2019", ("2010", "2019"))]:
    sub = fp[(fp.date >= d0) & (fp.date <= d1 + "-12-31")]
    _, e7, _ = ladder(sub, "tata_proxy")
    print(f"e7 era split {era}: TATA_proxy D10-D1 fwd-12m {e7:+.2f}")

_, e8, _ = ladder(big, "tata_proxy")
print(f"e8 large-cap-only (szQ5) TATA_proxy D10-D1 fwd-12m: {e8:+.2f} (repeats the large-cap row of e1)")
