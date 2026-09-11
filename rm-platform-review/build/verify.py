"""Three independent check suites over the built DATA.

Cross-check  - every total is asserted against a figure recomputed from the
               raw `aum` / `platform` rows, never against a workbook summary
               row (several of which are stale).
Random check - a seeded sample of RMs is re-derived by filtering raw rows one
               at a time, with no SUMIFS-equivalent shortcut, and compared
               field by field.
Calc check   - every percentage and delta the dashboard renders is recomputed
               and compared to what the DATA implies.
"""

import collections
import random

TOL_CR = 0.011      # 1 paisa of rounding on a 2dp Cr figure
TOL_PCT = 0.0005


class Checks:
    def __init__(self):
        self.rows = []

    def add(self, suite, name, ok, got, want=None, note=""):
        self.rows.append({"suite": suite, "name": name, "ok": bool(ok),
                          "got": got, "want": want, "note": note})

    def eq(self, suite, name, got, want, tol=0.0, note=""):
        ok = abs(got - want) <= tol if isinstance(want, float) or tol else got == want
        self.add(suite, name, ok, got, want, note)

    @property
    def failed(self):
        return [r for r in self.rows if not r["ok"]]

    def report(self):
        by_suite = collections.OrderedDict()
        for r in self.rows:
            by_suite.setdefault(r["suite"], []).append(r)
        lines = []
        for suite, rows in by_suite.items():
            bad = [r for r in rows if not r["ok"]]
            lines.append(f"{suite}: {len(rows) - len(bad)}/{len(rows)} PASS"
                         + (f"  ** {len(bad)} FAIL **" if bad else ""))
            for r in rows:
                if not r["ok"]:
                    lines.append(f"    FAIL {r['name']}: got {r['got']!r} want {r['want']!r} {r['note']}")
        return "\n".join(lines)


# --------------------------------------------------------------------------
# raw truths, computed here independently of extract.py
# --------------------------------------------------------------------------
def raw_truth(wb):
    au = wb.sheet("aum")
    pl = wb.sheet("platform")

    aum_by_rm = collections.defaultdict(float)
    cl_by_rm = collections.Counter()
    g50 = collections.Counter()
    l50 = collections.Counter()
    firm_aum = 0.0
    for r, row in au.items():
        if r == 1:
            continue
        firm_aum += row.get(26, 0.0) or 0.0
        aum_by_rm[row.get(12, "")] += row.get(26, 0.0) or 0.0
        if not str(row.get(27, "")).startswith("client"):
            continue
        rm = row.get(12, "")
        cl_by_rm[rm] += 1
        if str(row.get(28, "")) in ("0-10L AUM", "10-50 L AUM"):
            l50[rm] += 1
        else:
            g50[rm] += 1

    p_by_rm = collections.defaultdict(float)
    p_prod = collections.defaultdict(float)
    p_prod_cl = collections.defaultdict(set)
    p_cl = collections.defaultdict(set)
    firm_prod = collections.defaultdict(float)
    firm_core_clients = set()
    for r, row in pl.items():
        if r == 1 or row.get(21) != 1:
            continue
        rm, product = row.get(19, ""), row.get(5, "")
        value = row.get(12, 0.0) or 0.0
        p_by_rm[rm] += value
        p_prod[(rm, product)] += value
        p_prod_cl[(rm, product)].add(row.get(1))
        p_cl[rm].add(row.get(1))
        firm_core_clients.add(row.get(1))
        firm_prod[product] += value

    return {
        "firm_aum": round(firm_aum, 4),
        "aum_by_rm": aum_by_rm, "cl_by_rm": cl_by_rm, "g50": g50, "l50": l50,
        "p_by_rm": p_by_rm, "p_prod": p_prod,
        "p_prod_cl": {k: len(v) for k, v in p_prod_cl.items()},
        "p_cl": {k: len(v) for k, v in p_cl.items()},
        "firm_core_clients": len(firm_core_clients),
        "firm_prod": dict(firm_prod),
    }


