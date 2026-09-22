"""Validation helpers for frozen aggregate result tables."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path
from statistics import NormalDist

import pandas as pd


def load_result_table(
    path: str | Path,
    required_columns: Iterable[str] = (),
) -> pd.DataFrame:
    """Read a CSV result table and verify its declared columns."""
    table = pd.read_csv(path)
    missing = sorted(set(required_columns).difference(table.columns))
    if missing:
        raise ValueError(f"{Path(path).name} is missing columns: {missing}")
    if table.empty:
        raise ValueError(f"{Path(path).name} contains no rows")
    return table


def add_confidence_interval(
    table: pd.DataFrame,
    estimate: str = "beta",
    standard_error: str = "se",
    level: float = 0.95,
) -> pd.DataFrame:
    """Return a copy with normal-approximation confidence bounds."""
    if not 0 < level < 1:
        raise ValueError("level must be between zero and one")

    required = {estimate, standard_error}
    missing = sorted(required.difference(table.columns))
    if missing:
        raise ValueError(f"table is missing columns: {missing}")

    values = table[[estimate, standard_error]].apply(pd.to_numeric, errors="coerce")
    if values.isna().any().any():
        raise ValueError("estimate and standard-error columns must be numeric")
    if values[standard_error].lt(0).any():
        raise ValueError("standard errors cannot be negative")

    critical = NormalDist().inv_cdf(0.5 + level / 2)
    result = table.copy()
    result["ci_low"] = values[estimate] - critical * values[standard_error]
    result["ci_high"] = values[estimate] + critical * values[standard_error]
    return result
