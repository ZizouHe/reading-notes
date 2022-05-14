# Which Beta?

## Errors in Variables

- [Jegadeesh, Narasimhan, Joonki Noh, Kuntara Pukthuanthong, Richard Roll, and Junbo Wang. "Empirical tests of asset pricing models with individual assets: Resolving the errors-in-variables bias in risk premium estimation." *Journal of Financial Economics* 133, no. 2 (2019): 273-298.](https://www.sciencedirect.com/science/article/pii/S0304405X19300431)
- [Which Beta?](https://zhuanlan.zhihu.com/p/71072376)

首先考虑Fama Macbeth regression, $$R_{i,t}$$ 是个股收益率，$$i = 1, \ldots, N$$, $$t = 1, \ldots, T$$, $$f_t \in \mathbb{R}^K$$ 是 t 期因子向量，首先对每支个股进行时间序列回归，
$$
R_{i t}=a_{i}+\beta_{i}^{\prime} f_{t}+\varepsilon_{i t}, \; \; t \in [T], \;\; \forall i \in [N].
$$
 以此来得到因子暴露 $$\beta_i$$。在第二步截面回归中，Fama-MacBeth 在每个时间 t 上进行了一次截面回归，这是 Fama-MachBeth 和普通截面回归最大的不同，
$$
R_{i t}=\beta_{i}^{\prime} \lambda_{t}+\alpha_{i t}, \; \; \forall i = 1, \cdots, N.
$$
最后把这 T 次截面回归得到的参数取均值作为回归的 estimate，
$$
\begin{aligned}
\hat{\lambda} &=\frac{1}{T} \sum_{t=1}^{T} \hat{\lambda}_{t} \\
\hat{\alpha}_{i} &=\frac{1}{T} \sum_{t=1}^{T} \hat{\alpha}_{i t}.
\end{aligned}
$$
其中 $$\hat{\lambda} \in \mathbb{R}^K$$ 是因子收益率向量的估计，$$\hat{\alpha}_i$$是个股定价误差的估计。以此我们很容易得到各自的标准差估计，
$$
\begin{aligned}
\sigma^{2}(\hat{\lambda}) &=\frac{1}{T^{2}} \sum_{t=1}^{T}\left(\hat{\lambda}_{t}-\hat{\lambda}\right)^{2} \\
\sigma^{2}\left(\hat{\alpha}_{i}\right) &=\frac{1}{T^{2}} \sum_{t=1}^{T}\left(\hat{\alpha}_{i t}-\hat{\alpha}_{i}\right)^{2}
\end{aligned}
$$
Fama-MacBeth 回归的最大优点是它排除了残差截面相关性对标准误的影响。股票的残差收益率在截面上具有很高的相关性，因此该修正对于准确计算标准误至关重要。下面来说说它的不足。

1. Fama-MacBeth 回归对于残差在时序上的相关性无能为力。
1. 在截面回归中用到的 $$\beta_i$$ 并不是已知的，而是通过时间序列得到的估计值，因此存在误差。Fama-MacBeth 回归对此也无能为力，需要 Shanken correction。

针对第二点不足，Jegadeesh et al. (2019) 提出，第一步通过时序回归得到的因子载荷仅仅是真实但未知的 $$\beta$$ 的估计，因而存在估计误差 (无偏但有error)；将这个 estimate 直接作为解释变量用在第二步就引入了 **errors-in-variables 问题 (EIV)**。

对 EIV 问题，业界有着不同的做法。**我们熟悉的 Barra 的纯因子模型本质上正是 Fama-MacBeth Regression。**但是它没有使用第一步时序回归计算因子载荷，而是使用了 firm characteristics 作为因子载荷，然后进行截面回归。

Jegadeesh et al. (2019)  则考虑对第一步时间序列回归的结果进行修正，用工具变量来得到第二步的无偏估计。我们首先改写Fama Macbeth regression为矩阵形式，
$$
\mathbf{r}_{t}=\mathbf{B} \lambda+\xi_{t},
$$
where $$\mathbf{r}_{t} \in \mathbb{R}^N, \mathbf{B} \in \mathbb{R}^{N \times (K+1)},  \lambda \in \mathbb{R}^{K+1}$$, and $$\mathbf{B}$$ is the factor laoding matrix obtained from the time-series regression in step one. We now consider a instrumental variable setting, where we replace $$\mathbf{B}$$ by the estimate given by instrumental regression, i.e., 
$$
\widehat{\mathbf{B}} = \widehat{\mathbf{B}}_{IV} \left(\widehat{\mathbf{B}}_{IV}^\top \widehat{\mathbf{B}}_{IV} \right)^{-1} \left(\widehat{\mathbf{B}}_{IV}^\top \widehat{\mathbf{B}}_{EV}\right),
$$
where $$\widehat{\mathbf{B}}_{IV}$$ and $$\widehat{\mathbf{B}}_{EV}$$​ are the matrices of instrumental and explanatory variables, respectively. We then use $$\widehat{\mathbf{B}}$$ to obtain the estimation of $$\lambda$$.

具体来说，在每个月末，为了计算最新的  $$\widehat{\mathbf{B}}_{IV}$$ 和  $$\widehat{\mathbf{B}}_{EV}$$ ，Jegadeesh et al. (2019) 使用过去三年个股的日频收益率和多因子模型的日频收益率进行时序 multivariate regression：

1. **如果当前月是偶数月**（比如二月、四月、六月等），则使用过去三年窗口内所有的**偶数月**之中个股和多因子的收益率进行回归，得到的回归系数就是 $$\widehat{\mathbf{B}}_{EV}$$；使用这三年窗口内所有**奇数月**之中个股和多因子的收益率进行回归，得到的回归系数作为 $$\widehat{\mathbf{B}}_{IV}$$。
2. **如果当前月是奇数月**（比如一月、三月、五月等），则使用过去三年窗口内所有的**奇数月**之中个股和多因子的收益率进行回归，得到的回归系数就是 $$\widehat{\mathbf{B}}_{EV}$$；使用这三年窗口内所有**偶数月**之中个股和多因子的收益率进行回归，得到的回归系数作为 $$\widehat{\mathbf{B}}_{IV}$$。

Jegadeesh et al. (2019) 指出，上述 IV estimate 可以获得 risk premium 的无偏估计。

## Comparing Cross-section and Time-series Factor Models

- [Fama, Eugene F., and Kenneth R. French. "Comparing cross-section and time-series factor models." *The Review of Financial Studies* 33, no. 5 (2020): 1891-1926.](https://academic.oup.com/rfs/article/33/5/1891/5555879)
- [Which Beta (II)?](https://zhuanlan.zhihu.com/p/84462587)

一句话结论：截面回归得到的纯因子组合的 factor returns 比各种 double sort 得到的 factor returns 能够更好的解释资产的截面差异。

## PCA for Factor Models

- [Kozak, Serhiy, Stefan Nagel, and Shrihari Santosh. "Interpreting factor models." *The Journal of Finance* 73, no. 3 (2018): 1183-1223.](https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.12612)

- [Which Beta (III) ?](https://zhuanlan.zhihu.com/p/376931645)

哪怕在这个价格由情绪交易者驱动的世界中，资产和前几个主成分的协方差依然能在很大程度上解释资产预期收益的截面差异，而如果不采用更进一步的分析，人们是无法区分背后的原因是风险补偿还是非理性驱动的定价错误。

## Toward a Better Factor Model

- [Liao, Zhipeng, and Yan Liu. "Optimal cross-sectional regression." *Available at SSRN* (2021).](http://www.econ.ucla.edu/liao/papers_pdf/CSR_eff.pdf)
- [Barillas, Francisco, and Jay Shanken. "Which alpha?." *The Review of Financial Studies* 30, no. 4 (2017): 1316-1338.](https://academic.oup.com/rfs/article/30/4/1316/2758634)

- [Toward a better factor model](https://zhuanlan.zhihu.com/p/360857923)

