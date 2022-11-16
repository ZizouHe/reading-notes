# Technological Links and Predictable Returns

- [Lee, Charles MC, Stephen Teng Sun, Rongfei Wang, and Ran Zhang. "Technological links and predictable returns." *Journal of Financial Economics* 132, no. 3 (2019): 76-96.](https://www.sciencedirect.com/science/article/pii/S0304405X18303167)

- [获取$$\alpha$$的新思路：科技关联度, 知乎-石川](https://zhuanlan.zhihu.com/p/44781908)

- [背景知识：股票多因子模型的回归检验，知乎-石川](https://zhuanlan.zhihu.com/p/40984029)

## Main Points

- 使用 TECHRET 因子的 Long/Short 组合收益的时间序列和 Fama-French 三因子（Fama and French 1993）的时间序列在时序上回归，得到的截距恰好就是截面上 L/S 无法被三因子解释的超额收益
  - 考虑的不同因子模型之后获得的超额收益可以类似的解释。其中，4 factor model 是 Fama-French 三因子 + Carhart (1997) 的动量因子，5 factor model 是 Fama and French (2015) 提出的五因子模型，而 6 factor model 是该五因子加上动量因子。
- 使用 4 factor model 对 L/S 组合进行时序回归时，得到的因子载荷。以等权L/S为例，结果显示该组合在市场因子（MKT）上有负的暴露，在 SMB 和 MOM 因子上有正的暴露。这意味着该策略在市场下行、以及小市值和动量股表现好的时候额外有效。
- 使用 Fama and MacBeth (1973) 进行了截面回归检验，其目的是为了在控制住其他变量后考察 TECHRET 因子对于股票截面收益差异的解释程度。(Fama-MacBeth 回归是在每个时点在截面上用因子载荷和个股的收益率进行回归，从而得到每期各因子的收益率，然后在时序上取平均就得到因子的预期收益率)
- For each tech-peer firm, we first estimate its alpha and its factor loadings using the four-factor model (Fama and French, 1993; Carhart, 1997) and the previous 12 months of daily data ($$t-12$$ to $$t-1$$). We then use these parameter estimates, together with the realized factor returns, to obtain each tech-peer’s idiosyncratic return at time $$t$$.  [背景知识：股票多因子模型的回归检验，知乎-石川](https://zhuanlan.zhihu.com/p/40984029)
- 对于超额收益，学术界和业界主流的两种解释是**错误定价**和**风险补偿**。搞清楚 TECHRET 背后的机制至关重要：错误定价意味着投资者可以通过合理的策略获得潜在的超额收益；而风险补偿则意味着投资者获得的收益是以承担额外风险为代价的。
  - 或许价格对于与科技有关的基本面消息的吸收是缓慢的，从而导致了错误定价。研究了以下三个方面：
    - 科技相关新息（innovation）的性质；
    - 投资者对这类新息的有限注意力（limited attention）；
    - 投资者的套利成本。
  - 如果某个异象和错误定价有关，则该因子在盈余公告期内应该比其他时间内获得更高的收益，这是因为最新的盈余报告有助于修正投资者之前对该股票的估值错误。而反过来，如果该异象是源自风险补偿，我们将不会观察到上述现象

## 升级版科技关联度

- [Bekkerman, R., E. M. Fich, and N. V. Khimich (2022). The effect of innovation similarity on asset prices: Evidence from patents' big data. ***Review of Asset Pricing Studies***](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3147218)
- [科技关联度 (II)](https://zhuanlan.zhihu.com/p/577519685)
- Lee et al. (2019) 使用专利类别vector计算科技关联度，Bekkerman et al. (2022) 没有使用专利类别，而是直接对专利进行文本分析，通过提取专业术语并计算其重合度来描述公司之间的相似程度。不出意外，升级版科技关联度“打败”了 Lee, et al. (2019)。这体现在当控制了 Lee, et al. (2019) 的变量之后，新的变量依旧能够获得超额收益，而反之则不然。