## The Virtue of Complexity in Return Prediction

### **1. Introduction and Motivation**

- **Context and Problem:**

  Traditional return‐prediction models in finance typically use only a handful of predictors and parameters. While these “simple” models are easier to estimate and interpret, they tend to understate the true predictability of asset returns. In contrast, real-world data–generating processes (DGPs) are often very complex and may require models with many parameters to capture nonlinear relationships and interactions.

- **Central Claim:**

  The paper challenges conventional wisdom by theoretically proving and empirically demonstrating that when one properly applies shrinkage techniques (i.e., regularization), models of return prediction with high complexity (where the number of parameters exceeds the number of observations) can actually yield better out-of-sample forecast accuracy and superior portfolio performance. In effect, more complex models can more accurately approximate the unknown predictive function, even if conventional measures like predictive R² appear negative.

### **2. Theoretical Framework and Main Contributions**

- **Universal Approximation and High-Dimensionality:**

  The authors start with the idea that the true relationship between predictors (denoted G_t) and future returns can be modeled as a smooth function f(G_t). Leveraging the universal approximation theorem, they argue that one can approximate this unknown function with a sufficiently wide neural network. This approximator takes the form:

  f(G_t) \approx \sum_{i=1}^{P} S_{i,t}\beta_i,

  where S_{i,t} are nonlinear activations of the predictors and P is very large relative to the number of observations T.

- **Ridge Regression and Shrinkage:**

  As model complexity increases (i.e., as P grows relative to T), ordinary least squares estimation suffers from unstable coefficients (overfitting) if no regularization is applied. The authors show that applying appropriate shrinkage (regularization) not only curbs variance but in fact improves the out-of-sample performance of the model. They derive an optimal shrinkage parameter, demonstrating that the expected out-of-sample forecasting accuracy—and, crucially, the economic performance of a market timing strategy—is strictly increasing in model complexity when shrinkage is optimally applied.

- **Random Matrix Theory:**

  A central technical contribution is the use of random matrix theory to analyze the behavior of high-dimensional ridge regression (and its “ridgeless” limit). Even though the training error is zero in the overparameterized regime, the “benign overfitting” phenomenon ensures that the timing strategy based on these complex models produces positive expected returns and favorable Sharpe ratios out-of-sample.

- **Key Theoretical Result:**

  The paper proves that when the true data-generating process is highly complex, the gains from better approximating the nonlinear function f(G_t) outweigh the statistical “costs” (such as increased variance) as long as proper regularization is applied. In short, an analyst should use as many predictors as computationally feasible to capture return predictability.

### **3. Empirical Evidence and Applications**

- **Market Timing Strategy Performance:**

  Using historical U.S. equity market data (spanning from 1926 to 2020) and a set of 15 standard predictor variables from the literature (e.g., Goyal and Welch predictors), the paper implements high-dimensional models via the random Fourier feature (RFF) method. This approach creates an expanding neural network architecture that approximates the unknown f(G_t) while maintaining a ridge regression structure.

- **Economic Metrics over Traditional R²:**

  Although the traditional out-of-sample predictive R² of these models is often negative (reflecting high forecast variance), the authors show that the economic value—as measured by the Sharpe ratio of a market timing strategy—is substantially improved. For example, the out-of-sample market timing Sharpe ratio improvement relative to a buy-and-hold strategy is about 0.47 per annum with statistically significant performance improvements.

- **Robust Timing Behavior:**

  The empirical findings also indicate that timing positions derived from high-complexity models tend to behave like long-only strategies and can effectively reduce exposure ahead of market downturns (e.g., divesting before recessions). This supports the practical relevance of using complex machine learning models for return prediction in asset pricing.

### **4. Implications and Conclusions**

- **Implications for Machine Learning in Finance:**

  The study provides a strong theoretical and empirical rationale for employing complex, high-dimensional models in return prediction rather than relying on oversimplified models. It argues that more complex models, when regularized correctly, can extract a greater amount of predictive information—even if standard statistical metrics like R² appear discouraging.

- **Practical Applications:**

  The results encourage practitioners to adopt machine learning techniques that use large numbers of predictors. The enhanced predictive power translates into better timing strategies and improved portfolio performance, suggesting a paradigm shift in how asset returns should be modeled.

- **Broader Contribution:**

  Beyond return prediction, the paper bridges techniques from machine learning, random matrix theory, and empirical finance. It emphasizes that economic performance (e.g., Sharpe ratios and timing returns) can be a more meaningful measure of model success than traditional statistical accuracy metrics in the context of high-dimensional data.

### **1. The Prediction Framework and High-Dimensional Approximation**

- **Nonlinear Function Approximation:**

  The authors begin with the model
  $$
  R_{t+1} = f(G_t) + \varepsilon_{t+1},
  $$
  where $$R_{t+1}$$ is the asset return, G_t is a vector of predictive signals, and f is an unknown smooth function. Using the universal approximation theorem, they approximate f with a wide neural network:

  $$f(G_t) \approx \sum_{i=1}^{P} S_{i,t}\beta_i$$, where $$S_{i,t} = \tilde{f}(w{\prime}_i G_t)$$ are nonlinear activations with fixed (or randomly generated) weights w_i. The key is that the approximation improves as P (the number of features) increases, even if P becomes larger than the number of observations T.

- **High-Complexity Regime (P > T):**

  In this regime, standard OLS estimation fails because the covariance matrix of predictors becomes singular or nearly singular. However, the paper considers the “ridgeless” limit of ridge regression. The ridge estimator with shrinkage parameter z is given by:
  $$
  \hat{\beta}(z) = \left(z I + \frac{1}{T}\sum_{t=1}^T S_t S{\prime}t\right)^{-1} \frac{1}{T}\sum{t=1}^T S_t R_{t+1}
  $$
  When $$z \to 0^+$$, the estimator converges to the Moore-Penrose pseudoinverse solution. Despite zero training error, this solution can perform well out‐of‐sample—a core aspect of the double descent phenomenon.

### **2. The Double Descent and the Role of Shrinkage**

