#!/usr/bin/env python3
"""Assemble the India feasibility report: the JSONs produced by the analysis -> report/index.html.
Reuses the design system and chart helpers from ../overview/template.html.
Run:  python3 build_india_report.py
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REP = HERE / "report"


def load(name):
    p = HERE / name
    return json.loads(p.read_text()) if p.exists() else None


def main():
    data = {
        "checks": load("data/india_checks.json"),
        "costs": load("india_cost_table.json"),
        "results": load("india_results.json"),
        "tuning": load("india_tuning.json"),
        "overlay": load("india_overlay.json"),
    }
    ov = (HERE.parent / "overview" / "template.html").read_text()
    style = ov[ov.index("<style>"): ov.index("</style>") + 8]
    helpers = ov[ov.index("const $ = (s, r=document)"): ov.index("/* ============================== render ============================== */")]
    tpl = (REP / "template.html").read_text()
    html = (tpl.replace("__SHARED_STYLE__", style).replace("__SHARED_HELPERS__", helpers)
               .replace("__DATA_JSON__", json.dumps(data, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")))
    (REP / "index.html").write_text(html)
    print(f"wrote {REP/'index.html'} ({(REP/'index.html').stat().st_size//1024} KB)")


if __name__ == "__main__":
    main()