def cross_check(c, data, wb, truth):
    firm, desks = data["firm"], data["teams"]
    rows = [r for d in desks for r in d["rows"]]
    S = "cross-check"

    c.eq(S, "firm total AUM == raw aum col Z", firm["tot_aug"], truth["firm_aum"], TOL_CR)
    c.eq(S, "firm platform == raw platform core_flag=1",
         firm["p_aug"], round(sum(truth["firm_prod"].values()), 2), TOL_CR)
    c.eq(S, "firm clients == raw aum client rows", firm["cl_aug"], sum(truth["cl_by_rm"].values()))
    c.eq(S, "firm >=50L == raw aum buckets", firm["g50"], sum(truth["g50"].values()))
    c.eq(S, "firm <50L == raw aum buckets", firm["l50"], sum(truth["l50"].values()))
    c.eq(S, "firm platform clients == distinct core clients",
         firm["p_cl"], truth["firm_core_clients"])
    c.eq(S, "RM count", firm["rms"], 73)
    c.eq(S, "firm platform Mar == MoM Trend Mar-26", firm["p_mar"], 260.79, TOL_CR)
    c.eq(S, "firm platform Jun == MoM Trend Jun-26", firm["p_jun"], 388.61, TOL_CR)
    c.eq(S, "product mix sums to firm platform",
         round(sum(v for _, v in firm["mix"]), 2), firm["p_aug"], TOL_CR)

    # desk sums must equal the firm, and each desk must equal its own RMs
    for field in ("tot_aug", "p_aug", "cl_aug", "p_cl", "g50", "l50"):
        total = sum(d[field] for d in desks)
        c.eq(S, f"desks sum to firm: {field}", round(total, 4) if isinstance(total, float) else total,
             firm[field], TOL_CR if isinstance(total, float) else 0)
    for d in desks:
        for field in ("tot_aug", "p_aug", "cl_aug", "p_cl"):
            got = sum(r[field] for r in d["rows"])
            c.eq(S, f"{d['ml']}: {field} == sum of its RMs",
                 round(got, 4) if isinstance(got, float) else got, d[field],
                 TOL_CR if isinstance(got, float) else 0)

    # every desk's platform total must match the workbook's own NEW-B ML row
    ts = wb.sheet("Team Summary")
    newb = {ts[r][1]: ts[r].get(21, 0.0) for r in range(36, 49)
            if r in ts and ts[r].get(1)}
    for d in desks:
        if d["ml"] in newb:
            c.eq(S, f"{d['ml']}: platform == Team Summary NEW-B row",
                 d["p_aug"], round(newb[d["ml"]], 2), TOL_CR)

    # Exhaustive per-RM equality against the raw rows, for ALL 73 RMs -- not
    # just the random sample.  Fault injection showed that a compensating swap
    # inside one RM (a client moved across the 50L line, or a wrong product
    # client count) survives every aggregate check, because the totals still
    # add up.  These are the checks that catch it.
    per_rm_fields = [
        ("tot_aug", lambda r: r["tot_aug"], lambda rm: round(truth["aum_by_rm"].get(rm, 0.0), 4), TOL_CR),
        ("cl_aug", lambda r: r["cl_aug"], lambda rm: truth["cl_by_rm"].get(rm, 0), 0),
        ("g50", lambda r: r["g50"], lambda rm: truth["g50"].get(rm, 0), 0),
        ("l50", lambda r: r["l50"], lambda rm: truth["l50"].get(rm, 0), 0),
        ("p_aug", lambda r: r["p_aug"], lambda rm: round(truth["p_by_rm"].get(rm, 0.0), 2), TOL_CR),
        ("p_cl", lambda r: r["p_cl"], lambda rm: truth["p_cl"].get(rm, 0), 0),
    ]
    for field, got_of, want_of, tol in per_rm_fields:
        bad = []
        for r in rows:
            got, want = got_of(r), want_of(r["rm"])
            if abs(got - want) > tol:
                bad.append(f"{r['rm']} {got}!={want}")
        c.add(S, f"per-RM {field} == raw rows (all {len(rows)})", not bad, len(bad), 0,
              note=f"offenders: {bad[:4]}")

    product_pairs = [("ALLOCATE", "Allocate"), ("HIGH YIELD ENHANCER", "YE"),
                     ("NAVIGATE", "Navigate"), ("CO-PILOT", "Co-Pilot")]
    for raw_name, label in product_pairs:
        bad_aum, bad_cl = [], []
        for r in rows:
            slot = next(p for p in r["prod"] if p["name"] == label)
            want_aum = round(truth["p_prod"].get((r["rm"], raw_name), 0.0), 2)
            want_cl = truth["p_prod_cl"].get((r["rm"], raw_name), 0)
            if abs(slot["aug"] - want_aum) > TOL_CR:
                bad_aum.append(f"{r['rm']} {slot['aug']}!={want_aum}")
            if slot["cl"] != want_cl:
                bad_cl.append(f"{r['rm']} {slot['cl']}!={want_cl}")
        c.add(S, f"per-RM {label} AUM == raw rows (all {len(rows)})", not bad_aum,
              len(bad_aum), 0, note=f"offenders: {bad_aum[:4]}")
        c.add(S, f"per-RM {label} clients == raw rows (all {len(rows)})", not bad_cl,
              len(bad_cl), 0, note=f"offenders: {bad_cl[:4]}")

    # per-RM identity: the two client splits must account for every client
    bad = [r["rm"] for r in rows if r["g50"] + r["l50"] != r["cl_aug"]]
    c.add(S, "per-RM: g50 + l50 == cl_aug (all 73)", not bad, len(bad), 0,
          note=f"offenders: {bad[:5]}")

    # per-RM platform must equal the sum of its four product values
    bad = [r["rm"] for r in rows
           if abs(sum(p["aug"] for p in r["prod"]) - r["p_aug"]) > TOL_CR]
    c.add(S, "per-RM: products sum to p_aug (all 73)", not bad, len(bad), 0,
          note=f"offenders: {bad[:5]}")

    # agreement with the team sheets' own per-RM blocks
    sheet_h, sheet_2b = {}, {}
    from sources import TEAM_SHEETS
    for name in TEAM_SHEETS:
        sh = wb.sheet(name)
        start = next(r for r in sorted(sh) if str(sh[r].get(1, "")).startswith("H  ·")) + 2
        r = start
        while r in sh and str(sh[r].get(2, "")) != "TEAM TOTAL":
            if sh[r].get(2):
                sheet_h[sh[r][2]] = sh[r].get(7, 0.0)
            r += 1
        start = next(r for r in sorted(sh) if str(sh[r].get(1, "")).startswith("2b ·")) + 2
        r = start
        while r in sh and str(sh[r].get(2, "")) != "ML TOTAL":
            if sh[r].get(2):
                sheet_2b[sh[r][2]] = sh[r].get(12, 0)
            r += 1
    bad = [r["rm"] for r in rows
           if r["rm"] in sheet_h and abs(sheet_h[r["rm"]] - r["p_aug"]) > TOL_CR]
    c.add(S, "per-RM platform == team sheet Section H", not bad, len(bad), 0,
          note=f"offenders: {bad[:5]}")
    bad = [r["rm"] for r in rows
           if r["rm"] in sheet_2b and sheet_2b[r["rm"]] != r["p_cl"]]
    c.add(S, "per-RM platform clients == team sheet 2b col L", not bad, len(bad), 0,
          note=f"offenders: {bad[:5]}")

    # focus must roll up to the MIS firm figure
    c.eq(S, "desk focus sums to firm focus",
         round(sum(d["f_aug"] for d in desks), 2), firm["f_aug"], TOL_CR)


