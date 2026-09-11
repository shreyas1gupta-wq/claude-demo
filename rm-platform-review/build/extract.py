"""Pull the dashboard's figures out of the Aug-31 MIS workbook.

Everything here reads either a raw data sheet (`aum`, `platform`) or a
per-RM block that was verified live.  Nothing reads a block listed in
sources.STALE_BLOCKS.
"""

import collections

from sources import (GE_1CR_BUCKETS, MANUAL_ML, PRODUCTS, SUB_50L_BUCKETS,
                     TEAM_SHEETS)

# raw `aum` columns
AUM_RM, AUM_TOTAL, AUM_USERTYPE, AUM_BUCKET, AUM_HHPRIMARY = 12, 26, 27, 28, 30
AUM_HHAUM = 31
# raw `platform` columns
PL_CLIENT, PL_PRODUCT, PL_LATEST = 1, 5, 12
PL_RM, PL_LEAD, PL_CORE, PL_FIRST = 19, 20, 21, 22


def _is_client(row):
    """`aum` carries prospects too; only user_type 'client*' rows are clients."""
    return str(row.get(AUM_USERTYPE, "")).startswith("client")


def roster(wb):
    """The 73 HNI RMs, with the consolidated desk name the workbook shows."""
    pc = wb.sheet("Platform Charts (RM)")
    out = {}
    for r in range(5, 78):
        if r in pc and pc[r].get(1):
            out[pc[r][1]] = {
                "charts_team": pc[r].get(2),
                "p_mar": pc[r].get(6, 0.0),   # period-end actual, no live source
                "p_jun": pc[r].get(7, 0.0),   # period-end actual, no live source
            }
    return out


def market_leaders(wb, names):
    """13-ML attribution per RM, plus a note on how each was resolved."""
    sig = wb.sheet("rm signals")
    by_rm = {sig[r].get(2): sig[r].get(1) for r in sig if r > 1}
    out, notes = {}, {}
    for rm in names:
        if rm in by_rm and by_rm[rm]:
            out[rm], notes[rm] = by_rm[rm], "rm signals.market_leader"
        else:
            out[rm], notes[rm] = MANUAL_ML[rm]
    return out, notes


def aug_actuals(wb):
    """Per-RM Aug-31 AUM / clients / platform from 'Calculation SHeet'.

    Its cols B and D were repointed to SUMIFS over `aum` and `platform`
    (Validation item 31), so this ties to the firm exactly, unlike
    'Platform Charts' col C which is rounded per RM.
    """
    cs = wb.sheet("Calculation SHeet")
    out = {}
    for r in range(2, 82):
        if r in cs and cs[r].get(1):
            out[cs[r][1]] = {
                "tot_aug": cs[r].get(2, 0.0),
                "cl_aug": cs[r].get(3, 0),
                "p_aug": cs[r].get(4, 0.0),
            }
    return out


def platform_detail(wb):
    """Per-RM core-4 platform: AUM and deduplicated client counts, by product.

    `is_first_core_client_for_rm` (col V) is the workbook's own first-occurrence
    dedup flag, added in Validation item 26 to replace an array formula that
    returned 0 in desktop Excel.  Summing it gives 523 firm-wide.
    """
    pl = wb.sheet("platform")
    aum = collections.defaultdict(float)
    prod_aum = collections.defaultdict(float)
    prod_cl = collections.defaultdict(set)
    clients = collections.Counter()
    by_lead = collections.defaultdict(float)
    firm_prod = collections.defaultdict(float)
    recon_uplift = collections.defaultdict(float)
    all_core, live_core = set(), set()

    for r, row in pl.items():
        if r == 1 or row.get(PL_CORE) != 1:
            continue
        rm = row.get(PL_RM, "")
        product = row.get(PL_PRODUCT, "")
        value = row.get(PL_LATEST, 0.0) or 0.0
        client = row.get(PL_CLIENT)

        aum[rm] += value
        prod_aum[(rm, product)] += value
        prod_cl[(rm, product)].add(client)
        clients[rm] += row.get(PL_FIRST, 0)
        by_lead[row.get(PL_LEAD, "")] += value
        firm_prod[product] += value
        all_core.add(client)
        if value > 0:
            live_core.add(client)
        # rows 805:843 reconcile CLIENT LEVEL up to the authoritative RM LEVEL
        if str(client).startswith("RECON-"):
            recon_uplift[rm] += value

    return {
        "aum": aum,
        "prod_aum": prod_aum,
        "prod_cl": {k: len(v) for k, v in prod_cl.items()},
        "clients": clients,
        "by_lead": by_lead,
        "firm_prod": dict(firm_prod),
        "recon_uplift": dict(recon_uplift),
        "distinct_core": len(all_core),
        "live_core": len(live_core),
    }


