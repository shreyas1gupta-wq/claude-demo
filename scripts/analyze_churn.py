"""CH-D1..CH-D5 — the churn battery. Registered 2026-09-11 BEFORE this run
(ledger entry of record: "Entry CH-D1..CH-D5"). Prints only; interpretation
hand-appended after the print.

Cost comes from quant/costs/statutory (registry-driven) and tax rates from
config/costs.yaml capital_gains_tax_india — no rate constant is typed here
(process note #6). Formation and universe conventions are quoted verbatim from
MOM-D1/G4 (6-2) and the VAL runner (dec() n=5 per date, x1200/x100/QG-D3).
"""
import json

import numpy as np
import pandas as pd

from quant.costs.statutory import round_trip_bps
from quant.registry.loader import load_registry

V = "/home/user/claude-demo/ingest/vault"
OUT = {}

reg = load_registry()
RT_BPS = round_trip_bps(reg, "cash_delivery")
TAX = reg["costs"]["capital_gains_tax_india"]
H_THRESH = TAX["holding_threshold_months"]["value"]
RATES = {"pre-Jul2024": (TAX["pre_2024_07"]["stcg_rate"]["value"], TAX["pre_2024_07"]["ltcg_rate"]["value"]),
         "post-Jul2024": (TAX["post_2024_07"]["stcg_rate"]["value"], TAX["post_2024_07"]["ltcg_rate"]["value"])}
print(f"[registry] cash_delivery round-trip {RT_BPS:.2f}bps | LTCG threshold {H_THRESH}m | "
      f"post-Jul2024 stcg/ltcg {RATES['post-Jul2024'][0]:.3f}/{RATES['post-Jul2024'][1]:.3f}")


def ann_stats(mret):
    """CAGR, ann vol, maxDD from a monthly simple-return series (G1 helper, verbatim)."""
    w = (1 + mret).cumprod()
    yrs = len(mret) / 12
    return (w.iloc[-1] ** (1 / yrs) - 1) * 100, mret.std() * np.sqrt(12) * 100, ((w / w.cummax() - 1).min()) * 100


# ======================= India panel prep (MOM-D1/G4 conventions) =======================
pan = pd.read_csv(f"{V}/panel/n500_adjclose_2012_2022.csv.gz", parse_dates=["Date"]).set_index("Date").sort_index()
vt = pd.read_csv(f"{V}/panel/n500_value_traded_2012_2022.csv.gz", parse_dates=["Date"]).set_index("Date").sort_index()
pm = pan.resample("ME").last().pct_change()
pm = pm.loc[:, pm.notna().sum() >= 60]
lg = np.log1p(pm)
form62 = lg.rolling(5).sum().shift(2)      # 6-2: 6-month formation, 1-month skip (MOM-D1 verbatim)
print(f"[panel] {pm.shape[1]} names >=60 monthly obs, {pm.index[0].date()}..{pm.index[-1].date()}")

# prior-calendar-year median daily value traded -> liquidity tercile (MOM-D1's convention)
vt_yr = vt.resample("YE").median()
vt_yr.index = vt_yr.index.year
liq_t = {}
for dt in pm.index:
    py = dt.year - 1
    if py in vt_yr.index:
        s = vt_yr.loc[py].dropna()
        if len(s) >= 30:
            liq_t[dt] = np.ceil(s.rank(pct=True) * 3).clip(1, 3)
print(f"[panel] liquidity terciles available for {len(liq_t)} months")