- **Double Descent Phenomenon:**

  Traditionally, as the model complexity (number of predictors P) increases, the standard prediction error (typically measured by out-of-sample R^2 or mean squared error, MSE) worsens due to overfitting when P approaches T. However, beyond the interpolation threshold (P > T), the prediction error starts decreasing again. This “double descent” curve is rigorously examined in the paper by analyzing the asymptotic properties of the ridge regression estimator in the high-dimensional limit.

- **Optimal Shrinkage:**

  The authors derive that the optimal amount of shrinkage to counteract the variance inflation in the high-complexity regime is
  $$
  z^* = \frac{c}{b}
  $$
  *where* $$c = \lim_{T \to \infty} P/T$$ *denotes model complexity, and* b is a constant representing the average signal strength (or true risk premium across predictors). This optimal shrinkage minimizes the bias-variance trade-off and maximizes the economic performance—measured by the Sharpe ratio of the timing strategy based on the predictions.

- **Economic vs. Statistical Performance:**

  A key technical insight is that even if the traditional out-of-sample R^2 (which is strongly influenced by the variance of the predictions) is negative, the economic return of a market timing strategy built on these predictions can be positive. The paper decomposes the mean squared error (MSE) of the estimator into parts related to forecast bias and “leverage” (variance of the timing signal). Formally, they express:
  $$
  \text{MSE}(\hat{\beta}) = E\left[(R_{t+1} - S{\prime}t\hat{\beta})^2 \right] = E[R^2{t+1}] - 2E[S{\prime}t\hat{\beta} R{t+1}] + E\left[(S{\prime}_t\hat{\beta})^2\right].
  $$
  The optimal model maximizes the trade-off such that the expected excess return (numerator) over a certain level of leverage (denominator) yields a positive Sharpe ratio.

### **3. Random Matrix Theory (RMT) Foundations**

- **Eigenvalue Distribution and Stieltjes Transform:**

  In the high-dimensional limit where T, P \to \infty and P/T \to c > 0, classical asymptotics no longer apply; instead, one must study the spectral properties of the sample covariance matrix
  $$
  \hat{\Sigma} = \frac{1}{T}\sum_{t=1}^T S_t S{\prime}_t.
  $$
  The authors invoke the Stieltjes transform $$m(z; c)$$ of the eigenvalue distribution of $$\hat{\Sigma}$$. Under the assumptions made (including a mild structure on the predictor distribution via a population covariance matrix $$\Sigma$$ with eigenvalue distribution converging to a nonrandom limit H), the limiting behavior of $$m(z; c)$$ is used to derive the properties of ridge regression in the high-complexity regime.

- **Key Proposition and Lemma:**

  They prove that many out-of-sample performance metrics (expected return, variance, and hence the Sharpe ratio) depend solely on the empirical eigenvalue distribution of $$\hat{\Sigma}$$ rather than the true covariance $$\Sigma$$. For instance, Lemma 1 shows that for a bounded sequence of matrices A_P,
  $$
  \hat{\beta}{\prime} A_P \hat{\beta} - \frac{b^*}{P} \text{tr}(A_P) \to 0,
  $$
  indicating that the aggregate predictive performance converges as the model dimension grows.

- **Implication for Complexity:**

  The use of RMT reveals that even as the number of predictors explodes (with c > 1), the benign overfitting phenomenon allows the ridgeless estimator (or ridge estimator with optimal shrinkage) to control variance effectively. Essentially, as P increases, the many solutions available in the overparameterized system include one with a minimal norm—providing an implicit regularization effect that enhances out-of-sample performance.

### **4. Portfolio Performance and Practical Implications**

- **Market Timing Strategy:**

  The paper defines a timing strategy where the position is given by
  $$
  \hat{\pi}_t(z) = \hat{\beta}(z){\prime} S_t.
  $$
  The theoretical analysis shows that, under the optimal shrinkage $$z^*$$, the unconditional expected return and variance of this timing strategy can be characterized precisely. Even in scenarios where the fitted model has zero training error (perfect interpolation), the out-of-sample performance, measured via expected returns and the Sharpe ratio, improves with complexity—validating the “virtue of complexity.”

- **Economic Value vs. Predictive** $$R^2$$**:**

  A surprising insight is that a model may exhibit a highly negative predictive $$R^2$$ due to high variance but still deliver a substantial Sharpe ratio when used for market timing. This divergence arises because the predictive $$R^2$$ conflates a model’s leverage (scale of predictions) with its correlation with the true conditional expectation. In practical terms, investors should evaluate models based on their economic performance (e.g., timing returns and Sharpe ratios) rather than solely on conventional statistical metrics.

### **5. Concluding Technical Insights**

The paper provides a rigorous treatment by showing:

- Increasing model complexity, when coupled with optimal shrinkage, does not harm and can actually enhance out-of-sample return prediction and portfolio performance.
- The phenomenon of double descent is not merely a statistical curiosity; it has profound economic implications in asset pricing, as it explains why very high-dimensional, heavily parameterized models can outperform simpler models.
- The analytic results are grounded in advanced random matrix theory, enabling a precise characterization of how the sample covariance matrix’s eigenvalue distribution affects the ridge regression estimator in high dimensions.
- As a practical recommendation, the authors conclude that analysts should use the most complex model computationally feasible—subject to appropriate regularization—because the approximation gains from higher-dimensional predictors more than compensate for the statistical costs when the model is properly tuned.

These technical details underscore the major contribution of the paper: offering a theoretical and empirical justification for adopting complex machine learning models in return prediction, with significant implications for both academic research and practical portfolio management.



## Shall We Talk? The Role of Interactive Investor Platforms in Corporate Communication

This paper examines a novel form of corporate communication—investor interactive platforms (IIPs)—that emerged in China between 2010 and 2017. Using a comprehensive dataset of approximately 2.5 million investor questions and corresponding management responses, the authors (Charles M. C. Lee and Qinlin Zhong) investigate both what investors ask about and how these dialogues relate to market outcomes. Below is a detailed summary of the paper’s main findings and contributions:

### **1. Research Motivation and Context**

- **Demand‐Side of Corporate Communication:**

  Unlike traditional studies that focus on how managers disclose information, this paper shifts the focus to the “demand‐side” by investigating what ordinary investors need to know on a day-to-day basis and the challenges they face when processing publicly available information. The authors note that retail investors often incur significant integration costs when trying to understand complex financial disclosures.

