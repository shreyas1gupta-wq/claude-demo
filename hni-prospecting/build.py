#!/usr/bin/env python3
"""Assemble the HNI Prospecting deck.

    python3 hni-prospecting/build.py

The page is self-contained: every mark is abstract SVG authored inline, so
there is no sprite to inject. The build's job is to check that, and to report
the shape of the result. Standard library only.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "page.html")
OUT = os.path.join(HERE, "HNI_Prospecting_Dashboard.html")


def main():
    page = open(PAGE).read()

    # The human illustrations were removed at the client's request; guard
    # against a reference to the old figure sprite reappearing.
    stray = sorted(set(re.findall(r'<use href="#([\w-]+)"', page)))
    if stray:
        sys.exit(f"page still references sprite symbols: {stray}")
    if "<!--SPRITE-->" in page:
        sys.exit("page still carries the sprite placeholder")

    slides = re.findall(r'<section class="slide" id="(s\d+)">', page)
    navs = re.findall(r'data-t="(s\d+)"', page)
    if slides != navs:
        sys.exit(f"nav order does not match slide order:\n  slides {slides}\n  nav    {navs}")

    # every page must declare a 16:9 stage
    pages = len(re.findall(r'<div class="page', page))
    if pages != len(slides):
        sys.exit(f"{len(slides)} slides but {pages} page stages")

    with open(OUT, "w") as fh:
        fh.write(page)

    print(f"wrote {os.path.relpath(OUT)}  {len(page):,} bytes")
    print(f"  {len(slides)} slides, all 16:9, {len(re.findall(r'<svg', page))} inline SVG marks")
    print(f"  order: {' '.join(slides)}")


if __name__ == "__main__":
    main()
