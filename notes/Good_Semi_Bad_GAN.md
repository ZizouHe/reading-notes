# Good Semi-supervised Learning that Requires a Bad GAN

- [Dai, Z., Yang, Z., Yang, F., Cohen, W. W., & Salakhutdinov, R. R. (2017). Good semi-supervised learning that requires a bad gan. In Advances in neural information processing systems (pp. 6510-6520).](http://papers.nips.cc/paper/7229-good-semi-supervised-learning-that-requires-a-bad-gan.pdf)

## Summary

This paper shows that given a discriminator objective, good semi-supervised learning indeed requires a bad generator, and propose the definition of a preferred generator.

## Problem Setups

Given a labeled set $$L = \{(x, y)\}$$, let $$\{1, 2, \cdots , K\}$$ be the label space for classification. Let $$D$$ and $$G$$ denote the discriminator and generator, and $$P_D$$ and $$p_G$$ denote the corresponding distributions. Consider the discriminator objective function of GAN-based semi-supervised learning, (this is the standard objective function for GAN-based semi-supervised learning)
$$
\max _{D} \mathbb{E}_{x, y \sim \mathcal{L}} \log P_{D}(y | x, y \leq K)+\mathbb{E}_{x \sim p} \log P_{D}(y \leq K | x)+\mathbb{E}_{x \sim p_{G}} \log P_{D}(K+1 | x)
$$
where $$P$$ is the true data distribution. The probability distribution $$P_D$$ is over $$K + 1$$ classes where the first $$K$$ classes are true classes and the ($$K + 1$$)-th class is the fake class. The objective function consists of three terms. The first term is to maximize the log conditional probability for labeled data, which is the standard cost as in supervised learning setting. The second term is to maximize the log probability of the first $$K$$ classes for unlabeled data. The third term is to maximize the log probability of the ($$K + 1$$)-th class for generated data.

Let $$f(x)$$ be a nonlinear vector-valued function, and $$w_k$$ be the weight vector for class $$k$$. The discriminator $$D$$ can be defined as
$$
P_{D}(k | x)=\frac{\exp \left(w_{k}^{\top} f(x)\right)}{\sum_{k^{\prime}=1}^{K+1} \exp \left(w_{k^{\prime}}^{\top} f(x)\right)}
$$
Since this is a form of over-parameterization, $$w_{K+1}$$ is fixed as a zero vector.

## Perfect generator

**Theorem.** *If the generator distribution $$p_G$$ matches the truen data distribution $$p$$, i.e. $$p_G = p$$, and discriminator $$D$$ has infinite capacity, then for any optimal solution $$D = (w,f)$$ of the following supervised objective,*
$$
\max _{D} \mathbb{E}_{x, y \sim \mathcal{L}} \log P_{D}(y | x, y \leq K)
$$
*there exists $$D^* = (w^*, f^*)$$ such that $$D^*$$ maximizes the semi-supervised cost function and that for all $$x$$, $$P_{D}(y | x, y \leq K) = P_{D^*}(y | x, y \leq K)$$.*

This theorem states that given a perfect generator, there is no benefit for introducing the unlabeled data, i.e. the discriminator cannot improved by unsupervised part.

## Complement generator

The function $$f$$ maps data points in the input space to the feature space. Let $$p_k(f)$$ be the density of the data points of class $$k$$ in the feature space. Given a threshold $$\epsilon_k$$, let $$F_k$$ be a subset of the data support where $$p_{k}(f)>\epsilon_{k},$$ i.e., $$F_{k}=\left\{f : p_{k}(f)>\epsilon_{k}\right\}$$. We assume that given $$\left\{\epsilon_{k}\right\}_{k=1}^{K}$$, the $$F_k$$’s are disjoint with a margin.

Suppose $$\cup_{k=1}^{K} F_{k}$$ is bounded by a convex set $$\mathcal{B}$$. If the support $$F_G$$ of a generator $$G$$ in the feature space is a relative complement set in $$\mathcal{B}$$, i.e., $$F_{G}=\mathcal{B}-\cup_{k=1}^{K} F_{k}$$, we call $$G$$ a complement generator.

Then the paper states that when $$G$$ is a complement generator, under mild assumptions, a near- optimal $$D$$ learns correct decision boundaries in each high-density subset $$F_k$$ (defined by $$\epsilon_k$$) of the data support in the feature space. Intuitively, the generator generates complement samples so the logits of the true classes are forced to be low in the complement. As a result, the discriminator obtains class boundaries in low-density areas.

## Pros and cons of feature matching

By matching the first-order moment by SGD, feature matching is performing some kind of distribution matching, though in a rather weak manner. Loosely speaking, feature matching has the effect of generating samples close to the manifold. But due to its weak power in distribution matching, feature matching will inevitably generate samples outside of the manifold, especially when the data complexity increases. Consequently, the generator density $$p_G$$ is usually lower than the true data density $$p$$ within the manifold and higher outside. Hence, an optimal discriminator $$P_{D^*} (K+1 | x)=p(x) /\left(p(x)+p_{G}(x)\right)$$ could still distinguish between true and generated samples in many cases.
