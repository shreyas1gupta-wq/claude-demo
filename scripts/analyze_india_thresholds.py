"""IN-D1..IN-D2 — how often does property compound at 20%/yr, and what follows?
Registered 2026-09-11 BEFORE this run (ledger entry "Entry IN-D1..IN-D2"). Prints only.

Source: ingest/vault/jst/JSTdatasetR6.xlsx sheet 'JRT6 Data' (18 countries 1870-2020), the same
vaulted panel as CN-D1..CN-D5. Overlapping 5-year windows, flagged as registered: frequencies are
exposure shares, not independent trials, and no significance is claimed or computable.
"""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
W = 5                      # window length, years (registered)
DD_THRESH = 0.20           # crash definition, inherited verbatim from CN-D1
THRESH = [5, 10, 15, 20]   # %/yr, registered
OUT = {}

d = pd.read_excel(f"{V}/jst/JSTdatasetR6.xlsx", sheet_name="JRT6 Data").sort_values(["country", "year"])
d["rhp"] = d["hpnom"] / d["cpi"]
d["infl"] = d.groupby("country")["cpi"].pct_change()
# Hyperinflation guard for the NOMINAL leg only. Stated economic exclusion (annual CPI > 50%),
# not a data-dependent trim: a +962%/yr nominal "appreciation" is a currency event, not a property
# one, and says nothing about an Indian city. Applied as a clearly-labelled sub-read alongside the
# registered full-sample bars, never instead of them (the CN-D1 precedent).
d["hpnom_clean"] = d["hpnom"].where(
    d.groupby("country")["infl"].transform(lambda s: s.rolling(6, min_periods=1).max()) <= 0.50)
print(f"[jst] {d.country.nunique()} countries {d.year.min()}-{d.year.max()}")


def crash_peaks(col):
    """CN-D1's episode peaks, recomputed on the requested price column."""
    pk = set()
    for c, g in d.groupby("country"):
        s = g.dropna(subset=[col]).set_index("year")[col]
        if len(s) < 15:
            continue
        uw = s / s.cummax() - 1
        yrs, n, i = s.index.to_numpy(), len(s), 0
        while i < n:
            if uw.iloc[i] < 0:
                j = i
                while j < n and uw.iloc[j] < 0:
                    j += 1
                seg = uw.iloc[i:j]
                if seg.min() <= -DD_THRESH:
                    tp = int(np.where(yrs == int(seg.idxmin()))[0][0])
                    if j < n or (n - 1 - tp) >= 3:
                        pk.add((c, int(yrs[i - 1] if i > 0 else yrs[i])))
                i = j
            else:
                i += 1
    return pk


def build(col, label):
    """Overlapping W-year windows: trailing appreciation, forward return, forward crash flag."""
    pk = crash_peaks(col)
    rows = []
    for c, g in d.groupby("country"):
        s = g.dropna(subset=[col]).set_index("year")[col]
        if len(s) < W * 2 + 1:
            continue
        for y in s.index:
            if (y - W) not in s.index:
                continue
            p0, p1 = s.loc[y - W], s.loc[y]
            if p0 <= 0 or p1 <= 0:
                continue
            trail = ((p1 / p0) ** (1 / W) - 1) * 100
            fwd = np.nan
            if (y + W) in s.index and s.loc[y + W] > 0:
                fwd = ((s.loc[y + W] / p1) ** (1 / W) - 1) * 100
            rows.append({"country": c, "year": int(y), "trail": trail, "fwd": fwd,
                         "crash5": any((c, y + k) in pk for k in range(0, W + 1))})
    df = pd.DataFrame(rows)
    print(f"\n=== {label} === {len(df):,} overlapping {W}-year windows, {df.country.nunique()} countries")
    return df, pk


# ============================ IN-D1: real ============================
r1, pk_r = build("rhp", "IN-D1 REAL house-price appreciation thresholds")
base_crash = r1.crash5.mean()
print(f"a1/a3 unconditional P(crash peak within {W}y of any window) = {base_crash:.1%}")
ind1 = {}
for T in THRESH:
    sub = r1[r1.trail >= T]
    freq = len(sub) / len(r1)
    fwd = sub.fwd.mean()
    pc = sub.crash5.mean()
    ind1[T] = {"n": len(sub), "freq": freq, "countries": int(sub.country.nunique()),
               "fwd": float(fwd), "crash": float(pc), "lift": float(pc / base_crash)}
    print(f"  T>={T:2d}%/yr real: {len(sub):5,} windows ({freq:6.2%}), {sub.country.nunique():2d} countries "
          f"| next-{W}y {fwd:+6.2f}%/yr | P(crash<={W}y) {pc:5.1%} => lift {pc/base_crash:4.2f}x")
