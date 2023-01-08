# Behavioral Finance: an Introduction

- [让你投资亏钱的 15 个“偏差”](https://zhuanlan.zhihu.com/p/38293254)
- [投资中的 N 种认知偏差，总有一款打败你](https://zhuanlan.zhihu.com/p/48155082)

## Prospect Theory

- [前景理论](https://zhuanlan.zhihu.com/p/38526672)
- [Kahneman, Daniel, and Amos Tversky. "Prospect Theory: An Analysis of Decision under Risk." *Econometrica* 47, no. 2 (1979): 263-292.](http://3xfund.com.cn/images/article008.pdf)

1. 价值函数中价值的衡量由两个因素决定：变化的初始状态 (称作参考点) 以及变化的幅度。
2. 当结果为正收益时，价值函数为结果的凹函数；当结果为负收益时，价值函数为结果的凸函数。并且亏损部分价值函数的增长快于收益部分的增长。
3. 权重 w(p) 是结果的产生概率 p 的函数，但它不是概率。它衡量的是每个结果对其所在的选项的影响，而非仅仅是该结果发生的可能性。
   - 如果一个结果产生的概率非常小 (微乎其微) ，人们往往容易放大这种可能性。
   - 但同时对于 $$0<p<1, w(p)+w(1-p)<1$$. 函数$$w(p)$$ 在概率 $$p$$ 为 0 和 1 的时候是不连续的，是突变的。

## Mental Accounting Theory

- [心理账户理论](https://zhuanlan.zhihu.com/p/38610013)
- [Thaler, Richard. "Mental accounting and consumer choice." *Marketing science* 4, no. 3 (1985): 199-214.](https://pubsonline.informs.org/doi/abs/10.1287/mksc.4.3.199)

1. 决策评估
   - 前景理论
   - 在决定一笔交易的效用时，必须考虑两个方面：获取效用 (acquisition utility) 和交易效用 (transaction utility)。前者取决于收到的物品或服务相对于支出的价值 (主观价值)，而后者仅仅取决于人们对这笔交易的感知价值 (相对于参照价格的感知价值)。
2. 心理账户 mental accounts
   - 人们在消费时，不同的支出类别会有不同的预算；且这些预算的周期也不同。
   - 很多小额的日常消费不会被记账。
   - 心理账户理论指出，最佳礼品应该是比被赠与人平日消费的商品稍微奢侈一些的东西。
   - 收入账户专款专用
   - 财富也根据支出意愿从高到低划分在不同的账户之中
3. 决策归类
   - 之前的收益可以刺激同一个账户内的风险偏好；只有当眼前的赌局有回本的可能时，之前的亏损才能激发风险偏好。
   - 人们在做决策 (特别是投资决策) 时过度重视近期的得失而无法从全局考虑，从而导致非最优的决策。

## An Overview of Behavioral Finance

- [听 Richard Thaler 讲行为金融学的知识框架](https://zhuanlan.zhihu.com/p/64917245)
- [Barberis, Nicholas, and Richard Thaler. "A survey of behavioral finance." *Handbook of the Economics of Finance* 1 (2003): 1053-1128.](https://www.sciencedirect.com/science/article/abs/pii/S1574010203010276)

行为金融学的两大支柱：有限套利和心理学

- 有限套利

  有效市场假说不成立，背后的原因是有限套利 (limits to arbitrage)。当 mispricing 出现时，理性投资者想要利用它赚取收益时要面对以下三个风险，这些风险使得理性投资者无法做到充分套利。

  - 基本面风险 (fundamental risk) ：套利者在买入套利股票时暴露在它的基本面风险之中。一旦发生基本面负面信息，将会造成该股票的继续下跌，给套利者带来亏损。
  - 噪音交易者风险 (noise trader risk) ：当噪音交易者的非理性加大了 mispricing 时，由于套利策略的持续亏损，管理人将面临巨大的资金赎回压力，这将迫使他们卖掉手中的头寸，无法等待价格的回归。短期业绩惨淡造成资金被赎回正是管理人面对的职业风险。这是噪音交易者风险的直接结果。
  - 实施成本 (implementation costs) ： 
    - 建立套利头寸需要付出的成本：手续费、交易价差、价格冲击以及做空需要付出的费用
    - 寻找 mispricing 所付出的成本：由于内在价值难以确定，因此判断价格是否等于内在价值本身就是非常困难的。

- 心理学

  - 信念，下列基本都在 [让你投资亏钱的 15 个“偏差”](https://zhuanlan.zhihu.com/p/38293254)、[投资中的 N 种认知偏差，总有一款打败你](https://zhuanlan.zhihu.com/p/48155082) 中有介绍
    - 过度自信 (overconfidence) 
    - 乐观主义 (optimism) 
    - 保守主义 (conservatism) 
    - 确认偏误 (confirmation bias) 
    - 锚定效应 (anchoring) 
    - 可得性偏误 (availability bias) 
    - 代表性偏误 (representativeness) 
  - 偏好
    - 前景理论：[前景理论](https://zhuanlan.zhihu.com/p/38526672)
    - 模糊厌恶

用行为金融原理解释市场现象：

- 股权溢价之谜：美国股市平均回报约为 7%，而政府债券的回报率不足 1%。面对如此大的差异，债券投资者的比例却远超股票投资者。
  - 前景理论的价值函数是损失厌恶的
  - 不成熟的、非理性的投资者倾向于频繁查看自己的股票是赚了还是亏了。
- [Barberis, Nicholas, Andrei Shleifer, and Robert Vishny. "A model of investor sentiment." *Journal of financial economics* 49, no. 3 (1998): 307-343.](https://www.sciencedirect.com/science/article/pii/S0304405X98000270)
  - 当超出预期的盈利消息出现时，投资者因保守主义而愿意相信自己的先验判断，而对这个新息反应不足。他们会对这个利好持怀疑态度、不情愿更新他们对于该公司基本面的认知，因此新息无法有效的反映在股价上。随着时间的推移，当该公司又逐渐出现新的盈利利好时，其股价才会慢慢对其新的基本面反映到位，而这正好造就了 momentum 异象和**盈余动量现象** (post-earnings-announcement drift，PEAD, [Bernard and Thomas, 1989](https://www.jstor.org/stable/2491062)) 。
  - 当好的盈利消息接二连三出现时，会引起投资者的过度反应并陷入代表性偏误的误区。这意味着他们过度看中最近发生的这些连续的利好消息、并把这种预期错误的外推到对公司未来股价的预测上；一旦未来的盈利没有达到预期，就会引起他们的恐慌，造成股价的下跌，这会造成 long-term reversal 异象以及 value 异象。
- [Daniel, Kent, David Hirshleifer, and Avanidhar Subrahmanyam. "Investor psychology and security market under‐and overreactions." *the Journal of Finance* 53, no. 6 (1998): 1839-1885.](https://onlinelibrary.wiley.com/doi/full/10.1111/0022-1082.00077)
-  [Daniel, Kent D., David Hirshleifer, and Avanidhar Subrahmanyam. "Overconfidence, arbitrage, and equilibrium asset pricing." *The Journal of Finance* 56, no. 3 (2001): 921-965.](https://onlinelibrary.wiley.com/doi/full/10.1111/0022-1082.00350)
  - 投资者在处理私有信息时所容易产生的认知偏差。假设投资者对于某个上市公司做了大量深入研究。在这种情况下，他容易对自己的分析结果表现出过度自信。
  - 如果分析的结果认为该公司的基本面向好，他们就会大举买入该公司的股票。确认偏误会让他们在短期内仅仅关注与和自己分析结果相一致的公共信息，而忽略掉意见相左的信息，这就会造成 momentum 和 PEAD 这些现象。
  - 当股价被推高后，如果接连出现基本面变差的信息，这时价格就会发生下跌修正，从而造成 long-term reversal 以及 value 异象。

## Behavioral Finance in Asset Pricing

- [资产价格和交易量背后的行为金融学](https://zhuanlan.zhihu.com/p/78564724)
- [Barberis, Nicholas. "Psychology-based models of asset prices and trading volume." In *Handbook of behavioral economics: applications and foundations 1*, vol. 1, pp. 79-175. North-Holland, 2018.](https://www.sciencedirect.com/science/article/pii/S2352239918300010)

| 传统金融学         | 行为金融学                                                 |
| ------------------ | ---------------------------------------------------------- |
| 理性信念           | 过度外推 (extrapolation) 和过度自信 (overconfidence)       |
| 及时处理全部信息   | 认知限制 (cognitive limits)                                |
| 完全理性的决策偏好 | 前景理论 (prospect theory) 和模糊厌恶 (ambiguity aversion) |

**非理性信念**

- 外推信念 (extrapolative beliefs) ：当人们对未来做预测的时候，其预测值通常和当前数据正相关
  - 收益率外推：预测股票未来的收益率 (价格变化) 时，总偏好给近期的收益率更高的、且大于零的权重；这种集体的外推行为造成了市场中的以下行为：
    - **中期动量** (medium-term momentum) 和**长期反转** (long-term reversal) 、**截面上的价值效应** (Value Effect)
    - 市场整体 (非个股) 在时序上的高波动率以及收益率在一定程度上的可预测性
    - 泡沫 (bubbles) 
  - 基本面外推: cash flow 外推，即认为未来现金流变化率和近期现金流变化率正相关
    - 对未来现金流做出非理性外推时，会认为其在未来会按之前的增速继续增长从而买入该资产、造成价格提升。当未来现金流的增长率不符合外推的预期时，他们便会非常失望以至于开始抛售资产、造成其价格下跌，这边形成了一个先涨、后跌的周期
    - 造成中期动量、长期反转以及截面上的价值效应
- 过度自信 (overconfidence) : 越过度自信的人越倾向于去交易，产生**和基本面变化不相符的高交易量**
  - overprecision: 人们做判断时高估自己判断的准确性
  - overplacement: 总认为自己比别人的判断更加准确

**决策依据**

- 前景理论: 价值函数和权重函数，详见 [前景理论](https://zhuanlan.zhihu.com/p/38526672)

- 模糊厌恶: 详见 [听 Richard Thaler 讲行为金融学的知识框架 - 3.2节](https://zhuanlan.zhihu.com/p/64917245) 

**认知限制 (有限理性)**

- Inattention: 人脑对信息的分析处理能力是有限的，在任何给定的时刻，我们并不能处理所有的信息，而是偏好去应对最显著、最重要的信息
  - 典型的例子是 PEAD。由于人们对新的基本面信息反映不足，造成价格无法迅速对其反映到位，而是会在 earnings announcement 之后继续漂移，产生 PEAD
  - [DellaVigna and Pollet (2009 JoF)](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.2009.01447.x) 指出如果 earnings announcement 出现在星期五，随之而来的 PEAD 现象会更显著。它们猜测由于星期五临近周末，投资者的 inattention 比平时要更高，更无法对 earnings 做出足够的反映，造成 PEAD 显著
  - [Hirshleifer, Lim, and Teoh (2009 JoF)](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.2009.01501.x) 发现当多家上市公司同时发布财报时，PEAD 也会变得显著。这是因为投资者无法同时处理同时涌现的关于多家公司的大量新信息

- 分类思维 (categorical thinking)
  - 为了简化思维，投资者会把市场中的成千上万种资产分类，比如把股票按风格分成价值股、成长股、高质量股、小市值股等。**如此的分类让投资者在判断这些资产时，更多的考虑它们所处的类别，而非每个资产本身的基本面。这就造成了同类资产中显著的 co-movement。**
  - 对不同风格股票的外推造成了不同风格股票的波动，这就形成了我们看到的风格因子之间涨跌的差异，也由此派生出一门玄幻的配置诉求 —— 风格因子择时。
  - [Barberis, Shleifer, and Wurgler (2005 JFE)](https://www.sciencedirect.com/science/article/pii/S0304405X04001308) 提出，当一只股票入选 S&P 500 指数时，它的价格开始和其他成分股一起 co-movement。如果投资者是完全理性的，这种 co-movement 发生的唯一前提应该是该股票的基本面和其他成分股的基本面开始 co-movement；事实上，categorical-based co-movement 才是上述现象背后的原因。

