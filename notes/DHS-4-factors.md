# Short- and Long-Horizon Behavioral Factors

- [Daniel, Kent, David Hirshleifer, and Lin Sun. "Short-and long-horizon behavioral factors." *The Review of Financial Studies* 33, no. 4 (2020): 1673-1736.](https://academic.oup.com/rfs/article-abstract/33/4/1673/5522378)

- [主流多因子模型巡礼 第七节](https://zhuanlan.zhihu.com/p/211070896)
- [一个加入行为因子的复合模型](https://zhuanlan.zhihu.com/p/57314781)

# Summary

- Behavioral theories suggest distinct mispricing mechanisms that will correct at shorter or longer horizon.
  - Short term: investors with limited attention underreact to public information that arrives at fairly high-frequency, such as quarterly earnings announcements. 
    - A subset of investors fail to take into account the implications of the latest earnings surprises for future earnings. As a consequence, stock prices underreact to earnings surprises, resulting in predictable future abnormal returns. Such misperceptions about the subsequent earnings should be corrected at reasonably short time horizons when new earnings are reported. Consistent with this hypothesis, evidence in the literature suggesting that the resulting mispricing is corrected over the next few quarterly earnings announcements.
    - An under-extrapolative belief regime (their "mean-reverting" regime) leads to post-earnings announcement drift and momentum. In this regime the positive returns that follow a positive earnings surprise dissipate rapidly when the next few earnings surprises prove earnings to be higher than expected.
  - Long term: investors who are overconfident about their private information signals will overreact to these signals, leading to a value effect wherein firms with high stock valuations relative to fundamental measures subsequently experience low returns. 
    - Owing to overconfidence in their private signals, investors are relatively unwilling to correct their perceptions as further (public) earnings news arrives. The correction of overconfidence-driven mispricing will take place over a much longer time horizon than mispricing that derives solely from limited attention.
    - The over-extrapolative ("trending") regime is more persistent, because a brief trend-opposing sequence of earnings surprises does not provide sufficient evidence to overcome the extrapolative expectations investors have formed about more distant earnings.
    - When a firm becomes over- or underpriced, the optimal response for the firm is to issue or repurchase its own stock, while not necessarily changing its level of investment. Since managers have superior information about the intrinsic value of their firms, they are well-positioned to lead their firms to act as arbitrageurs of their own stock. If investors were fully rational, they would fully impound the information contained in a firm’s decision to issue or repurchase equity, so that the financing decision would not predict future returns. However, in models of investor overconfidence, the market does not fully impound this information, so market timing leads to return predictability.
    - For several reasons, it is much less likely to capture shorter-horizon mispricing. Equity issuance and repurchase have disclosure, legal, underwriting, and other costs that likely constrain firms from issuing to exploit very short-horizon mispricing. There are also informational barriers to high-frequency issuance/repurchase strategies. Owing to these frictions, such corporate events tend to occur only occasionally, rather than as continuously updated responses to even transient changes in market conditions.

- The long horizon factor FIN is a composite (average) of the 1-year net-share-issuance (NSI) and 5-year composite-share-issuance (CSI) measures of [Pontiff and Woodgate (2008)](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.2008.01335.x) and [Daniel and Titman (2006)](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.2006.00884.x), respectively. 
  $$
  \text { Composite Share Issuance } \iota(t-\tau, t)=\log \left(\frac{M E_{t}}{M E_{t-\tau}}\right)-r(t-\tau, t),
  $$
  where $$\iota$$ is the expression for CSI, $$\tau$$ is the period of time ago, $$t$$ is the specified time with $$ME$$ defined as the total Market Equity and $$r(t-\tau, t)$$ is the stock return between $$-\tau$$ and $$t$$. $$ME_t$$ can also be calculated as $$N_t \times P_t$$ where $$N_t$$ is the total number of shares outstanding at time $$t$$ and $$P_t$$ is the price of shares at time $$t$$.

  The above equation can be difficult to relate to any stock characteristics or accounting fundamental data. However, with a simple transformation, we decompose the above equation as follows,
  $$
  \iota(t-\tau, t) = \log \left(\frac{M E_{t}}{M E_{t-\tau}}\right)-r(t-\tau, t) = \log \left(\frac{N_{t}}{N_{t-\tau}}\right)+\log \left(\frac{P_{t}}{P_{t-\tau}}\right)-r(t-\tau, t).
  $$
  Therefore, conceptualising the math functions into words, we have
  $$
  \iota(t-\tau, t) =\text { Change of Total Market Shares }+\text { Price Return }-\text { Total Return }.
  $$
  Re-organising the results of above into two key elements: change of total market shares (includes buybacks and issuances) and trailing dividend yield,
  $$
  \iota(t-\tau, t) =\text { Change of Total Market Shares } -\text {Trailing Dividend Yield}.
  $$
  From the above equation, it is obvious that composite-share-issuance is comprised of two basic factors,

  - Share Changes (including issuances and buybacks)
  - Dividend yield