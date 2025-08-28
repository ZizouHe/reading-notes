[Code example](../assets/gpt_gen.py)

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

    


# High Frequency

- 每笔成交量差分标准差
  $$
  \begin{aligned}
  &\operatorname{diff}_i=\operatorname{volb}_i-\operatorname{volb}_{i-1}\\
  &\operatorname{diff-mean}_{\text {day }}=\operatorname{mean}\left(a b s\left(\frac{\operatorname{diff}_i}{\operatorname{mean}\left(\left\{\operatorname{volb}_i\right\}\right)}\right)\right.\\
  &\text { diff-std }_{\text {volb }}=\text { mean }\left(\left\{\text { diff-std }_{\text {day }}\right\}\right)
  \end{aligned}
  $$
  其中$$v o l b_i$$ 为个股日内 240 根 1 分钟 K 线的每笔成交量（成交量／成交笔数），diff_stdday取过去 20 个交易日数据。

  ```python
  def compute_diff_std_volb(
      da: xr.DataArray,
      half_life: int=20,
  ):
      for v in ("locVol","numTrade"):
          if v not in da.coords["V1"].values:
              raise ValueError(f"Missing required variable '{v}' in V1")
  
      v_locVol = da.sel(V1="locVol")
      v_numTr  = da.sel(V1="numTrade")
  
      volb = divide_safe(v_locVol, v_numTr)
  
      diff_raw = volb.diff(dim="E", label="upper")
      diff_full = diff_raw.reindex(E=volb["E"])
      day_mean_volb = volb.mean("E", skipna=True)
      day_mean_volb_b = day_mean_volb.broadcast_like(volb)
      norm_abs_diff = (diff_full.abs() / day_mean_volb_b).astype("float64")
      diff_std_day = norm_abs_diff.std("E", skipna=True)
      #diff_std_day = norm_abs_diff.mean("E", skipna=True)
      #fac_trailing = diff_std_day.rolling(D=half_life, min_periods=1).mean().isel(D=[-1])
      fac_trailing = _ewm_ma_halflife(diff_std_day, dim="D", half_life=half_life).isel(D=[-1])
      f_b = fac_trailing.broadcast_like(volb.D=[-1])
      out = xr.concat([f_b], dim="V1").assign_coords(V1=["factor_diff_std_volb"])
      out = out.transpose("S","D","E","V1")
      return out
  ```

  

- 高频上行波动占比
  $$
  \frac{\sum_t\left(r_i^t I_{\left\{r_i^t>0\right\}}\right)^2}{\sum_t\left(r_i^t\right)^2}
  $$

  其中
  （1）$$r_i^l$$ 为分钟频率下的股票收益序列，如 1 分钟、 5 分钟、 10 分钟等；
  （2）在任意选股时刻，因子值为前 N 日指标的均值，如月度选股，计算因子值时使用的是股票过去 20 个交易日的均值。

  股票高频收益的上行波动衡量了股票价格拉升的特征。假设有两只股票在过去一段时间有着相同的涨幅，其中一只股票的涨幅由持续稳定的小幅上涨䍗计带动，而另一只股票的上涨源自于股票短期的大幅拉升，那么后者更有可能在收益上出现反转，而后者在因子值上也会体现出较高的上行波动率。

  ```python
  def compute_hf_upvol_share(
      da: xr.DataArray,
      ret_var: str = "ret",
      half_life: int = 20,
  ) -> xr.DataArray:
      if ret_var not in da.coords["V1"].values:
          raise ValueError(f"Variable '{ret_var}' not found in V1")
  
      ret = da.sel(V1=ret_var)
      num_day = (ret.clip(min=0) ** 2).sum("E", skipna=True)
      den_day = (ret ** 2).sum("E", skipna=True)
      ratio_day = divide_safe(num_day, den_day)
      ratio_ema = _ewm_ma_halflife(ratio_day, dim="D", half_life=half_life)
  
      ratio_last = ratio_ema.isel(D=[-1])
      factor_last = ratio_last.broadcast_like(ret.isel(D=[-1]))
  
      out_list = [factor_last]
  
      out = xr.concat(out_list, dim="V1").assign_coords(V1=["hf_upvol_share"])
      out = out.transpose("S","D","E","V1")
      return -1*out
  ```

  

- 非流动性的变异系数: 股票的非流动性的变异系数较高，说明非流动性的波动较大，对于持有该类股票的投资者来说，未来卖出该类股票有着更高的交易成本不确定性，所以由此能够获得更高的风险溢价。

$$
\begin{aligned}
I L L I Q_{i, t} & =\frac{\left|r_{i, t}\right|}{\text { Amount }_{i, t}} \\
C V I L L I Q_i & =\frac{\sigma\left(I L L I Q_i\right)}{\overline{I L L I Q_i}}
\end{aligned}
$$

其中
（1） Amount $$_{i, t}$$ 为股票 i 在 t 时刻的交易金额；
（2）$$r_{i, t}$$ 是股票 i 在 t 时刻收益率；
（3）时间窗口期为过去 20 个交易日。

```python
def compute_cv_illiq(
    da: xr.DataArray,
    ret_var: str = "ret",
    vol_var: str = "locVol",
    half_life: float = 20,
) -> xr.DataArray:
    for v in (ret_var, vol_var):
        if v not in da.coords["V1"].values:
            raise ValueError(f"Variable '{v}' not found in V1")

    ret  = da.sel(V1=ret_var)
    amount   = da.sel(V1=vol_var)
    amount = close * vol
    illiq_min = divide_safe(ret.abs(), amount)
    illiq_day = illiq_min.mean("E", skipna=True)
    mu_ewm  = _ewm_ma_halflife(illiq_day, dim="D", half_life=half_life, mode='mean')
    std_ewm = _ewm_ma_halflife(illiq_day, dim="D", half_life=half_life, mode='std')
    cv_series = divide_safe(std_ewm, mu_ewm)

    factor_last = cv_series.isel(D=[-1]).broadcast_like(ret.isel(D=[-1]))
    out = xr.concat([factor_last], dim="V1").assign_coords(V1=['cv_illiq'])
    out = out.transpose("S","D","E","V1")
    return out
```

- 成交量波峰计数因子

  1. 计算全部 240 根 $K$ 线数据的均值与标准差，筛选出大于（均值 +1 倍标准差）的分钟数据；

  2. 计算上一步筛选出的每一分钟与前一分钟之间的时间差，只有时间差超过 1 分钟（即相隔超过 1 根 $K$ 线）时，该分钟数据才会被保留；

  3. 经过上述两步筛选后，剩余的数据全部被视作局部峰值，峰值个数即为当日成交量波峰计数因子的取值，而最终调仓日的因子值仍为过去 20 个交易日因子值的均值。

  - 出现日内＂放量＂现象次数更多的股票可能有更多的趋势或知情交易者参与交易，进而在未来一段时间内有更高的收益率，因子与未来收益正相关。

```python
def compute_vol_spike_count(
    da: xr.DataArray,
    vol_var: str = "volume",
    k_std: float = 1.0,
    half_life: float = 10.0,
) -> xr.DataArray:
    if vol_var not in da.coords["V1"].values:
        raise ValueError(f"Variable '{vol_var}' not found in V1")

    vol = da.sel(V1=vol_var)

    day_mean = vol.mean("E", skipna=True)                  # S x D
    day_std  = vol.std("E", skipna=True)                   # S x D
    thr = (day_mean + k_std * day_std).broadcast_like(vol) # S x D x E

    flagged = (vol > thr).fillna(False)                    # bool S x D x E

    prev_flagged = flagged.shift(E=1, fill_value=False)
    keep = flagged & (~prev_flagged)                       # bool S x D x E

    count_day = keep.sum("E").astype("float64")            # S x D
    count_ema = _ewm_ma_halflife(count_day, dim="D", half_life=half_life, mode="mean")  # S x D

    factor_last = count_ema.isel(D=[-1]).broadcast_like(vol.isel(D=[-1]))       # S x 1 x E

    out = xr.concat([factor_last], dim="V1").assign_coords(V1=[vol_spike_count])
    out = out.transpose("S","D","E","V1")
    return out
```

- 价格冲击偏差:

  - MoneyFlow
    $$
    MF_t = \frac{(locVolBuy_t - locVolSell_t)}{locVol_t}
    $$

  - 上涨/下跌用分钟收益 ret 的符号判定：$$I_t=\mathbf{1}_{\{ret_t\ge0\}}$$。

  - 在日内用零截距回归的解析式估计两条斜率：
    $$
    \gamma^{up}=\frac{\sum_{I_t=1} MF_t\cdot ret_t}{\sum_{I_t=1} MF_t^2},\quad \gamma^{down}=\frac{\sum_{I_t=0} MF_t\cdot ret_t}{\sum_{I_t=0} MF_t^2}
    $$
    

    因为两组互斥，等价于回归 $$ret_t=\gamma^{up}(I_t MF_t)+\gamma^{down}((1-I_t)MF_t)$$ 无截距。

  - 日度偏差：
    $$
    \text{bias}_{day}=\frac{\gamma^{up}-\gamma^{down}}{\gamma^{up}+\gamma^{down}}
    $$

  - 再取均值或者EMA

  - 价格冲击偏差主要表征了股票在某一时间区间上涨或者下跌的难易程度，价格冲击偏差较大（正值）的股票，相同比例的主动订单对其股价向下的冲击小于向上的冲击，股票容易上涨，反之，股票容易下跌。

  ```python
  def compute_price_impact_bias(
      da: xr.DataArray,
      ret_var: str = "ret",
      buy_var: str = "locVolBuy",
      sell_var: str = "locVolSell",
      amount_var: str = "locVol",
      half_life: float = 10.0,
  ) -> xr.DataArray:
      for v in (ret_var, "locVolBuy", "locVolSell", "locVol"):
          if v not in da.coords["V1"].values:
              raise ValueError(f"Variable '{v}' not found in V1")
  
      ret   = da.sel(V1=ret_var)
      buy   = da.sel(V1="locVolBuy")
      sell  = da.sel(V1="locVolSell")
      amount = da.sel(V1="locVol")
  
      moneyflow = buy - sell
      mf = divide_safe(moneyflow, amount)
  
      valid = xr.ufuncs.isfinite(mf) & xr.ufuncs.isfinite(ret)
      mf = xr.where(valid, mf, np.nan)
      ret = xr.where(valid, ret, np.nan)
  
      up_mask   = ret >= 0
      down_mask = ~up_mask
  
      mf_up   = xr.where(up_mask, mf, np.nan)
      mf_down = xr.where(down_mask, mf, np.nan)
  
      num_up  = (mf_up * ret).sum("E", skipna=True)          # S x D
      den_up  = (mf_up ** 2).sum("E", skipna=True)           # S x D
      gamma_up = divide_safe(num_up, den_up)                 # S x D
  
      num_dn  = (mf_down * ret).sum("E", skipna=True)
      den_dn  = (mf_down ** 2).sum("E", skipna=True)
      gamma_down = divide_safe(num_dn, den_dn)               # S x D
  
      bias_day = divide_safe(gamma_up - gamma_down, gamma_up + gamma_down)  # S x D
      bias_ema = _ewm_ma_halflife(bias_day, dim="D", half_life=half_life, mode="mean")  # S x D
  
      factor_last = bias_ema.isel(D=[-1]).broadcast_like(ret.isel(D=[-1]))  # S x 1 x E
  
      out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["price_impact_bias"]))
      out = out.transpose("S","D","E","V1")
      return out
  
  ```

- 量价相关性

  - PV＿corr＿std 从价量形态稳定性的角度，对反转因子进行了改进，即无论股票价格过去的涨跌，只要每日价量关系维持某种稳定形态，下个月就更有可能上涨；而价量关系在多种形态间 频繁切换的股票，下个月更有可能下跌。
  - PV＿corr＿avg 利用成交量的信息，修正了传统反转因子对股票价格涨跌的判断，即价格涨跌的反转不完全由价格自己决定，还需看成交量的信息，若有量的确认，则月度行情的反转效应更强；若没有量的确认，则月度行情更容易呈现动量效应。
  -  价量相关性趋势因子: 在跨日维度上，用指数加权的线性回归取斜率

  ```python
  def compute_pv_corr_family(
      da: xr.DataArray,
      price_var: str = "robust",
      vol_var: str = "locVol",
      half_life: float = 10.0,
      mode: str = "avg",   # 'avg' | 'std' | 'trend'
  ) -> xr.DataArray:
      ## todo: mean condi ret
      if mode not in {"avg", "std", "trend"}:
          raise ValueError("mode must be one of {'avg','std','trend'}")
      for v in (price_var, vol_var):
          if v not in da.coords["V1"].values:
              raise ValueError(f"Variable '{v}' not found in V1")
  
      price = da.sel(V1=price_var)  # S x D x E
      vol   = da.sel(V1=vol_var)    # S x D x E
  
      p_mean = price.mean("E", skipna=True)
      v_mean = vol.mean("E",   skipna=True)
      p_dm   = price - p_mean
      v_dm   = vol   - v_mean
      p_std  = price.std("E", skipna=True)
      v_std  = vol.std("E",   skipna=True)
  
      z_p = divide_safe(p_dm, p_std)
      z_v = divide_safe(v_dm, v_std)
      corr_day = (z_p * z_v).mean("E", skipna=True)  # S x D
  
      if mode == "avg":
          fac_series = _ewm_ma_halflife(corr_day, dim="D", half_life=half_life, mode="mean")  # S x D
          out_name = "pv_corr_avg"
  
      elif mode == "std":
          fac_series = -1*_ewm_ma_halflife(corr_day, dim="D", half_life=half_life, mode="std")   # S x D
          out_name = "pv_corr_std"
  
      else:  # mode == 'trend'
          nD = corr_day.sizes["D"]
          ages = xr.DataArray(np.arange(nD)[::-1], dims=["D"], coords={"D": corr_day["D"]}).astype("float64")
          w = (0.5 ** (ages / float(half_life))).astype("float64")   # D
          wB = w.broadcast_like(corr_day)                            # S x D
  
          x = xr.DataArray(np.arange(nD), dims=["D"], coords={"D": corr_day["D"]}).astype("float64")
          xB = x.broadcast_like(corr_day)                            # S x D
  
          wsum = w.sum("D", skipna=True)                             # scalar
          xbar = (w * x).sum("D", skipna=True) / wsum                # scalar
          x_center = xB - xbar                                       # S x D (broadcasted)
  
          y = corr_day                                               # S x D
          ybar = (wB * y).sum("D", skipna=True) / wsum               # S
          y_center = y - ybar.broadcast_like(y)                      # S x D
  
          num = (wB * x_center * y_center).sum("D", skipna=True)     # S
          den = (wB * x_center * x_center).sum("D", skipna=True)     # S
          fac_series = -1*divide_safe(num, den).expand_dims(D=[da["D"].values[-1]])  # S x 1 (treat as a day)
          out_name = "pv_corr_trend"
  
      factor_last = fac_series.isel(D=[-1]).broadcast_like(vol.isel(D=[-1]))  # S x 1 x E
      out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array([out_name]))
      return out.transpose("S","D","E","V1")
  
  ```



- 上下行波动率不对称性: 对每个交易日，把分钟收益平方并分方向累加。最后再取d日平均。
  - RSJ 衡量了上下行波动的不对称性；RSJ 通常有负风险溢价，短期日内的情绪不稳定的大幅上涨往往跟着未来的补跌（RSJ 越大），短期日内情绪不稳定的大幅下跌也往往跟着未来的补涨。

$$
RV_d=\sum r_{d,i}^2,\quad RV^{up}d=\sum r{d,i}^2\mathbf{1}{\{r{d,i}>0\}},\quad RV^{down}d=\sum r{d,i}^2\mathbf{1}{\{r{d,i}<0\}} \\
RSJ_d = \frac{RV^{up}_d - RV^{down}_d}{RV_d}
$$

```python
def compute_rsj_asymmetry(
    da: xr.DataArray,
    ret_var: str = "ret",
    half_life: float = 10.0,
) -> xr.DataArray:
    if ret_var not in da.coords["V1"].values:
        raise ValueError(f"Variable '{ret_var}' not found in V1")

    r = da.sel(V1=ret_var)                          # S x D x E
    r2 = r * r
    rv_all  = r2.sum("E", skipna=True)              # S x D
    rv_up   = xr.where(r > 0, r2, 0.0).sum("E", skipna=True)   # S x D
    rv_down = xr.where(r < 0, r2, 0.0).sum("E", skipna=True)   # S x D

    rsj_day = divide_safe(rv_up - rv_down, rv_all)  # S x D
    rsj_ema = _ewm_ma_halflife(rsj_day, dim="D", half_life=half_life, mode="mean")  # S x D

    factor_last = rsj_ema.isel(D=[-1]).broadcast_like(r.isel(D=[-1]))  # S x 1 x E
    out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["rsj_asym"]))
    return -1*out.transpose("S","D","E","V1")

```

- 模糊金额比
  - 模糊定义：5 分钟滚动波动率的5 分钟滚动标准差。
  - 模糊金额比：模糊值大于日均模糊值期间的成交量占当日成交量比值，再取d日平均。
  - 因子从金额维度统计了投资者在模糊性较大时的成交程度，同样衡量了投资者对模糊性的厌恶程度，与未来收益负相关；投资者对波动率模糊性的厌恶心理会使得投资者急于卖出而产生过度反应，未来很可能会补涨。
  - 可以用成交金额也可以用成交量

```python
def compute_ambiguity_amount_ratio(
    da: xr.DataArray,
    ret_var: str = "ret",
    half_life: float = 10.0,
    mode: str = "amount",         # 'amount' | 'volume' | 'spread'
) -> xr.DataArray:
    if mode not in {"amount", "volume", "spread"}:
        raise ValueError("mode must be one of {'amount','volume','spread'}")
    for v in (ret_var, "locVol", "volume"):
        if v not in da.coords["V1"].values:
            raise ValueError(f"Variable '{v}' not found in V1")

    r   = da.sel(V1=ret_var)        # S x D x E
    amt = da.sel(V1="locVol")     # S x D x E  (Amount ≡ locVol)
    vol = da.sel(V1="volume")    # S x D x E  (Quantity)

    sigma = r.rolling(E=5, min_periods=5).std()
    amb   = sigma.rolling(E=5, min_periods=5).std()

    amb_day_mean = amb.mean("E", skipna=True).broadcast_like(amb)
    fog = amb > amb_day_mean

    def _daily_ratio(x: xr.DataArray) -> xr.DataArray:
        fog_mean = x.where(fog).mean("E", skipna=True)  # S x D
        all_mean = x.mean("E", skipna=True)             # S x D
        return divide_safe(fog_mean, all_mean)          # S x D

    if mode in {"amount", "spread"}:
        ratio_amt_day = _daily_ratio(amt)               # S x D
    if mode in {"volume", "spread"}:
        ratio_vol_day = _daily_ratio(vol)              # S x D

    if mode == "amount":
        series_day = ratio_amt_day
        fac_name = "amb_amount_ratio"
    elif mode == "volume":
        series_day = ratio_vol_day
        fac_name = "amb_volume_ratio"
    else:
        spread_day = ratio_amt_day - ratio_vol_day      # S x D
        std10 = spread_day.rolling(D=half_life, min_periods=1).std()  # S x D
        neg_mask = spread_day < 0
        adjusted = xr.where(neg_mask, divide_safe(spread_day, std10), spread_day)  # S x D

        s1 = spread_day.where(spread_day < 0).fillna(0.0).sum("S", skipna=True)   # D
        s2 = adjusted.where(adjusted < 0).fillna(0.0).sum("S", skipna=True)       # D
        scale = divide_safe(s1, s2)                                               # D
        scaleB = scale.broadcast_like(adjusted)                                   # S x D
        adjusted = xr.where(adjusted < 0, adjusted * scaleB, adjusted)            # S x D
        series_day = adjusted
        fac_name = "amb_price_spread_adj"

    ema_mean = _ewm_ma_halflife(series_day, dim="D", half_life=half_life, mode="mean")  # S x D
    factor_last = ema_mean.isel(D=[-1]).broadcast_like(vol.isel(D=[-1]))  # S x 1 x E
    out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array([fac_name]))
    return -1*out.transpose("S","D","E","V1")
```

- 时间加权平均的股票相对价格位置: 衡量股票在价格相对高位停留的时间长短，股票在价格相对高位停留的时间越长，因子取值越大。
  $$
  \mathrm{ARPP}=\frac{1}{T}\int_0^T \mathrm{RPP}_t\,dt =\frac{\left(\frac{1}{T}\int_0^T P_t\,dt\right)-L}{H-L} =\frac{\mathrm{TWAP}-L}{H-L}
  $$

  ```python
  def compute_arpp(
      da: xr.DataArray,
      half_life: float = 10.0,
  ) -> xr.DataArray:
      for v in ("robust", "high", "low"):
          if v not in da.coords["V1"].values:
              raise ValueError(f"Variable '{v}' not found in V1")
  
      price = da.sel(V1="robust")
      high  = da.sel(V1="high")
      low   = da.sel(V1="low")
  
      twap_day = price.mean("E", skipna=True)
      high_day = high.max("E", skipna=True)
      low_day  = low.min("E", skipna=True)
  
      denom = high_day - low_day
      arpp_day = divide_safe(twap_day - low_day, denom)
      arpp_day = xr.where(np.isfinite(arpp_day), arpp_day.clip(0.0, 1.0), np.nan)
      arpp_ema = _ewm_ma_halflife(arpp_day, dim="D", half_life=half_life, mode="mean")
      factor_last = arpp_ema.isel(D=[-1]).broadcast_like(price.isel(D=[-1]))
      out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["arpp"]))
      return out.transpose("S","D","E","V1")
  
  ```

  

- 非流动性：

  - 分钟级“最短路径”

  $$
  \mathrm{shortcut}_t=2(\mathrm{high}_t-\mathrm{low}_t)-|\,\mathrm{close}_t-\mathrm{open}_t\,| .
  $$

  - 当日非流动性，再取d日平均

  $$
  \mathrm{ILLIQ}{\text{day}}=\sum{t\in\text{day}} \frac{\mathrm{shortcut}_t}{\mathrm{Amount}t}.
  $$

  ```python
  def compute_illiq_shortcut(
      da: xr.DataArray,
      half_life: float = 10.0,
  ) -> xr.DataArray:
      for v in ("open", "robust", "high", "low", "locVol"):
          if v not in da.coords["V1"].values:
              raise ValueError(f"Variable '{v}' not found in V1")
  
      o = da.sel(V1="open")       # S x D x E
      c = da.sel(V1="robust")
      h = da.sel(V1="high")
      l = da.sel(V1="low")
      amt = da.sel(V1="locVol")   # S x D x E
  
      shortcut = 2.0 * (h - l) - (c - o).abs()                       # S x D x E
      ratio = divide_safe(shortcut, amt)                              # S x D x E
      illiq_day = ratio.sum("E", skipna=True)                         # S x D
      illiq_ema = _ewm_ma_halflife(illiq_day, dim="D", half_life=half_life, mode="mean")  # S x D
      factor_last = illiq_ema.isel(D=[-1]).broadcast_like(c.isel(D=[-1]))  # S x 1 x E
  
      out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["illiq_shortcut"]))
      return out.transpose("S","D","E","V1")
  
  ```

  

- 负偏度系数：负偏度系数高的股票有着更高的暴跌可能，也就有着期望更高的风险溢价。

  $$
  N C S K E W_i=\frac{-(n(n-1))^{1.5} \sum\left(r_{i t}-\bar{r}_l\right)^3}{(n-1)(n-2)\left(\sum\left(r_{i t}-\bar{r}_l\right)^2\right)^{1.5}}
  $$

  ```python
  def compute_ncskew(
      da: xr.DataArray,
      ret_var: str = "ret",
      half_life: float = 10.0,
  ) -> xr.DataArray:
      if ret_var not in da.coords["V1"].values:
          raise ValueError(f"Variable '{ret_var}' not found in V1")
  
      r_min = da.sel(V1=ret_var)                         # S x D x E
      r_day = (1.0 + r_min).prod("E", skipna=True) - 1.0 # S x D
  
      mu = _ewm_ma_halflife(r_day, dim="D", half_life=half_life, mode="mean")  # S x D
      sigma = _ewm_ma_halflife(r_day, dim="D", half_life=half_life, mode="std")# S x D
  
      c = r_day - mu
      m3_ewm = _ewm_ma_halflife(c**3, dim="D", half_life=half_life, mode="mean")  # S x D
  
      denom = sigma ** 3
      ncs = - divide_safe(m3_ewm, denom)                 # S x D
  
      factor_last = ncs.isel(D=[-1]).broadcast_like(r_min.isel(D=[-1]))  # S x 1 x E
      out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["ncskew_ewm"]))
      return out.transpose("S","D","E","V1")
  ```

  

- 价格自相关性因子:

  - 价格一阶差分序列 (ret 序列)，取正的部分做一阶自相关，负的部分也做一阶自相关，然后合并

  ```python
  def compute_cdpp(
      da: xr.DataArray,
      price_var: str = "robust",
      half_life: float = 10.0,
  ) -> xr.DataArray:
      if "robust" not in da.coords["V1"].values:
          raise ValueError(f"Variable '{"robust"}' not found in V1")
  
      p = da.sel(V1="robust")
      dP = p.diff("E")
      dP = dP.reindex(E=p["E"])
      dP_lead = dP.shift(E=-1)
      pos = dP > 0
      neg = dP < 0
  
      dP_pos = xr.where(pos, dP, np.nan)
      dP_lead_pos = xr.where(pos, dP_lead, np.nan)
      corr_pos_day = xr.corr(dP_pos, dP_lead_pos, dim="E")   # S x D
  
      dP_neg = xr.where(neg, dP, np.nan)
      dP_lead_neg = xr.where(neg, dP_lead, np.nan)
      corr_neg_day = xr.corr(dP_neg, dP_lead_neg, dim="E")   # S x D
  
      ema_pos = _ewm_ma_halflife(corr_pos_day, dim="D", half_life=half_life, mode="mean")
      ema_neg = _ewm_ma_halflife(corr_neg_day, dim="D", half_life=half_life, mode="mean")
  
      mu_p = ema_pos.isel(D=-1).mean("S", skipna=True)
      sd_p = ema_pos.isel(D=-1).std("S",  skipna=True)
      z_p = divide_safe(ema_pos.isel(D=-1) - mu_p, sd_p)
  
      mu_n = ema_neg.isel(D=-1).mean("S", skipna=True)
      sd_n = ema_neg.isel(D=-1).std("S",  skipna=True)
      z_n = divide_safe(ema_neg.isel(D=-1) - mu_n, sd_n)
  
      combined = 0.5 * (z_p + z_n)                       # S
      series_last = combined.expand_dims(D=[da["D"].values[-1]])  # S x 1
  
      factor_last = series_last.broadcast_like(p.isel(D=[-1]))    # S x 1 x E
      out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["cdpp"]))
      return out.transpose("S","D","E","V1")
  ```

- 成交量分布

  - 计算同价成交量：将日内相同分钟收盘价的成交量累加至一起，得到在当前价格上的成交量总和；
  - 将成交量累计最大的价格定义为该股当日的成交量支撑点 Volume Support Price，包含该支撑点的附近区域定义为成交量支撑区域 Volume Support Area；
  - 逐步计算 VSP 周围的成交量累计值（价格由近及远，成交量由大及小），该累计值与全天成交量总和的比值超 50 \% 的最小区域，即为成交量支撑区域VSA，该区域上限价格为VSA_High，下限价格为VSA_Low；
  - VSA_High, VSA_Low 可以分别与当日最高价、最低价、收盘价进行比较得到不同feature

  ```python
  def compute_volume_support_pb(
      da: xr.DataArray,
      half_life: float = 10.0,
      mode: str = "b"
  ) -> xr.DataArray:
      for v in ("robust", "volume", "high", "low"):
          if v not in da.coords["V1"].values:
              raise ValueError(f"Variable '{v}' not found in V1")
  
      price = da.sel(V1="robust")  # S x D x E
      vol   = da.sel(V1="volume") # S x D x E
      high  = da.sel(V1="high")   # S x D x E
      low   = da.sel(V1="low")    # S x D x E
  
      high_day = high.max("E", skipna=True)   # S x D
      low_day  = low.min("E", skipna=True)    # S x D
      close_day  = price.isel(E=-1)    # S x D
  
      def _vsa_bounds_1d(p_arr: np.ndarray, v_arr: np.ndarray):
          mask = np.isfinite(p_arr) & np.isfinite(v_arr) & (v_arr > 0)
          if mask.sum() == 0:
              return np.nan, np.nan
          df = pd.DataFrame({"p": p_arr[mask], "v": v_arr[mask]})
          agg = df.groupby("p", sort=True)["v"].sum()
          total = float(agg.sum())
          if total <= 0:
              return np.nan, np.nan
  
          vmax = agg.max()
          vsp = agg[agg == vmax].index.values.mean()
  
          uniq_prices = agg.index.values
          vols = agg.values
          dist = np.abs(uniq_prices - vsp)
          order = np.lexsort((-vols, dist))
  
          cum = 0.0
          sel = np.zeros_like(order, dtype=bool)
          for idx in order:
              sel[idx] = True
              cum += vols[idx]
              if cum >= 0.5 * total:
                  break
          chosen_prices = uniq_prices[sel]
          return float(chosen_prices.min()), float(chosen_prices.max())
  
      vsa_low, vsa_high = xr.apply_ufunc(
          _vsa_bounds_1d,
          price, vol,
          input_core_dims=[["E"], ["E"]],
          output_core_dims=[[], []],
          vectorize=True,
          dask="parallelized",
          output_dtypes=[np.float64, np.float64],
      )
  
      if mode == "p":
          vsa_low2max_day  = divide_safe(high_day - vsa_low, high_day)
          vsa_ema = _ewm_ma_halflife(vsa_low2max_day,  dim="D", half_life=half_life, mode="mean")
          out_name = "vsa_p_low2max"
      elif mode == "b":
          vsa_high2min_day = divide_safe(vsa_high - low_day, low_day)
          vsa_ema = _ewm_ma_halflife(vsa_high2min_day, dim="D", half_life=half_life, mode="mean")
          out_name = "vsa_b_high2min"
      elif mode == 'r':
          vsa_high2min_day = divide_safe(vsa_low - close_day, close_day)
          vsa_ema = _ewm_ma_halflife(vsa_high2min_day, dim="D", half_life=half_life, mode="mean")
          out_name =
  
      f_last = vsa_ema.isel(D=[-1]).broadcast_like(vol.isel(D=[-1]))  # S x 1 x E
  
      out = xr.concat([f_last], dim="V1").assign_coords(V1=[out_name])
      return out.transpose("S","D","E","V1")
  ```

- 跳跃波动率

  - 日内1分钟/5分钟收益率序列

  - 正/负半方差 realized semivariance)
    $$
    RS_t^+ \;=\; \sum_{i=1}^{n_t} r_{t,i}^2\,\mathbf{1}{\{r_{t,i}>0\}}, \qquad RS_t^- \;=\; \sum_{i=1}^{n_t} r_{t,i}^2\,\mathbf{1}{\{r_{t,i}<0\}}.
    $$

  - 三乘幂变差（Tripower Variation, 跳跃稳健的已实现方差）：
    $$
    \widehat{IV}t \;=\; \mu{2/3}^{-3}\sum_{i=3}^{n_t} \big|r_{t,i}\big|^{2/3}\big|r_{t,i-1}\big|^{2/3}\big|r_{t,i-2}\big|^{2/3}, \\ \mu_q \;=\; \mathbb{E}|Z|^q = \frac{2^{q/2}}{\sqrt{\pi}}\Gamma\!\Big(\tfrac{1+q}{2}\Big),\; Z\sim\mathcal N(0,1).
    $$

  - 上/下行跳跃波动率

  $$
  \,RVJP_t \;=\; \max\!\Big(RS_t^+ - \tfrac12 \widehat{IV}_t,\; 0\Big), \\RVJN_t \;=\; \max\!\Big(RS_t^- - \tfrac12 \widehat{IV}_t,\; 0\Big)
  $$

  - 上下行跳跃不对称性

  $$
  SRVJ_t \;=\; RVJP_t - RVJN_t
  $$

  - 大/小跳分解的阈值

  $$
  \,\gamma_t \;=\; \alpha\,\Delta_n^{0.49}\sqrt{\widehat{IV}_t}\,, \; \Delta_n \;=\; \frac{1}{n_t},\;\; \alpha \approx 4.
  $$

  

  - “大的”上/下行跳跃波动率

  $$
  \,RVLJP_{\gamma,t} \;=\; \min\!\Big(RVJP_t,\;\sum_{i=1}^{n_t} r_{t,i}^2\mathbf{1}{\{r{t,i}>\gamma_t\}}\Big)\,\\
  
  \,RVLJN_{\gamma,t} \;=\; \min\!\Big(RVJN_t,\;\sum_{i=1}^{n_t} r_{t,i}^2\mathbf{1}{\{r{t,i}<-\gamma_t\}}\Big)\,
  $$

  - “小的”上/下行跳跃波动率

  $$
  \,RVSJP_t \;=\; RVJP_t - RVLJP_{\gamma,t}, \\
  \,RVSJN_t \;=\; RVJN_t - RVLJN_{\gamma,t}\,.
  $$

  - “大的 / 小的”上下行跳跃不对称性
    $$
    \,SRVLJ_t \;=\; RVLJP_{\gamma,t} - RVLJN_{\gamma,t}\,,\\
    \,SRVSJ_t \;=\; RVSJP_t - RVSJN_t\,.
    $$

  - 显著性加权的上下行跳跃不对称性（工程友好版）

    - 超阈值强度权重（当日）：
      $$
      W_t \;=\; \sum_{i=1}^{n_t}\max\!\Big(\frac{|r_{t,i}|}{\gamma_t}-1,\,0\Big).
      $$
      

    - 时间加权不对称性（跨日用 EMA，半衰期 half_life）：
      $$
      \,TSRJV \;=\; \frac{\mathrm{EMA}_t\!\big(W_t\cdot SRVJ_t\big)} {\mathrm{EMA}_t\!\big(W_t\big)}\,.
      $$

  - 统计检验权重（如 BNS/Jacod 检验的
    $$
    W_{t} =\frac{B V_t}{N^{-1} \sqrt{\hat{\Omega}_{S w V}} \Phi_{1-\alpha}^{-1}}\left(1-\frac{R V_t}{S w V_t}\right).
    $$
    

