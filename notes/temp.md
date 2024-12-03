# Linkage

## Momentum Information Propagation through Global Supply Chain Networks

#### **Introduction**
The paper introduces a novel customer momentum strategy utilizing global supply chain network data. The authors address a gap in financial strategies by applying their approach to large-scale global supply chains, expanding beyond the traditionally explored US and Japanese stock markets. 

#### **Methodology**
1. **Network Theory**: This foundational approach models the interactions and relationships within supply chain networks.
2. **Medium-Term Momentum Propagation**: The authors examine how momentum propagates through supply chains over medium time periods.
3. **Higher-Layer Customer Information**: The strategy incorporates complex data, such as transaction periods and customer-to-supplier sales ratios.

To validate the model, the authors conducted empirical analyses on global stock markets using a long–short portfolio analysis.

#### **Data**
The study utilizes:
- **Supply Chain Data**: Covering 210,000 relationships globally, including approximately 18,000 suppliers and 19,000 customers (e.g., sourced from the FactSet Supply Chain Relationships database as of December 2019).
- **Quantitative Metrics**: Transaction periods and the sales ratio (percentage of customer relationships contributing to total supplier sales) are key elements.

#### **Findings**
1. **Performance of the Proposed Strategy**:
   - Achieved a **4.5% annual return**, outperforming standard momentum strategies from previous studies.
2. **Global Applicability**:
   - The strategy proved more effective than previous models (standard and customer momentum), showcasing robustness across diverse financial markets.

#### **Conclusion**
The proposed momentum strategy leverages supply chain network data to yield superior performance in global financial markets. By integrating advanced data modeling techniques and empirical validations, the study highlights the untapped potential of supply chain analytics in driving financial decision-making.

## The Dynamics of Disagreement

#### **Introduction**
This paper investigates how differences in investor beliefs (disagreement) evolve in response to large information shocks. The authors use a unique dataset and focus on securities constrained by short selling. Two groups of investors—overreacting optimists and underreacting pessimists—are analyzed to understand their influence on asset pricing.

#### **Methodology**
The authors employ:
1. **Portfolio Sorting**: Stocks are sorted based on past returns, institutional ownership ratio (IOR), and short-interest ratio (SIR).
2. **Cumulative Abnormal Returns (CAR)**: Examines how stock prices deviate over 5 years post-formation.
3. **Disagreement Measures**: Uses borrowing costs, lending fees, and forecast dispersion as proxies for disagreement.
4. **Dynamic Modeling**: A heterogeneous-agent model incorporating behavioral biases like overconfidence and slow information diffusion is proposed to explain observed patterns.

#### **Data**
1. **Period**: Analysis spans from May 1980 to June 2020, with a focus on constrained stocks.
2. **Sources**:
   - Stock data: Center for Research in Security Prices (CRSP).
   - Borrowing fees: Markit database.
   - Analyst forecasts: IBES database.
3. **Sample**:
   - 27 portfolios derived from a 3×3×3 sort on past returns, IOR, and SIR.
   - Markit lending fee data from 2004 to 2020.

#### **Findings**
1. **Return Dynamics**:
   - **Constrained Winners** (stocks with positive shocks): Show prolonged negative returns over 5 years, reflecting overly optimistic beliefs of certain investors.
   - **Constrained Losers** (stocks with negative shocks): Exhibit negative returns initially, stabilizing after one year as pessimistic beliefs adjust.
2. **Belief Dynamics**:
   - Overreacting optimists persist for up to 5 years post-positive shocks.
   - Disagreement between investors persists over 5 years, as shown by high borrowing costs and forecast dispersion.
3. **Momentum and Reversal**:
   - Results align with momentum and reversal patterns but indicate that constrained securities amplify these effects due to limits on arbitrage.

#### **Conclusion**
The study highlights how differences in investor beliefs contribute to asset pricing anomalies. Constrained stocks reveal long-term belief adjustments, challenging traditional momentum and reversal models. The proposed behavioral model captures these dynamics and offers insights into the persistence of mispricing in financial markets.

## Cross-stock momentum and factor momentum

#### **Introduction**
This paper explores the dynamics of cross-stock momentum, emphasizing its distinction from factor momentum. It identifies asymmetric and symmetric components within cross-stock linkages, building a comprehensive framework for understanding the lead-lag relationships across stocks. The study highlights the profitability of leveraging data-driven linkages to enhance stock return predictions.

#### **Methodology**
1. **Principal Portfolio (PP) Method**:
   - Uses a prediction matrix to relate stock returns to lagged signals across the cross-section of stocks.
   - Employs singular value decomposition (SVD) for dimensionality reduction and analysis of cross-stock linkages.

2. **Asymmetric and Symmetric Linkages**:
   - **Asymmetric Linkages**: Capture directional relationships (e.g., whether stock A leads stock B).
   - **Symmetric Linkages**: Reflect simultaneous co-movements between stocks over different time horizons.

3. **Data Sources**:
   - Stock data from CRSP spanning 1926–2018.
   - Industry classifications, analyst coverage, and factor returns from standard financial databases.

#### **Findings**
1. **Cross-stock Momentum Profitability**:
   - Generates a **monthly alpha of 1.62%** relative to a five-factor model, highlighting its economic significance.
   - Asymmetric components alone provide a monthly alpha of 1.02%, underscoring their unique contribution.

2. **Comparison with Factor Momentum**:
   - Cross-stock momentum differs from factor momentum through the presence of asymmetric relationships, which are absent in factor momentum.
   - Factor momentum profits are mainly driven by high cross-stock links.

3. **Time-varying Linkages**:
   - Cross-stock linkages are less persistent than previously identified linkages, such as those based on geographic or industry connections.
   - Predictability is attributed to short-term, time-varying linkages.

4. **Machine Learning Insights**:
   - SVD results confirm that key cross-stock momentum features align with theoretical expectations, validating the framework’s utility.

#### **Conclusion**
The study establishes cross-stock momentum as a distinct and profitable strategy, driven by asymmetric lead-lag relationships. By leveraging data-driven linkages and advanced modeling techniques, it provides insights into the interplay between cross-stock and factor momentum. This contributes significantly to the asset pricing and portfolio management literature.

## Understanding momentum and reversal

#### **Introduction**
The paper revisits the momentum and long-term reversal phenomena in financial markets through the lens of conditional asset pricing models. The central question addresses whether these phenomena can be explained by time-varying risk compensation linked to dynamic factor exposures.

---

#### **Methodology**
1. **Data**:
   - Spans 1966–2014.
   - Over 12,800 unique stocks and 1.4 million stock-month observations.
   - Employs characteristics such as momentum, long-term reversal, and firm-specific traits.

