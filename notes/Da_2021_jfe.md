# Extrapolative beliefs in the cross-section: What can we learn from the crowds?

- [Da, Zhi, Xing Huang, and Lawrence J. Jin. "Extrapolative beliefs in the cross-section: What can we learn from the crowds?." *Journal of Financial Economics* 140, no. 1 (2021): 175-196.](https://www.sciencedirect.com/science/article/pii/S0304405X20302786)

## Summary

This paper studies the crowdsourced stock ranking data from Forcerank. It shows that investors extrapolate from stocks’ recent past returns, with more weight on more recent returns, es- pecially when recent returns are negative, salient, or from a dispersed cross-section. Such extrapolative beliefs are stronger among nonprofessionals and large stocks.



- Regression using consensus Forcerank score as the dependent variable and past stock returns as the explanatory variables. 

  - The coefficients on the past 12 weekly returns are all positive and mostly significant. More important, the coefficients on recent past returns are in general higher than those on distant past returns.
  - They further **decompose past weekly returns into their systematic and idiosyncratic components using the CAPM**. The results show that investors extrapolate only from past idiosyncratic returns.

- We have observed a clear and robust decay pattern in the relation between investors’ current return expec- tation and recent past returns. To capture this pattern parsimoniously, we now estimate a parametric regression model that assumes an exponential decay of weights on past returns:
  $$
  \begin{aligned}
  &\text { Forcerank }_{i, t}=\lambda_{0}+\lambda_{1} \cdot \sum_{s=0}^{n} w_{s} R_{i, t-s}+\varepsilon_{i, t} \\
  &\text { where } w_{s}=\frac{\lambda_{2}^{s}}{\sum_{j=0}^{n} \lambda_{2}^{j}}.
  \end{aligned}
  $$
  

  - The first parameter, $$\lambda_1$$—a scaling factor that multiplies all past returns of stock i—captures a “level” effect (i.e., **the overall extent to which investor expectations respond to these past returns**). The second parameter, $$\lambda_2$$— **which governs how past returns are relatively weighted in forming expectations**—captures a “slope” effect: a $$\lambda_2$$ closer to zero means that investors put much higher weight on recent past returns as opposed to distant past returns. 

  - The parametric regression reports an estimate of $$34.12$$ for $$\lambda_{1}$$ and an estimate of $$0.55$$ for $$\lambda_{2}$$. These joint estimates suggest that Forcerank participants exhibit a strong degree of extrapolation. 
  - Interestingly, between professional and nonprofessional users, the extrapolation parameters are quite different. We find that financial professionals have a $$\lambda_{1}$$ of $$26.35$$, which is lower than that of the nonprofessionals (33.77), suggesting that professionals rely less on past stock returns when forming expectations about stock returns over the next week. Moreover, professionals have a $$\lambda_{2}$$ of $$0.773$$, which is higher than that of the nonprofessionals (0.552).

- To develop a deeper understanding of expectation formation, we generalize the parametric regression by separately estimating $$\lambda_{1}$$ and $$\lambda_{2}$$ for past returns of different characteristics. 
  $$
  \begin{aligned}
  \text { Forcerank }_{i, t}=& \lambda_{0}+\lambda_{1, p} \cdot \sum_{s=0}^{n} \mathbb{1}_{\left\{R_{i, t-s} \geq 0\right\}} \cdot w_{s, p} R_{i, t-s} +\lambda_{1, n} \cdot \sum_{s=0}^{n} \mathbb{1}_{\left\{R_{i, t-s}<0\right\}} \cdot w_{s, n} R_{i, t-s}+\varepsilon_{i, t}.
  \end{aligned}
  $$
  where $$w_{s, p}=\frac{\lambda_{2, p}^{s}}{\sum_{j=0}^{n} \lambda_{2, p}^{j}}$$ and $$w_{s, n}=\frac{\lambda_{2, n}^{s}}{\sum_{j=0}^{n} \lambda_{2, n}^{j}}$$.

  - The results show that return extrapolation is asymmetric. In particular, individuals seem to put more weight on negative past returns -$$\lambda_{1, n}$$ is much larger than $$\lambda_{1, p}$$-and this weight decays more slowly into the past for negative past returns - $$\lambda_{2, n}$$ is much higher than $$\lambda_{2, p}$$ and is therefore much closer to one. 

- To understand the source of the return predictability, we further decompose the Forcerank score into two components: a predicted score and the residual. The predicted score is computed as the fitted value from the nonlinear regression. Then we run regressions where future returns is $$Y$$ and these scores are the explanatory variables.

  - Forcerank score and the predicted score both drive out past-return measures when they are included in the same regression.
  - By construction, the residual score is orthogonal to past returns. Interestingly, regressions show that the residual score also negatively predicts the next week’s return, with or without controlling for past returns. **This finding suggests that the predictive power of the Forcerank score is not completely driven by its association with past returns**. 
  - A large literature on the short-term return reversal has already shown that the **past return of a stock negatively predicts its future return and this reversal can be driven by liquidity shocks** unrelated to return extrapolation (see Jegadeesh and Titman, 1995 and Campbell et al., 1993, among others). A priori, we do not expect liquidity shocks to be the main explanation for return predictability because stocks in our sample tend to be very large stocks.
  - To evaluate the economic significance of our return predictability results, we form trading strategies. At the beginning of each week, we sort the stocks into five quintiles based on different variables. The portfolio is rebalanced every week. Stocks with prices below $5 at the beginning of the week are removed to reduce the impact of illiquidity.
  - The low-score-minus-high-score re- turn spread is 8.11 bps per day (*t*-value of 2.33). The return spread remains significant after risk adjustments using the CAPM, the Fama-French five-factor model, or the five-factor model augmented with the momentum factor and the short-term reversal factor.

​		