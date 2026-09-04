#!/usr/bin/env python3
"""Inject analytics.json + stated_figures.json into overview/template.html -> overview/index.html.
Usage: python3 build_overview.py [--model-url URL]"""
import argparse, json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--model-url", default=""); a = ap.parse_args()
    tpl = (HERE / "overview" / "template.html").read_text()
    def js(o):
        return json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    analytics = json.loads((HERE / "analytics.json").read_text())
    stated = json.loads((HERE / "data" / "stated_figures.json").read_text())
    html = (tpl.replace("__ANALYTICS_JSON__", js(analytics)).replace("__STATED_JSON__", js(stated))
               .replace("__MODEL_URL__", json.dumps(a.model_url)))
    out = HERE / "overview" / "index.html"; out.write_text(html)
    print(f"wrote {out} ({out.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
