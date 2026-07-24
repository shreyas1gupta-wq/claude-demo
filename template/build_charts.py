#!/usr/bin/env python3
"""Ionic-palette chart library for the AZBY template deck. Renders every chart as
a transparent PNG into template/assets/charts/. Flat, frameless, semantic-colour
style matching the Ionic Wealth house look. Reads template/azby_data.json."""
import json, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, PathPatch, Rectangle
from matplotlib.path import Path as MPath
import squarify

HERE = Path(__file__).resolve().parent
D = json.loads((HERE / "azby_data.json").read_text())
OUT = HERE / "assets" / "charts"; OUT.mkdir(parents=True, exist_ok=True)
P = {k: "#" + v for k, v in D["palette"].items()}

plt.rcParams.update({
    "font.family": "Carlito", "font.size": 15, "text.color": P["navy"],
    "axes.edgecolor": P["grid"], "axes.labelcolor": P["navy"],
    "xtick.color": P["slate"], "ytick.color": P["slate"],
    "axes.linewidth": 1.0, "figure.dpi": 200, "savefig.dpi": 200,
    "svg.fonttype": "none",
})

def bare(ax, keep=()):
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(s in keep)
    ax.tick_params(length=0)

def save(fig, name, pad=0.12):
    fig.savefig(OUT / f"{name}.png", transparent=True, bbox_inches="tight", pad_inches=pad)
    plt.close(fig); print("  ·", name)

