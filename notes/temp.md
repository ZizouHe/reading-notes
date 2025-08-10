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

## Selling Fast and Buying Slow: Heuristics and Trading Performance of Institutional Investors

**1. Background & Research Question**

Are experienced institutional investors subject to heuristics, and do these biases differ when they buy versus when they sell? The authors examine whether market experts—who manage large, concentrated portfolios—display skill symmetrically across buying and selling, or whether one decision systematically underperforms .

**2. Data**

- **Source**: Inalytics Ltd database of 783 long-only equity portfolios (average AUM $573 million) from 2000–2016, covering 4.4 million high-stakes trades .
- **Characteristics**: Portfolios are highly active, hold on average 78 stocks, and deviate substantially from benchmarks, with limited cash and no leverage.

**3. Methodology**

- **Counterfactuals**: For each buy (sell), compare realized factor-neutral returns to a “no-skill” strategy that randomly buys (sells) another held position for the same dollar amount.

- **Value-added measure**:

  \Delta R_{\text{buy}} = R_{\text{buy}} - R_{\text{hold}}, \quad \Delta R_{\text{sell}} = R_{\text{hold}} - R_{\text{sell}}

  computed over horizons from 1 week to 1 year .

- **Inference**: Double-clustered standard errors allow serial and cross-sectional correlation.

**4. Main Findings**

- **Buying skill**: Stocks purchased outperform the random-buy benchmark by about **120 bp per annum** over a 1-year horizon .
- **Selling underperformance**: Stocks sold underperform the random-sell benchmark by about **80 bp per annum** at 1 year .
- **Robustness**: Results hold across alternative weighting schemes, matching on characteristics (size, momentum, volatility), excluding microcaps or illiquid names, and unadjusted returns.

**5. Mechanism: Asymmetric Attention & Heuristics**

- **Cognitive allocation**: Managers devote more effort to finding buys; sales receive less systematic attention .
- **Two-stage selling heuristic**:
  1. **Selection**: Attention focuses on positions with **extreme prior returns**.
  2. **Disposition**: Within that set, they sell the **least-conviction** ideas—those with lower intended portfolio weight—leading to costly premature exits.

**6. Earnings-Announcement Evidence**

On days when firms in the portfolio release earnings, selling performance jumps by over **150 bp per annum**, matching buying skill—suggesting PMs *can* sell well when attention is directed .

**7. Conclusions & Implications**

Even top-tier institutional investors succumb to costly selling heuristics, sacrificing significant alpha. The authors recommend:

- **Enhanced feedback** on selling performance (e.g., counterfactual reports)
- **Decision aids** or alternative selling rules to mitigate attention-driven biases .

This study highlights that selling, not just buying, is a critical locus of behavioral bias—even among market experts.

## Ambiguity about volatility and investor behavior

**1. Research Question & Contribution**

The paper asks how **time-varying aggregate ambiguity about volatility**—measured by the V-VSTOXX (the 30-day implied volatility of the Euro Stoxx’s implied volatility)—affects individual investors’ trading and risk-taking . Unlike prior work that focuses on cross-sectional ambiguity aversion, this study exploits **daily innovations in market-based and survey‐based ambiguity** to trace *within-person* responses over time.

**2. Data**

- **Sample**: Over **100,000** retail clients of a major German online broker, covering **23.4 million** trades from **March 2010 to December 2015**.
- **Ambiguity Measures**:
  1. **Short-term**: V-VSTOXX innovations (daily).
  2. **Long-term**: Interquartile range of professional GDP‐forecast standard deviations (quarterly).
- **Investor Survey**: A random subset (n = 644) completed an Ellsberg-urn task, classifying them as ambiguity-averse, neutral, or seeking .

**3. Methodology**

Panel regressions with **investor fixed effects**, relating daily dV-VSTOXX to:

1. **Activity**: Probability of logging in or trading on a given day.

2. **Risk-taking**: Excess buy–sell imbalances (demeaned by each investor’s one-year average) .

   Models control for innovations in expected volatility (dVSTOXX), sentiment (FEARS), market returns, calendar effects, and investor wealth.

**4. Key Findings**

1. **Higher Ambiguity → More Activity**
   - A one-unit rise in dV-VSTOXX raises the daily login likelihood by 0.12 pp and trading likelihood by 0.02 pp (both p < 0.01), economically comparable to well-known attention and wealth effects .
