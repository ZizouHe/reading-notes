## Breaking Bad Trends

**1. Motivation and Definitions**

- **Trend-following** (time-series momentum) strategies go long (buy) when recent past returns are positive and short (sell) when negative.
- A **turning point** occurs when a “slow” momentum signal (e.g. 12-month average) and a “fast” signal (e.g. 1- or 2-month average) disagree in sign—indicating a potential break from an established trend.

**2. Key Empirical Findings**

1. **Trend Breaks Hurt Performance**
   - Across 43 futures markets (equities, bonds, commodities) from 1990–2022, years with more turning-point months had materially lower risk-adjusted returns to a static 12-month trend strategy (e.g. each +1 SD in turns → –8.9 pp annual return) .
2. **Post-GFC Deterioration Explained**
   - In the 2009–2019 expansion post-2008, turning points became more frequent (median rose from 4.54 to 4.80 per year), helping explain why classic trend following struggled over that decade .
3. **Dynamic Blending Recovers Returns**
   - By classifying each month into four states—**Bull**, **Correction** (slow > 0, fast < 0), **Bear**, and **Rebound** (slow < 0, fast > 0)—and dynamically mixing slow & fast signals with state-dependent weights, one can harvest returns after turning points rather than suffer whipsaw losses .

**3. Methodological Highlights**

- **Static strategy**: Go ±1 unit based solely on the sign of the trailing 12-month return.

- **Turning points**: Months where

  sign(12-mo avg) ≠ sign(1- or 2-mo avg).

- **Dynamic strategy**:

  - In **Bull/Bear**, follow the slow signal (same as static).
  - In **Correction/Rebound**, blend slow and fast returns using ex-ante mixing parameters a_{Co},a_{Re} estimated to maximize Sharpe ratios (shrink-wrapped to [0,1]) .

- Portfolios equally weight assets within each asset class and then equally across equities, bonds, and commodities.

**4. Performance Comparison**

- Over 1990–2022 at 10% volatility:
  - **Static 12-mo**: ~6.4% annualized return (0.64 Sharpe), virtually 0% in 2009–2019.
  - **Dynamic (2- and 12-mo blend)**: ~9% annualized return (0.80 Sharpe), ~3.4% in 2009–2019—with almost half of gains coming in months following turning points .

**5. Conclusions and Implications**

- Trend-following’s “Achilles’ heel” is whipsaws at trend breaks.
- The post-GFC rise in turning-point frequency helps explain why many CTAs underperformed in 2009–2019.
- A simple dynamic blending rule can substantially recover returns by adaptively emphasizing faster signals after corrections and rebounds.
- Further applications could tailor both lookback horizons and asset-class allocations to exploit heterogeneous turning-point dynamics.

This approach sheds light on when and why classic trend strategies falter—and offers a practical way to “repair” them using only lagged return signals.

## Momentum Turning Points

Here’s a concise overview of **“Momentum Turning Points”** by Goulding, Harvey & Mazzoleni (2023) :

**1. Motivation and Conceptual Framework**

- Classic time-series (TS) momentum (trend-following) uses a single look-back horizon—often 12 months (“slow”)—to go long when past returns are positive and short when negative. Fast momentum (e.g. 1-month) reacts more quickly but is noisier.
- **Turning points** occur when slow and fast signals disagree, marking potential trend reversals that tend to inflict “whipsaw” losses on static strategies .

**2. A Simple AR(1) Model of Trend and Noise**

- Expected excess returns follow μₜ = ϕ μₜ₋₁ + εₜ (persistence ϕ), while realized returns rₜ = μₜ + zₜ include noise.
- The **noise ratio** θ captures the fraction of realized-return variance due to noise.
- Closed-form Sharpe ratios show:
  - Slow (12 mo) dominates when persistence is high and noise is large.
  - Fast (1 mo) shines when noise is low or around turning points .

**3. Empirical “Market Cycles” from Realized Returns**

- Define four observable states each month by the signs of 12- and 1-month returns:
  1. **Bull** (both ≥ 0)
  2. **Correction** (slow ≥ 0, fast < 0)
  3. **Bear** (both < 0)
  4. **Rebound** (slow < 0, fast ≥ 0) .
- Over the U.S. 1969–2018 sample, these occur ~48%, 18%, 17% and 17% of the time, respectively.

**4. Conditional Return Patterns**