def lighten(hex_, f):
    hex_ = hex_.lstrip("#"); r, g, b = (int(hex_[i:i+2], 16) for i in (0, 2, 4))
    r, g, b = (int(c + (255 - c) * f) for c in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"

ROSE = lighten(P["red"], 0.55)          # dusty rose for the sell zone
ROSE_BG = lighten(P["red"], 0.90)

# --------------------------------------------------------------------------
def donut_split():
    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    vals = [D["meta"]["equity_l"], D["meta"]["fund_l"]]
    ax.pie(vals, colors=[P["indigo"], P["indigo_t"]], startangle=90, counterclock=False,
           wedgeprops=dict(width=0.34, edgecolor="white", linewidth=2))
    ax.text(0, 0.10, f"₹{D['meta']['book_cr']} Cr", ha="center", va="center",
            fontsize=25, fontweight="bold", color=P["navy"])
    ax.text(0, -0.16, "total portfolio", ha="center", va="center", fontsize=13, color=P["slate"])
    ax.text(0, -1.28, f"Direct equity  ₹{D['meta']['equity_l']/100:.2f} Cr · {D['meta']['equity_frac']}%",
            ha="center", fontsize=13, color=P["indigo"], fontweight="bold")
    ax.text(0, -1.46, f"Mutual funds  ₹{D['meta']['fund_l']/100:.2f} Cr · {D['meta']['fund_frac']}%",
            ha="center", fontsize=13, color=P["indigo_t"], fontweight="bold")
    ax.set(aspect="equal"); save(fig, "donut_split")

def score_hist():
    fig, ax = plt.subplots(figsize=(9.6, 4.5))
    bins = D["hist"]; xs = list(range(0, 100, 10))
    ax.axvspan(0, 40, color=ROSE_BG, zorder=0)
    colors = [ROSE if x < 40 else P["indigo"] for x in xs]
    ax.bar([x + 5 for x in xs], bins, width=9, color=colors, zorder=3)
    for x, v in zip(xs, bins):
        if v: ax.text(x + 5, v + 0.4, str(v), ha="center", fontsize=13,
                      color=P["navy"], fontweight="bold")
    ax.axvline(40, color=P["amber"], lw=3, zorder=4)
    ax.text(41, max(bins) * 0.96, "Sell below 40", color=P["amber"], fontsize=13,
            fontweight="bold", va="top")
    ax.set_xlim(0, 100); ax.set_ylim(0, max(bins) * 1.18)
    ax.set_xticks(range(0, 101, 10)); ax.set_yticks([])
    ax.set_xlabel("Ionic Score  (0–100)"); bare(ax, keep=("bottom",))
    save(fig, "score_hist")

def concentration_bubble():
    fig, ax = plt.subplots(figsize=(9.4, 5.0))
    st = D["stocks"]
    for s in st:
        if s["score"] is None: continue
        c = P["red"] if s["call"] == "Sell" else P["green"]
        ax.scatter(s["score"], s["value_l"] / D["meta"]["equity_l"] * 100,
                   s=max(30, s["value_l"] * 22), color=c, alpha=0.72,
                   edgecolor="white", linewidth=0.8, zorder=3)
    ax.axvline(40, color=P["amber"], lw=2.5, zorder=2)
    ax.axhline(8, color=P["slate"], lw=1.2, ls=(0, (5, 4)), zorder=2)
    ax.text(40.6, ax.get_ylim()[1] * 0.97, "Sell < 40", color=P["amber"],
            fontsize=12, fontweight="bold", va="top")
    ax.text(99, 8.3, "single-name guideline  8% of equity", color=P["slate"],
            fontsize=11, ha="right")
    for nm, sc, w in [("Titan", D["spot_hold"]["score"], D["spot_hold"]["value_l"]),
                      ("Reliance", D["spot_sell"]["score"], D["spot_sell"]["value_l"])]:
        ax.annotate(nm, (sc, w / D["meta"]["equity_l"] * 100), fontsize=12,
                    fontweight="bold", color=P["navy"], xytext=(8, 6),
                    textcoords="offset points")
    ax.set_xlim(0, 100); ax.set_xlabel("Ionic Score"); ax.set_ylabel("Weight  (% of equity sleeve)")
    ax.grid(axis="y", color=P["grid"], lw=0.8); ax.set_axisbelow(True); bare(ax, keep=("bottom", "left"))
    save(fig, "concentration_bubble")

def hbar(name, items, guideline=None, gl_label=None, unit="%", fudge=1.18, size=(8.6, 5.2)):
    fig, ax = plt.subplots(figsize=size)
    labels = [k for k, _ in items][::-1]; vals = [v for _, v in items][::-1]
    y = range(len(labels))
    bars = ax.barh(list(y), vals, color=P["indigo"], height=0.64, zorder=3)
    if guideline:
        for b, v in zip(bars, vals):
            if v > guideline: b.set_color(P["amber"])
    for i, v in enumerate(vals):
        ax.text(v + max(vals) * 0.012, i, f"{v:.1f}{unit}", va="center",
                fontsize=12, color=P["navy"], fontweight="bold")
    if guideline:
        ax.axvline(guideline, color=P["red"], lw=1.6, ls=(0, (5, 4)), zorder=4)
        ax.text(guideline, len(labels) - 0.3, gl_label or f"{guideline}% limit",
                color=P["red"], fontsize=11, ha="center", va="bottom")
    ax.set_yticks(list(y)); ax.set_yticklabels(labels, fontsize=12, color=P["navy"])
    ax.set_xlim(0, max(vals) * fudge); ax.set_xticks([]); bare(ax)
    save(fig, name)

def sector_bar():
    items = list(D["sectors"].items())[:10]
    hbar("sector_bar", items, guideline=30, gl_label="30% sector guideline", size=(8.8, 5.4))

def mcap_bar():
    fig, ax = plt.subplots(figsize=(9.2, 1.9))
    order = ["Large", "Mid", "Small", "Unmapped"]
    cols = {"Large": P["indigo"], "Mid": P["indigo2"], "Small": P["indigo_t"], "Unmapped": P["grid"]}
    left = 0
    for k in order:
        v = D["caps"].get(k, 0)
        if v <= 0: continue
        ax.barh(0, v, left=left, color=cols[k], height=0.5, edgecolor="white", linewidth=1.5)
        if k == "Large":
            ax.text(left + v / 2, 0, f"{k}  {v:.1f}%", ha="center", va="center",
                    color="white", fontsize=13, fontweight="bold")
        left += v
    rest = " · ".join(f"{k} {D['caps'].get(k,0):.1f}%" for k in ("Mid", "Small", "Unmapped")
                      if D["caps"].get(k, 0) > 0)
    ax.text(100, -0.5, rest, ha="right", va="top", color=P["slate"], fontsize=10.5)
    ax.set_xlim(0, 100); ax.set_ylim(-0.8, 0.4); ax.axis("off"); save(fig, "mcap_bar", pad=0.05)

def treemap():
    fig, ax = plt.subplots(figsize=(10.2, 5.0))
    st = sorted(D["stocks"], key=lambda s: -s["value_l"])
    vals = [s["value_l"] for s in st]
    rects = squarify.normalize_sizes(vals, 100, 100)
    rects = squarify.squarify(rects, 0, 0, 100, 100)
    for s, r in zip(st, rects):
        c = P["red"] if s["call"] == "Sell" else P["green"]
        ax.add_patch(Rectangle((r["x"], r["y"]), r["dx"], r["dy"], facecolor=c,
                     edgecolor="white", linewidth=1.4, alpha=0.92))
        if r["dx"] > 9 and r["dy"] > 7:
            ax.text(r["x"] + r["dx"] / 2, r["y"] + r["dy"] / 2,
                    s["symbol"] + f"\n{s['weight']:.1f}%", ha="center", va="center",
                    color="white", fontsize=min(13, r["dx"] / 2.4), fontweight="bold")
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    ax.scatter([], [], c=P["green"], label=f"Hold · {sum(1 for s in st if s['call']=='Hold')}")
    ax.scatter([], [], c=P["red"], label=f"Sell · {sum(1 for s in st if s['call']=='Sell')}")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.08), ncol=2, frameon=False,
              fontsize=13, handletextpad=0.3)
    save(fig, "treemap")

