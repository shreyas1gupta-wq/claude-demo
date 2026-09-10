"""Count DISTINCT parameter sets evaluated on DEV for volmanaged.
Canonical sources: batch JSON files (scratch batches 1-3), the two harness grid CSVs, and the single-run
harness/diag evaluations listed here. Writes dev_results/volmanaged_iterations.csv (one row per distinct set)."""
import json
from pathlib import Path
import pandas as pd
HERE = Path(__file__).resolve().parents[1] / "dev_results"
KEYS = ["target_vol", "hl", "long_mult", "band_up", "band_dn", "est", "power", "discrete", "weekly", "shock_z", "shock_days"]
DEF = dict(long_mult=4.0, est=None, power=2, discrete=0, weekly=0, shock_z=0.0, shock_days=0)


def canon(v: dict, default_est: str) -> tuple:
    d = dict(DEF); d.update(v)
    if "band" in d:                                   # legacy batches 1-2
        d.setdefault("band_up", d["band"]); d.setdefault("band_dn", d["band"] * float(d.get("bdr", 1.0)))
    if d.get("est") is None: d["est"] = default_est
    if not (float(d["shock_z"]) > 0 and int(d["shock_days"]) > 0): d["shock_z"], d["shock_days"] = 0.0, 0
    return tuple(round(float(d[k]), 6) if k != "est" else d[k] for k in KEYS)


rows = []
for f, default_est in (("volmanaged_batch1.json", "ewma"), ("volmanaged_batch2.json", "ewma"), ("volmanaged_batch3.json", "max2")):
    for v in json.loads((HERE / f).read_text()):
        rows.append((canon(v, default_est), f))
for f in ("volmanaged_grid.csv", "volmanaged_grid2_grid.csv"):
    g = pd.read_csv(HERE / f)
    for _, r in g.iterrows():
        rows.append((canon({k: r[k] for k in ["target_vol", "hl", "long_mult", "band_up", "band_dn"]}, "max2"), f))
# single runs (harness smoke, grid bases, diagnostics, final) -- all coincide with sets above but listed for completeness
singles = {"smoke/grid1-base": dict(target_vol=0.15, hl=10, long_mult=4, band_up=0.5, band_dn=0.3),
           "diag_base(batch1#5)": dict(target_vol=0.15, hl=10, band=0.5, est="ewma"),
           "diag_c14/diag_final/FINAL": dict(target_vol=0.14, hl=13, long_mult=8, band_up=0.75, band_dn=0.3),
           "diag_c13": dict(target_vol=0.13, hl=13, long_mult=8, band_up=0.75, band_dn=0.3)}
for tag, v in singles.items():
    rows.append((canon(v, "max2"), tag))
df = pd.DataFrame([dict(zip(KEYS, k), src=s) for k, s in rows])
print("total evaluations listed (incl. repeats):", len(df), df.src.value_counts().to_dict())
d = df.drop_duplicates(subset=KEYS)
print("DISTINCT parameter sets:", len(d))
print("distinct by first source:", d.src.value_counts().to_dict())
d.to_csv(HERE / "volmanaged_iterations.csv", index=False)