- **Corrections** tend to revert: ~61% are followed by Bull/up months. Thus, fast short-bets in Corrections often lose, favoring slower positions.
- **Rebounds** tend to continue: ~56% are followed by up months, so fast long-bets in Rebounds are rewarded .

**5. Intermediate & Dynamic-Speed Strategies**

- Blend slow and fast weights via a parameter a∈[0,1]:

  wₜ(a) = (1–a)·wₛₗₒw,ₜ + a·w_{fast,ₜ}.

- The “medium” strategy (a=½) scales back positions when signals conflict, reducing whipsaws.

- **Dynamic-speed**: estimate state-conditional speeds a₍Co₎ and a₍Re₎ for Corrections and Rebounds, using historical data, then apply them going forward.

**6. Performance Highlights**

- **Static** medium-speed (a=½) often outperforms the average Sharpe of pure slow and pure fast, across U.S. and 20 international equity markets .
- **Dynamic** strategies—slower after Corrections, faster after Rebounds—capture most of the lost returns post-turning-point and typically beat both static slow and static fast on risk-adjusted grounds.

**7. Conclusions & Implications**

- Turning-point risk is the “Achilles’ heel” of classic trend-following.
- Simple blending of slow and fast momentum, especially when tailored to market-cycle states, can substantially recover returns by mitigating whipsaws and exploiting post-break momentum.
- These insights offer a practical recipe for more resilient, adaptive momentum strategies across asset classes and geographies .

## Style Switching and Asset Pricing

Here’s a structured summary of **Wang (2024), “Style Switching and Asset Pricing”** :

**1. Motivation & Key Insight**

- **Style investing**—allocating capital based on firm “characteristics” (value, momentum, profitability, etc.)—is pervasive but may distort prices via flow‐driven comovements.
- Wang shows that when investors extrapolate past returns, they **switch** between “twin” styles (assets with similar characteristics) and “dual” styles (assets with opposite characteristics), inducing **cross‐asset momentum** among twins and **cross‐asset reversals** among duals .

**2. Conceptual Framework**

- **Characteristics‐based demand**: Investors’ portfolio weights are linear in firm characteristics, $$L_{i,t} = \Omega_t^\prime C_i$$.

- **Extrapolative beliefs**: Expected returns are weighted averages of past returns, so flow into one style comes at the expense of others.

- **Style‐switching** emerges endogenously:

  $$\frac{\partial L_{i,t}}{\partial \text{Return}_{j,t-1}} \propto C_i^\prime (\Theta’\Theta)^{-1} C_j$$,

  negative for duals (reversal) and positive for twins (momentum) .

**3. Data & Construction of Style Signals**

- **Universe**: U.S. common stocks, June 1963–Dec 2021, excluding financials and sub‐$1 shares; prices from CRSP, fundamentals from Compustat; factors from Kenneth French and Global-q.
- **Characteristics**: Value (book-to-market), profitability, investment, volatility, momentum—each standardized cross‐sectionally.
- **Dual/Twin sets**: At each June, compute cosine similarity between firms’ 5-dim vectors; firms with similarity < –0.25 form the **DUAL** style, > +0.25 form the **TWIN** style (excluding same‐industry peers).
- **Style returns**: From July to next June, DUAL (TWIN) signals are the value‐weighted average monthly return of a firm’s dual (twin) peers .

**4. Main Empirical Findings**

1. **Cross‐stock reversals (DUAL)**: Top vs. bottom DUAL quintile spreads ≈ –1.00% /mo (t≈–4.6); five-factor alpha ≈ –1.02% /mo; controlling for momentum and reversal factors deepens the effect to –1.51% /mo .
2. **Cross‐stock momentum (TWIN)**: Top vs. bottom TWIN spread ≈ +1.02% /mo (t≈4.9); robust across factor models with alphas up to +1.57% /mo.
3. **Independence**: DUAL’s reversal persists after purging correlation with TWIN (and vice-versa) .
4. **Fama–MacBeth**: In month-t regressions controlling for industry returns, size–value peers, shared‐analyst coverage, etc., a 1 SD increase in DUAL predicts –0.244% t+1 return; TWIN predicts +0.191% .

**5. Time‐Variation & Horizon Tests**

- **Macroeconomic predictors** (BM, DP, EP, TMS, CAY, etc.) fail to forecast style profits, suggesting these are not mere risk‐premia proxies.
- **Long‐horizon** (Jegadeesh–Titman style): Both DUAL and TWIN pay off over the first 12 months, then drift toward zero—and slightly reverse by 30 months—consistent with eventual correction to fundamentals .

