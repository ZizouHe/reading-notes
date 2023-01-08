# Stambaugh-Yuan Four Factors

- [Stambaugh, Robert F., and Yu Yuan. "Mispricing factors." *The Review of Financial Studies* 30, no. 4 (2017): 1270-1315.](https://academic.oup.com/rfs/article/30/4/1270/2965095)
- [主流多因子模型巡礼 第六节](https://zhuanlan.zhihu.com/p/211070896)

## Some Discussion

Stambaugh-Yuan 四因子模型中的规模因子，它的构建方法与传统方法差异更大。上述分别使用管理和表现分别与市值进行双重排序 (2x3 sort)，共得到 12 个投资组合。为构建规模因子，Stambaugh and Yuan (2017) 摒弃了管理和表现两变量的高、低组共 8 个组合，而仅使用剩余的 4 个组合。换句话说，管理和表现分别与市值双重排序，得到各自的 S/M 和 B/M 组合。将两个 S/M 组合取平均并做多，将两个 B/M 组合取平均并做空，以此构建规模因子（SMB）的投资组合。

注意到这种2x3 sort之后取高3组平均和低3组平均的做法是为了

- By averaging across the three mispricing categories, that approach would seek to **neutralize the effects of mispricing** when computing the size factor.  (消除管理/表现因子的mispricing)
- The problem is that such a neutralization can be thwarted by arbitrage asymmetry ([Stambaugh, Yu and Yuan (2015 JoF) Arbitrage asymmetry and the idiosyncratic volatility puzzle](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12286))—a greater ability or willingness to buy than to short for many investors. With such asymmetry, the mispricing within the overpriced category is likely to be more severe than the mispricing within the underpriced category.
- Moreover, this asymmetry is likely to be greater for small stocks than for large ones, given that small stocks present potential arbitrageurs with greater risk (idiosyncratic volatility). 
- Thus, simply averaging across mispricing categories would not neutralize the effects of mispricing, and the resulting SMB would have an overpricing bias.