- **Institutional Setting in China:**

  The study centers on IIPs—officially sanctioned online platforms established by the Shenzhen and Shanghai stock exchanges. These platforms mandate that almost every listed company engage in direct dialogue with investors by providing timely, publicly logged responses to investor inquiries. Importantly, the content shared on these platforms is limited to information already in the public domain, which makes them an excellent setting to study investors’ processing challenges.

### **2. Methodology and Data Analysis**

- **Data Collection:**

  The researchers collected complete dialogue histories from firm-specific community pages covering a period from January 2010 to December 2017. This massive dataset allowed them to capture investor questions and management responses across nearly all listed firms in China.

- **Content Classification Using NLP:**

  To parse the large volume of text, the authors manually classified a random sample of around 50,000 questions and then employed a state-of-the-art BERT-based algorithm to classify the remaining 2.45 million postings.

  - **Findings:** About 80% of questions seek clarification or explanation about specific items in financial reports or company operations, 16.6% are comments or suggestions to management, and the remaining questions pertain to verifying rumors or addressing misunderstandings.

- **Case Studies:**

  The paper includes illustrative examples that span several categories—clarifications on business transactions, confusion regarding accounting treatment, and even investor suggestions—demonstrating the range of investor concerns.

### **3. Link Between IIP Activity and Market Behavior**

- **Impact on Trading Activity:**

  Analyzing daily data, the study shows that higher levels of IIP activity are statistically associated with increases in abnormal trading volume and return volatility. This suggests that the interactive nature of the platforms draws investor attention and may stimulate trading.

- **Market Liquidity Improvements:**

  The research finds that on days with increased IIP activity, key liquidity measures—such as bid-ask spreads and the Amihud illiquidity ratio—improve. Lower bid-ask spreads indicate reduced information asymmetry, while a lower Amihud ratio suggests that price impact diminishes when investor engagement is high.

- **Effect on Price Informativeness:**

  Using longer-window (quarterly) tests, the study demonstrates that when IIP activity is more vigorous, stock prices better incorporate information about future earnings. Specifically, the pre-earnings announcement returns are more predictive of forthcoming unexpected earnings (a measure known as the future earnings response coefficient), indicating a more efficient price discovery process.

### **4. The Role of Regulatory and Institutional Changes**

- **Adoption of New Accounting Standards:**

  A key part of the analysis shows that when new accounting standards were mandated (in July 2014), there was a notable uptick in financial statement–related questions and responses on the IIPs. This supports the idea that increased reporting complexity raises investor processing costs, which in turn can be mitigated by interactive communication.

- **Quasi-Mandatory Participation:**

  Firms’ near-universal participation in IIPs (with adoption rates reaching 99% over time) and the public monitoring of engagement levels suggest that these platforms are not merely optional communication channels but have become integral to the corporate disclosure process in China.

### **5. Contributions and Implications**

- **Reducing Integration Costs:**

  The study provides empirical evidence that interactive dialogue helps lower investors’ information processing (or integration) costs. By addressing uncertainties and clarifications in near-real time, these platforms facilitate more informed investor decisions.

- **Enhancing Market Efficiency:**

  The reduction in information asymmetry as a result of IIP activities is linked not only to increased liquidity but also to more informative stock prices, which ultimately benefits both investors and the broader market.

- **Policy and Regulatory Insights:**

  The findings have implications for regulators focused on transparency and investor protection. Enhancing dialogue between firms and investors—thereby reducing integration costs—could improve the overall quality of market information and ensure a more level playing field for retail investors.

### 6. **In Conclusion**

The paper demonstrates that investor interactive platforms are more than a communication novelty; they fundamentally alter the dynamics of investor information processing and market price formation. Through systematic analysis and robust empirical testing, the authors show that these platforms alleviate common investor challenges, stimulate trading, improve market liquidity, and enhance the informativeness of stock prices. This research contributes to a growing literature on corporate communication and investor relations, suggesting that integrating interactive elements into disclosure practices can yield tangible benefits for financial markets.



## Price Discovery and Trading After Hours

This paper investigates how trading outside of regular hours influences the process of price discovery—that is, how new information becomes incorporated into stock prices over a 24‐hour period. The authors—Michael J. Barclay and Terrence Hendershott—analyze detailed trade and quote data for Nasdaq stocks (from March through December 2000) to compare different trading sessions and their effectiveness in reflecting new information into prices.

Below is a comprehensive summary of the study’s major themes, methodology, findings, and implications:

### **1. Research Motivation and Objectives**

**Motivation:**

Traditional trading predominantly occurs during regular market hours (9:30 A.M. to 4:00 P.M. Eastern Time), where large volumes of trade support efficient price formation. However, advances in trading technology (especially electronic communications networks or ECNs) have enabled trading in after-hours periods despite generally lower volumes. The paper explores whether these lower volumes still contribute meaningfully to price discovery and how the nature of trades in these off-hours periods differs from those during the trading day.

**Primary Research Questions:**

- **How is the timing and magnitude of price discovery distributed over the 24-hour cycle?**
- **Where do informed traders prefer to operate (before the open vs. after the close), and how does this influence the incorporation of private information into prices?**
- **How do the characteristics of after-hours trading—such as lower volume, larger trade sizes, and different liquidity profiles—affect price efficiency and volatility?**

### **2. Data and Methodological Framework**

**Data:**

- The authors use comprehensive datasets comprising all after-hours trades and quote changes for Nasdaq-listed stocks over a specified period (March–December 2000).
- They segment the 24-hour trading cycle into several key periods: the **preopen** (approximately 8:00–9:30 A.M.), the **postclose** (approximately 4:00–6:30 P.M.), and also consider the regular trading session and an overnight period.

**Methodology:**

- **Descriptive Analysis:**

  The study first examines patterns in trading volume, volatility, and trade sizes across these time intervals. For instance, while overall volume is much higher during the trading day, individual trades after hours are substantially larger and often occur at times with elevated volatility.

