# Statistical Inference with M-Estimators on Adaptively Collected Data

- [Zhang, Kelly, Lucas Janson, and Susan Murphy. "Statistical inference with m-estimators on adaptively collected data." *Advances in Neural Information Processing Systems* 34 (2021).](https://proceedings.neurips.cc/paper/2021/file/3d7d9461075eb7c37fbbfcad1d7042c1-Paper.pdf)

## Summary

This paper consider the problem of M-estimators for contextual bandit under the adaptive collected data scheme. Using particular adaptive weights, the M-estimators can be used to construct asymptotically valid confidence regions for a variety of inferential targets.

## Settings

We assume that the data we have after running a contextual bandit algorithm is comprised of contexts $$\left\{X_{t}\right\}_{t=1}^{T}$$, actions $$\left\{A_{t}\right\}_{t=1}^{T}$$, and primary outcomes $$\left\{Y_{t}\right\}_{t=1}^{T} $$. $$T$$ is deterministic and known. We use potential outcome notation and let $$\left\{Y_{t}(a): a \in \mathcal{A}\right\}$$ denote the potential outcomes of the primary outcome and let $$Y_{t}:=Y_{t}\left(A_{t}\right)$$ be the observed outcome. We assume a stochastic contextual bandit environment in which $$\left\{X_{t}, Y_{t}(a): a \in \mathcal{A}\right\} \stackrel{i . i . d}{\sim} \mathcal{P} \in \mathbf{P}$$ for $$t \in[1: T]$$. We define the history $$\mathcal{H}_{t}:=\left\{X_{t^{\prime}}, A_{t^{\prime}}, Y_{t^{\prime}}\right\}_{t^{\prime}=1}^{t}$$ for $$t \geq 1$$ and $$\mathcal{H}_{0}:=\emptyset$$. Actions $$A_{t} \in \mathcal{A}$$ are selected according to policies $$\pi:=\left\{\pi_{t}\right\}_{t \geq 1}$$, which define action selection probabilities $$\pi_{t}\left(A_{t}, X_{t}, \mathcal{H}_{t-1}\right):=\mathbb{P}\left(A_{t} \mid \mathcal{H}_{t-1}, X_{t}\right)$$.

We assume that $$\theta^*(\mathcal{P})$$ is a conditionally maximizing value of criterion $$m_{\theta}$$, i.e., for all $$\mathcal{P} \in \mathbf{P}$$,
$$
\theta^{*}(\mathcal{P}) \in \underset{\theta \in \Theta}{\operatorname{argmax}} \mathbb{E}_{\mathcal{P}}\left[m_{\theta}\left(Y_{t}, X_{t}, A_{t}\right) \mid X_{t}, A_{t}\right].
$$
The M-estimator is defined as
$$
\hat{\theta}_{T}:=\underset{\theta \in \Theta}{\operatorname{argmax}} \frac{1}{T} \sum_{t=1}^{T} m_{\theta}\left(Y_{t}, X_{t}, A_{t}\right).
$$

## Adaptively Weighted M-Estimators

Our proposed estimator for $$\theta^*(\mathcal{P})$$, $$\hat{\theta}_{T}$$, is the maximizer of a weighted version of the M-estimation criterion,
$$
\hat{\theta}_{T}:=\underset{\theta \in \Theta}{\operatorname{argmax}} \frac{1}{T} \sum_{t=1}^{T} W_{t} m_{\theta}\left(Y_{t}, X_{t}, A_{t}\right)=: \underset{\theta \in \Theta}{\operatorname{argmax}} M_{T}(\theta),
$$
where 
$$
W_{t}=\sqrt{\frac{\pi_{t}^{\text {sta }}\left(A_{t}, X_{t}\right)}{\pi_{t}\left(A_{t}, X_{t}, \mathcal{H}_{t-1}\right)}}.
$$
Here $$\left\{\pi_{t}^{\mathrm{sta}}\right\}_{t \geq 1}$$ are pre-specified stabilizing policies that do not depend on data $$\left\{Y_{t}, X_{t}, A_{t}\right\}_{t \geq 1}$$. A default choice for the stabilizing policy when the action space is of size $$|\mathcal{A}|<\infty$$ is just $$\pi_{t}^{\mathrm{sta}}(\bar{a}, x)=1 /|\mathcal{A}|$$ for all $$x, a, t$$. 

This weight is very similar to the result in [Hadid et al. (2021)](./wager_athey_pnas_2021.html), where $$\pi_{t}\left(A_{t}, X_{t}, \mathcal{H}_{t-1}\right)$$ serves as the propensity score and $$\pi_{t}^{\mathrm{sta}}\left(A_{t}, X_{t}\right)$$ is basically a constant.

To construct uniformly valid confidence regions for $$\theta^{*}(\mathcal{P})$$ we prove that $$\hat{\theta}_{T}$$ is uniformly asymptotically normal in the following sense:
$$
\Sigma_{T}(\mathcal{P})^{-1 / 2} \ddot{M}_{T}\left(\hat{\theta}_{T}\right) \sqrt{T}\left(\hat{\theta}_{T}-\theta^{*}(\mathcal{P})\right) \stackrel{D}{\rightarrow} \mathcal{N}\left(0, I_{d}\right) \text { uniformly over } \mathcal{P} \in \mathbf{P},
$$
where $$\ddot{M}_{T}(\theta):=\frac{\partial^{2}}{\partial^{2} \theta} M_{T}(\theta)$$ and $$\Sigma_{T}(\mathcal{P}):=\frac{1}{T} \sum_{t=1}^{T} \mathbb{E}_{\mathcal{P}, \pi_{t}^{s t a}}\left[\dot{m}_{\theta^{*}(\mathcal{P})}\left(Y_{t}, X_{t}, A_{t}\right)^{\otimes 2}\right]$$. We define $$\dot{m}_{\theta}:=\frac{\partial}{\partial \theta} m_{\theta}$$. Similarly we define respectively $$\ddot{m}_{\theta}$$ and $$\dddot{m}_{\theta}$$ as the second and third partial derivatives of $$m_{\theta}$$ with respect to $$\theta$$. For any vector $$z$$ we define $$z^{\otimes 2}:=z z^{\top}$$. 

Notice that the basic conditions and intuitions behind these can be traced back to the classical asymptotic results for M-estimator (Van der Vaart. *Asymptotic Statistics*, chapter 5).

