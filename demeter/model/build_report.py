#!/usr/bin/env python3
"""Assemble the pass-2 replication-study report: results/*.json + dev_results/* -> report/report_data.json -> report/index.html.
Usage: python build_report.py [--final final_model] [--fewtrades final_model_fewtrades] [--overview-url URL] [--headline TEXT]
Read-only: it never runs evaluate.py / oos_final.py and never writes into results/ or dev_results/.
Loader rule (REPORT_SPEC.md): for each signals/*.py prefer results/<stem>_p2.json, else results/<stem>.json; a stem with
no out-of-sample file appears in the DEV gauntlet only."""
from __future__ import annotations
import argparse, ast, json, re, sys
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
RES, REP, DEV, SIG = HERE / "results", HERE / "report", HERE / "dev_results", HERE / "signals"
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402
import verify_tools as VT  # noqa: E402
from gate_check import check as gate_check  # noqa: E402
from dev_summary import DEFAULT as DEV_PANEL  # noqa: E402  (name, lens) panel definition, one source of truth

# tags that mark a variant/cost-row/daily file rather than a candidate of its own
TAGS = ("_verify", "_oos2005", "_es", "_nq", "_fin40", "_daily", "_final", "_p2", "_c240", "_s690")
SKIP = {"demeter_inference", "panel_summary", "critic", "pass2_summary"}
GENERATED = "2026-09-12"
COST_LABELS = {"c240": "2 bp / 40 bp", "headline": "3 bp / 60 bp", "s690": "6 bp / 90 bp"}


def load(stem):
    p = RES / f"{stem}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def dev_load(stem):
    p = DEV / f"{stem}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def clean(o):
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (float, np.floating)):
        return None if (np.isnan(o) or np.isinf(o)) else float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, pd.Timestamp):
        return o.strftime("%Y-%m-%d")
    return o


def docstring(module_rel):
    p = HERE / module_rel
    if not p.exists():
        return ""
    try:
        return ast.get_docstring(ast.parse(p.read_text(encoding="utf-8"))) or ""
    except Exception:
        return ""


# ------------------------------------------------------------------ markdown helpers (all text comes from files)
def md_sections(text):
    """{heading line without '## ' : body} for every level-2 heading."""
    out, cur, buf = {}, None, []
    for line in text.splitlines():
        if line.startswith("## "):
            if cur is not None:
                out[cur] = "\n".join(buf).strip()
            cur, buf = line[3:].strip(), []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        out[cur] = "\n".join(buf).strip()
    return out


def md_section(text, prefix):
    for k, v in md_sections(text).items():
        if k.lower().startswith(prefix.lower()):
            return f"## {k}\n\n{v}"
    return ""


def md_table(block):
    """First pipe table in a block -> (header cells, [row cells])."""
    rows = [l.strip() for l in block.splitlines() if l.strip().startswith("|")]
    if len(rows) < 2:
        return [], []
    cells = lambda l: [c.strip() for c in l.strip().strip("|").split("|")]
    head = cells(rows[0])
    body = [cells(r) for r in rows[2:] if not set(r.replace("|", "").strip()) <= {"-", " "}]
    return head, [r for r in body if any(c for c in r)]


def md_list(block):
    """Bullets / numbered items in a block, continuation lines folded in."""
    items, cur = [], None
    for line in block.splitlines():
        m = re.match(r"^\s*(?:[*-]|\d+\.)\s+(.*)$", line)
        if m:
            if cur:
                items.append(cur.strip())
            cur = m.group(1)
        elif cur is not None and line.strip():
            cur += " " + line.strip()
        elif cur is not None:
            items.append(cur.strip())
            cur = None
    if cur:
        items.append(cur.strip())
    return items