2. **Higher Ambiguity → Less Risk-Taking**
   - Ambiguity shocks **reduce** investors’ excess buy–sell imbalances, indicating a **pull-back from risky assets** that persists for at least ten days .
3. **Heterogeneity by Ambiguity Aversion**
   - Surveyed **ambiguity-averse** investors react **four times more strongly** to V-VSTOXX shocks than the average client, whereas neutral or seeking investors show no significant response .
4. **Robustness**
   - Results hold using the dispersion of forecasters, alternative market-based (Brenner & Izhakian) and newspaper‐based (EPU) measures of ambiguity, and after controlling for expected volatility .

**5. Implications**

Individual investors not only buy less but also **sell more cautiously** when volatility ambiguity spikes—especially if they are ambiguity-averse—suggesting that **trading decisions**, not just initial portfolio choice, amplify the classic “buy high, sell low” patterns under uncertainty. This has important implications for understanding retail flow dynamics and designing tools to mitigate ambiguity‐driven behavior.

## Pairs Trading Using a Novel Graphical Matching Approach

**1. Background & Motivation**

Traditional pairs-trading portfolios select highly cointegrated asset pairs, but often include multiple pairs sharing the same stock. This overlap raises portfolio variance through positive covariance among spreads and drives up transaction costs via higher turnover. The authors propose a graph-theoretic solution to build lower-risk, more diversified pairs portfolios .

**2. Graphical Matching Method**

- **Graph construction**: Represent each stock as a node and each candidate pair as an edge weighted by the strength of cointegration (e.g., negative ADF t-statistic).
- **Maximum weight matching**: Compute a matching (set of edges sharing no nodes) that maximizes total edge weight. This ensures each stock appears in at most one pair, eliminating shared-asset covariance and capping portfolio size at ⌊N/2⌋ for N stocks .

**3. Theoretical Analysis**

- **Return moments**: Derive closed-form expressions for the mean, variance, and covariance of returns for both cointegrated and non-cointegrated pairs (Theorems 1–4).
- **Portfolio Sharpe**: Show analytically that excluding shared-stock covariance (m = 0) raises the portfolio’s Sharpe ratio from ~0.50 under the baseline to ~1.18 under matching, principally by cutting variance in half .

**4. Empirical Implementation & Results**

- **Simulation setup**: Use S&P 500 data (2017–2023), monthly rebalancing, two-year rolling windows for cointegration tests and spread regression. Compare:
  - **Baseline**: Top 250 pairs by lowest p-value.
  - **Matching**: Maximum-weight matching of all candidate edges, selecting ≤ 250 disjoint pairs.
- **Trading signals**: Both z-score (standardized spread) and robust q-score (quantile-based) triggers.
- **Performance**:
  - **Gross Sharpe**: Matching ≈ 1.23 vs Baseline ≈ 0.48 (S&P 500 ≈ 0.59).
  - **Net returns** (after realistic 1% annual turnover cost): Matching ≈ 7–8% p.a. vs Baseline negative.
  - **Turnover & Concentration**: Matching reduces turnover by ~66% and enforces single-stock concentration = 1, whereas baseline’s concentration averages > 10 

**5. Conclusions & Extensions**

Graphical matching transforms pairs trading by systematically avoiding shared-stock overlap, yielding superior risk-adjusted returns, lower trading costs, and muted drawdowns. The framework naturally extends to hypergraph “multi-asset” strategies and alternative edge-weight definitions, opening rich avenues for future portfolio-construction research .

## Using GPT models to measure the complexity of business transactions

**1. Motivation & Definition**

The authors introduce **business complexity** as a decision-maker’s difficulty in understanding the economic substance of a firm’s transactions and financial position. Traditional proxies (e.g., report length, Fog index) miss aspects like transaction uniqueness. They propose an algorithmic, fact-level measure to capture this construct .

**2. Data & Methodology**

1. **Data**: 58,148 iXBRL-tagged 10-K and 10-Q filings (July 2016–May 2024), comprising over eight million numeric “facts” in footnotes.
2. **Model**: Fine-tune Meta’s open-source Llama 3 (8B) on 200,000 sentences with embedded iXBRL tags, teaching it to predict each tag based on surrounding text .
3. **Complexity Measure**: For each fact, complexity = 1 – (model’s confidence), where confidence is derived from token probabilities on the predicted tag .

**3. Validation**

