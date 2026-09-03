"""Landing-day machinery: puller auth templates + the census->DSR wiring."""
import subprocess
import sys
from pathlib import Path

import pytest

from quant.stats.dsr import census_n

ROOT = Path(__file__).resolve().parents[1]
PULLERS = ["ingest/pull_india_vix.py", "ingest/pull_ccil.py"]


@pytest.mark.parametrize("puller", PULLERS)
def test_auth_template_emits_then_refuses_overwrite(tmp_path, puller):
    # clean cwd: the skeleton must emit (exit 0) with the two-pass discipline in it
    r1 = subprocess.run([sys.executable, str(ROOT / puller), "--emit-auth-template"],
                        cwd=tmp_path, capture_output=True, text=True)
    assert r1.returncode == 0, r1.stderr + r1.stdout
    files = list(tmp_path.rglob("AUTHENTICATION.md"))
    assert len(files) == 1
    body = files[0].read_text().lower()
    assert "anchor" in body and "before" in body   # anchors-before-values, stated in the skeleton
    # second run: WORM — refuse to overwrite, nonzero exit
    r2 = subprocess.run([sys.executable, str(ROOT / puller), "--emit-auth-template"],
                        cwd=tmp_path, capture_output=True, text=True)
    assert r2.returncode != 0
    assert "refus" in (r2.stdout + r2.stderr).lower()


def test_census_n_reads_register_and_never_shrinks_below_floor():
    n = census_n()
    assert n >= 164        # the census is append-only; this floor rises with the record
    # a Sharpe claim wired through census_n() can never silently undercount trials
