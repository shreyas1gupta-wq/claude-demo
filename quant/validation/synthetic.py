"""Seeded synthetic generators with KNOWN ground truth — the estimator-validation fixtures.

Purpose (Track R6): before any estimator touches Indian data, it must demonstrably recover known
parameters on synthetic data at India-like sample sizes (~380 monthly obs). These generators are
the ground truth for tests/ and scripts/run_estimator_validation.py.
"""
from __future__ import annotations

import numpy as np


def ar1_series(rho: float, T: int, sigma: float = 1.0, seed: int = 0,
               burn: int = 200) -> np.ndarray:
    """Stationary AR(1) with known rho (true tau_half = ln(.5)/ln(rho)).

    Vectorized via scipy.signal.lfilter with a burn-in for stationarity — the parametric
    bootstrap in quant.stats.tau_half simulates thousands of these."""
    from scipy.signal import lfilter
    rng = np.random.default_rng(seed)
    eps = rng.normal(0.0, sigma, T + burn)
    y = lfilter([1.0], [1.0, -rho], eps)
    return y[burn:]


def regime_vol_returns(T: int, seed: int = 0, p_calm_to_stress: float = 0.02,
                       p_stress_to_calm: float = 0.10, mu: float = 0.0004,
                       sigma_calm: float = 0.008, sigma_stress: float = 0.028,
                       stress_drift: float = -0.002, return_states: bool = False):
    """Two-state volatility-clustered daily returns (calm/stress persistence) — used to
    demonstrate that iid bootstrap understates drawdown tails vs the block bootstrap.
    Ground truth: stress episodes have mean length 1/p_stress_to_calm days."""
    rng = np.random.default_rng(seed)
    r = np.empty(T)
    states = np.zeros(T, dtype=bool)
    stress = False
    for t in range(T):
        states[t] = stress
        if stress:
            r[t] = rng.normal(stress_drift, sigma_stress)
            stress = rng.random() > p_stress_to_calm
        else:
            r[t] = rng.normal(mu, sigma_calm)
            stress = rng.random() < p_calm_to_stress
    return (r, states) if return_states else r


def trend_plus_cycle(T: int, cycle_rho: float = 0.9, trend: float = 0.01,
                     sigma_cycle: float = 1.0, seed: int = 0):
    """Random-walk-with-drift trend + known AR(1) cycle; returns (y, true_cycle) for
    Hamilton-filter recovery tests."""
    rng = np.random.default_rng(seed)
    cyc = ar1_series(cycle_rho, T, sigma_cycle, seed=seed + 1)
    tr = np.cumsum(trend + rng.normal(0, 0.2, T))
    return tr + cyc, cyc


def boom_bust_economy(T: int = 480, seed: int = 7) -> dict:
    """Monthly synthetic economy with a KNOWN credit boom and bust (the L10 fixture).

    Income grows steadily; credit grows WITH income except a boom (months 200-320: credit
    outgrows income by 60bps/mo) then a bust (320-400: credit growth 70bps/mo below income).
    Deposits track income, so the credit-deposit ratio rises through the boom and unwinds
    after it. Ground truth: boom=(200, 320), bust=(320, 400), returned alongside the series."""
    rng = np.random.default_rng(seed)
    g_income = 0.005 + 0.002 * rng.standard_normal(T)
    income = 100 * np.cumprod(1 + g_income)
    g_credit = g_income.copy()
    g_credit[200:320] += 0.006            # boom: credit outgrows income
    g_credit[320:400] -= 0.007            # bust: credit contracts vs income
    credit = 80 * np.cumprod(1 + g_credit + 0.001 * rng.standard_normal(T))
    deposits = 110 * np.cumprod(1 + g_income + 0.0005 * rng.standard_normal(T))
    return dict(income=income, credit=credit, deposits=deposits,
                boom=(200, 320), bust=(320, 400))


