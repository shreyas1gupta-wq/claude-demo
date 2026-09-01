"""L3/L4 momentum modules vs the planted-truth universe (momentum + engineered DM crash).

Assertion bounds were frozen only after a 10-seed dev sweep (dev log, 2026-09-01): calm WML
+2.5 to +4.0%/m; rebound WML negative in 7-9/10 seeds (one seed's crash never materialized —
crashes are probabilistic, and the fixture keeps that honesty); guard-ON months average
-1.56%/m vs +3.33%/m when OFF; guard fired in the panic window 10/10. The fixture itself was
falsified once in dev (drift channel dwarfed the beta channel; bear had no vol spike) and
retuned — see the calibration note in quant/validation/synthetic.py.
"""
import numpy as np
import pytest

from quant.ladder import (crash_guard, momentum_composite, trailing_return,
                          tsmom_state, wml_monthly_returns)
from quant.validation.synthetic import momentum_universe

SEEDS = (11, 0, 1)   # fixed BEFORE freezing; pooled assertions below held on all 10 dev seeds


@pytest.fixture(scope="module")
def panel():
    out = []
    for s in SEEDS:
        p, mkt, ph = momentum_universe(seed=s)
        score = momentum_composite(p)
        out.append(dict(p=p, mkt=mkt, ph=ph, score=score,
                        wml=wml_monthly_returns(p, score), g=crash_guard(mkt)))
    return out


def test_trailing_return_exact():
    p = np.array([[1.0, 1.1, 1.21, 1.331, 1.4641]])
    r = trailing_return(p, lookback=3, skip=1)
    assert r[0, 3] == pytest.approx(1.21 / 1.0 - 1)
    assert np.isnan(r[0, :3]).all()


def test_planted_momentum_is_recovered_in_calm(panel):
    calms = []
    for d in panel:
        calm_end = d["ph"]["bear"][0] // 21 - 1
        calms.append(np.nanmean(d["wml"][13:calm_end]))
    assert np.mean(calms) > 0.015, f"pooled calm WML too weak: {np.mean(calms):.4f}"


def test_wml_crashes_in_the_planted_rebound(panel):
    rebs = []
    for d in panel:
        b1, b2 = d["ph"]["rebound"]
        rebs.append(np.nanmean([d["wml"][k] for k in range(len(d["wml"]))
                                if b1 <= (k + 1) * 21 - 1 < b2]))
    assert np.mean(rebs) < -0.03, f"pooled rebound WML should crash: {np.mean(rebs):.4f}"


def test_guard_fires_in_the_panic_window(panel):
    for d in panel:
        b1 = d["ph"]["rebound"][0]
        assert np.nanmax(d["g"][b1 - 10:b1 + 21]) == 1, "guard silent through the panic window"


def test_guard_on_months_are_the_bad_months(panel):
    on, off = [], []
    for d in panel:
        for k in range(13, len(d["wml"])):
            t0 = (k + 1) * 21 - 1
            if np.isnan(d["wml"][k]) or np.isnan(d["g"][t0]):
                continue
            (on if d["g"][t0] == 1 else off).append(d["wml"][k])
    assert len(on) > 10 and len(off) > 30
    assert np.mean(on) < np.mean(off) - 0.02, \
        f"guard must separate bad months: ON {np.mean(on):.4f} vs OFF {np.mean(off):.4f}"


def test_composite_no_lookahead(panel):
    d = panel[0]
    p = d["p"]
    for T in (600, 900):
        tr = momentum_composite(p[:, :T])
        full = d["score"][:, :T]
        m = ~np.isnan(full) & ~np.isnan(tr)
        assert np.allclose(full[m], tr[m], atol=1e-12)


def test_tsmom_state_signs():
    up = np.cumprod(np.full(400, 1.001))
    dn = np.cumprod(np.full(400, 0.999))
    su, sd = tsmom_state(up), tsmom_state(dn)
    assert np.all(su[np.isfinite(su)] == 1.0)
    assert np.all(sd[np.isfinite(sd)] == -1.0)
    assert np.isnan(su[:252]).all()
