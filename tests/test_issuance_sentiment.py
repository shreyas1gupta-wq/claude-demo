"""L7 issuance-sentiment module vs the planted issuance-chases-valuation economy.

Bounds frozen after an 8-seed dev sweep (2026-09-02): chase-corr +0.77..+0.87; froth-window
state 0.89-0.93 vs winter 0.16-0.28; froth flag rate 0.51-0.83; ~34-43 degraded (no-listing)
months per run. SEEDS are the first three, no curation."""
import numpy as np

from quant.ladder import expanding_percentile, froth_flag, issuance_sentiment_state
from quant.validation.synthetic import issuance_economy

SEEDS = (0, 1, 2)


def test_fixture_plants_issuers_chasing_valuation():
    for s in SEEDS:
        e = issuance_economy(seed=s)
        chase = np.corrcoef(e["volume_ratio"][5:], e["valuation"][1:-4])[0, 1]
        assert chase > 0.7, f"seed {s}: planted chase too weak {chase:.2f}"


def test_state_separates_froth_from_winter():
    froth_all, winter_all, flag_all = [], [], []
    for s in SEEDS:
        e = issuance_economy(seed=s)
        st, _ = issuance_sentiment_state(e["volume_ratio"], e["pop"])
        f0, f1 = e["froth"]
        w0, w1 = e["winter"]
        froth_all.append(np.nanmean(st[f0 + 24:f1]))
        winter_all.append(np.nanmean(st[w0 + 24:w1]))
        flag_all.append(froth_flag(st)[f0 + 24:f1].mean())
    assert np.mean(froth_all) > 0.8
    assert np.mean(winter_all) < 0.35
    assert np.mean(froth_all) - np.mean(winter_all) > 0.5
    assert np.mean(flag_all) > 0.4


def test_degrades_to_volume_leg_when_no_listings():
    e = issuance_economy()
    st, n = issuance_sentiment_state(e["volume_ratio"], e["pop"])
    pv = expanding_percentile(e["volume_ratio"], min_obs=36)
    pp = expanding_percentile(e["pop"], min_obs=36)
    one = (n == 1)
    assert one.sum() > 10                       # the fixture plants no-listing months
    assert np.isnan(pp[one]).all() or (~np.isnan(pv[one])).all()
    ok = one & ~np.isnan(pv)
    assert np.allclose(st[ok], pv[ok], atol=1e-12)


def test_no_lookahead_truncation():
    e = issuance_economy()
    st_full, _ = issuance_sentiment_state(e["volume_ratio"], e["pop"])
    T = 350
    st_tr, _ = issuance_sentiment_state(e["volume_ratio"][:T], e["pop"][:T])
    m = ~np.isnan(st_full[:T]) & ~np.isnan(st_tr)
    assert np.allclose(st_full[:T][m], st_tr[m], atol=1e-12)