def momentum_universe(N: int = 200, T: int = 1260, seed: int = 11,
                      crash: tuple = (900, 960, 1020)):
    """Daily panel of N stocks with PLANTED cross-sectional momentum and a PLANTED
    Daniel-Moskowitz-style momentum crash (the L3 fixture).

    Mechanics: each stock's drift mu_i,t is a slow AR(1) (rho=0.997 daily) => past winners
    genuinely keep winning (the momentum effect). Market path m_t is calm, then a bear
    (crash[0]..crash[1]), then a violent rebound (crash[1]..crash[2]). Each stock's beta rises
    with its OWN drawdown (leverage effect), so by the rebound the loser leg is high-beta and
    rallies hardest — the planted WML crash. Returns (prices[N,T], market[T], phases dict)."""
    rng = np.random.default_rng(seed)
    # calibration note (dev falsification, 2026-09-01): first cut used sig_mu=3.5e-4
    # (stationary drift dispersion ~0.45%/day -> WML ~+25%/MONTH, absurd) and a bear with no
    # vol spike (panic guard had nothing to see) - the planted crash never crashed because the
    # drift channel dwarfed the beta channel. Retuned: realistic momentum spread, crisis vol
    # 3x in the bear/rebound, stronger leverage-effect slope.
    rho, sig_mu = 0.997, 8e-5
    mu = np.zeros((N, T))
    mu[:, 0] = rng.normal(0, sig_mu / np.sqrt(1 - rho**2), N)
    eps_mu = rng.normal(0, sig_mu, (N, T))
    for t in range(1, T):
        mu[:, t] = rho * mu[:, t - 1] + eps_mu[:, t]
    g_m = np.full(T, 0.0003)
    b0, b1, b2 = crash
    g_m[b0:b1] = -0.005          # bear leg (~ -26% over 60d)
    g_m[b1:b2] = +0.008          # violent rebound
    sig_m = np.full(T, 0.008)
    sig_m[b0:b2] = 0.024         # crisis vol regime through bear AND rebound
    m = g_m + sig_m * rng.standard_normal(T)
    base_beta = rng.uniform(0.7, 1.3, N)
    r = np.zeros((N, T))
    level = np.ones(N)
    peak = np.ones(N)
    for t in range(T):
        dd = 1.0 - level / peak                       # own drawdown, known at t-1 close
        beta_t = base_beta + 2.5 * dd                 # leverage effect: losers get high-beta
        r[:, t] = beta_t * m[t] + mu[:, t] + 0.012 * rng.standard_normal(N)
        level = level * (1.0 + r[:, t])
        peak = np.maximum(peak, level)
    prices = np.cumprod(1.0 + r, axis=1)
    market = np.cumprod(1.0 + m)
    return prices, market, dict(bear=(b0, b1), rebound=(b1, b2))


def value_universe(N: int = 150, T: int = 240, seed: int = 21,
                   spread_episode: tuple = (140, 180)):
    """Monthly panel with PLANTED value and quality effects (the value/quality fixture).

    Fair value F grows at a common drift plus a persistent per-stock quality drift q_i
    (observable with noise -> quality effect). Price = F * exp(m), mispricing m is slow AR(1)
    (rho=0.97 monthly, tau_half ~ 23m) -> low P/B names are genuinely underpriced and converge
    (value effect). Book value proxies F with reporting noise and is REPORTED with a lag the
    consumer must respect. During spread_episode the mispricing volatility doubles (a planted
    dispersion regime for the value-spread state). Returns dict of panels + truth."""
    rng = np.random.default_rng(seed)
    q = rng.normal(0.000, 0.0025, N)                    # monthly quality drift differences
    rho_m, sig_m = 0.97, 0.02
    m = np.zeros((N, T))
    m[:, 0] = rng.normal(0, sig_m / np.sqrt(1 - rho_m**2), N)
    F = np.ones((N, T))
    for t in range(1, T):
        s = sig_m * (2.0 if spread_episode[0] <= t < spread_episode[1] else 1.0)
        m[:, t] = rho_m * m[:, t - 1] + rng.normal(0, s, N)
        F[:, t] = F[:, t - 1] * np.exp(0.005 + q + rng.normal(0, 0.01, N))
    prices = F * np.exp(m)
    book = F * np.exp(rng.normal(0, 0.05, (N, T)))      # noisy fair-value proxy
    profit_obs = q[:, None] + rng.normal(0, 0.002, (N, T))
    return dict(prices=prices, book=book, profit_obs=profit_obs,
                mispricing=m, quality=q, spread_episode=spread_episode)


def financial_cycle_economy(T: int = 480, seed: int = 31,
                            boom: tuple = (180, 330), bust: tuple = (330, 420)):
    """Monthly economy with a PLANTED credit-property financial cycle (the L12 fixture).

    Mutual amplification per Borio/Kiyotaki-Moore: credit growth responds to lagged property
    appreciation (collateral channel) and property appreciation responds to lagged credit growth
    (funding channel), around a slow exogenous forcing that turns positive in the boom window
    and negative in the bust. Income grows steadily; CPI drifts. Returns dict of levels + truth."""
    rng = np.random.default_rng(seed)
    g_inc = 0.004 + 0.002 * rng.standard_normal(T)
    income = 100 * np.cumprod(1 + g_inc)
    force = np.zeros(T)
    force[boom[0]:boom[1]] = +0.0025
    force[bust[0]:bust[1]] = -0.0035
    g_cr = np.zeros(T)
    g_hp = np.zeros(T)
    credit = np.empty(T)
    hp = np.empty(T)
    credit[0], hp[0] = 80.0, 100.0
    for t in range(1, T):
        g_cr[t] = (0.004 + force[t] + 0.35 * g_hp[t - 1]
                   + 0.0015 * rng.standard_normal())
        g_hp[t] = (0.002 + force[t] + 0.35 * g_cr[t - 1]
                   + 0.004 * rng.standard_normal())
        credit[t] = credit[t - 1] * (1 + g_cr[t])
        hp[t] = hp[t - 1] * (1 + g_hp[t])
    cpi = np.cumprod(1 + 0.003 + 0.001 * rng.standard_normal(T))
    return dict(credit=credit, income=income, hp=hp, cpi=cpi,
                boom=boom, bust=bust)


