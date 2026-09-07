"""Build the Return Distribution Atlas HTML from research/notes/tl_atlas_stats.json."""
import json
import math

ROOT = "/home/user/claude-demo"
D = json.load(open(f"{ROOT}/research/notes/tl_atlas_stats.json"))
W, H = 940, 260


def logy(c, mx, h):
    return h - h * (math.log10(c + 1) / math.log10(mx + 1))


def zhist_svg():
    hist = D["daily"]["hist"]
    edges = [(-14 + 0.5 * i) for i in range(len(hist) + 1)]
    n = D["daily"]["n"]
    mx = max(hist)
    bw = W / len(hist)
    bars, gauss_pts = [], []
    for i, c in enumerate(hist):
        lo, hi = edges[i], edges[i + 1]
        exp = n * 0.5 * (math.erf(hi / math.sqrt(2)) - math.erf(lo / math.sqrt(2)))
        x = i * bw
        if c > 0:
            y = logy(c, mx, H)
            col = "var(--s8)" if hi <= -3 else ("var(--s3)" if lo >= 3 else "var(--s1)")
            bars.append(f'<rect x="{x+1:.1f}" y="{y:.1f}" width="{bw-2:.1f}" height="{H-y:.1f}" rx="2" fill="{col}" data-tip="z in [{lo:.1f},{hi:.1f}): {c} days (Gaussian expects {exp:.2f})"/>')
        gauss_pts.append(f"{x+bw/2:.1f},{logy(exp, mx, H):.1f}")
    ticks = "".join(f'<text x="{(z+14)/28*W:.0f}" y="{H+16}" text-anchor="middle" class="tk">{z}σ</text>'
                    for z in (-12, -9, -6, -3, 0, 3, 6, 9, 12))
    return (f'<svg viewBox="0 0 {W} {H+24}" role="img" aria-label="Daily return z-score histogram vs Gaussian">'
            + "".join(f'<line x1="{(z+14)/28*W:.0f}" y1="0" x2="{(z+14)/28*W:.0f}" y2="{H}" stroke="var(--grid)"/>' for z in (-6,-3,0,3,6))
            + "".join(bars)
            + f'<polyline points="{" ".join(gauss_pts)}" fill="none" stroke="var(--s2)" stroke-width="2" stroke-dasharray="1 4" stroke-linecap="round"/>'
            + ticks + "</svg>")


