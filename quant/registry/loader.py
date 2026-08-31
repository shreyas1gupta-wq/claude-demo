"""Registry loader — the single access path to config/*.yaml.

Rules (CONTRACT §10, red-team finding on hardcoded constants):
- No module reads a YAML file or declares a tunable constant directly; everything comes through
  Registry.
- Loading VALIDATES first: a registry violating its own budgets must fail to load, so we run
  config/validator.py's checks before returning any value.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

CONFIG_DIR = Path(__file__).resolve().parents[2] / "config"
FILES = ("mandate", "books", "ladder", "risk", "sleeves", "costs")


class RegistryError(RuntimeError):
    pass


class Registry:
    """Read-only view over the six registry files, validated at construction."""

    def __init__(self, config_dir: Path = CONFIG_DIR, validate: bool = True):
        self.config_dir = Path(config_dir)
        if validate:
            self._validate()
        self._docs = {
            name: yaml.safe_load((self.config_dir / f"{name}.yaml").read_text())
            for name in FILES
        }

    def _validate(self) -> None:
        result = subprocess.run(
            [sys.executable, str(self.config_dir / "validator.py")],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            raise RegistryError(
                "registry refused to load (validator failed):\n" + result.stdout + result.stderr
            )

    def __getitem__(self, name: str) -> dict:
        return self._docs[name]

    def param(self, file: str, *path: str):
        """Fetch a parameter node by path; returns the node's `value` if it is a provenanced
        parameter (dict with a non-dict 'value'), else the raw node."""
        node = self._docs[file]
        for key in path:
            node = node[key]
        if isinstance(node, dict) and "value" in node and not isinstance(node["value"], dict):
            return node["value"]
        return node


def load_registry(validate: bool = True) -> Registry:
    return Registry(validate=validate)
