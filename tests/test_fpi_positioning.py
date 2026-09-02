"""L14 FPI-positioning module vs the planted flows-follow-returns economy.

Bounds frozen after an 8-seed dev sweep (2026-09-02, post-retune: flow coefficient 0.12):
follow-corr +0.97 all seeds, lead-corr |<0.13|; pooled late-boom flag rate 0.63 vs pre-boom
0.11 on the first three seeds (seed 2's late-boom miss kept honest in the pool). The module's
defining property is an EXCLUSION: no flow-based API exists — flow momentum is the atlas's
§7 REJECT, and the interface enforces it structurally."""
import numpy as np

import quant.ladder.fpi_positioning as fpi_mod
from quant.ladder import fpi_positioning_state, positioning_extreme
from quant.validation.synthetic import fpi_economy

SEEDS = (0, 1, 2)


def test_fixture_plants_flows_following_returns():
    for s in SEEDS:
        e = fpi_economy(seed=s)
        follow = np.corrcoef(e["flow"][1:], e["ret"][:-1])[0, 1]
        lead = np.corrcoef(e["ret"][1:], e["flow"][:-1])[0, 1]
        assert follow > 0.9, f"seed {s}: planted follow-corr too weak {follow:.2f}"
        assert abs(lead) < 0.2, f"seed {s}: flows must NOT lead returns ({lead:.2f})"


def test_module_exposes_no_flow_signal():
    """The §7 REJECT is structural: nothing flow-named is importable from the seat."""
    public = [n for n in dir(fpi_mod) if not n.startswith("_")]
    assert not any("flow" in n.lower() for n in public), public


def test_extreme_flag_discriminates_late_boom_from_early():
    late_all, early_all = [], []
    for s in SEEDS:
        e = fpi_economy(seed=s)
        ex = positioning_extreme(fpi_positioning_state(e["ownership"]))
        b0, b1 = e["boom"]
        late_all.append(ex[b1 - 24:b1].mean())
        early_all.append(ex[60:b0].mean())
    assert np.mean(late_all) > 0.5, f"late-boom flag rate too low: {np.mean(late_all):.2f}"
    assert np.mean(early_all) < 0.25, f"early flag rate too high: {np.mean(early_all):.2f}"


def test_flag_is_risk_off_only_and_nan_safe():
    e = fpi_economy()
    st = fpi_positioning_state(e["ownership"])
    ex = positioning_extreme(st, hi=0.9)
    ok = ~np.isnan(st)
    assert not ex[~ok].any()                      # no flag without ranks
    assert not ex[ok & (st < 0.9)].any()          # never fires below the extreme
    assert (st[ok & ex[ok]] >= 0.9).all()


def test_no_lookahead_truncation():
    e = fpi_economy()
    st_full = fpi_positioning_state(e["ownership"])
    T = 350
    st_tr = fpi_positioning_state(e["ownership"][:T])
    m = ~np.isnan(st_full[:T]) & ~np.isnan(st_tr)
    assert np.allclose(st_full[:T][m], st_tr[m], atol=1e-12)
