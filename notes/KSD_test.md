# A Kernelized Stein Discrepancy for Goodness-of-fit Tests

- [Liu, Qiang, Jason Lee, and Michael Jordan. "A kernelized Stein discrepancy for goodness-of-fit tests." International Conference on Machine Learning. 2016.](https://arxiv.org/pdf/1602.03253.pdf)

- [Python Package - KSD](https://github.com/MinHyung-Kang/KSD)

- See my notes on [reproducing kernel Hilbert Space](https://zizouhe.github.io/stats-and-beyond/contents/RKHS.html) and [Stein's Method](https://zizouhe.github.io/stats-and-beyond/contents/steins.html) for more details.

## Summary

This paper derive a new discrepancy statistic for measuring differences between two probability distributions based on combining Stein’s identity with the reproducing kernel Hilbert space theory.

## Stein Discrepancy Measure

For two smooth densities $$p(x)$$ and $$q(x)$$ supported on $$\mathbb{R}$$ are identical if and only if

$$
\mathbb{E}_{p}\left[s_{q}(x) f(x)+\nabla_{x} f(x)\right]=0
$$

for smooth functions f (x) with proper zero-boundary conditions, where

$$
s_{q}(x)=\nabla_{x} \log q(x)= \frac{\nabla_{x} q(x)}{q(x)}
$$

is the *stein score function* of $$q$$. Therefore, one can define a Stein discrepancy measure between $$p$$ and $$q$$ via

$$
\mathbb{S}(p, q)=\max _{f \in \mathcal{F}}\left(\mathbb{E}_{p}\left[\boldsymbol{s}_{q}(x) f(x)+\nabla_{x} f(x)\right]\right)^{2}
$$

where F is a set of smooth functions that satisfies $$\mathbb{E}_{p}\left[s_{q}(x) f(x)+\nabla_{x} f(x)\right]=0$$ and is also rich enough to ensure $$\mathbb{S}(p, q)  > 0$$ whenever $$p \neq q$$. The problem is that $$\mathbb{S}(p, q)$$ is often computationally intractable.

## Kernelized Stein Discrepancy

This paper propose a simpler method for obtaining computational tractable Stein discrepancy $$\mathbb{S}(p, q)$$ by ***taking $$\mathcal{F}$$ to be the unit ball in the reproducing kernel Hilbert space associated with a smooth positive definite kernel $$k(x, x^\prime)$$***, and the associated Stein discrepancy is defined as

$$
\mathbb{S}(p, q)=\mathbb{E}_{x, x^{\prime} \sim p}\left[u_{q}\left(x, x^{\prime}\right)\right]
$$

where $$x, x^{\prime}$$ are i.i.d. random variables drawn from $$p$$ and
$$u_{q}\left(x, x^{\prime}\right)$$ is a function depends on $$q$$ only through the score function $$\nabla_{x} \log q(x)$$ ***which can be calculated efficiently even when $$q$$ has an intractable normalization constant***. Specifically, assuming

$$
q(x) = \frac{f(x)}{z}, \; \; \Rightarrow \; \; \boldsymbol{s}_q(x) = \frac{\nabla_{x} f(x)}{f(x)} =
$$

## Estimate Kernelized Stein Discrepancy

With an i.i.d. sample $$\left\{x_{i}\right\}$$ drawn from the (unknown) $$p(x)$$, the kernel Stein discrepancy also enables efficient empirical estimation of $$\mathbb{S}(p, q)$$ via a $$U$$ -statistic,

$$
\hat{\mathrm{S}}(p, q)=\frac{1}{n(n-1)} \sum_{i \neq j} u_{q}\left(x_{i}, x_{j}\right)
$$

The distribution of $$\hat{S}(p, q)$$ can be well characterized using the theory of $$U$$-statistics,

**Theorem.** *Let $$k\left(x, x^{\prime}\right)$$ be a positive definite kernel in the Stein class of $$p$$ and $$q$$. With some mild conditions, and $$\mathbb{E}_{x, x^{\prime} \sim p}\left[u_{q}\left(x, x^{\prime}\right)^{2}\right]<\infty$$ we have*

- *If $$p \neq q$$, then $$\hat{\mathrm{S}}_{u}(p, q)$$ is asymptotically normal with*

$$
\sqrt{n}\left(\hat{\mathbb{S}}_{u}(p, q)-\mathbb{S}(p, q)\right) \stackrel{d}{\rightarrow} \mathcal{N}\left(0, \sigma_{u}^{2}\right)
$$

*where $$\sigma_{u}^{2}=\operatorname{var}_{x \sim p}\left(\mathbb{E}_{x^{\prime} \sim p}\left[u_{q}\left(x, x^{\prime}\right)\right]\right)$$ and $$\sigma_{u}^{2} \neq 0$$*

- *If $$p=q$$, then we have $$\sigma_{u}^{2}=0$$ (the $$U$$-statistics is degenerate) and*

$$
n \hat{\mathrm{S}}_{u}(p, q) \stackrel{d}{\rightarrow} \sum_{j=1}^{\infty} c_{j}\left(Z_{j}^{2}-1\right)
$$

*where $$\left\{Z_{j}\right\}$$ are i.i.d. standard Gaussian random variables, and $$\left\{c_{j}\right\}$$ are the eigenvalues of kernel $$u_{q}\left(x, x^{\prime}\right)$$ under $$p(x)$$ that is, they are the solutions of*

$$
c_{j} \phi_{j}(x)= \int_{x^{\prime}} u_{q}\left(x, x^{\prime}\right) \phi_{j}\left(x^{\prime}\right) p\left(x^{\prime}\right) d x^{\prime}
$$

*for non-zero $$\phi_{j}$$.*


The above theorem allows us to reduce the testing of $$p=q$$ to the following hypothesis testing.

$$
H_{0} : \mathbb{E}_{p}\left[u_{q}\left(x, x^{\prime}\right)\right]=0 \quad \text{vs.} \quad H_{1} : \mathbb{E}_{p}\left[u_{q}\left(x, x^{\prime}\right)\right]>0
$$
