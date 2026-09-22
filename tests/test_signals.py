import pandas as pd
import pytest

from pm_price_discovery.signals import signed_probability_revision


def test_signed_probability_revision_normalizes_direction():
    before = pd.Series([0.40, 0.70])
    after = pd.Series([0.55, 0.50])
    sign = pd.Series([1, -1])

    result = signed_probability_revision(before, after, sign)

    assert result.tolist() == pytest.approx([15.0, 20.0])


def test_signed_probability_revision_rejects_invalid_probability():
    with pytest.raises(ValueError, match=r"\[0, 1\]"):
        signed_probability_revision(
            pd.Series([0.50]),
            pd.Series([1.10]),
            pd.Series([1]),
        )
