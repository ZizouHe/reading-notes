# Quant Machine Learning

## Backtesting

### Scientific Backtesting

- [科学回测中的大学问](https://zhuanlan.zhihu.com/p/38256574)

1. 超参数
   - 对于量化投资策略来说，超参数的调优除了从数学角度（如策略的 Profit/Loss 曲线）考量外，还需要考虑超参数本身是否具有清晰的业务含义以及是否适合策略的使用者。
2. 训练集和测试集
   - 由于市场流动性环境和宏观经济的变化，以及波动率聚类等特点，投资品价格数据的短期相关性比较高，而在不同的历史时期往往反应出不同的特点。如果训练集和测试集的数据代表了不同的市场状态，那么它们之间的交易数据就没有多少共性可言。
   - 一个经科学回测过的策略必须能够捕捉市场的某种特点。只要这个特点有明确的业务支持而非数据挖掘的产物，那么针对这个特点构建及优化策略参数时，是分别使用训练、测试集，还是使用所有数据来整体优化，这并不重要。

3. 各种偏差

   - 优化偏差：指的是通过不断地增加参数个数，直到策略的收益曲线在回测中表现的非常好。

   - 通过考察参数平原（parameter surface）也可以检查过拟合。将策略表现的指标（比如收益率或者最大回撤）画成参数的函数就是参数平原。对于一个好的策略，在微调参数取值时，它的表现应该比较稳定，参数平原应该十分光滑。

   - 前视偏差：指的是错误的使用了未来数据。

   - 幸存者偏差：一般针对选股策略而言，指的是在数据集中错误忽略退市的股票。在构建选股策略时，我们有时会下意识的仅考虑在整个回测期内都存在（"活着"）的股票，而忽略掉在回测期内退市的股票。这么做会提高提高策略在回测期内的表现。

4. 交易费用

   - 手续费
   - 滑点：在交易信号产生到交易实际执行之间价格的（不利）变动造成的额外费用。
     - 这对于中、高频策略额外重要。这些策略捕捉日内转瞬即逝的交易机会
     - 回测中可以考虑的是按照每个 bar 的收盘价来交易。这个 bar 的频率可以很高，比如分钟级，但一定是按照它的 close 价格来成交，而非在这个 bar 的形成过程中信号触发的瞬时价格。或者在回测时考虑信号出现后一段时间内按照 TWAP（时间平均）成交。
   - 冲击成本：投资品流动性不足带来的额外交易费用
     - 如果投资品的流动性不足，那么为了完成交易，策略就势必会 walk the book，直到完成我们的交易量需求。这个冲击成本和每笔交易时的具体流动性有关，因此回测中难以准确估计。
     - 能否有效的控制交易费用直接关系到一个策略的资金容量。资金量（交易量）越大，完成交易所需的时间越长，而交易成本（及不确定性）随交易时间呈非线性增长。
     - 由于交易量巨大，华尔街的大型金融公司都会针对市场微观结构（即 order book 上买单、卖单出现的 dynamics）来建模，以此构建交易模型（注意是交易模型，而不是投资策略模型），从而尽可能的降低交易成本。

5. 回测并非无所不能

   - 对于任何一个策略，几乎可以确定的是它在回测中的表现是其在实盘中表现的上限（比如以最大回撤而言，很多经验都指出，实盘的最大回撤差不多是回测中最大回撤的 2 倍)
   - 任何量化策略都需要定期进行事后评价，比较它在样本外和回测期内的表现，评判它是否仍然有效，或者根据实盘的反馈进行调整
   - 一个经过科学回测的量化投资策略仍然是投资中的利器，它刻画了市场的某种具备清晰业务逻辑支撑的特性，并假设该特性在未来会重复，从而捕捉这些机会。

### Backtesting in Machine Learning

