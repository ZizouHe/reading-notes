# Size and Value in China

- [Liu, Jianan, Robert F. Stambaugh, and Yu Yuan. "Size and value in China." *Journal of Financial Economics* 134, no. 1 (2019): 48-69.](https://www.sciencedirect.com/science/article/pii/S0304405X19300625)
- [中国版的 Fama-French 三因子模型](https://zhuanlan.zhihu.com/p/48728998)



1. Fama-French 三因子模型：市场因子 MKT，市值因子 SMB 和 价值因子HML
2. 本文改动：
   - Liu et al. (2018) 认为是中国市场特有的 IPO 监管造成的壳价值问题，造成了主流因子在 asset pricing 时的效果被破坏，他们将这个现象称为壳价值污染。中国股市中市值最小的 30% 的上市公司会受到壳价值污染的严重影响，造成 asset pricing 模型不能正确反映出股票截面预期收益率的差异。为了更好的研究 A 股的定价机制，必须“壮士断腕”，**抛弃这市值最小的 30% 的公司。**
   - 通过Fama-MacBeth regression（Fama and MacBeth 1973）比较 EP(Earnings-to-Price)，BM(Book-to-Market)，AM(Assets-to-Market) 以及 CP(Cash flow-to-Price)这四个价值因子指标的效果。**最终选择 EP 来构建价值因子**。
   - 三因子模型可以解释中国市场中的 size、value、profitability、volatility 异象。三因子模型也有它的极限 —— 它无法解释 reversal 和 turnover 异象。
   - 在三因子的基础上加入了第四个因子 —— **换手率因子 PMO（Pessimistic Minus Optimistic）**，核心逻辑是低换手率的因子比高换手率的因子能获得更高的收益。这便得到了中国市场的四因子模型。新加入的 PMO 有效的填弥补了三因子的不足，使得被研究的十个异象均能被四因子模型很好的解释。