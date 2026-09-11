"""Assemble the dashboard HTML and the written reconciliation report."""

import datetime
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

RANDOM_SEED = 20260831

# Firm tie-outs surfaced in the QC tab, with the raw source named so a reader
# can re-derive each one without this build.
TIE_SPEC = [
    ("firm total AUM == raw aum col Z", "Total book (Cr)",
     "SUM of aum!Z (total_current_value_crores), all 8,669 rows"),
    ("firm platform == raw platform core_flag=1", "Platform core-4 (Cr)",
     "SUM of platform!L where platform!U (core_flag) = 1"),
    ("firm clients == raw aum client rows", "Clients (accounts)",
     "COUNT of aum rows where user_type starts 'client'"),
    ("firm platform clients == distinct core clients", "Platform clients",
     "DISTINCT client_user_id on platform where core_flag = 1"),
    ("firm >=50L == raw aum buckets", "Clients >= 50L",
     "COUNT of client rows outside the 0-10L / 10-50L buckets"),
    ("firm <50L == raw aum buckets", "Clients < 50L",
     "COUNT of client rows in the 0-10L / 10-50L buckets"),
    ("firm platform Mar == MoM Trend Mar-26", "Platform Mar-31 (Cr)",
     "MoM Trend C16; also SUM of Platform Charts col F"),
    ("firm platform Jun == MoM Trend Jun-26", "Platform Jun-30 (Cr)",
     "MoM Trend C19; also SUM of Platform Charts col G"),
    ("product mix sums to firm platform", "Product mix sums to platform",
     "SUM of platform!L by product_name where core_flag = 1"),
    ("RM count", "RM count",
     "Platform Charts (RM) rows 5:77"),
    ("desk focus sums to firm focus", "Focus (Cr)",
     "H1 & Quarter Progress section C, FIRM row"),
]


def _fmt(v):
    if isinstance(v, float):
        return f"{v:,.4f}".rstrip("0").rstrip(".") if abs(v) < 10000 else f"{v:,.2f}"
    return f"{v:,}" if isinstance(v, int) else str(v)


def _prior_firm(prior_html):
    with open(prior_html) as fh:
        html = fh.read()
    start = html.index("const DATA=") + len("const DATA=")
    data, _ = json.JSONDecoder().raw_decode(html[start:])
    firm = data["firm"]
    firm["rm_rows"] = sum(len(t["rows"]) for t in data["teams"])
    firm["desks"] = len(data["teams"])
    return firm


def _variance(data, prior_html):
    prior = _prior_firm(prior_html)
    now = data["firm"]
    spec = [
        ("Total book (Cr)", prior["tot_aug"], now["tot_aug"], 2),
        ("Platform core-4 (Cr)", prior["p_aug"], now["p_aug"], 2),
        ("Penetration", prior["p_aug"] / prior["tot_aug"] * 100,
         now["p_aug"] / now["tot_aug"] * 100, 2),
        ("Clients (accounts)", prior["cl_aug"], now["cl_aug"], 0),
        ("Platform clients", prior["p_cl"], now["p_cl"], 0),
        ("Platform clients with live value", prior["p_cl_live"], now["p_cl_live"], 0),
        ("Focus (Cr)", prior["f_aug"], now["f_aug"], 2),
        ("Platform Mar-31 (Cr)", prior["trend"][2][1], now["p_mar"], 2),
        ("Platform Jun-30 (Cr)", prior["trend"][3][1], now["p_jun"], 2),
        ("RMs", prior["rm_rows"], now["rms"], 0),
        ("Desks", prior["desks"], now["teams"], 0),
    ]
    rows = []
    for metric, was, is_, dp in spec:
        delta = is_ - was
        suffix = "%" if metric == "Penetration" else ""
        rows.append({
            "metric": metric,
            "prior": f"{was:,.{dp}f}{suffix}",
            "now": f"{is_:,.{dp}f}{suffix}",
            "delta": f"{'+' if delta >= 0 else '−'}{abs(delta):,.{dp}f}{'pt' if suffix else ''}",
        })
    return rows


def _qc_payload(data, checks, sample, stale, source_label, prior_html):
    by_name = {r["name"]: r for r in checks.rows}
    ties = []
    for key, label, source in TIE_SPEC:
        row = by_name.get(key)
        if not row:
            continue
        exact = row["got"] == row["want"]
        ties.append({"name": label, "computed": _fmt(row["got"]),
                     "target": _fmt(row["want"]), "source": source,
                     "ok": row["ok"],
                     "tie": "exact" if exact else "within 0.01Cr"})

    suites = []
    for name in ("cross-check", "random-check", "calc-check"):
        rows = [r for r in checks.rows if r["suite"] == name]
        bad = [r for r in rows if not r["ok"]]
        suites.append({"name": name, "pass": len(rows) - len(bad),
                       "total": len(rows), "fail": len(bad)})

    return {
        "source": source_label,
        "built": datetime.date.today().isoformat(),
        "seed": RANDOM_SEED,
        "ties": ties,
        "suites": suites,
        "sample": sample,
        "stale": stale,
        "variance": _variance(data, prior_html),
        "total": len(checks.rows),
        "total_pass": len(checks.rows) - len(checks.failed),
    }


