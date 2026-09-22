# Methodology

## Hard-closure window

The signal window runs from Friday 8:00 p.m. to Sunday 8:00 p.m. Eastern. U.S.-listed equities cannot trade during this interval, while Polymarket and Kalshi can continue updating. Ending the window on Sunday evening avoids overlap with the earliest resumption of overnight equity trading.

The design identifies temporal price discovery: the prediction market can move before the linked equity reopens. Both markets may still be responding to the same underlying news.

## Signed prediction-market revision

For reviewed link $\ell$ and reopening date $d$, let $p^F_{\ell d}$ and $p^S_{\ell d}$ be the latest contract probabilities at or before the Friday and Sunday boundaries. Let $g_\ell \in \{-1,+1\}$ record whether a higher probability of the contract's YES outcome is unfavorable or favorable to the linked firm.

$$
S_{\ell d} = g_\ell \times 100\left(p^S_{\ell d}-p^F_{\ell d}\right).
$$

$S_{\ell d}$ is measured in percentage points. A positive value is favorable to the linked stock, regardless of how the underlying contract is worded.

## Reopening outcome

The equity reopening price combines quote and trade information. A usable two-sided quote midpoint and a volume-weighted trade-price measure are constructed from the first five regular-session minutes. A stock-date is retained only when the two estimates agree within a threshold calibrated outside the analysis sample.

For stock $s$ on date $d$, the raw reopening gap is compared with a set $\mathcal{P}_{\ell d}$ of matched same-date firms that have no reviewed exposure to the event:

$$
Y_{\ell d} = g_{sd} - \frac{1}{|\mathcal{P}_{\ell d}|}
\sum_{j \in \mathcal{P}_{\ell d}} g_{jd}.
$$

Peers are selected using only pre-closure characteristics: size, trailing opening-gap volatility, prior-session return, and final-30-minute return.

## Primary regression

The estimating equation is

$$
Y_{\ell d} = \beta S_{\ell d} + \alpha_\ell + \lambda_d
+ X_{s,d-1}'\gamma + \varepsilon_{\ell d},
$$

where $\alpha_\ell$ are event–firm-link fixed effects and $\lambda_d$ are reopening-date fixed effects. The controls in $X_{s,d-1}$ are known before the weekend: prior-session return, final-30-minute return, and trailing 20-session opening-gap volatility.

The coefficient $\beta$ is an event-to-equity conversion rate: basis points of peer-adjusted reopening movement per one-percentage-point favorable prediction-market revision.

The primary estimate is $\hat\beta=2.773$. Standard errors are two-way clustered by stock and date; the repository also reports clustering by prediction market and date, a date-cluster wild bootstrap, and a within-date permutation test.

## Scope of the public files

The notebooks reproduce figures and summaries from frozen aggregate outputs. They do not re-estimate the model from contract-level and stock-level observations because those inputs include licensed data and the reviewed event–firm ledger.
