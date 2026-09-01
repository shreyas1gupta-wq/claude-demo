#!/usr/bin/env python3
"""Fixture manifest: sha256 + size + vintage for every raw file under a data root.

Usage: python ingest/manifest.py data/           # writes/updates data/manifest.json
The manifest is the fixture contract (MASTER_PLAN §9): the pipeline reads only manifested files;
a refresh adds a new entry (new vintage), never mutates an old one.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import date
from pathlib import Path


def sha256(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def main(root: str) -> None:
    rootp = Path(root)
    manifest_path = rootp / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    today = date.today().isoformat()
    n_new = 0
    for p in sorted(rootp.rglob("*")):
        # .md files are protocol/documentation (e.g. two-pass authentication notes), not data
        # fixtures — the WORM contract covers raw files only
        if p.is_dir() or p.name == "manifest.json" or p.suffix == ".md":
            continue
        rel = str(p.relative_to(rootp))
        digest = sha256(p)
        if rel in manifest and manifest[rel]["sha256"] == digest:
            continue
        if rel in manifest and manifest[rel]["sha256"] != digest:
            # never silently mutate: an in-place change is a violation, not a refresh
            print(f"ERROR {rel}: content changed under an existing manifest entry - "
                  f"refreshes must land as NEW vintage-named files", file=sys.stderr)
            sys.exit(1)
        manifest[rel] = {"sha256": digest, "bytes": p.stat().st_size, "vintage": today}
        n_new += 1
    manifest_path.write_text(json.dumps(manifest, indent=1, sort_keys=True))
    print(f"manifest: {len(manifest)} files ({n_new} new) -> {manifest_path}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data")