2. **Instrumented Principal Component Analysis (IPCA)**:
   - The key modeling framework allowing time-varying factor exposures (betas) driven by observable firm characteristics.
   - Uses latent factors instead of predefined ones (e.g., Fama-French factors) for better flexibility and accuracy.

3. **Empirical Models**:
   - Models conditional factor loadings based on firm traits.
   - Tests various return predictors (momentum, residual momentum, and model-based expected returns).

---

#### **Findings**
1. **Momentum and Conditional Risk**:
   - Momentum is strongly linked to time-varying risk exposure.
   - The conditional factor model explains a significant portion of the momentum premium.
   - Raw momentum signals provide an 8.3% annualized return; the model-based strategy achieves 33.6%, with much higher precision.

2. **Long-Term Reversal**:
   - Long-term reversal is partially captured by the same conditional risk framework, though it remains distinct from momentum effects.
   - Time-varying factors subsume predictive power from both momentum and reversal signals.

3. **Residual Momentum**:
   - Contrasts with previous findings; residual momentum (momentum in residuals after controlling for conditional factors) is less significant.
   - Suggests that most of the momentum phenomenon is driven by conditional factor exposures rather than idiosyncratic components.

4. **Out-of-Sample Performance**:
   - The IPCA model maintains predictive strength even in out-of-sample tests.
   - Produces robust results with an annualized Sharpe ratio of 2.29 compared to 0.48 for traditional momentum.

5. **Robustness**:
   - Excluding momentum or all return variables still preserves significant explanatory power.
   - Results are consistent across different test specifications and with alternate factor structures.

---

#### **Conclusion**
The study demonstrates that conditional factor models, which account for dynamic risk exposures, can explain much of the momentum and reversal phenomena. These findings challenge previous notions that momentum is purely an anomaly or a residual effect, positioning it instead as a manifestation of systematic risk compensation.

## Psychological barrier and cross-firm return predictability

#### **Introduction**
The paper investigates the delayed price response to news about economically linked firms, such as suppliers and customers, through the lens of the psychological anchoring effect of the 52-week high price. The study posits that this effect distorts belief updating and contributes to market inefficiencies like underreaction to public information.

---

#### **Methodology**
1. **Data**:
   - Timeframe: January 1981 to December 2018.
   - Includes supplier firms traded on NYSE, Amex, and Nasdaq.
   - Customer-supplier link data derived from Compustat customer segment files.

2. **Key Variables**:
   - **Customer Returns (CR)**: Equal-weighted returns of a firm's customers.
   - **Nearness to the 52-Week High (PRC)**: Ratio of a stock’s month-end price to its 52-week high price.

3. **Portfolio Sorting**:
   - Double sorting firms by customer returns (CR) and PRC into 25 portfolios.
   - Analysis of Fama-French-Carhart (FFC4) alphas for each portfolio.

4. **Return Decomposition**:
   - Splits returns into components: customer momentum, 52-week high effect, and their interaction.
   - Fama-MacBeth regressions are used to compute these components.

---

#### **Findings**
1. **52-Week High Effect**:
   - The nearness to the 52-week high significantly moderates the predictability of supplier returns based on customer returns.
   - Returns for firms close to their 52-week high are higher when customers exhibit strong performance.

2. **Interaction Effect**:
   - Interaction between CR and PRC produces a positive and significant FFC4 alpha of 1.44% per month, explaining a substantial portion of customer momentum.

3. **Analyst Behavior**:
   - Analysts’ reactions to news about linked firms are influenced by the 52-week high effect, resulting in underreaction to economically relevant news.

4. **Robustness**:
   - Results hold under alternative risk adjustments (e.g., Fama-French models) and across other economic linkages like geographic and industry momentum.

---

#### **Conclusion**
The study introduces the 52-week high effect as a psychological barrier that distorts market responses to news about linked firms. This effect significantly contributes to cross-firm return predictability and provides a unified explanation for the underreaction observed in customer and geographic momentum strategies.



## Style Switching and Asset Pricing

#### **Introduction**
The paper investigates how style-switching behavior in asset allocation impacts asset pricing and market dynamics. Style switching refers to investors reallocating funds between investment styles based on past performance, leading to cross-asset momentum and reversal patterns.

---

#### **Methodology**
1. **Conceptual Framework**:
   - A portfolio choice model integrating **characteristics-based trading** and **extrapolative beliefs**.
   - Identifies **dual styles** (assets negatively correlated in characteristics) and **twin styles** (positively correlated).
   - Examines how demand shifts between dual and twin styles affect price dynamics.

2. **Empirical Strategy**:
   - Dual and twin styles are constructed using **cosine similarity** of firm characteristics (value, profitability, investment, volatility, momentum).
   - Data sources include CRSP and Compustat (1963–2021).

3. **Portfolio Analysis**:
   - Stocks are sorted into quintile portfolios based on dual and twin style signals.
   - Analyzes return spreads and their persistence over different horizons.

4. **Regression Analysis**:
   - Fama-MacBeth regressions test the robustness of the cross-asset momentum and reversal effects.
   - Controls for industry effects, shared analyst coverage, and firm-specific characteristics.

---

#### **Data**
- Sample includes NYSE, NASDAQ, and AMEX stocks (1963–2021).
- Variables: firm characteristics (e.g., book-to-market ratio, profitability, momentum), institutional ownership, and macroeconomic factors.
- Additional data on institutional trading (13F filings) and retail trading (TAQ millisecond tools).

---

#### **Findings**
1. **Cross-Asset Reversals and Momentum**:
   - **Dual styles** exhibit **reversal patterns**: Stocks with high dual-style returns tend to underperform subsequently.
   - **Twin styles** display **momentum patterns**: Stocks with high twin-style returns tend to outperform.

2. **Institutional Trading**:
   - Institutional investors drive style-switching, reallocating funds based on dual/twin performance.
   - Active institutions (e.g., hedge funds) are primary agents of style-based demand shifts.

3. **Short Sellers and Retail Investors**:
   - Short sellers align with style-switching behavior, increasing short interest in high-dual stocks.
   - Retail investors exhibit style-following tendencies, but with less consistent patterns.

4. **Long-Term Effects**:
   - Style strategy returns reverse after 30 months, indicating price deviations due to demand shifts eventually normalize.

5. **Macroeconomic Insensitivity**:
   - Style effects are weakly correlated with macroeconomic conditions, supporting the behavioral rather than systematic risk-driven nature of the findings.

---

