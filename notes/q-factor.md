# Q-Factor Model

- [从 Factor Zoo 到 Factor War，实证资产定价走向何方？](https://zhuanlan.zhihu.com/p/72957469)
- [主流多因子模型巡礼 第5节](https://zhuanlan.zhihu.com/p/211070896)
- [Hou, Kewei, Chen Xue, and Lu Zhang. "Digesting anomalies: An investment approach." *The Review of Financial Studies* 28, no. 3 (2015): 650-705.](https://academic.oup.com/rfs/article/28/3/650/1574802)
- [Hou, K., H. Mo, C. Xue, and L. Zhang. *q5. Charles A*. No. 2018-10. Dice Center Working Paper, 2018.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3198011)
- [Hou, Kewei, Haitao Mo, Chen Xue, and Lu Zhang. "Which factors?." *Review of Finance* 23, no. 1 (2019): 1-35.](https://academic.oup.com/rof/article-abstract/23/1/1/5133564)
- [Hou, Kewei, Chen Xue, and Lu Zhang. "Replicating anomalies." *The Review of Financial Studies* 33, no. 5 (2020): 2019-2133.](https://academic.oup.com/rfs/article/33/5/2019/5236964)

## Some Points of Digesting anomalies: An investment approach

- 当预期盈利给定时，股票收益率和投资成反比；当投资给定时，股票收益率和预期盈利成正比。在构建因子时，为了体现上述条件预期收益率的关系，他们特意选择了通过 size、I/A 以及 ROE 将股票池独立进行 2 × 3 × 3 的 triple sort（使用 ROE 和 I/A 将股票分成三组时使用学术界常用的 30% 和 70% 分位数，中间的 40% 为 Middle 组），一共得到 18 个投资组合（每个投资组合中的股票都是按市值加权）:
  - **SMB：**9 个 small size 组合的简单平均收益率与 9 个 large size 组合的简单平均收益率之差；
  - **I/A：**6 个 low investment 组合的简单平均收益率与 6 个 high investment 组合的简单平均收益率之差；
  - **ROE：**6 个 high ROE 组的简单平均收益率与 6 个 low ROE 组的简单平均收益率之差。
  - **从上面的分析也可看出，学术界常见的 double sort 或者 triple sort 是为了反映预期收益率和因子之间的条件关系**
  - 投资和收益率的负相关是在控制了 ROE 之后的。因此，q-factor model 在构建投资因子时利用 size，ROE 和 total assets 增长率三个指标使用 **2 × 3 × 3 triple sort**，从而更好的反映了在控制 ROE 之后，投资和收益率的关系。
  - 无论是triple sort 还是 double sort, 都是对每个指标独立排序，而不是先对一个指标分组，再在组内排序

- This paper examines in total 80 anomaly variables proposed previously. Using GRS test, 38 are insignificant in the broad cross section. 

  - **GRS tests**  [Gibbons, Michael R., Stephen A. Ross, and Jay Shanken. "A test of the efficiency of a given portfolio." *Econometrica: Journal of the Econometric Society* (1989): 1121-1152.](https://www.jstor.org/stable/1913625) 

  - Also see [Anomalies, Factors, and Multi-Factor Models](https://zhuanlan.zhihu.com/p/56614427)


## Some Points of Which Factors?

- 这篇文章使用 spanning test 比较了他们提出的 q 和 $$q^5$$ 以及其他几个主流的多因子模型。 结果是q 和 $$q^5$$完胜。 

  - **Mean-Variance Spanning tests** 考察 n 个已知资产构建的 mean-variance 有效前沿能否包含某个新资产（[Huberman, Gur, and Shmuel Kandel. "Mean‐variance spanning." *The Journal of Finance* 42, no. 4 (1987): 873-888.](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.1987.tb03917.x)）。在比较两个多因子模型时，使用每个模型的因子构建有效前沿，并逐一检验其能否包含另一个模型中的因子。

  - 举个例子。[《美股上一个跨越时间尺度的趋势因子》](https://zhuanlan.zhihu.com/p/51043407)介绍了一个新的趋势因子。考虑新的趋势因子和三个已有因子（SREV、MOM 以及 LREV）的回归模型如下：
    $$
    r_{\text {Trend }, t}=\alpha+\beta_{1} r_{\mathrm{SREV}, t}+\beta_{2} r_{\mathrm{MOM}, t}+\beta_{3} r_{\mathrm{LREV}, t}+\epsilon_{t}
    $$
    该检验的 null hypothesis 是：
    $$
    \alpha=0, \quad \beta_{1}+\beta_{2}+\beta_{3}=1
    $$
    检验结果显著的拒绝原假设，说明已有三因子无法解释新的趋势因子。

- The Fama–French (2015) assumption that the expected return is the same for all horizons contradicts the notion of time-varying expected returns. The IRR can differ greatly from the one-period-ahead expected return. 

## Some Points of Replicating Anomalies

- 这篇文章复现了学术界提出的 447 个异象，涵盖动量 momentum（57个）、价值/成长 value versus growth（68个）、投资 investment（38个）、盈利 profitability（79个）、无形资产 intangibles（103个）、以及交易摩擦 trading frictions（102个）六大类。
- 对于这 447 个异象，当排除了微小市值股票的影响后，其中 286 个（64%）不再显著（在 5% 的显著性水平下，下同）；如果按照 Harvey, Liu and Zhu (2016) 的建议把 t-statistic 阈值提升到 3.0，则其中 380 个（85%）异象不再显著；最后，如果使用 Hou, Xue and Zhang (2015) 提出的 4 因子模型作为定价模型，那么其中 436 个（98%）异象不再显著，剩余存活的仅有 11 个。
  - To control the reliability of the replicated anomalies, we control for microcaps (stocks smaller than the 20th percentile of the market equity for NYSE stocks) via portfolio sorts with **NYSE breakpoints and value-weighted returns**. Many original studies overweight microcaps via equal-weighted returns and often with **NYSE-Amex-NASDAQ breakpoints in portfolio sorts.**