**6. Evidence on Trading Behavior**

- **Institutional flows** (13F): A 1 SD rise in lagged DUAL → –0.072 pp change in institutional ownership; TWIN → +0.070 pp .
- **Investor types**: Active advisors (IIAs/hedge funds) drive style‐switching; pensions, insurance, passive funds show negligible switching .
- **Short sellers**: Higher short‐interest builds on high‐DUAL stocks (sell) and unwinds on high-TWIN (buy)—over 1–12 mo horizons, aligning with style effects.
- **Retail**: Net retail buying in response to TWIN/DUAL is significant only over long horizons, indicating more persistent trend‐following.

**7. Conclusions & Implications**

- **Style‐switching demand** creates predictable **cross‐reversals** and **cross‐momentum** beyond traditional factor models.
- **Active managers** (hedge funds, advisors) are the marginal liquidity providers fueling these effects.
- **Practical takeaway**: Monitoring shifts in performance across empirically derived dual/twin style groups can yield economically large trading signals (≈12% ann. from simple style‐spread strategies).

## Price Discovery and Trading After Hours

Here’s a concise, structured summary of **Barclay & Hendershott (2003), Price Discovery and Trading After Hours** :

**1. Motivation & Setting**

- With the rise of ECNs, trading in U.S. equities now occurs well beyond the 9:30 A.M.–4:00 P.M. core hours.
- The paper asks: **How does after-hours trading—especially in the pre-open (8:00–9:30 A.M.) and post-close (4:00–6:30 P.M.) sessions—affect when, how much, and with what efficiency new information is incorporated into prices?** .

**2. Data & Descriptive Facts**

- **Sample**: All trades & quotes on Nasdaq‐listed stocks from March–December 2000, focusing on the top 250 by dollar volume.
- **Volume & Volatility**: After-hours volume is <5% of daytime volume, yet return volatility remains high—e.g. the last half-hour pre-open has only 5% of day‐volume but ~72% of its volatility .

**3. Who Trades When? Informed vs. Liquidity**

- Using the Easley–Kiefer–O’Hara (EKO) structural model, they estimate the **probability of informed trading (PIN)** in each session.
- **Key finding**: The **pre-open** has the highest PIN (≈25%), followed by the **post-close** (≈21%), with the trading day much lower (≈13%)—showing informed traders disproportionately concentrate in thin-liquidity windows.

**4. Total Price Discovery (Section 4)**

- Measured via the **Weighted Price Contribution (WPC)** to overnight (close–open) and 24-hour (close–close) returns.
- **Result**:
  - **Pre-open** accounts for ~74% of overnight price discovery.
  - **Post-close** contributes ~15%, and overnight (6:30 P.M.–8:00 A.M.) almost none .
  - Over the full 24 hours, 12–19% of total discovery occurs after hours, declining for lower-volume stocks.

**5. Information per Trade (Section 5)**

- Normalizing by trade counts yields the **Weighted Price Contribution per Trade (WPCT)**.
- **Insight**: Individual after-hours trades—especially in the pre-open—move prices much more than daytime trades, reflecting higher information content per trade.

**6. Venue, Public vs. Private & Efficiency (Sections 6–7)**

- **Venue split**:
  - **Pre-open** discovery is almost entirely on ECNs (speed, anonymity).
  - **Post-close** is dominated by market-maker trades, but with much less informed flow.
- **Public vs. Private**: Both public announcements and private signals are impounded pre-open; post-close price moves are weaker signals of private information.
- **Efficiency**: After-hours prices are **less efficient**—bid–ask spreads are wider, temporary reversals are common, and signal-to-noise ratios are lower, especially post-close.

**7. Conclusion**

> **“Trend-following strategies at the monthly trading frequency have experienced notably weaker performance in the expansion period after the global financial crisis of 2008 compared with the decades before. The frequency of turning points … can help explain this phenomenon. … We show that observed market corrections and rebounds carry predictive information about subsequent returns and we utilize such breaks to enhance the performance of trend-following strategies.”**

*(Note: The above conclusion snippet illustrates how breaking (“turning”) points in momentum can be harnessed dynamically; it parallels the paper’s broader message on the value of high-information, off–core‐hours trading.)*

**Implications**: Even with thin liquidity, after-hours sessions—especially just before the open—play a critical role in incorporating both public and private information into prices. Market participants and regulators should recognize that price discovery is not confined to regular trading hours and that post-close/pre-open activity carries outsized informational value.

