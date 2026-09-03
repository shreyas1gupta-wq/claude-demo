"""The challenger registry's CI enforcement — the adaptivity-admission law has teeth."""
import shutil
import subprocess
import sys
from pathlib import Path

CONFIG = Path(__file__).resolve().parents[1] / "config"


def _run_validator(tmpdir: Path) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(tmpdir / "validator.py")],
                          capture_output=True, text=True)


def _copy_config(tmp_path: Path) -> Path:
    d = tmp_path / "config"
    shutil.copytree(CONFIG, d, ignore=shutil.ignore_patterns("__pycache__"))
    return d


def test_registry_loads_clean_as_shipped(tmp_path):
    d = _copy_config(tmp_path)
    r = _run_validator(d)
    assert r.returncode == 0, r.stdout + r.stderr


def test_online_lane_refused_without_review_gate(tmp_path):
    d = _copy_config(tmp_path)
    ch = (d / "challengers.yaml").read_text().replace("lane: challenger", "lane: online", 1)
    (d / "challengers.yaml").write_text(ch)
    r = _run_validator(d)
    assert r.returncode != 0 and "review-gated" in r.stdout


def test_missing_registry_file_refused(tmp_path):
    d = _copy_config(tmp_path)
    (d / "challengers.yaml").unlink()
    r = _run_validator(d)
    assert r.returncode != 0 and "must be laned" in r.stdout


def test_unknown_lane_refused(tmp_path):
    d = _copy_config(tmp_path)
    ch = (d / "challengers.yaml").read_text().replace("lane: shadow", "lane: production", 1)
    (d / "challengers.yaml").write_text(ch)
    r = _run_validator(d)
    assert r.returncode != 0 and "not in" in r.stdout