# ============================ CH-D1: rank buffer (hysteresis) ============================
print(f"\n=== CH-D1 rank-buffer (hysteresis) on the 6-2 India momentum sleeve ===")
print(f"    enter at pct-rank >= 0.90, exit below (0.90 - b); EW long; net of {RT_BPS:.2f}bps round-trip")
ch1 = {}
dates = form62.index
start = 36
for b in [0.00, 0.05, 0.10, 0.20, 0.30]:
    held = set()
    rets, turns = [], []
    for i in range(start, len(dates) - 1):
        s = form62.loc[dates[i]].dropna()
        if len(s) < 50:
            continue
        pr = s.rank(pct=True)
        keep = {n for n in held if n in pr.index and pr[n] >= 0.90 - b}
        new = set(pr.index[pr >= 0.90])
        tgt = keep | new
        if not tgt:
            continue
        # one-way turnover = fraction of the (equal-weighted) book replaced
        prev_n, tgt_n = len(held), len(tgt)
        if prev_n == 0:
            ow = 1.0
        else:
            # EW weights before/after; L1 distance / 2 = one-way turnover
            allnames = held | tgt
            ow = sum(abs((1 / tgt_n if n in tgt else 0.0) - (1 / prev_n if n in held else 0.0))
                     for n in allnames) / 2
        nxt = pm.loc[dates[i + 1], list(tgt)]
        nxt = nxt[nxt.notna()]
        if not len(nxt):
            continue
        rets.append(nxt.mean())
        turns.append(ow)
        held = tgt
    r = pd.Series(rets, index=dates[start:start + len(rets)])
    t = np.array(turns)
    cagr, vol, dd = ann_stats(r)
    ow_m = t.mean()
    cost_m = 2 * ow_m * RT_BPS / 1e4            # two-way traded notional x round-trip
    # gross and net on the SAME arithmetic-compounded basis so their difference is cost alone
    gross = ((1 + r.mean()) ** 12 - 1) * 100
    net = ((1 + r.mean() - cost_m) ** 12 - 1) * 100
    stcg = RATES["post-Jul2024"][0]
    net_tax = ((1 + (r.mean() - cost_m) * (1 - stcg)) ** 12 - 1) * 100
    ch1[b] = {"gross": gross, "cagr": cagr, "vol": vol, "dd": dd, "ow_month": ow_m * 100,
              "ow_year": ow_m * 1200, "net": net, "net_tax": net_tax, "cost_ann": gross - net,
              "n_names": len(held), "n": len(r)}
    print(f"  b={b:.2f}  gross {gross:6.2f}%  net {net:6.2f}%  net-after-STCG {net_tax:6.2f}%  "
          f"| cost drag {gross-net:5.2f}pp  one-way {ow_m*100:5.2f}%/mo ({ow_m*1200:6.1f}%/yr)  "
          f"| CAGR {cagr:6.2f}  vol {vol:5.2f}  maxDD {dd:7.2f}  (book {len(held)} names, n={len(r)})")
base = ch1[0.00]["net"]
best_b = max((b for b in ch1 if b > 0), key=lambda b: ch1[b]["net"])
print(f"  CH-D1 BAR (a): best buffered net {ch1[best_b]['net']:.2f}% at b={best_b:.2f} vs unbuffered "
      f"{base:.2f}% => gain {ch1[best_b]['net']-base:+.2f}pp/yr "
      f"{'PASS (>= +0.50)' if ch1[best_b]['net']-base >= 0.50 else 'FAIL (< +0.50) - buffering cosmetic'}")
ows = [ch1[b]["ow_month"] for b in sorted(ch1)]
print(f"  CH-D1 PRIOR (b) turnover monotone in b: {' > '.join(f'{o:.2f}' for o in ows)} "
      f"=> {'HIT' if all(x > y for x, y in zip(ows, ows[1:])) else 'MISS'}")
gd = ch1[0.00]["gross"] - ch1[0.30]["gross"]
print(f"  CH-D1 PRIOR (c) gross decay b=0->0.30 = {gd:+.2f}pp/yr "
      f"=> {'HIT (< 3.0)' if abs(gd) < 3.0 else 'MISS (>= 3.0)'}")
OUT["CH-D1"] = ch1

