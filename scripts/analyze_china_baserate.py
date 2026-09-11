"""CN-D1..CN-D5 — the property-crash base rate. Registered 2026-09-11 BEFORE this run
(ledger entry of record: "Entry CN-D1..CN-D5"). Prints only; interpretation hand-appended.

Source: ingest/vault/jst/JSTdatasetR6.xlsx sheet 'JRT6 Data' (Jorda-Schularick-Taylor
Macrohistory R6, 18 countries 1870-2020). REAL house prices throughout (hpnom/cpi).
Episode definition frozen at registration: a real-house-price peak followed by a cumulative
decline >= 20% to trough, peaks >= 10 years apart (deeper kept on collision), trough reached
on or before 2020. Unfinished declines are EXCLUDED from the episode statistics and reported
separately, as registered.
"""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
DD_THRESH = 0.20        # registered
PEAK_SEP = 10           # registered
HYPERINF = 0.50         # stated economic exclusion for real-equity cells (not a data-dependent trim)
OUT = {}

d = pd.read_excel(f"{V}/jst/JSTdatasetR6.xlsx", sheet_name="JRT6 Data")
d = d.sort_values(["country", "year"]).reset_index(drop=True)
d["rhp"] = d["hpnom"] / d["cpi"]
d["infl"] = d.groupby("country")["cpi"].pct_change()
d["mort_gdp"] = d["tmort"] / d["gdp"]
d["hh_gdp"] = d["thh"] / d["gdp"]
print(f"[jst] {d.country.nunique()} countries {d.year.min()}-{d.year.max()}; "
      f"real HP obs {d.rhp.notna().sum():,}")


def episodes(g):
    """Completed >=20% real drawdown episodes for one country, plus any unfinished tail."""
    s = g.dropna(subset=["rhp"]).set_index("year")["rhp"]
    if len(s) < 15:
        return [], []
    cm = s.cummax()
    uw = s / cm - 1
    done, unfinished = [], []
    i, n = 0, len(s)
    yrs = s.index.to_numpy()
    while i < n:
        if uw.iloc[i] < 0:
            j = i
            while j < n and uw.iloc[j] < 0:
                j += 1
            seg = uw.iloc[i:j]
            if seg.min() <= -DD_THRESH:
                pk_year = yrs[i - 1] if i > 0 else yrs[i]
                tr_year = int(seg.idxmin())
                tr_pos = int(np.where(yrs == tr_year)[0][0])
                rec = {"peak": int(pk_year), "trough": tr_year, "depth": float(seg.min()) * 100,
                       "dur": int(tr_year - pk_year), "recovered": bool(j < n)}
                # trough identifiable = recovered, or >=3 further observations after the trough
                if j < n or (n - 1 - tr_pos) >= 3:
                    done.append(rec)
                else:
                    unfinished.append(rec)
            i = j
        else:
            i += 1
    return done, unfinished


rows, unfin = [], []
for c, g in d.groupby("country"):
    dn, un = episodes(g)
    s = g.dropna(subset=["rhp"]).set_index("year")
    for r in dn:
        r["country"] = c
        rows.append(r)
    for r in un:
        r["country"] = c
        unfin.append(r)

ep = pd.DataFrame(rows).sort_values(["country", "peak"]).reset_index(drop=True)
# enforce the registered 10-year peak separation: on collision keep the DEEPER episode
keep = []
for c, g in ep.groupby("country"):
    g = g.sort_values("depth")           # most negative (deepest) first
    chosen = []
    for _, r in g.iterrows():
        if all(abs(r.peak - k) >= PEAK_SEP for k in chosen):
            chosen.append(r.peak)
            keep.append(r.name)
ep = ep.loc[sorted(keep)].reset_index(drop=True)

