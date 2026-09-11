"""Turn the extracted figures into the dashboard's DATA structure."""

import collections
import csv
import json
import os
import re

from sources import (DESK_TO_TEAM8, PRODUCTS, TEAM8_PRIMARY_DESK)

# Keep Rohit Onkar and Vishal Rakyan as their own tabs, mirroring the
# workbook's own attribution.  Set False to merge them into one "Other desks"
# tab instead -- the only change needed to collapse them.
SPLIT_SINGLE_RM_DESKS = True
MERGED_DESK_NAME = "Other desks"


def prior_focus(prior_html_path):
    """Per-RM focus from the previous dashboard, used until the MIS carries it.

    The Aug MIS reports focus (SHASTRA + Bond + Edel) only at 8-team level, so
    there is no per-RM source in it.  These figures reconcile exactly to 6 of
    the 8 new team totals, which is why they are trusted as a carry-forward
    rather than discarded.
    """
    with open(prior_html_path) as fh:
        html = fh.read()
    start = html.index("const DATA=") + len("const DATA=")
    data, _ = json.JSONDecoder().raw_decode(html[start:])
    out = {}
    for team in data["teams"]:
        for row in team["rows"]:
            out[row["rm"]] = {
                "f_mar": row.get("f_mar", 0.0), "f_aug": row.get("f_aug", 0.0),
                "f_cl": row.get("f_cl", 0), "cl_focplat": row.get("cl_focplat", 0),
            }
    return out


def mis_focus(path):
    """Per-RM focus from a drop-in file, once the RM-wise split is supplied.

    Expected columns: rm, f_mar, f_aug, f_cl, cl_focplat.
    """
    if not path or not os.path.exists(path):
        return None
    out = {}
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            name = (row.get("rm") or "").strip()
            if not name:
                continue
            out[name] = {
                "f_mar": float(row.get("f_mar") or 0),
                "f_aug": float(row.get("f_aug") or 0),
                "f_cl": int(float(row.get("f_cl") or 0)),
                "cl_focplat": int(float(row.get("cl_focplat") or 0)),
            }
    return out


def _vintage_years(text):
    """'1.8 yr' -> 1.8, for the vintage band; None when the sheet has no value."""
    if not text:
        return None
    m = re.search(r"([\d.]+)", str(text))
    return float(m.group(1)) if m else None


def _remark(rec):
    """A one-line read on the RM, derived from this cycle's own numbers.

    Regenerated rather than carried over: the prior remarks quoted the old
    platform basis and would contradict the figures beside them.  Users can
    still overwrite any remark in the browser.
    """
    pen = rec["p_aug"] / rec["tot_aug"] if rec["tot_aug"] else 0
    d_jun = rec["p_aug"] - rec["p_jun"]
    breadth = sum(1 for p in rec["prod"] if p["aug"] > 0)

    if rec["p_aug"] == 0:
        head = "No platform book yet"
    elif pen >= 0.30:
        head = f"Deep platform desk ({pen * 100:.0f}% of book)"
    elif pen >= 0.15:
        head = f"Building platform share ({pen * 100:.0f}% of book)"
    elif pen >= 0.05:
        head = f"Thin platform share ({pen * 100:.0f}% of book)"
    else:
        head = f"Platform barely started ({pen * 100:.1f}% of book)"

    move = (f"{'+' if d_jun >= 0 else '−'}₹{abs(d_jun):.1f}Cr since Jun"
            if abs(d_jun) >= 0.01 else "flat vs Jun")

    tail = []
    if rec["new_ja"]:
        tail.append(f"{rec['new_ja']} new client{'s' if rec['new_ja'] != 1 else ''} since Jun")
    if rec["p_aug"] > 0 and breadth == 1:
        only = next(p["name"] for p in rec["prod"] if p["aug"] > 0)
        tail.append(f"single-product ({only}) — widen the platform mix")
    elif rec["p_aug"] == 0 and rec["tot_aug"] >= 10:
        tail.append(f"₹{rec['tot_aug']:.0f}Cr book with nothing on platform — priority")
    if not rec["f_aug"]:
        tail.append("no focus product yet")

    return f"{head}, {move}" + ("; " + "; ".join(tail) if tail else "") + "."


def build_records(roster, ml, ml_notes, actuals, platform, buckets, sheets,
                  focus_map, focus_basis):
    """One record per RM, in the shape the dashboard's card() renders."""
    records = {}
    for rm, meta in roster.items():
        act = actuals.get(rm, {})
        sheet = sheets.get(rm, {})
        focus = focus_map.get(rm, {})

        prod = []
        for raw_name, label in PRODUCTS:
            prod.append({
                "name": label,
                "aug": round(platform["prod_aum"].get((rm, raw_name), 0.0), 2),
                "cl": platform["prod_cl"].get((rm, raw_name), 0),
            })

        rec = {
            "rm": rm,
            "vintage": sheet.get("vintage"),
            "vintage_yr": _vintage_years(sheet.get("vintage")),
            "cl_mar": sheet.get("cl_mar"),
            "cl_jun": sheet.get("cl_jun"),
            "cl_aug": act.get("cl_aug", 0),
            "new_ja": sheet.get("new_ja", 0) or 0,
            "new_aum": round(sheet.get("new_aum", 0.0) or 0.0, 2),
            "g50": buckets["g50"].get(rm, 0),
            "l50": buckets["l50"].get(rm, 0),
            "tot_mar": sheet.get("tot_mar", 0.0) or 0.0,
            "tot_jun": sheet.get("tot_jun", 0.0) or 0.0,
            "tot_aug": round(act.get("tot_aug", 0.0), 4),
            "p_mar": meta["p_mar"] or 0.0,
            "p_jun": meta["p_jun"] or 0.0,
            "p_aug": round(act.get("p_aug", 0.0), 2),
            "p_cl": platform["clients"].get(rm, 0),
            "prod": prod,
            "core_pos": sheet.get("core_pos", sum(1 for p in prod if p["aug"] > 0)),
            "recon_uplift": round(platform["recon_uplift"].get(rm, 0.0), 2),
            "f_mar": focus.get("f_mar", 0.0),
            "f_aug": focus.get("f_aug", 0.0),
            "f_cl": focus.get("f_cl", 0),
            "cl_focplat": focus.get("cl_focplat", 0),
            "ml": ml[rm],
            "ml_src": ml_notes[rm],
            "team_sheet": sheet.get("team_sheet"),
            "no_team_sheet": rm not in sheets,
        }
        rec["remark"] = _remark(rec)
        records[rm] = rec
    return records


