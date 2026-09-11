"""G1-G4 — the construction-mechanics battery. Registered 2026-09-11 BEFORE this run
(ledger entry of record: "Entry G1-G4"). Prints only; interpretation hand-appended after.

Statutory cost comes from quant/costs/statutory (registry-driven, never a hardcoded rate)
and tax rates from config/costs.yaml capital_gains_tax_india — per process note #6 no
estimation or rate constant is re-implemented here.
"""
import numpy as np
import pandas as pd

from quant.costs.statutory import round_trip_bps
from quant.registry.loader import load_registry

V = "/home/user/claude-demo/ingest/vault"
SEED = 20260911

reg = load_registry()
RT_BPS = round_trip_bps(reg, "cash_delivery")
TAX = reg["costs"]["capital_gains_tax_india"]
H_THRESH = TAX["holding_threshold_months"]["value"]
print(f"[registry] cash_delivery round-trip = {RT_BPS:.2f} bps | LTCG threshold = {H_THRESH}m")
print(f"[registry] pre-Jul2024 stcg/ltcg = {TAX['pre_2024_07']['stcg_rate']['value']:.3f}/"
      f"{TAX['pre_2024_07']['ltcg_rate']['value']:.3f} | post = "
      f"{TAX['post_2024_07']['stcg_rate']['value']:.3f}/{TAX['post_2024_07']['ltcg_rate']['value']:.3f}")


def ann_stats(mret: pd.Series):
    """CAGR, ann vol, maxDD from a monthly simple-return series."""
    w = (1 + mret).cumprod()
    yrs = len(mret) / 12
    cagr = w.iloc[-1] ** (1 / yrs) - 1
    vol = mret.std() * np.sqrt(12)
    dd = (w / w.cummax() - 1).min()
    return cagr * 100, vol * 100, dd * 100


# ============================ G1: rebalance grid ============================
nif = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).sort_values("Date")
nif_m = nif.set_index("Date")["Adj Close"].resample("ME").last()
gold = pd.read_csv(f"{V}/commodities/gold_monthly_1833_2026.csv", parse_dates=["Date"])
gold = gold.set_index("Date")["Price"].sort_index()
fx = pd.read_csv(f"{V}/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"])
fx = fx.set_index("Date")["INR_per_USD"].sort_index()
# gold in INR (T3's convention), all three on month-end index
gold.index = gold.index + pd.offsets.MonthEnd(0)
fx.index = fx.index + pd.offsets.MonthEnd(0)
gold_inr = (gold * fx.reindex(gold.index)).dropna()

px = pd.DataFrame({"eq": nif_m, "gld": gold_inr}).dropna()
r = px.pct_change().dropna()
print(f"\n=== G1 rebalance grid === blend window {r.index[0].date()}..{r.index[-1].date()} (n={len(r)} months)")


def run_blend(r, rule, target=0.5):
    """rule: ('cal', k months) or ('band', pp) or ('never', None). Returns net/gross series."""
    kind, param = rule
    w_eq = target
    out_g, out_n, turn = [], [], []
    for i, (dt, row) in enumerate(r.iterrows()):
        # accrue the month on current weights
        g = w_eq * row["eq"] + (1 - w_eq) * row["gld"]
        w_eq_end = (w_eq * (1 + row["eq"])) / (1 + g)
        # decide rebalance AFTER the month's return (trade at month end)
        do = False
        if kind == "cal" and ((i + 1) % param == 0):
            do = True
        elif kind == "band" and abs(w_eq_end - target) >= param:
            do = True
        traded = 0.0
        if do:
            traded = abs(w_eq_end - target)  # |dw| on one leg == notional turned over
            w_eq_end = target
        cost = traded * RT_BPS / 1e4
        out_g.append(g)
        out_n.append(g - cost)
        turn.append(traded)
        w_eq = w_eq_end
    idx = r.index
    return (pd.Series(out_g, idx), pd.Series(out_n, idx), pd.Series(turn, idx))


RULES = [("monthly", ("cal", 1)), ("quarterly", ("cal", 3)), ("semi-annual", ("cal", 6)),
         ("annual", ("cal", 12)), ("never", ("never", None)),
         ("band +-3pp", ("band", 0.03)), ("band +-5pp", ("band", 0.05)),
         ("band +-10pp", ("band", 0.10))]
g1 = {}
for name, rule in RULES:
    gs, ns, tn = run_blend(r, rule)
    cg, vg, ddg = ann_stats(gs)
    cn, vn, ddn = ann_stats(ns)
    g1[name] = dict(gross=cg, net=cn, vol=vg, dd=ddg, turn=tn.sum() / (len(r) / 12) * 100,
                    events=int((tn > 0).sum()))
    print(f"  {name:14s} gross {cg:6.2f}% net {cn:6.2f}% vol {vg:5.2f}% maxDD {ddg:7.2f}% "
          f"turnover {g1[name]['turn']:5.2f}%/yr events {g1[name]['events']:3d} "
          f"CAGR/vol {cg/vg:.3f}")