#### **Conclusion**
The study identifies style switching as a significant driver of cross-asset return predictability, creating distinct momentum and reversal effects. These findings highlight the role of active institutional trading in shaping market dynamics and offer new insights into the interplay between investor behavior and asset pricing.

## Similar Stocks

#### **Introduction**
This paper examines the concept of similarity investing, which measures the similarity between stocks based on characteristics such as size, book-to-market ratio, operating profitability, investment-to-assets, and price. The study investigates how the past returns of a stock's similar stocks predict its future performance, identifying a new return anomaly distinct from existing explanations like style investing or factor momentum.

---

#### **Methodology**
1. **Similarity Measure**:
   - Similarity between stocks is quantified using the Euclidean distance in a multi-dimensional space of standardized firm characteristics.
   - Characteristics include price, size, book-to-market, operating profitability, and investment-to-assets.

2. **Portfolio Construction**:
   - Stocks are sorted monthly into decile portfolios based on the past returns of their 50 most similar stocks (Residual Similarity Measure, RSIM).
   - A long-short strategy is constructed by taking long positions in portfolios with high similar-stock returns and short positions in portfolios with low similar-stock returns.

3. **Regression Analysis**:
   - Fama-MacBeth regressions are employed to account for firm-specific characteristics and control for other anomalies (e.g., momentum, reversal).

4. **Robustness Tests**:
   - Controlled for style investing, industry momentum, economic linkages, and factor momentum.
   - Used high-dimensional similarity measures involving 171 firm-level characteristics to extend analysis.

---

#### **Data**
- **Period**: 1963–2019.
- **Sources**:
  - Stock returns: CRSP.
  - Firm characteristics: Compustat.
  - Retail trading data: TAQ and ISSM for 1983–2000.
  - Institutional holdings: Thomson Reuters 13F data.

---

#### **Findings**
1. **Predictability of Similarity Returns**:
   - Stocks with high similar-stock returns outperform those with low similar-stock returns by **1.44% per month (CAPM alpha)** and **1.39% (Fama-French five-factor alpha)**.
   - The predictability is robust across multiple controls and alternative similarity measures.

2. **Mechanism**:
   - Evidence supports **continued overreaction** rather than underreaction as the primary driver.
   - Retail investor behavior, including attention spillover and categorical trading, plays a significant role.
   - Retail order imbalance increases for high similar-stock return portfolios, reflecting stronger demand from individual investors.

3. **High-Dimensional Characteristics**:
   - Extending the similarity measure to 171 characteristics strengthens the predictive power, increasing monthly return spreads by 32%.

4. **Role of Retail vs. Institutional Investors**:
   - The similarity effect is stronger among firms with low institutional ownership, suggesting retail investors are primary drivers.

5. **International Evidence**:
   - Results generalize across 38 international markets, with significant return spreads consistent across regions.

---

#### **Conclusion**
The paper establishes the similarity effect as a robust return anomaly driven by behavioral factors, particularly retail investor attention and demand. The findings contribute to asset pricing literature by highlighting a distinct mechanism of cross-sectional predictability that persists after accounting for known anomalies.

## Joint News, Attention Spillover, and Market Returns

#### **Introduction**
This study introduces a novel measure of joint news coverage—news articles that mention multiple firms—and examines its influence on market returns and investor behavior. The paper demonstrates how joint news coverage generates attention spillover across firms, resulting in market overvaluation and subsequent return reversals. The analysis is built on extensive datasets of over 2.6 million news articles and investor activity records.

---

#### **Methodology**
1. **Data**:
   - News Data: 2.6 million articles (1996–2014) from Thomson Reuters and S&P 500 index firms.
   - Investor Attention: Derived from SEC EDGAR filing downloads (5.97 million unique IPs).
   - Stock Data: CRSP and Compustat for financial variables.
   - Market Variables: Economic indicators (e.g., VIX, macro uncertainty indices) and market frictions (e.g., short interest ratios).

2. **News Measures**:
   - **Joint News**: Articles mentioning multiple firms; aggregated to a market-level indicator (JointNewsM).
   - **Self News**: Articles mentioning only one firm; less significant in marketwide effects.

3. **Attention Spillover Analysis**:
   - Abnormal Google search volume and EDGAR IP activities used to quantify attention shifts.
   - Eigenvector centrality measures firm importance in news coverage networks.

4. **Market Return Predictability**:
   - Regression models evaluate JointNewsM's power to predict future market returns.
   - Instrumental variable approach uses sensational non-financial news as an exogenous shock to validate causality.

---

#### **Findings**
1. **Market Predictability**:
   - JointNewsM strongly and negatively predicts one-month-ahead market returns.
   - Predictability persists for up to six months, indicating market overvaluation driven by attention spillovers.
   - In-sample \( R^2 \): 3.93%; Out-of-sample \( R^2 \): 6.52%.

2. **Investor Attention Spillovers**:
   - Joint news increases Google search activity and EDGAR filings for connected firms, more so than self news.
   - A one standard deviation increase in joint news leads to a 20.3% rise in new EDGAR downloads.

3. **Economic Gains**:
   - Predictive models using JointNewsM yield annualized certainty equivalent returns (CER) gains up to 9.31%.
   - Sharpe ratios of portfolios based on JointNewsM exceed those of buy-and-hold strategies.

4. **Behavioral vs. Rational Mechanisms**:
   - Stronger predictability during high uncertainty and market friction periods suggests behavioral (mispricing) over rational explanations (risk-sharing).

---

#### **Conclusion**
The paper establishes joint news coverage as a significant driver of market-wide attention spillovers, contributing to temporary overvaluation and subsequent reversals. These effects underscore the critical role of media networks in influencing investor behavior and market dynamics, providing robust tools for market prediction and investment strategies.



# Temp

## Identifying Risk Factor Regimes with Machine Learning: Implications for Tactical Asset Allocation

The paper titled "Identifying Risk Factor Regimes with Machine Learning: Implications for Tactical Asset Allocation" by Sheikh Sadik, dated January 2024, explores the use of machine learning (ML) to model and predict shifts in risk factor regimes and their potential impact on tactical asset allocation. Here's a summary of the key points and findings:

1. **Introduction and Motivation**: The paper starts by discussing the time-varying nature of asset price exposure to underlying risk factors, which can manifest as structural breaks or persistent shocks. Identifying shifts in these regimes can have significant implications for portfolio construction and asset allocation strategies.

2. **Traditional Regime Detection Methods**: The paper critiques traditional methods of regime detection, such as Hidden Markov Models, trend filtering, and rule-based approaches. It points out their limitations, including reliance on a subset of features and data-driven parametric frameworks that may not be realistic.