def line_svg(series, ylab, color="var(--s1)", area=False, yfmt="{:.0f}"):
    xs = [s[0] for s in series]
    ys = [s[1] for s in series]
    ymin, ymax = min(ys + [0]), max(ys)
    pad = (ymax - ymin) * 0.05 or 1
    ymin -= pad; ymax += pad
    def X(i): return i / (len(ys) - 1) * W
    def Y(v): return H - (v - ymin) / (ymax - ymin) * H
    pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(ys))
    gl = ""
    import numpy as _np
    for gv in _np.linspace(ymin + pad, ymax - pad, 4):
        gl += (f'<line x1="0" y1="{Y(gv):.0f}" x2="{W}" y2="{Y(gv):.0f}" stroke="var(--grid)"/>'
               f'<text x="4" y="{Y(gv)-4:.0f}" class="tk">{yfmt.format(gv)}{ylab}</text>')
    yrs = sorted({x[:4] for x in xs})
    step = max(1, len(yrs) // 8)
    xt = ""
    for y in yrs[::step]:
        i = next(i for i, x in enumerate(xs) if x.startswith(y))
        xt += f'<text x="{X(i):.0f}" y="{H+16}" text-anchor="middle" class="tk">{y}</text>'
    body = (f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>' if not area
            else f'<polygon points="0,{Y(0):.1f} {pts} {W},{Y(0):.1f}" fill="{color}" opacity="0.25"/><polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2"/>')
    return f'<svg viewBox="0 0 {W} {H+24}" role="img">{gl}{body}{xt}</svg>'


def hist_svg(hist, x0, x1, color="var(--s1)", h=140, w=W, unit="", zero_line=None):
    mx = max(hist) or 1
    bw = w / len(hist)
    bars = ""
    for i, c in enumerate(hist):
        if c == 0:
            continue
        y = h - h * c / mx
        lo = x0 + (x1 - x0) * i / len(hist)
        hi = x0 + (x1 - x0) * (i + 1) / len(hist)
        bars += f'<rect x="{i*bw+0.5:.1f}" y="{y:.1f}" width="{max(bw-1,1):.1f}" height="{h-y:.1f}" rx="1.5" fill="{color}" data-tip="[{lo:.1f}, {hi:.1f}){unit}: {c}"/>'
    zl = ""
    if zero_line is not None and x0 < 0 < x1:
        zx = (0 - x0) / (x1 - x0) * w
        zl = f'<line x1="{zx:.1f}" y1="0" x2="{zx:.1f}" y2="{h}" stroke="var(--ink3)" stroke-dasharray="3 3"/>'
    lab = (f'<text x="2" y="{h+14}" class="tk">{x0:.0f}{unit}</text>'
           f'<text x="{w-2}" y="{h+14}" text-anchor="end" class="tk">{x1:.0f}{unit}</text>')
    return f'<svg viewBox="0 0 {w} {h+18}" role="img">{zl}{bars}{lab}</svg>'


def acf_svg():
    ac = D["clustering"]["ac_abs"]
    acr = D["clustering"]["ac_r"]
    mx = max(ac) * 1.15
    bw = W / 30
    h = 180
    bars = "".join(
        f'<rect x="{i*bw+3:.1f}" y="{h - h*max(a,0)/mx:.1f}" width="{bw-6:.1f}" height="{h*max(a,0)/mx:.1f}" rx="2" fill="var(--s1)" data-tip="lag {i+1}: autocorr(|r|) = {a:+.2f}, autocorr(r) = {acr[i]:+.2f}"/>'
        for i, a in enumerate(ac))
    dots = "".join(f'<circle cx="{i*bw+bw/2:.1f}" cy="{h - h*max(a,0)/mx:.1f}" r="3.5" fill="var(--s2)"/>' for i, a in enumerate(acr))
    return (f'<svg viewBox="0 0 {W} {h+22}" role="img"><line x1="0" y1="{h}" x2="{W}" y2="{h}" stroke="var(--grid)"/>{bars}{dots}'
            + "".join(f'<text x="{(l-1)*bw+bw/2:.0f}" y="{h+16}" text-anchor="middle" class="tk">{l}</text>' for l in (1,5,10,15,20,25,30))
            + "</svg>")


def ladder_svg():
    rows = D["ladder"]
    mx = max(r[1] for r in rows) * 1.1
    h = len(rows) * 44
    out = ""
    for i, (lab, ek, sk) in enumerate(rows):
        y = i * 44 + 8
        w = max(ek / mx * (W - 320), 3)
        out += (f'<text x="0" y="{y+15}" class="lb">{lab}</text>'
                f'<rect x="300" y="{y}" width="{w:.0f}" height="22" rx="4" fill="var(--s1)" data-tip="{lab}: excess kurtosis {ek}, skew {sk:+.2f}"/>'
                f'<text x="{306+w:.0f}" y="{y+15}" class="nm">{ek:.1f}</text>')
    return f'<svg viewBox="0 0 {W} {h}" role="img">{out}</svg>'


hz = D["horizons"]
def multiples():
    cards = ""
    for hzd in hz:
        e = hzd["edges"]
        unit = "%" if hzd["lab"] == "1m" else "%/yr"
        cards += f'''<div class="mini">
  <div class="mini-head"><span class="mini-lab">{hzd["lab"]}</span><span class="mini-pos">{100*hzd["pos"]:.0f}% positive</span></div>
  {hist_svg(hzd["hist"], e[0], e[-1], h=110, w=290, unit=unit, zero_line=0)}
  <div class="mini-foot">median <b>{100*hzd["med"]:+.1f}</b> · worst <b class="dn">{100*hzd["worst"]:+.1f}</b> · best <b class="up">{100*hzd["best"]:+.1f}</b> {unit}</div>
</div>'''
    return cards


st = D["sigma_table"]
sig_rows = "".join(
    f"<tr><td>±{r['k']}σ ({r['k']*1.30:.1f}%)</td><td>{r['lo']+r['hi']}</td><td>{r['lo']} / {r['hi']}</td>"
    f"<td>{r['gauss']:.2f}</td><td>{(r['lo']+r['hi'])/r['gauss']:,.0f}×</td></tr>" if r['gauss'] >= 0.005 else
    f"<tr><td>±{r['k']}σ ({r['k']*1.30:.1f}%)</td><td>{r['lo']+r['hi']}</td><td>{r['lo']} / {r['hi']}</td>"
    f"<td>≈0.00001</td><td>≈700,000×</td></tr>"
    for r in st)
ev_w = "".join(f"<tr><td>{d}</td><td class='dn'>{x:+.1f}%</td></tr>" for d, x in D["events"]["worst"])
ev_b = "".join(f"<tr><td>{d}</td><td class='up'>{x:+.1f}%</td></tr>" for d, x in D["events"]["best"])
yr_w = "".join(f"<tr><td>{y}</td><td class='dn'>{x:+d}%</td></tr>" for y, x in D["us_years"]["worst"])
yr_b = "".join(f"<tr><td>{y}</td><td class='up'>{x:+d}%</td></tr>" for y, x in D["us_years"]["best"])
hz_rows = "".join(
    f"<tr><td>{h['lab']}</td><td>{100*h['mean']:+.1f}</td><td>{100*h['med']:+.1f}</td><td>{100*h['sd']:.1f}</td>"
    f"<td class='dn'>{100*h['worst']:+.1f}</td><td class='up'>{100*h['best']:+.1f}</td><td>{100*h['pos']:.0f}%</td><td>{h['n']:,}</td></tr>"
    for h in hz)
cl = D["clustering"]


d2 = D["d2"]
def sigrows(key, label):
    return "".join(f"<tr><td>{label if i==0 else ''}</td><td>±{r['k']}σ</td><td>{r['obs']}</td>"
                   f"<td>{r['gauss']:.2f}" + ("</td><td>" + (f"{r['obs']/r['gauss']:,.0f}×" if r['gauss']>=0.005 else "≈10⁶×") + "</td></tr>")
                   for i, r in enumerate(d2[key]))

uhz = d2["us_hz"]
hz_sm = "".join(f"<tr><td>{m[0]}y</td><td>{m[1]:+.1f}</td><td class='dn'>{m[2]:+.1f}</td><td>{m[3]:.0f}%</td>"
                f"<td>{s2[1]:+.1f}</td><td class='dn'>{s2[2]:+.1f}</td><td>{s2[3]:.0f}%</td></tr>"
                for m, s2 in zip(uhz["mkt"], uhz["sml"]))
d2_html = f"""
<h2>The S&amp;P at 155 years</h2>
<p class="sub">Nominal monthly returns, 1871–2026 (1,867 months; Shiller monthly-average smoothing mutes these tails —
and they are still enormous). The US market total-return series below (CRSP value-weight, true month-end, 1926–2024)
is the maximal unsmoothed US series; Dow <em>daily</em> remains a principal-machine pull.</p>
<div class="grid2" style="margin-top:16px">
<div class="twrap"><table><tr><th>series</th><th>threshold</th><th>observed</th><th>Gaussian</th><th>ratio</th></tr>
{sigrows("spx_sigma","S&amp;P monthly 1871–2026")}{sigrows("usmkt_sigma","US market 1926–2024")}</table>
<p class="cap">Same law at every frequency and every era: honest to ±2σ, then failure by orders of magnitude.
The S&amp;P has four 6σ months in 155 years (a Gaussian expects ~0.000004); the unsmoothed market has three in 99 years.
S&amp;P monthly excess kurtosis 16.7 — and skew <b>+0.37</b>: the single most extreme month of American history is
<em>up</em> (Aug-1932, +50.3%), not down. A booked lean-miss, same lesson as NIFTY's daily skew.</p></div>
<div class="twrap"><table><tr><th colspan="2">Worst S&amp;P months</th><th colspan="2">Best S&amp;P months</th></tr>
{"".join(f"<tr><td>{w[0]}</td><td class='dn'>{w[1]:+.1f}%</td><td>{b[0]}</td><td class='up'>{b[1]:+.1f}%</td></tr>" for w, b in zip(d2["spx"]["worst"], d2["spx"]["best"]))}</table>
<p class="cap">Every extreme month sits inside four regimes: 1929–33, 1938, 2008, 2020. The best months live
next door to the worst — Aug-1932 (+50%) follows Apr-1932 (−24%) by four months.</p></div>
</div>

<h2>Small versus large: two markets, opposite verdicts</h2>
<div class="twrap"><table>
<tr><th></th><th>US market (99y)</th><th>US small*</th><th>India market (32y)</th><th>India small*</th></tr>
<tr><td>Mean return (nominal)</td><td>{100*uhz["mean"][0]:.1f}%/yr</td><td><b>{100*uhz["mean"][1]:.1f}%/yr</b></td><td>{100*d2["in_sum"]["mean"][0]:.1f}%/yr</td><td class="dn"><b>{100*d2["in_sum"]["mean"][1]:.1f}%/yr</b></td></tr>
<tr><td>Monthly vol ratio vs market</td><td>1.00×</td><td>{uhz["volratio"]:.2f}×</td><td>1.00×</td><td>{d2["in_sum"]["volratio"]:.2f}×</td></tr>
<tr><td>Worst month</td><td class="dn">−29.1%</td><td class="dn">−31.1%</td><td class="dn">−28.4%</td><td class="dn">−35.3%</td></tr>
<tr><td>Deepest drawdown</td><td class="dn">−{uhz["dd"]["mkt"][0]:.0f}% ({uhz["dd"]["mkt"][1]})</td><td class="dn">−{uhz["dd"]["sml"][0]:.0f}% ({uhz["dd"]["sml"][1]})</td><td class="dn">−{d2["in_sum"]["dd"]["mkt"][0]:.0f}% ({d2["in_sum"]["dd"]["mkt"][1]})</td><td class="dn">−{d2["in_sum"]["dd"]["sml"][0]:.0f}% ({d2["in_sum"]["dd"]["sml"][1]})</td></tr>
<tr><td>Monthly AR(1) (staleness)</td><td>{uhz["ar1"][0]:+.2f}</td><td>{uhz["ar1"][1]:+.2f}</td><td>{d2["in_sum"]["ar1"][0]:+.2f}</td><td>{d2["in_sum"]["ar1"][1]:+.2f}</td></tr>
</table></div>
<p class="cap">*US small = market + SMB (CRSP proxy, 1926–2024); India small = market + SMB (IIMA, 1993–2025).
Proxy construction understates true bottom-decile extremes — stated.</p>
<div class="twrap" style="margin-top:16px">
<table><tr><th>horizon</th><th>US mkt mean</th><th>worst</th><th>%&gt;0</th><th>US small mean</th><th>worst</th><th>%&gt;0</th></tr>{hz_sm}</table>
</div>
<p class="cap"><b>The US verdict:</b> small paid — +1.5 to +2.7pp/yr at every horizon for 1.32× the volatility,
and at 20 years its worst case (+5.3%/yr) beats the market's (+1.9%): the small premium compounds into a
<em>higher</em> long-horizon floor. <b>The India verdict is the opposite:</b> over 32 years the smallcap tilt
<em>lost</em> 2.9pp/yr against the market while carrying 1.34× the volatility, a deeper worst month, and a
−90% drawdown (the 2001 bust). At the factor level, Indian smallcap beta has not been compensated —
the smallcap money in India is stock <em>selection inside</em> the segment, never the segment itself.
Daily survivor-tercile detail (2013–21, severe survivorship — a lower bound on damage): the small basket
prints daily AR(1) of <b>+0.20</b> vs the NIFTY's 0.00 — the stale-price signature of illiquidity: measured
smallcap volatility understates true risk, because part of every shock arrives the next day.</p>
"""

html = f"""<title>Return Distribution Atlas</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,540;9..144,640&family=Public+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap');
:root {{
  --bg:#fcfcfb; --panel:#f4f3ee; --ink:#141412; --ink2:#52514e; --ink3:#8a887f;
  --grid:rgba(20,20,18,.09); --line:#e3e1da;
  --s1:#2a78d6; --s2:#eb6834; --s3:#1baf7a; --s8:#e34948;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#1a1a19; --panel:#232321; --ink:#f4f3ee; --ink2:#c3c2b7; --ink3:#8f8d83;
  --grid:rgba(255,255,255,.10); --line:#34332f;
  --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s8:#e66767;
}} }}
:root[data-theme="dark"] {{
  --bg:#1a1a19; --panel:#232321; --ink:#f4f3ee; --ink2:#c3c2b7; --ink3:#8f8d83;
  --grid:rgba(255,255,255,.10); --line:#34332f;
  --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s8:#e66767;
}}
body {{ background:var(--bg); color:var(--ink); font:16px/1.55 "Public Sans",system-ui,sans-serif; margin:0; }}
main {{ max-width:1000px; margin:0 auto; padding:40px 24px 80px; }}
h1 {{ font:640 44px/1.1 Fraunces,Georgia,serif; letter-spacing:-.01em; margin:.2em 0 .1em; text-wrap:balance; }}
h2 {{ font:540 27px/1.2 Fraunces,Georgia,serif; margin:2.2em 0 .5em; text-wrap:balance; }}
.sub {{ color:var(--ink2); max-width:64ch; }}
.eyebrow {{ font:500 12px/1 "IBM Plex Mono",monospace; letter-spacing:.14em; text-transform:uppercase; color:var(--ink3); }}
.heroband {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:14px; margin:28px 0 8px; }}
.stat {{ background:var(--panel); border-radius:10px; padding:16px 18px; }}
.stat .v {{ font:540 32px/1.1 Fraunces,Georgia,serif; }}
.stat .k {{ color:var(--ink2); font-size:13.5px; margin-top:4px; }}
table {{ border-collapse:collapse; width:100%; font-family:"IBM Plex Mono",monospace; font-size:13.5px; font-variant-numeric:tabular-nums; }}
th {{ text-align:left; color:var(--ink3); font-weight:500; padding:6px 12px 6px 0; border-bottom:1px solid var(--line); font-family:"Public Sans",sans-serif; }}
td {{ padding:6px 12px 6px 0; border-bottom:1px solid var(--line); }}
.tk {{ font:11.5px "IBM Plex Mono",monospace; fill:var(--ink3); }}
.lb {{ font:13px "Public Sans",sans-serif; fill:var(--ink2); }}
.nm {{ font:12.5px "IBM Plex Mono",monospace; fill:var(--ink); }}
.dn {{ color:var(--s8); }} .up {{ color:var(--s3); }}
svg {{ width:100%; height:auto; display:block; }}
.fig {{ margin:18px 0 6px; }}
.cap {{ color:var(--ink3); font-size:13px; max-width:72ch; margin:6px 0 0; }}
.legend {{ display:flex; gap:18px; font-size:13px; color:var(--ink2); margin:8px 0 2px; flex-wrap:wrap; }}
.sw {{ display:inline-block; width:11px; height:11px; border-radius:3px; margin-right:6px; vertical-align:-1px; }}
.grid2 {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:24px; }}
.minis {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:16px; }}
.mini {{ background:var(--panel); border-radius:10px; padding:12px 14px; }}
.mini-head {{ display:flex; justify-content:space-between; align-items:baseline; margin-bottom:4px; }}
.mini-lab {{ font:540 20px/1 Fraunces,Georgia,serif; }}
.mini-pos {{ font:500 12px "IBM Plex Mono",monospace; color:var(--s1); }}
.mini-foot {{ font-size:12.5px; color:var(--ink2); margin-top:4px; }}
.note {{ background:var(--panel); border-radius:10px; padding:16px 20px; font-size:13.5px; color:var(--ink2); margin-top:40px; }}
.tt {{ position:fixed; pointer-events:none; background:var(--ink); color:var(--bg); font:12.5px "IBM Plex Mono",monospace; padding:5px 9px; border-radius:6px; z-index:9; max-width:320px; }}
.twrap {{ overflow-x:auto; }}
</style>
<main>
<p class="eyebrow">The Cycle Program · descriptive atlas · registered TL-D1</p>
<h1>Return Distribution Atlas</h1>
<p class="sub">Where index returns actually live: the daily tails, the sigma ledger, volatility and its clustering,
and how the distribution changes from one day to twenty years. Series: <b>S&amp;P monthly 1871–2026</b> (nominal to 2026-08; real total return to 2023); <b>US market + smallcap monthly 1926–2024</b> (CRSP/Fama-French); <b>NIFTY 50 daily 2007–2026</b>; <b>India market + smallcap monthly 1993–2025</b> (IIMA); <b>VIX daily 1990–2026</b>; JST US annual as cross-check. US <em>daily</em> (Dow 1896–) remains a principal-machine pull — on the runsheet.</p>

<div class="heroband">
<div class="stat"><div class="v">6</div><div class="k">daily moves beyond 6σ in 4,553 NIFTY days. A Gaussian market expects 0.00001 — the observed count is ~700,000× the model.</div></div>
<div class="stat"><div class="v">15.8</div><div class="k">daily excess kurtosis. By one week it is 4.6; by one year, 0.2 — tails are a high-frequency phenomenon.</div></div>
<div class="stat"><div class="v">82 days</div><div class="k">half-life of a volatility shock (rolling-vol AR(1) φ = 0.992). Vol is a regime, not a coin flip.</div></div>
<div class="stat"><div class="v">100%</div><div class="k">of 1,593 rolling 20-year windows since 1871 ended with a positive US real total return. Worst: −0.2%/yr.</div></div>
</div>

<h2>The daily distribution, against the Gaussian that risk models assume</h2>
<div class="legend"><span><span class="sw" style="background:var(--s1)"></span>observed days (log scale)</span>
<span><span class="sw" style="background:var(--s8)"></span>beyond −3σ</span>
<span><span class="sw" style="background:var(--s3)"></span>beyond +3σ</span>
<span><span class="sw" style="background:var(--s2)"></span>Gaussian expectation (dotted)</span></div>
<div class="fig">{zhist_svg()}</div>
<p class="cap">NIFTY 50 daily z-scores (full-sample σ = 1.30%). The vertical scale is logarithmic — on a linear scale
the tails would be invisible, which is exactly how they get ignored. The dotted curve dies at ±4σ; the market does not.</p>

<div class="grid2" style="margin-top:26px">
<div class="twrap"><h2 style="margin-top:0">The sigma ledger</h2>
<table><tr><th>threshold (move)</th><th>observed</th><th>down / up</th><th>Gaussian expects</th><th>ratio</th></tr>{sig_rows}</table>
<p class="cap">Between ±1σ and ±2σ the Gaussian is roughly honest. From 3σ out it fails by growing orders of magnitude:
±3σ days run 5.6×, ±4σ days 121×, and 6σ days — “impossible” — happened six times in nineteen years.
Skew is +0.06: at daily frequency the up-tail is as fat as the down-tail (a booked prior miss —
the felt asymmetry lives in volatility timing, not in daily skew).</p></div>
<div class="twrap"><h2 style="margin-top:0">Both ends of the tail</h2>
<div class="grid2">
<table><tr><th colspan="2">Worst NIFTY days</th></tr>{ev_w}</table>
<table><tr><th colspan="2">Best NIFTY days</th></tr>{ev_b}</table>
</div>
<p class="cap">All twenty extreme days fall inside three episodes — 2008, the 2009 election reopen, and March 2020.
The best days live inside the worst regimes: missing the crash means missing the rebound.</p></div>
</div>

<h2>Volatility: its path, its distribution, its memory</h2>
<div class="fig">{line_svg(cl["vol_series"], "%", "var(--s1)")}</div>
<p class="cap">Rolling 21-day annualized NIFTY volatility. Median 14.3%, 95th percentile 38.6%, peak 87.9% (March 2020)
— a 6× range between the calm and stressed regimes of the same index.</p>
<div class="grid2" style="margin-top:20px">
<div><div class="legend"><span><span class="sw" style="background:var(--s1)"></span>21-day realized vol (NIFTY)</span></div>
{hist_svg(cl["vol_hist"], 4, 92, h=150, unit="%")}
<p class="cap">Realized vol is right-skewed and lognormal-ish: it lives near 10–18% and visits 40%+ rarely but unforgettably.</p></div>
<div><div class="legend"><span><span class="sw" style="background:var(--s1)"></span>VIX daily close, 1990–2026</span></div>
{hist_svg(D["vix"]["hist"], 8, 84, h=150)}
<p class="cap">Implied vol says the same: median 17.6, mean 19.4 (mean &gt; median — the right tail), maximum 82.7 on 2020-03-16.</p></div>
</div>
<div class="legend" style="margin-top:22px"><span><span class="sw" style="background:var(--s1)"></span>autocorrelation of |return| (clustering)</span>
<span><span class="sw" style="background:var(--s2)"></span>autocorrelation of return (signal)</span></div>
<div class="fig">{acf_svg()}</div>
<p class="cap">The defining asymmetry of markets: the <em>sign</em> of yesterday's return tells you nothing (orange dots ≈ 0),
but its <em>size</em> echoes for months — |r| autocorrelation is +0.28 at lag 1 and still +0.18 thirty days out.
Volatility is forecastable; direction is not. This is the license behind vol-managed sizing (F3a) and the L2 stress band.</p>

<h2>The same market at eight speeds</h2>
<p class="sub">US real total returns, rolling windows over 152 years. Every window length is the same underlying series —
only the holding period changes. Overlapping windows; distributions are descriptive, not independent draws.</p>
<div class="minis" style="margin-top:16px">{multiples()}</div>
<div class="twrap" style="margin-top:22px">
<table><tr><th>horizon</th><th>mean</th><th>median</th><th>sd</th><th>worst</th><th>best</th><th>% positive</th><th>windows</th></tr>{hz_rows}</table>
</div>
<p class="cap">The compression is the story: annualized dispersion falls 19.3% → 2.9% from 1y to 20y, the worst case rises
−58% → −0.2%/yr, and the positive fraction climbs 69% → 100%. Time does not remove equity risk — it converts
“will I lose?” into “how much less than 7% will I compound?” (JST annual cross-check: worst US 20y +0.9%/yr.)
The US caveat from the disaster census stands: this is the <em>shallowest-disaster</em> country of the 16 —
the 16-country median worst drawdown is −78% with an 18-year recovery.</p>

<h2>Why horizon changes the shape: the kurtosis ladder</h2>
<div class="fig">{ladder_svg()}</div>
<p class="cap">Excess kurtosis by aggregation step (0 = Gaussian). Fat tails wash out as returns aggregate —
daily 15.8 collapses to 0.2 at annual — with one exception that proves the rule: US <em>monthly</em> over 152 years
keeps kurtosis 18, because it contains the 1930s. Within any calm few decades, aggregation tames the tails;
across a century that includes a Depression, it never fully does. (Shiller monthly prices are month-averages —
the 1-month cells are smoothed; ≥ 1y horizons are unaffected.)</p>

<h2>The 152-year real drawdown path</h2>
<div class="fig">{line_svg(D["us_dd"], "%", "var(--s8)", area=True, yfmt="{:.0f}")}</div>
<p class="cap">Drawdown of the US real total-return index from its running peak. The deepest: −77% (June 1932).
The longest full recoveries cluster around the 1910s inflation, the Depression, and 1966–1982 —
the last of which never printed a −77% but took sixteen years of real losses to escape.</p>

{d2_html}
<div class="note"><b>Provenance & caveats.</b> S&amp;P: github.com/datasets/s-and-p-500 mirror of Shiller ie_data,
vaulted 2026-09-07, 6/6 pre-stated anchors passed (sha256 in manifest); real columns end 2023-09 (CPI lag) — series
truncated there, run-noted. NIFTY 50 &amp; VIX: authenticated vaults. Monthly Shiller prices are monthly <em>averages</em>:
1-month statistics are smoothed (vol understated); horizons ≥ 1y unaffected. All rolling-window distributions overlap —
n is windows, not independent observations. Sigma thresholds use full-sample σ; a rolling-σ variant is a different,
unrun design. Registered as TL-D1 (8 cells) in research/register/trial-ledger.md; census 525.
Dow Jones daily (100y+) is not freely reachable from this environment — runsheet row added for the principal machine.</div>
</main>
<script>
const tt = document.createElement('div'); tt.className='tt'; tt.hidden=true; document.body.appendChild(tt);
document.addEventListener('mousemove', e => {{
  const t = e.target.closest('[data-tip]');
  if (t) {{ tt.textContent = t.getAttribute('data-tip'); tt.hidden=false;
    tt.style.left = Math.min(e.clientX+14, innerWidth-330)+'px'; tt.style.top = (e.clientY+16)+'px'; }}
  else tt.hidden = true;
}});
</script>
"""
open(f"{ROOT}/docs/learn/artifacts/return-distribution-atlas.html", "w").write(html)
print("written", len(html), "bytes")
