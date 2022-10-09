# Momentum

- [给你的动量选股策略加点“料”](https://zhuanlan.zhihu.com/p/40468929)
- [PEAD, R.I.P.? PEAD.txt 来代替](https://zhuanlan.zhihu.com/p/400510484)
- [Da, Zhi, Umit G. Gurun, and Mitch Warachka. "Frog in the pan: Continuous information and momentum." *The review of financial studies* 27, no. 7 (2014): 2171-2218.](https://academic.oup.com/rfs/article-abstract/27/7/2171/1578455)
- [Bali, Turan G., Nusret Cakici, and Robert F. Whitelaw. "Maxing out: Stocks as lotteries and the cross-section of expected returns." *Journal of financial economics* 99, no. 2 (2011): 427-446.](https://www.sciencedirect.com/science/article/abs/pii/S0304405X1000190X)
- [Meursault, Vitaly, Pierre Jinghong Liang, Bryan Routledge, and Madeline Scanlon. "PEAD. txt: Post-Earnings-Announcement Drift Using Text." *Available at SSRN 3778798* (2021).](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3778798)

## 寻找高质量动量

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

## 解释动量

1. 当好的盈利消息接二连三出现时，会引起投资者的过度反应，因为他们会出现 representative bias，过度看中最近发生的这些连续的利好消息、并把这种预期外推到对公司未来股价的预测上；一旦未来的盈利没有达到预期，就会引起他们的恐慌，造成股价的下跌，这恰恰是成长投资（growth investment）的特点。
2. 盈余动量PEAD：当好的盈利消息离散的、非连续的出现时，投资者会对它们反应不足。这时投资者会出现 conservatism bias（保守主义）。他们会对这个利好持怀疑态度、不情愿更新他们对于该公司基本面的认知，这导致他们无法有效的对股价做出调整。随着时间的推移，当该公司又逐渐出现新的盈利利好时，其股价才会慢慢对其新的基本面反映到位，这就是动量投资。Bernard 和 Thomas 于 1989 提出了盈余动量现象（post-earnings-announcement drift，PEAD），也是投资者对利好消息反应不足的体现、符合上面这种解释。
3. 有限套利：交易动量策略最大的套利风险是由于动量策略在短期相对于基准指数的弱势表现而造成的职业风险（career risk）。职业风险产生的原因是，市场上的资金委托专业机构代表他们管理自己的资本。不幸的是，这些资金大多都是 short-sighted performance chasers，他们往往仅根据短期相对于基准的表现来评估基金经理的业绩。这让基金经理于进退两难的局面。一方面，基金经理希望利用错误定价机会交易动量策略，因为长期来看这么做的期望收益能够战胜基准；但另一方面，他们这样做的前提是，利用错误定价在短期不会威胁到他们手中的资金 —— 投资者不会因为业绩短期跑输基准而撤回资金。

动量策略如下的特点：

1. 动量策略在短期可能会（大幅）跑输市场，因此并不适合所有人（资金）；
2. 长期来看，动量策略会战胜市场。对于那些过程驱动、以长期盈利为目标（而忽视短期波动）、能够严格遵守交易纪律的投资者来说，动量策略值得配置。

## PEAD.txt

Meursault et al. (2021) 使用 earnings call 代替传统的 earnings number，将 PEAD 延伸，提出了 PEAD.txt。实证数据表明，PEAD.txt 的异常超额收益几乎是 PEAD 的两倍。

顾名思义，PEAD.txt 就是文本版的 PEAD。为了研究它，Meursault et al. (2021) 仿照传统 SUE 提出了 SUE.txt。简单的说，该文将 earnings call 中的 presentation 和 Q&A 环节区分对待，使用两部分的词频作为特征，使用 earnings call 下一个交易日的异常收益作为标签，使用滚动窗口进行有监督学习。

Meursault et al. (2021) 把词汇聚类到不同的段落组中，并给段落组赋予了有财务含义的类别（包括 Financial accounting，Global economics，Operations and marketing 以及 Strategy；每个大类下又有细分小类），从而考察不同财务类别对 SUE.txt 的贡献。

从结果不难看出，贡献最大的是 metrics FIN 类别，它对应的是财务数据。这也许并不意外，但其他高贡献 —— 包括 segment performance（segment OPE），公司前景展望（forward FOR）以及公司策略（gen. strategy STR）—— 也对找到超预期的公司贡献很高。这就是在财务数据本身之外，通过研究 earnings call 能够得到的增量信息。

