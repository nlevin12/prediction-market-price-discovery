"""Core transformation for economically signed event-market revisions."""

from __future__ import annotations

import numpy as np
import pandas as pd


def signed_probability_revision(
    before: pd.Series,
    after: pd.Series,
    economic_sign: pd.Series,
) -> pd.Series:
    """Return favorable probability revisions in percentage points.

    Probabilities must use the unit interval. ``economic_sign`` is +1 when a
    higher YES probability is favorable to the firm and -1 when unfavorable.
    """
    before_numeric = pd.to_numeric(before, errors="coerce")
    after_numeric = pd.to_numeric(after, errors="coerce")
    sign_numeric = pd.to_numeric(economic_sign, errors="coerce")

    if before_numeric.isna().any() or after_numeric.isna().any():
        raise ValueError("probabilities must be numeric and non-missing")
    if not before_numeric.between(0, 1).all() or not after_numeric.between(0, 1).all():
        raise ValueError("probabilities must lie in [0, 1]")
    if not np.isin(sign_numeric, [-1, 1]).all():
        raise ValueError("economic_sign must contain only -1 and +1")

    return sign_numeric * 100 * (after_numeric - before_numeric)
