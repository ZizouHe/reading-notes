# Quant Finance Notes

## Alternative Data

- [另类数据与分析师盈利预测](https://zhuanlan.zhihu.com/p/621054463)
  - Dessaint, O., T. Foucault, and L. Fresard (2022). Does alternative data improve financial forecasting? The horizon effect. Working paper.
  - 假设分析师在进行盈利预测时，需要最优地分配其投入到不同时间尺度预测的精力，从而最小化预测误差以及获取不同时间尺度预测信息的成本这二者之和。另类数据的出现降低了获取短期预测数据的成本，并同时提高了短期预测数据的准确度。因此，它促使分析师将更多的精力投入到获取和分析短期预测信息上，以此来提高短期预测的准确度。然而顾此失彼，由于分析师的精力是有限的，这造成的后果是降低了他们长期预测的准确度。

- Wolfe Research | Global Stock Selection with Proprietary Global Trademark Data

  - USPTO, foreign applications, Madrid filing, international registration
  - Trademark is not a proxy of advertising spending. Firms with very high advertising spending may over-spend and suffer from agency problem. 
  - Signal transformations: growth rate, vintage ratio (long term number / short term number), long/short lookback window; residualizing size (log revenue) and sector.
  - Use life cycle of trademark to construct signals: applications, success rate of application, renewal ratio, trademark age, age dispersion, dispersion in trademark category, secretive foreign priority application (to keep trademark information under protection, and re-file in US using international registration)
  - Trademark category to construct linkage.

- Wolfe Research | The Intangible Asset Premia

  - KC (Knowledge Capital): accumulate past R&D spending with discount (perpetual inventory method)

  - OC (Organizational Capital): accumulate 30% of past SG&A expenses.

  - IAI (Intangible Asset Intensity), KCI, OCI:
    $$
    \begin{aligned}
    IAI &= \frac{KC + OC}{KC + OC + \text{total asset} - \text{goodwill}}, \\
    KCI &= \frac{KC}{KC + OC + \text{total asset} - \text{goodwill}}, \\ 
    OCI &= \frac{OC}{KC + OC + \text{total asset} - \text{goodwill}}.
    \end{aligned}
    $$
    
  - OCI+KCI combined has consistently more relevant than growth factor (as risk factor).

  - Firm with higher IAI score has higher momentum scores. 

- Wolfe Research | Patent, Innovation, and Alpha

  - Innovation industry: all industries where at least 50% firms have patent grants. High R&D spending (log R&D residualized by log market cap) is negatively correlated to future return, but is positively correlated to future return in innovation industry group. 
  - Signals: 
    - number of unique patent class / number of patent
    - Inward citation number, unique inward citation assignee; Outward citation number, unique outward citation assignee
    - Citation as linkage; patent class as linkage.
    - Patent maintenance.

- Wolfe Research | Innovation Relevance

  - Total citations for all patents that a firm has cited to form a firm i's knowledge base (**we can normalize within each patent class for citation**)
    $$
    \mathrm{Cit}^i_{t} = \sum_{k=1}^{K_t} \mathbb{I}^i_{p_k}  \mathrm{Cit}_t(p_k)
    $$
    where indicator of $$p_k$$ indicates whether a patent $$p_k$$ has been cited by firm i, and $$\mathrm{Cit}_t(p_k)$$ is the total number of citations of patent $$p_k$$ at time $$t$$. Then technological obsolescence is defined as the rate of change over a window $$w$$.
    $$
    \log \mathrm{Cit}^i_{t} - \ln \mathrm{Cit}^i_{t-w}
    $$

  - Investors disagree most on high innovation relevance firms, we can assign higher risk budget to these firms.

- [Lerner, Josh, and Amit Seru. "The use and misuse of patent data: Issues for finance and beyond." *The Review of Financial Studies* 35.6 (2022): 2667-2704.](https://academic.oup.com/rfs/article-abstract/35/6/2667/6324822)

  - **Patent Data Challenges**: Patent data is valuable but can be problematic due to truncation (not all patents are granted by the end of the study period) and changes in inventor composition over time. (Both patent grants and patent citations).
  - **Biases in Aggregation**: When patent data is aggregated at the firm level, biases can persist even after common adjustment methods are applied.
  - **Correlation with Firm Characteristics**: Patent and citation biases are correlated with firm characteristics such as size, market-to-book ratio, and R&D intensity.	![](../notes/pic/patent_checklist.png)

- [Shu, Tao, Xuan Tian, and Xintong Zhan. "Patent quality, firm value, and investor underreaction: Evidence from patent examiner busyness." *Journal of Financial Economics* 143.3 (2022): 1043-1069.](https://www.sciencedirect.com/science/article/pii/S0304405X21004785)
  - This paper attempts to study the causal effect of examiner busyness on patent quality and firm value. Using a broad set of patent quality measures, we find strong evidence that patents allowed by busy examiners exhibit significantly lower quality.

- [Bekkerman, Ron, Eliezer M. Fich, and Natalya V. Khimich. "The effect of innovation similarity on asset prices: Evidence from patents’ big data." *The Review of Asset Pricing Studies* 13.1 (2023): 99-145.](https://academic.oup.com/raps/article-abstract/13/1/99/6656364)

  - [科技关联度 (II)](https://zhuanlan.zhihu.com/p/577519685)
  - Methodology: 
    - Patent text analysis: use external sources such as Wikipedia and professional dictionaries to establish the professional termi- nology for every patent in our sample. This process enables us to define two patents as similar if they share the same professional terminology.
    - Remove “boilerplates” (i.e., long lists of terminology used in patent texts to illus- trate the invention generality).
    - Patent similarity: Two patents' distance is represented as a vector of their common terms weighted by a TFIDF (term frequency– inverse document frequency) variant.
    - Firm similarity: log of the sum of similar patent pairs discounted by the age of the newer patent in each pair and normalize it by the log of the product of the total number of patents for each firm in the pair.

  - 基本面解释：For R&D-to-Total Assets and ROA terms, peer firms have both contemporaneous correlation and prediction power.
  - **信息扩散缓慢的原因是投资者注意力不足，而不是投资者完全完全意识不到关联。**注意力不足意味着投资者未来能认识到关联，因而会有信息的进一步扩散和关联动量。而后者意味着投资者压根就看不到关联的存在，因此也就没关联动量效应了。

- [Narrative Momentum](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4912496)

  - Data
    - The collected news articles are classified into media reservoirs: General, Corporate, FX, and Country Equity.
    - Articles are classified into 347 narratives: including 53 pre-specified Journal of Economic Literature (JEL) narratives and around 300 additional narratives. The 347 narratives are classified into 14 narrative tags including Geopolitics, Macro, Micro, etc. The narrative series are provided by MKT MediaStats, LLC.

  - Construction
    - **Narrative Intensities**: Negative (positive) intensity is the fraction of negative (positive) sentiment articles pertaining to a narrative out of the overall discussion, with a value in [0,1].
    - **Narrative market beta**: whether narratives can explain excess market returns. univariate regressions of the one-month market excess returns on contemporaneous one-month intensity changes.
    - **stock-level narrative betas**: univariate regression of stock return and intensity changes.

  - Conclusion:
    - Financial analysts also tend to underreact to narrative-sensitive stocks
    - Narrative momentum is different from price momentum.

- [Goldman, Eitan, Jordan Martel, and Jan Schneemeier. "A theory of financial media." *Journal of Financial Economics* 145.1 (2022): 239-258.](https://www.sciencedirect.com/science/article/pii/S0304405X21003081)

  - Firms are more likely to manipulate their announcements when media coverage is more extensive.
  - Negative news is more likely to be reported than positive news.
  - The presence of financial journalists can lead to more efficient pricing.

- [Froot, Kenneth, et al. "Predicting Performance Using Consumer Big Data." *Journal of Portfolio Management* 48.3 (2022).](https://scholar.harvard.edu/files/kenfroot/files/Predicting_Performance_Using_Consumer_Big_Data-Aug18.2021.pdf)
  - **Proxies for Corporate Sales**: The authors construct three proxies for real-time corporate sales using distinct information sources: in-store foot traffic (IN-STORE), web traffic to companies' websites (WEB), and consumers' interest level in corporate brands and products (BRAND).
  - Predict SUE, SUR, Analyst forecast error.
  - Check analyst coverage and media exposure, and market attention level to see if the market consensus really matters, whether we want to trade the surprise from consensus or just the quarterly change. 

- Wolfe Research | Global shipping and supply chain alpha

  - S&P global panjiva supply chain intelleigence (US, Brazil, India, Mexico); FactSet (US only)
  - BOL: bill of lading form.
  - Features: 
    - shipping volume (predict sales), (level/growth)
    - supplier, product, country of origin (diversity)
    - supply-chain network (company's position in supply chain)
    - shipping network momentum

- Wolfe Research | Alpha insights from global job postings data

  - RavenPack dataset (most likely use LinkUp)
  - Term construction: job postings level/growth (we can use SOC median salary as importance weight); technical skill intensity, level/growth, uniqueness in skills, adoption of new technical skills, skill importance (TF-IDF).

- DB Research | Macro and Micro JobEconomics

  - LinkUp job posting dataset: scrape from company website. Data since 2007, description data since 2014. Includes SOC job classification, geolocation data, and technical skills data. Most coverage in the USA.
  - Term construction similar for micro.
  - Macro: use to predict employment, PMI index, CPI, retail, consumer sentiment.


## Analyst

- Analyst Forecast Bundling Intensity and Earnings Surprise

  - [Barth, Mary E., et al. "Analyst Forecast Bundling Intensity and Earnings Surprise." *Available at SSRN 4839739* (2024).](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4839739)

  - The authors explore how financial analysts convey information about a company's earnings without necessarily making full revisions to their earnings forecasts. They achieve this by increasing what they term 'bundling intensity,' which refers to the extent to which an analyst's report that includes an earnings forecast revision also includes revisions to price targets and/or recommendations that have the same direction as the earnings forecast revision.

  - The researchers have developed a measure called BF_Score at the firm level to quantify bundling intensity. Their findings suggest that BF_Score is a significant predictor of earnings surprises based on analyst forecasts. These surprises often result from biases in consensus earnings forecasts, which are influenced by the information analysts communicate through bundling intensity. Below is definition of BR score, where TP is target price.

    ![](../notes/pic/br_score.png)

  - The use of bundling and the predictive power of BF_Score increase during times of higher macroeconomic uncertainty, when analysts have greater incentives to avoid bold revisions to their earnings forecasts. 

- [He, Jie Jack, and Xuan Tian. "The dark side of analyst coverage: The case of innovation." *Journal of financial economics* 109.3 (2013): 856-878.](https://www.sciencedirect.com/science/article/pii/S0304405X13001086)

  - Firms covered by a larger number of analysts generate fewer patents and patents with lower impact. 
  - The evidence is consistent with the hypothesis that analysts exert too much pressure on managers to meet short-term goals, impeding firms' investment in long-term innovative projects.



## Anomalies

- [Crowdsourced employer reviews and stock returns](../notes/green_2019_jfe.html)
- [Extrapolative beliefs in the cross-section: What can we learn from the crowds?](../notes/Da_2021_jfe.html)
- [Chinese Stock Market Shell Value](../notes/cn_shell.html)
- [Size and Value in China](../notes/cn_ff3.html)
- [Time Series Momentum](../notes/TSM.html)
- [Tracking Retail Investor Activity](../notes/retail.html)
- [Overnight Return Reserval](../notes/overnight.html)
- [Idiosyncratic Volatility](../notes/ivol.html)
- [Volume](../notes/volume.html)
- [ESG](../notes/ESG.html)
- [Loughran, Tim, and Bill McDonald. "Measuring firm complexity." *Journal of Financial and Quantitative Analysis* (2023): 1-28.](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/measuring-firm-complexity/D737FD0A697AF699C5AADD62842ACAB8)
  - Measure firm complexity: use 10-K filing text data. 
    - RHS: 374 pre-defined words related to firm complexity.
    - LHS: use audit fees (adjusted by size and industry) as complexity proxy.
    - Run lasso regression -> identify 50+ words as final firm complexity related set.
    - Complexity = percentage of complexity word set in 10-K filiing corpus length. 
- [Cohen, Lauren, and Dong Lou. "Complicated firms." *Journal of financial economics* 104.2 (2012): 383-400.](https://www.sciencedirect.com/science/article/pii/S0304405X11001899)
  - Complication of a firm is measured by income segment. 
  - The more complicated the firm, the more pronounced the return predictability. In addition, we find that sell-side analysts are subject to these same information processing constraints, as their forecast revisions of easy-to-analyze firms predict their future revisions of more complicated firms.

## Asset Pricing

- [Q-Factor Model](../notes/q-factor.html)
- [Which Beta?](../notes/whichbeta.html)
- [Stambaugh-Yuan Four Factors](../notes/Stambaugh-Yuan-2017.html)
- [P-hacking](../notes/phack.html)
- [Chan, Kam Fong, and Terry Marsh. "Asset pricing on earnings announcement days." *Journal of Financial Economics* 144.3 (2022): 1022-1042.](https://www.sciencedirect.com/science/article/pii/S0304405X21002920)
  - The paper provides evidence that the capital asset pricing model (CAPM) seems to hold on days when influential firms announce earnings, challenging the conventional wisdom that the beta-return relationship is generally flat in the market. The findings have implications for investors, suggesting that strategic trading around earnings announcements could yield significant returns.


## Behavorial Finance

- [Behavioral Finance: an Introduction](../notes/behave.html)
- [Short- and Long-Horizon Behavioral Factors](../notes/DHS-4-factors.html)
- [Nominal Price Ilusion](../notes/nominal_illusion.html)
- [PEAD](../notes/PEAD.html)
- [Financial Statement Related](../notes/fin_stat.html)
- Wolfe Research | Seeking alpha from insider transactions
  - Form 4 fillings from EDGAR database
  - Findings:
    - Insider purchases are more effective than sales (might be personal liquidity needs)
    - Insider purchases after positive earnings surprise is a strong confirmatory signal
    - Collective insider purchases by multiple executives is strong
    - Infrequent insider transactions are more informative than reoccurring trades. 


## Crypto

* [Decentralized mining in centralized pools](../notes/defi_RFS.html)
* [Majority is not enough: Bitcoin mining is vulnerable](../notes/ES_2014_majority.html)
* [Blockchain without waste: Proof-of-stake](../notes/PoS.html)
* [A Survey of Attacks on Ethereum Smart Contracts](../notes/SoK.html)
* [Multi-factor in Cryptocurrency](../notes/FF3_cryoto.html)
* [Kogan, Shimon, et al. "Are cryptos different? evidence from retail trading." *Journal of Financial Economics* 159 (2024): 103897.](https://www.sciencedirect.com/science/article/pii/S0304405X2400120X)
  * While investors exhibit contrarian behavior in stocks and gold, they follow a momentum-like strategy with cryptocurrencies, holding onto their investments even after large price movements.
  * Retail investors may view cryptocurrency price changes as indicators of the likelihood of future widespread adoption, leading them to update their price expectations in the direction of the price change.


## Event

- [Lottery-like Stocks](../notes/miscell.html)
- [Bargeron, Leonce, and Alice Bonaime. "Why do firms disagree with short sellers? Managerial myopia versus private information." *Journal of Financial and Quantitative Analysis* 55.8 (2020): 2431-2465.](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/why-do-firms-disagree-with-short-sellers-managerial-myopia-versus-private-information/4CF658C5427FB1B762F47DEF17D2BBA6)
  - **Disagreement Definition**: The paper defines disagreement as situations where firms engage in significant share repurchases while short interest increases.
  - The authors explore whether such repurchases are driven by managerial myopia (an attempt to defend inflated stock prices for short-term gains) or by private information (managers possessing positive, value-relevant information that the market is not yet aware of).
  - The paper finds that repurchases are more likely motivated by managers' private information rather than agency issues or a defense of overvalued stock.
- [Boudoukh, Jacob, et al. "Information, trading, and volatility: Evidence from firm-specific news." *The Review of Financial Studies* 32.3 (2019): 992-1033.](https://academic.oup.com/rfs/article-abstract/32/3/992/5061375)
  - Identified news (relevant to firm events) explains approximately 20%-40% of overnight volatility and 6% during trading hours



## Linkage

* [Geographic Lead-Lag Effects](../notes/Parsons_2020_rfs.html)

* [Technological Links and Predictable Returns](../notes/Lee_2019_jfe.html)

* [Shared Analyst Coverage: Unifying Momentum Spillover Effects](../notes/Ali_2020_jfe.html)

* [Lazy Prices](../notes/lazy-prices.html)

* Market data linkage
  * [Sarmento, Simão Moraes, and Nuno Horta. "Enhancing a pairs trading strategy with the application of machine learning." *Expert Systems with Applications* 158 (2020): 113490.](https://github.com/simaomsarmento/PairsTrading/blob/master/Thesis.pdf)
    * Stock mktdata -> dimension reduction -> clustering -> within each cluster: 
      * The pair’s constituents are cointegrated. 
      * The pair’s spread Hurst exponent reveals a mean-reverting character. ($$H < 0.5$$)
      * The pair’s spread diverges and converges within convenient periods. (1 < half life < 12)
      * The pair’s spread reverts to the mean with enough frequency. (yearly mean-cross >= 12)

* [Co-trade Network](../notes/co-trade.html)

* [Papenkov, Maksim, et al. "Multi-Industry Simplex: A Probabilistic Extension of GICS." *arXiv preprint arXiv:2310.04280* (2023).](https://arxiv.org/pdf/2310.04280.pdf)
  * Multi-industry classification using business description (10K + broker report + earnings call) + Bag of Words + LDA

* [Bagnara, Matteo, and Milad Goodarzi. "Clustering-based sector investing." (2023).](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4528879_code1661302.pdf?abstractid=4528879&mirid=1)
  
  * Data: 94 firm characteristics for CRSP from Dacheng Xiu's Paper (Empirical Asset Pricing with Machine Learning)
  * Bisecting K-means clustering
  * Clustering feature importance: rank feature variation/PCA on cluster-centroid vector
  
* [TT Shi et al. (2023) Production Complementarity and Information Transmission Across Industries](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4190096)

  * Sales segment + industry input-output relation to construct linkage (Benchmark Input-Output Surveys of the Bureau of Economic Analysis to identify product complementary relationships)

    ![](..\notes\pic\BEA-IO.png)

- Linkage and information discreteness: 

  - [Da, Zhi, Umit G. Gurun, and Mitch Warachka. "Frog in the pan: Continuous information and momentum." *The review of financial studies* 27, no. 7 (2014): 2171-2218.](https://academic.oup.com/rfs/article-abstract/27/7/2171/1578455)

  - [Huang, Shiyang, et al. "A frog in every pan: Information discreteness and the lead-lag returns puzzle." *Journal of Financial Economics* 145.2 (2022): 83-102.](https://www.sciencedirect.com/science/article/pii/S0304405X21004761)

  - 行为金融学中的温水煮青蛙：人的这种缺陷叫做limited attention（有限注意力）。由于人们的认知资源是有限的，在任何给定的时刻，我们的大脑都偏好去处理那些最显著、最重要的信息，而忽视那些不显著的、经济效应微弱的因素。一系列频繁但微小的变化对于人的吸引力远不如少数却显著的变化；因此投资者对于连续信息造成的股价变化反应不足。
  
  - 信息离散性（information discreteness，ID）：ID 低（说明信息连续性强）的动量才是高质量动量
  
  $$
  ID = \text{sign(过去一段时间的收益率) × (这段时间内下跌交易日\% - 这段时间内上涨收益日\%)}
  $$
  
  - Da et al. (2014) 说明，与传统动量相比，通过 ID 因子筛选找到的高质量动量能够获得更高的超额收益，且该收益在样本外的持续性更强（这有助于我们降低调仓频率、减少换手率、节约交易成本）。
  
  - Information discreteness (ID) serves as a cognitive trigger that reduces investor inattention and improves inter-firm news transmission.

- [Yan, Jingda, and Jialin Yu. "Cross-stock momentum and factor momentum." *Journal of Financial Economics* 150.2 (2023): 103716.](https://www.sciencedirect.com/science/article/pii/S0304405X23001563)

  - **Cross-stock momentum:** Based on asymmetry in lead-lag linkages and differences between long-run and short-run co-movements.
  - **Factor momentum:** The phenomenon where returns of certain factors (like size, value, or industry factors) exhibit momentum.
  - The asymmetry in cross-stock linkages is a key differentiator from factor momentum. The paper shows that cross-stock momentum is not entirely driven by factor momentum.

- [Chen, Xin, et al. "Attention spillover in asset pricing." *The Journal of Finance* 78.6 (2023): 3515-3559.](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.13281)

  - The paper leverages a unique feature of stock display on trading platforms in China, where the order of stock display is determined by the stock's listing code. This feature creates an attention spillover effect, where investors are more likely to notice and trade stocks with listing codes adjacent to those of stocks they currently hold.
  - The authors propose that overconfident investors, following positive investment experiences, are likely to increase their trading activities and are more likely to direct their attention to neighboring stocks on the display.

- [Jin, Zuben. "Business aspects in focus, investor underreaction and return predictability." *Journal of Corporate Finance* 84 (2024): 102525.](https://www.sciencedirect.com/science/article/pii/S0929119923001748)

  - Conference call transcripts -> topic model -> firm similarity -> linkage signals
- [Feng, Jian, et al. "Economic Links from Bonds and Cross-Stock Return Predictability." *Available at SSRN 4047776* (2022).](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4047776)
  - **Main idea: linkage from bond market credit-rating comovements.**
  - This study identifies a "market segmentation" effect between the equity and bond markets, showing that information from bond markets is often not incorporated promptly by equity market investors.
  - Firms are connected through "credit-rating comovements," defined as instances when two firms' bond ratings are updated in the same direction within a ±10-day window. 

- [Chen, Xin, and Huaixin Wang. "News Links and Predictable Returns." *Available at SSRN 4458612* (2023).](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4458612)
  - **Main idea: news-implied linkages in China where firms are connected based on shared media coverage.**
  - News-based links were established by identifying instances where two firms were mentioned in the same article within a 12-month window. 
  - The authors perform robustness checks to validate these results, including a placebo test using shared media platforms, demonstrating that only specific news stories—not general media coverage—predict future returns. 
  - They explore linkage complexity, showing stronger predictability when linkages are more complex (e.g., higher numbers of shared stories or connections).

- [Wang, Huaixin. "The Day and Night Tale of Momentum Spillover Effects." *Available at SSRN 4179413* (2022).](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4262645)
  - **Main idea: high overnight returns for peer stocks predict elevated opening prices for focal stocks, followed by intraday reversals, while peer intraday returns consistently predict positive future intraday returns for focal stocks.**
  - Retail investors, who trade primarily on overnight information due to news salience, and professional investors, who engage in intraday trading, correcting the market.
  - Predictable patterns arise not only from underreaction but from a systematic interplay between the different investor types. Retail-driven overnight price distortions are followed by intraday reversals managed by professionals


## Machine Learning

* [Out of Sample Predictability](../notes/OOS.html)
* [Quant Machine Learning](../notes/quant_ml.html)
* [Time Seris Machine Learning](../notes/mlts.html)
* [NLP in Finance](../notes/nlp_fin.html)
* [Remlinger, Carl, et al. "Expert aggregation for financial forecasting." *arXiv preprint arXiv:2111.15365* (2021).](https://arxiv.org/pdf/2111.15365.pdf)
* [Liu, Quan, et al. "PREDICTION OF EARNING SURPRISE USING DEEP LEARNING TECHNIQUE."](https://assets.bbhub.io/professional/sites/10/earning_surprise_prediction_china.pdf)
* [Cong, Lin William, Tengyuan Liang, and Xiao Zhang. "Textual factors: A scalable, interpretable, and data-driven approach to analyzing unstructured information." (2019).](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3307057)
  * **Textual Factor (TF) Generation**: The authors generate TFs through three main steps:
    - Representing text using vector word embedding (Word2Vec).
    - Clustering these vectors using Locality-Sensitive Hashing (LSH) to identify topics.
    - Applying topic modeling to identify interpretable textual factors. (Use topic exposure as latent factors, apply standard factor analysis framework)

## Macro

- [He, Wei, Zhiwei Su, and Jianfeng Yu. "Macroeconomic perceptions, financial constraints, and anomalies." *Journal of Financial Economics* 162 (2024): 103952.](https://www.sciencedirect.com/science/article/pii/S0304405X24001752)

  - [石川：主观宏观经济感知、财务约束和股票收益](https://mp.weixin.qq.com/s/4xnEeeYvEOw68pPdzSXuYg)

  ![](../notes/pic/macro_perception_1.png)

  ![](../notes/pic/macro_perception_2.png)

  - 当主观预期上调的时候，财务约束更大的公司未来的预期收益率更低。当主观预期下调的时候，财务约束更大的公司未来的预期收益率更高。
  - Factor timing

## Microstructure

* [Realized Variance and Market Microstructure Noise](../notes/realized_var.html)
* [Order Imbalance with Trade Flow Decomposition](../notes/COI_flow_decomp.html)

## Miscellaneous

- Information Aggregation
  - [更有效的信息聚合方法?](https://zhuanlan.zhihu.com/p/529605892)
  - [Light, Nathaniel, Denys Maslov, and Oleg Rytchkov. "Aggregation of information about the cross section of stock returns: A latent variable approach." *The Review of Financial Studies* 30, no. 4 (2017): 1339-1381.](https://academic.oup.com/rfs/article-abstract/30/4/1339/2756101)

- Missing Financial Data
  - [Missing Financial Data](https://zhuanlan.zhihu.com/p/517848480)
  - [Bryzgalov, S., S. Lerner, M. Lettau, and M. Pelger (2022). Missing financial data. Working paper.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4106794)

- Interest Rate
  - [van Binsbergen, Jules H. Liang Ma, and Michael  Schwert. "The Factor Multiverse: The Role of Interest Rates in Factor Discovery." *SSRN Working Paper* (2022).](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4231626)
  - [当利率不再下降，异象还成其为异象吗？](https://mp.weixin.qq.com/s/ymE-bTz4aWgVOA6Qz5Vyow)


- Information Search

  - [Xu, Yongxin, Yuhao Xuan, and Gaoping Zheng. "Internet searching and stock price crash risk: Evidence from a quasi-natural experiment." *Journal of Financial Economics* 141, no. 1 (2021): 255-275.](https://www.sciencedirect.com/science/article/pii/S0304405X21000933)

  - [【JFE论文速递】网络搜索和股票价格崩盘风险:准自然实验的证据](https://mp.weixin.qq.com/s/aP_RwZzJNNuc35Gw-YDvLQ)
- Fund Research

  - [抄基金作业可以随随便便成功吗？](https://zhuanlan.zhihu.com/p/582989958)
  - [Cao, Sean Shun, Kai Du, Baozhong Yang, and Alan Zhang. (JAR 2021) Copycat skills and disclosure costs: Evidence from peer companies’ digital footprints.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3280744)
- [George, Thomas J., Chuan-Yang Hwang, and Yuan Li. "February, Share Turnover, and Momentum in China." *Available at SSRN 4541025* (2023).](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4541025)

  - A strong Seasonal February reversal exists. The reversal is associated with a spike in turnover for recent loser stocks, which we attribute to an appetite for lottery-like stocks by retail investors around the Chinese New Year season.
  - Excluding February, there is a strong mid-to-long term momentum signal in China stock market.
  - Momentum construction: at beginning of month T+1, calculate signal as closing price at the end of month T-1 divide by the highest price in the past 52 weeks. Skip one month due to strong short-term reversal in China.
- [Du, Qianqian, et al. "Concept links and return momentum." *Journal of Banking & Finance* 134 (2022): 106329.](https://www.sciencedirect.com/science/article/pii/S0378426621002806)

  - China theme/concept linkage.
- [Brogaard, Jonathan, et al. "What moves stock prices? The roles of news, noise, and information." *The Review of Financial Studies* 35.9 (2022): 4341-4386.](https://academic.oup.com/rfs/article-abstract/35/9/4341/6493385)

  - **Main idea: This study introduces a decomposition model to quantify these effects, aiming to clarify the contributions of each component to stock price movements.**
  - The authors develop a return variance decomposition model that categorizes stock price variance into four components:
    - **Noise**: Non-informational price movements due to liquidity issues, overreaction, and other trading frictions.
    - **Private Firm-Specific Information**: Informed trading that reveals proprietary insights about a firm.
    - **Public Firm-Specific Information**: Information from publicly available sources, such as news and announcements.
    - **Market-Wide Information**: Broad economic or market news that impacts all firms.



## Momentum and Factor Timing

- [Momentum](../notes/moment.html)
- [Regime Modeling](../notes/regime.html)
- [Factor Timing](../notes/timing.html)
- Structural Breaks: Advances in Financial Machine Learning Chapter 17
  - **CUSUM tests**: These test whether the cumulative forecasting errors significantly deviate from white noise.
  - **Explosiveness tests:** Beyond deviation from white noise, these test whether the process exhibits exponential growth or collapse, as this is inconsistent with a random walk or stationary process, and it is unsustainable in the long run.
  - **Right-tail unit-root tests:** These tests evaluate the presence of exponential growth or collapse, while assuming an autoregressive specification.
  - **Sub/super-martingale tests:** These tests evaluate the presence of exponential growth or collapse under a variety of functional forms.
- A tug of war
  - [Lou, Dong, Christopher Polk, and Spyros Skouras. "A tug of war: Overnight versus intraday expected returns." *Journal of Financial Economics* 134.1 (2019): 192-213.](https://www.sciencedirect.com/science/article/pii/S0304405X19300650)
  - [Lou, Dong, Christopher Polk, and Spyros Skouras. "The day destroys the night, night extends the day: A clientele perspective on equity premium variation." *London School of Economics Working Paper* (2022).](https://www.carloalberto.org/wp-content/uploads/2023/01/Day-Destroys-The-Night-Night-Extends-The-Day.pdf)
  - **Main idea: overnight momentum and intraday reversal.**
  - High overnight returns tend to continue overnight in future months but exhibit a reversal during the intraday period, suggesting a “tug of war” effect. 
  - Clientele Hypothesis: The study attributes these effects to different types of investors. This segmentation results in a predictable pattern where:
    - Retail Investors drive demand at the open, impacting overnight returns.
    - Institutional Investors provide liquidity intraday, which causes reversal effects.
  - The study reveals a robust negative relation between past overnight returns and future intraday returns, a pattern they describe as "the day destroys the night." Conversely, intraday returns positively forecast overnight returns ("night extends the day"), reflecting a continuation effect. 
- [Jiang, Jingwen, Bryan Kelly, and Dacheng Xiu. "(Re‐) Imag (in) ing price trends." *The Journal of Finance* 78.6 (2023): 3193-3249.](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.13268)
  - **CNN on OCHL charts**: open, close, high, and low prices, trading volume, and moving average price over the past 5, 20, and 60 days to forecast short (five-day), medium (20-day), and long (60-day) horizons return.
  - **Transfer learning**: they show that the predictive patterns identified by the CNN from daily U.S. stock data transfer well to international markets and to other time scales. 

- [Han, Yufeng, Guofu Zhou, and Yingzi Zhu. "A trend factor: Any economic gains from using information over investment horizons?." *Journal of Financial Economics* 122.2 (2016): 352-375.](https://www.sciencedirect.com/science/article/pii/S0304405X16301271)
  - Construct various lag lengths moving average to cover different time horizons, ranging from short-term (3–20 days) to long-term (up to 1000 days).
  - Each month, the expected return for each stock is predicted using a cross-sectional regression of returns on the normalized MA signals.
  - Then use the estimated coefficients for next month return prediction.

## NLP

- Wolfe Research | Text mining unstructured corporate filing data
  - EDGAR 10-K and 10-Q filings (by section comparison)
  - Features:
    - Sentiment and tone analysis
    - chanes in sentiment
    - distance measures (YoY embedding/BoW)


## Portfolio Construction

- [Risk Parity](../notes/risk_parity.html)

## General Knowledge

- [The Element of Financial Econometrics](../notes/Fin_Fan_Book.html)