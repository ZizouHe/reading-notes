# A Complete Recipe for Stochastic Gradient MCMC

- [Ma, Y. A., Chen, T., & Fox, E. (2015). A complete recipe for stochastic gradient MCMC. In Advances in Neural Information Processing Systems (pp. 2917-2925).](http://papers.nips.cc/paper/5891-a-complete-recipe-for-stochastic-gradient-mcmc.pdf)

- For an introduction to MCMC, see [my notes/Monte Carlo Sampling](https://zizouhe.github.io/stats-and-beyond/contents/MC.html).

## Summary

In this paper, a complete framework to direct the MCMC samplers has been presented. It shows that this framework is sufficient and necessary for all MCMC samplers. As many recent work try to use stochastic gradient version MCMC samplers as a consideration of computation, this method mainly introduce a systematical way to guide SGMCMC. Based on this framework, a new MCMC sampler called stochastic gradient Riemann Hamiltonian Monte Carlo (SGRHMC) has also been introduced

## A Stochastic Gradient MCMC Framework

In general, we can write all continuous Markov processes as the following form stochastic differential equation:

$$
\mathrm{d} \mathbf{z}= f(\mathbf{z}) \mathrm{d} t+ \sqrt{2 \mathrm{D}(\mathbf{z})} \mathrm{d} \mathrm{W}(t)
$$

where $$f(\mathbf{z})$$ denotes the deterministic drift and $$\mathrm{W}(t)$$ is a $$d$$-dimensional Wiener Process, and $$D(\mathbf{z})$$ is a positive semi-definite diffusion matrix. ***Notice that only some choices of $$f(\mathbf{z})$$ and $$\mathrm{D}(\mathbf{z})$$ yields a stationary distribution with the form $$p^s(\mathbf{z}) \propto \exp^{-H(\mathbf{z})}$$***. Here $$H(\mathbf{z})$$ is related to Hamiltonian MC as well as other MCMC algorithms.

This paper proposes to write $$f(\mathbf{z})$$ into the following form:

$$
\mathrm{f}(\mathbf{z})=-[\mathrm{D}(\mathbf{z})+\mathrm{Q}(\mathbf{z})] \nabla H(\mathbf{z})+\Gamma(\mathbf{z}), \quad \mathrm{P}_{i}(\mathbf{z})=\sum_{j=1}^{d} \frac{\partial}{\partial \mathbf{z}_{j}}\left(\mathrm{D}_{i j}(\mathbf{z})+\mathrm{Q}_{i j}(\mathbf{z})\right)
$$

Here $$\mathrm{Q}(\mathbf{z})$$ is a skew-symmetric curl matrix representing the deterministic traversing effects seen in HMC procedures. In contrast, the diffusion matrix $$\mathrm{D}(\mathbf{z})$$ determines the strength of the Wiener-process-driven diffusion. Matrices $$\mathrm{Q}(\mathbf{z})$$ and $$\mathrm{D}(\mathbf{z})$$ can be adjusted to attain faster convergence to the posterior distribution.

It is stated that if we specifically write $$f(\mathbf{z})$$ into the above form, then the stationary distribution of SDE has the form of $$p^s(\mathbf{z}) \propto \exp^{-H(\mathbf{z})}$$. Moreover, if the stationary distribution of SDE uniquely exists, then there exists skew-symmetric curl matrix $$\mathrm{Q}(\mathbf{z})$$ such that we can write $$f(\mathbf{z})$$ in the SDE to our specified form, and therefore the stationary distribution has our desired form.

## Practical Algorithms and Discussions

### $$\varepsilon$$-discretization Update

In practice, we choose a step size of $$\varepsilon$$ and update using the following discretized form of SDE:

$$
\mathbf{z}_{t+1} \leftarrow \mathbf{z}_{t}-\epsilon_{t}\left[\left(\mathrm{D}\left(\mathbf{z}_{t}\right)+\mathrm{Q}\left(\mathbf{z}_{t}\right)\right) \nabla H\left(\mathbf{z}_{t}\right)+\Gamma\left(\mathbf{z}_{t}\right)\right]+\mathcal{N}\left(0,2 \epsilon_{t} \mathrm{D}\left(\mathbf{z}_{t}\right)\right)
$$

In the above step, instead of evaluating the gradient using full data, we can use part of the data to do a stochastic-gradient-descent-style update in order to achieve computation efficiency. Although this SG step is unbiased, it does introduce extra noise into the training procedure. It can be shown that this noise is asymptotically normal, and we can partly subtract this noise by

$$
\mathbf{z}_{t+1} \leftarrow \mathbf{z}_{t}-\epsilon_{t}\left[\left(\mathrm{D}\left(\mathbf{z}_{t}\right)+\mathrm{Q}\left(\mathbf{z}_{t}\right)\right) \nabla \widetilde{H}\left(\mathbf{z}_{t}\right)+\Gamma\left(\mathbf{z}_{t}\right)\right]+\mathcal{N}\left(0, \epsilon_{t}\left(2 \mathrm{D}\left(\mathbf{z}_{t}\right)-\epsilon_{t} \hat{\mathrm{B}}_{t}\right)\right)
$$

where $$\widetilde{H}\left(\mathbf{z}_{t}\right)$$ is the down-sampled version of gradient and $$\hat{\mathrm{B}}_{t}$$ is our estimated noise term. It is also true that this SGD-correction training procedure also yields the correct invariant distribution.

### Construct Samplers with Proposed Framework

The authors shows that all previous MCMC methods, e.g. Hamiltonian Monte Carlo (HMC), Stochastic Gradient Hamiltonian Monte Carlo (SGHMC), Stochastic Gradient Langevin Dynamics (SGLD) as well as Stochastic Gradient Riemannian Langevin Dynamics (SGRLD) are all adapted to this framework. 

Since the matrices $$\mathrm{Q}(\mathbf{z})$$ and $$\mathrm{D}(\mathbf{z})$$ can be adjusted, a new sampler called Stochastic Gradient Riemann Hamiltonian Monte Carlo (SGRHMC) has been presented which introduces Fisher information metric as a way to utilize the geometry information of our targeted distribution. For a detailed discussion on how to use geometry information in the MCMC procedure, please refer to [Girolami, M., & Calderhead, B. (2011). Riemann manifold langevin and hamiltonian monte carlo methods. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 73(2), 123-214.](https://rss.onlinelibrary.wiley.com/doi/pdf/10.1111/j.1467-9868.2010.00765.x).