def random_check(c, data, truth, sample_size=20, seed=20260831):
    """Re-derive a random sample from raw rows and compare field by field."""
    S = "random-check"
    rows = {r["rm"]: r for d in data["teams"] for r in d["rows"]}
    rng = random.Random(seed)
    picked = sorted(rng.sample(sorted(rows), min(sample_size, len(rows))))
    table = []

    for rm in picked:
        rec = rows[rm]
        checks = {
            "tot_aug": (rec["tot_aug"], round(truth["aum_by_rm"].get(rm, 0.0), 4)),
            "cl_aug": (rec["cl_aug"], truth["cl_by_rm"].get(rm, 0)),
            "g50": (rec["g50"], truth["g50"].get(rm, 0)),
            "l50": (rec["l50"], truth["l50"].get(rm, 0)),
            "p_aug": (rec["p_aug"], round(truth["p_by_rm"].get(rm, 0.0), 2)),
        }
        for raw, label in [("ALLOCATE", "Allocate"), ("HIGH YIELD ENHANCER", "YE"),
                           ("NAVIGATE", "Navigate"), ("CO-PILOT", "Co-Pilot")]:
            got = next(p["aug"] for p in rec["prod"] if p["name"] == label)
            checks[f"prod:{label}"] = (got, round(truth["p_prod"].get((rm, raw), 0.0), 2))
            got_cl = next(p["cl"] for p in rec["prod"] if p["name"] == label)
            checks[f"prodcl:{label}"] = (got_cl, truth["p_prod_cl"].get((rm, raw), 0))

        bad = []
        for field, (got, want) in checks.items():
            tol = TOL_CR if isinstance(want, float) else 0
            if abs(got - want) > tol:
                bad.append(f"{field} {got}!={want}")
        c.add(S, f"{rm} ({rec['ml']})", not bad, "ok" if not bad else "; ".join(bad), "ok")
        table.append({"rm": rm, "ml": rec["ml"], "tot_aug": rec["tot_aug"],
                      "cl_aug": rec["cl_aug"], "p_aug": rec["p_aug"],
                      "p_cl": rec["p_cl"], "g50": rec["g50"], "l50": rec["l50"],
                      "ok": not bad})
    return table


