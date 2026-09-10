"""Assemble the deliverable grid CSV for crash_exit_dual from the three signal-file grids (R1, R1b, R1c), tagging each row
with the grid it came from. The R2 scratch-variant grid has a different parameter (f) and stays in its own file."""
from pathlib import Path
import pandas as pd
HERE = Path(__file__).resolve().parent
parts = []
for tag in ("gridR1", "gridR1b", "gridR1c"):
    g = pd.read_csv(HERE / f"crash_exit_dual_{tag}_grid.csv")
    g.insert(0, "grid", tag)
    parts.append(g)
out = pd.concat(parts, ignore_index=True)
out.to_csv(HERE / "crash_exit_dual_grid.csv", index=False, float_format="%.4f")
print(len(out), "rows ->", HERE / "crash_exit_dual_grid.csv", "| per grid:", out.groupby("grid").size().to_dict(),
      "| errors:", int(out["error"].notna().sum()) if "error" in out else 0)