3. **Machine Learning Approach**: The author proposes a supervised ML approach to model risk factor regimes. ML is beneficial due to its ability to handle a large set of features and mitigate overfitting through hyperparameter tuning.

4. **Shapley Values for Interpretability**: To address the 'black box' nature of ML algorithms, the paper introduces 'Shapley Values' from cooperative game theory. This method provides an intuitive interpretation of the prediction contribution of each feature in the model.

5. **Methodology**: The paper focuses on modeling regimes for the Equity Factor, defined as a basket of seven global equity indices. The author tags historical periods into "Crash" and "Normal" regimes based on market volatility and drawdowns.

6. **Data Description**: The analysis relies on real-time variables from Bloomberg and DataStream, covering a wide range of market variables, surprise indices, and other economic and financial indicators.

7. **Feature Engineering**: The paper describes various feature engineering techniques applied to the initial set of variables, resulting in approximately 501 features after transformations and the creation of new features.

8. **Candidate Models and Estimation Methodology**: The author estimates several supervised classification models, including Logistic Regression, Support Vector Classifier, Extreme Gradient Boosting, Random Forest, and Neural Network. A probit model with principal components is used as a benchmark.

9. **Performance Evaluation**: The paper evaluates the models using various metrics such as ROC AUC, Average Precision Score, Brier Skill Score, Accuracy, F1 Score, and Matthews Correlation. The ensemble of all candidate models performs the best.

10. **Position Sizing Using Regime Probabilities**: The predicted probabilities from the ML models are used to adjust position sizes in a simple trading strategy on the equity factor, demonstrating the potential for improved risk-adjusted returns.

11. **Performance Benchmark Analysis**: The ML model's performance is compared to traditional benchmarks like trend following, VIX-based timing signals, volatility targeting, and Hidden Markov Models. The ML ensemble model outperforms these benchmarks.

12. **Applications in Portfolio Construction**: The paper illustrates how the predicted regime probabilities can be used in portfolio construction for tactical asset allocation, such as rotating between risk-on and risk-off assets and incorporating regimes in risk-based views.

13. **Interpreting the Predicted Regimes**: The paper discusses the use of Shapley Values to interpret the ML model predictions, providing insights into the contribution of each feature to the predicted probabilities.

In conclusion, the paper presents a comprehensive approach to using machine learning for tactical asset allocation by identifying and predicting risk factor regimes. It demonstrates the potential of ML models to improve portfolio construction and risk management through better understanding and utilization of market dynamics.



## Pairs Trading Using a Novel Graphical Matching Approach

The paper titled "Pairs Trading Using a Novel Graphical Matching Approach" by Khizar Qureshi and Tauhid Zaman introduces an innovative method for pairs trading, a popular investment strategy that capitalizes on the price movements of asset pairs driven by similar factors. The authors argue that traditional pairs trading, which often involves selecting highly cointegrated pairs, can inadvertently increase portfolio variance and reduce risk-adjusted returns due to the inclusion of multiple pairs sharing common assets.

To address this issue, the study proposes a new pair selection method that utilizes graphical matchings. The authors model all assets and their cointegration levels with a weighted graph, where edges represent pairs and weights indicate the extent of cointegration. The portfolio of pairs is a subgraph of this graph, and the strategy involves constructing a portfolio that is a maximum weighted matching of this graph. This ensures that pairs with strong cointegration are selected without sharing assets within any pair of pairs, leading to a lower variance in the matching-based portfolio compared to traditional approaches.

Theoretical analysis and empirical testing using data from the S&P 500 between 2017 and 2023 confirm the efficacy of the method. The matching-based strategy demonstrates a significant improvement in risk-adjusted performance, with a gross Sharpe ratio of 1.23, compared to a baseline value of 0.48 and market value of 0.59. Additionally, the approach shows reduced trading costs due to lower turnover and minimized single asset risk due to a more diversified asset base.

Key contributions of the paper include:
1. Identifying the impact of covariance/variance in pairs trading portfolios and proposing a graphical matching-based approach to select pairs.
2. Theoretical analysis providing formulas for analyzing the returns of different portfolio compositions.
3. Empirical testing that validates the theoretical findings and demonstrates the practical value of the proposed strategy.
4. Demonstrating the potential for reduced trading costs and lower single asset risk, contributing to a more diversified and less risky portfolio.

The authors conclude that their graph-theoretical approach to pairs trading could pave the way for numerous innovative modifications to the pairs trading methodology, offering a significant advancement over conventional strategies.



## A Modular Measure of Business Complexity

The paper titled "A Modular Measure of Business Complexity" by Darren Bernard, Elizabeth Blankespoor, Ties de Kok, and Sara Toynbee from the University of Washington and the University of Texas at Austin, respectively, addresses the challenge of measuring business complexity, which is an important but difficult-to-quantify aspect of business operations that can affect decision-making, valuation, and financial reporting.

The authors develop a novel, modular measure of business complexity using a large language model (LLM) fine-tuned on narrative disclosures and inline XBRL (eXtensible Business Reporting Language) tags. Their approach is guided by the definition of complexity as the processing resources required for a decision-maker to understand the economic substance of a business's transactions and financial position.

Key points from the paper include:

1. **Modular Measure Development**: The authors create a measure that reflects the intuition that information frictions from complexity depend on the user's familiarity and experience with a given transaction type. The measure is captured at the fact-level, allowing for complexity to vary across a firm's transactions.
2. **Use of LLM**: A large language model is trained on firms' financial reports to proxy for the knowledge and experience of an external user. The model predicts XBRL tags based on the surrounding narrative text, with the complexity measure being one minus the algorithm's confidence in its predictions.
3. **Validation and Correlation**: The measure is validated through several tests, showing positive correlations with existing measures of complexity, such as financial report length, Fog score, and the number of unique XBRL tags.
4. **Market and Regulatory Implications**: The paper finds that higher business complexity is associated with slower capital market price adjustments to financial reports and a higher likelihood of filing delays. It also shows that more complex transactions receive more regulatory scrutiny.
5. **Corporate Decision-Making**: The authors demonstrate that business complexity correlates with greater cash holdings, which may reflect precautionary motives due to increased uncertainty.
6. **Future Performance**: There is a negative relation between complexity and future performance, suggesting that complex contracts might reduce managers' ability to adapt to changing conditions or fully understand the implications of transactions for firm value.
7. **Methodological Contributions**: The paper contributes to the literature by introducing novel techniques using GPT algorithms for modeling complex narrative disclosure tasks in accounting and finance.
8. **Limitations and Opportunities**: The authors acknowledge limitations, such as potential measurement error from the mechanics of training the model and the difficulty of fully disentangling business complexity from reporting complexity. However, they also highlight opportunities for using the model in other areas of financial reports.