# attach velocities and cycle statistics
idx = d.set_index(["country", "year"])
for i, r in ep.iterrows():
    c, pk, tr = r.country, int(r.peak), int(r.trough)
    def rhp(y):
        try:
            return float(idx.loc[(c, y), "rhp"])
        except KeyError:
            return np.nan
    p0, pp = rhp(pk), rhp(pk)
    ep.loc[i, "decl_vel"] = ((rhp(tr) / pp) ** (1 / max(tr - pk, 1)) - 1) * 100
    for w in (5, 10):
        pv = rhp(pk - w)
        ep.loc[i, f"pre{w}_vel"] = ((pp / pv) ** (1 / w) - 1) * 100 if pv and pv > 0 else np.nan
    for lbl, y in (("yd_pre5", pk - 5), ("yd_peak", pk), ("yd_trough", tr)):
        try:
            ep.loc[i, lbl] = float(idx.loc[(c, y), "housing_rent_yd"]) * 100
        except KeyError:
            ep.loc[i, lbl] = np.nan
ep["vel_ratio"] = ep.decl_vel.abs() / ep.pre5_vel

# ============================ CN-D1 ============================
print(f"\n=== CN-D1 crash anatomy === (real HP, >= {DD_THRESH:.0%} drawdown, peaks >= {PEAK_SEP}y apart)")
print(f"c1 EPISODE CENSUS: {len(ep)} completed episodes across {ep.country.nunique()} countries; "
      f"{len(unfin)} unfinished declines EXCLUDED (reported separately)")
print(ep[["country", "peak", "trough", "dur", "depth", "decl_vel", "pre5_vel", "pre10_vel", "vel_ratio"]]
      .to_string(index=False, float_format=lambda x: f"{x:7.2f}"))
