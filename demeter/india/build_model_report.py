#!/usr/bin/env python3
"""Assemble the India model specification page. Run: python3 build_model_report.py"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REP = HERE / "model_report"


def main():
    data = {"model": json.loads((HERE / "india_model_results.json").read_text()),
            "vrp": json.loads((HERE / "india_vrp.json").read_text()),
            "costs": json.loads((HERE / "india_cost_table.json").read_text()),
            "checks": json.loads((HERE / "data" / "india_checks.json").read_text())}
    ov = (HERE.parent / "overview" / "template.html").read_text()
    style = ov[ov.index("<style>"): ov.index("</style>") + 8]
    helpers = ov[ov.index("const $ = (s, r=document)"): ov.index("/* ============================== render ============================== */")]
    html = ((REP / "template.html").read_text().replace("__SHARED_STYLE__", style)
            .replace("__SHARED_HELPERS__", helpers)
            .replace("__DATA_JSON__", json.dumps(data, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")))
    (REP / "index.html").write_text(html)
    print(f"wrote {REP/'index.html'} ({(REP/'index.html').stat().st_size//1024} KB)")


if __name__ == "__main__":
    main()
