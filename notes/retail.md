# Tracking Retail Investor Activity

- [Boehmer, Ekkehart, Charles M. Jones, Xiaoyan Zhang, and Xinran Zhang. "Tracking retail investor activity." *The Journal of Finance* 76, no. 5 (2021): 2249-2305.](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.13033)
- [顶刊上的另类数据与股票收益研究 Section 4](https://zhuanlan.zhihu.com/p/354068567)



1. Identify retail order flow: due to regulatory restrictions in the United States and the resulting institutional arrangements, retail order flow—but not institutional order flow—can receive price improvement, measured in small fractions of a cent per share. Use this observation to identify marketable retail price-improved orders from the Trade and Quote (TAQ) data

   - **Retail orders are typically executed by wholesalers or via internalization**, meaning that orders are filled from a broker’s own inventory
   - Wholesalers are willing to provide a small price improvement to induce the retail trader’s broker to route the order to the wholesaler. Due to Regulation 606T, Internalizers need to show that they execute their clients’ orders optimally and thus also have incentives to provide price improvement to their clients. **This price improvement is typically only a small fraction of a cent. **
   - Institutional orders are almost never internalized or sold to wholesalers. Instead, their orders are sent to exchanges and dark pools, and Reg NMS prohibits these orders from having subpenny limit prices. Thus, institutional transaction prices **are usually in round pennies**. The only exception applies to midpoint trades. Reg NMS has been interpreted to allow executions at the midpoint between the best bid and best offer, this means that many institutional transactions are also **reported at a half-penny price.**
   - Transactions with a retail seller tend to be reported on a TRF at prices that are just above a round penny due to the small price improvement, while transactions with a retail buyer tend to be reported on a TRF at prices just below a round penny.

2. Measuring marketable retail investors order imbalance:

   - mrbvol: the average daily buy volume from marketable retail orders 

   - mrsvol: the average daily sell volume from marketable retail orders

   - mrbtrd: the average number of buy trades from marketable retail orders

   - mrstrd: the average number of sell trades from marketable retail orders

   - oddmrbvol and oddmrsvol: the daily averages of odd lot marketable retail buy and sell volumes **(odd lot trades are trades of fewer than 100 shares)**

   - oddmrbtrd and oddmrstrd: the daily averages of odd lot marketable retail buy and sell trades
     $$
     \begin{aligned}
     \text { mroibvol }(i, t) &=\frac{\operatorname{mrbvol}(i, t)-\operatorname{mrsvol}(i, t)}{\operatorname{mrbvol}(i, t)+\operatorname{mrsvol}(i, t)} \\
     \operatorname{mroibtrd}(i, t) &=\frac{\operatorname{mrbtrd}(i, t)-m r s t r d(i, t)}{\operatorname{mrbtrd}(i, t)+\operatorname{mrstrd}(i, t)} \\
     \text { oddmroibvol }(i, t) &=\frac{\text { oddmrbvol }(i, t)-\text { oddmrsvol }(i, t)}{\text { oddmrbvol }(i, t)+\text { oddmrsvol }(i, t)} \\
     \text { oddmroibtrd }(i, t) &=\frac{\text { oddmrbtrd }(i, t)-\text { oddmrstrd }(i, t)}{\text { oddmrbtrd }(i, t)+\text { oddmrstrd }(i, t)}
     \end{aligned}
     $$

3. Predictability: the authors find that retail investors are slightly contrarian at a weekly horizon, and that the cross-section of weekly marketable retail order imbalances predicts the cross-section of returns over the next several weeks.

4. The explanation of predictive power: 

   - Hypothesis 1 (**persistence in retail order flow**): as in Chordia and Subrahmanyam (2004), order flows are persistent, and, since the retail buying/selling pressure is also persistent, this could lead directly to the predictability of future returns
   - wHypothesis 2 (**liquidity provision**): as in Kaniel, Saar, and Titman (2008), these retail traders are contrarian at weekly horizons, and since their contrarian trading provides liquidity to the market, their trades might positively predict future returns.
   - Hypothesis 3 **(informed trading)**: as in Kelley and Tetlock (2013), retail investors, especially ag- gressive investors using market orders, may have valuable information about the firm, and thus, their trading could correctly predict the direction of future returns 
   - See paper P2276 - 2277 for the two-stage decomposition.
   - The empirical findings show that persistence in order flow and order flow driven by return reversals (the proxy for liquidity provision) account for about half of the predictive power of the marketable retail order imbalance for future returns. **The other half of this predictive power is attributed to potential informed trading.**