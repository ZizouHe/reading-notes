# Temp

## The Expected Returns on Machine-Learning Strategies

The paper titled "The Expected Returns on Machine-Learning Strategies" by Vitor Azevedo, Christopher Hoegner, and Mihail Velikov investigates the profitability of machine learning-based anomaly trading strategies in the stock market. The study takes into account transaction costs, post-publication decay, and the impact of the post-decimalization era of high liquidity on these strategies.

Key points from the paper include:

1. **Sophisticated Machine Learning Strategies**: Contrary to previous claims, more advanced machine learning strategies can be profitable. They can achieve net out-of-sample monthly returns of up to 1.42%, even with high turnover rates exceeding 50% and the selection of stocks that are traditionally difficult to arbitrage.

2. **Performance Metrics**: The study uses various machine learning techniques, including Ordinary Least Squares with Huber Loss Function (OLS-HUBER), Elastic Net (ENET), Feedforward Neural Networks (FFNN), Long Short-Term Memory networks (LSTM), and an ensemble model. These models are evaluated based on out-of-sample regression metrics and their ability to generate returns after costs.

3. **Return Predictability**: The paper documents that deep-learning models can predict returns that cannot be explained by common risk factors or limits to arbitrage. A trading strategy using a long short-term memory model yields a significant six-factor generalized (net) alpha of 1.20% with a t-statistic of 3.46.

4. **Cost Mitigation Techniques**: While prevalent techniques can reduce turnover and costs, they do not improve net anomaly performance. The study explores various cost mitigation strategies, such as increasing the holding period, using quintile portfolios, and applying a Buy-Hold-Spread (BHS) strategy.

5. **Post-2005 Performance**: The study finds that machine learning combination signals perform well out-of-sample, even in the high liquidity environment post-2005, and only including anomalies after their publication dates.

6. **Transaction Costs**: The improved liquidity in the post-2005 period means that the trading costs associated with these strategies are relatively low, at 20-25 basis points per month. Despite these costs, most machine learning strategies continue to deliver significant returns.

7. **Generalized Alphas**: The paper also introduces the concept of generalized alphas to evaluate the ability of machine learning strategies to expand the net-of-costs mean-variance efficient frontier based on the six factors of the Fama and French (2018) model.

8. **Implications**: The findings suggest that machine learning strategies can be profitable in the current era of high liquidity and discovered anomalies, challenging previous conclusions that suggested otherwise.

9. **Methodology**: The paper uses an expanding window approach for training data and a fixed-length moving validation set to avoid data snooping or look-ahead bias. It also employs hyperparameter tuning to optimize model parameters.

10. **Conclusion**: The study concludes that machine learning-based trading strategies can yield significant returns even after accounting for transaction costs and other factors, providing valuable insights for both academic research and practical investment strategy design.

The paper contributes to the growing literature on machine learning in asset pricing by focusing on the expected returns of machine learning strategies and carefully considering trading costs and other practical implementation issues.



## Number Processing Constraints and Earnings News

The paper titled "Number Processing Constraints and Earnings News" by Stephen A. Karolyi, Thomas G. Ruchti, and Phong Truong explores how human neurological constraints in processing numbers may affect stock market reactions to earnings announcements (EAs). Here's a summary of the key points:

1. **Neuroscience Background**: The study is grounded in neuroscience research indicating that the human brain processes small numbers linearly and large numbers logarithmically, which can lead to an underreaction to larger numbers as their perceived differences become smaller.

2. **Hypothesis**: The authors hypothesize that investors will respond less to the same earnings news for stocks with high earnings per share (EPS) magnitudes compared to those with low EPS magnitudes due to these neurological constraints.

3. **Earnings Announcements (EAs)**: EAs are chosen as a setting to test the hypothesis because they are significant corporate events that present investors with numerical data for decision-making.

4. **Earnings Response Coefficient (ERC)**: The study uses the ERC framework to test the hypothesis. The market response to earnings news is expected to increase with the standardized earnings surprise, but the number processing constraints hypothesis predicts a reduced response for high EPS magnitudes.

5. **Findings**: The research finds that investors indeed react less to earnings news for stocks with high EPS magnitudes, which is consistent with the number processing constraints hypothesis. This effect is distinct from other risk-based and behavioral explanations.

6. **Robustness Tests**: The results hold up under various robustness tests, including controlling for stock price levels, limited attention, and other factors that could influence market reactions to earnings news.

7. **Machine Presence**: The study finds that the effect of number processing constraints is less pronounced for stocks with a high presence of machines or robotic activity, suggesting that non-human market participants are not subject to the same cognitive limitations.

8. **Post-Earnings Announcement Drift (PEAD)**: Stocks with high EPS magnitudes are found to have a higher post-EA drift, suggesting that the initial underreaction to earnings news contributes to this phenomenon.