- **Fact-level**: Confidence correlates 0.75 with tag-prediction accuracy; standard tags yield 90% vs. 78% confidence on custom tags .
- **Firm-level**: Average filing complexity negatively predicts the speed of price discovery (intra-period timeliness), even after controlling for length, Fog, segment count, and unique-tag proxies .

**4. Disaggregation & Category-Level Insights**

- **Within-filing heterogeneity**: Firms’ filings show substantial variation across individual facts.
- **By transaction type**: Collaborative arrangements, government assistance, and contingencies rank among the most complex; earnings per share and goodwill among the least .

**5. Debt Complexity Application**

Focusing on debt contracts, the paper finds:

- **Determinants**: Higher debt complexity in smaller, riskier, less profitable, and less‐covered firms—consistent with financial constraints .
- **Outcomes**:
  1. **Interest persistence**: Complex-debt firms exhibit more stable interest expenses quarter to quarter.
  2. **Performance in stress**: During the July 2021–June 2022 tightening cycle, firms with more complex debt outperformed peers, suggesting complexity can mitigate financing risk .

**6. Conclusion**

The GPT-based, iXBRL-driven measure delivers a flexible, disaggregated proxy for business complexity. It:

- Captures transaction uniqueness beyond standard text measures
- Impedes price formation, reflecting real processing costs
- Reveals why vulnerable firms adopt complex debt to manage risk

This fact-level approach opens avenues for future research on complexity in other disclosure contexts and across different user sophistication levels .

## Identifying Risk Factor Regimes with Machine Learning: Implications for Tactical Asset Allocation

1. **Motivation & Regime Tagging**

   Financial risk factors (e.g. equity returns) exhibit distinct “crash” vs. “normal” regimes that—if detected ex-ante—can guide tactical tilts. This paper defines an **Equity Factor** as a 7-index global basket and **tags crash periods** whenever its cumulative drawdown breaches –10%, including both peak-to-trough and trough-to-recovery phases .

2. **Feature Construction & Selection**

   Over **500 features** are engineered from real-time market and macro data: index returns, FX forwards, commodity and volatility surfaces, CDS spreads, economic-surprise indices, Mahalanobis turbulence, absorption ratio, risk-adjusted momentum, skewness/kurtosis, option-flow signals, term-structure slopes, and more . A univariate filter—combining point-biserial correlations and mutual-information rankings—reduces this to the most predictive subset before modeling.

3. **Machine-Learning Framework**

   Six classifiers (Logit, SVM, Random Forest, XGBoost, Neural Net, plus a Probit + PCA benchmark) are trained in a **rolling, temporal 4-fold cross-validation** with hyperparameter tuning. **Shapley values** from cooperative game theory provide feature-level interpretability, mitigating the “black-box” concern .

4. **Out-of-Sample Performance**

   The **ensemble average** of all ML models achieves the highest ROC AUC, Brier Skill, F1 and Matthews’ MCC scores. When used to time one-month ahead crash probabilities in a simple long-only equity strategy, the ML ensemble delivers a **Sharpe ≈ 0.80**—well above trend-following, VIX-timing, volatility-targeting, and hidden-Markov benchmarks (each 0.52–0.76) . Spanning regressions confirm the ML signals generate statistically significant alpha versus those benchmarks.

5. **Tactical Applications**

   - **Probability-Weighted Rotation**: Allocating dynamically between ‘risk-on’ (equities, high yield) and ‘risk-off’ (IG bonds, inflation-linked, gold, CTA) buckets based on predicted crash probability improves portfolio Sharpe by ~0.1 versus a static 80/20 split.
   - **Regime-Aware Risk Views**: Incorporating the same probabilities into covariance forecasts and risk-parity allocations yields further gains, demonstrating broad applicability beyond pure timing .

   By systematically tagging regimes, leveraging rich feature sets, and applying interpretable ML, this approach meaningfully enhances tactical asset-allocation decisions.

## **Using accounting earnings and macro indicators to estimate firm-level systematic risk** 

**Core idea**

Instead of proxying “the market” with listed-firm indexes, the authors use two macro indicators—changes in Total Factor Productivity (TFP) and changes in household wealth (excluding equities)—and regress firms’ (portfolio-level) earnings on these to estimate two *earnings betas*: a supply beta (to TFP) and a demand beta (to wealth). They argue these capture aggregate risk more broadly than public-equity indexes and, crucially, align in timing with annual earnings.

**Why this approach**

