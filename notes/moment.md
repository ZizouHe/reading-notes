# Momentum

## Introduction to Momentum

- [Momentum](https://zhuanlan.zhihu.com/p/459019458)
- [残差动量 —— 有理有据还是数据挖掘？](https://zhuanlan.zhihu.com/p/95259084)
- Momentum construction:
  - Use a one-month gap between the end of the ranking period and the start of the holding period to avoid the short-term reversals shown by Jegadeesh (1990) and Lehmann (1990). 
- 动量因子成因
  - 系统性风险敞口：在一个市场状态的初期，动量组合对于当前的市场状态有着负的暴露，从而导致该时期的大幅损失，这意味着动量组合需要获得更高的收益来弥补相关的风险。Daniel and Moskowitz (2016) 将此形象地描述为“动量崩溃”（momentum crashes），并指出这一尾部风险正是动量的风险溢价来源。
  - 投资者行为偏差：投资者对其私有信息的过度自信及有偏的业绩自我归因会造成动量效应。Hur and Singh (2016) 进一步指出反应不足是主要原因。
  - 推定预期偏差：投资者通过将当前数据外推来得到对未来表现的预期，而这一朴素估计是有偏的。
  - 知情交易
  - 市场情绪
- 动量因子改进
  - 残差动量：由个股的残差收益率计算，定义为个股收益率中无法被给定多因子模型解释的部分。
  - 价格高点距离：当前最新价与最高点的距离。
  - 加速度动量：价格对时序的期数以及期数的平方项回归，并取平方项的系数为加速度动量指标。
  - Condi on 买方竞争度指标，(condition on crowdness)
  - 左尾动量：投资者对尾部风险或者坏消息往往反应不足，导致尾部动量得以持续
    - [Atilgan et al. (2020 JFE) Left-tail momentum- Underreaction to bad news, costly arbitrage and equity returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3070777)
    - Investors underestimate the persistence in left-tail risk and overprice stocks with large recent losses. Thus, low returns in the left-tail of the distribution persist into the future causing left-tail return momentum. The left-tail risk anomaly is stronger for stocks that are more likely to be held by retail investors, that receive less investor attention, and that are costlier to arbitrage.

## Momentum Crashes

- [Daniel and Moskowitz (2016 JFE) Momentum crashes](https://www.sciencedirect.com/science/article/pii/S0304405X16301490)

- Momentum crashes: despite their strong positive average returns across numerous asset classes, momentum strategies can experience infrequent and persistent strings of negative returns. 

- Observation from data: Momentum premium falls when the past three-year market return has been negative and that the momentum premium is low when market volatility is high.

- The crash performance is mostly attributable to the short side or the performance of losers, and **the short side beta increases dramatically during crash periods.**

- Solutions:

  - the optimal weight (alpha size) on the risky asset at time $$t-1$$ is
    $$
    w_{t-1} = \frac{1}{2 \lambda} \frac{\mu_{t-1}}{\sigma_{t-1}^2},
    $$
    where $$\mu_{t-1}$$ is the conditional expected return on the (zero-investment) WML portfolio over the coming month, it is estimated using the following regression
    $$
    R_{t} = \left(\alpha_0 + \alpha_{B} I_{B, t-1}\right) + \left(\beta_0 + \beta_{B} I_{B, t-1}\right) R_{m, t} + \epsilon_t
    $$
    where $$I_{B, t-1}$$ is  an ex ante bear market indicator that equals one if the cumulative index return $$R_{m,t}$$ in the past 24 months is negative and is zero otherwise.
    
    The conditional variance is given by GARCH model,
    $$
    \begin{aligned}
    R_t &= \mu + \epsilon_t, \; \; \epsilon_t \sim \mathcal{N}(0, \sigma^2_t), \\
    \sigma_t^2 &= w + \beta \sigma_{t-1}^2 + \left(\alpha + \gamma I (\epsilon_{t-1} < 0)\right) \epsilon_{t-1}^2.
    \end{aligned}
    $$
    

## 寻找高质量动量

- [给你的动量选股策略加点“料”](https://zhuanlan.zhihu.com/p/40468929)
- [Da, Zhi, Umit G. Gurun, and Mitch Warachka. "Frog in the pan: Continuous information and momentum." *The review of financial studies* 27, no. 7 (2014): 2171-2218.](https://academic.oup.com/rfs/article-abstract/27/7/2171/1578455)
- [Bali, Turan G., Nusret Cakici, and Robert F. Whitelaw. "Maxing out: Stocks as lotteries and the cross-section of expected returns." *Journal of financial economics* 99, no. 2 (2011): 427-446.](https://www.sciencedirect.com/science/article/abs/pii/S0304405X1000190X)

1. **寻找依靠价格缓慢增长实现的高动量；**

   - 行为金融学中的温水煮青蛙：人的这种缺陷叫做limited attention（有限注意力）。由于人们的认知资源是有限的，在任何给定的时刻，我们的大脑都偏好去处理那些最显著、最重要的信息，而忽视那些不显著的、经济效应微弱的因素。一系列频繁但微小的变化对于人的吸引力远不如少数却显著的变化；因此投资者对于连续信息造成的股价变化反应不足。

   - 信息离散性（information discreteness，ID）：ID 低（说明信息连续性强）的动量才是高质量动量
     $$
     ID = \text{sign(过去一段时间的收益率) × (这段时间内下跌交易日\% - 这段时间内上涨收益日\%)}
     $$

   - Da et al. (2014) 说明，与传统动量相比，通过 ID 因子删选找到的高质量动量能够获得更高的超额收益，且该收益在样本外的持续性更强（这有助于我们降低调仓频率、减少换手率、节约交易成本）。

2. **避免大波动造成的高动量。**

   - 行为金融学中重要的理论 —— 前景理论 —— 指出，人们对于极小概率事件发生的主观感受存在认知偏差，会高估它们发生的概率。对于小概率事件发生可能性的高估导致投资者会过度追逐具有正偏度分布的股票，造成它们的高动量。
   - Bali et al. (2011) 使用一个称作 MAX 的代理指标研究了这个问题。MAX 是过去 1 个月内日收益率的最大值（美股不设涨跌停板限制，因此更能反映人们对 lottery-like 股票追逐的疯狂程度）。使用 MAX 将股票分成 10 组，MAX 值最高的那一组为 lottery-like 股票，而 MAX 值最低的那一组称为“无聊”股票。数据显示，“无聊”股票能显著跑赢 lottery-like 股票。在挑选高动量股票时，我们可以主动避免那些 lottery-like 股票。

## 加强版反转

- [加强版反转](https://zhuanlan.zhihu.com/p/70129890)
- [寻找股票市场中的预期差](https://zhuanlan.zhihu.com/p/53944793)

- [Da, Liu, and Schaumburg (2013 MS) A Closer Look at the Short-Term Return Reversal](https://pubsonline.informs.org/doi/10.1287/mnsc.2013.1766)
- [Piotroski (2000 JAR) Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers](https://www.semanticscholar.org/paper/Value-Investing%3A-The-Use-of-Historical-Financial-to-Piotroski/0559e92e06dae21e77ea79d79417b8a1d40be772)
- [Zhu, Z., L. Sun, and M. Chen (2019). Fundamental strength and short-term return reversal.](https://www.sciencedirect.com/science/article/abs/pii/S0927539819300234#:~:text=Fundamental%20strength%20information%20helps%20better%20identify%20short-term%20return,winners%20with%20weak%20fundamentals%20experience%20stronger%20short-term%20reversals.)
- [Piotroski and So (2012 RFS) Identifying Expectation Errors in Value/Glamour Strategies](https://academic.oup.com/rfs/article-abstract/25/9/2841/1589567)

Da, Liu, and Schaumburg (2013) 将和现金流有关的新息从股票收益率中减去，以此排除基本面变化对于收益率的影响，以期捕捉由于过度反应和流动性冲击造成的非理性下跌。
$$
\mathrm{Residual}_{t+1} = r_{t+1} - CF_{t+1}
$$
其中 CF代表最新的cash flow news, 使用了基于分析师预期修正的计算方法。然而，上述残差计算方法存在两个问题：

1. **股票价格对于基本面消息的吸收是缓慢的，因此仅考虑最新的基本面信息是不够的，还应考虑过去一段时间的；**
2. 分析师并不能覆盖全部股票，因此使用分析师预期修正无法对全市场的股票进行实证分析。

解决第一点：计算过去一段时间窗口内 CF 的变化

解决全部两点：Zhu, Sun, and Chen (2019) 用 Piotroski (2000) 的 F-Score 代替 cash flow news 作为基本面信息的代理变量
$$
\mathrm{Residual}_{t+1} = r_{t+1} - \text{F-score}
$$
其中 F-score 通过 9 个指标给股票的基本面打分，计算方式为以下九个dummy量的和：

- Performance-related Factors:

  - ROA: net income before extraordinary items scaled by beginning-of-the-year total asset. (Take 1 if positive else 0)
  - CFO: cash flow from operations scaled by beginning-of-the-year total asset (Take 1 if positive else 0)
  - $$\Delta$$ ROA: the current year's ROA less the prior year's ROA (Take 1 if positive else 0)
  - ACCRUAL: the current year's net income before extraordinary items less cash flow from operations, scaled by beginning-of-the-year total asset (Take 1 if positive else 0)
  - $$\Delta$$ LEVER: the historical change in the ratio of total long-term debt to average total assets, and view an increase (decrease) in financial leverage as a negative (positive) signal. (Take 1 if positive else 0)
  - $$\Delta$$ LIQUID: the historical change in the firm's current ratio between the current and prior year, where I define the current ratio as the ratio of current assets to current liabilities at fiscal year-end. (Take 1 if positive else 0)
  - EQ-OFFER: equal to one if the firm did not issue common equity in the year preceding portfolio formation, zero otherwise. (Similar to an increase in long-term debt, financially dis- tressed firms that raise external capital could be signaling their inability to generate sufficient internal funds to service future obligation)

  - $$\Delta$$ MARGIN: the firm's current gross margin ratio (gross margin scaled by total sales) less the prior year's gross margin ratio. (Take 1 if positive else 0)

  - $$\Delta$$ TURN as the firm's current year asset turnover ratio (total sales scaled by beginning-of-the-year total assets) less the prior year's asset turnover ratio.  (Take 1 if positive else 0)

Zhu, Sun, and Chen (2019) 将这个剔除了基本面信息的反转异象称为**基本面锚定反转（Fundamental-anchored reversal）**。



类似地，Piotroski and So (2012) 使用P/B 和 F-Score 作为市场和基本面的代理变量，寻找存在预期差的股票；而上述反转策略使用过去短期的涨跌幅替换 P/B，和 F-Score 一起寻找存在预期差的股票。

- 预期差：价格反映了投资者对股票的市场预期，而内在价值反映了股票本身的基本面预期。高、低估说明这两个预期之间存在差异，这个差异为预期差。
- 价值股跑赢成长股的内在逻辑是预期差的修正

## 因子动量和动量因子

- [因子动量和动量因子](https://zhuanlan.zhihu.com/p/606461747)

- [Ehsani and Linnainmaa (2022 JoF). Factor momentum and the momentum factor.](https://onlinelibrary.wiley.com/doi/10.1111/jofi.13131)

- **Q1：**因子收益率是否有时序自相关性？
- **A1：**绝大多数因子的收益率存在自相关性。
- **Q2：**因子满足何种条件时，更容易出现自相关性？
- **A2：**和个股收益率协方差矩阵更相关的因子，自相关性更强。
- **Q3：**利用自相关性、基于因子历史收益率构造的因子动量策略（注意，它类似于 UMD，是以因子组合为 assets 的截面动量策略）和个股截面动量因子（即 UMD）有什么关系？谁是因？谁又是果？
- **A3：**因子动量能够解释个股动量因子（及其各种变化版本），但个股动量（及其各种版本）无法解释因子动量。个股动量效应背后的驱动（之一）是因子动量。
- **Q4：**因子动量能否解释个股残差动量？
- **A4：**残差动量是多因子模型中存在遗漏变量所致，仅仅是被遗漏的因子的动量。一旦不存在模型设定偏误，残差动量消失。
- **Q5：**如何理解个股动量因子和其他因子时序无关的实证现象？
- **A5：**当控制了历史收益率之后，个股动量因子和其他因子有很强的正相关或负相关。个股动量因子和其他因子时变的条件相关性使其看上去和其他因子非条件无关。
