# Volume

## Expected return, volume, and mispricing

- [Han, Yufeng, Dashan Huang, Dayong Huang and Guofu Zhou, 2022, Expected return, volume, and mispricing, Journal of Financial Economics 143(3), 1295-1315.](https://www.sciencedirect.com/science/article/pii/S0304405X21001963)
- [Atmaz, Adem, and Suleyman Basak. "Belief dispersion in the stock market." *The Journal of Finance* 73, no. 3 (2018): 1225-1279.](https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.12618)

- [预期收益、交易量和错误定价](https://zhuanlan.zhihu.com/p/526639807)

- 结论：预期收益与低估股票的交易量正相关，与高估股票的交易量负相关。因此，交易量放大了错误定价。交易量会影响股票收益，因其与投资者分歧、波动性、流动性、投资者注意力、私人信息等都相关。

- 用 [Stambaugh et al. (2015)](./IdioVol.html) 的错误定价指标(MISP)和1965年7月-2019年12月的交易量数据，进行双重分组，构建5*5投资组合。研究发现，在低估股票中，FF五因子月度alpha随交易量单调递增。而在高估股票中，FF五因子的月度alpha随交易量单调递减。并且低减高(underpriced-minus- overpriced, UMO)投资组合的FF五因子月度alpha在低交易量股票中为0.26%，在高交易量股票中为1.18%，两者差值称为交易量的放大效应，相当于每月0.93%(t值为4.24)。这些结果表明，错误定价影响交易量与收益率之间的关系，并且这种影响集中在高交易量的股票组合中。

- 交易量不同于现有对错误定价有放大效应的其他变量。控制特质波动率(IVOL)、规模、非流动性、机构所有权、偏度和相对浮盈(capital gain overhang)后，交易量的放大效应仍然显著。

- **对于以上现象的解释**：

  - 投资者分歧
    - A trade, in general, is driven by one of the three motives: liquidity needs, private information, and disagreement due to speculation/overconfidence.
    - Trading volume is positively associated with two **economically clean disagreement measures**, analysts’ return forecast dispersion and earnings forecast dispersion.
    - Measure return (earnings) forecast dispersion as the cross-sectional standard deviation of analysts’ return (earnings) forecasts.
    - **Trading volume is a reasonable disagreement measure**, and lends direct support to [Atmaz and Basak (2018)](https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.12618) that **investor disagreement has an amplification effect on investor expectation bias.**

  - 投资者预期偏差
    - Expectation bias in the cross section [Atmaz and Basak (2018)](https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.12618): defined as realized earnings minus the median of analyst forecasts divided by stock price
    - Among the underpriced stocks that are more likely to have experienced negative news, the expectation biases are more likely to be dominated by pessimistic investors. As a result, the ex post analyst forecast errors are expected to be positive, and the higher the trading volume/investor disagreement, the more positive the forecast errors (i.e., the more negative the expectation biases). Similarly, among the overpriced stocks, we expect that the higher the trading volume, the more negative the forecast errors (i.e., the more positive the expectation biases).
    - Expectation bias in time series [Atmaz and Basak (2018)](https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.12618): overpricing is concentrated in high sentiment periods.