def radar(stock, name, sell=False):
    axes_ = [("Quality", "quality"), ("Value", "value"), ("Growth 3Y", "g3"),
             ("Growth 1Y", "g1"), ("Price-trend", "st1"), ("Sector-macro", "macro")]
    vals = [stock.get(k) or 0 for _, k in axes_]
    ang = np.linspace(0, 2 * np.pi, len(axes_), endpoint=False).tolist()
    vals += vals[:1]; ang += ang[:1]
    fig, ax = plt.subplots(figsize=(4.7, 4.7), subplot_kw=dict(polar=True))
    c = P["red"] if sell else P["green"]
    ax.plot(ang, vals, color=c, lw=2.2); ax.fill(ang, vals, color=c, alpha=0.22)
    ax.plot(ang, [50] * len(ang), color=P["slate"], lw=0.8, ls=(0, (3, 3)))
    ax.set_xticks(ang[:-1]); ax.set_xticklabels([a for a, _ in axes_], fontsize=12, color=P["navy"])
    ax.set_yticks([25, 50, 75]); ax.set_yticklabels(["25", "50", "75"], fontsize=9, color=P["slate"])
    ax.set_ylim(0, 100); ax.grid(color=P["grid"], lw=0.8)
    ax.spines["polar"].set_color(P["grid"]); save(fig, name)

def factor_radar():
    axes_ = list(D["factor"].items())
    vals = [v for _, v in axes_]
    ang = np.linspace(0, 2 * np.pi, len(axes_), endpoint=False).tolist()
    vals += vals[:1]; ang += ang[:1]
    fig, ax = plt.subplots(figsize=(4.9, 4.9), subplot_kw=dict(polar=True))
    ax.plot(ang, vals, color=P["indigo"], lw=2.4); ax.fill(ang, vals, color=P["indigo"], alpha=0.20)
    ax.plot(ang, [50] * len(ang), color=P["slate"], lw=0.9, ls=(0, (3, 3)))
    ax.set_xticks(ang[:-1]); ax.set_xticklabels([a for a, _ in axes_], fontsize=12, color=P["navy"])
    ax.set_yticks([25, 50, 75]); ax.set_yticklabels(["25", "50", "75"], fontsize=9, color=P["slate"])
    ax.set_ylim(0, 100); ax.grid(color=P["grid"], lw=0.8); ax.spines["polar"].set_color(P["grid"])
    save(fig, "factor_radar")