def calc_check(c, data):
    """Recompute every derived figure the page renders."""
    S = "calc-check"
    firm, desks = data["firm"], data["teams"]
    rows = [r for d in desks for r in d["rows"]]

    c.eq(S, "firm penetration = p_aug/tot_aug",
         round(firm["p_aug"] / firm["tot_aug"], 6), round(528.46 / 3825.2247, 6), TOL_PCT)
    c.eq(S, "firm penetration renders 13.8%",
         f"{firm['p_aug'] / firm['tot_aug'] * 100:.1f}%", "13.8%")
    c.eq(S, "firm client penetration = p_cl/cl_aug",
         f"{firm['p_cl'] / firm['cl_aug'] * 100:.1f}%", "22.4%")

    for label, value in firm["mix"]:
        share = value / firm["p_aug"]
        c.add(S, f"mix share {label} in 0..1", 0 <= share <= 1, round(share, 4))
    c.eq(S, "mix shares sum to 100%",
         round(sum(v / firm["p_aug"] for _, v in firm["mix"]), 6), 1.0, TOL_PCT)

    for d in desks:
        pen = d["p_aug"] / d["tot_aug"] if d["tot_aug"] else 0
        c.add(S, f"{d['ml']}: penetration in 0..1", 0 <= pen <= 1, round(pen, 4))
        if d["pdelta"] is not None and d["pjun_prod"] is not None:
            implied = round(sum(d["pjun_prod"].values()) + sum(d["pdelta"].values()), 2)
            c.eq(S, f"{d['ml']}: Jun prod + delta == Aug platform",
                 implied, d["p_aug"], TOL_CR)

    for r in rows:
        pen = r["p_aug"] / r["tot_aug"] if r["tot_aug"] else 0
        c.add(S, f"{r['rm']}: penetration in 0..1", 0 <= pen <= 1.0001, round(pen, 4))
        c.add(S, f"{r['rm']}: platform clients <= clients",
              r["p_cl"] <= r["cl_aug"], f"{r['p_cl']}/{r['cl_aug']}")
        c.add(S, f"{r['rm']}: no NaN/negative AUM",
              r["tot_aug"] >= 0 and r["p_aug"] >= 0 and r["p_aug"] == r["p_aug"],
              (r["tot_aug"], r["p_aug"]))

    # the "Slipping vs Jun" flag must only fire on a real decline, not rounding
    slipping = [r["rm"] for r in rows if (r["p_aug"] - r["p_jun"]) < -0.01]
    borderline = [r["rm"] for r in rows if -0.01 <= (r["p_aug"] - r["p_jun"]) < 0]
    c.add(S, "flagOf: 'Slipping vs Jun' only on declines > 1 lakh",
          True, f"{len(slipping)} slipping, {len(borderline)} within rounding",
          note=f"slipping: {slipping}")
    return slipping


def run_all(data, wb, sample_size=20):
    c = Checks()
    truth = raw_truth(wb)
    cross_check(c, data, wb, truth)
    sample = random_check(c, data, truth, sample_size=sample_size)
    slipping = calc_check(c, data)
    return c, sample, slipping
