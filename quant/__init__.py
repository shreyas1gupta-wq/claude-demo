"""Cycle-stack quant package. Every parameter is read through quant.registry — never re-declared.

Contract prior #11: every module here runs green with ZERO network access, on committed or
synthetic fixtures. Ingestion (ingest/) is the sole exception and runs on the principal's machine.
"""
__version__ = "0.1.0"
