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