9. **Stock Splits**: The paper uses stock splits as a quasi-experimental design to test the hypothesis further. Stock splits, which increase the number of outstanding shares and thus decrease EPS magnitude, provide a setting to observe changes in market reactions to earnings news.

10. **Implications**: The findings suggest that number processing constraints have implications for stock price efficiency and can contribute to the well-documented phenomenon of underreaction to earnings news and subsequent drift.

11. **Contribution**: The study contributes to the literature at the intersection of accounting, finance, and neuroscience by linking cognitive neuroscience to stock market phenomena and offering a fresh perspective on the systematic underreaction to earnings news.

The paper concludes that human cognitive limitations in number processing can have a significant impact on financial decision-making and market efficiency, and that the advent of machine involvement in trading may mitigate some of these effects.



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



## From Transcripts to Insights: Uncovering Corporate Risks Using Generative AI

The paper titled "From Transcripts to Insights: Uncovering Corporate Risks Using Generative AI" by Alex G. Kim, Maximilian Muhn, and Valeri V. Nikolaev explores the application of generative AI tools, such as ChatGPT, in assessing and uncovering corporate risks. The authors develop and validate measures of firm-level risk exposure related to political, climate, and AI-related risks using the GPT 3.5 model. They generate risk summaries and assessments from earnings call transcripts to demonstrate that these AI-based measures have significant information content and can predict firm-level volatility and corporate decisions related to investment and innovation more effectively than existing risk measures.

Key points from the paper include:

1. **AI in Risk Assessment**: The authors leverage large language models (LLMs) to detect and analyze critical corporate risks from textual data, such as earnings call transcripts.

2. **GPT-based Measures**: They use the GPT 3.5 model to create risk exposure measures that outperform traditional measures in predicting stock market volatility and firms' economic outcomes.

3. **Value of General AI Knowledge**: The paper establishes that the information in risk assessments, which utilize the general knowledge of the AI in addition to the text context, is more valuable than that in risk summaries.

4. **Detection of Emerging Risks**: Generative AI is effective at identifying emerging risks, such as AI risk, which has gained significance in recent times.

5. **Performance Outside Training Window**: The measures developed perform well both within and outside the training window of the GPT model, indicating their robustness.

6. **Equity Market Pricing**: The paper also discusses how the risk measures are priced in equity markets, suggesting that they provide useful insights to investors.

7. **Contribution to Literature**: The study contributes to the literature by demonstrating the economic usefulness of AI-powered LLMs in risk assessment and by enhancing the understanding of corporate risks through AI-based technology.

8. **Methodology**: The authors use a variety of econometric models and analyses, including variance decomposition and Fama-MacBeth regressions, to validate their findings.

9. **Implications for Firm Decisions**: The paper shows that firms' investment decisions and actions to mitigate risks, such as lobbying activity and patent filings, are associated with the risk exposure measures generated by the AI.

10. **Robustness Checks**: The results are robust to various research design choices and hold true in out-of-sample tests, suggesting that the AI model's ability to produce valid risk measures is not due to in-sample knowledge.

In conclusion, the paper highlights the potential of generative AI in providing valuable insights into corporate risks at a low cost, which can be useful for investors and corporate decision-makers. However, it also acknowledges the limitations and challenges associated with relying on generative LLMs, such as the sensitivity to prompt quality and the potential for incorrect information.



## The Ghost in the Machine: Generating Beliefs with Large Language Models

The paper titled "The Ghost in the Machine: Generating Beliefs with Large Language Models" by J. Leland Bybee from Yale University introduces a methodology for generating economic expectations using large language models (LLMs) applied to historical news data. The author makes these key contributions:

1. **Methodology Introduction**: The paper introduces a new method for generating economic expectations using large language models (LLMs) applied to historical news data.

2. **Alignment with Survey Measures**: Generated expectations closely match existing survey measures and capture similar deviations from full-information rational expectations.

3. **Historical Economic Expectations**: The methodology is used to create 120 years of economic expectations, allowing for the construction of a long-term economic sentiment measure.

4. **Economic Sentiment and Bubbles**: The economic sentiment measure is employed to investigate behavioral theories of bubbles, revealing a link between industry exposure to sentiment and the likelihood of a crash along with lower future returns.

5. **Feedback Mechanism**: The study finds a higher degree of feedback between returns and sentiment during run-ups that crash, suggesting return extrapolation as a key bubble mechanism.

6. **Data Sources**: Historical news articles from The Wall Street Journal and The New York Times are used to train the LLM and generate expectations.

7. **Comparison with SPF**: Generated macroeconomic expectations are compared with the Survey of Professional Forecasters (SPF), showing significant correlation with SPF revisions.

8. **Out-of-Sample Validation**: The paper addresses the concern of look-ahead bias by evaluating generated expectations out-of-sample, post-training period of the LLM.

9. **Economic Sentiment Dynamics**: The 120-year time series of economic sentiment is analyzed, showing its correlation with past returns and disconnect from objective measures of expected returns.