def capex_economy(T: int = 480, seed: int = 41,
                  boom: tuple = (160, 300), bust: tuple = (300, 380)):
    """Monthly economy with a PLANTED capex cycle (the L11 fixture).

    Accelerator dynamics: utilization rises under boom forcing; capital-goods output growth
    follows lagged utilization pressure (orders when tight); the GFCF share ratchets up with
    both, then the bust collapses utilization first and the other legs bleed with time-to-build
    inertia — the repair period keeps utilization depressed. Returns dict of levels + truth:
    util (a bounded rate in [0.5, 0.95]), capgoods (an output index), gfcf_share, output."""
    rng = np.random.default_rng(seed)
    force = np.zeros(T)
    force[boom[0]:boom[1]] = +0.008
    force[bust[0]:bust[1]] = -0.015
    util = np.empty(T)
    util[0] = 0.72
    g_cg = np.zeros(T)
    capgoods = np.empty(T)
    capgoods[0] = 100.0
    gfcf_share = np.empty(T)
    gfcf_share[0] = 0.28
    g_out = 0.003 + 0.0015 * rng.standard_normal(T)
    output = 100 * np.cumprod(1 + g_out)
    for t in range(1, T):
        util[t] = np.clip(util[t - 1] + force[t] + 0.10 * (0.72 - util[t - 1])
                          + 0.003 * rng.standard_normal(), 0.5, 0.95)
        g_cg[t] = (0.003 + 0.9 * (util[t - 1] - 0.72) + 0.25 * g_cg[t - 1]
                   + 0.004 * rng.standard_normal())
        capgoods[t] = capgoods[t - 1] * (1 + g_cg[t])
        gfcf_share[t] = np.clip(gfcf_share[t - 1] + 0.25 * (util[t] - util[t - 1])
                                * gfcf_share[t - 1] + 0.0008 * rng.standard_normal(),
                                0.15, 0.45)
    return dict(util=util, capgoods=capgoods, gfcf_share=gfcf_share, output=output,
                boom=boom, bust=bust)


def fpi_economy(T: int = 480, seed: int = 51,
                boom: tuple = (140, 300), unwind: tuple = (300, 380)):
    """Monthly economy with PLANTED flows-follow-returns and a positioning unwind (L14 fixture).

    Flows chase LAGGED returns (the Griffin-Nardari-Stulz direction); ownership share of float
    integrates flows with slow attrition; the boom builds ownership to an extreme; in the
    unwind window forced selling subtracts from returns proportional to the ownership overhang
    (the capacity mechanism planted). Returns dict: ret, flow, ownership (share of float),
    plus truth windows."""
    rng = np.random.default_rng(seed)
    ret = np.zeros(T)
    flow = np.zeros(T)
    own = np.empty(T)
    own[0] = 0.10
    for t in range(1, T):
        base = 0.006 if boom[0] <= t < boom[1] else 0.002
        overhang = max(own[t - 1] - 0.18, 0.0)
        forced = -0.9 * overhang if unwind[0] <= t < unwind[1] else 0.0
        ret[t] = base + forced + 0.035 * rng.standard_normal()
        flow[t] = 0.12 * ret[t - 1] + 0.001 * rng.standard_normal() \
            + (-0.05 * overhang if unwind[0] <= t < unwind[1] else 0.0)
        own[t] = np.clip(own[t - 1] * 0.999 + flow[t], 0.02, 0.60)
    return dict(ret=ret, flow=flow, ownership=own, boom=boom, unwind=unwind)


def issuance_economy(T: int = 480, seed: int = 61,
                     froth: tuple = (200, 300), winter: tuple = (300, 380)):
    """Monthly economy with PLANTED issuance-chases-valuation (the L7 fixture).

    A slow valuation wave (price/fundamental ratio) peaks in the froth window; issuance
    volume responds to LAGGED valuation (issuers file when markets are expensive — the
    Baker-Wurgler incentive, with a filing delay), first-day pops rise with the same wave,
    and in the winter both collapse while some months have NO listings (pop = NaN — the
    degradation reality). Returns dict: valuation, volume_ratio, pop, plus truth windows."""
    rng = np.random.default_rng(seed)
    val = np.empty(T)
    val[0] = 1.0
    for t in range(1, T):
        target = 1.6 if froth[0] <= t < froth[1] else (0.7 if winter[0] <= t < winter[1]
                                                       else 1.0)
        val[t] = val[t - 1] + 0.06 * (target - val[t - 1]) + 0.02 * rng.standard_normal()
    vol = np.empty(T)
    pop = np.empty(T)
    for t in range(T):
        v_lag = val[max(t - 4, 0)]
        vol[t] = max(0.0002 + 0.004 * max(v_lag - 0.9, 0.0)
                     + 0.0006 * rng.standard_normal(), 0.0)
        pop[t] = 0.02 + 0.30 * max(val[t] - 1.0, 0.0) + 0.05 * rng.standard_normal()
        if winter[0] <= t < winter[1] and rng.random() < 0.5:
            pop[t] = np.nan   # no listings that month
    return dict(valuation=val, volume_ratio=vol, pop=pop, froth=froth, winter=winter)