## Moving Targets

Here’s a concise overview of **“Moving Targets”** by Cohen & Nguyen (Draft: February 1, 2024) :

**1. Motivation & Research Question**

Managers publicize performance **targets** (e.g., revenue, same-store sales, product metrics) in earnings-call presentations. When they fail to hit a given target, they often **shift the discussion** to a different metric—“moving the target” to ensure they still clear a self-set hurdle. This paper asks:

> *Do such shifts convey information about true future performance, and how do markets react?*

**2. Data & Target-Extraction Methodology**

- **Sample**: All U.S. firms’ quarterly earnings-call transcripts, 2006–2020 (≈143 000 calls).
- **NLP approach**: Use spaCy to identify “targets” via named-entity recognition (Products, Money, Percent) plus syntactic parsing to link metrics to their referents (e.g., “12% increase in Mac sales” → target = Mac sales).
- **Moving-Targets metric**: Fraction of prior-year targets dropped in the current call (ranges 0–1; mean ≈0.56).

**3. Key Empirical Findings**

1. **Underperformance after moved targets**
   - Firms in the top quintile of movers (biggest drop in targets) underperform by **0.78 pp per month** (≈9.4% p.a.) over the next quarter; effects persist up to 18 months and do not reverse.
2. **No immediate announcement reaction**
   - On the call day, stock returns are statistically zero—information is only gradually impounded, consistent with investor inattention.
3. **Robust to controls**
   - Results hold controlling for Fama-French factors, earnings surprises, liquidity, firm size, industry, and across equal- and value-weighted portfolios.

**4. Mechanism & Heterogeneity**

- **Complexity & Persistence**
  - Effects are **stronger** when target sets are more complex (many different metrics) or when dropped targets were highly persistent (discussed for ≥3 prior years).
- **Financial vs. Non-financial**
  - Shifts in **non-financial** targets (e.g., subscriber counts, product units) predict larger underperformance than purely financial ones.
- **Analyst attention**
  - When analysts explicitly question a dropped target and management is forced to address it, the underperformance effect is **attenuated**, indicating that **inattention** drives the gradual price drift.

**5. Conclusions & Implications**

- **Investor take-away**: Subtle shifts in reported targets carry **real, predictive** information about future fundamentals and stock performance—market participants often overlook these cues until much later.
- **Broader relevance**: The “moving-targets” phenomenon likely extends beyond earnings calls to other corporate disclosures (bond covenants, M&A prospectuses, etc.) where repeated benchmarks are set and shifted.

This study highlights a simple yet powerful insight: tracking **year-over-year changes** in the metrics firms emphasize can reveal hidden signals about underlying performance that markets tend to underreact to in the short term.

## Confirmatory Bias in Financial Markets

Here’s a structured summary of **“A Mind Is a Terrible Thing to Change: Confirmatory Bias in Financial Markets”** by Pouget, Sauvagnat & Villeneuve (2016) :

**1. Motivation**

- **Confirmatory bias**—the tendency to overweight evidence that supports one’s prior views and disregard contradicting information—is well documented in psychology but under-studied in market settings.
- The paper asks: *How does this bias affect traders’ belief updating, create differences of opinion, and thereby drive trading volume, volatility, momentum, and under-/over-reaction in asset prices?* .

**2. Theoretical Model**

- **Economy**: One risky asset, public signals arrive over T=4 trading dates, followed by a terminal payoff v\in\{0,1\} determined by an unobserved state H or L.
- **Agents**:
  - **Speculators** (1-\lambda mass) are fully Bayesian.
  - **Biased traders** (\lambda mass) suffer confirmatory bias: with probability q they ignore any new signal that contradicts their current belief .
- **Trading costs** (quadratic) prevent infinite arbitrage, so divergent beliefs translate into trade and price effects.
- **Equilibrium price** at each date is a weighted average of speculators’ and biased traders’ posterior beliefs.

**3. Model Implications (Stylized Facts)**

When \lambda q>0, the confirmatory bias generates:

1. **Excess volume**—trading arises whenever biased and rational traders disagree.
2. **Excess volatility**—along “mixed” histories (e.g. good signal then bad), some traders ignore the bad update and keep pushing prices too high (and vice-versa).
3. **Momentum**—because biased traders who have been optimistic are more likely to under-react to subsequent bad news (and vice versa), past price moves predict future moves.
4. **Bubbles & crashes**—after an initial positive signal, biased traders’ optimism fuels further price increases; similarly for crashes after initial bad news .