- Public-equity indexes omit large swaths of aggregate assets (private firms, debt, human capital, durables, non-profits, public assets), so index-based “market” risk is measured with error (Roll, 1977).
- Annual earnings and macro indicators are realized outcomes in the same period; returns are forward-looking and thus misaligned for capturing contemporaneous co-movements.  

**Measures & data (1964–2018)**

- **Supply shocks**: ΔTFP (Fernald method).
- **Demand shocks**: Δhousehold wealth **excluding equities** (Fed Z.1); first-differenced to reduce serial correlation.
- **Earnings**: operating income (OIADP) minus preferred dividends (fallback to IB), winsorized; portfolio-level changes scaled by market cap at t–2. 
- The macro series coverage is 55 annual observations; ΔTFP and ΔWealth are correlated but not identical sources of risk.

**Method (estimation & pricing)**

1. Sort firms annually by characteristics; estimate portfolio-level regressions of earnings changes on ΔTFP and/or ΔWealth to get supply/demand betas; assign those betas back to firms. 2) Run Fama–MacBeth cross-sectional tests of average returns on these betas.

**Main findings**

- **Two distinct sources of systematic earnings risk**: firm supply and demand betas are **negatively correlated**, reflecting heterogeneous exposure to productivity vs. wealth shocks across firms/industries. 
- **Pricing**: Both supply (TFP) and demand (wealth) earnings betas earn **positive, significant risk premia** in Fama–MacBeth tests; a two-beta model outperforms an index-earnings-beta model (higher adjusted R²).
- **Links to classic characteristics**: Higher B/M and smaller size portfolios have **higher** supply and demand earnings betas; higher asset growth has **lower** betas; momentum patterns are generally increasing but somewhat sensitive to scaling. 
- **Mechanism vs. “factors”**: After controlling for the two earnings betas, the combined explanatory power of B/M, momentum, size, and asset growth **drops by ~25%**, suggesting part of their “pricing” reflects underlying systematic risk exposures captured by supply/demand betas.

**Validation & alignment checks**

Aggregate earnings changes co-move contemporaneously with both ΔTFP and ΔWealth; by contrast, stock returns predict *future* earnings and macro outcomes rather than contemporaneous ones—supporting the earnings–macro alignment premise.

**Limitations (as the authors note)**

The macro instruments are imperfect; firm-level monthly return noise keeps cross-sectional R²’s small; momentum results can depend on the earnings deflator; several other signals (e.g., E/P, PEAD, profit margin) don’t show similar associations.

## When Smart Beta Meets Machine Learning and Portfolio Optimization

**What the authors ask**

Why have popular smart-beta factors underwhelmed since 2005, and can we do better by (i) diversifying across many academic factors, (ii) using ML to map factor exposures to expected **alpha**, and (iii) building long-only portfolios with a **mean tracking-error** optimizer (MTO) instead of simple tilts?  

**Data & set-up**

- **Universe/period.** Stocks from **38** MSCI ACWI countries; country start is the later of **Jan 2005** or when ≥50 stocks are eligible. Data sources: Datastream (prices), Worldscope (financials), IBES (analyst forecasts). Benchmarks are float-adjusted cap-weighted.  
- **Signals.** They compute **86** of the **97** McLean & Pontiff (2016) cross-sectional signals globally (some are infeasible with available data). 
- **Portfolio overlay (baseline).** Start from each country’s cap-weighted index, overlay a long–short gradient portfolio on a given signal, remove shorts to keep it long-only. 

**Methods**

1. **Many-factor composites.** Besides textbook factors, they form a broad composite from McLean–Pontiff signals; across 2005–2022, the composite averages **1.83%** excess in the US and **2.38%** globally (long-only overlays). 
2. **ML for expected alpha.** Predict one-month **alpha** with (a) OLS, (b) **ridge (L2)** to reduce overfitting, and (c) **gradient boosting (XGBoost)** for nonlinearities/interactions; estimation is cross-sectional and rolled forward. 
3. **Optimization (MTO).** Maximize expected return minus a penalty on **tracking error** using a stock covariance matrix; impose tight stock/industry constraints (e.g., ~±2% at stock/industry levels) to avoid concentration.  

**Key results**