# ------------------------------------------------------------------ verification digest
def parse_digest(path):
    """dev_results/PASS2_VERIFICATION_SUMMARY.md -> {candidate: {lenses, refuted, refuted_by, true_tunables, findings}}."""
    if not path.exists():
        return {}
    hdr = re.compile(r"^(?P<name>[a-z0-9_]+)\s+(?P<lens>L\d)\s+refuted=(?P<ref>\w+)\s+true_tunables=(?P<tt>\S+)\s+oos_range=(?P<rng>.*)$")
    out, cur = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = hdr.match(line.strip())
        if m:
            d = out.setdefault(m.group("name"), {"name": m.group("name"), "lenses": {}})
            tt = m.group("tt")
            rng = m.group("rng").strip()
            cur = {"lens": m.group("lens"), "refuted": m.group("ref") == "True",
                   "true_tunables": (int(tt) if tt.isdigit() else None),
                   "oos_range": (None if rng in ("None", "") else rng),
                   "severe": [], "material": [], "disclose": []}
            d["lenses"][m.group("lens")] = cur
            continue
        f = re.match(r"^\s*\[(SEVERE|MATERIAL|DISCLOSE)\]\s*(.+)$", line)
        if f and cur is not None:
            cur[f.group(1).lower()].append(f.group(2).strip())
    for name, d in out.items():
        ls = d["lenses"]
        order = sorted(ls)
        d["refuted_by"] = [k for k in order if ls[k]["refuted"]]
        d["refuted"] = bool(d["refuted_by"])
        d["verdict"] = ("REFUTED" if d["refuted"] else "holds")
        tt = [ls[k]["true_tunables"] for k in order if ls[k]["true_tunables"] is not None]
        d["true_tunables"] = max(tt) if tt else None
        rng = [ls[k]["oos_range"] for k in order if ls[k]["oos_range"]]
        d["oos_range"] = rng[0] if rng else None
        d["severe"] = [f"{k}: {s}" for k in order for s in ls[k]["severe"]]
        d["material"] = [f"{k}: {s}" for k in order for s in ls[k]["material"]]
        d["disclose"] = [f"{k}: {s}" for k in order for s in ls[k]["disclose"]]
        first = (d["refuted_by"] or order)
        src = ls[first[0]] if first else None
        d["decisive"] = ((src["severe"] or src["material"] or src["disclose"] or [None])[0] if src else None)
        d["decisive_lens"] = first[0] if first else None
        # verifier-corrected count of DEV parameter sets, where a verifier stated one
        sets = [int(x) for x in re.findall(r"(\d{3,5})\s+distinct parameter (?:sets|combinations)",
                                           " ".join(d["severe"] + d["material"] + d["disclose"]))]
        d["dev_param_sets_verified"] = max(sets) if sets else None
    return out


# ------------------------------------------------------------------ rules ladder, generated from the docstring
def rules_ladder(module_rel):
    """Numbered rules out of a signal's docstring; if the file defers to another signal ('Identical logic to `x`'),
    that file's numbered rules are the base ladder and this file's bullets are appended as deltas."""
    doc = docstring(module_rel)
    if not doc:
        return []

    def numbered(text):
        items, cur = [], None
        for line in text.splitlines():
            m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
            if m and re.match(r"^[A-Z][A-Z \-]", m.group(2)):
                if cur:
                    items.append(cur)
                cur = {"n": m.group(1), "text": m.group(2).strip()}
            elif cur is not None and line.strip() and line.startswith(" "):
                cur["text"] += " " + line.strip()
            elif cur is not None and not line.strip():
                items.append(cur)
                cur = None
        if cur:
            items.append(cur)
        return items

    def split_title(t):
        m = re.match(r"^([A-Z][A-Za-z0-9 \-/+]*(?:\([^)]*\))?)\.\s+(.*)$", t)
        return (m.group(1).strip(), m.group(2).strip()) if m else (None, t)

    steps = []
    base = numbered(doc)
    if len(base) < 2:  # this file defers to another signal file
        for ref in re.findall(r"`([a-z0-9_]+)`", doc):
            if (SIG / f"{ref}.py").exists() and ref != Path(module_rel).stem:
                for it in numbered(docstring(f"signals/{ref}.py")):
                    title, body = split_title(it["text"])
                    steps.append({"n": it["n"], "title": title, "body": body, "kind": "rule", "source": f"signals/{ref}.py"})
                break
        for i, b in enumerate(re.findall(r"^\s*\*\s+(.*)$", doc, flags=re.M), 1):
            steps.append({"n": f"Δ{i}", "title": "Low-turnover change", "body": b.strip(), "kind": "delta",
                          "source": module_rel})
    else:
        for it in base:
            title, body = split_title(it["text"])
            steps.append({"n": it["n"], "title": title, "body": body, "kind": "rule", "source": module_rel})
    return steps


