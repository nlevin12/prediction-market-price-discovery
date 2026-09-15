"""Public-safe feature construction for the illustrative weekend notebook."""

from __future__ import annotations

import pandas as pd

from src.validation import validate_weekend_panel


def build_weekend_signal(panel: pd.DataFrame) -> pd.DataFrame:
    """Add unsigned and economically signed probability revisions.

    ``probability_change_pp`` is the prediction-market probability change in
    percentage points during the illustrative closure interval.

    ``signed_revision_pp`` multiplies that change by the reviewed economic
    direction of the event--firm link.  A positive signed value therefore has
    the same economic interpretation across links.

    The function is intentionally small: it demonstrates the public-facing
    signal transformation, not the project's confidential data assembly or
    empirical estimation pipeline.
    """

    validate_weekend_panel(panel)

    result = panel.copy()
    result["probability_change_pp"] = 100 * (
        result["sunday_probability"] - result["friday_probability"]
    )
    result["signed_revision_pp"] = (
        result["economic_sign"] * result["probability_change_pp"]
    )
    return result
