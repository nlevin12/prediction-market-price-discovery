import pandas as pd
import pytest

from pm_price_discovery.results import add_confidence_interval, load_result_table


def test_add_confidence_interval_uses_estimate_and_standard_error():
    table = pd.DataFrame({"beta": [2.0], "se": [0.5]})
    result = add_confidence_interval(table)

    assert result.loc[0, "ci_low"] == pytest.approx(1.020018, rel=1e-5)
    assert result.loc[0, "ci_high"] == pytest.approx(2.979982, rel=1e-5)


def test_load_result_table_checks_schema(tmp_path):
    path = tmp_path / "result.csv"
    pd.DataFrame({"beta": [1.0]}).to_csv(path, index=False)

    with pytest.raises(ValueError, match="missing columns"):
        load_result_table(path, required_columns=["beta", "se"])