- **Microstructure Modeling:**

  The authors employ the Easley, Kiefer, and O’Hara (EKO) model to estimate the probability of informed trading (often denoted as PIN). This model distinguishes between liquidity (uninformed) trading and trading driven by private (informed) information.

- **Price Discovery Metrics:**

  Two key measures are used:

  - **Weighted Price Contribution (WPC):** This metric quantifies the fraction of the total price change (e.g., from the previous close to the next open) that occurs during each defined period.
  - **Weighted Price Contribution per Trade (WPCT):** By normalizing the WPC by the fraction of trades occurring in a period, this measure assesses how much information is revealed on average by each trade.

### **3. Main Findings**

**A. Trading Activity and its Distribution:**

- **Regular Trading vs. After-Hours:**

  The bulk of liquidity and efficient price discovery happens during the regular trading day due to high volumes. However, despite its low volume, after-hours trading still generates significant price discovery.

- **Preopen vs. Postclose:**

  - **Preopen Period:**
    - Exhibits a higher probability of informed trading compared to other periods.
    - Although trading volumes are low, individual trades are much more informative on a per-trade basis.
    - A large share of the overall price change (from the previous close to the next open) is determined before the market officially opens.
  - **Postclose Period:**
    - Characterized by a larger proportion of liquidity or inventory-driven trades rather than trades based on private information.
    - Despite some price discovery occurring, the contribution per trade tends to be lower and prices are noisier—reflected in wider bid–ask spreads and higher volatility relative to trade volume.

**B. Informed Trading Dynamics:**

- Using the EKO model, the paper finds that the estimated probability of an informed trade (PIN) is significantly higher in the preopen than in the postclose. Moreover, during the regular trading day, the probability of informed trading is about half of that during the preopen. This indicates a concentration of informed trading in the early after-hours session when private information has a stronger effect on prices.

**C. Price Efficiency and Volatility:**

- **Efficiency:**
  - Prices are generally more efficient (with lower noise and tighter spreads) during the day due to the high volume of liquidity trading.
  - After hours, prices are less efficient; even though there is significant price discovery on a per-trade basis in the preopen, the overall lower volume leads to noisier price adjustments.
- **Volatility Patterns:**
  - The preopen is associated with relatively large price changes that reflect higher private information content.
  - In contrast, the postclose, despite experiencing significant volatility (in part due to liquidity imbalances), shows less efficient price discovery, with many price changes being temporary and subsequently reversed.

**D. Weighted Price Contribution:**

- A substantial fraction of the total overnight price change occurs in the preopen. For the overall sample, about 74% of the close-to-open price discovery takes place in the preopen period, while the postclose accounts for roughly 15%.
- This pattern underscores the importance of the preopen session as a period during which substantial private information is quickly incorporated into stock prices—even with relatively sparse trading.

### **4. Implications and Conclusion**

**Market Structure and Regulation:**

- The findings suggest that even low-volume trading periods can play a critical role in the price discovery process. This has direct implications for market participants such as exchanges, market makers, and regulators when designing trading hours and after-hours trading rules.
- Decisions regarding whether to extend trading hours, how to price trades, or the degree of regulatory oversight during these periods may be informed by understanding the tradeoff between liquidity and the informational content of trades.

**Trading Strategies:**

- For informed traders, the preopen period offers an opportunity to trade on private information when the market is less crowded and liquidity is low, albeit with higher price volatility.
- Conversely, liquidity-seeking traders might prefer the regular trading day or postclose periods, where they can benefit from the greater volume and tighter spreads.

**Efficiency of Price Discovery:**

- Although the trading day remains the primary driver of efficient price discovery, the study highlights that after-hours trading contributes meaningfully to the overall incorporation of new information—albeit less efficiently.
- The disproportionate impact of individual trades after hours (especially in the preopen) on price changes helps explain the observed dynamics in market volatility and efficiency during different sessions.

**Conclusion:**

The paper demonstrates that after-hours trading, particularly in the preopen session, plays a significant role in the price discovery process despite its low volume. While the regular trading day provides efficient and high-volume liquidity that leads to smoother price adjustments, after-hours trading reveals substantial private information on a per-trade basis. This duality—high efficiency during the day versus concentrated, information-rich trading outside regular hours—offers important insights for market design, trading strategy, and regulatory policy.



## Charting By Machines

“Charting By Machines” challenges the weak form of the efficient market hypothesis (EMH) by demonstrating that machine learning (ML) techniques can extract profitable signals from historical price data—signals that traditional academic research and classical technical analysis have largely dismissed. Below is a comprehensive summary of the paper’s motivation, methodology, key findings, and contributions.

### **1. Research Motivation and Objectives**

- **Testing the EMH through Technical Data:**

  The weak form of the EMH posits that all information derivable from past price movements is already reflected in current stock prices, rendering technical analysis ineffective. However, despite academic skepticism, technical analysis remains popular among practitioners. The paper re-examines this debate by employing ML algorithms to forecast stock returns using only information that can be gleaned from historical price plots—in this case, the cumulative monthly returns over the past year.

- **Core Research Questions:**

  - Can ML models forecast future stock returns using only historical price information?
  - Do these forecasts predict the cross-section of future returns even after accounting for well-established effects such as momentum and reversal?
  - Is the forecasting function characterized by meaningful nonlinearities and interactions, and is it stable over long periods?
  - Do models that perform well during the model-optimization phase continue to deliver out-of-sample predictive power?

### **2. Data and Sample Construction**

- **Data Source and Time Frame:**

  The authors use monthly stock data from CRSP covering an extensive period—from January 1927 to December 2022. This long sample is divided into an “optimization period” (January 1927 to June 1963) and a “test period” (July 1963 to December 2022) to ensure that model selection and forecast evaluation are separated temporally.

- **Input Variables and Dependent Variable:**

  The ML models are fed with 12 inputs representing cumulative stock returns over the past 12 months (denoted as CR1 through CR12). These variables mirror the type of information traditionally used by chartists. The forecasts target the normalized excess return of a stock for the upcoming month. Different transformations of the future excess return are considered (such as a standardized, a normalized, and percentile-based version) to mitigate issues with leptokurtosis and to focus on rank ordering across stocks.

### **3. Machine Learning Methodology**