def capture_scatter():
    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    fu = [f for f in D["funds"] if f.get("ucr")]
    for f in fu:
        good = f["dcr"] < 100 and f["roll3"] >= 60
        c = P["green"] if good else (P["amber"] if f["roll3"] >= 55 else P["red"])
        ax.scatter(f["ucr"], f["dcr"], s=max(70, f["aum_l"] * 9), color=c, alpha=0.75,
                   edgecolor="white", linewidth=1, zorder=3)
        ax.annotate(f["name"].replace(" Fund", ""), (f["ucr"], f["dcr"]), fontsize=10.5,
                    color=P["navy"], xytext=(7, 5), textcoords="offset points")
    ax.axhline(100, color=P["slate"], lw=1, ls=(0, (5, 4)))
    ax.axvline(100, color=P["slate"], lw=1, ls=(0, (5, 4)))
    ax.text(ax.get_xlim()[1], 99, "captures less downside  ↓ better", ha="right", va="top",
            color=P["green"], fontsize=11)
    ax.set_xlabel("Upside capture  (%)"); ax.set_ylabel("Downside capture  (%)")
    ax.grid(color=P["grid"], lw=0.7); ax.set_axisbelow(True); bare(ax, keep=("bottom", "left"))
    save(fig, "capture_scatter")

def rolling_consistency():
    fu = sorted([f for f in D["funds"] if f.get("roll3")], key=lambda f: f["roll3"])
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    names = [f["name"].replace(" Fund", "") for f in fu]; vals = [f["roll3"] for f in fu]
    cols = [P["green"] if v >= 60 else (P["amber"] if v >= 50 else P["red"]) for v in vals]
    ax.barh(range(len(fu)), vals, color=cols, height=0.6, zorder=3)
    for i, v in enumerate(vals):
        ax.text(v + 0.6, i, f"{v}%", va="center", fontsize=12, color=P["navy"], fontweight="bold")
    ax.axvline(60, color=P["green"], lw=1.4, ls=(0, (5, 4)))
    ax.text(60, len(fu) - 0.3, "60% = consistent", color=P["green"], fontsize=10.5, ha="center", va="bottom")
    ax.set_yticks(range(len(fu))); ax.set_yticklabels(names, fontsize=11.5, color=P["navy"])
    ax.set_xlim(0, 100); ax.set_xticks([]); bare(ax)
    ax.set_title("Rolling 3Y windows beaten  (%)", fontsize=13, color=P["navy"], loc="left", pad=10)
    save(fig, "rolling_consistency")

def hybrid_risk():
    hy = [f for f in D["funds"] if "maxdd" in f]
    hy = sorted(hy, key=lambda f: f["maxdd"])
    fig, ax = plt.subplots(figsize=(8.6, 4.4))
    names = [f["name"].replace("ICICI Pru ", "ICICI ").replace(" Advantage", " Adv") for f in hy]
    dd = [f["maxdd"] for f in hy]
    cols = [P["green"] if d > -3 else (P["indigo"] if d > -10 else P["amber"]) for d in dd]
    ax.barh(range(len(hy)), dd, color=cols, height=0.6, zorder=3)
    for i, f in enumerate(hy):
        ax.text(f["maxdd"] - 0.3, i, f"{f['maxdd']}%", va="center", ha="right",
                fontsize=11.5, color=P["navy"], fontweight="bold")
        ax.text(0.3, i, f"Sharpe {f['sharpe']} · worst 1Y {f['worst1y']:+.1f}%",
                va="center", ha="left", fontsize=10.5, color=P["slate"])
    ax.set_yticks(range(len(hy))); ax.set_yticklabels(names, fontsize=11.5, color=P["navy"])
    ax.axvline(0, color=P["grid"], lw=1); ax.set_xticks([]); bare(ax)
    ax.set_title("Maximum drawdown  (peak-to-trough, %)", fontsize=13, color=P["navy"], loc="left", pad=10)
    save(fig, "hybrid_risk")

def waterfall_deploy():
    pl = D["plan"]
    fig, ax = plt.subplots(figsize=(9.6, 5.0))
    steps = [("19 Sells", pl["sells_l"], P["indigo"]),
             ("Titan trim", pl["titan_trim_l"], P["indigo2"])]
    sleeves = [(s[0].split("(")[0].strip(), -s[1], P["green"]) for s in pl["sleeves"]]
    seq = steps + [("Cash freed", None, None)] + sleeves
    cum = 0; x = 0; xt = []
    for name, val, col in seq:
        if val is None:   # marker: deployable total
            ax.bar(x, cum, color=P["amber"], width=0.62, zorder=3, alpha=0.9)
            ax.text(x, cum + 1, f"₹{cum/100:.2f} Cr", ha="center", fontsize=11.5,
                    color=P["navy"], fontweight="bold")
            xt.append((x, "Cash\nfreed")); x += 1; continue
        bottom = cum if val > 0 else cum + val
        ax.bar(x, abs(val), bottom=bottom, color=col, width=0.62, zorder=3)
        ax.text(x, bottom + abs(val) + 0.6, f"{'+' if val>0 else ''}{val:.0f}",
                ha="center", fontsize=10.5, color=P["navy"])
        cum += val; xt.append((x, name.replace(" ", "\n"))); x += 1
    ax.set_xticks([t[0] for t in xt]); ax.set_xticklabels([t[1] for t in xt], fontsize=10.5, color=P["navy"])
    ax.set_ylabel("₹ Lakh"); ax.grid(axis="y", color=P["grid"], lw=0.7); ax.set_axisbelow(True)
    bare(ax, keep=("left",)); save(fig, "waterfall_deploy")