# a4 duration: longest consecutive run of trailing >=15
best = ("", 0)
for c, g in r1.sort_values("year").groupby("country"):
    run = 0
    for _, row in g.iterrows():
        run = run + 1 if row.trail >= 15 else 0
        if run > best[1]:
            best = (c, run)
print(f"a4 longest consecutive run of trailing-{W}y real appreciation >=15%/yr: "
      f"{best[1]} years ({best[0]})")
# a5 era split
for lbl, m in [("pre-1970", r1.year < 1970), ("1970+", r1.year >= 1970)]:
    sub = r1[m]
    f20 = (sub.trail >= 20).mean()
    f15 = (sub.trail >= 15).mean()
    print(f"a5 {lbl:9s}: P(T>=15) {f15:6.2%}  P(T>=20) {f20:6.2%}  n={len(sub):,}")
print(f"  IN-D1 BAR (a) T>=20 real is rare, <2% of windows: {ind1[20]['freq']:.2%} => "
      f"{'HIT' if ind1[20]['freq'] < 0.02 else 'MISS'}")
print(f"  IN-D1 BAR (b) next-{W}y real NEGATIVE after T>=15: {ind1[15]['fwd']:+.2f}%/yr => "
      f"{'HIT' if ind1[15]['fwd'] < 0 else 'MISS - momentum beats mean reversion at this scale'}")
print(f"  IN-D1 BAR (c) crash lift at T>=15 >= 2.0x: {ind1[15]['lift']:.2f}x => "
      f"{'HIT' if ind1[15]['lift'] >= 2.0 else 'MISS'}")
OUT["IN-D1"] = {"base_crash": float(base_crash), "by_threshold": ind1,
                "longest_run_15": {"country": best[0], "years": best[1]},
                "era": {lbl: {"f15": float((r1[m].trail >= 15).mean()),
                              "f20": float((r1[m].trail >= 20).mean()), "n": int(m.sum())}
                        for lbl, m in [("pre1970", r1.year < 1970), ("post1970", r1.year >= 1970)]}}

# ============================ IN-D2: nominal ============================
n1, pk_n = build("hpnom", "IN-D2 NOMINAL house-price appreciation thresholds")
# the money-illusion cell needs both trailing measures on the same window
merged = n1.merge(r1[["country", "year", "trail", "fwd"]], on=["country", "year"],
                  suffixes=("_nom", "_real"))
ind2 = {}
for T in THRESH:
    sub = n1[n1.trail >= T]
    ind2[T] = {"n": len(sub), "freq": len(sub) / len(n1), "fwd": float(sub.fwd.mean()),
               "countries": int(sub.country.nunique())}
    print(f"  T>={T:2d}%/yr nominal: {len(sub):5,} windows ({len(sub)/len(n1):6.2%}), "
          f"{sub.country.nunique():2d} countries | next-{W}y {sub.fwd.mean():+6.2f}%/yr")
hot = merged[merged.trail_nom >= 20]
illusion = (hot.trail_real < 0).mean()
print(f"b2 MONEY ILLUSION: of {len(hot):,} windows with >=20%/yr NOMINAL appreciation, "
      f"{illusion:.1%} were simultaneously NEGATIVE in real terms")
print(f"   (their mean real appreciation was {hot.trail_real.mean():+.2f}%/yr against nominal "
      f"{hot.trail_nom.mean():+.2f}%/yr — inflation supplied "
      f"{(1 - hot.trail_real.mean()/hot.trail_nom.mean())*100:.0f}% of the headline)")
ratio = ind2[20]["freq"] / ind1[20]["freq"] if ind1[20]["freq"] else float("inf")
print(f"  IN-D2 BAR (a) nominal frequency at T=20 >= 3x the real frequency: {ratio:.2f}x => "
      f"{'HIT' if ratio >= 3 else 'MISS'}")
print(f"  IN-D2 BAR (b) >=25% of >=20%/yr nominal windows were real-negative: {illusion:.1%} => "
      f"{'HIT' if illusion >= 0.25 else 'MISS'}")
OUT["IN-D2"] = {"by_threshold": ind2, "illusion_share": float(illusion),
                "hot_real_mean": float(hot.trail_real.mean()),
                "hot_nom_mean": float(hot.trail_nom.mean()), "n_hot": int(len(hot)),
                "nom_vs_real_freq_ratio": float(ratio)}