- **Model Optimization and Architecture Selection:**

  The authors explore 96 different ML model configurations, which are generated from the combinations of:

  - **Architectures:** Four neural network types are considered: a feed-forward neural network (FNN), a convolutional neural network (CNN), a long short-term memory (LSTM) network, and a hybrid CNNLSTM.
  - **Loss Functions:** Both mean squared error (MSE) and mean absolute error (MAE) are used.
  - **Weighting Schemes:** Models are evaluated with different ways to weight observations (equal weighting, equal per month, and value-weighted within each month).
  - **Dependent Variable Transformations:** Different transformations of future excess returns (raw excess return, standardized, normalized, and percentile values) are tested.

  Through rigorous out-of-sample cross-validation based solely on data from the optimization period, the optimal configuration was determined to be a CNNLSTM architecture with the MSE loss function, using an equal weight per month (EWPM) scheme and the normalized excess return (rNorm) as the dependent variable. Ensemble averaging over 30 independent fits is employed to reduce randomness in the ML output and to ensure robust forecasts.

- **Generating Forecasts:**

  The selected ML model is then applied using an expanding-window methodology. That is, the forecasting function is re-estimated at various points in time using all available past data up to that moment. The resulting forecast for any given stock and month (denoted MLER) is the ensemble average of multiple runs of the ML process.

### **4. Empirical Findings**

- **Strong Cross-Sectional Predictive Power:**

  Portfolios formed by sorting stocks into deciles based on their MLER forecasts exhibit a monotonic pattern in realized excess returns. For example, the decile with the highest predicted returns earns, on average, substantially higher returns compared to the decile with the lowest predicted returns. A long-short portfolio (long the top decile and short the bottom decile) generates an average excess return of approximately 1.08% per month, which is economically significant and statistically robust (with a t-statistic of 5.51). These return differences persist even among large stocks, such as when the sample is restricted to the top 500 by market capitalization.

- **Risk-Adjusted Performance Not Explained by Traditional Factors:**

  Comprehensive asset pricing tests reveal that even after controlling for popular risk factors—including momentum, reversal, and other factor models (CAPM, Fama–French 3-factor, Carhart 4-factor, among others)—the ML-based decile portfolio’s alpha remains positive and significant. This suggests that the ML model uncovers information not captured by conventional risk premia.

- **Stability and Persistence of the Forecasting Function:**

  The study shows that forecasts generated from early periods (e.g., data ending in 1963) continue to have predictive power even over 50 years later, indicating a substantial time-invariant component of the forecasting function. At the same time, while there is evidence of a slowly evolving, time-varying component, overall the forecasting relationships are remarkably stable.

- **Importance of Nonlinearities and Interactions:**

  Analysis of the forecasting function reveals that nonlinear patterns and interactions among past return signals account for a large share of the model’s predictive variation. These complex patterns are crucial in explaining future returns and indicate that simple linear models may miss critical signals that the ML approach captures.

- **Efficacy of the Optimization Procedure:**

  The researchers validate that models selected on the basis of their performance during the optimization period continue to perform well out-of-sample. There is a strong positive correlation (around 0.69) between the performance metric used during optimization and the subsequent Sharpe ratios of the associated long–short portfolios.

### **5. Contributions and Implications**

- **Evidence Supporting Technical Analysis:**

  The paper provides robust evidence contrary to the weak form EMH by showing that historical price patterns, when processed through advanced ML models, contain exploitable predictive information. This lends empirical support to the practice of technical analysis and charting, suggesting that these methods have merit when modern computational techniques are applied.

- **Advancement in ML Applications in Finance:**

  By systematically comparing multiple ML architectures and rigorously addressing overfitting and data-mining concerns, the study showcases the potential of deep learning and ensemble methods in asset pricing. The robust out-of-sample performance across decades enhances the credibility of ML as a tool to uncover subtle nonlinear effects in financial markets.

- **Practical Implications for Investment Management:**

  The findings offer actionable insights for portfolio managers. The ability to forecast cross-sectional returns using only easily available historical price information could lead to the development of new quantitative trading strategies and enhance risk management. Moreover, the fact that these signals are not subsumed by existing risk factors implies that they offer an independent source of return.

- **Methodological Contributions:**

  The paper’s approach to model selection—using an entirely ex-ante optimization period and ensemble averaging to generate forecasts—provides a rigorous framework that other researchers can replicate when applying ML to similar problems in finance.

### **6. Conclusion**

“Charting By Machines” delivers compelling evidence that machine learning can successfully extract predictive signals from historical price data—signals that have historically been dismissed by mainstream finance theory. The paper documents that:

- ML-based forecasts (MLER) predict the cross-section of future stock returns with significant economic and statistical strength.
- The predictive relationship exhibits important nonlinearities and interactions that are stable over long time periods.
- The returns from portfolios based on these forecasts are robust to risk adjustments and not merely a reflection of exposure to known risk factors like momentum or reversal.



## Social learning and analyst behavior

This paper investigates whether and how sell‐side equity analysts adjust their earnings forecasts by learning from the forecasts and forecast outcomes of their “peer” analysts—that is, other analysts who cover different firms within the same coverage portfolio. The study’s main findings and contributions can be summarized as follows:

### **1. Research Question and Motivation**

- **Social Learning in Forecasting:**

  The paper tests the notion that analysts not only rely on firm‐specific information but also incorporate signals from the forecast errors and forecast revisions (especially “bold” forecasts) made by peers covering other firms in their coverage portfolio.

- **Beyond Traditional Herding:**

  Unlike classic herding models that focus on analysts mimicking peers on the same firm, this study examines whether analysts learn from peers’ forecasting behavior on other firms they follow, thereby adjusting their own forecasts based on the perceived accuracy (or bias) of these peers.

### **2. Data and Methodology**

- **Data Sources and Sample:**

  The analysis uses quarterly earnings forecasts from the I/B/E/S Detail U.S. file, augmented with share price data from CRSP and firm information from Compustat, covering the period from 1984 to 2017. The authors also collect demographic data (gender and ethnicity) on analysts.

