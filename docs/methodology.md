# Methodology note

## Question

The research asks a timing question: when a prediction market updates while U.S. equities are closed, is that information reflected in the reopening return of an economically linked firm?

The design is deliberately not framed as prediction markets causing stock returns. Both markets may respond to the same underlying information. The closure helps establish which market was able to move first.

## Event--firm links and economic signs

An observation begins with an economically defensible link between a prediction-market contract and a public company. Each link receives an economic sign:

- `+1` when an increase in the event probability is favorable to the linked firm;
- `-1` when an increase is unfavorable.

The sign makes different events comparable. For example, a higher probability of a favorable regulatory decision and a lower probability of an adverse event can both become positive signed revisions for the relevant firm.

## Illustrative signal construction

Let \(p_{i,t}^{\mathrm{before}}\) be the contract probability before the closure interval and \(p_{i,t}^{\mathrm{after}}\) its probability after the interval. The probability revision in percentage points is:

\[
\Delta p_{i,t} = 100 \times \left(p_{i,t}^{\mathrm{after}} - p_{i,t}^{\mathrm{before}}\right).
\]

With an economic sign \(g_i \in \{-1,+1\}\), the standardized event signal is:

\[
s_{i,t} = g_i \times \Delta p_{i,t}.
\]

`src/features.py` implements this public transformation. The synthetic notebook uses the same schema and calculation, but it does not estimate or reproduce the underlying research results.

## Full workflow versus public companion

The protected research workflow includes more than this small transformation:

1. Freeze raw inputs and record reproducibility manifests.
2. Canonicalize equity and prediction-market data into explicit schemas.
3. Validate timestamps, probability paths, market status, and event--firm link metadata.
4. Construct weekend boundary states and peer-adjusted reopening outcomes.
5. Estimate within-link relationships and apply robustness and randomization checks.

The public repository presents selected engineering and design elements only. Its code and data are not a full replication package, and no empirical conclusion should be inferred from its synthetic example.

## Interpretation

The central interpretation is temporal price discovery: a market for real-world states can incorporate information during a period when the linked financial claim is unable to trade. The design does not establish that a prediction market itself moves equity prices, nor does it provide investment advice.
