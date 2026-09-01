"""Value/quality modules vs the planted-truth universe (mean-reverting mispricing + quality
drift + a dispersion episode). Bounds frozen after a 5-seed dev sweep (2026-09-01): value 12m
decile spread +8.8-9.5%, quality +7.3-10.3%, PIT-cheat inflation on every seed, spread-state
episode separation 0.25-0.28 vs 0.16, and corr(value, momentum ranks) -0.26 to -0.29 — the
negative value-momentum correlation EMERGES from the physics, matching the real-data batch
(India -0.37, US -0.41; trials V2)."""
import numpy as np

from quant.ladder import quality_score, value_score, value_spread
from quant.ladder.momentum import cross_rank
from quant.validation.synthetic import value_universe


def decile_spread_12m(prices, score, month0=24):
    N, T = prices.shape
    sp = []
    for t in range(month0, T - 12, 3):
        s = score[:, t]
        m = ~np.isnan(s)
        if m.sum() < 50:
            continue
        hi, lo = np.nanquantile(s[m], 0.9), np.nanquantile(s[m], 0.1)
        fwd = prices[:, t + 12] / prices[:, t] - 1
        sp.append(np.nanmean(fwd[m & (s >= hi)]) - np.nanmean(fwd[m & (s <= lo)]))
    return float(np.mean(sp))


def test_planted_value_convergence_is_recovered():
    u = value_universe()
    v = value_score(u["book"], u["prices"], report_lag=3)
    assert decile_spread_12m(u["prices"], v) > 0.05


def test_pit_cheat_inflates_the_backtest():
    """Using un-lagged book value (information not yet public) must LOOK better than the honest
    lagged version — the classic fundamentals-backtest trap, demonstrated rather than asserted."""
    u = value_universe()
    honest = decile_spread_12m(u["prices"], value_score(u["book"], u["prices"], report_lag=3))
    cheat = decile_spread_12m(u["prices"], value_score(u["book"], u["prices"], report_lag=0))
    assert cheat > honest + 0.003


def test_planted_quality_is_recovered():
    u = value_universe()
    q = quality_score(u["profit_obs"], report_lag=3)
    assert decile_spread_12m(u["prices"], q) > 0.04


def test_value_spread_state_detects_the_dispersion_episode():
    u = value_universe()
    vs = value_spread(u["book"], u["prices"])
    e0, e1 = u["spread_episode"]
    assert np.nanmean(vs[e0 + 6:e1]) > np.nanmean(vs[24:e0 - 6]) + 0.05


def test_value_momentum_negative_correlation_emerges():
    u = value_universe()
    v = value_score(u["book"], u["prices"], report_lag=3)
    mom = np.full_like(v, np.nan)
    for t in range(13, u["prices"].shape[1]):
        mom[:, t] = u["prices"][:, t - 1] / u["prices"][:, t - 12] - 1
    mr = cross_rank(mom)
    m = ~np.isnan(v) & ~np.isnan(mr)
    corr = float(np.corrcoef(v[m], mr[m])[0, 1])
    assert corr < -0.15, f"value and momentum ranks should oppose: {corr:+.2f}"


def test_no_lookahead_truncation():
    u = value_universe()
    v_full = value_score(u["book"], u["prices"], report_lag=3)
    T = 150
    v_tr = value_score(u["book"][:, :T], u["prices"][:, :T], report_lag=3)
    m = ~np.isnan(v_full[:, :T]) & ~np.isnan(v_tr)
    assert np.allclose(v_full[:, :T][m], v_tr[m], atol=1e-12)
    vs_full = value_spread(u["book"], u["prices"])
    vs_tr = value_spread(u["book"][:, :T], u["prices"][:, :T])
    mm = ~np.isnan(vs_full[:T]) & ~np.isnan(vs_tr)
    assert np.allclose(vs_full[:T][mm], vs_tr[mm], atol=1e-12)