- **Popular factors disappointed; broad diversification helped.** From 2005–2022, popular long-only factors delivered modest excess returns (e.g., US average ~**1.11%**), whereas equally-weighted many-factor composites performed more consistently across countries.  
- **ML beats simple averaging/OLS.** In the **United States**, long-only overlays based on predicted alphas earned **1.56%** (OLS), **1.77%** (ridge), and **2.11%** (gradient boosting) excess per year; corresponding alphas were **2.18%**, **2.30%**, and **2.55%**—all beating the simple composite. 
- **Optimization adds another step-change.** Adding MTO lifts the **US** excess return to **4.08%** with **4.16%** alpha (using ML ERs), illustrating the benefit of sizing by signal strength and risk. 
- **Global summary (cap-weighted across countries).** Versus long-only overlays, MTO raises excess returns from **2.40 → 3.02%** (OLS), **2.72 → 3.43%** (ridge), and **3.02 → 4.83%** (gradient boosting); information ratios likewise improve.  
- **Information ratios up to ~1.95.** For cap-weighted countries, IRs climb from **0.91** (87-factor composite) to **1.15/1.26/1.62** (OLS/ridge/GB overlays) and to **1.37/1.50/1.95** with MTO. 

**Why it matters**

The evidence suggests the **factor zoo is useful when diversified**, and that **regularized/nonlinear ML** plus **tracking-error-aware optimization** can turn weak smart-beta tilts into stronger, more benchmark-relevant long-only portfolios (higher excess returns **and** higher IRs).  

**Notable caveats the authors flag**

- Many markets in the 38-country set are small/hard to access; results show robustness, not necessarily implementable investability in all markets. 
- Reported turnovers can be high; exhibits include turnover panels alongside returns/IRs (practical trading costs matter). 

## Business News and Business Cycles

The authors use a topic model on ~800k full-text WSJ articles (1984–2017) to measure “news attention” across 180 interpretable topics. These attention series closely track economic activity, explain **~25%** of aggregate U.S. stock‐market return variation, and add incremental predictive power for output and employment in a text-augmented VAR—especially the **“recession”** topic. 

**Data & method**

- **Corpus:** Full text of ~800,000 *Wall Street Journal* articles, 1984–2017. 
- **Model:** Latent Dirichlet Allocation (LDA) extracts **topics** (probability distributions over terms) and **article-level mixtures**; aggregating mixtures over time yields monthly **news attention** per topic.  
- **Specification:** Model selection favors ~170–180 topics; authors use **K=180**.  

**What they find**

- **News structure:** Attention exhibits persistent, seasonal, and emergent patterns—e.g., *recession* & *health insurance* (persistent), *elections* & *earnings forecasts* (seasonal), *terrorism* & *natural disasters* (emergent).  
- **Macro correlations (lasso, five topics per series):**
  - Industrial production: “**recession**” and “**oil market**” attention negatively associated; a 1σ rise in “recession” attention ↘ output growth by **0.38σ**. Employment ↘ **0.61σ**.  
  - **Stock returns:** Five topic attentions explain **R² ≈ 0.25** contemporaneously; “recession” is the largest (≈ −0.35). Benchmarks underperform (CFNAI R²≈0.02; FRED-MD R²≈0.09). Out-of-sample: R²≈**17.8%** (returns), **43.6%** (volatility).   
- **Finance/activity examples:** Attention to “**IPOs**” and “**venture capital**” tracks IPO volume; “**takeovers**” & “**control stakes**” track LBOs (explaining **~58%** of variation).  
- **Text-augmented VAR (macro + news):**
  - “**Recession**” attention **predicts future output and employment** beyond stock prices, rates, and uncertainty measures.  
  - Impulse responses: a positive recession-attention shock lowers stock prices on impact (~−5%), cumulating to ~−7% over a year when news is ordered first; effects remain sizeable under alternative ordering and exceed those from EPU shocks.  
- **Narrative retrieval:** Combining VAR dynamics with topic weights surfaces the specific WSJ articles that best “explain” forecast movements (e.g., headlines about confidence and growth concerns).  

**Why it matters**

- Shows that **unstructured news text** provides a compact, interpretable state variable for the economy, resolving part of the classic “low R²” puzzle for returns and adding **incremental** macro forecasting power.  

**Caveats & scope**

- The approach is **descriptive** for many results (correlations), not causal; narratives are meant to interpret fluctuations rather than identify structural shocks. 
- Coverage is WSJ-specific (though very broad); topic modeling choices (e.g., K) are data-driven but still modeling assumptions. 

## Investor attention and stock returns under negative shocks

The paper builds a “clean” investor‐attention measure from China’s **Dragon & Tiger (DT) list** and shows that when attention spikes **during negative shocks**, subsequent stock returns tend to be **lower**. The effect is most evident in the following month and is stronger for certain firm types and market states. 