nets = {k: v["net"] for k, v in g1.items()}
best, worst = max(nets, key=nets.get), min(nets, key=nets.get)
cvs = [v["gross"] / v["vol"] for v in g1.values()]
print(f"  G1 SPREAD: best={best} {nets[best]:.2f}% worst={worst} {nets[worst]:.2f}% "
      f"=> net spread {nets[best]-nets[worst]:.3f}pp/yr | gross CAGR/vol spread {max(cvs)-min(cvs):.3f}")

# ============================ panel prep ============================
pan = pd.read_csv(f"{V}/panel/n500_adjclose_2012_2022.csv.gz", parse_dates=["Date"])
pan = pan.set_index("Date").sort_index()
pm = pan.resample("ME").last().pct_change()
pm = pm.loc[:, pm.notna().sum() >= 60]
print(f"\n[panel] {pm.shape[1]} names with >=60 monthly obs, {pm.index[0].date()}..{pm.index[-1].date()}")

# ============================ G2: concentration curve ============================
print("\n=== G2 concentration curve === (200 draws/N, seed fixed, EW monthly rebal)")
rng = np.random.default_rng(SEED)
cols = pm.columns.to_numpy()
g2 = {}
for N in [5, 10, 15, 20, 30, 50, 100, 200, len(cols)]:
    cg_l, vol_l, tw_l = [], [], []
    draws = 1 if N == len(cols) else 200
    for _ in range(draws):
        sel = cols if N == len(cols) else rng.choice(cols, size=N, replace=False)
        pr = pm[sel].mean(axis=1, skipna=True).dropna()
        c, v, _ = ann_stats(pr)
        cg_l.append(c); vol_l.append(v); tw_l.append((1 + pr).prod())
    lab = "all" if N == len(cols) else str(N)
    g2[lab] = dict(cagr=np.median(cg_l), vol=np.median(vol_l),
                   cv=np.median(cg_l) / np.median(vol_l), p10=np.percentile(tw_l, 10))
    print(f"  N={lab:4s} median CAGR {g2[lab]['cagr']:6.2f}% vol {g2[lab]['vol']:5.2f}% "
          f"CAGR/vol {g2[lab]['cv']:.3f} p10 terminal wealth {g2[lab]['p10']:.3f}x")
imp = (g2["50"]["p10"] / g2["20"]["p10"] - 1) * 100
print(f"  G2 BAR: p10 terminal wealth N=20 -> N=50 = {imp:+.2f}% (bar >= +10% for the tail argument)")

# ============================ G3 / G4 shared: 6-2 momentum ============================
lg = np.log1p(pm)
form62 = lg.rolling(5).sum().shift(2)          # 6-2: 6m formation, 1m skip (MOM-D1 verbatim)
vol12 = pm.rolling(12).std()


def decile_spread(sig, fwd, n=10):
    """EW mean fwd return of top decile minus bottom decile, per date; returns a Series."""
    out = {}
    for dt in sig.index:
        s, f = sig.loc[dt], fwd.loc[dt] if dt in fwd.index else None
        if f is None:
            continue
        m = s.notna() & f.notna()
        if m.sum() < 50:
            continue
        sr, fr = s[m], f[m]
        q = np.ceil(sr.rank(pct=True) * n).clip(1, n)
        out[dt] = fr[q == n].mean() - fr[q == 1].mean()
    return pd.Series(out)


fwd1 = pm.shift(-1)
fwd12 = (np.exp(lg.rolling(12).sum().shift(-12)) - 1)
mom_sp1 = decile_spread(form62, fwd1) * 1200          # ann %
mom_sp12 = decile_spread(form62, fwd12) * 100
lv_sp1 = decile_spread(-vol12, fwd1) * 1200
lv_sp12 = decile_spread(-vol12, fwd12) * 100

disp = pm.std(axis=1)                                  # cross-sectional dispersion
rvol = pm.mean(axis=1).rolling(12).std() * np.sqrt(12)  # panel realized vol (12m)
# expanding terciles, min 36m, lagged 1m -> real-time
dt_state = {}
for i, dt in enumerate(disp.index):
    if i < 36:
        continue
    hist = disp.iloc[:i]                               # strictly prior data
    v = disp.iloc[i - 1]                               # lagged 1m
    if np.isnan(v):
        continue
    p = (hist < v).mean()
    dt_state[dt] = "LOW" if p <= 1 / 3 else ("HIGH" if p >= 2 / 3 else "MID")
