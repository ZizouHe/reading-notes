# Trust Region Policy Optimization

- [Schulman, J., Levine, S., Abbeel, P., Jordan, M., & Moritz, P. (2015, June). Trust region policy optimization. In International conference on machine learning (pp. 1889-1897).](https://arxiv.org/pdf/1502.05477.pdf)

## Abstract

- The theory justifies optimizing a surrogate objective with a penalty on KL divergence. However, the large penalty coefficient C leads to prohibitively small steps, so we would like to decrease this coefficient. Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter $$\delta$$ (the bound on KL divergence).

- The constraint on $$D_{\mathrm{KL}}^{\max }\left(\theta_{\mathrm{old}}, \theta\right)$$ is hard for numerical optimization and estimation, so instead we constrain $$\bar{D}_{\mathrm{KL}}\left(\theta_{\mathrm{old}}, \theta\right)$$

- Our theory ignores estimation error for the advantage function. Kakade and Langford (2002) consider this error in their derivation, and the same arguments would hold in the setting of this paper, but we omit them for simplicity.

## Comparison between algorithms

- Traditional gradient descent

$$
\theta^{\prime} \leftarrow \arg \max _{\theta^{\prime}}\left(\theta^{\prime}-\theta\right)^{T} \nabla_{\theta} J(\theta) \text{, s.t. } \left\|\theta^{\prime}-\theta\right\|^{2} \leq \epsilon
$$

some parameters change probabilities a lot more than others!

- We can rescale the gradient so this doesn't happen, using trust region optimization:

$$
\theta^{\prime} \leftarrow \arg \max _{\theta^{\prime}}\left(\theta^{\prime}-\theta\right)^{T} \nabla_{\theta} J(\theta) \text {, s.t. } D\left(\pi_{\theta^{\prime}}, \pi_{\theta}\right) \leq \epsilon
$$

Notice that

$$
D_{\mathrm{KL}}\left(\pi_{\theta^{\prime}} \| \pi_{\theta}\right)=E_{\pi_{\theta^{\prime}}}\left[\log \pi_{\theta}-\log \pi_{\theta^{\prime}}\right] \approx \left(\theta^{\prime}-\theta\right)^{T} \mathbf{F}\left(\theta^{\prime}-\theta\right)
$$

where $$\mathbf{F}$$ is the Fisher-information matrix,

$$
\mathbf{F}=E_{\pi_{\theta}}\left[\log \pi_{\theta}(\mathbf{a} | \mathbf{s}) \log \pi_{\theta}(\mathbf{a} | \mathbf{s})^{T}\right]
$$

- Natural policy gradient, pick $$\alpha$$

$$
\theta \leftarrow \theta+\alpha \mathbf{F}^{-1} \nabla_{\theta} J(\theta)
$$

## Computation

Fisher-information matrix $$\mathbf{F}$$ can be estimated using samples. The updated rule for TRPO is a quadratic form.

- we first solve linear system and get the direction of update:

$$
\mathbf{F} \theta = g
$$

this can be done using conjugate gradient method. 

- Having computed the search direction, we next need to compute the maximal step length which satisfies the KL divergence constraint. The solution has a analytic form.