**What counts as a “negative shock”**

They test four situations when a stock appears on the DT list and conditions are bad:

1. negative **same-day cumulative return**; 2) negative **current monthly cumulative return**; 3) negative **monthly cumulative net purchases by top 10 institutions**; 4) **bottom-30%** monthly **total trading** by top 10 institutions. 

**Measuring attention**

Attention is proxied three ways from the DT list: **Times** (monthly appearances), **Purchase** (net purchase ratio), and **Atrade** (top-10 total trading ratio). These appear in the regression as current and lagged variables (Times, Purchase, Atrade, and their t−1 versions). 

**Data & setup**

A monthly panel of Shanghai/Shenzhen **A-shares (2014–2018)**; regressions include firm controls (Size, Tvol, Turnover, PB) and **time fixed effects**. 

**Core findings**

- Across all four negative-shock definitions, **more attention → lower returns**, especially at **t−1** for Purchase/Atrade; **R² ≈ 0.55.** 

- **Bear vs. bull markets.**

  • **Bear:** Times, Purchase, and Atrade are **significantly negative contemporaneously**—attention reacts quickly to bad news and associates with lower returns. 

  • **Bull:** Times stays negative; **Purchase and Atrade flip sign**—**positive now but negative at t−1**, consistent with sell-pressure showing up before a short-run adjustment. 

**Cross-sectional patterns**

- **Institutional ownership:** The negative attention–return link in the **next month** is **stronger when institutional ownership is low**. 
- **Firm age:** The next-month negative effect is present for both, but **stronger for young firms** (larger absolute coefficients than mature firms). 
- **State ownership:** Effect exists for both, but **stronger for non-SOEs**. 

**Takeaways**

- **Negative attention effect:** When bad news hits, **heightened attention reliably predicts lower subsequent returns**—robust across market states and firm characteristics. 
- **Why it matters:** Results speak to **limited attention and investor behavior** in emerging markets and can inform **regulators** aiming to curb bubbles and herding. 

**Caveats & scope**

Authors note the approach is likely **more relevant in emerging markets**; in mature markets, investors rely more on fundamentals and diversified information sources, making DT-style lists less informative. 

## Emotional State and Market Behavior

Here’s a tight summary of **Breaban & Noussair (2018), “Emotional State and Market Behavior” (Review of Finance)**:

- **Question.** Do traders’ real-time emotions help explain bubbles and crashes? The authors pair classic laboratory asset markets with automated facial-expression (FaceReader) measures of emotions/valence. 
- **Design (lab markets).** 13 sessions at Tilburg University; 6–11 traders each; continuous double-auction; 15 periods per market (2 minutes each). Asset pays dividends drawn from {0, 8, 28, 60}; expected dividend per period = 24, so fundamental value is f_t=384-24t.   
- **Big picture pattern.** Markets typically show a bubble then a sharp crash toward fundamentals. 
- **Core findings.**
  - **Initial mood → price level.** More positive **valence before trading** is associated with **higher subsequent average prices** (Spearman ρ ≈ 0.62, p<.01). Conversely, **more fear** before trading is associated with **lower average prices** (ρ ≈ −0.83, p=.01).  
  - **Within-session dynamics.** Higher **average fear in period t−1** predicts a **price drop in period t** (fixed-effects logit). Neutrality, happiness, and anger are associated with a lower chance of a price decrease. 
  - **Individual behavior.** Positive emotion is linked to **buying** and overpricing; **fear** is linked to **selling** and price declines (captured already in the abstract/overview). 
  - **During crashes.** Traders who display **more neutral** expressions in the crash tend to end with **higher earnings** (correlation ≈ 0.21; also fewer units held—i.e., less “bag-holding”—by more neutral traders). 
  - **Loss aversion link.** Ex-ante **loss aversion** correlates **positively with fear** and **negatively with valence** measured before trading. 
- **Interpretation.** Emotions—especially **valence** and **fear**—are tightly intertwined with market outcomes: upbeat cohorts sustain higher prices/bigger bubbles; rising fear presages selloffs. The results line up with psychological theories where positive affect lowers perceived risk while fear heightens it.
- **Caveats.** Lab setting with small cohorts and automated emotion detection; FaceReader captures facial proxies for emotion, not self-reports or physiology.

## Todo

- Factor Timing
- The Virtue of Complexity in Return Prediction
- The Prediction Framework and High-Dimensional Approximation
- Influence of Market States on Security Returns