def module_constants(module_rel):
    """Structural constants declared in the signal file (and in the file it defers to)."""
    out, seen = [], set()
    paths = [module_rel]
    doc = docstring(module_rel)
    for ref in re.findall(r"`([a-z0-9_]+)`", doc):
        if (SIG / f"{ref}.py").exists() and ref != Path(module_rel).stem:
            paths.append(f"signals/{ref}.py")
    for rel in paths:
        p = HERE / rel
        if not p.exists():
            continue
        for c in VT.constants(p):
            if c["name"] in seen or len(c["value"]) > 24:
                continue
            seen.add(c["name"])
            out.append(c)
    return out


# ------------------------------------------------------------------ series / summaries
def monthly_from_daily(file_stem, start=None):
    p = RES / f"{file_stem}_daily.csv"
    if not p.exists():
        return None
    d = pd.read_csv(p, parse_dates=["date"]).set_index("date")
    if start:
        d = d.loc[start:]
    if d.empty:
        return None
    m = (1 + d["ret"]).resample("ME").prod() - 1
    mkt = (1 + d["x"] + d["rf"]).resample("ME").prod() - 1
    cash = (1 + d["rf"]).resample("ME").prod() - 1
    lev = d["lev"].resample("ME").mean()
    eq, eqm, eqc = (1 + m).cumprod(), (1 + mkt).cumprod(), (1 + cash).cumprod()
    return {"months": [i.strftime("%Y-%m") for i in m.index], "model": list(m * 100), "spy": list(mkt * 100),
            "eq_model": list(eq * 1000), "eq_spy": list(eqm * 1000), "eq_cash": list(eqc * 1000),
            "dd_model": list((eq / eq.cummax() - 1) * 100), "dd_spy": list((eqm / eqm.cummax() - 1) * 100), "avg_lev": list(lev)}


def position_changes(file_stem, start, end=None):
    """Every out-of-sample position change, read off the daily file — not hard-coded."""
    p = RES / f"{file_stem}_daily.csv"
    if not p.exists():
        return None
    d = pd.read_csv(p, parse_dates=["date"])
    o = d[d["date"] >= start] if start else d
    if end:
        o = o[o["date"] <= end]
    if o.empty:
        return None
    prev = o["lev"].shift()
    ch = o[(prev.notna()) & (o["lev"] != prev)]
    rows = [{"date": r["date"].strftime("%Y-%m-%d"), "to": float(r["lev"]), "from": float(prev.loc[i])}
            for i, r in ch.iterrows()]
    tail = o[o["date"] >= (ch["date"].max() if len(ch) else o["date"].min())]
    return {"changes": rows, "n": len(rows),
            "since_last_change": {"date": (rows[-1]["date"] if rows else None), "n_days": int(len(tail)),
                                  "pct_cash": float((tail["lev"] == 0).mean() * 100)}}


