# Riemann manifold Langevin and Hamiltonian Monte Carlo methods

- [Girolami, M., & Calderhead, B. (2011). Riemann manifold langevin and hamiltonian monte carlo methods. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 73(2), 123-214.](https://rss.onlinelibrary.wiley.com/doi/pdf/10.1111/j.1467-9868.2010.00765.x)

- [Python Implementation](https://github.com/ehbihenscoding/Riemann_manifold_HMCM)

## Summary

This paper extend two MCMC algorithms: Metropolis adjusted Langevin and Hamiltonian Monte Carlo from Euclidean space to Riemann manifold to resolve the shortcomings of existing Monte Carlo algorithms when sampling from target densities that may be high dimensional and exhibit strong correlations. This is done by utilizing the geometry information associated with probability density function.


## Enlightenment from Metropolis Adjusted Langevin and HMC

### Metropolis Adjusted Langevin

Based on a Langevin diffusion, the SDE with stationary distribution $$p(\boldsymbol{\theta})$$ is

$$
\mathrm{d} \theta(t)=\nabla_{\boldsymbol{\theta}} \mathcal{L}\{\boldsymbol{\theta}(t)\} \mathrm{d} t / 2+\mathrm{d}\boldsymbol{b}(t)
$$

where $$\mathcal{L}(\boldsymbol{\theta}) \equiv \log \{p(\boldsymbol{\theta})\}$$ and $$\mathbf{b}$$ denotes a D-dimensional Brownian motion. A first-order Euler discretization of the SDE gives the proposal mechanism

$$
\boldsymbol{\theta}^{*}=\boldsymbol{\theta}^{n}+\varepsilon^{2} \nabla_{\boldsymbol{\theta}} \mathcal{L}\left(\boldsymbol{\theta}^{n}\right) / 2+\varepsilon \mathbf{z}^{n}
$$

where $$\mathbf{z} \sim \mathcal{N}(\mathbf{z} | \mathbf{0}, \mathbf{I})$$ and $$\epsilon$$ is the integration step size. Notice that the error this discretization introduces can be corrected by employing a Metropolis acceptance probability after each integration step.

Although the drift term in the proposal mechanism for the Metropolis Adjusted Langevin defines the direction for the proposal based on the gradient information, it is clear that the isotropic diffusion will be inefficient for strongly correlated variables $$\boldsymbol{\theta}$$ with widely differing variances forcing the step size to accommodate the variate with smallest variance. This issue can be circumvented by employing a preconditioning matrix $$M$$ such that

$$
\boldsymbol{\theta}^{*}=\boldsymbol{\theta}^{n}+\varepsilon^{2} \mathbf{M} \nabla_{\boldsymbol{\theta}} \mathcal{L}\left(\boldsymbol{\theta}^{n}\right) / 2+\varepsilon \sqrt{\mathbf{M} \mathbf{z}}^{n}
$$

### HMC

With a auxiliary variable $$\boldsymbol{p} \sim \mathcal{N}(\boldsymbol{0}, M)$$, we can define the negative joint log-probability as

$$
H(\boldsymbol{\theta}, \mathbf{p})=-\mathcal{L}(\boldsymbol{\theta})+\frac{1}{2} \log \left\{(2 \pi)^{D}|\mathbf{M}|\right\}+\frac{1}{2} \mathbf{p}^{\mathrm{T}} \mathbf{M}^{-1} \mathbf{p}
$$

where the kinetic energy term $$\mathbf{p}^{\mathrm{T}} \mathbf{M}^{-1} \mathbf{p} / 2$$ where the covariance matrix $$\mathbf{M}$$ denotes a mass matrix.

**It can be shown that the discrete version of HMC (leapfrog method) is equivalent to a Metropolis Adjusted Langevin with precondition matrix $$\mathbf{M}$$**.

## Geometry Information in Probability

A distance metric based on a first order expression for the symmetric Kullback-Liebler divergence between two densities $$p$$ and $$q$$ is defined as

$$
D_{\mathcal{S}}(p \| q)=D(p \| q)+D(q \| p)
$$

Therefore, up to a small term, we have

$$
D_{\mathcal{S}}(p(\mathbf{y} ; \boldsymbol{\theta}+\delta \boldsymbol{\theta}) \| p(\mathbf{y} ; \boldsymbol{\theta})) = \delta \boldsymbol{\theta}^{\top} E_{\mathbf{y} | \boldsymbol{\theta}}\left\{\nabla_{\boldsymbol{\theta}} \log p(\mathbf{y} ; \boldsymbol{\theta}) \nabla_{\boldsymbol{\theta}} \log p(\mathbf{y} ; \boldsymbol{\theta})^{\top}\right\} \delta \boldsymbol{\theta}=\delta \boldsymbol{\theta}^{\top} \mathbf{G}(\boldsymbol{\theta}) \delta \boldsymbol{\theta}
$$

where $$\mathbf{G}(\boldsymbol{\theta})$$ is the Fisher Information matrix.

The parameter space of a statistical model is a Riemannian manifold. Therefore
the natural geometric structure of the density model $$p(\boldsymbol{\theta})$$ is defined by the Riemannian manifold and associated metric tensor. Given this geometric structure of the parameter space of statistical models the appropriate adoption of the position specific metric, $$\mathbf{G}(\boldsymbol{\theta})$$, within an MCMC scheme should yield more effective transitions in the overall algorithm.

## Manifold Metropolis adjusted Langevin algorithm

Given the geometric structure for probability models a Langevin diffusion with invariant measure $$p(\boldsymbol{\theta})$$ can be defined directly upon the Riemannian manifold with metric tensor $$\mathbf{G}(\boldsymbol{\theta})$$:

$$
d \boldsymbol{\theta}(t)=\frac{1}{2} \tilde{\nabla}_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta}(t)) d t+d \tilde{\mathbf{b}}(t)
$$

where

$$
\tilde{\nabla}_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta}(t))=\mathbf{G}^{-1}(\boldsymbol{\theta}(t)) \nabla_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta}(t))
$$

and

$$
d \tilde{\mathbf{b}}_{i}(t)=|\mathbf{G}(\boldsymbol{\theta}(t))|^{-1 / 2} \sum_{j=1}^{D} \frac{\partial}{\partial \boldsymbol{\theta}_{j}}\left(\mathbf{G}^{-1}(\boldsymbol{\theta}(t))_{i j}|\mathbf{G}(\boldsymbol{\theta}(t))|^{1 / 2}\right) d t+\left(\sqrt{\mathbf{G}^{-1}(\boldsymbol{\theta}(t))} d \mathbf{b}(t)\right)_{i}
$$

## Riemann manifold Hamiltonian Monte Carlo methods

Similarly, we can replace the covariance matrix $$M$$ with $$\mathbf{G}(\boldsymbol{\theta})$$:

$$
H(\boldsymbol{\theta}, \mathbf{p})=-\mathcal{L}(\boldsymbol{\theta})+\frac{1}{2} \log \left((2 \pi)^{D}|\mathbf{G}(\boldsymbol{\theta})|\right)+\frac{1}{2} \mathbf{p}^{\top} \mathbf{G}(\boldsymbol{\theta})^{-1} \mathbf{p}
$$

and the marginal density of $$p(\boldsymbol{\theta})$$ does not depend on $$\mathbf{p}$$.