state = pd.Series(dt_state)
print(f"\n=== G3 dispersion as a state === n={len(state)} months stated "
      f"(LOW {(state=='LOW').sum()} / MID {(state=='MID').sum()} / HIGH {(state=='HIGH').sum()})")
for nm, ser in [("mom 6-2 fwd-1m", mom_sp1), ("mom 6-2 fwd-12m", mom_sp12),
                ("low-vol fwd-1m", lv_sp1), ("low-vol fwd-12m", lv_sp12)]:
    al = ser.reindex(state.index).dropna()
    st = state.reindex(al.index)
    vals = {k: al[st == k].mean() for k in ["LOW", "MID", "HIGH"]}
    gap = vals["HIGH"] - vals["LOW"]
    print(f"  {nm:18s} LOW {vals['LOW']:7.2f} MID {vals['MID']:7.2f} HIGH {vals['HIGH']:7.2f} "
          f"=> HIGH-LOW {gap:+7.2f}pp (bar >= +5 and monotone)")
both = pd.concat([disp.rename("disp"), rvol.rename("rvol")], axis=1).dropna()
print(f"  G3 REDUNDANCY CELL: corr(dispersion, panel realized vol) = {both.corr().iloc[0,1]:.3f} "
      f"(>= 0.70 fires the redundancy branch)")

# ============================ G4: after-tax holding ladder ============================
print("\n=== G4 after-tax holding-period ladder === (6-2 long leg, top decile, non-overlapping)")
rates = {"pre-Jul2024": (TAX["pre_2024_07"]["stcg_rate"]["value"], TAX["pre_2024_07"]["ltcg_rate"]["value"]),
         "post-Jul2024": (TAX["post_2024_07"]["stcg_rate"]["value"], TAX["post_2024_07"]["ltcg_rate"]["value"])}
g4 = {}
for H in [1, 3, 6, 12, 13]:
    per = []
    dates = form62.index
    i = 36
    while i + H < len(dates):
        dt = dates[i]
        s = form62.loc[dt]
        m = s.notna()
        if m.sum() >= 50:
            sr = s[m]
            q = np.ceil(sr.rank(pct=True) * 10).clip(1, 10)
            top = sr.index[q == 10]
            seg = pm.loc[dates[i + 1]:dates[i + H], top]
            hp = (1 + seg).prod(axis=0, skipna=True)
            hp = hp[hp.notna()]
            if len(hp):
                per.append(hp.mean() - 1)
        i += H
    per = np.array(per)
    gross_ann = (1 + per.mean()) ** (12 / H) - 1
    row = {"n": len(per), "gross": gross_ann * 100, "per": per.mean() * 100}
    for lbl, (stcg, ltcg) in rates.items():
        rate = stcg if H < H_THRESH else ltcg
        row[lbl] = ((1 + per.mean() * (1 - rate)) ** (12 / H) - 1) * 100
        row[lbl + "_rate"] = rate
    if H == H_THRESH:   # on the boundary: show BOTH treatments
        for lbl, (stcg, ltcg) in rates.items():
            row[lbl + "_asSTCG"] = ((1 + per.mean() * (1 - stcg)) ** (12 / H) - 1) * 100
    g4[H] = row
    extra = ""
    if H == H_THRESH:
        extra = (f" | ON-BOUNDARY as-STCG: pre {row['pre-Jul2024_asSTCG']:.2f}% "
                 f"post {row['post-Jul2024_asSTCG']:.2f}%")
    print(f"  H={H:2d}m n={row['n']:3d} per-period {row['per']:6.2f}% gross-ann {row['gross']:6.2f}% "
          f"| after-tax pre-Jul2024 {row['pre-Jul2024']:6.2f}% (rate {row['pre-Jul2024_rate']:.3f}) "
          f"post-Jul2024 {row['post-Jul2024']:6.2f}% (rate {row['post-Jul2024_rate']:.3f}){extra}")
for lbl in rates:
    v13, v1 = g4[13][lbl], g4[1][lbl]
    print(f"  G4 BAR [{lbl}]: 13m {v13:.2f}% vs 1m {v1:.2f}% => "
          f"{'13m WINS - the LTCG line reshapes the design' if v13 > v1 else '1m still wins - tax line is second-order'}"
          f" (gap {v13-v1:+.2f}pp/yr)")
    need = (1 + v13 / 100) ** (1 / 12) - 1
    stcg = rates[lbl][0]
    print(f"    break-even: a 1m-hold strategy needs {need/(1-stcg)*100:.3f}%/month gross "
          f"to match the 13m hold after tax (actual 1m gross was {g4[1]['per']:.3f}%/month)")