10. **Trading Strategy**: A trading strategy based on sentiment betas and impulse response functions is proposed, which predicts crashes with significant accuracy and earns substantial returns.



## Financial Statement Analysis with Large Language Models

The paper titled "Financial Statement Analysis with Large Language Models" by Alex G. Kim, Maximilian Muhn, and Valeri V. Nikolaev investigates the capability of Large Language Models (LLMs), specifically GPT4, in performing financial statement analysis (FSA) akin to professional human analysts. The authors aim to understand if LLMs can analyze and interpret financial data to predict future earnings without relying on narrative or industry-specific information.

Key findings and contributions of the paper include:

1. **LLM's Capability in FSA**: The study reveals that LLMs, when provided with standardized and anonymous financial statements, can outperform human financial analysts in predicting changes in future earnings. This suggests that LLMs can effectively perform a task traditionally done by humans, which involves numerical analysis and judgment.

2. **Comparison with Human Analysts**: The LLM demonstrates a relative advantage in situations where human analysts typically struggle, such as with small or loss-making companies. The model's performance is on par with or exceeds the performance of human analysts and narrowly trained machine learning models.

3. **Prediction Accuracy**: The LLM's prediction accuracy is comparable to that of a state-of-the-art machine learning model, indicating that LLMs can leverage their vast knowledge base to analyze financial numbers and generate useful insights.

4. **Chain-of-Thought Prompting**: The study employs a "Chain-of-Thought" (CoT) prompting technique, which instructs the LLM to mimic the step-by-step analysis process of human financial analysts. This approach significantly improves the model's predictive performance.

5. **Out-of-Sample Testing**: The paper also presents out-of-sample tests using financial data from 2022 to predict 2023 earnings, which shows that the LLM's predictive ability is not reliant on its training data or memory, but rather on its ability to analyze and interpret new data.

6. **Economic Usefulness**: The authors demonstrate that trading strategies based on the LLM's predictions yield higher Sharpe ratios and alphas compared to strategies based on other models, indicating the potential economic value of using LLMs for financial decision-making.

7. **Information Content of LLM-Generated Texts**: The paper shows that the narratives generated by the LLM during its analysis have informational value and contribute to its predictive ability. These narratives are found to be useful in predicting stock price movements.

8. **Implications for Financial Markets**: The findings suggest that LLMs could play a central role in financial decision-making processes, complementing or potentially replacing some aspects of human analysts' work.

9. **Limitations and Future Research**: While the study provides evidence of LLMs' capabilities in FSA, it also acknowledges the challenges in understanding precisely how and why the model makes accurate predictions. The authors call for further research to explore the integration of LLMs in financial markets and their impact on decision-making.

In conclusion, the paper presents a comprehensive analysis of LLMs' potential to transform financial statement analysis, offering insights into their ability to understand and predict financial outcomes based solely on numerical data. The results highlight the growing relevance of AI in the financial sector and open avenues for future exploration of LLMs in complex decision-making tasks.



## Predicting Performance Using Consumer Big Data

The paper titled "Predicting Performance Using Consumer Big Data," authored by Kenneth Froot, Namho Kang, Gideon Ozik, and Ronnie Sadka, explores the efficacy of consumer big data as a tool for predicting firms' fundamentals and stock returns. Here's a summary of the key points:

1. **Proxies for Corporate Sales**: The authors construct three proxies for real-time corporate sales using distinct information sources: in-store foot traffic (IN-STORE), web traffic to companies' websites (WEB), and consumers' interest level in corporate brands and products (BRAND).

2. **Sample and Timeframe**: The study uses data from a sample of 330 firms over the period 2009–2020.

3. **Significant Profitability**: Trading strategies using these proxies result in significant net-of-transaction-costs profitability.

4. **Pandemic Impact**: During the pandemic, there was a significant increase in WEB activity and a notable decrease in IN-STORE, reflecting a shift from physical stores to online platforms.

5. **Information Dissemination**: The study suggests that information from IN-STORE and BRAND is not immediately available to investors, while WEB information is more rapidly diffused.

6. **Performance During Pandemic**: The results indicate that information diffusion worsened during the pandemic, with an increased return predictability of sales proxies.

7. **Portfolio Returns**: The paper examines the performance of portfolio strategies based on the sales proxies and finds that they provide positive alphas, indicating profitability after considering transaction costs.

8. **Consumer Activities Shift**: The COVID-19 pandemic has significantly impacted consumer behavior, leading to a decrease in in-store activities and an increase in online activities.

9. **Predictability of Returns**: The predictability of portfolio returns using sales proxies increased during the pandemic, suggesting slower information dissemination compared to the pre-pandemic period.

10. **Conclusion**: The paper concludes that big data on consumer activities can predict firms' fundamentals and stock returns, with different proxies reflecting different aspects of market fundamentals and information dissemination speed.

The paper is set to be published in the April 2022 issue of the Journal of Portfolio Management.



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