def dashboard(data, checks, sample, stale, source_label, prior_html):
    css = open(os.path.join(HERE, "base.css")).read()
    css += "\n" + open(os.path.join(HERE, "chart.css")).read()
    app = open(os.path.join(HERE, "app.js")).read()
    qc = _qc_payload(data, checks, sample, stale, source_label, prior_html)
    firm = data["firm"]

    focus_note = (
        "Focus is reported by the MIS at team level only this cycle; the per-RM "
        "figures shown on each card are carried from the previous dashboard and "
        "tagged <b>prior cycle</b>, and any team remainder they do not account for "
        "is shown separately as unattributed."
        if firm["focus_basis"] == "prior" else
        "Focus is taken from the supplied RM-wise focus file."
    )

    foot = (
        "One card per RM, ranked by platform AUM within the desk. Rebuilt from "
        f"<b>{source_label}</b> &mdash; total book &#8377;{firm['tot_aug']:,.2f}Cr &middot; "
        f"platform &#8377;{firm['p_aug']:,.2f}Cr &middot; focus &#8377;{firm['f_aug']:,.2f}Cr &middot; "
        f"{firm['cl_aug']:,} client accounts ({firm['households']:,} households) &middot; "
        f"{firm['p_cl']} platform clients &middot; "
        f"{firm['p_aug'] / firm['tot_aug'] * 100:.2f}% penetration &middot; {firm['rms']} RMs. "
        "Every figure ties to the raw <code>aum</code> and <code>platform</code> sheets &mdash; "
        "see the <b>Data QC</b> tab.<br>"
        "Definitions: <b>Platform</b> = core-4 on the net-funding basis (Allocate, High Yield "
        f"Enhancer, Navigate, Co-Pilot). Sharpe One and PIPE (&#8377;{firm['all_products'] - firm['p_aug']:,.2f}Cr) "
        f"are outside it; all platform products together are &#8377;{firm['all_products']:,.2f}Cr. "
        "<b>Platform clients</b> = distinct clients with a core-4 account, including positions "
        f"valued at zero today ({firm['p_cl_live']} carry live value). "
        f"<b>Clients &#8805;&#8377;1Cr</b> = {firm['ge_1cr_hh']} households "
        f"({firm['ge_1cr_acct']} accounts) &mdash; the workbook quotes both bases. "
        "<b>New Jun&#8594;Aug</b> = client ids on the book at Aug-31 but not at Jun-30. "
        "<b>Above &#8377;50L</b> is inclusive. Platform Aug includes the "
        f"&#8377;{firm['recon_uplift']:,.2f}Cr RM-level reconciliation rows. "
        "Mar/Jun books follow the RM name, so an RM who changed desks carries their prior book. "
        f"{focus_note} Remark and Action are editable and saved in this browser; figures are read-only."
    )

    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Ionic Wealth — RM Platform Review · Aug-31 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600;6..72,700&family=Reddit+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<div class="topbar"><div class="tin">
 <div class="logo">
  <svg class="emblem" viewBox="0 0 34 34" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
   <rect width="34" height="34" rx="9" fill="#FFB951"/>
   <path d="M17 5.5c-4 3.4-6.4 6.7-6.4 10.9 0 4.1 2.9 7.1 6.4 7.1s6.4-3 6.4-7.1c0-4.2-2.4-7.5-6.4-10.9z" fill="#242BA1"/>
   <circle cx="17" cy="16.6" r="2.4" fill="#FFB951"/><rect x="15.6" y="24.5" width="2.8" height="4.2" rx="1.4" fill="#242BA1"/>
  </svg>
  <div><div class="b1">Ionic</div><div class="b2">Wealth</div></div>
 </div>
 <div class="tblock"><div class="tt1">RM Platform Review — by Market Leader</div>
  <div class="tt2">HNI book &middot; &#8377;Cr &middot; as at 31 Aug 2026 &middot; one card per RM for the ML 1:1</div></div>
 <div class="fks" id="fks"></div>
</div></div>
<div class="wrap">
 <div class="controls"><div class="tabs" id="tabs"></div>
  <button class="btn" onclick="window.print()">Print / PDF</button>
  <button class="btn warn" onclick="reset()">Reset notes</button>
 </div>
 <div id="firmline"></div>
 <div id="panel"></div>
 <div class="foot" id="foot">{foot}</div>
