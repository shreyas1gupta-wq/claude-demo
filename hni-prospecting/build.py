#!/usr/bin/env python3
"""Assemble the HNI Prospecting dashboard.

    python3 hni-prospecting/build.py

Takes the authored page and injects the figure sprite from the illustration
set, so the artwork stays authored in one place and the dashboard ships
self-contained. Standard library only.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGE = os.path.join(HERE, "page.html")
SPRITE = os.path.join(ROOT, "hni-prospecting-art", "figures-inline.html")
OUT = os.path.join(HERE, "HNI_Prospecting_Dashboard.html")

# Every symbol the page references, so a renamed or dropped figure fails the
# build rather than rendering an empty box.
REQUIRED = ["fig-hero", "fig-promoter", "fig-executive", "fig-professional",
            "fig-inheritor", "fig-founder", "fig-engine", "fig-trust",
            "fig-watchouts", "fig-week"]


def main():
    page = open(PAGE).read()
    sprite = open(SPRITE).read()

    if "<!--SPRITE-->" not in page:
        sys.exit("page.html has no <!--SPRITE--> placeholder")

    missing = [s for s in REQUIRED if f'id="{s}"' not in sprite]
    if missing:
        sys.exit(f"sprite is missing symbols: {missing}")

    # static <use> in the markup, plus the ids the persona data injects at
    # runtime -- a JS-only reference would otherwise skip this check entirely
    used = set(re.findall(r'<use href="#([\w-]+)"', page))
    used |= set(re.findall(r'fig:"([\w-]+)"', page))
    undefined = sorted(u for u in used if f'id="{u}"' not in sprite)
    if undefined:
        sys.exit(f"page references symbols the sprite does not define: {undefined}")

    html = page.replace("<!--SPRITE-->", sprite.rstrip() + "\n")
    with open(OUT, "w") as fh:
        fh.write(html)

    print(f"wrote {os.path.relpath(OUT)}  {len(html):,} bytes")
    unused = sorted(set(REQUIRED) - used)
    print(f"  {len(re.findall(r'<section class=.slide', html))} slides, "
          f"{len(used)}/{len(REQUIRED)} figures referenced"
          + (f", unused: {unused}" if unused else ", all used"))


if __name__ == "__main__":
    main()
