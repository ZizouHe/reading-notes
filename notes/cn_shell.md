# Chinese Stock Market Shell Value

- [Lee, Charles, Yuanyu Qu, and Tao Shen. "Reverse mergers, shell value, and regulation risk in Chinese equity markets." (2017).](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3038446)
- [屈源育, 沈涛, and 吴卫星. "壳溢价: 错误定价还是管制风险?." *金融研究* 453, no. 3 (2018): 155-171.](http://www.jryj.org.cn/CN/article/downloadArticleFile.do?attachType=PDF&id=447)
- [量化壳价值](https://zhuanlan.zhihu.com/p/46386808)



1. 作为“壳”的上式公司的壳价值的计算公式为：
   $$
   \mathrm{SV}=(\mathrm{MVCE} \times \mathrm{SFS})-\mathrm{OC}.
   $$
   其中 SV 代表壳价值（Shell Value），MVCE 是 Market Value of Combined Entity，SFS 为借壳后原壳公司的股份所有权，OC 是在借壳过程中壳公司所有者付出的资本。

   - SFS 的公式为：
     $$
     \mathrm{SFS}=(\mathrm{S}-\mathrm{TS}) /(\mathrm{S}+\Delta \mathrm{S}).
     $$
     其中，S 是借壳前壳公司的股本，$$\Delta \mathrm{S}$$ 是在借壳上市过程中增发的、给予未上市公司的股本。如果$$\Delta \mathrm{S}$$的股本数不足以使未上市公司对壳公司拥有控股权，壳公司会将一部分股本，记为TS，转给未上市公司。在这种情况下，壳公司最终的股本是S – TS。因此借壳上市之后，壳公司的控股权为 $$(S - TS) / (S + \Delta S)$$，即 SFS。

   - 对于 MVCE，Lee et al. (2017) 考虑了三种计算方法：
     $$
     \begin{aligned}
     MVCE &= PE_{pre} \times E+W \\
     MVCE &= PE_{ind} \times E+W \\
     MVCE &= P_{Day1} \times (S + \Delta S)
     \end{aligned}
     $$

     - 前两种方法中，E 是未上市公司的 earning forecast；W 是壳公司和未上市公司的净资产总和。这两种方法的区别在于市盈率 PE 的计算。在第一种方法中，PE_pre 代表了 peer-based PE ratio，它是壳公司自己根据同类公司的 PE 估计出来的市盈率；而在第二种方法中，PE\_ind 代表了 industry-based PE ratio，它是壳公司所在行业的全部公司的平均市盈率。通常来说，PE\_pre 大于 PE\_ind。

     - 在一个完整的借壳上市过程中，壳公司首先会被停牌，随后会出现和它有关的资产重组的公告（不涉及任何细节）。在三到四个月后，壳公司会复牌，并伴随最初的 reverse merger 的提案。由于 reverse merger 对壳公司是极大的利好，复牌后它的股票通常会经历几个涨停，P\_Day1 代表了复牌后第一个非涨停的交易日的收盘价，它表示着市场已经完全 priced in 这个潜在的 reverse merger。$$P_{Day1} \times  (S + \Delta S)$$ 就是第三种 MVCE 的计算方法。

     - 相对前两种方法，第三种计算 MVCE 的方法最为保守。这是因为最初的提案需要经过股东和董事会的批准得到最终的提案，而最终的提案还要经过证监会的审批，这其中存在很高的失败风险。因此，P\_Day1 反映出来的壳价值是存在折价的，这就是第三种方法相对保守的原因。

2. Lee et al. (2017) 提出了一个 Expected Shell Value to Market (ESVM) 指标作为壳价值因子。顾名思义，它是预期壳价值和市值之比。Expected Shell Value 是成为壳的概率与 Shell Value 的乘积，ESVM是ESV divided by each firm’s market equity。

   - 成为壳的概率是用 市值、利润率、退市风险(ST)、所有权集中度等几个指标做自变量，进行logistic regression拟合的模型进行预测得到的

   - Shell Value 是 average prevailing shell value

   - 在屈、沈 (2018) 中，成为壳的概率考虑了额外的ROA、主营业务收入增长率、宏观政策下IPO拒绝率以及过去12个月的超额收益率等变量进行logistic regression

   - 在屈、沈 (2018) 中，SV 是一个根据借壳上市交易数据构建的壳价值指数：
     $$
     S V_{i t}=\exp \left(-4.421+3.118 \times \ln M V_{i t-1}-0.187 \times\left(\ln M V_{i t-1}\right)^{2}-0.592 \times S O E_{i t-1}\right),
     $$
     其中 MV是市值，SOE是是否为国企的dummy，是为1。

3. 屈、沈 (2018) 探讨了壳溢价的来源：

   - 假设1：市场存在套利成本 (错误)
     - 参考 Campbell et al. (2008)、Wang and Yu (2013) 等文献的做法，选取机构投资者持股、分析师覆盖率、异质波动率以及非流动性 4 个指标衡量套利成本。
       - Institutional Holdings:机构投资者持股比例。D'Avolio(2002) 发现，机构投资者持股比例越低的股票，越难融到券，因此越难以卖空，套利成本越大。
       - Analyst Coverage: 分析师覆盖率。分析师覆盖率越低的股票，投资者关注度越低，越可能发生反应不足的现象(Hong and Stein, 1999)，套利成本越大。
       - IVOL: 异质性风险。Shleifer and Vishny (1997)预测异质波动率会阻碍套利行为，Pontiff(2006) 的研究结果表明异质波动率是套利者面临的最大的套利成本。因此，IVOL 越大,套利成本越大。
       - Illiquidity : 非流动性指标 ( Amihud, 2002)。Illiquidity 值越大，说明单位订单流的价格影响越大，套利者的套利成本越大。
     - 由于套利成本的度量指标与股票规模有很高的相关度，为了避免分组结果受规模效应的影响，屈、沈 (2018) 参照 Hong et al. (2000)、Campbell et al. (2008) 等文献的做法，取上述变量对股票相对规模回归的残差作为对应套利成本的代理变量。
     - 壳溢价在高套利成本和低套利成本的股票中都显著存在,说明错误定价对壳溢价的解释能力非常有限。
   - 假设2：市场存在投资者情绪 (错误)
     - Stambaugh et al. (2012)发现大多数异象在高投资情绪时期更为显著、溢价更大，并且异象对冲组合的收益主要来自于卖空组合的负收益。这是因为在高投资者情绪时期卖空变得更为困难，套利者难以通过卖空手段套利，导致卖空组合过高估值严重。
     - 与大多数异象的不同，壳溢价在低投资者情绪时期显著,而在高投资情绪时期不显著，并且低投资者情绪时期的壳溢价远远大于高投资者情绪时期的溢价。
   - 假设3：IPO管制与壳溢价 (正确)
     - 在现行的 IPO 审核制下,证监会主要通过控制 IPO 企业审批数量的方式控制 IPO 节奏，实现对资本市场的管制。证监会不定期召开发审委员会议,对上会的 IPO 申请进行审 核,并实时公布审核结果。我们在月度频率上汇总了当月上会的 IPO 申请审核结果,并计 算了发审委每月对 IPO 申请的拒绝率。
     - 当 IPO 暂停时,借壳成为企业上市的唯一途径，上市公司被借壳的概率大幅增加，期望壳价值上升，从而导致壳溢价的大幅升高。
   - 假设4：高管制风险
     - 根据理性资产定价模型，股票的超额回报率来自于系统性风险补偿。 如果壳溢价反映了管制风险,那么壳溢价应该是对投资者承受管制风险的补偿。具体来说，当面临管制政策风险(不确定性)时，风险厌恶者会倾向于出售手中的壳股票，壳股票的当期价格下跌，从而导致政策风险兑现后壳股票会有一部分超额收益,这部分超额收益 (壳溢价) 就是对承受政策风险的投资者的风险补偿。
     - 用 EPU 指数( Baker et al., 2016) 作为管制政策不确定性的代理变量。EPU 指数记录了每个月关于中国经济政策不确定性新闻的频率，这些新闻涵盖的主题包括货币、 财政、监管、改革、税收、贸易等等。 $E P U$ 的优势在于其反映的政策不确定性是外生的、实时的，因此,当期的 EPU 越高，代表当期的政策不确定性越高。
     - 当面临管制政策不确定性时,风险厌恶投资者会倾向于出售暴露于管制风险的壳股票，转向相对安全的非壳股票，进而导致当期壳股票价格下跌非壳股票价格上升，政策风险兑现后壳股票有正的超额回报，而非壳股票有负的超额回报。因此，壳溢价就是对承受政策风险的投资者的风险补偿。

​	