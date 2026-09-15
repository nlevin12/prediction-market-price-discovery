import pandas as pd
import pytest

from src.features import build_weekend_signal


def test_build_weekend_signal_adds_expected_percentage_point_columns():
    panel = pd.DataFrame(
        {
            "platform": ["example", "example"],
            "market_key": ["event-a", "event-b"],
            "stock_ticker": ["EXMP", "DEMO"],
            "session_date": ["2026-01-05", "2026-01-12"],
            "friday_probability": [0.40, 0.70],
            "sunday_probability": [0.55, 0.50],
            "economic_sign": [1, -1],
            "reopening_return_bps": [12.0, 14.0],
        }
    )

    result = build_weekend_signal(panel)

    assert result["probability_change_pp"].tolist() == pytest.approx([15.0, -20.0])
    assert result["signed_revision_pp"].tolist() == pytest.approx([15.0, 20.0])
    assert "probability_change_pp" not in panel.columns
