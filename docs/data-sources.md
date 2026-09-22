# Data sources and release boundary

## Inputs used in the research

| Source | Role | Public here? |
| --- | --- | --- |
| Polymarket | Contract metadata, prices, and trade histories | No raw records |
| Kalshi | Contract metadata, prices, and trade histories | No raw records |
| Databento U.S. equities | Minute quotes, trades, and market benchmarks | No; licensed data |
| Reviewed event–firm ledger | Economic links and direction assignments | No; research construction |

The initial search covered the 50,000 largest markets on each prediction-market platform. Candidate links were manually reviewed. The final map contains 749 links covering 736 prediction markets and 65 stocks; 501 links have the data and economic sign needed for the signed analysis.

## Files released here

`data/derived` contains only non-identifying outputs:

- regression coefficients, standard errors, and sample counts;
- randomization-test draws and summary quantiles;
- robustness estimates under alternative peer, weighting, and influence choices;
- horizon-level response estimates.

These are empirical research results. They contain no synthetic observations, contract identifiers, ticker mappings, local paths, API credentials, or vendor data.

## Why `.gitignore` is public

`.gitignore` is a normal tracked project file. It tells Git which local files must not be committed, including raw data, virtual environments, and credentials. It is not a security boundary: secrets or licensed files that have already been committed must be removed from Git history separately.
