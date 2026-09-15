# Illustrative Notebook Guide

`notebooks/01_hard_weekend_design_demo.ipynb` is a small, public-safe walkthrough of the research design.

It creates synthetic prediction-market probabilities and synthetic reopening returns, then uses `src/features.py` to construct two quantities:

- `probability_change_pp`: the probability revision during the illustrative closure interval, measured in percentage points;
- `signed_revision_pp`: that revision multiplied by the economic direction of the event--firm link.

The notebook is a teaching and software demonstration only. Its numbers are generated locally and are **not** paper estimates, source data, or a trading signal.

## Opening it

After the project's Conda environment has been created, open JupyterLab from the repository folder and run all cells in order. The plot and fitted line are reproducible because the notebook fixes its synthetic random seed.

The real research pipeline adds data contracts, canonicalization, input freezes, peer adjustments, fixed effects, and randomization-based checks. Those protected inputs and empirical outputs are deliberately excluded from this public companion repository.