KEYS = ["annualized_return_pct", "annualized_std_dev", "sharpe", "sortino", "calmar", "max_drawdown_pct", "max_drawdown_daily_pct",
        "pct_positive_months", "beta_to_spy", "correlation_to_spy", "alpha_ann_jensen_pct", "up_capture_pct", "down_capture_pct",
        "pct_days_cash", "pct_days_levered_gt1", "avg_leverage", "avg_leverage_when_invested", "n_position_changes",
        "position_changes_per_year", "turnover_notional_per_year", "total_cost_drag_pct_annual", "avg_invested_spell_days",
        "median_invested_spell_days", "pct_days_positive_return", "quad_loss_avoidance_pct", "quad_gain_sacrifice_pct",
        "quad_amplified_gains_pct", "quad_amplified_losses_pct", "quad_days", "growth_of_1000", "total_growth_pct",
        "start_date", "end_date", "n_months", "spy_annualized_return_pct", "spy_max_drawdown_pct", "spy_sharpe", "spy_annualized_std_dev"]


def summarize(r, file_stem=None):
    o, dv, fu = r["windows"].get("oos", {}), r["windows"].get("dev", {}), r["windows"].get("full", {})
    cmp = r.get("demeter_comparison_oos", {})
    pick = lambda w: {k: w.get(k) for k in KEYS}
    return {"name": r["name"], "file_stem": file_stem, "family": r.get("family"), "hypothesis": r.get("hypothesis"),
            "module": r.get("module"), "params": r.get("params"), "asset": r.get("asset"), "cost_bps": r.get("cost_bps"),
            "financing_spread_bps": r.get("financing_spread_bps"),
            "oos": pick(o), "dev": pick(dv), "full": pick(fu), "lookahead_ok": (r.get("lookahead_check") or {}).get("ok"),
            "n_lookahead_cutoffs": len(((r.get("lookahead_check") or {}).get("details") or [])),
            "corr_with_demeter": cmp.get("monthly_corr_model_vs_demeter"), "rmse_vs_demeter_pct": cmp.get("monthly_rmse_pct"),
            "same_sign_pct": cmp.get("same_sign_months_pct"), "leverage_distribution_oos": r.get("leverage_distribution_oos"),
            "cost_sensitivity_oos": r.get("cost_sensitivity_oos"), "param_sensitivity_oos": r.get("param_sensitivity_oos"),
            "param_sensitivity_dev": r.get("param_sensitivity_dev"), "sub_periods": r.get("sub_periods"),
            "yearly_oos": cmp.get("yearly"), "monthly_oos": cmp.get("monthly"), "demeter_stats": cmp.get("demeter"),
            "spy_stats_demeter_data": cmp.get("spy_demeter_data"), "spy_stats_model_data": cmp.get("spy_model_data"),
            "window": cmp.get("window"), "n_params": len(r.get("params") or {})}


def cost_rows(file_stem):
    out = {}
    for label, suffix in (("c240", "_c240"), ("headline", ""), ("s690", "_s690")):
        r = load(file_stem + suffix)
        if not r:
            out[label] = None
            continue
        o = r["windows"].get("oos", {})
        out[label] = {"cost_bps": r.get("cost_bps"), "fin_bps": r.get("financing_spread_bps"),
                      "cagr_pct": o.get("annualized_return_pct"), "sharpe": o.get("sharpe"),
                      "max_drawdown_pct": o.get("max_drawdown_pct"), "pct_days_cash": o.get("pct_days_cash"),
                      "position_changes_per_year": o.get("position_changes_per_year")}
    return out


# ------------------------------------------------------------------ pass-2 block
def look_log_labels(log_md, stems):
    """Who was looked at, and when — parsed from results/OOS_LOOK_LOG.md."""
    labels, looked = {}, []
    rows = [l for l in log_md.splitlines() if l.strip().startswith("|")][2:]
    for stem in stems:
        lab, when = None, None
        for row in rows:
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) < 4 or stem not in cells[1]:
                continue
            if "signal look" in cells[3]:
                lab, when = "pass 2", cells[0]
                break
            if "not a new look" in cells[3] or "pass-1" in cells[1]:
                lab = lab or "pass 1"
        labels[stem] = lab
        if lab == "pass 2":
            looked.append((stem, when))
    return labels, looked