def build_desks(records, focus_team8, product_deltas):
    """Group RMs into market-leader desks and rank them by platform AUM."""
    grouped = collections.defaultdict(list)
    for rec in records.values():
        grouped[rec["ml"]].append(rec)

    # Focus residual: what the MIS reports for an 8-team group, less what the
    # per-RM figures account for.  Parked on the group's primary desk and
    # rendered as "unattributed at RM level" rather than spread on a guess.
    residual, team8_ctx = {}, {}
    for team8, figures in focus_team8.items():
        primary = TEAM8_PRIMARY_DESK[team8]
        # primary market leader first, matching how the MIS names the team
        member_desks = [primary] + sorted(
            d for d, t in DESK_TO_TEAM8.items() if t == team8 and d != primary)
        covered = sum(r["f_aug"] for r in records.values()
                      if DESK_TO_TEAM8.get(r["ml"]) == team8)
        gap = round(figures["actual"] - covered, 2)
        team8_ctx[team8] = {
            "actual": figures["actual"], "goal": figures["goal"],
            "covered": round(covered, 2),
            # how the team is named in the MIS's own 8-team focus block
            "label": team8 if len(member_desks) == 1 else " + ".join(member_desks),
            "desks": len(member_desks),
        }
        if abs(gap) >= 0.005:
            residual[TEAM8_PRIMARY_DESK[team8]] = gap

    if not SPLIT_SINGLE_RM_DESKS:
        merged = []
        for name in list(grouped):
            if name not in DESK_TO_TEAM8:
                merged += grouped.pop(name)
        if merged:
            grouped[MERGED_DESK_NAME] = merged

    desks = []
    for name, rows in grouped.items():
        rows.sort(key=lambda r: (-r["p_aug"], -r["tot_aug"], r["rm"]))
        unattr = residual.get(name, 0.0)
        team8 = DESK_TO_TEAM8.get(name)
        desks.append({
            "ml": name,
            "rms": len(rows),
            "tot_mar": round(sum(r["tot_mar"] for r in rows), 2),
            "tot_jun": round(sum(r["tot_jun"] for r in rows), 2),
            "tot_aug": round(sum(r["tot_aug"] for r in rows), 4),
            "cl_aug": sum(r["cl_aug"] for r in rows),
            "g50": sum(r["g50"] for r in rows),
            "l50": sum(r["l50"] for r in rows),
            "new_ja": sum(r["new_ja"] for r in rows),
            "p_mar": round(sum(r["p_mar"] for r in rows), 2),
            "p_jun": round(sum(r["p_jun"] for r in rows), 2),
            "p_aug": round(sum(r["p_aug"] for r in rows), 2),
            "p_cl": sum(r["p_cl"] for r in rows),
            "f_aug": round(sum(r["f_aug"] for r in rows) + unattr, 2),
            "f_unattr": unattr,
            "f_goal": focus_team8.get(team8, {}).get("goal") if team8 else None,
            "team8": team8,
            "team8_focus": team8_ctx.get(team8),
            "pdelta": product_deltas.get(name, {}).get("delta"),
            "pjun_prod": product_deltas.get(name, {}).get("jun"),
            "rows": rows,
        })

    desks.sort(key=lambda d: (-d["p_aug"], -d["tot_aug"], d["ml"]))
    for i, desk in enumerate(desks, 1):
        desk["rank"] = i
    return desks


def build_firm(desks, records, buckets, platform, series, focus_firm, focus_basis):
    mix_by_label = {label: round(platform["firm_prod"].get(raw, 0.0), 2)
                    for raw, label in PRODUCTS}
    return {
        "tot_aug": round(sum(d["tot_aug"] for d in desks), 4),
        "p_aug": round(sum(d["p_aug"] for d in desks), 2),
        "f_aug": focus_firm["actual"],
        "f_goal": focus_firm["goal"],
        "focus_basis": focus_basis,
        "cl_aug": sum(d["cl_aug"] for d in desks),
        "households": buckets["households"],
        "ge_1cr_hh": buckets["ge_1cr_households"],
        "ge_1cr_acct": buckets["ge_1cr_accounts"],
        "g50": sum(d["g50"] for d in desks),
        "l50": sum(d["l50"] for d in desks),
        "p_cl": sum(d["p_cl"] for d in desks),
        "p_cl_live": platform["live_core"],
        "p_mar": round(sum(d["p_mar"] for d in desks), 2),
        "p_jun": round(sum(d["p_jun"] for d in desks), 2),
        "rms": len(records),
        "teams": len(desks),
        "trend": series["trend"],
        "mix": [[label, mix_by_label[label]] for _, label in PRODUCTS],
        "all_products": 601.39,
        "recon_uplift": round(sum(platform["recon_uplift"].values()), 2),
    }