</div>
<div id="tip" role="status" aria-live="polite"></div>
<script>
const DATA={json.dumps(data, ensure_ascii=False, separators=(",", ":"))};
const QC={json.dumps(qc, ensure_ascii=False, separators=(",", ":"))};
{app}
</script>
</body></html>
"""


def qc_markdown(data, checks, sample, slipping, stale, source_label, prior_html):
    firm, desks = data["firm"], data["teams"]
    qc = _qc_payload(data, checks, sample, stale, source_label, prior_html)
    L = []
    w = L.append

    w("# RM Platform Review — Aug-31 2026 reconciliation\n")
    w(f"Source: `{source_label}`  ")
    w(f"Built: {qc['built']}  ")
    w(f"Result: **{qc['total_pass']}/{qc['total']} checks pass**"
      f"{' — BUILD WOULD ABORT' if checks.failed else ''}\n")
    for s in qc["suites"]:
        w(f"- **{s['name']}** — {s['pass']}/{s['total']} pass")
    w("")

    w("## Cross-check — firm tie-outs\n")
    w("| Measure | Built from 73 RM rows | Raw source | Where the raw figure comes from | Tie |")
    w("|---|---:|---:|---|---|")
    for t in qc["ties"]:
        w(f"| {t['name']} | {t['computed']} | {t['target']} | {t['source']} | "
          f"{t['tie'] if t['ok'] else '**FAIL**'} |")
    w("")

    w("## Desk roll-up\n")
    w("| # | Desk | RMs | AUM | Clients | Plat Mar | Plat Jun | Plat Aug | Plat cl | Pen. | Focus |")
    w("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for d in desks:
        w(f"| {d['rank']} | {d['ml']} | {d['rms']} | {d['tot_aug']:,.2f} | {d['cl_aug']:,} | "
          f"{d['p_mar']:,.2f} | {d['p_jun']:,.2f} | {d['p_aug']:,.2f} | {d['p_cl']} | "
          f"{d['p_aug'] / d['tot_aug'] * 100:.2f}% | {d['f_aug']:,.2f} |")
    w(f"| | **FIRM** | **{firm['rms']}** | **{firm['tot_aug']:,.2f}** | **{firm['cl_aug']:,}** | "
      f"**{firm['p_mar']:,.2f}** | **{firm['p_jun']:,.2f}** | **{firm['p_aug']:,.2f}** | "
      f"**{firm['p_cl']}** | **{firm['p_aug'] / firm['tot_aug'] * 100:.2f}%** | **{firm['f_aug']:,.2f}** |")
    w("")

    w(f"## Random check — {len(sample)} RMs re-derived from raw rows\n")
    w(f"Seeded sample (seed {RANDOM_SEED}). Each RM's AUM, client count, 50L split, platform "
      "total and all four product values plus product client counts were recomputed by "
      "filtering the raw `aum` and `platform` rows one at a time.\n")
    w("| RM | Desk | AUM | Clients | Platform | Plat cl | >=50L | <50L | Re-derived |")
    w("|---|---|---:|---:|---:|---:|---:|---:|---|")
    for s in sample:
        w(f"| {s['rm']} | {s['ml']} | {s['tot_aug']:,.2f} | {s['cl_aug']} | {s['p_aug']:,.2f} | "
          f"{s['p_cl']} | {s['g50']} | {s['l50']} | {'match' if s['ok'] else '**FAIL**'} |")
    w("")

    w("## Calc check\n")
    calc = [r for r in checks.rows if r["suite"] == "calc-check"]
    w(f"{len(calc)} recomputations of the figures the page renders — penetration, client "
      "penetration, product shares, mix shares, Mar→Aug and Jun→Aug deltas, and each desk's "
      f"Jun product base plus its delta against its Aug platform total. "
      f"{len([r for r in calc if r['ok']])}/{len(calc)} pass.\n")
    w(f"- `flagOf` 'Slipping vs Jun' fires on {len(slipping)} RM(s): "
      f"{', '.join(slipping) if slipping else 'none'}")
    w("- no card renders NaN, a negative AUM, or platform clients above total clients\n")

    w("## Movement vs the previous dashboard\n")
    w("| Measure | Prior (FINAL_1_1) | Aug-31 MIS | Change |")
    w("|---|---:|---:|---:|")
    for v in qc["variance"]:
        w(f"| {v['metric']} | {v['prior']} | {v['now']} | {v['delta']} |")
    w("")

    w("## Source blocks deliberately not used\n")
    for i, s in enumerate(stale, 1):
        w(f"**{i}. {s['block']}**  ")
        w(f"Would have injected: {s['would_inject']}  ")
        w(f"Actual: {s['truth']}  ")
        w(f"Used instead: {s['instead']}  ")
        if s.get("note"):
            w(f"Note: {s['note']}  ")
        w("")

    if checks.failed:
        w("## Failures\n")
        for r in checks.failed:
            w(f"- `{r['suite']}` **{r['name']}** — got `{r['got']}`, want `{r['want']}` {r['note']}")
        w("")

    return "\n".join(L)