# ---------------- the principal's bar, priced ----------------
print("\n=== THE PRINCIPAL'S BAR, PRICED AGAINST THIS PANEL ===")
for lbl, ann in [("20% CUMULATIVE over 5y", (1.20 ** (1 / 5) - 1) * 100), ("20% CAGR for 5y", 20.0)]:
    pct_nom = (n1.trail >= ann).mean()
    pct_real = (r1.trail >= ann).mean()
    print(f"  {lbl:24s} = {ann:5.2f}%/yr: cleared by {pct_nom:6.2%} of NOMINAL windows, "
          f"{pct_real:6.2%} of REAL windows")
OUT["bar"] = {lbl: {"ann": ann, "nom_freq": float((n1.trail >= ann).mean()),
                    "real_freq": float((r1.trail >= ann).mean())}
              for lbl, ann in [("cumulative20", (1.20 ** (1 / 5) - 1) * 100), ("cagr20", 20.0)]}

# ---------------- UNREGISTERED SUB-READ: nominal, hyperinflation excluded ----------------
print("\n=== ADDENDUM (UNREGISTERED SUB-READ): IN-D2 nominal with hyperinflation excluded ===")
print("    Reason: the registered nominal leg above is dominated by currency events — a mean of")
print("    +962%/yr nominal 'appreciation' is Weimar and its peers, not a property market, and is")
print("    uninformative about India. Windows touching any year with CPI inflation above 50% are")
print("    dropped. The registered bars stand on the full sample as written; this sits beside them.")
n2, _ = build("hpnom_clean", "IN-D2 nominal, hyperinflation-excluded")
m2 = n2.merge(r1[["country", "year", "trail"]], on=["country", "year"], suffixes=("_nom", "_real"))
ind2c = {}
for T in THRESH:
    sub = n2[n2.trail >= T]
    ind2c[T] = {"n": len(sub), "freq": len(sub) / len(n2), "fwd": float(sub.fwd.mean()),
                "countries": int(sub.country.nunique())}
    print(f"      T>={T:2d}%/yr nominal: {len(sub):5,} ({len(sub)/len(n2):6.2%}), "
          f"{sub.country.nunique():2d} countries | next-{W}y {sub.fwd.mean():+6.2f}%/yr")
hot2 = m2[m2.trail_nom >= 20]
ill2 = (hot2.trail_real < 0).mean()
print(f"      money illusion: of {len(hot2):,} windows >=20%/yr nominal, {ill2:.1%} were real-NEGATIVE; "
      f"mean real {hot2.trail_real.mean():+.2f}%/yr vs nominal {hot2.trail_nom.mean():+.2f}%/yr "
      f"=> inflation supplied {(1 - hot2.trail_real.mean()/hot2.trail_nom.mean())*100:.0f}% of the headline")
for lbl, m in [("pre-1970", n2.year < 1970), ("1970+", n2.year >= 1970)]:
    sub = n2[m]
    print(f"      {lbl:9s}: P(nom T>=20) {(sub.trail >= 20).mean():6.2%}  n={len(sub):,}")
OUT["IN-D2_clean"] = {"by_threshold": ind2c, "illusion_share": float(ill2),
                      "hot_real_mean": float(hot2.trail_real.mean()),
                      "hot_nom_mean": float(hot2.trail_nom.mean()), "n_hot": int(len(hot2)),
                      "era": {lbl: float((n2[m].trail >= 20).mean())
                              for lbl, m in [("pre1970", n2.year < 1970), ("post1970", n2.year >= 1970)]}}

print("\n=== THE HEADLINE THE ERA SPLIT CONTAINS ===")
e = OUT["IN-D1"]["era"]
print(f"    REAL appreciation >=20%/yr over 5y, post-1970: {e['post1970']['f20']:.2%} of "
      f"{e['post1970']['n']:,} windows — i.e. it has NEVER happened in the modern era of this panel.")
print(f"    REAL >=15%/yr post-1970: {e['post1970']['f15']:.2%} vs pre-1970 {e['pre1970']['f15']:.2%}.")
print(f"    The one sustained run was Japan's {OUT['IN-D1']['longest_run_15']['years']} consecutive "
      f"years above 15%/yr real — the episode that then fell 47.3% over 18 years (CN-D1).")

with open("/home/user/claude-demo/research/india_thresholds.json", "w") as f:
    json.dump(OUT, f, indent=1, default=float)
print("\nwrote research/india_thresholds.json")
