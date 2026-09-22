import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def test_primary_result_matches_readme_value():
    result = pd.read_csv(ROOT / "data/derived/h1_primary_result.csv").iloc[0]
    assert round(result["estimate"], 3) == 2.773
    assert int(result["observations"]) == 1173


def test_notebooks_are_valid_executed_documents():
    notebook_paths = sorted((ROOT / "notebooks").glob("*.ipynb"))
    assert len(notebook_paths) == 2

    for path in notebook_paths:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        assert notebook["nbformat"] == 4
        assert all(cell.get("id") for cell in notebook["cells"])
        code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
        assert code_cells
        assert all(cell["execution_count"] is not None for cell in code_cells)