- **Key Variables:**

  - **Forecast Error and Optimism:** Analysts’ forecast error is measured as the difference between their earnings per share (EPS) forecast and the actual EPS (scaled by the share price). Optimism is defined either directly from forecast error or relative to the consensus forecast.
  - **Peer Variables:** The central explanatory variables capture the average forecast error of other analysts (excluding the focal analyst) on other firms in the same analyst’s portfolio from the previous quarter, as well as the incidence of “bold” forecasts—defined as forecasts that deviate significantly from both the analyst’s previous forecast and the contemporaneous consensus.

- **Empirical Approach:**

  The authors use panel regressions with earnings announcement fixed effects (and firm-analyst fixed effects) to isolate the effect of peers’ past forecasting performance on an analyst’s current forecast. The setup allows them to compare differences across analysts who cover the focal firm and to exploit the heterogeneity in the composition of analysts’ coverage portfolios.

### **3. Key Findings**

- **Peer Forecast Errors and Analyst Optimism:**

  Analysts tend to adjust their forecasts in the direction opposite to the errors made by their peers on other portfolio firms. In other words, when peer analysts have been overoptimistic (i.e., their forecasts were too high), a focal analyst’s subsequent forecast becomes less optimistic (and vice versa). The estimated effect is economically meaningful, implying that the social learning mechanism leads to a forecast adjustment corresponding to roughly 2% of the average deviation from consensus.

- **Influence on Bold Forecasting:**

  The study finds that analysts are more likely to issue “bold” forecasts (forecasts that significantly deviate from both their own prior forecast and the consensus) when a higher percentage of their peers have recently issued bold forecasts in the same direction. This suggests that bold forecast revisions are at least partly driven by social learning.

- **Role of Peer Similarity:**

  The impact of peer forecasts is stronger when the peer group shares similar personal characteristics (e.g., gender and ethnicity) with the focal analyst. This indicates that analysts are more influenced by those with whom they share an in-group identity, a finding that aligns with broader social psychology theories.

- **Benefits for Forecast Accuracy:**

  The evidence suggests that social learning improves forecast accuracy. In particular, the actual forecasts made by analysts (which incorporate peer information) are more accurate on average than hypothetical forecasts that would have been made if social learning effects were absent.

### **4. Contributions and Implications**

- **New Insights into Analyst Behavior:**

  The paper extends the literature on analyst herding by demonstrating that sell-side analysts not only mimic peers’ forecasts for the same firm but also update their beliefs based on information gleaned from peers covering different firms within their portfolio.

- **Implications for Market Efficiency and Information Dissemination:**

  As analysts adjust their forecasts based on peer performance, this social learning process may contribute to a more informed and interconnected network of analyst forecasts. Such behavior can help in correcting systematic biases and may enhance the overall quality of earnings predictions.

- **Policy and Practical Insights:**

  Understanding the role of social learning in forecasting can help firms, regulators, and market participants better interpret analyst forecasts. It also provides insights into how professional networks and demographic characteristics influence information processing in financial markets.

In summary, the paper provides robust evidence that sell‐side equity analysts engage in social learning—adjusting their optimism and boldness in forecasts based on the past performance of their peers within their coverage portfolios. This social learning not only influences forecast behavior but also contributes to improving forecast accuracy, offering important insights into how public information and interpersonal dynamics shape analyst behavior in financial markets.



## Institutional Trading, News, and Accounting Anomalies

“Institutional Trading, News, and Accounting Anomalies” examines how institutional investors trade relative to a broad set of accounting-based stock anomalies and explores whether their trading behavior is influenced more by news sentiment than by the anomalies themselves. The authors—Feifei Wang, Xuemin (Sterling) Yan, and Lingling Zheng—analyze institutional trading patterns during the anomaly formation period and provide a fresh perspective on the mixed evidence regarding institutions’ ability to exploit accounting anomalies.

Below is a detailed summary of the study’s key components:

### **1. Research Motivation and Background**

- **Accounting Anomalies and Market Mispricing:**

  Previous literature documents that various accounting measures (e.g., earnings, cash flows, accruals) predict the cross-section of stock returns. These predictions have been attributed to market inefficiencies arising from incomplete incorporation of accounting information—often interpreted through a behavioral lens.

- **Institutional Investors and Anomaly Exploitation:**

  If accounting anomalies are driven by mispricing, sophisticated investors—especially institutional investors—should be able to arbitrage and correct these pricing errors. However, prior studies yield mixed findings on whether institutions successfully exploit these anomalies.

- **Research Question:**

  The paper investigates whether institutional investors trade in line with accounting-based anomaly signals and, crucially, whether the observed heterogeneous trading patterns can be explained by institutions’ tendency to trade based on news sentiment.

### **2. Methodology and Data**

- **Classification of Anomalies:**

  The authors compile a sample of 56 continuous accounting anomalies from prior studies. Using a K-means clustering algorithm, they objectively separate these anomalies into two groups:

  - **Overreaction Anomalies:** Typically associated with value anomalies (e.g., book-to-market, cash flow-to-price) where the market is thought to overreact to news.
  - **Underreaction Anomalies:** Generally related to profitability measures (e.g., return on assets, gross profitability) where the market underreacts, as seen in phenomena like the post-earnings-announcement drift (PEAD).

- **Measuring Institutional Trading:**

  The study measures institutional trading over a six-quarter anomaly formation period using two metrics:

  1. **Change in Institutional Ownership:** The change in the percentage of shares held by institutions.
  2. **Percentage Change in the Number of Institutional Holders:** Reflecting entry and exit activity.

  For each anomaly, they calculate the net institutional trading as the difference between trading in the anomaly’s “long leg” (stocks expected to outperform) and its “short leg” (stocks expected to underperform).

- **Data Sources:**

  Stock and accounting data are sourced from CRSP and COMPUSTAT, while institutional holdings are obtained from the Thomson/Refinitiv 13F database. The sample covers U.S. common stocks (excluding financials) from 1982 to 2021.

### **3. Main Empirical Findings**

