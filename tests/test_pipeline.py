"""Track P scaffold: planted-truth tests for triple-barrier, meta-labels, vintage stamping."""
import numpy as np
import pandas as pd

from quant.pipeline import VintageSeries, meta_labels, triple_barrier


def test_triple_barrier_hits_are_deterministic():
    # price rises 1%/bar (log): barrier at 1.5% sits strictly inside bar 2's move
    close = 100 * np.exp(0.01 * np.arange(20))
    vol = np.full(20, 0.015)
    ev = triple_barrier(close, events=[0], vol=vol, pt_mult=1.0, sl_mult=1.0, max_hold=10)[0]
    assert ev.label == 1 and ev.t1 == 2  # 2 bars * 1% = 2% > 1.5% barrier; bar 1 (1%) is not
    # falling path hits the stop
    ev2 = triple_barrier(close[::-1].copy(), [0], vol, 1.0, 1.0, 10)[0]
    assert ev2.label == -1 and ev2.t1 == 2
    # flat path times out at the vertical barrier with label 0
    ev3 = triple_barrier(np.full(20, 100.0), [0], vol, 1.0, 1.0, 7)[0]
    assert ev3.label == 0 and ev3.t1 == 7 and ev3.ret == 0.0


def test_triple_barrier_short_side_flips_barriers():
    close = 100 * np.exp(-0.01 * np.arange(20))   # falling market
    vol = np.full(20, 0.015)
    ev = triple_barrier(close, [0], vol, 1.0, 1.0, 10, side=np.array([-1.0]))[0]
    assert ev.label == 1 and ev.ret > 0          # a short profits from the fall


def test_meta_labels_reward_realized_profit_only():
    close = 100 * np.exp(0.01 * np.arange(20))
    vol = np.full(20, 0.015)
    evs = triple_barrier(close, [0, 0], vol, 1.0, 1.0, 10,
                         side=np.array([1.0, -1.0]))   # long right, short wrong
    assert list(meta_labels(evs)) == [1, 0]


def test_vintage_series_hides_the_future_and_serves_revisions():
    v = VintageSeries()
    v.record("2020-01-31", as_of="2020-02-15", value=1.0)     # first print
    v.record("2020-01-31", as_of="2020-03-15", value=1.5)     # revision
    v.record("2020-02-29", as_of="2020-03-20", value=2.0)
    # before any publication: empty
    assert v.asof("2020-02-01").empty
    # after first print, before revision: the UNREVISED value
    s1 = v.asof("2020-02-20")
    assert list(s1.values) == [1.0]
    # after revision + second obs: revised value and both dates
    s2 = v.asof("2020-04-01")
    assert list(s2.values) == [1.5, 2.0]
    assert list(v.final().values) == [1.5, 2.0]
