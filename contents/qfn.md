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

## Analyst

- Analyst Forecast Bundling Intensity and Earnings Surprise

  - [Barth, Mary E., et al. "Analyst Forecast Bundling Intensity and Earnings Surprise." *Available at SSRN 4839739* (2024).](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4839739)

  - The authors explore how financial analysts convey information about a company's earnings without necessarily making full revisions to their earnings forecasts. They achieve this by increasing what they term 'bundling intensity,' which refers to the extent to which an analyst's report that includes an earnings forecast revision also includes revisions to price targets and/or recommendations that have the same direction as the earnings forecast revision.

  - The researchers have developed a measure called BF_Score at the firm level to quantify bundling intensity. Their findings suggest that BF_Score is a significant predictor of earnings surprises based on analyst forecasts. These surprises often result from biases in consensus earnings forecasts, which are influenced by the information analysts communicate through bundling intensity. Below is definition of BR score, where TP is target price.

    ![](../notes/pic/br_score.png)

  - The use of bundling and the predictive power of BF_Score increase during times of higher macroeconomic uncertainty, when analysts have greater incentives to avoid bold revisions to their earnings forecasts. 

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

## Asset Pricing

- [Q-Factor Model](../notes/q-factor.html)
- [Which Beta?](../notes/whichbeta.html)
- [Stambaugh-Yuan Four Factors](../notes/Stambaugh-Yuan-2017.html)
- [P-hacking](../notes/phack.html)

## Behavorial Finance

- [Behavioral Finance: an Introduction](../notes/behave.html)
- [Short- and Long-Horizon Behavioral Factors](../notes/DHS-4-factors.html)
- [Nominal Price Ilusion](../notes/nominal_illusion.html)
- [PEAD](../notes/PEAD.html)
- [Financial Statement Related](../notes/fin_stat.html)

## Crypto

* [Decentralized mining in centralized pools](../notes/defi_RFS.html)
* [Majority is not enough: Bitcoin mining is vulnerable](../notes/ES_2014_majority.html)
* [Blockchain without waste: Proof-of-stake](../notes/PoS.html)
* [A Survey of Attacks on Ethereum Smart Contracts](../notes/SoK.html)
* [Multi-factor in Cryptocurrency](../notes/FF3_cryoto.html)

## Event

- [Lottery-like Stocks](../notes/miscell.html)

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

## Machine Learning

* [Out of Sample Predictability](../notes/OOS.html)
* [Quant Machine Learning](../notes/quant_ml.html)
* [Time Seris Machine Learning](../notes/mlts.html)
* [NLP in Finance](../notes/nlp_fin.html)
* [Remlinger, Carl, et al. "Expert aggregation for financial forecasting." *arXiv preprint arXiv:2111.15365* (2021).](https://arxiv.org/pdf/2111.15365.pdf)
* [Liu, Quan, et al. "PREDICTION OF EARNING SURPRISE USING DEEP LEARNING TECHNIQUE."](https://assets.bbhub.io/professional/sites/10/earning_surprise_prediction_china.pdf)

## Microstructure

* [Realized Variance and Market Microstructure Noise](../notes/realized_var.html)
* [Order Imbalance with Trade Flow Decomposition](../notes/COI_flow_decomp.html)

## Miscellaneous

- [Factor Timing](../notes/timing.html)
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
    

## Momentum and Factor Timing

- [Momentum](../notes/moment.html)
- [Regime Modeling](../notes/regime.html)
- Structural Breaks: Advances in Financial Machine Learning Chapter 17
  - **CUSUM tests**: These test whether the cumulative forecasting errors significantly deviate from white noise.
  - **Explosiveness tests:** Beyond deviation from white noise, these test whether the process exhibits exponential growth or collapse, as this is inconsistent with a random walk or stationary process, and it is unsustainable in the long run.
  - **Right-tail unit-root tests:** These tests evaluate the presence of exponential growth or collapse, while assuming an autoregressive specification.
  - **Sub/super-martingale tests:** These tests evaluate the presence of exponential growth or collapse under a variety of functional forms.

## Portfolio Construction

- [Risk Parity](../notes/risk_parity.html)

## General Knowledge

- [The Element of Financial Econometrics](../notes/Fin_Fan_Book.html)