- [机器学习时代的回测规程](https://zhuanlan.zhihu.com/p/66721234)
- [Arnott, Rob, Campbell R. Harvey, and Harry Markowitz. "A backtesting protocol in the era of machine learning." *The Journal of Financial Data Science* 1, no. 1 (2019): 64-74.](https://jfds.pm-research.com/content/1/1/64.short)

### The Probability of Backtest Overfitting

- [Bailey, David H., Jonathan Borwein, Marcos Lopez de Prado, and Qiji Jim Zhu. "The probability of backtest overfitting." *Journal of Computational Finance, forthcoming* (2016).](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf)
- [美丽的回测 —— 定量计算过拟合概率](https://zhuanlan.zhihu.com/p/47440419)

假设一共有 $$N$$ 组不同的参数构建的策略，令$$n^*$$代表样本内表现最好的那组参数 (最好意味着样本内SR夏普率最高，或者其他类似的指标)，令 $$SR_{OOS}(n)$$表示第 $$n$$ 组参数在样本外的夏普率 (下标 OOS 意为 out of sample)，令$$ME[SR_{OOS}]$$ 表示所有 $$N$$ 组参数在样本外夏普率的中位数；Probability of Backtest Overfitting（PBO）的定义如下：
$$
\operatorname{PBO} \equiv \operatorname{Prob}\left(\mathrm{SR}_{\mathrm{oos}}\left(n^{\star}\right)<\mathrm{ME}\left[\mathrm{SR}_{\mathrm{oos}}\right]\right).
$$
由于样本内存在过拟合，因此样本内的最优参数不一定是样本外最好的。回测中过拟合的概率 PBO 的定义为样本内最优参数 $$n^*$$ 在样本外的夏普率小于所有 $$N$$ 组参数在样本外夏普率的中位数的概率。

下面介绍计算 PBO 的框架。它的名字叫 Combinatorially-Symmetric Cross-Validation（组合对称交叉验证，简称 CSCV）。假设我们一共测试了 $$N$$ 组参数，回测期长度为 $$T$$。CSCV 由以下步骤构成：

1. 首先在回测期内使用 N 组参数各自跑策略，得到每组参数在 T 期的收益率序列，以此构建一个 $$T \times N$$ 阶矩阵 M，M 的每一列代表为某组参数 n 的 T 期收益率序列。

2. 将 M 矩阵按行划分成 S 个互不相交的 $$T/S \times N$$ 阶子矩阵。例如，假设原始的 $$T = 1000$$ 期，则可以取 $$S = 10$$，并把 M 划分成 10 个子集，每个子集为 $$100 \times N$$ 阶矩阵。

3. 从全部 S 个子矩阵中，取出 $$S/2$$ 个，令 $$C_s$$ 代表所有可能的组合。举例来说，如果 $$S = 10$$，则从 10 个子集中取出 5 个，一共有 252 种组合方法，$$C_s$$ 就是这 252 种组合的合集。

4. 对 $$C_s$$ 中的每一个特定组合 c，进行如下操作：

   - 将 $$c$$ 包含的子矩阵拼在一起构成训练集 $$J$$，它是一个 $$T/2 \times N$$ 阶矩阵；

   - 将全部 $$S$$ 个子矩阵中不被 $$c$$ 包含的子矩阵拼在一起构成测试集 $$J_c$$ ，它也是一个 $$T/2 \times N$$ 阶矩阵；

   - 在训练集 J 矩阵中，计算每一列收益率序列的夏普率，它们之中夏普率最大的对应的策略 $$n^*$$ 为样本内的最优策略；

   - 在对应的测试集 $$J_c$$ 矩阵中，计算每一列收益率序列的夏普率，并求出 $$n^*$$ 这组参数在样本外的相对排名 $$w$$，$$w$$ 的取值在 0 到 1 之间，1 意味着样本内最优的策略 $$n^*$$ 在样本外同样最优。

   - 定义 logit 变量如下：
     $$
     \lambda=\ln \frac{w}{1-w},
     $$
     由定义可知，如果 $$n^*$$ 在样本外的表现等于所有参数在样本外夏普率的中位数，则 $$w = 0.5$$，而 $$\lambda = 0$$。

5. 上一步后会得到 $$\lambda$$ 的经验分布 $$f(\lambda)$$, 由此就可以求出 PBO :
   $$
   \mathrm{PBO}=\int_{-\infty}^{0} f(\lambda) d \lambda.
   $$
   通过考察 PBO 的大小，就能够定量的评价一个策略是否靠谱：真正有效的策略的 PBO 应该较小。

CSCV 具有以下优点：

1. CSCV 保证了训练集和测试集同样大小，从而使得样本内外的夏普率具有可比性。
2. 由于考虑了全部的组合，任何一个被用做训练集的组合都在之后反过来被当作测试集（反之亦然），这保证了训练集和测试集的数据是对称的，因此夏普率在样本外的降低只可能来自过拟合。
3. CSCV 将整个 T 期数据划分成长度为 $$T/S$$ 的 S 个子集，而非随机的从 T 期内选出一定长度的数据，这保证了策略收益率的时序相关性。
4. 整个求解 PBO 的过程是 model-free 以及 non-parametric 的；它得到 $$\lambda$$ 的经验分布 $$f(\lambda)$$，进而计算出过拟合的概率，不需要对 PBO 的模型或者参数做任何假设。



### 机器学习与资产定价: Facts and Fictions

- [机器学习与资产定价: Facts and Fictions](https://zhuanlan.zhihu.com/p/638705301)

## Machine Learning

### Some Methods

- [用 K-means 聚类做市场状态分析](https://zhuanlan.zhihu.com/p/43872533)
- [机器学习驱动的基本面量化投资](https://mp.weixin.qq.com/s?__biz=MzUxNzY0NjU3Mw==&mid=2247484256&idx=1&sn=0789b472815f8ebaff87debf47e008f9&chksm=f995b2e2cee23bf440f8e007f4cdb10388c071ca0555cf532a1948d4c2e55ab3a28292eac95e&scene=178&cur_album_id=1506150283578556420#rd)
- [李斌, 邵新月, and 李玥阳. "机器学习驱动的基本面量化投资研究." *中国工业经济* 8 (2019): 61-79.](http://www.cqvip.com/qk/93800a/20198/7002727845.html)
- [因子投资中的机器学习](https://mp.weixin.qq.com/s?__biz=MzUxNzY0NjU3Mw==&mid=2247484568&idx=1&sn=986ec4bed9bc5c72409cdc3899679bc5&scene=21#wechat_redirect)
- [Gu, Shihao, Bryan Kelly, and Dacheng Xiu. "Empirical asset pricing via machine learning." *The Review of Financial Studies* 33, no. 5 (2020): 2223-2273.](https://academic.oup.com/rfs/article-abstract/33/5/2223/5758276)
- [海通证券选股因子系列研究：从加权 IC 到机器学习：高频因子多头失效的修正](https://www.htsec.com/jfimg/colimg/upload/20200323/26211584942439271.pdf)

### Which Characteristics?

- [Which Characteristics?](https://mp.weixin.qq.com/s?__biz=MzUxNzY0NjU3Mw==&mid=2247484364&idx=1&sn=fa2f763f6ec767b2090a94bb48a750bd&chksm=f995b24ecee23b58fb31868e2c1cec676ec1d445d2fb4db3ed2a0a432becbb96bfa2a4ab34c3&scene=178&cur_album_id=1506150283578556420#rd)
- [Han, Yufeng, Ai He, David Rapach, and Guofu Zhou. "What firm characteristics drive us stock returns." *Available at SSRN* (2018).](https://economics.indiana.edu/documents/workshop-papers/fall2018/what-firm-characteristics-drive-us-stock-returns.pdf)

为了解决多元线性回归可能的多重共线性和由此导致的预测能力不足，HHRZ (2018) 引入了其常用的 forecast combination (FC) 方法。具体而言，在 t 月末，对于每一个公司特征，拟合下述截面一元回归模型：
$$
r_{i, t}=a_{j, t}+b_{j, t} z_{i, j, t-1}+\varepsilon_{i, t},
$$
其中，$$r_{i, t}$$ 为 $$t$$ 月末股票 $$i$$ 的收益，$$z_{i, j, t−1}$$ 为 $$t - 1$$ 月末股票 $$i$$ 的第 $$j$$ 个特征。估计方法则采用 OLS 或 WLS。

然后，代入 $$t$$ 月的公司特征，得到对 $$t+1$$ 月的股票收益的预测：
$$
\hat{r}_{i, j, t+1 \mid t}^{j}=\hat{a}_{j, t}+\hat{b}_{j, t} z_{i, j, t}.
$$
最后，对不同特征的预测值取平均得到最后的预测：
$$
\hat{\boldsymbol{r}}_{i, t+1 \mid t}^{\text {Mean }}=\frac{1}{J_{t}} \sum_{j=1}^{J_{t}} \hat{r}_{i, j, t+1 \mid t}^{j}.
$$
除了直接对全部预测值取平均外，HHRZ(2018) 还考虑了以下三种方法：

- Trimmed-mean: 剔除掉最大和最小 5% 的预测结果，再取均值。
- 线性机器学习算法 LASSO（或 elastic net）

在实验中，HHRZ(2018)考虑了 FC方法的预测值/传统多元线性回归方法的预测值 与 实际return进行Fama-Macbeth 回归的结果，结果显示

- 2003 年之后，用FM计算的t统计量显示，传统方法失效了，但 FC 方法的显著性则几乎不受影响，仍然高度显著。
- 在所有设定下，FC 方法的 R 方都显著高于传统方法，表明其确实有更好的预测能力。
- 传统多元线性回归方法的系数远小于 1 ，这表明股票的真实收益远低于模型预测收益 (真实收益率 = 系数*预测值)，模型的过拟合风险较大。而FC方法的FM回归系数都大于1。
-  LASSO 和 elastic net 可以自动筛选显著的解释变量，超过 40% 的时间显著的特征，一共有 9 个。按照 McLean and Pontiff (2016) 和 GHZ (2017) 的分类方法，其中 5 个属于基本面因子，2 个属于事件类因子，1 个属于市场类因子，最后一个则不属于他们的分类。最后这个因子是 sin （是否从事有害业务），即公司的主营业务是否属于烟草、酒类或赌博，这是一个典型的 ESG (Environmental, Social, and Governance) 因子。