The paper concludes by reinforcing the role of complexity as a friction to decision-making and provides a richer and more flexible measure of complexity for future research. It also discusses the potential for the measure to help standard setters and regulators target efforts to reduce complexity for financial statement users.



## Moving Targets

The paper titled "Moving Targets" by Lauren Cohen from Harvard Business School and NBER, and Quoc Nguyen from DePaul University, explores how managers strategically shift performance targets in their communications with investors and markets. The study uses the complete history of earnings conference call transcripts by U.S. corporations from 2006 to 2020 and employs natural language processing techniques to analyze these calls.

Key findings and themes from the paper include:

1. **Strategic Target Shifting**: Managers are found to strategically shift targets to ensure they meet their own endogenously chosen hurdles. For example, if a company has seen consistent growth in same-store sales, they will emphasize this metric. However, if there is a quarter without growth, they will shift focus to another metric like cost savings or strategic R&D.
2. **Market Reaction**: When managers change the target, it predicts significant negative returns for the firm. In the quarter following a moved target, firms underperform by up to 99 basis points per month in value-weighted monthly abnormal return.
3. **Complexity and Persistence**: The effects are stronger with more complex targets, non-financial targets, and the most persistent targets. The paper suggests that investors may have an easier time digesting financial targets compared to non-financial targets.
4. **Real Activity Measures**: Moving targets predict future earnings, profitability, future news announcements, and the future value of those targets. These predictions appear to be largely unanticipated by the market.
5. **Robustness Checks**: The documented effects are not driven by firm size, time, industry, or firm events. The results suggest that the return patterns are not due to transaction costs or limits to arbitrage.
6. **Investor Inattention**: The paper suggests that investors may be differentially inattentive to non-financial targets compared to financial targets. This inattention could be a reason why the information about target changes is not immediately reflected in stock prices.
7. **Analyst Interaction**: When analysts prompt about dropped targets during conference calls, and CEOs are forced to address them, the moving target effect on returns is considerably reduced.
8. **Broader Implications**: The paper concludes that understanding the subtle ability to move targets and its implications can be critical for predicting future dynamics in financial markets. It suggests that simple insights from tracking performance targets can contain powerful information that is seemingly being ignored by the capital markets.

The paper contributes to the literature on stock price underreaction, investor inattention, textual analysis in finance and accounting, and the information content of firms' disclosure choices. It also provides a novel perspective on how firms can strategically use target setting and communication to influence investor perceptions and market outcomes.



The paper "Moving Targets" by Lauren Cohen and Quoc Nguyen employs natural language processing (NLP) techniques to analyze earnings conference call transcripts. Here's a detailed look at their methodology, particularly how they use a large language model (LLM) for their analysis:

1. **Data Collection**: The researchers obtained conference call transcripts from S&P Capital IQ and Refinitiv StreetEvents, which cover a wide range of global companies and provide verbatim representations of corporate events.

2. **NLP Library**: They utilized spaCy, an open-source library for NLP in Python. spaCy includes pre-trained pipelines that consist of multiple components trained on labeled data, such as a tagger, lemmatizer, parser, and entity recognizer.

3. **Identifying Targets**: The researchers identified targets in the transcripts using two main methods:
   - Named Entity Recognition (NER): They searched for named entities that are categorized as Products, Money, or Percent. For example, product names like "Mac" or "iPhone" were recorded as targets.
   - Part-of-Speech (POS) Tagging: For sentences containing Money or Percent entities, they used POS tagging to identify the related nouns and noun chunks. For instance, if a sentence mentioned "$1.67 billion" as a Money entity, the model would identify the subject related to this amount, such as "Net income," and record it as a target.

4. **Target Analysis**: The researchers analyzed the frequency and changes in the targets mentioned across different conference calls. They examined how often certain financial metrics or non-financial indicators like product sales were discussed and how these discussions evolved over time.

5. **Quantifying Target Movement**: They calculated a measure called "Moving Targets," which quantifies the degree to which firms change their focus from one reporting period to the next. This measure is based on the similarity between the targets discussed in consecutive conference calls.

6. **Statistical Analysis**: The researchers conducted calendar-time portfolio analysis and Fama-MacBeth cross-sectional regressions to examine the implications of target movement on future stock returns. They controlled for various factors known to influence stock returns, such as firm size, book-to-market ratio, past returns, and standardized unexpected earnings (SUE).

7. **Investor Attention and Analyst Interaction**: To explore the mechanism behind their findings, they looked at the complexity of target sets, the persistence of targets, and the distinction between financial and non-financial targets. They also examined how analyst interactions during conference calls, such as questions about dropped targets, might affect the market's reaction to target movement.

8. **Robustness Checks**: The researchers performed several robustness checks to ensure their findings were not driven by firm characteristics, industry effects, or other factors. They also considered the possibility of limits to arbitrage and transaction costs.

By using an LLM and NLP techniques, the researchers were able to systematically analyze a large corpus of unstructured data from earnings conference calls, providing new insights into how changes in the communication of performance targets can affect investor perceptions and market outcomes.



## Influence of Market States on Security Returns

The paper titled "Influence of Market States on Security Returns" by Warren Thomson from Griffith Business School, Griffith University, explores the impact of market conditions on future industry returns. The study investigates whether an industry's past relative performance in a similar market state can predict its future performance and suggests that market states can be utilized to develop profitable dynamic industry rotation strategies.

Key points from the paper include:

1. **Introduction**: The paper examines the theory that investors should consider market states when selecting industries for investment, using industry rotation strategies based on market states.

2. **Literature Review**: Previous research has shown that industry rotation can provide abnormal returns, and studies have explored the interaction between market states and industry performance.

3. **Data and Methodology**: The study uses monthly returns from the Center for Research into Security Prices (CRSP) and other sources, covering a period from January 1950 to December 2011. The author employs a non-parametric method to construct market states, using breakpoints of +20% or -20% market returns to form four distinct states.

4. **Portfolio Formation**: The study sorts industries into portfolios based on their past performance in the same market state, creating long-term winner (LW) and long-term loser (LL) portfolios for different formation periods.

5. **Results**: The results indicate that all formation periods provide significant, risk-adjusted, profitable returns. The study also finds that the strongest profitability is found in extreme market states.

6. **Risk Adjustment**: The paper uses the Fama-French three-factor model to adjust for risk, finding that the profitability of the strategies cannot be explained by these risk factors.

7. **State-Specific Analysis**: The study examines the performance of portfolios in different market states, finding significant profits in positive market states and supporting the theory that certain industries perform better at different stages of the market cycle.