```python
def _mu_abs_normal(q: float) -> float:
    """E|Z|^q for Z~N(0,1) = 2^{q/2} / sqrt(pi) * Gamma((1+q)/2)."""
    return (2.0 ** (q / 2.0)) / math.sqrt(math.pi) * math.gamma((1.0 + q) / 2.0)

def compute_jump_volatility_family(
    da: xr.DataArray,
    ret_var: str = "ret",
    half_life: float = 10.0,
    alpha: float = 4.0,
) -> xr.DataArray:
    if ret_var not in da.coords["V1"].values:
        raise ValueError(f"Variable '{ret_var}' not found in V1")

    r = da.sel(V1=ret_var)  # S x D x E

    rs_plus  = xr.where(r > 0, r*r, 0.0).sum("E", skipna=True)   # S x D
    rs_minus = xr.where(r < 0, r*r, 0.0).sum("E", skipna=True)   # S x D

    mu23 = _mu_abs_normal(2.0/3.0)
    ar = r.abs() ** (2.0/3.0)
    tp = (ar * ar.shift(E=1) * ar.shift(E=2)).sum("E", skipna=True)  # S x D
    iv_hat = tp / (mu23 ** 3)

    rv_all = (r*r).sum("E", skipna=True)                           # S x D
    nbar = r.count("E")                                            # S x D  (per-day valid bar count)
    delta_n = divide_safe(1.0, nbar)                               # S x D

    rvjp = xr.ufuncs.maximum(rs_plus - 0.5 * iv_hat, 0.0)          # S x D
    rvjn = xr.ufuncs.maximum(rs_minus - 0.5 * iv_hat, 0.0)         # S x D
    srvj = rvjp - rvjn                                             # S x D

    gamma = alpha * (delta_n ** 0.49) * xr.ufuncs.sqrt(iv_hat)     # S x D
    gamma_b = gamma.broadcast_like(r)                               # S x D x E

    sum_up_big   = xr.where(r >  gamma_b, r*r, 0.0).sum("E", skipna=True)  # S x D
    sum_down_big = xr.where(r < -gamma_b, r*r, 0.0).sum("E", skipna=True)  # S x D

    rvljp = xr.ufuncs.minimum(rvjp, sum_up_big)                    # S x D
    rvljn = xr.ufuncs.minimum(rvjn, sum_down_big)                  # S x D
    rvsjp = rvjp - rvljp                                           # S x D
    rvsjn = rvjn - rvljn                                           # S x D
    srvlj = rvljp - rvljn                                          # S x D
    srvsj = rvsjp - rvsjn                                          # S x D

    abs_r = r.abs()
    W = xr.ufuncs.maximum(divide_safe(abs_r, gamma_b) - 1.0, 0.0).sum("E", skipna=True)  # S x D
    num_tsrjv = _ewm_ma_halflife(W * srvj, dim="D", half_life=half_life, mode="mean")    # S x D
    den_tsrjv = _ewm_ma_halflife(W,         dim="D", half_life=half_life, mode="mean")   # S x D
    tsrjv = divide_safe(num_tsrjv, den_tsrjv)                                            # S x D

    series_map = {
        "rvjp":  _ewm_ma_halflife(rvjp,  dim="D", half_life=half_life, mode="mean"),
        "rvjn":  _ewm_ma_halflife(rvjn,  dim="D", half_life=half_life, mode="mean"),
        "srvj":  _ewm_ma_halflife(srvj,  dim="D", half_life=half_life, mode="mean"),
        "rvljp": _ewm_ma_halflife(rvljp, dim="D", half_life=half_life, mode="mean"),
        "rvljn": _ewm_ma_halflife(rvljn, dim="D", half_life=half_life, mode="mean"),
        "rvsjp": _ewm_ma_halflife(rvsjp, dim="D", half_life=half_life, mode="mean"),
        "rvsjn": _ewm_ma_halflife(rvsjn, dim="D", half_life=half_life, mode="mean"),
        "srvlj": _ewm_ma_halflife(srvlj, dim="D", half_life=half_life, mode="mean"),
        "srvsj": _ewm_ma_halflife(srvsj, dim="D", half_life=half_life, mode="mean"),
        "tsrjv": tsrjv,
    }

    out = xr.concat(list(series_map.values()), dim="V1").assign_coords(V1=list(series_map.keys()))
    return out.transpose("S","D","E","V1")
```



# Risk Factor

- Semi-beta

  - 基于个股收益和市场基准收益方向的不同，可将传统 Beta 因子拆解为 4 个部分。以下展示其中一个因子 (四种都可以作为beta measure)：对应市场收益和资产收益同为正的情况，在 A 股市场该因子的负溢价更明显。
    $$
    \begin{gathered}
    \hat{\beta}_{t, i}^P=\frac{\sum_{k=1}^m r_{t, k, i}^{+} f_{t, k}^{+}}{\sum_{k=1}^m f_{t, k}^2} \\
    r_{t, k, i}^{+}=\max \left(r_{t, k, i}, 0\right) \\
    f_{l, k}^{+}=\max \left(f_{t, k}, 0\right)
    \end{gathered}
    $$
    其中
    （1）$$r_{t, k, i}$$ 为股票 i 在交易日 t 内第 k 个区间的收益率数据；
    （2）$$f_{t, k}$$ 为市场基准在交易日 t 内第 k 个区间的收益率数据，市场基准可以为沪深 300、中证 500 等指数；
    （3）$$m$$ 为交易日t内的时间区间数量。