def sankey_deploy():
    """Custom bezier-ribbon Sankey: proceeds sources -> destination sleeves."""
    pl = D["plan"]
    src = [("Reliance exit", D["spot_sell"]["value_l"], P["red"]),
           ("Other 14 Sells", pl["sells_l"] - D["spot_sell"]["value_l"], ROSE),
           ("Titan trim", pl["titan_trim_l"], P["indigo2"]),
           ("Fund actions", pl["fund_actions_l"], P["indigo_t"])]
    dst = [(s[0].split("(")[0].strip(), s[1]) for s in pl["sleeves"]]
    dst.append(("Fund reshuffle", pl["fund_actions_l"]))
    total = sum(s[1] for s in src)
    fig, ax = plt.subplots(figsize=(10.0, 5.4)); ax.axis("off")
    ax.set_xlim(0, 10); ax.set_ylim(0, total * 1.02)
    gap = total * 0.02
    # source nodes (left)
    sy = total; spos = {}
    for name, v, col in src:
        y1 = sy; y0 = sy - v
        ax.add_patch(Rectangle((0.9, y0), 0.28, v, color=col, zorder=3))
        ax.text(0.8, (y0 + y1) / 2, f"{name}\n₹{v/100:.2f} Cr", ha="right", va="center",
                fontsize=10.5, color=P["navy"])
        spos[name] = [y1, y0, col]; sy -= v + gap
    # destination nodes (right), scaled to same total
    dtot = sum(d[1] for d in dst); scale = total / dtot
    dy = total; dpos = {}
    for name, v in dst:
        v2 = v * scale; y1 = dy; y0 = dy - v2
        ax.add_patch(Rectangle((8.82, y0), 0.28, v2, color=P["green"] if "reshuffle" not in name.lower() else P["indigo_t"], zorder=3))
        ax.text(9.2, (y0 + y1) / 2, f"{name}\n₹{v/100:.2f} Cr", ha="left", va="center",
                fontsize=10.5, color=P["navy"])
        dpos[name] = [y1, y0]; dy -= v2 + gap
    # ribbons: equity proceeds -> the sleeve destinations; fund actions -> fund reshuffle only
    sleeve_names = [d[0] for d in dst if "reshuffle" not in d[0].lower()]
    sleeve_tot = sum(dv for dn, dv in dst if dn in sleeve_names)
    def targets(sname):
        if sname == "Fund actions":
            return [("Fund reshuffle", 1.0)]
        return [(dn, dv / sleeve_tot) for dn, dv in dst if dn in sleeve_names]
    scur = {k: v[0] for k, v in spos.items()}
    dcur = {k: v[0] for k, v in dpos.items()}
    for sname, v, col in src:
        for dname, frac in targets(sname):
            share = v * scale * frac
            s_hi = scur[sname]; s_lo = s_hi - share; scur[sname] = s_lo
            d_hi = dcur[dname]; d_lo = d_hi - share; dcur[dname] = d_lo
            x0, x1 = 1.18, 8.82; mx = (x0 + x1) / 2
            verts = [(x0, s_hi), (mx, s_hi), (mx, d_hi), (x1, d_hi),
                     (x1, d_lo), (mx, d_lo), (mx, s_lo), (x0, s_lo), (x0, s_hi)]
            codes = [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4,
                     MPath.LINETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4, MPath.CLOSEPOLY]
            ax.add_patch(PathPatch(MPath(verts, codes), facecolor=col, edgecolor="none", alpha=0.32))
    save(fig, "sankey_deploy")