# ============================ CH-D2: overlapping re-formation ============================
print("\n=== CH-D2 overlapping re-formation frequency (Jegadeesh-Titman tranches) ===")
ch2 = {}
for k in [1, 2, 3, 6, 12]:
    tranches = []          # list of (expiry_index, [names])
    rets, turns, w_prev = [], [], {}
    for i in range(start, len(dates) - 1):
        s = form62.loc[dates[i]].dropna()
        if len(s) < 50:
            continue
        q = np.ceil(s.rank(pct=True) * 10).clip(1, 10)
        top = list(s.index[q == 10])
        tranches = [(e, n) for (e, n) in tranches if e > i]
        tranches.append((i + k, top))
        tranches = tranches[-k:]
        w = {}
        for _, names in tranches:
            for n in names:
                w[n] = w.get(n, 0.0) + 1.0 / (len(names) * len(tranches))
        nxt = pm.loc[dates[i + 1], list(w)]
        nxt = nxt[nxt.notna()]
        if not len(nxt):
            continue
        wt = pd.Series({n: w[n] for n in nxt.index})
        rets.append(float((nxt * wt).sum() / wt.sum()))
        # ACTUAL one-way turnover = L1 weight change / 2 (the CH-D1 measure, not a 1/k proxy:
        # consecutive tranches overlap, so 1/k overstates trading and would flatter large k)
        allk = set(w) | set(w_prev)
        turns.append(sum(abs(w.get(n, 0.0) - w_prev.get(n, 0.0)) for n in allk) / 2)
        w_prev = w
    r = pd.Series(rets, index=dates[start:start + len(rets)])
    cagr, vol, dd = ann_stats(r)
    ow_m = np.mean(turns)
    cost_m = 2 * ow_m * RT_BPS / 1e4
    gross = ((1 + r.mean()) ** 12 - 1) * 100          # same basis as net (cost is the only difference)
    net = ((1 + r.mean() - cost_m) ** 12 - 1) * 100
    row = {"n": len(r), "gross": gross, "cagr": cagr, "vol": vol, "dd": dd,
           "ow_month": ow_m * 100, "ow_year": ow_m * 1200, "net": net, "cost_ann": gross - net}
    for lbl, (stcg, ltcg) in RATES.items():
        rate = ltcg if k >= H_THRESH else stcg
        row[lbl] = ((1 + (r.mean() - cost_m) * (1 - rate)) ** 12 - 1) * 100
        row[lbl + "_rate"] = rate
    ch2[k] = row
    print(f"  k={k:2d}m n={len(r):3d}  gross {gross:6.2f}%  net {net:6.2f}%  | cost drag {gross-net:5.2f}pp  "
          f"one-way {ow_m*100:5.1f}%/mo  | CAGR {cagr:6.2f}  vol {vol:5.2f}  maxDD {dd:7.2f}  "
          f"after-tax pre {row['pre-Jul2024']:6.2f}% / post {row['post-Jul2024']:6.2f}% (rate {row['post-Jul2024_rate']:.3f})")
hump = ch2[3]["gross"] >= ch2[1]["gross"] and ch2[3]["gross"] >= ch2[6]["gross"]
print(f"  CH-D2 BAR (a) G4's 3-month gross hump reproduces on n in the hundreds: "
      f"k1 {ch2[1]['gross']:.2f} / k3 {ch2[3]['gross']:.2f} / k6 {ch2[6]['gross']:.2f} => "
      f"{'CONFIRMED' if hump else 'NOT CONFIRMED - G4 hump was small-sample'}")
for lbl in RATES:
    g = ch2[3][lbl] - ch2[1][lbl]
    print(f"  CH-D2 BAR (b) [{lbl}] k=3 net-after-tax {ch2[3][lbl]:.2f}% vs k=1 {ch2[1][lbl]:.2f}% => {g:+.2f}pp/yr "
          f"{'PASS (>= +0.50)' if g >= 0.50 else 'FAIL (< +0.50)'}")
print("  CH-D2 PRIOR (c) turnover ~ 1/k: " + " ".join(f"k{k}={ch2[k]['ow_month']:.1f}%" for k in sorted(ch2)))
OUT["CH-D2"] = ch2

# ============================ CH-D3: partial adjustment ============================
nif = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).sort_values("Date")
nif_m = nif.set_index("Date")["Adj Close"].resample("ME").last()
gold = pd.read_csv(f"{V}/commodities/gold_monthly_1833_2026.csv", parse_dates=["Date"]).set_index("Date")["Price"].sort_index()
fx = pd.read_csv(f"{V}/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"]).set_index("Date")["INR_per_USD"].sort_index()
gold.index = gold.index + pd.offsets.MonthEnd(0)
fx.index = fx.index + pd.offsets.MonthEnd(0)
gold_inr = (gold * fx.reindex(gold.index)).dropna()
rb = pd.DataFrame({"eq": nif_m, "gld": gold_inr}).dropna().pct_change().dropna()
print(f"\n=== CH-D3 partial adjustment (lambda toward the 50/50 target) === "
      f"{rb.index[0].date()}..{rb.index[-1].date()} n={len(rb)}")