**4. Novel Theoretical Predictions**

- **Belief dispersion** is higher when past signals have *different* signs vs. when they all agree.

- **Belief updating** is *less* likely in the direction of the latest signal if that signal’s sign conflicts with (a) any *prior* signals, or (b) the trader’s own *last* belief revision.

  These emerge because contradictory news offers more opportunities for biased traders to ignore updates .

**5. Empirical Tests**

Using U.S. quarterly earnings surprises (SUE) and I/B/E/S analysts’ annual-forecast revisions (1982–2014):

1. **Forecast revisions**: Analysts are ~2 pp less likely to revise in the direction of a current surprise when its sign *differs* from the surprise one or two quarters earlier.

2. **Analyst heterogeneity**: When an analyst’s *own* prior revision sign conflicts with a new earnings surprise, she is ~20 pp less likely to update in that direction.

3. **Forecast dispersion**: Cross-analyst dispersion in annual forecasts is *higher* following sign-changes in the last two SUEs.

   All effects remain after controlling for firm size, book-to-market, analyst coverage, realized and implied volatility, and fixed effects .

**6. Conclusions**

- Confirmatory bias alone—parameterized by a single “ignore” probability q—can unify explanations for volume, volatility, momentum, and gradual under-reaction in markets.
- It delivers empirically validated, novel predictions about when and for whom updates will *not* occur, highlighting how subtle belief frictions shape observable price dynamics.

## What Drives Momentum and Reversal?

Here’s a concise, structured summary of **“What Drives Momentum and Reversal? Evidence from Day and Night Signals”** by Li (2024) :

**1. Motivation**

Despite being one of the most robust anomalies, the **sources** of equity momentum and long-run reversal remain debated. This paper leverages the empirical fact that **public news** chiefly moves prices **overnight**, whereas **private information** (revealed through trading) drives **intraday** returns, to disentangle these two channels .

**2. Data & Portfolio Construction**

- **Sample:** U.S. common stocks, January 1926–December 2019.
- **Return Decomposition:**
  - **Overnight return:** Close *t–1* to Open *t*.
  - **Intraday return:** Open *t* to Close *t*.
- **Portfolios:** At each month *t*, sort stocks into deciles by their past J-month **intraday** returns or past J-month **overnight** returns, then hold for K months .

**3. Main Findings**

1. **Intraday-based portfolios** (capturing trading‐driven, private‐info shocks) exhibit **strong momentum** over both short and long horizons, **without** subsequent long-run reversal.
2. **Overnight-based portfolios** (capturing public-news shocks) show **long-run reversal** but **no short-run momentum**.

Together, this cleanly separates the two effects—**momentum** arises from underreaction to private information, whereas **reversal** reflects overreaction (or correction) to public news .

**4. Evidence for the Private-Information Channel**

- **Volume Dependence:** Momentum on past intraday returns is **stronger on low-volume days**, consistent with slower incorporation of private signals when trading is thin.
- **Analyst Forecast Errors:** Stocks with high past intraday returns also exhibit larger subsequent forecast errors, linking intraday gains to information that analysts initially miss.
- **Robustness:** Results persist after controlling for liquidity at the open, stale‐price effects, bid–ask bounces, the “frog-in-pan” inattentiveness hypothesis, and across both pre– and post-1963 samples .

**5. Conclusions**

By decomposing returns into **day** and **night** components, this study demonstrates that:

- **Momentum** predominantly reflects **private‐information diffusion** via trading, and
- **Reversal** predominantly reflects **public‐news corrections**.

This distinction not only clarifies the drivers of these classic anomalies but also suggests that trading strategies should consider the **timing** of information arrival when harvesting momentum or avoiding reversal risk.

## Todo

- Factor Timing
- Estimating General Equilibrium Spillovers of Large-Scale Shocks
- Ambiguity about volatility and investor behavior
- When Smart Beta Meets Machine Learning and Portfolio Optimization
- Selling Fast and Buying Slow: Heuristics and Trading Performance of Institutional Investors
- The Virtue of Complexity in Return Prediction
- The Prediction Framework and High-Dimensional Approximation
- Ambiguity about Volatility and Investor Behavior
- Identifying Risk Factor Regimes with Machine Learning: Implications for Tactical Asset Allocation
- Pairs Trading Using a Novel Graphical Matching Approach
- A Modular Measure of Business Complexity
- Influence of Market States on Security Returns