print(f"  by decade of peak: " + ", ".join(f"{k}s:{v}" for k, v in
      sorted(((ep.peak // 10 * 10).value_counts()).items())))
q = lambda s, p: float(np.nanpercentile(s.dropna(), p))
for lbl, col, unit in [("c2 DEPTH (peak-to-trough real)", "depth", "%"),
                       ("c3 DURATION", "dur", "y"),
                       ("c4 DECLINE VELOCITY", "decl_vel", "%/yr"),
                       ("c5a PRE-CRASH 5y APPRECIATION", "pre5_vel", "%/yr"),
                       ("c5b PRE-CRASH 10y APPRECIATION", "pre10_vel", "%/yr"),
                       ("c6 VELOCITY RATIO |decline|/pre5", "vel_ratio", "x")]:
    s = ep[col]
    print(f"  {lbl:38s} median {s.median():7.2f}{unit:5s} p25 {q(s,25):7.2f}  p75 {q(s,75):7.2f}  "
          f"worst {(s.min() if col in ('depth','decl_vel') else s.max()):7.2f}  n={s.notna().sum()}")
OUT["CN-D1"] = {"episodes": ep.to_dict("records"), "unfinished": unfin,
                "median_depth": float(ep.depth.median()), "median_dur": float(ep.dur.median()),
                "median_decl_vel": float(ep.decl_vel.median()),
                "median_pre5": float(ep.pre5_vel.median()),
                "median_vel_ratio": float(ep.vel_ratio.median())}
md, mdur, mvr = ep.depth.median(), ep.dur.median(), ep.vel_ratio.median()
print(f"  CN-D1 BAR (a) median depth in [-40,-25]: {md:.2f} => {'HIT' if -40 <= md <= -25 else 'MISS'}")
print(f"  CN-D1 BAR (b) median duration >= 4y: {mdur:.1f} => {'HIT' if mdur >= 4 else 'MISS'}")
print(f"  CN-D1 BAR (c) median velocity ratio < 1.0 (bust slower than boom): {mvr:.3f} => "
      f"{'HIT - busts are slower per year than booms' if mvr < 1.0 else 'MISS - busts are FASTER than booms'}")
if unfin:
    print("  unfinished (excluded): " + "; ".join(
        f"{u['country']} {u['peak']}->{u['trough']} {u['depth']:.1f}%" for u in unfin))

# ============================ CN-D2 ============================
print("\n=== CN-D2 rental yield through the cycle === (housing_rent_yd, %)")
e2 = ep.dropna(subset=["yd_peak", "yd_trough"])
e2 = e2.assign(yd_chg=e2.yd_trough - e2.yd_peak, yd_comp=e2.yd_peak - e2.yd_pre5)
for lbl, col in [("d1 yield AT PEAK", "yd_peak"), ("d2 yield AT TROUGH", "yd_trough"),
                 ("d3 peak->trough CHANGE (pp)", "yd_chg"), ("d4 peak-5y -> peak CHANGE (pp)", "yd_comp")]:
    s = e2[col]
    print(f"  {lbl:32s} median {s.median():6.2f}  p25 {q(s,25):6.2f}  p75 {q(s,75):6.2f}  n={s.notna().sum()}")
ych, ycm = e2.yd_chg.median(), e2.yd_comp.median()
print(f"  CN-D2 BAR (a) median peak->trough yield expansion >= +1.0pp: {ych:+.2f} => "
      f"{'HIT' if ych >= 1.0 else 'MISS'}")
print(f"  CN-D2 BAR (b) yield COMPRESSES into the peak (peak below peak-5y): {ycm:+.2f}pp => "
      f"{'HIT' if ycm < 0 else 'MISS - no compression, so low yield is not a warning marker'}")
OUT["CN-D2"] = {"med_yd_peak": float(e2.yd_peak.median()), "med_yd_trough": float(e2.yd_trough.median()),
                "med_chg": float(ych), "med_compression": float(ycm), "n": int(len(e2))}

# ============================ CN-D3 ============================
print("\n=== CN-D3 what predicted it === (5y change in credit/GDP ahead of the peak; contingency lift)")
d["d5_mort"] = d.groupby("country")["mort_gdp"].diff(5) * 100
d["d5_hh"] = d.groupby("country")["hh_gdp"].diff(5) * 100
d["d5_pub"] = d.groupby("country")["debtgdp"].diff(5) * 100
pk = {(r.country, int(r.peak)) for _, r in ep.iterrows()}
d["is_peak"] = [(c, y) in pk for c, y in zip(d.country, d.year)]
d["peak_next3"] = (d.groupby("country")["is_peak"]
                   .transform(lambda s: s.shift(-1).fillna(False).astype(bool)
                              | s.shift(-2).fillna(False).astype(bool)
                              | s.shift(-3).fillna(False).astype(bool) | s.astype(bool)))
OUT["CN-D3"] = {}
for lbl, col in [("e1/e2 MORTGAGE credit", "d5_mort"), ("e3 HOUSEHOLD debt", "d5_hh"),
                 ("e4 PUBLIC debt (debtgdp)", "d5_pub")]:
    sub = d.dropna(subset=[col])
    at_peak = sub[sub.is_peak][col]
    uncond = sub[col]
    cut = np.nanpercentile(uncond, 80)
    top = sub[sub[col] >= cut]
    p_top = top.peak_next3.mean()
    p_base = sub.peak_next3.mean()
    lift = p_top / p_base if p_base else np.nan
    fp = 1 - p_top
    print(f"  {lbl:26s} run-up AT PEAK {at_peak.mean():+6.2f}pp vs panel mean {uncond.mean():+6.2f}pp "
          f"| top-quintile cut {cut:+6.2f}pp: P(peak<=3y) {p_top:5.1%} vs base {p_base:5.1%} "
          f"=> LIFT {lift:4.2f}x | false-positive {fp:5.1%} (n_top={len(top)})")
    OUT["CN-D3"][col] = {"at_peak": float(at_peak.mean()), "uncond": float(uncond.mean()),
                         "cut": float(cut), "p_top": float(p_top), "p_base": float(p_base),
                         "lift": float(lift), "fp": float(fp), "n_top": int(len(top))}
lm = OUT["CN-D3"]["d5_mort"]["lift"]
lp = OUT["CN-D3"]["d5_pub"]["lift"]
fpm = OUT["CN-D3"]["d5_mort"]["fp"]
print(f"  CN-D3 BAR (a) mortgage lift >= 1.5x: {lm:.2f} => {'HIT' if lm >= 1.5 else 'MISS'}")
print(f"  CN-D3 BAR (b) public-debt lift in [0.8,1.25] (no predictive power): {lp:.2f} => "
      f"{'HIT' if 0.8 <= lp <= 1.25 else 'MISS'}")
print(f"  CN-D3 BAR (c) mortgage false-positive rate >= 50%: {fpm:.1%} => {'HIT' if fpm >= 0.50 else 'MISS'}")

# ============================ CN-D4 ============================
print("\n=== CN-D4 does a bigger boom crash faster, or only further? ===")
e4 = ep.dropna(subset=["pre5_vel"])
med = e4.pre5_vel.median()
big, small = e4[e4.pre5_vel >= med], e4[e4.pre5_vel < med]
print(f"  split at median pre-crash 5y velocity {med:.2f}%/yr (big n={len(big)}, small n={len(small)})")
for lbl, col in [("f1 DEPTH", "depth"), ("f2 DURATION", "dur"), ("f3 DECLINE VELOCITY", "decl_vel")]:
    print(f"  {lbl:22s} big-boom {big[col].median():7.2f}  small-boom {small[col].median():7.2f}  "
          f"gap {big[col].median()-small[col].median():+7.2f}")
dgap = small.depth.median() - big.depth.median()      # positive = big-boom episodes are deeper
vgap = abs(big.decl_vel.median() - small.decl_vel.median())
print(f"  CN-D4 BAR big-boom episodes deeper by >= 8pp: {dgap:+.2f}pp => {'HIT' if dgap >= 8 else 'MISS'}")
print(f"  CN-D4 PRIOR not materially faster (velocity gap < 2pp/yr): {vgap:.2f} => "
      f"{'HIT' if vgap < 2 else 'MISS'}")
OUT["CN-D4"] = {"median_split": float(med), "depth_gap": float(dgap), "vel_gap": float(vgap),
                "big": {k: float(big[k].median()) for k in ("depth", "dur", "decl_vel")},
                "small": {k: float(small[k].median()) for k in ("depth", "dur", "decl_vel")}}

# ============================ CN-D5 ============================
print("\n=== CN-D5 equities after a housing peak === (real eq_tr; hyperinflation years excluded)")
d["real_eq"] = (1 + d["eq_tr"]) / (1 + d["infl"]) - 1
d.loc[d.infl.abs() > HYPERINF, "real_eq"] = np.nan     # stated economic exclusion, not a trim
d["crisis3"] = d.groupby("country")["crisisJST"].transform(
    lambda s: s.rolling(4, min_periods=1).max().shift(-3))
eqi = d.set_index(["country", "year"])["real_eq"]
cri = d.set_index(["country", "year"])["crisis3"]


def fwd(c, y, h):
    v = [eqi.get((c, y + k), np.nan) for k in range(1, h + 1)]
    v = [x for x in v if pd.notna(x)]
    if len(v) < h:
        return np.nan
    return (np.prod([1 + x for x in v]) ** (1 / h) - 1) * 100


res = []
for _, r in ep.iterrows():
    c, pk = r.country, int(r.peak)
    res.append({"country": c, "peak": pk,
                "f1": fwd(c, pk, 1), "f3": fwd(c, pk, 3), "f5": fwd(c, pk, 5),
                "crisis": cri.get((c, pk), np.nan)})
R = pd.DataFrame(res)
# horizon-matched unconditional benchmarks, same geometric annualization as the episode cells
UNC = {}
for h in (1, 3, 5):
    vals = [fwd(c, y, h) for c, y in zip(d.country, d.year)]
    vals = [v for v in vals if pd.notna(v)]
    UNC[h] = float(np.mean(vals))
u1 = UNC[1]
print(f"  g5 panel UNCONDITIONAL real equity return, horizon-matched and geometric: "
      f"1y {UNC[1]:+.2f}%  3y {UNC[3]:+.2f}%  5y {UNC[5]:+.2f}%")
for lbl, col, h in [("g1 next-1y", "f1", 1), ("g2 next-3y ann", "f3", 3), ("g3 next-5y ann", "f5", 5)]:
    print(f"  {lbl:16s} all episodes {R[col].mean():+7.2f}%  (excess vs matched {R[col].mean()-UNC[h]:+7.2f}pp)  "
          f"n={R[col].notna().sum()}")
cy, cn = R[R.crisis == 1], R[R.crisis == 0]
print(f"  g4 SPLIT by banking crisis within 3y of the peak (crisis n={len(cy)}, no-crisis n={len(cn)}):")
for col, lbl, h in [("f1", "next-1y", 1), ("f3", "next-3y ann", 3), ("f5", "next-5y ann", 5)]:
    print(f"     {lbl:14s} crisis {cy[col].mean():+7.2f}% (excess {cy[col].mean()-UNC[h]:+6.2f}pp)  "
          f"no-crisis {cn[col].mean():+7.2f}% (excess {cn[col].mean()-UNC[h]:+6.2f}pp)  "
          f"gap {cy[col].mean()-cn[col].mean():+7.2f}pp")
e_cy = cy.f1.mean() - u1
e_cn = cn.f1.mean() - u1
print(f"  CN-D5 BAR (a) crisis subset next-1y negative AND <= -8pp excess: {cy.f1.mean():+.2f}% / "
      f"{e_cy:+.2f}pp => {'HIT' if cy.f1.mean() < 0 and e_cy <= -8 else 'MISS'}")
print(f"  CN-D5 BAR (b) no-crisis subset within 3pp of unconditional: {e_cn:+.2f}pp => "
      f"{'HIT - a housing peak alone is not an equity event' if abs(e_cn) <= 3 else 'MISS'}")
OUT["CN-D5"] = {"uncond": UNC,
                "all": {k: float(R[k].mean()) for k in ("f1", "f3", "f5")},
                "crisis": {k: float(cy[k].mean()) for k in ("f1", "f3", "f5")},
                "nocrisis": {k: float(cn[k].mean()) for k in ("f1", "f3", "f5")},
                "n_crisis": int(len(cy)), "n_nocrisis": int(len(cn))}

# ---------------- UNREGISTERED SUB-READ: the modern era (peaks from 1970) ----------------
print("\n=== ADDENDUM (UNREGISTERED SUB-READ): peaks from 1970 only ===")
print("    Reason: the pre-WWII episodes are dominated by war and inflation, not property cycles")
print("    (65- and 56-year 'declines', a real fall beyond -90%). The registered bars above stand")
print("    on the full sample as written; this is reported alongside, never instead.")
mod = ep[ep.peak >= 1970]
print(f"    n={len(mod)} episodes, {mod.country.nunique()} countries")
for lbl, col, unit in [("depth", "depth", "%"), ("duration", "dur", "y"),
                       ("decline velocity", "decl_vel", "%/yr"),
                       ("pre-crash 5y appreciation", "pre5_vel", "%/yr"),
                       ("velocity ratio", "vel_ratio", "x")]:
    s_ = mod[col]
    print(f"      {lbl:28s} median {s_.median():7.2f}{unit:5s} p25 {q(s_,25):7.2f} p75 {q(s_,75):7.2f} n={s_.notna().sum()}")
m2 = mod.dropna(subset=["yd_peak", "yd_trough"])
if len(m2):
    print(f"      rental yield peak {m2.yd_peak.median():.2f}% -> trough {m2.yd_trough.median():.2f}% "
          f"(change {(m2.yd_trough-m2.yd_peak).median():+.2f}pp, n={len(m2)})")
m4 = mod.dropna(subset=["pre5_vel"])
mm = m4.pre5_vel.median()
mb, ms = m4[m4.pre5_vel >= mm], m4[m4.pre5_vel < mm]
print(f"      CN-D4 re-read: big-boom depth {mb.depth.median():.2f} vs small {ms.depth.median():.2f} "
        f"(gap {ms.depth.median()-mb.depth.median():+.2f}pp); velocity {mb.decl_vel.median():.2f} vs "
        f"{ms.decl_vel.median():.2f}")
OUT["modern_era"] = {"n": int(len(mod)),
                     "median": {k: float(mod[k].median()) for k in ("depth", "dur", "decl_vel", "pre5_vel", "vel_ratio")},
                     "yd_peak": float(m2.yd_peak.median()) if len(m2) else None,
                     "yd_trough": float(m2.yd_trough.median()) if len(m2) else None,
                     "d4_depth_gap": float(ms.depth.median() - mb.depth.median())}

with open("/home/user/claude-demo/research/china_baserate.json", "w") as f:
    json.dump(OUT, f, indent=1, default=float)
print("\nwrote research/china_baserate.json")
