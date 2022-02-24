# Sharp Minima Can Generalize For Deep Nets

- [Dinh, L., Pascanu, R., Bengio, S., & Bengio, Y. (2017, August). Sharp minima can generalize for deep nets. In Proceedings of the 34th International Conference on Machine Learning-Volume 70 (pp. 1019-1028).](https://arxiv.org/pdf/1703.04933.pdf)

## Summary

This paper criticizes some previous definitions of sharpness (for the local minima of loss function) to be unsuitable under the settings of deep neural networks. However, this phenomenon is because the loss function of deep neural networks typically cannot guarantee the positive definite property of Hessian matrix around local minima and those definitions of sharpness usually require some assumptions include positive definite Hessian and smoothness to guarantee the generalization property.

## Proof using Re-parameterization Tricks

Deep neural network has the issue of over-parameterization. Consider a one-hidden layer network, $$\boldsymbol{y} = \sigma(\boldsymbol{x} \boldsymbol{\theta_1}) \boldsymbol{\theta_2}$$ with ReLU as activation function $$\sigma(\cdot)$$, a transformation $$T_\alpha(\cdot)$$ on the parameter space $$(\boldsymbol{\theta_1}, \boldsymbol{\theta_2})$$ is

$$
T_\alpha(\cdot): (\boldsymbol{\theta_1}, \boldsymbol{\theta_2}) \rightarrow (\alpha \boldsymbol{\theta_1}, \alpha^{-1} \boldsymbol{\theta_2})
$$

This transformation can be extended to deeper networks and convolution layer can also be included. For the sharpness defined below,

**Definition.** *Given $$\varepsilon > 0$$, a minimum $$\theta$$, and a loss $$L$$, we define $$C(L, \theta, \varepsilon)$$ as the largest (using inclusion as the partial order over the subsets of $$\theta$$) connected set containing $$\theta$$ such that $$\forall \theta^\prime \in C(L,\theta,\varepsilon), L(\theta′) < L(\theta) + \varepsilon$$. The $$\varepsilon$$-flatness will be defined as the volume of $$C(L, \theta, \varepsilon)$$. We will call this measure the volume $$\varepsilon$$-flatness.*

**Definition.** *Let $$\mathcal{B}_2(\varepsilon,\theta)$$ be an Euclidean ball centered on a minimum $$\theta$$ with radius $$\varepsilon$$. Then, for a non-negative valued loss function $$L$$, the $$\varepsilon$$-sharpness will be defined as proportional to*

$$
\frac{\max _{\theta^{\prime} \in \mathcal{B}_{2}(\epsilon, \theta)}\left(L\left(\theta^{\prime}\right)-L(\theta)\right)}{1+L(\theta)} \approx \frac{\left|\left\|\left(\nabla^{2} L\right)(\theta)\right\|\right|_{2} \epsilon^{2}}{2(1+L(\theta))}
$$

we can use re-parameterization trick to get the result that for neural networks defined above, $$C(L, \theta, \varepsilon)$$ has infinite volume and $$\varepsilon$$-sharpness can be arbitrarily large or small without changing the generalization power.

Moreover, for any Hessian-based or Jacobian-based definition, it is not valid to be considered in deep neural networks settings.

