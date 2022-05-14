# Out of Sample Predictability

- [所有历史数据都是样本内](https://mp.weixin.qq.com/s?__biz=MzIyMDEwNDk1Mg==&mid=2650878785&idx=1&sn=6df2c7e02b2f3cf0e1482d6319988c79&chksm=8c2482d6bb530bc0e25735e7df8a3885d77c67f238f3c055e7e8b73144d6ffc1c7aa80393956&scene=21#wechat_redirect)

## High Dimensional Learning 

- [Martin, Ian WR, and Stefan Nagel. "Market efficiency in the age of big data." *Journal of Financial Economics* (2021).](https://www.sciencedirect.com/science/article/pii/S0304405X21004566)

- [False In-Sample Predictability?](https://zhuanlan.zhihu.com/p/382885396)

**Rational Expectation**

If investors knew the coefficients of the predictive model, they could form expectations of cash-flow growth, and hence price assets, in such a way that returns would not be predictable in the cross-section. This is the conventional rational expectations (RE) equilibrium that is the foundation for typical market efficiency tests. Similarly, if the parameter dimension $$d$$ is small relative to N (the number of individual stocks), investors could estimate the parameters of their cash-flow forecasting model with great precision, leading to asset prices that are close to those in the RE equilibrium.

**High-dimensional Learning**

从直观上来理解，这是因为投资者高维学习问题会导致均衡状态下资产的价格和理性预期情况下相比出现偏差；该偏差的存在将造成事后（ex post）从计量经济学家的视角来看，已实现收益率不再随机，而是包含了一部分可预测的成分；因此当人们事后用统计检验分析变量和收益率的关系时，会误以为某些变量对收益率有预测性。在作者的假设中，参数向量 $$g$$ 满足多元正态分布：
$$
g \sim \mathcal{N}\left(0, \frac{\theta}{J} I_{J}\right), \; \; g \in \mathbb{R}^J.
$$
其中 $$\theta$$ 是一个常数, $$I_{J}$$ 是 $$J$$ 阶单位矩阵。**这个假设的核心是 $$g$$ 的方差和 $$J$$ (变量的个数) 成反比。**它对模型尽可能贴合现实世界至关重要。这是因为上述假设保证了无论 $$J$$ 怎么变，模型中的信噪比都是不变的。如果没有这个约束，则随着使用的变量越来越多， $$r_{t+1}$$ 中可解释的部分将会越来越大，远超过噪音 $$e_{t}$$，这显然是不切实际的。以上就是关于资产基本面的建模。在这个假设下，$$J$$ 相当于股票数量变大会使得估计产生不可忽略的误差，从而偏离理性预期模型。

## 因子样本外表现为什么变差？

- [因子样本外表现为什么变差？](https://zhuanlan.zhihu.com/p/96990210)

造成因子样本内、外表现差异的最主要原因自然是样本内的 data snooping (即因子本来就是假的)，但如果因子确实是真实的，那么它们在样本外变差的原因是什么呢？学术界和业界的主要观点包括以下三种：

1. 曝光导致错误定价减弱
2. 因子拥挤
3. 交易成本

### 曝光对定价的修正

- [McLean, R. David, and Jeffrey Pontiff. "Does academic research destroy stock return predictability?." *The Journal of Finance* 71, no. 1 (2016): 5-32.](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365)

- [Bowles, Boone, Adam V. Reed, Matthew C. Ringgenberg, and Jacob R. Thornock. "Anomaly time." *Available at SSRN 3069026* (2020).](https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=3069026)

McLean and Pontiff (2016) 研究了 97 个因子，发现因子样本外的表现比样本内的表现下降了 26%、而发表后 (post-publication) 的表现较样本内则下降了 58%。McLean and Pontiff (2016) 考虑样本内外差异是为了控制过拟合的影响。上述结果表明，58% 与 26% 之差 —— 即 32% —— 就是发表本身造成因子效果的减弱。McLean and Pontiff (2016) 把它称作 publication-informed trading。这背后的逻辑链是：

​	因子被发表导致它被公布于众 --> 越来越多的人交易该因子从而减弱了错误定价 --> 最终导致因子收益率降低

学术界在研究因子的时候为了避免未来数据，通常采用每年再平衡的方法 (量价相关的指标通常是月频再平衡)，导致构建因子的指标数据严重滞后。Bowles et al. (2019) 一文则使用 Compustat Snapshot 数据库对因子时效进行了分析。利用 Snapshot 数据，Bowles et al. (2019) 研究了一些常见的源自财务数据的因子，发现绝大多数因子在最新数据更新后的 120 天之内 (特别是最初的 30 天内) 能够获得显著的超额收益。而在 120 天之后，超额收益消失。不过，Bowles et al. (2019) 也指出，最近几年的实证结果显示，因子的超额收益消失的更快。基于这些发现，Bowles et al. (2019) 认为因子是真实的 (而非 data snooping 出来的)，但很快就会因套利交易而消失。

### 因子拥挤

- [Bonne, George, Leon Roisenberg, Roman Kouzmenko, and Peter Zangari. "MSCI integrated factor crowding model." (2020).](https://www.msci.com/documents/10199/acf506d5-4254-b85f-e213-eaef95661970)
- [Bayraktar, M., Stuart Doole, Altaf Kassam, and Stan Radchenko. "Lost in the Crowd? Identifying and Measuring Crowded Strategies and Trades." *MSCI Research Insight* (2015).]()
- [海通证券 - 因子失效预警: 因子拥挤](https://www.htsec.com/jfimg/colimg/upload/20181112/10121541986928288.pdf)

### 交易成本

- [Novy-Marx, Robert, and Mihail Velikov. "A taxonomy of anomalies and their trading costs." *The Review of Financial Studies* 29, no. 1 (2016): 104-147.](https://academic.oup.com/rfs/article-abstract/29/1/104/1844518)
- [Chen, Andrew Y., and Mihail Velikov. "Accounting for the anomaly zoo: A trading cost perspective." *Available at SSRN* 3073681 (2017).](https://jacobslevycenter.wharton.upenn.edu/wp-content/uploads/2019/09/Accounting-for-the-Anomaly-Zoo.pdf)

Novy-Marx and Velikov (2015) 研究了交易费用对因子效果的影响，并提出三个思路降低交易成本：

1. 仅使用交易费用低的股票构建因子组合
2. 降低因子组合再平衡的频率
3. 在交易时考虑更严格的买卖价差约束

