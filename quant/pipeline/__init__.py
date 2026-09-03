"""Track P — the PIT ML pipeline's committed machinery (pipeline-v2's architecture, built early).

Everything here is data-agnostic and synthetic-truth tested; the PIT bhavcopy plugs in at
landing day. Purged CV and the walk-forward judge live in quant/stats and quant/validation.
"""
from .labeling import triple_barrier, meta_labels  # noqa: F401
from .vintage import VintageSeries  # noqa: F401
