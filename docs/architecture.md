\# Research Pipeline Architecture



This project studies whether probability revisions in prediction markets are reflected in economically linked equity prices after U.S. equity-market closures.



\## Design



The hard-closure setting creates a one-way timing structure: prediction markets can update while the linked equities cannot trade. The analysis asks whether economically signed probability revisions during the closure are reflected when equities reopen.



\## Pipeline



```text

Frozen raw market data

&#x20;       ↓

Stock and prediction-market canonicalization

&#x20;       ↓

Schema checks, reconciliation, and trade-cache validation

&#x20;       ↓

Human-reviewed event–firm links and economic signs

&#x20;       ↓

Weekend boundary-state construction

&#x20;       ↓

Peer-adjusted equity reopening outcomes

&#x20;       ↓

Fixed-effects, portfolio, randomization, and robustness analyses