def efficient_frontier():
    rng = np.random.default_rng(7)
    n = 900
    ret = rng.uniform(6, 14, n); vol = np.zeros(n)
    for i in range(n):
        base = 3 + (ret[i] - 6) * 1.15
        vol[i] = base + rng.uniform(0, 6) + (0.06 * (ret[i] - 10) ** 2)
    sharpe = (ret - 5.5) / vol
    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    sc = ax.scatter(vol, ret, c=sharpe, cmap="YlGnBu", s=16, alpha=0.7, zorder=2)
    # frontier: upper-left hull
    order = np.argsort(vol)
    fx, fy, best = [], [], -1e9
    for i in order:
        if ret[i] > best: fx.append(vol[i]); fy.append(ret[i]); best = ret[i]
    ax.plot(fx, fy, color=P["navy"], lw=2.4, zorder=3)
    ax.scatter([13.1], [10.6], s=240, color=P["red"], edgecolor="white", linewidth=1.5, zorder=5)
    ax.annotate("Today", (13.1, 10.6), color=P["red"], fontsize=12, fontweight="bold",
                xytext=(10, -14), textcoords="offset points")
    ax.scatter([9.4], [10.9], s=240, color=P["green"], edgecolor="white", linewidth=1.5, zorder=5)
    ax.annotate("House-view target", (9.4, 10.9), color=P["green"], fontsize=12, fontweight="bold",
                xytext=(-6, 12), textcoords="offset points", ha="center")
    ax.set_xlabel("Risk  (volatility, %)"); ax.set_ylabel("Expected return  (%)")
    ax.grid(color=P["grid"], lw=0.7); ax.set_axisbelow(True); bare(ax, keep=("bottom", "left"))
    save(fig, "efficient_frontier")

def quality_price():
    fig, ax = plt.subplots(figsize=(9.4, 5.6))
    st = [s for s in D["stocks"] if s["pe"] and s["roe"] is not None and 0 < s["pe"] < 120]
    pe_med = np.median([s["pe"] for s in st]); roe_med = np.median([s["roe"] for s in st])
    for s in st:
        c = P["red"] if s["call"] == "Sell" else P["green"]
        ax.scatter(s["pe"], s["roe"], s=max(40, s["value_l"] * 16), color=c, alpha=0.72,
                   edgecolor="white", linewidth=0.7, zorder=3)
    ax.axvline(pe_med, color=P["slate"], lw=1, ls=(0, (5, 4))); ax.axhline(roe_med, color=P["slate"], lw=1, ls=(0, (5, 4)))
    for lbl, xy in [("quality, sensibly priced", (0.02, 0.96)), ("quality at a price", (0.55, 0.96)),
                    ("cheap for a reason", (0.02, 0.05)), ("expensive & mediocre", (0.55, 0.05))]:
        ax.text(*xy, lbl, transform=ax.transAxes, color=P["slate"], fontsize=11.5, style="italic")
    for nm in ("Titan Company", "Reliance Industries", "Tata Consultancy Svcs", "Infosys"):
        s = next((x for x in st if x["name"] == nm), None)
        if s: ax.annotate(s["symbol"], (s["pe"], s["roe"]), fontsize=11, fontweight="bold",
                          color=P["navy"], xytext=(7, 5), textcoords="offset points")
    ax.set_xlabel("Valuation  (P/E, x)"); ax.set_ylabel("Quality  (ROE, %)")
    bare(ax, keep=("bottom", "left")); save(fig, "quality_price")

def growth_cone():
    yrs = np.arange(0, 16); start = D["meta"]["book_cr"]; mu, sig = 0.11, 0.13
    med = start * np.exp(mu * yrs)
    lo = start * np.exp(mu * yrs - 1.28 * sig * np.sqrt(yrs))
    hi = start * np.exp(mu * yrs + 1.28 * sig * np.sqrt(yrs))
    fig, ax = plt.subplots(figsize=(9.4, 5.0))
    ax.fill_between(yrs, lo, hi, color=P["indigo"], alpha=0.13, zorder=1)
    ax.plot(yrs, med, color=P["indigo"], lw=2.6, zorder=3)
    ax.plot(yrs, hi, color=P["indigo_t"], lw=1); ax.plot(yrs, lo, color=P["indigo_t"], lw=1)
    for g, y in [("Next-gen setup ₹12 Cr", 12), ("Philanthropy ₹8 Cr", 8)]:
        ax.axhline(y, color=P["amber"], lw=1.2, ls=(0, (5, 4)))
        ax.text(0.2, y + 0.3, g, color=P["amber"], fontsize=11, fontweight="bold")
    ax.text(15, med[-1], f"median\n₹{med[-1]:.1f} Cr", color=P["indigo"], fontsize=11,
            fontweight="bold", ha="right", va="bottom")
    ax.set_xlabel("Years"); ax.set_ylabel("Portfolio value  (₹ Cr)")
    ax.grid(color=P["grid"], lw=0.7); ax.set_axisbelow(True); bare(ax, keep=("bottom", "left"))
    ax.set_xlim(0, 15); save(fig, "growth_cone")