ch3 = {}
for lam in [0.00, 0.25, 0.50, 0.75, 1.00]:
    w_eq, gs, ns, turn = 0.5, [], [], []
    for _, row in rb.iterrows():
        g = w_eq * row["eq"] + (1 - w_eq) * row["gld"]
        w_end = (w_eq * (1 + row["eq"])) / (1 + g)
        traded = lam * abs(w_end - 0.5)
        w_eq = w_end - lam * (w_end - 0.5)
        gs.append(g)
        ns.append(g - 2 * traded * RT_BPS / 1e4)
        turn.append(traded)
    gr = pd.Series(gs, index=rb.index)
    nr = pd.Series(ns, index=rb.index)
    gc, gv, gdd = ann_stats(gr)
    nc, nv, ndd = ann_stats(nr)
    ch3[lam] = {"gross_cagr": gc, "net_cagr": nc, "vol": nv, "dd": ndd,
                "ow_year": float(np.mean(turn)) * 1200, "cagr_vol": nc / nv}
    print(f"  lambda={lam:.2f}  net CAGR {nc:6.2f}%  vol {nv:5.2f}  maxDD {ndd:7.2f}  "
          f"CAGR/vol {nc/nv:5.3f}  one-way {np.mean(turn)*1200:5.2f}%/yr")
best_net = max(ch3[l]["net_cagr"] for l in ch3)
dd0 = ch3[0.00]["dd"]
qual = [l for l in ch3 if 0 < l < 1 and best_net - ch3[l]["net_cagr"] <= 0.20 and ch3[l]["dd"] >= dd0]
print(f"  CH-D3 BAR (a) interior lambda within 0.20pp of best net ({best_net:.2f}%) AND maxDD no deeper "
      f"than lambda=0 ({dd0:.2f}%): {qual if qual else 'NONE'} => {'PASS' if qual else 'FAIL'}")
dds = [ch3[l]["dd"] for l in sorted(ch3)]
print(f"  CH-D3 PRIOR (b) maxDD monotone deeper in lambda: {' '.join(f'{d:.2f}' for d in dds)} => "
      f"{'HIT' if all(x > y for x, y in zip(dds, dds[1:])) else 'MISS'}")
ts = [ch3[l]["ow_year"] for l in sorted(ch3)]
print(f"  CH-D3 PRIOR (c) turnover rising in lambda: {' '.join(f'{t:.2f}' for t in ts)} => "
      f"{'HIT' if all(x < y for x, y in zip(ts, ts[1:])) else 'MISS'}")
OUT["CH-D3"] = ch3

# ============================ CH-D4: turnover as a signal (US panel) ============================
use = ["stock_id", "date", "Share_Turn_3M", "Share_Turn_6M", "Share_Turn_12M",
       "Mom_11M_Usd", "Mkt_Cap_12M_Usd", "R1M_Usd", "R12M_Usd"]
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", usecols=use, parse_dates=["date"])
rr = fp.pivot_table(index="date", columns="stock_id", values="R1M_Usd")
lgu = np.log1p(rr)
f36 = ((np.exp(lgu.rolling(36, min_periods=27).sum().shift(-35) * (12 / 36)) - 1) * 100).stack().rename("f36")
fp = fp.set_index(["date", "stock_id"]).join(f36).reset_index()


def dec(s, n=5):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


