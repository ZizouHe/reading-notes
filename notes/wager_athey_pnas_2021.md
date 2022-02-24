# Confidence Intervals for Policy Evaluation in Adaptive Experiments

- [Hadad, Vitor, David A. Hirshberg, Ruohan Zhan, Stefan Wager, and Susan Athey. "Confidence intervals for policy evaluation in adaptive experiments." *Proceedings of the National Academy of Sciences* 118, no. 15 (2021).](https://www.pnas.org/content/118/15/e2014602118.short)



## Summary

For adaptively collected data in a potential outcome model, naive average results in a biased estimation, and the inverse-probability weighting estimator results in a non-normal asymptotic distribution. This paper propose a test statistic that is asymptotically unbiased and normal.

 

## Details

Denote our data as $$(W_t, Y_t)$$, The random variables $$W_{t} \in \mathcal{W}$$ are called the arms, treatments or interventions. Arms are categorical. The reward or outcome $$Y_{t}$$ represents the individual's response to the treatment. The treatment assignment probabilities $$e_{t}(w):=\mathbb{P}\left[W_{t}=w \mid H^{t-1}\right]$$, also called propensity scores, are time-varying and decided via some known algorithm. Given this setup, we are concerned with the problem of estimating and testing pre-specified hypotheses about the value of an arm, denoted by $$Q(w):=\mathbb{E}\left[Y_{t}(w)\right]$$, as well as differences between two such values, denoted by $$\Delta\left(w, w^{\prime}\right):=\mathbb{E}\left[Y_{t}(w)\right]-\mathbb{E}\left[Y_{t}\left(w^{\prime}\right)\right]$$. 

IPW estimator is defined as
$$
\widehat{Q}_{T}^{I P W}(w):=\frac{1}{T} \sum_{t=1}^{T} \widehat{\Gamma}_{t}^{I P W}(w), \quad \widehat{\Gamma}_{t}^{I P W}(w):=\frac{\mathbb{I}\left\{W_{t}=w\right\}}{e_{t}(w)} Y_{t},
$$
and the augmented inverse propensity weighted (AIPW) estimator is defined as
$$
\begin{aligned}
&\widehat{Q}_{T}^{A I P W}(w):=\frac{1}{T} \sum_{t=1}^{T} \widehat{\Gamma}_{t}^{A I P W}(w) \\
&\widehat{\Gamma}_{t}^{A I P W}(w):=\frac{\mathbb{I}\left\{W_{t}=w\right\}}{e_{t}(w)} Y_{t}+\left(1-\frac{\mathbb{I}\left\{W_{t}=w\right\}}{e_{t}(w)}\right) \hat{m}_{t}(w).
\end{aligned}
$$
The symbol $$\hat{m}_{t}(w)$$ denotes an estimator of the conditional mean function $$m(w)=\mathbb{E}\left[Y_{t}(w)\right]$$ based on the history $$H^{t-1}$$, but it need not be a good one: it could be biased or even inconsistent (doubly robust estimator). **The second term of $$\widehat{\Gamma}_{t}^{A I P W}(w)$$ acts as a control variate: adding it preserves unbiasedness but can reduce variance,** as it has mean zero conditional on $$H^{t-1}$$ and, if $$\hat{m}_{t}(w)$$ is a reasonable estimator of $$m(w)$$, is negatively correlated with the first term.

**Inverse-probability weighting fixes the bias problem but results in a non-normal asymptotic distribution. In fact, when the probability of assignment to the arm of interest tends to zero, the inverse probability weights increase, which in turn causes the tails of the distribution to become heavier.**

This paper considers the adaptively-weighted AIPW estimator:
$$
\widehat{Q}_{T}^{h}(w)=\frac{\sum_{t=1}^{T} h_{t}(w) \widehat{\Gamma}_{t}^{A I P W}(w)}{\sum_{t=1}^{T} h_{t}(w)},
$$
with a sequence of evaluation weights $$h_t(w)$$. Then given some assumptions,

Suppose that either $$\hat{m}_{t}(w)$$ is consistent or $$e_{t}(w)$$ has a limit $$e_{\infty}(w) \in[0,1]$$, i.e., either
$$
\hat{m}_{t}(w) \underset{t \rightarrow \infty}{\stackrel{a . s .}{\longrightarrow}} Q(w) \quad \text { or } \quad e_{t}(w) \underset{t \rightarrow \infty}{\stackrel{a . s .}{\longrightarrow}} e_{\infty}(w).
$$
Then (basically, use **martingale central limit theorem**)
$$
\begin{aligned}
&\frac{\widehat{Q}_{T}^{h}(w)-Q(w)}{\widehat{V}_{T}^{h}(w)^{\frac{1}{2}}} \stackrel{d}{\rightarrow} \mathcal{N}(0,1), \text { where } \\
&\widehat{V}_{T}^{h}(w):=\frac{\sum_{t=1}^{T} h_{t}^{2}(w)\left(\widehat{\Gamma}_{t}(w)-\widehat{Q}_{T}(w)\right)^{2}}{\left(\sum_{t=1}^{T} h_{t}(w)\right)^{2}}.
\end{aligned}
$$
A simple choice of $$h_t$$ could be $$h_t = \sqrt{e_t / T}$$, and some complicated schemes can be constructed to result in a variance-optimal estimator.