def glidepath():
    yrs = np.arange(0, 21)
    eq = np.clip(70 - yrs * 1.4, 40, 70); intl = np.full_like(yrs, 14, dtype=float)
    gold = np.full_like(yrs, 6, dtype=float); debt = 100 - eq - intl - gold
    fig, ax = plt.subplots(figsize=(9.4, 4.8))
    ax.stackplot(yrs, eq, intl, gold, debt,
                 colors=[P["indigo"], P["indigo2"], P["amber"], P["indigo_t"]],
                 labels=["Domestic equity", "Foreign equity", "Gold & silver", "Fixed income"])
    ax.set_xlim(0, 20); ax.set_ylim(0, 100); ax.set_xlabel("Years"); ax.set_ylabel("Allocation  (%)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=4, frameon=False, fontsize=11)
    bare(ax, keep=("bottom", "left")); save(fig, "glidepath")

def drawdown():
    rng = np.random.default_rng(3); m = 120
    r = rng.normal(0.009, 0.038, m); nav = 100 * np.cumprod(1 + r)
    peak = np.maximum.accumulate(nav); dd = (nav - peak) / peak * 100
    x = np.arange(m)
    fig, ax = plt.subplots(figsize=(9.4, 4.2))
    ax.fill_between(x, dd, 0, color=P["red"], alpha=0.18); ax.plot(x, dd, color=P["red"], lw=1.6)
    ax.axhline(dd.min(), color=P["slate"], lw=1, ls=(0, (5, 4)))
    ax.text(m - 1, dd.min(), f" max drawdown {dd.min():.1f}%", color=P["red"], fontsize=11,
            va="bottom", ha="right", fontweight="bold")
    ax.set_xlabel("Months"); ax.set_ylabel("Drawdown  (%)"); ax.set_xlim(0, m - 1)
    ax.grid(color=P["grid"], lw=0.7); ax.set_axisbelow(True); bare(ax, keep=("bottom", "left"))
    save(fig, "drawdown")

def corr_heatmap():
    labels = ["Dom. eq", "Intl eq", "Debt", "Gold", "AIF", "Cash"]
    M = np.array([[1,.62,.05,-.12,.55,.02],[.62,1,.1,.05,.48,.03],[.05,.1,1,.2,.15,.4],
                  [-.12,.05,.2,1,-.05,.1],[.55,.48,.15,-.05,1,.05],[.02,.03,.4,.1,.05,1]])
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("ig", [P["red"], "white", P["indigo"]])
    fig, ax = plt.subplots(figsize=(6.0, 5.2))
    im = ax.imshow(M, cmap=cmap, vmin=-1, vmax=1)
    ax.set_xticks(range(6)); ax.set_yticks(range(6))
    ax.set_xticklabels(labels, fontsize=11, color=P["navy"]); ax.set_yticklabels(labels, fontsize=11, color=P["navy"])
    for i in range(6):
        for j in range(6):
            ax.text(j, i, f"{M[i,j]:.2f}", ha="center", va="center", fontsize=10,
                    color="white" if abs(M[i,j]) > 0.6 else P["navy"])
    ax.tick_params(length=0); [s.set_visible(False) for s in ax.spines.values()]
    save(fig, "corr_heatmap")

def montecarlo_fan():
    rng = np.random.default_rng(11); yrs = 12; n = 400; start = D["uhni"]["corpus_cr"]
    paths = np.zeros((n, yrs + 1)); paths[:, 0] = start
    for t in range(1, yrs + 1):
        paths[:, t] = paths[:, t-1] * np.exp(rng.normal(0.095, 0.11, n))
    x = np.arange(yrs + 1)
    fig, ax = plt.subplots(figsize=(9.4, 5.0))
    for i in range(0, n, 3):
        ax.plot(x, paths[i], color=P["indigo"], lw=0.4, alpha=0.06)
    for q, c in [(90, P["indigo_t"]), (50, P["indigo"]), (10, P["indigo2"])]:
        ax.plot(x, np.percentile(paths, q, axis=0), color=c, lw=2.2)
    goal = start * 2.2
    ax.axhline(goal, color=P["amber"], lw=1.4, ls=(0, (5, 4)))
    succ = (paths[:, -1] >= goal).mean() * 100
    ax.text(0.3, goal + 3, f"Goal ₹{goal:.0f} Cr · P(success) ≈ {succ:.0f}%", color=P["amber"],
            fontsize=11.5, fontweight="bold")
    ax.set_xlabel("Years"); ax.set_ylabel("Corpus  (₹ Cr)"); ax.set_xlim(0, yrs)
    ax.grid(color=P["grid"], lw=0.7); ax.set_axisbelow(True); bare(ax, keep=("bottom", "left"))
    save(fig, "montecarlo_fan")

def uhni_entities():
    ents = D["uhni"]["entities"]
    hbar("uhni_entities", [(e[0], e[2]) for e in ents], unit=" Cr", size=(8.8, 4.4), fudge=1.22)

def uhni_alloc():
    fig, ax = plt.subplots(figsize=(4.9, 4.9))
    al = D["uhni"]["alloc"]; vals = [a[1] for a in al]
    cols = [P["indigo"], P["indigo2"], P["indigo_t"], P["amber"], P["green"], P["grid"]]
    w, _ = ax.pie(vals, colors=cols, startangle=90, counterclock=False,
                  wedgeprops=dict(width=0.36, edgecolor="white", linewidth=2))
    ax.text(0, 0.08, f"₹{D['uhni']['corpus_cr']}", ha="center", fontsize=22, fontweight="bold", color=P["navy"])
    ax.text(0, -0.16, "Cr consolidated", ha="center", fontsize=12, color=P["slate"])
    ax.legend([f"{a[0]} · {a[1]:.0f}%" for a in al], loc="center", bbox_to_anchor=(0.5, -0.16),
              ncol=2, frameon=False, fontsize=10.5)
    ax.set(aspect="equal"); save(fig, "uhni_alloc")

def uhni_goals():
    goals = D["uhni"]["goals"]; fig, ax = plt.subplots(figsize=(9.4, 3.6))
    years = {"Perpetual": 2026, "2027": 2027, "2031": 2031, "2029–2034": 2031}
    ax.axhline(0, color=P["grid"], lw=2, zorder=1)
    for i, (g, amt, when) in enumerate(goals):
        yr = years.get(when, 2030); up = i % 2 == 0; y = 0.6 if up else -0.6
        ax.scatter(yr, 0, s=120, color=P["indigo"], zorder=3)
        ax.plot([yr, yr], [0, y * 0.7], color=P["indigo_t"], lw=1)
        ax.text(yr, y, f"{g}\n{amt} · {when}", ha="center", va="center", fontsize=10.5, color=P["navy"])
    ax.set_xlim(2025.5, 2035); ax.set_ylim(-1.2, 1.2); ax.set_yticks([]); ax.set_xticks(range(2026, 2035, 2))
    ax.tick_params(length=0); [s.set_visible(False) for s in ax.spines.values()]
    save(fig, "uhni_goals")

if __name__ == "__main__":
    print("Rendering charts →", OUT)
    donut_split(); score_hist(); concentration_bubble(); sector_bar(); mcap_bar(); treemap()
    radar(D["spot_hold"], "radar_titan", sell=False)
    radar(D["spot_sell"], "radar_reliance", sell=True)
    factor_radar(); capture_scatter(); rolling_consistency(); hybrid_risk()
    waterfall_deploy(); sankey_deploy(); efficient_frontier(); quality_price()
    growth_cone(); glidepath(); drawdown(); corr_heatmap(); montecarlo_fan()
    uhni_entities(); uhni_alloc(); uhni_goals()
    print("done.")
