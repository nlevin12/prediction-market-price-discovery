"""Portable data-contract checks for the public companion workflow."""

from __future__ import annotations

from collections.abc import Iterable

import pandas as pd


def require_columns(frame: pd.DataFrame, required: Iterable[str], name: str = "data") -> None:
    """Raise a clear error when a table does not meet its declared schema."""
    absent = sorted(set(required).difference(frame.columns))
    if absent:
        raise ValueError(f"{name} is missing required columns: {absent}")


def validate_probability(frame: pd.DataFrame, column: str = "probability") -> None:
    """Verify that a prediction-market probability is finite and in [0, 1]."""
    require_columns(frame, [column])
    values = pd.to_numeric(frame[column], errors="coerce")
    invalid = values.isna() | values.lt(0) | values.gt(1)
    if invalid.any():
        raise ValueError(f"{column} contains {int(invalid.sum())} invalid probability values")


def validate_weekend_panel(frame: pd.DataFrame) -> None:
    """Check the minimal contract for a public weekend event–stock example panel."""
    required = [
        "platform",
        "market_key",
        "stock_ticker",
        "session_date",
        "friday_probability",
        "sunday_probability",
        "economic_sign",
        "reopening_return_bps",
    ]
    require_columns(frame, required, name="weekend panel")
    validate_probability(frame, "friday_probability")
    validate_probability(frame, "sunday_probability")
    signs = set(pd.to_numeric(frame["economic_sign"], errors="coerce").dropna().unique())
    if not signs.issubset({-1, 1}):
        raise ValueError("economic_sign must contain only -1 or 1")