8. **Conclusion**: The paper concludes that market states can predict future security returns and that an industry's performance in the past can predict its future performance in different market states. This has implications for asset selection, allocation, and pricing, and is particularly important for investors looking to understand the changing risk/return profiles of different industries.

The paper provides empirical evidence that supports the use of market states in investment strategies and contributes to the literature on asset allocation and industry performance.



## Breaking Bad Trends

The paper "Breaking Bad Trends" by Christian L. Goulding, Campbell R. Harvey, and Michele G. Mazzoleni, published in the Financial Analysts Journal, investigates the impact of trend breaks (turning points in asset price trajectories) on the performance of standard monthly trend-following strategies across various assets and asset classes. The authors find that there has been an increase in the frequency of trend breaks during the US economic expansion following the 2008 global financial crisis, which correlates with the lower performance of trend-following strategies in that period.

Key findings of the study include:

1. **Impact of Turning Points**: The paper establishes a negative relationship between the number of turning points an asset experiences and the risk-adjusted performance of its 12-month trend-following strategy. More turning points indicate more frequent shifts in trends, which can undermine the performance of trend-following strategies.

2. **Post-Financial Crisis Analysis**: The authors observe that the 11-year expansion period post-2008 global financial crisis (GFC) had an increased number of turning points compared to other years, leading to a decrease in sustained trend periods where trend-following is most effective.

3. **Dynamic Trend-Following Approach**: The paper introduces a dynamic trend-following approach that responds to asset turning points, which are classified into market corrections and rebounds. This approach blends slow and fast momentum strategies based on four-state cycle-conditional information to improve the performance of multi-asset trend strategies, especially after asset turning points.

4. **Practical Implications**: The findings suggest that the frequency of turning points and the dynamic response to them can be used to enhance the profitability of trend-following strategies. This is particularly relevant for investors who use technical analysis and trend-following as part of their investment approach.

5. **Data and Methodology**: The study uses monthly returns data from 43 futures markets across equity indices, bond markets, and commodities. The authors construct binary time-series momentum strategies and define market states based on the agreement or disagreement of slow (longer lookback horizon) and fast (shorter lookback horizon) momentum signals.

6. **Conclusion**: The authors conclude that the increased frequency of trend breaks post-GFC has contributed to the weaker performance of trend-following strategies. They demonstrate that a dynamic approach to trend-following, which adapts to market corrections and rebounds, can recover much of the loss experienced by static-window trend following.

The paper contributes to the literature on trend-following investing by highlighting the importance of adapting strategies to account for changes in market dynamics, particularly the frequency of trend breaks. It offers investors a method to potentially improve the performance of their trend-following strategies in the face of market volatility and turning points.



## Momentum Turning Points

The paper titled "Momentum Turning Points" from the Journal of Financial Economics (2023), authored by Christian L. Goulding, Campbell R. Harvey, and Michele G. Mazzoleni, explores the dynamics of time-series (TS) momentum strategies in the stock market. The authors use slow and fast TS momentum to identify and characterize different market cycles, including Bull, Correction, Bear, and Rebound phases. They develop a model to analyze the performance of these strategies under varying conditions of expected returns and noise levels in realized returns.

Key points from the paper include:

1. **Market Cycles Identification**: The authors distinguish four market cycles based on the agreement or disagreement between slow (12-month) and fast (1-month) momentum indicators. These cycles are:
   - **Bull**: Both slow and fast momentum indicate a positive trend (uptrend).
   - **Bear**: Both indicators suggest a negative trend (downtrend).
   - **Correction**: Slow momentum indicates a positive trend, while fast momentum indicates a negative trend, suggesting a potential turning point from uptrend to downtrend.
   - **Rebound**: Slow momentum indicates a negative trend, while fast momentum indicates a positive trend, signaling a potential turning point from downtrend to uptrend.

2. **Model Analysis**: The paper presents a model that estimates the mean persistence of U.S. stock market returns and the noise level in realized returns. The model suggests that high persistence and high noise are key characteristics of the market, making the combination of slow and fast momentum signals valuable for trend detection and identifying turning points.

3. **Performance of Momentum Strategies**: The authors find that intermediate-speed momentum portfolios, which blend slow and fast strategies, can translate predictive information in market cycles into positive unconditional alpha. They propose a novel decomposition of this alpha into market timing and volatility timing components.

4. **Macroeconomic and Business Cycle Linkages**: The paper documents that the identified market cycles have close connections to macroeconomic conditions and business cycles. For instance, Bear states, which predict negative expected returns, are more frequent early in recessions and coincide with negative macroeconomic news.

5. **Behavioral and Rational Foundations**: The authors discuss how behavioral models of slow information absorption might explain the prevalence of negative expected return states early in recessions and the transition to positive expected return states later in recessions.

6. **Dynamic Speed Selection**: The paper introduces a dynamic momentum strategy that adjusts its speed based on market cycles, aiming to maximize the Sharpe ratio. This strategy is shown to have out-of-sample performance that can efficiently track the best possible state-dependent performance.

7. **International Evidence**: The authors extend their analysis to international equity markets and find that intermediate-speed strategies generally have higher Sharpe ratios than the average of slow and fast strategies across all markets.

8. **Conclusion**: The paper concludes that intermediate-speed momentum strategies offer several advantages over slow and fast strategies in terms of risk-adjusted performance, tail behavior, and alpha generation. The findings are robust across different markets and suggest that dynamic adjustment of momentum speed based on market cycles can improve performance.

The paper contributes to the literature on momentum investing by providing a deeper understanding of how different momentum strategies perform under various market conditions and by highlighting the importance of market timing and volatility timing in momentum strategy performance.



## Factor Timing

The paper titled "Factor Timing" by Valentin Haddad, Serhiy Kozak, and Shrihari Santosh from the NBER Working Paper Series (Number 26708) explores the concept of optimal factor timing in portfolio management and its implications for the stochastic discount factor (SDF). Here's a summary of the key points:

1. **Optimal Factor Timing Portfolio**: The authors propose that the optimal factor timing portfolio is equivalent to the SDF, which is significant for investors looking to maximize returns.

2. **Predictability of Market-Neutral Equity Factors**: The paper finds that market-neutral equity factors are strongly predictable, and exploiting this predictability can significantly improve portfolio performance compared to static factor investing.

3. **Stochastic Discount Factor (SDF)**: The authors develop a method to characterize the SDF empirically, focusing on the predictability of the largest principal components of factors. They find that the variance of the SDF is larger and more variable over time than estimates that ignore predictability.

