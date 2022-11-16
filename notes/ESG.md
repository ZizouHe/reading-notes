# ESG

- [绿色溢价与价值因子失去的 10 年](https://mp.weixin.qq.com/s/KYPhIbG2Jt4BtHl0XEGquA)
- [Pástor, Ľuboš, Robert F. Stambaugh, and Lucian A. Taylor. "Sustainable investing in equilibrium." *Journal of Financial Economics* 142, no. 2 (2021): 550-571.](https://www.sciencedirect.com/science/article/pii/S0304405X20303512)
- [Pástor, Ľuboš, Robert F. Stambaugh, and Lucian A. Taylor. "Dissecting green returns." *Journal of Financial Economics* 146, no. 2 (2022): 403-424.](https://www.sciencedirect.com/science/article/pii/S0304405X22001672)

## PST (2021) Theory

- [Pástor, Ľuboš, Robert F. Stambaugh, and Lucian A. Taylor. "Sustainable investing in equilibrium." *Journal of Financial Economics* 142, no. 2 (2021): 550-571.](https://www.sciencedirect.com/science/article/pii/S0304405X20303512)
- 均衡下，green firms 有负的 CAPM-alpha (**构造Green-Brown的多空投资组合，在CAPM模型下查看alpha**)：因为那些持有 brown firms 的投资者需要额外的补偿。换言之，绿色溢价平均而言为负。
- Green firms 可以提供对气候/环境风险的对冲。因此，当投资者对环境问题的担忧加剧时，green firms 会有更好的表现。更进一步，对环境问题的担忧，既可能来自于投资者路径（investor channel），也可能来自消费者路径（customer channel）。投资者路径指一段时期内环境问题风险的上升超出了投资者的预期，green firms 恰好在此时可以提供有效的对冲，从而表现更好；而消费者路径则指终端客户对环境问题的担忧会促使他们更多地购买 green firms 的产品，从而使得这些企业的营收、利润等基本面改善，进而推动股价上涨，使得 green firms 表现更好。

## PST (2022) Empirical Results

- [Pástor, Ľuboš, Robert F. Stambaugh, and Lucian A. Taylor. "Dissecting green returns." *Journal of Financial Economics* 146, no. 2 (2022): 403-424.](https://www.sciencedirect.com/science/article/pii/S0304405X22001672)

- 在 2012 至 2020 的样本期间，green firms 的表现远好于 brown firms（8.2 年间，累计收益差异高达 174%）。据此构造的多空因子（GMB），月均收益为 0.65%（t=3.23），隐含的月度 Sharpe ratio 则高达 0.33。

- 按照市场因子+green因子的两因子模型，green因子溢价可以表示为
  $$
  \hat{f}_{g t}=\frac{g_{t-1}^{\prime} \tilde{r}_t^e}{g_{t-1}^{\prime} g_{t-1}},
  $$
  其中, $$\tilde{r}_t^e=r^e-\beta_{m, t-1} r_{m, t}$$ 为公司 $$i$$ 的 CAPM-alpha ( $$\beta_{m, t-1}$$ 基于过去 60 个月的数据来估计），$$g_{t-1}$$是本期开始前的green score。

- GMB（green-brown 多空）因子与绿色因子总体上还是非常相似的（相关性为 0.72）。

- 根据前述 PST 2021 的理论模型，当市场对环境问题的担忧显著上升时，green firms 会有正的已实现收益。PST 2022 采用了 Ardia et al. (2021) 构建的新闻媒体气候变化担忧指数（Media Climate Change Concerns index, MCCC）来度量市场对环境问题的担忧。回归结果表明，投资者对环境问题的担忧的 shock 的确对绿色溢价有显著的影响。尤其值得注意的是，投资者对环境问题担忧 shock 的反应呈现出显著的滞后性：当月的 shock 对绿色溢价的影响虽然为正，但不显著；相反，前一月的 shock 的影响在统计和经济意义上都十分显著。这表明投资者对环境问题相关信息的反应是不够及时、理性的。

- 绿色因子的确可帮助解释价值因子过去近 10 年间的低迷表现；动量因子有显著的 CAPM-alpha，但这一 alpha 可以被绿色因子所解释。

- 价值股中包含大量 brown firms；相反，成长股包含大量 green firms，而成长又与动量紧密相关。由于样本期间市场对环境问题的担忧持续攀升，使得绿色因子获得了显著为正的已实现收益，进而使得价值因子表现糟糕。根据上述分析，随着人们对环境问题的担忧逐渐回落，绿色溢价迟早要回归其期望收益水平（为负）。相应地，价值因子回归正常也可以期待。