- **Opposite Institutional Trading Patterns:**

  - **Overreaction Anomalies:**

    Institutions tend to trade “in the wrong direction.” In the sample of overreaction anomalies, they are net sellers of the long leg relative to the short leg (net institutional trading averages around –2.47% in ownership changes and –15.33% in changes in the number of institutional holders). This implies institutions buy more of the short-leg stocks, which, according to the anomaly, are expected to eventually outperform.

  - **Underreaction Anomalies:**

    Conversely, institutions trade “in the right direction” by buying more of the long leg than the short leg (with net institutional trading averaging 1.59% and 9.26% across the two measures, respectively).

- **News Sentiment as the Driving Factor:**

  The authors propose that the divergent trading behaviors are not necessarily due to superior or inferior anomaly-trading skills but are instead driven by institutions’ propensity to trade in the direction of news:

  - Institutions generally buy stocks experiencing good news and sell stocks facing bad news.
  - Empirical evidence using both standardized unexpected earnings (SUE) and a comprehensive newswire release database (TRNA) shows that stocks with positive news attract higher institutional buying.
  - For overreaction anomalies, stocks in the short leg (often growth stocks) tend to display more good news relative to those in the long leg (often value stocks), leading institutions to trade contrary to the anomaly prescriptions.
  - For underreaction anomalies, stocks in the long leg (typically firms with better profitability) experience more positive news, resulting in institutional trading that conforms with anomaly predictions.

- **Institutional Heterogeneity:**

  The paper further distinguishes between different types of institutional investors:

  - Both mutual funds and hedge funds exhibit similar overall patterns—trading against overreaction anomalies and in favor of underreaction anomalies.
  - Short sellers (proxied by changes in short interest) generally trade in the “right” direction for both anomaly types.
  - When considering hedge funds’ combined long and short positions, the evidence suggests they correct for underreaction anomalies while the mispricing associated with overreaction anomalies remains exacerbated.

- **Impact on Subsequent Anomaly Returns:**

  The analysis shows that the subsequent returns on the anomaly-based long-short portfolios are conditional on institutional trading:

  - When institutions trade in the wrong direction (as seen in overreaction anomalies), the resulting mispricing and subsequent anomaly returns are larger.
  - In contrast, when institutions trade in the right direction (as in underreaction anomalies), the mispricing is mitigated, and subsequent long-short returns diminish.

### **4. Interpretation and Implications**

- **Unified Explanation:**

  The study argues that institutional investors’ trading is primarily driven by news sentiment rather than by the exploitation of accounting anomalies per se. Institutions’ inclination to follow recent news causes them to:

  - Trade against the theoretical predictions of overreaction anomalies.
  - Trade in line with underreaction anomalies.

- **Potential Drivers Behind News-Based Trading:**

  Several explanations are explored for why institutions trade in the direction of news:

  - **Agency Problems and Short-Termism:** Transient institutions (with shorter investment horizons) are more prone to follow news sentiment, which aligns with the observed trading behavior.
  - **Market Underreaction and Over-Extrapolation:** Institutions may be motivated by beliefs about market inefficiencies—for instance, expecting the market to underreact (or overreact) to new information.
  - The study finds little evidence for alternative explanations such as the prudent-man law (which would suggest stronger adherence to risk-based trading norms among banks and insurance companies) or window dressing (making portfolios appear better at reporting time).

- **Broader Implications for Market Efficiency:**

  The findings suggest that institutional trading patterns, driven by news sentiment, may contribute to persistent mispricings in the market. In overreaction anomalies, this trading behavior exacerbates mispricing, while in underreaction anomalies, it helps correct it—thereby influencing the evolution and persistence of accounting anomalies over time.

- **Contributions to Literature:**

  This work builds upon previous studies by offering a comprehensive look at how institutions interact with accounting anomalies across a large sample and by providing a unified explanation based on news-driven behavior. It also contributes to our understanding of the role that institutional trading plays in market efficiency, anomaly persistence, and the dissemination of information.

### **5. Conclusion**

The paper concludes that institutional investors, rather than systematically arbitraging away accounting mispricings, exhibit heterogeneous trading behavior that aligns with news sentiment. Institutions tend to:

- Trade against overreaction anomalies (buying more of stocks that, according to the anomaly, should be shorted) because those stocks tend to have more favorable news.
- Trade in accordance with underreaction anomalies (buying stocks with better fundamentals) as these stocks tend to exhibit more positive news during the anomaly formation period.

This news-driven trading behavior, influenced further by institutional characteristics such as short-termism, ultimately exacerbates mispricing in overreaction anomalies while mitigating it in underreaction anomalies. The findings have significant implications for our understanding of market efficiency, the persistence of accounting anomalies, and the behavior of institutional investors.



## Ambiguity about Volatility and Investor Behavior

“Ambiguity about Volatility and Investor Behavior” investigates how time‐varying market ambiguity—specifically, ambiguity about future volatility—affects the trading and risk‐taking behavior of individual investors. The authors (Kostopoulos, Meyer, and Uhr) use detailed transaction data from a major German online brokerage (covering March 2010 to December 2015) along with market‐based measures of ambiguity to explore this question. Below is a comprehensive summary of the paper’s key components:

### **1. Research Motivation and Theoretical Background**

- **Risk versus Ambiguity:**

  In traditional finance, uncertainty is separated into risk (where outcomes and their probability distributions are known) and ambiguity (where the probability distribution itself is unknown). Drawing on Knight (1921) and later work by Ellsberg (1961), the paper emphasizes that investors are not only exposed to risk but also to ambiguity.

- **Ambiguity about Volatility:**

  While prior research has largely focused on the impact of risk (or expected volatility) on investor behavior, this paper concentrates on ambiguity regarding volatility—that is, the uncertainty about how volatile asset returns will be in the near future. This “second‐order” uncertainty is believed to influence investor decisions beyond the effects of simple risk measures.

- **Investor Behavior under Ambiguity:**

  Theoretical models suggest that when ambiguity is high, investors might face difficulty in assessing fundamental risks, which can lead to behavioral responses such as increased attention (more frequent logins) and portfolio adjustments (altered trading activity, often leading to a reduction in exposure to risky assets). Moreover, ambiguity aversion implies that investors with a higher dislike for ambiguity are expected to react more strongly to ambiguity shocks.

### **2. Data and Measurement of Ambiguity**