fp["sz"] = fp.groupby("date").Mkt_Cap_12M_Usd.transform(dec)
print("\n=== CH-D4 share-turnover ladder (US firm_panel, REHEARSAL; LOW-minus-HIGH turnover) ===")
ch4 = {}
for col in ["Share_Turn_3M", "Share_Turn_6M", "Share_Turn_12M"]:
    fp["q"] = fp.groupby("date")[col].transform(dec)
    s1 = (fp[fp.q == 1].R1M_Usd.mean() - fp[fp.q == 5].R1M_Usd.mean()) * 1200
    s12 = (fp[fp.q == 1].R12M_Usd.mean() - fp[fp.q == 5].R12M_Usd.mean()) * 100
    s36 = fp[fp.q == 1].f36.mean() - fp[fp.q == 5].f36.mean()
    big = fp[fp.sz == 5].copy()
    big["q"] = big.groupby("date")[col].transform(dec)
    b12 = (big[big.q == 1].R12M_Usd.mean() - big[big.q == 5].R12M_Usd.mean()) * 100
    ch4[col] = {"f1m": s1, "f12m": s12, "f36m": s36, "szQ5_12m": b12}
    print(f"  {col:>15}: 1m {s1:+6.2f} | 12m {s12:+6.2f} | 36m {s36:+6.2f} | szQ5 12m {b12:+6.2f}")
bars = {c: ch4[c]["szQ5_12m"] for c in ch4}
print(f"  CH-D4 BAR (a) any lookback szQ5 12m >= +2.00: max {max(bars.values()):+.2f} "
      f"({max(bars, key=bars.get)}) => {'PASS' if max(bars.values()) >= 2.00 else 'FAIL'}")
print(f"  CH-D4 PRIOR (b) positive at every lookback: "
      f"{'HIT' if all(v > 0 for v in bars.values()) else 'MISS'}; 12M >= 3M: "
      f"{'HIT' if ch4['Share_Turn_12M']['szQ5_12m'] >= ch4['Share_Turn_3M']['szQ5_12m'] else 'MISS'}")
fp["mq"] = fp.groupby("date").Mom_11M_Usd.transform(dec)
win = fp[fp.mq == 5].copy()
win["q"] = win.groupby("date").Share_Turn_12M.transform(dec)
inter = (win[win.q == 1].R12M_Usd.mean() - win[win.q == 5].R12M_Usd.mean()) * 100
ch4["interaction_quiet_winners_12m"] = inter
print(f"  CH-D4 (c) Lee-Swaminathan: within Mom_11M Q5, LOW-minus-HIGH turnover fwd-12m {inter:+.2f}pp "
      f"=> {'HIT (>= +2.00)' if inter >= 2.00 else 'MISS (< +2.00)'}")
OUT["CH-D4"] = ch4

# ============================ CH-D5: India volume shock ============================
print("\n=== CH-D5 within-stock VOLUME SHOCK, India panel (no share count exists -> own-history measure) ===")
lv = np.log(vt.where(vt > 0))
short = lv.rolling(21, min_periods=15).median()
long_ = lv.rolling(252, min_periods=180).median()
vs_d = (short - long_)
vs = vs_d.resample("ME").last()
vs = vs.reindex(pm.index).loc[:, [c for c in vs.columns if c in pm.columns]]
f12 = np.exp(lg.rolling(12).sum().shift(-12)) - 1     # fwd-12m simple, aligned to decision month
f3 = np.exp(lg.rolling(3).sum().shift(-3)) - 1
f1 = pm.shift(-1)
print(f"[CH-D5] volume-shock panel {vs.notna().sum().sum():,} stock-months, "
      f"{vs.index[0].date()}..{vs.index[-1].date()}")
ch5 = {}
for lbl, fwd, scale in [("f1m", f1, 1200), ("f3m", f3, 400 / 1), ("f12m", f12, 100)]:
    lo, hi = [], []
    for dt in vs.index[start:]:
        s = vs.loc[dt].dropna()
        if len(s) < 50:
            continue
        t = np.ceil(s.rank(pct=True) * 3).clip(1, 3)
        fr = fwd.loc[dt] if dt in fwd.index else None
        if fr is None:
            continue
        a = fr[t[t == 1].index].dropna()
        b_ = fr[t[t == 3].index].dropna()
        if len(a) and len(b_):
            lo.append(a.mean())
            hi.append(b_.mean())
    sp = (np.mean(lo) - np.mean(hi)) * (scale if lbl != "f3m" else 400)
    ch5[lbl] = {"low": np.mean(lo) * (scale if lbl != "f3m" else 400),
                "high": np.mean(hi) * (scale if lbl != "f3m" else 400), "spread": sp, "n_months": len(lo)}
    print(f"  {lbl:>5}: LOW-shock {ch5[lbl]['low']:+7.2f}%/yr  HIGH-shock {ch5[lbl]['high']:+7.2f}%/yr  "
          f"spread {sp:+6.2f}pp/yr (n={len(lo)} months)")
