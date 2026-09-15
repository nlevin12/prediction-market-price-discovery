import pandas as pd
import pytest

from src.validation import validate_probability, validate_weekend_panel


def test_validate_probability_accepts_probability_scale():
    validate_probability(pd.DataFrame({"probability": [0.0, 0.35, 1.0]}))


def test_validate_probability_rejects_out_of_range_value():
    with pytest.raises(ValueError, match="invalid probability"):
        validate_probability(pd.DataFrame({"probability": [1.1]}))


def test_validate_weekend_panel_accepts_minimal_contract():
    frame = pd.DataFrame(
        {
            "platform": ["example"],
            "market_key": ["illustrative-market"],
            "stock_ticker": ["EXMP"],
            "session_date": ["2026-01-05"],
            "friday_probability": [0.42],
            "sunday_probability": [0.55],
            "economic_sign": [1],
            "reopening_return_bps": [18.0],
        }
    )
    validate_weekend_panel(frame)
