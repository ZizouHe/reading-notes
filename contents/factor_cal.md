# Momentum

- Information Discreteness (ID)

  - [Da, Zhi, Umit G. Gurun, and Mitch Warachka. "Frog in the pan: Continuous information and momentum." *The review of financial studies* 27.7 (2014): 2171-2218.](https://www3.nd.edu/~zda/Frog.pdf)

  - Definition
    $$
    ID = \mathrm{sign} (PRET) \times (\%\mathrm{neg} - \% \mathrm{pos})
    $$
    where PRET is 12-1 month cumulative return, %neg and %pos are negative (positive) daily return percentage within the same period. Smaller ID value gives more positive return in the future.

  - Theory: frequent arrival of small signals draws less attention compared to infrequent but big signals. The former has underreaction and the latter has overreaction.

- Capital Gains Overhang (CGO) 

  - [Wang, Huijun, Jinghua Yan, and Jianfeng Yu. "Reference-dependent preferences and the risk–return trade-off." *Journal of Financial Economics* 123.2 (2017): 395-414.](https://www.sciencedirect.com/science/article/pii/S0304405X16301787)

  - Definition
    $$
    \begin{gathered}
    R P_t=\frac{1}{k} \sum_{n=1}^T\left(V_{t-n} \prod_{\tau=1}^{n-1}\left(1-V_{t-n+\tau}\right)\right) P_{t-n} \\
    C G O_t=\frac{P_{t-1}-R P_l}{P_{t-1}}
    \end{gathered}
    $$
    where  $$V_t$$ is week-t turnover rate (volume / outShs), $$P_t$$ is week-t close price. $$RP_t$$ is reference price. Higher CGO has higher return.

  - Theory: Prospect Theory suggests that investors are risk-seeking in the loss domain and risk-averse in the gain domain relative to a reference point. Using Capital Gains Overhang (CGO) as a proxy for investors’ unrealized gains or losses, the authors find:

    - Positive risk–return relation among stocks with high CGO (i.e., investors have unrealized gains).
    - Negative risk–return relation among stocks with low CGO (i.e., investors have unrealized losses).
    - When investors are holding stocks at a loss (low CGO), they may prefer high-risk stocks, driving down prices and expected returns.
    - When investors are in a gain position (high CGO), they behave more traditionally (risk-averse), and high-risk stocks yield higher expected returns.

  - Thoughts: better to use CGO x risk proxy (TRISK / SRISK / Beta / etc) interaction.

- Acceleration Momentum

  - [Investor Attention, Visual Price Pattern, and Momentum Investing](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2292895)

  - Definition
    $$
    P_{i, t}=\alpha+\beta t+\gamma t^2
    $$
    where $$P_{i,t}$$ is stock-i price at day-t, t=[1, ..., n] is the past 1, ..., n days. Run a regression over the past t days and obtain $$\gamma$$ as acceleration momentum. 

  -  Trade acceleration momentum $$\gamma$$ or $$\widehat{P}$$.

  - Theory: acceleration draw investor attention and create overreaction. 

- Return Seasonality

  - [Heston, Steven L., and Ronnie Sadka. "Seasonality in the cross-section of stock returns." *Journal of Financial Economics* 87.2 (2008): 418-445.](https://www.sciencedirect.com/science/article/pii/S0304405X0700195X)
  - Definition: past N year same month average return can be used to predict stock performance in the current month (cross-sectionally).

- Rank Momentum

  - Definition: each day take normalized (0-1) ascending rank of daily return. Each month take average, then take average within each lookback period.

- PEAD

  - Definition: 3-day cumulative mret after earnings anouncement. 

- 振幅切割动量

  - 开源金工 | A股市场如何构造动量因子
  - Definition: 以 160 个交易日作为窗口期，将振幅较低的 $$\lambda \%$$ 个交易日的涨跌幅加总，得到动量因子，$$\lambda \%$$ 取值范围在 $$[50 \%, 70 \%]$$ 。
  - Theory: 低振幅水平下涨跌幅因子呈现动量效应，高振幅水平下涨跌幅因子呈现反转效应，并且动量效应和反转效应的分布和强度具有不对称性。
  - Thoughts: filter using risk model risk * multiplier

- Fundamental Implied Return

  - [Huang, Dashan, Huacheng Zhang, and Guofu Zhou. "Twin momentum: Fundamental trends matter." (2017): 1.](https://ink.library.smu.edu.sg/lkcsb_research/5157/)

  - Definition: L-quarter moving average on some fundamental factors (EPS, ROE, ROA, APE, CPA, GPA, Payout ratio)

    $$
    M A_{i, t, L}^k=\frac{F_{i, t}+F_{i, t-1}+\cdots+F_{i, t-L+1}}{L}
    $$


    Run regression on the next month return:

    $$
    R_{i, t}=\alpha_t+\sum_{k=1}^K \sum_{L=1,2,4,8} \beta_{L, t}^k M A_{i, t-1, L}^k+\varepsilon_{i, t}
    $$
    Conduct prediction based on most recent fundamental factor MA and estimated coef
    $$
    \mathrm{FIR}_{i, t}=\sum_{k=1}^K \sum_{L=1,2,4,8} \beta_{L, t}^k M A_{i, t, L}^k
    $$

  - Theory: fundamental factor momentum.

- Financial Linkage

  - Use some accouting / financial factors to construct linkage.
  - Thoughts: Barra linkage.

- Time Series Momentum

  - [Moskowitz, Tobias J., Yao Hua Ooi, and Lasse Heje Pedersen. "Time series momentum." *Journal of financial economics* 104.2 (2012): 228-250.](https://www.sciencedirect.com/science/article/pii/S0304405X11002613)

  - Definition: 
    $$
    \mathrm{T S M O M}_{t i}=\operatorname{sign}\left(\frac{1}{N} \sum_{j=1}^{12} \hat{r}_{t-j, i}\right) \frac{1}{\widehat{\sigma}_{m, i}}
    $$
    where $$\widehat{\sigma}_{m, i}$$ is the EMA monthly volatility and $$\hat{r}_{t-j, i}$$ is the monthly excessive return (monthly return subtract EMA mean of monthly return)

  - Thoughts: using risk/realized volatility to adjust momentum.

# Technical Indicator

- Rate of Change

  - Definition
    $$
    \mathrm{ROC} = \frac{\mathrm{Close}_t - \mathrm{Close}_{t-N}}{\mathrm{Close}_{t-N}}
    $$

    $$
    \mathrm{MAROC} = \mathrm{MA}(\mathrm{ROC}, M), \; \; \mathrm{EMAROC} = \mathrm{EMA}(\mathrm{ROC}, M)
    $$

  - 趋势明显的⾏情中，当 ROC 向下跌破零，卖出信号，ROC 向上突破零，买⼊信号；震荡⾏情中，当 ROC 向下跌破 MAROC/EMAROC 时，卖出信号，当 ROC 上穿 MAROC/EMAROC 时，买⼊信号。

- ADTM

  - Definition

    ```{python}
    N = 23
    M = 8
    
    DTM = 0 if open < open_yesterday else max( high - open, open - open_yesterday)
    DBM = 0 if open > open_yesterday else max( open - low, open - open_yesterday)
    STM = sum(DTM, N)
    SDM = sum(DBM, N)
    ADTM = (STM - SBM) / STM if STM > SBM else (STM - SBM) / SBM
    ADTMMA = sum(ADTM, M)
    ```

  - Theory: ADTM指标在+1到-1之间波动。差于-0.5时为低风险区,好于+0.5时为高风险区，需注意风险。ADTM上穿ADTMMA时，购入股票；ADTM跌穿ADTMMA时，出售股票。

- DBCD

  - Definition
    $$
    \begin{gathered}
    \mathrm{BIAS}=(\mathrm{CLOSE}-\mathrm{SMA}(\mathrm{CLOSE}, \mathrm{~N} 1)) / \mathrm{SMA}(\mathrm{CLOSE}, \mathrm{~N} 1) \\
    \mathrm{DIF}=\mathrm{BIAS}-\mathrm{BIAS}[\mathrm{~N} 2] \\
    \mathrm{DBCD}=\mathrm{SMA}(\mathrm{DIF}, \mathrm{~N} 3, 1)
    \end{gathered}
    $$
    where N1=5, N2=16, N3=17, and $$[N]$$ is the t-N value if current time is t. 
    $$
    SMA(X, m, n):= Y_t = \frac{n}{m} X + \frac{m-n}{m} Y_{t-1}
    $$

- KDJ

  - Definition

    ```{python}
    N = 9
    M1 = 3
    M2 = 3
    
    RSV = 100 * (close - np.min(low[-N:])) / (np.max(high[-N:]) - np.min(low[-N:])) # highest high and lowest low in the past N days
    K = SMA(RSV, M1, 1)
    D = SMA(RSV, M2, 1)
    J = J = 3*K - 2*D
    ```

  - Theory: 

    - When the K line breaks above the D line on the graph, it is commonly known as the golden cross, which is a signal to buy. 
    - When the K value is diminishing and then breaks below the D line from above, it is commonly called a dead cross and seen as a signal to sell. 
    - When the J value is greater than 90, especially for more than five consecutive days, the stock price will at least form a short-term peak. On the contrary, when the J value is less than 10, especially for several consecutive days, the stock price will at least form a short-term bottom.

  - Thoughts: The main limitation of the KDJ is that it can generate false signals under volatile markets.  We can use idio risk / realized vol / etc. to rescale RSV values for each stock.

- ATR

  - Definition

    ```{python}
    N = 20
    
    TR = max(high-low, abs(high-close_prev), abs(low-close_prev))
    ATR = EMA(TR, N)
    ```

  - Theory: ⽤于表⽰价格的波动程度，价格波动幅度的突破通常也预⽰着价格的突破，该指标价值越⾼，趋势改变的可能性就越⾼；该招标的价億越低，趋势的移动性就越弱。

  - Thoughts: use as indicator.

- Chaikin Volatility

  - Definition

    ```{python}
    N = 10
    M = 10
    
    REM = EMA(high - low, N)
    CV = 100* (REM - REM_{t-M}) / REM_{t-M}
    ```

  - Theory: ⽤于股价的波动情况；⼀个相对较短时间内的波动率上升意味着市场底部的到来，⼀段相对较长时间内波动率的下降意味着市场顶部的来到，可以根据波动率预测股票未来的趋势。

  - Thoughts: use as indicator.

- BBI

  - Definition

    ```{python}
    M1 = 3
    M2 = 6
    M3 = 12
    M4 = 20
    
    BBI = ( MA(close, M1) + MA(close, M2) + MA(close, M3) + MA(close, M4) ) / 4
    ```

- Chaikin Oscillator

  - Definition

    ```{python}
    X = (2*close - high - low) / (high - low)
    ADL = Volume * X
    #ADL = ADL + ADL_prev
    CO = EMA(ADL, 3) - EMA(ADL, 10)
    ```

  - Theory:

    - CO is an improvement of ADL (Accumulation/Distribution Line).
    - Monitor General Money Flow - An ADL's move higher is a signal that buying pressure is starting to prevail. On the flip side, an ADLs downward move signals increased selling pressure is beginning to gain a foothold.
    - Confirmation - You can also use the ADL to confirm the strength, and possibly the longevity, of a current move.

- Mass Index

  - Definition:
    $$
    \text { Mass Index }= \frac{\text { EMA(High - Low, 9)}}{\text{EMA((EMA(High - Low, 9), 9) }}
    $$

  - Theory: surges in the mass index can correlate with turning points in the price trend.

  - Thoughts: use as indicator.

- PSY

  - Definition
    $$
    \text { PSY } = \frac{100 * \operatorname{COUNT}\left(\operatorname{CLOSE}_t > \operatorname{CLOSE}_{t-1}, N\right)}{N}
    $$
    where N = 12.

  - Theory: PSY 将⼀定时期内投资者趋向买⽅或卖⽅的⼼理事实转化为数值，形成⼈⽓指数，从⽽判断股价的未来趋势；通常，指标⼩于25时关注做多机会，⼤于75时关注做空机会，⼩于10为极度超卖，⼤于90为圾度超买，市场宽幅振荡时，PSY 也会25~75区间反复與破，给出⽆效信号。

    

    

    

  