4. **Economic Implications**: The results challenge existing theories aiming to match the cross-section of stock returns and suggest that the SDF's properties are more volatile and exhibit different cyclical behavior than previously thought.

5. **Factor Investing and Market Timing**: The paper discusses how factor investing strategies can be enhanced by factor timing, which involves adjusting portfolio weights based on the predictability of factor returns.

6. **Data and Methodology**: The authors use fifty standard stock "anomaly" portfolios and impose restrictions on the dynamics of expected returns to construct robust forecasts of factor returns.

7. **Principal Components Analysis (PCA)**: The paper employs PCA to reduce the dimensionality of the factor space and focuses on the first five principal components, which explain a significant portion of the variation in realized returns.

8. **Predictability of Anomaly Portfolios**: The authors find that the largest principal components of anomaly returns are predictable, with the first and fourth PCs showing the strongest predictability.

9. **Investment Benefits**: The paper demonstrates that factor timing strategies can provide substantial investment gains, with a pure factor timing portfolio achieving a high Sharpe ratio.

10. **SDF Variance and Heteroskedasticity**: The benefits from factor timing are found to be strongly time-varying, leading to more heteroskedasticity in the SDF.

11. **Macroeconomic Variables**: The fluctuations in the SDF variance are related to different macroeconomic variables and occur mostly at shorter business-cycle frequencies.

12. **Challenges for Theories**: The paper suggests that current theories may not fully capture the dynamic properties of the cross-section of returns, as the estimated SDF is more volatile and heteroskedastic than what these theories predict.

The paper concludes that factor timing is valuable and has important implications for the understanding of risk premia and the construction of economic models. The findings emphasize the importance of considering time-varying risk premia in asset pricing and portfolio management.

## Estimating General Equilibrium Spillovers of Large-Scale Shocks

The paper titled "Estimating General Equilibrium Spillovers of Large-Scale Shocks" by Kilian Huber, published in The Review of Financial Studies in 2023, discusses the impact of large-scale economic shocks and how they ripple through the economy, affecting various firms and households both directly and indirectly. The author outlines a methodology for researchers to estimate these spillover effects using quasi-experimental or experimental variations and highlights potential biases that can skew these estimates.

**Key Points of the Paper:**

1. **Definition and Importance of Spillovers:**
   - Spillovers refer to the indirect effects that large-scale shocks have on entities not directly impacted by the shock. These can occur through various channels such as financial markets, input-output networks, or regional economies.
   - Understanding spillovers is crucial for formulating economic policies and for constructing accurate macroeconomic models.

2. **Methodology for Estimating Spillovers:**
   - The paper suggests using regression frameworks that incorporate 'leave-out means,' which are the average treatment statuses of other firms or households in a group (like a region or sector) excluding the entity in question.
   - This method allows for the direct comparison of different types of spillovers and provides a standard error for statistical inference.

3. **Challenges in Estimation:**
   - **Mechanical Bias:** The paper identifies and discusses two main sources of mechanical bias in spillover estimates. The first is the presence of multiple spillover types, which can lead to incorrect conclusions if not all types are accounted for in the analysis. The second is the mismeasurement of treatment status due to nonlinear effects or measurement error, which can artificially inflate or deflate spillover estimates.
   - **Practical Solutions:** The author offers guidance on how to detect and correct for these biases. Solutions include testing for heterogeneous effects based on economic theory, using flexible functional forms to capture nonlinearities, and employing instrumental variables to ensure the exogeneity of treatment effects.

4. **Application to Real-World Data:**
   - Huber applies the discussed methods to study the spillover effects of a credit shock caused by Commerzbank during the 2008 financial crisis. The analysis shows that regional spillovers can be significant and that neglecting to account for multiple types of spillovers can lead to incorrect interpretations of the shock's impact.

5. **Policy Implications:**
   - Accurate spillover estimates are essential for policymakers to understand the broader economic impact of their decisions and to calculate multiplier effects accurately.
   - The paper demonstrates how direct and spillover effects can be used to estimate the impact of policy interventions, such as public credit programs, on employment and regional economies.

6. **Conclusion:**
   - The paper concludes that while direct estimation of spillovers is a powerful tool for understanding the general equilibrium effects of large-scale shocks, researchers must be vigilant about potential biases and employ rigorous methods to ensure the accuracy of their estimates.

The paper is a significant contribution to the fields of finance and macroeconomics, providing both theoretical insights and practical guidance for empirical research on the propagation of economic shocks through complex economic systems.



# Temp2

## Ambiguity about volatility and investor behavior

The paper titled "Ambiguity about volatility and investor behavior" from the Journal of Financial Economics (2022) explores the relationship between ambiguity regarding market volatility and individual investor behavior. Here's a summary of the key points:

1. **Study Focus**: The research centers on how variations in aggregate ambiguity about volatility, as measured by the V-VSTOXX index, influence individual investor trading activities.

2. **Data and Methodology**: The authors utilize trading records from over 10,000 individual investors from a large German online brokerage firm between March 2010 and December 2015. They examine the impact of ambiguity on two dimensions of investor activity: logins and trades.

3. **Key Findings**:
   - **Increased Ambiguity and Investor Activity**: The study finds that an increase in ambiguity is associated with heightened investor activity, both in terms of logging into trading platforms and executing trades.
   - **Risk-Taking Behavior**: During periods of high ambiguity, investors tend to reduce their risk exposure by trading out of risky securities, and this behavior is not temporary, persisting over subsequent days.
   - **Ambiguity-Averse Investors**: Investors identified as ambiguity averse through an Ellsberg urn experiment are found to be more sensitive to ambiguity shocks, leading them to decrease their exposure to riskier assets more significantly than average investors.

4. **Theoretical Implications**: The findings support the notion that ambiguity, distinct from risk, plays a crucial role in investor decision-making. The paper also provides evidence that the effect of investor sentiment is more pronounced during periods of high ambiguity, aligning with Hirshleifer's hypothesis.

5. **Robustness Checks**: The results are robust to the inclusion of various control variables and alternative measures of ambiguity, such as economic policy uncertainty and market-based measures like the omega measure.

6. **Conclusion**: The paper concludes that ambiguity about volatility is an important factor that influences individual investor behavior, leading to changes in trading activity and risk-taking strategies.

This study contributes to the literature by providing empirical evidence on how ambiguity, as opposed to just risk, affects the trading decisions of individual investors, highlighting the need for a nuanced understanding of investor behavior under conditions of uncertainty.



## Investor Behavior at the 52 Week High

