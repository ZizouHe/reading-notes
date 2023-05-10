# Time Series Momentum

- [因子动物园 - 时序动量真的更好吗？](https://zhuanlan.zhihu.com/p/120835716)
- [刀疤连 - 和趋势做纯纯的朋友](https://zhuanlan.zhihu.com/p/81421085)

**学术上在解释因子的收益来源时，往往从两个角度入手：risk-based 和 mispricing。前者是经典金融学的角度，认为一个异象如果能获得超额收益，肯定是承担了某种讨厌的风险，超额收益是这种风险的补偿；后者从行为金融学的角度，认为要么是某种限制阻碍了异象的消失，要么是投资者认知偏差导致的行为不理性。**

## 时序动量

- [Moskowitz, Tobias J., Yao Hua Ooi, and Lasse Heje Pedersen. "Time series momentum." *Journal of financial economics* 104, no. 2 (2012): 228-250.](https://www.sciencedirect.com/science/article/pii/S0304405X11002613)

1. 时序动量与横截面动量的区别
   - Cross-sectional momentum literature focuses on the relative performance of securities in the cross-section, finding that securities that recently outperformed their peers over the past three to 12 months continue to outperform their peers on average over the next month.
   - Time series momentum focuses purely on a security’s own past return.
2. This positive time series momentum that partially reverse over the long-term may be consistent with initial under-reaction and delayed over-reaction, which theories of sentiment suggest can produce these return patterns
   - 有效市场假说认为，当出现某个重要的新信息时，价格会立即得到反应，以匹配最新的内在价值。然而，行为金融的角度认为，由于投资者认知偏差的纯在，市场并不是完全有效，而是慢慢地吸收新信息的影响。
   - 初始阶段，由于锚点效应 ( Anchoring )、处置效应 ( The disposition effect) 和非盈利操作等，导致价格对信息反应不足。
     - 锚点效应。投资者往往会把自己的观点锚定在最近历史数据上，不愿意很快改变自己的想法，当新消息到来时反应很迟钝，造成价格反应缓慢；
     - 处置效应。投资者往往会过早低卖出盈利股票以兑现收益；相反，对那些亏损的股票迟迟不肯止损。这样的后果是，上涨不会一蹴而就，下跌不会一跌到底，造成价格慢慢的移动；
     - 非盈利操作。一些非盈利操作，也会减缓价格的反应速度，例如中央银行在外汇市场和固定收益市场进行斡旋，以减少汇率和利率的波动。
   - 一旦趋势起来，就进入了第二阶段：趋势持续甚至过度反应，这往往是由于羊群效应 ( Herding ) ，以及确认和代表偏差 ( Confirmation bias 和 representativene)等因素导致的。
     - 羊群效应。羊群效应也叫从众效应，当投资者观点和其他大多数投资者观点不一致时，容易怀疑和改变自己的观点，以使得和群体一致。在价格上涨或下跌开启后，投资会想羊群一样，加入到趋势行情中来；
     - 确认和代表性偏差。行情开启后，投资者会用最近的价格变动来推断未来，选择性地关注最近盈利的方向；不仅如此，一旦确认了自己的观点，便会找各种数据和信息支持自己的看法，这使得价格趋势得以延续。
   - 最后，趋势不会永不眠，价格不会一直朝一个方向走下去。在趋势的末端，价格可能已经过度反应导致严重偏离基本面，因此最终会出现反转趋势宣告结束。

3. We focus on the most liquid instruments to avoid returns being contaminated by illiquidity or stale price issues and to match more closely an implementable strategy at a significant trade size.

4. The ex ante annualized variance 

5. The ex ante annualized variance $$\sigma_{t}^{2}$$ for each instrument is calculated as follows:
   $$
   \sigma_{t}^{2}=261 \sum_{i=0}^{\infty}(1-\delta) \delta^{i}\left(r_{t-1-i}-\bar{r}_{t}\right)^{2}.
   $$
   where the scalar 261 scales the variance to be annual, the weights $$(1-\delta) \delta^{i}$$ add up to one, and $$\bar{r}_{t}$$ is the exponentially weighted average return computed similarly. The parameter $$\delta$$ is chosen so that the center of mass of the weights is $$\sum_{i=0}^{\infty}(1-\delta) \delta^{i} i=\delta /(1-\delta)=60$$ days.

6. The regression is given by
   $$
   r_{t}^{s} / \sigma_{t-1}^{s}=\alpha+\beta_{h} r_{t-h}^{s} / \sigma_{t-h-1}^{s}+\varepsilon_{t}^{s},
   $$
   or
   $$
   r_{t}^{s} / \sigma_{t-1}^{s}=\alpha+\beta_{h} \operatorname{sign}\left(r_{t-h}^{s}\right)+\varepsilon_{t}^{s}.
   $$

7. 交易策略：For each instrument $$s$$ and month $$t$$, we consider whether the excess return over the past $$k$$ months is positive or negative and go long the contract if positive and short if negative, holding the position for $$h$$ months. We set the position size to be inversely proportional to the instrument's ex ante volatility, $$1 / \sigma_{t-1}^{s}$$, each month. 

8. 如果只考虑用过去12个月收益为基准，hold未来一个月的交易策略, the TSMOM return for any instrument $$s$$ and month $$t$$ is therefore:
   $$
   r_{t, t+1}^{T S M O M, s}=\operatorname{sign}\left(r_{t-12, t}^{s}\right) \frac{40 \%}{\sigma_{t}^{s}} r_{t, t+1}^{s}.
   $$

   - If we regress the TSMOM strategy for each security on the strategy of always being long (i.e., replacing ‘‘sign’’ with a 1 in the above equation), then we get a positive alpha in 90% of the cases (of which 26% are statistically significant; none of the few negative ones are significant).

9. The link between time series momentum returns and the positions of speculators and hedgers indicates that speculators profit from time series momen- tum at the expense of hedgers. This evidence is consistent with speculators earning a premium via time series momentum for providing liquidity to hedgers.

## 时序动量的问题

- [Huang, Dashan, Jiangyuan Li, Liyao Wang, and Guofu Zhou. "Time series momentum: Is it there?." *Journal of Financial Economics* 135, no. 3 (2020): 774-794.](https://www.sciencedirect.com/science/article/abs/pii/S0304405X19301953)

1. 不同资产未调整的收益对未来收益的预测能力，并发现只有 8（3）种资产在 10%（5%）的显著性水平下有显著的预测能力。样本外表现则更加糟糕，有 45 种资产的样本外 R 方是负的。

2. 考虑MOP(2012)的回归，

$$
r_{t}^{s} / \sigma_{t-1}^{s}=\alpha+\beta_{h} r_{t-h}^{s} / \sigma_{t-h-1}^{s}+\varepsilon_{t}^{s},
$$

make an implicit assumption that the mean returns of all assets are the same by imposing a common intercept. To highlight fixed effects, a possible specification is
$$
r_{t}^{s} / \sigma_{t-1}^{s}=\alpha+\beta_{h} r_{t-h}^{s} / \sigma_{t-h-1}^{s}+ \mu_s / \sigma_s +\varepsilon_{t}^{s}
$$
where $$\mu_s$$ and $$\sigma_s$$ are the unconditional mean and volatility of asset $$s$$. Hence, the estimate of $$\beta$$ should be
$$
\hat{\beta}=\beta+\frac{\operatorname{Cov}\left(r_{t-h+1}^{s} / \sigma_{t-h}^{s}, \mu_{s} / \sigma_{s}\right)}{\operatorname{Var}\left(r_{t-h+1}^{s} / \sigma_{t-h}^{s}\right)}.
$$
If all assets have the same Sharpe ratio (or mean, if volatilities are the same), the second term is zero ($$\mu_{s} / \sigma_{s}$$ is fixed). Otherwise, it would be significantly positive when the number of assets is large, as the correlation between realized returns and their means is mechanically positive. As a result, the slope estimate of MOP(2012) regression is biased upward.

- Two more reasons:
  - Because volatility varies dramatically across assets, volatility scaling in the pooled regression without controlling for fixed effects can further exacerbate the upward bias.
  - As a predictor, the past 12-month cumulative return is persistent and can generate substantial size distortions. (large sample result when sample size is non-asymptotic, slow non-asymptotic rate).

3. 构建了一个 TSH 策略，which does not require predictability：
   $$
   r_{t+1}^{T S H, s}=\operatorname{sign}\left(r_t^{s}\right) r_{t+1}^{s}.
   $$

   - find that the TSM and TSH strategies perform virtually the same and their differences in average returns, as well as in risk-adjusted ones, are indifferent from zero. We find that the performances of the TSM and TSH strategies mainly stem from their long legs, and their short legs have insignificant average and risk-adjusted returns.
   - Examine the overall predictability of TSM across assets. The slope measures how realized returns are explained by predicted returns. If the past 12-month return perfectly predicts the next one-month return, the slope should have a value of one. We find that for the TSM forecasts the slope has a value close to zero. When regressing the TSM forecasts on the TSH forecasts, the slope is very close to one. This result indicates little difference in predictability between the two forecasts, suggesting, again, no evidence of TSM across the assets.
   - 显然，TSH 的持仓会比较稳定，不太会频繁调仓。某种程度上，TSH 类似买入持有（buy-and-hold），当然，严格来讲，不仅仅是 buy-and-hold ，还有 sell-and-hold 。

## 时序动量与截面动量

- [Goyal, Amit, and Narasimhan Jegadeesh. "Cross-sectional and time-series tests of return predictability: What is the difference?." *The Review of Financial Studies* 31, no. 5 (2018): 1784-1824.](https://academic.oup.com/rfs/article-abstract/31/5/1784/4636242)

1. 考虑到资产总体上会更多上涨而非下跌，做多过去收益率大于 0 的资产而做空过去收益率小于 0 的资产的时序动量平均而言会有净多头寸。相比之下，截面动量是完全对冲的、资金中性多空组合。To make these strategies directly comparable, we add to the CS strategy a time-varying investment in the market (TVM) equal to the dollar value of the difference between the long and short sides of the TS strategy each month.

2. 作者们进一步将净头寸带来的收益拆分为（静态持仓获取的）风险溢价和择时收益：
   $$
   \begin{aligned}
   R_{t}^{T V M}&=\operatorname{NetLong}_{t} \times \bar{R}_{t}=\sum_{i} w_{i t-1}^{T S} \times \bar{R}_{t}, \\
   \overline{R_{t}^{T V M}}&=\underbrace{\overline{\text { NetLong }_{t}} \times \overline{\bar{R}_{t}}}_{\text {Risk Premium }}+\underbrace{\operatorname{cov}\left(\operatorname{NetLong}_{t}, \bar{R}_{t}\right)}_{\text {Market Timing }},
   \end{aligned}
   $$
   where $$\overline{\mathrm{NetLong}_{t}}$$ and $$\overline{\bar{R}}_{t}$$ are the average net long position and the average equalweighted excess return, respectively, over the sample period. Table 7 展示了上述分解的结果，

   - 风险溢价部分无论在经济意义上还是统计上看都非常显著。
   - 择时收益仅在回望期为 1 月时显著，随着回望期变长，择时收益逐渐下降，甚至变为负的。

   - 时序动量的确有显著的净多头暴露，且随着回望期变长，净多头暴露也变得更大。因子时序动量的收益主要来自 buy-and-hold 所提供的风险溢价。The TS strategy benefits from the risk premium component due to large net long position in the market. 高beta