- **Investor Data:**

  The empirical analysis is based on the trading records of over 100,000 individual investors from a large German online brokerage. The data record all transaction-level security trades and logins from January 2001 through December 2015 (with ambiguity measures available from March 2010 onward). The dataset includes detailed information on investor characteristics (e.g., demographics, portfolio value) and trading activity (e.g., number of logins, executed trades).

- **Market-Based Ambiguity Measure:**

  The primary ambiguity measure used is the V-VSTOXX, which captures the “volatility of volatility” of the Euro Stoxx index’s options.

  - **VSTOXX vs. V-VSTOXX:**

    While VSTOXX reflects the market’s expectation for volatility over the next 30 days, V-VSTOXX measures the uncertainty about that expected volatility—that is, it serves as a proxy for ambiguity about volatility. The paper uses daily innovations in V-VSTOXX (denoted as dVVSTOXX) to capture changes in aggregate ambiguity.

- **Alternative Ambiguity Measures:**

  For robustness, the authors also employ a survey-based measure—derived from the dispersion of professional forecasters’ predictions of real GDP growth (from the Survey of Professional Forecasters)—which provides a more long-term view of ambiguity. Additional controls include sentiment measures like the FEARS index (an index based on Google search volumes for negative economic terms).

### **3. Empirical Methodology**

- **Behavioral Outcomes Studied:**

  The paper analyzes two key dimensions of investor behavior:

  1. **Activity:** Measured by the frequency of logins (i.e., how often investors check their portfolios) and by actual trading (the decision to execute a trade on a given day).
  2. **Risk-Taking:** Assessed by changes in portfolio exposure, operationalized as deviations in “buy-sell imbalance” from an investor’s typical trading behavior. The imbalance is computed both in terms of trade counts and in euro value, with adjustments (demeaning) relative to the investor’s average activity over a prior period.

- **Econometric Framework:**

  The authors use panel regressions with individual investor fixed effects to control for both observable and unobservable heterogeneity across investors. The basic regression framework links an investor’s trading behavior (logins or trades) or their risk-taking measure (excess buy-sell imbalance) to innovations in ambiguity (dVVSTOXX), while controlling for:

  - Expected volatility (using the innovation in VSTOXX, dVSTOXX)

  - Sentiment (using the FEARS index)

  - A host of calendar and market controls (e.g., holidays, market returns, announcements)

    Standard errors are clustered at the individual investor level, ensuring robustness to heteroscedasticity and autocorrelation.

### **4. Main Empirical Findings**

- **Increased Trading Activity:**

  When aggregate ambiguity rises—as captured by positive innovations in dVVSTOXX—individual investors are more active:

  - **Logins:** There is a statistically significant increase in the probability that an investor logs into their brokerage account on a day when ambiguity is higher. This suggests that higher ambiguity prompts investors to recheck their portfolios for updates.
  - **Trades:** Similarly, the likelihood of executing a trade also increases significantly with higher ambiguity. The effect remains robust after controlling for expected volatility and sentiment, indicating that ambiguity exerts an independent influence on investor activity.

- **Reduced Risk-Taking:**

  Despite the increase in overall activity, higher ambiguity shocks lead investors to reduce their exposure to risky assets:

  - The paper measures risk-taking via the deviation of an investor’s buy-sell imbalance from their typical (demeaned) trading behavior. The findings show that a one-unit increase in dVVSTOXX is associated with a statistically significant decrease in the excess buy-sell imbalance.
  - In practical terms, when market ambiguity is high, investors tend to trade out of or reduce positions in riskier securities. This adjustment in portfolio risk does not quickly reverse over the next ten days, suggesting that ambiguity shocks have a lasting impact on investors’ risk exposure.

- **Economic Significance:**

  When standardized, the effect of ambiguity on investor behavior is comparable to that of key household finance variables. For example, a one-standard-deviation increase in dVVSTOXX translates into an increase in the probability of logging in that is of a similar magnitude to (or even exceeds) that of well-documented attention effects (such as those induced by large market returns).

- **Ambiguity versus Volatility:**

  Importantly, the effects of ambiguity are distinct from those associated with expected volatility. Although both volatility and ambiguity measures are related to market uncertainty, only the ambiguity measure (dVVSTOXX) consistently shows a significant relationship with increased investor activity and decreased risk-taking, even when both measures are included in the model.

- **Heterogeneous Effects Based on Ambiguity Aversion:**

  Using survey data derived from an Ellsberg-type urn experiment, the study identifies that ambiguity averse investors (those with a stronger dislike for ambiguity) are considerably more sensitive to ambiguity shocks. In essence, when ambiguity rises, these investors reduce their risky asset exposure much more than investors who are ambiguity neutral or ambiguity seeking.

### **5. Conclusions and Implications**

- **Investor Behavior Under Uncertainty:**

  The paper provides robust evidence that aggregate ambiguity about future volatility significantly influences individual investor behavior. When ambiguity increases, investors become more active (as measured by more frequent logins and trades) but simultaneously act to reduce the riskiness of their portfolios.

- **Policy and Market Design Implications:**

  These findings have important implications for understanding market dynamics during periods of heightened uncertainty. Since ambiguity leads to a sustained reduction in risk-taking, it can influence asset prices and the overall allocation of capital. Recognizing that ambiguity (and not just expected volatility) affects investor trading can help regulators and market participants better interpret trading patterns during uncertain economic times.

- **Contribution to the Literature:**

  This work extends the literature on investor behavior by separating the effects of ambiguity from traditional risk. It highlights that ambiguity shocks matter in real trading decisions, and that they operate independently of, and sometimes more strongly than, conventional volatility measures. The use of high-frequency, market-based measures like the V-VSTOXX offers a fresh, model-free approach to quantifying ambiguity in capital markets.

In summary, “Ambiguity about Volatility and Investor Behavior” finds that higher levels of aggregate ambiguity (measured by innovations in the volatility-of-volatility, dVVSTOXX) increase individual investors’ activity (more logins and trades) while prompting them to reduce their exposure to risky assets. These effects are robust to controls for volatility and sentiment, and ambiguity-averse investors exhibit the strongest behavioral responses. The study underscores the role of ambiguity—distinct from risk—in shaping investor trading and portfolio adjustments.