This finance paper titled "Investor Behavior at the 52 Week High" by Joshua Della Vedova, Andrew Grant, and P. Joakim Westerholm, explores how individual investors influence the 52-week high (52WH) effect in stock prices. The 52WH is the highest price a stock has reached in the past year, and it's a significant reference point for investors. The study uses detailed trading data from the NASDAQ Helsinki exchange to analyze the behavior of individual and institutional investors.

Key Findings:

1. **Increased Volume and Returns at 52WH**: The study finds that as stocks approach their 52WH, there is a significant increase in trading volume and a tendency for stocks to continue performing well after reaching this price point, a phenomenon referred to as the 52WH effect.

2. **Individual Investor Behavior**: Individual investors tend to sell more as the stock price nears the 52WH, particularly using limit orders. This behavior suggests anchoring, where investors use the 52WH as a reference point to make decisions.

3. **Institutional Investor Benefit**: The selling by individual investors at the 52WH benefits institutional investors who act as counterparties, often buying at these prices and benefiting from the subsequent price increase.

4. **Anchoring and Disposition Effects**: The study suggests that individual investors are more likely to sell stocks near the 52WH due to the disposition effect (a tendency to sell assets that have increased in value) and anchoring bias (relying too heavily on the 52WH as a reference point).

5. **Impact of Market Uncertainty**: During periods of market uncertainty, individual investors are more likely to sell stocks at the 52WH, potentially exacerbating the 52WH effect.

6. **Post-52WH Returns**: The paper finds that stocks that experience high levels of limit order selling by individual investors at and around the 52WH tend to have abnormally high returns in the period following the 52WH.

7. **Data and Methodology**: The study uses a unique dataset that allows for the classification of trades by investor type (individual or institutional) and order type (limit or market), providing a granular view of trading behavior.

8. **Implications for Investor Performance**: The findings suggest that individual investors' tendency to anchor to the 52WH and use limit orders may contribute to their overall underperformance relative to institutional investors.

The paper contributes to the literature on behavioral finance by providing evidence that individual investors' trading behavior around the 52WH has significant implications for stock price dynamics and their own investment performance. It also highlights the role of institutional investors in exploiting the opportunities created by individual investors' behavior.



## When Smart Beta Meets Machine Learning and Portfolio Optimization

The finance paper titled "When Smart Beta Meets Machine Learning and Portfolio Optimization" by Jason Hsu, Xiaoyang Liu, Vivek Viswanathan, and Yingfan Xia explores the integration of smart beta strategies with machine learning techniques and portfolio optimization. Here's a summary of the key findings and discussions in the paper:

1. **Diversification in Factor Investing**: The authors argue that diversifying into a wide range of factors, rather than focusing on a few popular ones, leads to more consistent outperformance. They use data from 38 developed and emerging market countries to support their claim.

2. **Machine Learning Models**: The paper suggests that machine learning models such as linear ridge and gradient boosting are more effective in predicting a stock's future returns based on its factor exposures compared to traditional methods. This effectiveness is observed to be robust over time and across different countries.

3. **Portfolio Optimization**: The authors propose that a portfolio optimizer focused on tracking error can significantly improve the portfolio's information ratio compared to simple tilting heuristics. This approach is more aligned with the modern portfolio theory that advocates for estimating expected returns and covariances.

4. **Smart Beta Performance**: The paper discusses the underwhelming performance of smart beta products from 2005 to 2022, particularly those focused on common factors like value, low volatility, quality, and small cap. It challenges the notion that most factors are data-mined and without investment merit.

5. **Factor Zoo**: The authors refer to the comprehensive set of factors identified in the academic literature as the "factor zoo" and suggest that diversifying across these factors is prudent.

6. **Data and Methodology**: The paper uses a dataset covering market and financial data for 48 countries from June 1986 to May 2022. It employs various machine learning techniques and optimization methods to analyze the performance of different investment strategies.

7. **Conclusion**: The paper concludes that machine learning models and portfolio optimization techniques can enhance the performance of smart beta strategies, providing evidence against the claim that most documented factors lack investment merit.

The paper provides a comprehensive analysis of how advanced techniques can be applied to traditional investment strategies to improve their effectiveness and performance. It also emphasizes the importance of considering a broad range of factors and using sophisticated methods for portfolio construction.



## Selling Fast and Buying Slow: Heuristics and Trading Performance of Institutional Investors

The finance paper titled "Selling Fast and Buying Slow: Heuristics and Trading Performance of Institutional Investors" by Klakow Akepanidtaworn, Rick Di Mascio, Alex Imas, and Lawrence Schmidt investigates the trading behaviors and performance of institutional investors. Here's a summary of the key points:

1. **Investigative Focus**: The paper focuses on whether market experts, specifically institutional investors, are prone to heuristics in their trading decisions and if such biases transfer between buying and selling activities.

2. **Data and Sample**: The study uses a unique dataset of institutional investors managing portfolios averaging $573 million. The data includes detailed daily holdings and trades from 783 portfolios over the period from 2000 to 2016.

3. **Findings**:
   - **Skill in Buying**: The investors demonstrated clear skill in buying decisions, with purchased assets outperforming both benchmarks and random buying strategies.
   - **Underperformance in Selling**: In contrast, selling decisions significantly underperformed, even when compared to random selling strategies. This underperformance was substantial and consistent across various specifications and robustness checks.

4. **Cognitive Resource Allocation**: The paper suggests that an asymmetric allocation of cognitive resources, such as attention, might explain the discrepancy between buying and selling performance. Investors seem to allocate more attention to buying decisions, which are forward-looking and belief-driven, while selling decisions appear to be more heuristic and driven by limited attention.

5. **Heuristic Process**: The authors propose a two-stage process for selling decisions that involves heuristic thinking. First, limited attention leads to a focus on assets with extreme prior returns. Second, from this narrowed set, investors sell positions where they have the least conviction, which can lead to the sale of potentially viable investment ideas.

6. **Performance on Earnings Announcement Days**: The study finds that selling decisions made on earnings announcement days, which naturally draw investor attention, outperform those made on non-announcement days. This suggests that attention can improve selling performance.

7. **Heterogeneity in Performance**: The underperformance in selling is more pronounced among managers with a fundamental orientation who manage more active and concentrated portfolios.

8. **Implications**: The findings challenge the assumption of unbiased institutional investors and highlight the importance of attention and cognitive resource allocation in investment decision-making. The paper suggests that better reporting standards and decision aids could improve the selling performance of institutional investors.

9. **Conclusion**: The paper concludes that institutional investors display systematic heuristics in their selling decisions, which can be costly, and that these heuristics are linked to the asymmetric allocation of cognitive resources towards buying at the expense of selling.

The paper provides valuable insights into the behavioral biases of expert investors and contributes to the literature on heuristics and biases in financial decision-making.