def aum_buckets(wb):
    """Per-RM client counts split at the 50L line, plus firm household figures.

    Taken from raw `aum` rather than the team sheets' E-3 block because E-3
    only covers the 8 sheets, missing Devyani Dhuri (3 clients) and Madhuri
    Rathod (1).  Verified to reproduce E-3's >=50L figure exactly (1,335).
    """
    au = wb.sheet("aum")
    above = collections.Counter()
    below = collections.Counter()
    clients = collections.Counter()
    firm_total = households = hh_aum = 0.0
    ge_1cr_accounts = ge_1cr_households = 0

    for r, row in au.items():
        if r == 1:
            continue
        firm_total += row.get(AUM_TOTAL, 0.0) or 0.0
        if row.get(AUM_HHPRIMARY) == 1:
            households += 1
            hh_aum += row.get(AUM_HHAUM, 0.0) or 0.0
            if (row.get(AUM_HHAUM, 0.0) or 0.0) >= 1.0:
                ge_1cr_households += 1
        if not _is_client(row):
            continue
        rm = row.get(AUM_RM, "")
        clients[rm] += 1
        if str(row.get(AUM_BUCKET, "")) in SUB_50L_BUCKETS:
            below[rm] += 1
        else:
            above[rm] += 1
        if str(row.get(AUM_BUCKET, "")) in GE_1CR_BUCKETS:
            ge_1cr_accounts += 1

    return {
        "g50": above, "l50": below, "clients": clients,
        "firm_total": round(firm_total, 4),
        "households": int(households),
        "hh_aum": round(hh_aum, 4),
        # Two different, both-correct bases.  The account figure is what READ ME
        # quotes (819); the household figure is what every team sheet's Section A
        # and Team Summary quote (743).  The dashboard shows the household one
        # and says so, to stay consistent with the rest of the workbook.
        "ge_1cr_accounts": ge_1cr_accounts,
        "ge_1cr_households": ge_1cr_households,
    }


def _find_section(sheet, prefix):
    for r in sorted(sheet):
        if str(sheet[r].get(1, "")).startswith(prefix):
            return r
    raise KeyError(prefix)


def _walk(sheet, start, stop_label, name_col=2):
    """Yield rows of a per-RM block until its total row."""
    r = start
    while r in sheet:
        label = str(sheet[r].get(name_col, ""))
        if label == stop_label:
            return
        if label:
            yield sheet[r]
        r += 1


def team_sheet_detail(wb):
    """Per-RM vintage, Mar/Jun book, new clients and the 2b cross-check cells."""
    out = collections.defaultdict(dict)
    for name in TEAM_SHEETS:
        sh = wb.sheet(name)

        # C-1: vintage + Mar-31 / Jun-30 / Aug-31 total AUM
        for row in _walk(sh, _find_section(sh, "C-1") + 3, "TEAM TOTAL"):
            out[row[2]].update(
                vintage=row.get(3), tot_mar=row.get(4, 0.0),
                tot_jun=row.get(5, 0.0), team_sheet=name,
            )
        # C-2: clients won between Jun-30 and Aug-31
        for row in _walk(sh, _find_section(sh, "C-2") + 3, "TEAM TOTAL"):
            out[row[2]].update(new_ja=row.get(4, 0), new_aum=row.get(5, 0.0))
        # Section H: per-product platform AUM (cross-check against raw)
        for row in _walk(sh, _find_section(sh, "H  ·") + 2, "TEAM TOTAL"):
            out[row[2]].update(h_alloc=row.get(3, 0.0), h_hye=row.get(4, 0.0),
                               h_nav=row.get(5, 0.0), h_cop=row.get(6, 0.0),
                               h_total=row.get(7, 0.0), core_pos=row.get(8, 0))
        # 2b: per-RM platform client count (cross-check against raw col V)
        for row in _walk(sh, _find_section(sh, "2b ·") + 2, "ML TOTAL"):
            out[row[2]].update(cl_hh=row.get(11, 0), p_cl_2b=row.get(12, 0))
        # E-3: per-RM client counts at each period end, from the TOTAL rows
        r = _find_section(sh, "E-3  ·") + 3
        while r in sh:
            label = str(sh[r].get(1, ""))
            if not label:
                break
            if label.endswith("— TOTAL"):
                rm = label[: -len("— TOTAL")].strip()
                mar, jun = sh[r].get(3), sh[r].get(4)
                out[rm].update(
                    cl_mar=mar if isinstance(mar, int) else None,
                    cl_jun=jun if isinstance(jun, int) else None,
                )
            r += 1
    return out


def firm_series(wb):
    """Firm platform trend and the desk-level Jun->Aug product deltas."""
    mom = wb.sheet("MoM Trend")
    trend = []
    for r in sorted(mom):
        if r >= 4 and mom[r].get(3) is not None and mom[r].get(1):
            trend.append([mom[r][1], mom[r][3]])

    ts = wb.sheet("Team Summary")
    deltas = {}
    for r in range(36, 49):                      # NEW-B ML rows only, not r49
        if r not in ts or not ts[r].get(1):
            continue
        jun = {"Allocate": ts[r].get(12, 0.0), "Co-Pilot": ts[r].get(13, 0.0),
               "Navigate": ts[r].get(14, 0.0), "YE": ts[r].get(15, 0.0)}
        aug = {"Allocate": ts[r].get(17, 0.0), "Co-Pilot": ts[r].get(18, 0.0),
               "Navigate": ts[r].get(19, 0.0), "YE": ts[r].get(20, 0.0)}
        deltas[ts[r][1]] = {
            "jun": jun, "aug": aug,
            "delta": {k: round(aug[k] - jun[k], 2) for k in aug},
            "aug_total": ts[r].get(21, 0.0),
        }
    return {"trend": trend, "product_deltas": deltas}


def focus_team_actuals(wb):
    """Focus (SHASTRA + Bond + Edel) Q2 goal vs actual, per 8-team group."""
    sh = wb.sheet("H1 & Quarter Progress")
    start = _find_section(sh, "C · FOCUS") + 2
    out, firm = {}, None
    r = start
    while r in sh and sh[r].get(1):
        name = sh[r][1]
        record = {"goal": sh[r].get(2, 0.0), "actual": sh[r].get(3, 0.0)}
        if name == "FIRM":
            firm = record
        else:
            out[name] = record
        r += 1
    return out, firm