# liquid-tercile sub-read at 12m
lo, hi = [], []
for dt in vs.index[start:]:
    if dt not in liq_t:
        continue
    lt = liq_t[dt]
    names = [c for c in vs.columns if c in lt.index and lt[c] == 3]
    s = vs.loc[dt, names].dropna()
    if len(s) < 30 or dt not in f12.index:
        continue
    t = np.ceil(s.rank(pct=True) * 3).clip(1, 3)
    a = f12.loc[dt, t[t == 1].index].dropna()
    b_ = f12.loc[dt, t[t == 3].index].dropna()
    if len(a) and len(b_):
        lo.append(a.mean())
        hi.append(b_.mean())
liq_sp = (np.mean(lo) - np.mean(hi)) * 100
ch5["f12m_liquid"] = {"low": np.mean(lo) * 100, "high": np.mean(hi) * 100, "spread": liq_sp, "n_months": len(lo)}
print(f"  f12m LIQUID tercile: LOW {np.mean(lo)*100:+7.2f}  HIGH {np.mean(hi)*100:+7.2f}  "
      f"spread {liq_sp:+6.2f}pp/yr (n={len(lo)})")
# momentum interaction: within 6-2 top decile, low-shock minus high-shock at 12m
lo, hi = [], []
for dt in vs.index[start:]:
    s62 = form62.loc[dt].dropna() if dt in form62.index else None
    if s62 is None or len(s62) < 50 or dt not in f12.index:
        continue
    q = np.ceil(s62.rank(pct=True) * 10).clip(1, 10)
    top = [n for n in s62.index[q == 10] if n in vs.columns]
    s = vs.loc[dt, top].dropna()
    if len(s) < 15:
        continue
    med = s.median()
    a = f12.loc[dt, s[s <= med].index].dropna()
    b_ = f12.loc[dt, s[s > med].index].dropna()
    if len(a) and len(b_):
        lo.append(a.mean())
        hi.append(b_.mean())
qw = (np.mean(lo) - np.mean(hi)) * 100
ch5["quiet_winners_12m"] = {"low": np.mean(lo) * 100, "high": np.mean(hi) * 100, "spread": qw, "n_months": len(lo)}
print(f"  quiet-winners (within 6-2 top decile, low-shock minus high-shock, 12m): {qw:+6.2f}pp/yr (n={len(lo)})")
# redundancy check: pooled corr of VS rank vs 6-2 rank
cs = []
for dt in vs.index[start:]:
    if dt not in form62.index:
        continue
    a = vs.loc[dt].dropna()
    b_ = form62.loc[dt].dropna()
    com = a.index.intersection(b_.index)
    if len(com) >= 50:
        cs.append(a[com].rank().corr(b_[com].rank()))
rho = float(np.mean(cs))
ch5["redundancy_corr"] = rho
print(f"  CH-D5 redundancy: mean per-date rank corr(VS, 6-2) = {rho:+.3f} => "
      f"{'FIRES - demote (|corr| >= 0.50)' if abs(rho) >= 0.50 else 'does NOT fire (|corr| < 0.50)'}")
s12 = ch5["f12m"]["spread"]
sign_ok = np.sign(s12) == np.sign(liq_sp)
print(f"  CH-D5 BAR (a) |12m spread| >= 4.00 AND sign agrees in liquid tercile: "
      f"|{s12:.2f}| and liquid {liq_sp:+.2f} => "
      f"{'PASS' if abs(s12) >= 4.00 and sign_ok else 'FAIL'}")
flip = np.sign(s12) > 0 and np.sign(ch5["f1m"]["spread"]) <= 0
print(f"  CH-D5 PRIOR (b) sign FLIP across horizon (positive 12m, negative/null 1m): "
      f"1m {ch5['f1m']['spread']:+.2f} / 12m {s12:+.2f} => {'HIT' if flip else 'MISS'}")
OUT["CH-D5"] = ch5

with open("/home/user/claude-demo/research/churn.json", "w") as f:
    json.dump(OUT, f, indent=1, default=float)
print("\nwrote research/churn.json")