def dev_table(verif, oos_labels):
    rows = []
    for name, lens in DEV_PANEL:
        r = dev_load(name)
        if not r:
            continue
        g = gate_check(str(DEV / f"{name}.json"))
        ret_p = DEV / f"{name}_RETURN.json"
        ret = json.loads(ret_p.read_text(encoding="utf-8")) if ret_p.exists() else {}
        vp = DEV / f"{name}_VERIFY.json"
        vj = json.loads(vp.read_text(encoding="utf-8")) if vp.exists() else {}
        w = r["windows"].get("dev_1990") or {}
        w5 = r["windows"].get("dev_1950") or {}
        s690 = ((r.get("windows_stress_cost_6_90") or {}).get("dev_1990") or {})
        c240 = ((r.get("windows_cost_2_40") or {}).get("dev_1990") or {})
        st = r.get("stress_episodes") or {}
        eras = {k: v for k, v in (r.get("eras") or {}).items()}
        live = [v for v in eras.values() if v["pct_days_cash"] <= 99]
        v = verif.get(name) or {}
        panel = "pass2" if lens.startswith("lens") else ("reinstated" if name == "vix_vrp" else
                                                         ("incumbent" if name == "final_model_fewtrades" else "pass1"))
        rows.append({
            "name": name, "lens": lens, "panel": panel, "module": r.get("module"), "family": r.get("family"),
            "declared_tunables": r.get("n_tunable_params"), "true_tunables": v.get("true_tunables"),
            "dev_sharpe": w.get("sharpe"), "dev_cagr_pct": w.get("annualized_return_pct"), "dev_maxdd_pct": w.get("max_drawdown_pct"),
            "dev_start": w.get("start_date"), "dev_end": w.get("end_date"),
            "spy_dev_sharpe": w.get("spy_sharpe"), "spy_dev_cagr_pct": w.get("spy_annualized_return_pct"),
            "spy_dev_maxdd_pct": w.get("spy_max_drawdown_pct"), "spy_sharpe_1950": w5.get("spy_sharpe"),
            "changes_per_year": w.get("position_changes_per_year"), "pct_days_cash": w.get("pct_days_cash"),
            "avg_leverage_when_invested": w.get("avg_leverage_when_invested"), "up_capture_pct": w.get("up_capture_pct"),
            "down_capture_pct": w.get("down_capture_pct"), "sharpe_1950": w5.get("sharpe"), "uses_vix": (r.get("signal_coverage") or {}).get("uses_vix"),
            "sharpe_6_90": s690.get("sharpe"), "sharpe_2_40": c240.get("sharpe"),
            "worst_era_dd_pct": min((e["max_dd_pct"] for e in live), default=None),
            "bear_2000_02_pct": (st.get("2000_02_bear") or {}).get("model_total_pct"),
            "gfc_pct": (st.get("2007_09_gfc") or {}).get("model_total_pct"),
            "rec_2009_pct": (st.get("2009_recovery") or {}).get("model_total_pct"),
            "plateau_share": (r.get("plateau_dev_1990") or {}).get("share_within_25pct"),
            "eras": eras, "gates_pass": g["all_pass"], "gates": g["gates"],
            "gates_failed": [k.split("_")[0] for k, gv in g["gates"].items() if not gv["pass"]],
            "verdict": v.get("verdict"), "refuted_by": v.get("refuted_by"), "decisive": v.get("decisive"),
            "decisive_lens": v.get("decisive_lens"), "oos_range": v.get("oos_range"),
            "n_iterations": ret.get("n_iterations"), "dev_param_sets": (v.get("dev_param_sets_verified") or ret.get("n_iterations")),
            "dev_param_sets_corrected": v.get("dev_param_sets_verified") is not None,
            "headline": ret.get("headline"), "biggest_weakness": ret.get("biggest_weakness"),
            "thirds": ((vj.get("subsamples") or {}).get("thirds")), "halves": ((vj.get("subsamples") or {}).get("halves")),
            "lag_test": vj.get("lag_test_dev_1990"), "n_verify_cutoffs": len(((vj.get("causality_12_cutoffs") or {}).get("details") or [])),
            "oos_look": oos_labels.get(name),
        })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--final", default="final_model")
    ap.add_argument("--fewtrades", default="final_model_fewtrades")
    ap.add_argument("--overview-url", default="")
    ap.add_argument("--headline", default="")
    a = ap.parse_args()

    # ---- candidates: one per signal file that has an out-of-sample result (prefer the pass-2 cost basis)
    files = {}
    for p in sorted(SIG.glob("*.py")):
        stem = p.stem
        if stem.startswith("_") or stem in SKIP or any(t in stem for t in TAGS):
            continue
        for cand in (f"{stem}_p2", stem):
            if (RES / f"{cand}.json").exists():
                files[stem] = cand
                break
    cands = {}
    for stem, file_stem in files.items():
        r = load(file_stem)
        if r and "windows" in r:
            c = summarize(r, file_stem)
            c["cost_rows"] = cost_rows(file_stem)
            cands[stem] = c
    if not cands:
        raise SystemExit("no candidate results found")

    # ---- pass-2 evidence
    verif = parse_digest(DEV / "PASS2_VERIFICATION_SUMMARY.md")
    look_md = (RES / "OOS_LOOK_LOG.md").read_text(encoding="utf-8") if (RES / "OOS_LOOK_LOG.md").exists() else ""
    panel_names = [n for n, _ in DEV_PANEL]
    oos_labels, looked = look_log_labels(look_md, sorted(set(panel_names) | set(cands)))
    drows = dev_table(verif, oos_labels)
    summary = json.loads((RES / "pass2_summary.json").read_text(encoding="utf-8")) if (RES / "pass2_summary.json").exists() else {"rows": []}
    by_stem = {}
    for row in summary.get("rows", []):
        s = row["name"][:-3] if row["name"].endswith("_p2") else row["name"]
        by_stem[s] = row
    prereg_md = (HERE / "PREREG.md").read_text(encoding="utf-8") if (HERE / "PREREG.md").exists() else ""
    results_md = (HERE / "RESULTS.md").read_text(encoding="utf-8") if (HERE / "RESULTS.md").exists() else ""
    rsec = md_sections(results_md)
    changed_key = next((k for k in rsec if k.lower().startswith("what changed since pass 1")), None)
    ch_head, ch_rows = md_table(rsec.get(changed_key, "")) if changed_key else ([], [])
    lim_key = next((k for k in rsec if k.lower().startswith("limitations")), None)
    next_key = next((k for k in rsec if k.lower().startswith("next steps")), None)
    lesson_key = next((k for k in rsec if k.lower().startswith("what failed and why")), None)

    # recommended: the incumbent unless a pass-2 candidate meets every acceptance criterion
    accepted = [s for s, row in by_stem.items() if (row.get("acceptance") or {}).get("ALL")]
    rec_key = a.fewtrades if a.fewtrades in cands else next(iter(cands))
    for s in accepted:
        if s in cands and s != a.fewtrades:
            rec_key = s
            break

    pass2 = {
        "dev_table": drows,
        "verification": verif,
        "look_log": look_md,
        "look_log_rows": [[c.strip() for c in l.strip().strip("|").split("|")]
                          for l in look_md.splitlines() if l.strip().startswith("|")][2:],
        "summary": summary,
        "summary_by_stem": by_stem,
        "prereg": {"verification_outcomes": md_section(prereg_md, "Verification outcomes"),
                   "look_budget": md_section(prereg_md, "Outcome of the look budget"),
                   "deviations": md_section(prereg_md, "Deviations")},
        "changed": {"head": ch_head, "rows": ch_rows},
        "limitations": md_list(rsec.get(lim_key, "")) if lim_key else [],
        "next_steps": md_list(rsec.get(next_key, "")) if next_key else [],
        "lessons": md_list(rsec.get(lesson_key, "")) if lesson_key else [],
        "oos_labels": oos_labels,
        "looked": [s for s, _ in looked],
        "looked_when": {s: w for s, w in looked},
        "looked_monthly": {s: (cands[s].get("monthly_oos") if s in cands else None) for s, _ in looked},
        "accepted": accepted,
        "cost_labels": COST_LABELS,
        "position_changes": {},
    }
    for s, _ in looked:
        c = cands.get(s)
        if c:
            pass2["position_changes"][s] = position_changes(c["file_stem"], c["oos"].get("start_date"), c["oos"].get("end_date"))
    lens_rows = [r for r in drows if r["panel"] == "pass2"]
    pass2["counts"] = {
        "new_candidates": len(lens_rows),
        "gate_passers": sum(1 for r in lens_rows if r["gates_pass"]),
        "refuted": sum(1 for r in lens_rows if r["verdict"] == "REFUTED"),
        "verified": sum(1 for r in lens_rows if r["verdict"] == "holds"),
        "refuted_all": sum(1 for r in drows if r["verdict"] == "REFUTED"),
        "panel_rows": len([r for r in drows if r["panel"] in ("pass2", "reinstated", "incumbent")]),
        "new_looks": len(looked),
        "candidates_with_oos": len(cands),
        "dev_cutoffs": max([r["gates"]["G1_causality"].get("n_cutoffs") or 0 for r in drows] or [0]),
        "verify_cutoffs": max([r["n_verify_cutoffs"] for r in drows] or [0]),
        "dev_param_sets_total": sum(r["dev_param_sets"] or 0 for r in lens_rows),
        "verifiers": sum(len((verif.get(r["name"]) or {}).get("lenses") or {}) for r in drows),
    }

    # ---- the recommended model's neighbours, unchanged pass-1 material
    final_key = a.final if a.final in cands else rec_key
    final, few = cands[final_key], cands.get(a.fewtrades)
    rec = cands[rec_key]
    rec_mod = rec["module"] or f"signals/{rec_key}.py"
    if not (HERE / rec_mod).exists():
        rec_mod = f"signals/{rec_key}.py"
    variants = {k: (summarize(v) if v else None) for k, v in
                {"oos2005": load(f"{final_key}_oos2005"), "nq": load(f"{final_key}_nq"),
                 "fin40": load(f"{final_key}_fin40"), "es": load(f"{final_key}_es")}.items()}
    df = E.load_market()
    refs = []
    oos_start = rec["oos"].get("start_date") or "2012-07-01"
    oos_end = rec["oos"].get("end_date") or "2026-01-31"
    for lev in (1.0, 2.0, 3.0):
        m = E.run(df, E.buy_and_hold(df, lev), asset="spx_tr", cost_bps=0.0, start=oos_start, end=oos_end).metrics()
        refs.append({"name": f"Buy & hold {int(lev)}x", "cagr_pct": m["annualized_return_pct"], "max_dd_pct": m["max_drawdown_pct"],
                     "sharpe": m.get("sharpe"), "std": m["annualized_std_dev"]})
    infer = load("demeter_inference") or {}
    inf = {}
    try:
        rows = infer["a_implied_exposure"]["rows"]
        inf["exposure_rows"] = [{"month": r["month"], "strategy": r["strategy"], "spy": r["spy"], "exposure": r.get("exposure"),
                                 "full_cash": r.get("full_cash"), "vix_avg": r.get("vix_avg")} for r in rows]
        inf["full_cash_months"] = infer["a_implied_exposure"].get("full_cash_months")
        inf["rolling12"] = infer["b_rolling"].get("summary_12m")
        inf["rolling36"] = infer["b_rolling"].get("summary_36m")
        inf["down_summary"] = infer["c_down_months"].get("summary")
        inf["down_rows"] = infer["c_down_months"].get("rows")
        inf["mar2020"] = infer["d_daily_inference"].get("mar2020_enter_3x_and_hold")
        inf["days_below_sma200"] = infer["d_daily_inference"].get("days_below_sma200")
        qf = (infer.get("e_summary") or {}).get("quadrant_fingerprint") or {}
        cnt, tot = qf.get("demeter_counts") or {}, qf.get("demeter_total_days")
        inf["quadrant"] = {"counts": cnt, "total_days": tot, "pct_cash": qf.get("demeter_pct_cash"),
                           "pct": {k: (100.0 * v / tot if tot else None) for k, v in cnt.items()}}
    except Exception as ex:
        inf["error"] = repr(ex)
    checks = json.loads((HERE / "data" / "dataset_checks.json").read_text(encoding="utf-8"))

    report = {
        "generated": GENERATED, "pass": 2, "final_key": final_key, "fewtrades_key": a.fewtrades if few else None,
        "rec_key": rec_key, "overview_url": a.overview_url, "headline": a.headline,
        "final": final, "fewtrades": few, "rec": rec,
        "final_rules": docstring(final["module"] or f"signals/{final_key}.py"),
        "fewtrades_rules": docstring(few["module"]) if few and few.get("module") else "",
        "rec_rules_doc": docstring(rec_mod), "rec_ladder": rules_ladder(rec_mod), "rec_constants": module_constants(rec_mod),
        "final_series_oos": monthly_from_daily(final["file_stem"], oos_start),
        "final_series_full": monthly_from_daily(final["file_stem"], "1950-01-01"),
        "rec_series_oos": monthly_from_daily(rec["file_stem"], oos_start),
        "looked_series_oos": {s: monthly_from_daily(cands[s]["file_stem"], oos_start) for s, _ in looked if s in cands},
        "variants": variants,
        "candidates": {k: {kk: vv for kk, vv in v.items() if kk not in ("monthly_oos", "param_sensitivity_dev")} for k, v in cands.items()},
        "bh_refs": refs, "inference": inf, "dataset_checks": checks, "results_md": results_md, "pass2": pass2,
    }
    REP.mkdir(exist_ok=True)
    (REP / "report_data.json").write_text(json.dumps(clean(report), separators=(",", ":")), encoding="utf-8")
    tpl = (REP / "template.html").read_text(encoding="utf-8")
    # one source of truth for the design system: reuse the overview page's token/style block and chart helpers
    ov = (HERE.parent / "overview" / "template.html").read_text(encoding="utf-8")
    style = ov[ov.index("<style>"): ov.index("</style>") + 8]
    helpers = ov[ov.index("const $ = (s, r=document)"): ov.index("/* ============================== render ============================== */")]
    html = (tpl.replace("__SHARED_STYLE__", style).replace("__SHARED_HELPERS__", helpers)
               .replace("__REPORT_JSON__", json.dumps(clean(report), separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")))
    (REP / "index.html").write_text(html, encoding="utf-8")
    print(f"candidates ({len(cands)}): {sorted(cands)}")
    print(f"  files used: {[f'{k} -> results/{v}.json' for k, v in sorted(files.items())]}")
    print(f"  recommended={rec_key} (acceptance.ALL true: {accepted or 'none'}); pass-2 looks: {pass2['looked'] or 'none'}")
    print(f"  DEV panel rows={len(drows)} (lens candidates {pass2['counts']['new_candidates']}, "
          f"gate passers {pass2['counts']['gate_passers']}, refuted {pass2['counts']['refuted']}, verified {pass2['counts']['verified']})")
    print(f"wrote report/index.html ({(REP / 'index.html').stat().st_size // 1024} KB) and report/report_data.json")


if __name__ == "__main__":
    main()
