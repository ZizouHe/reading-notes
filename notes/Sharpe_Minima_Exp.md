# On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima

- [Keskar, N. S., Mudigere, D., Nocedal, J., Smelyanskiy, M., & Tang, P. T. P. (2016). On large-batch training for deep learning: Generalization gap and sharp minima. arXiv preprint arXiv:1609.04836.](https://arxiv.org/pdf/1609.04836.pdf)

## Summary

This paper discusses the phenomenon the generalization gap (test error drop) for the large-batch SGD. It states that large-batch SGD training is more likely to converge to the sharp minima while the small-batch SGD converges to the flat minima, which is due to the inherent noise in the training.

## Generalization Gap for Large-batch

Empirically, large-batch SGD experience a drop in test error and by experiment, we can check that this is not caused by over-fitting. Another explanation could be sharpness, as in the lens of the minimum description length (MDL) theory, which states that statistical models that require fewer bits to describe generalize better. Since flat minima can be specified with lower precision than to sharp minima, they tend to have better generalization performance. Alternative theory of sharpness and generalization are presented through the Bayesian view of learning and the lens of free Gibbs energy.

## Sharpness and Explanation

As defined in the paper, let

$$
\mathcal{C}_{\epsilon}=\left\{z \in \mathbb{R}^{p} :-\epsilon\left(\left|\left(A^{+} x\right)_{i}\right|+1\right) \leq z_{i} \leq \epsilon\left(\left|\left(A^{+} x\right)_{i}\right|+1\right) \quad \forall i \in\{1,2, \cdots, p\}\right\}
$$

where $$A^+$$ denotes the pseudo-inverse of $$A \in \mathbb{R}^{n \times p}$$ and $$\epsilon > 0$$ controls the size of the box. Therefore, we define the $$\left(\mathcal{C}_{\epsilon}, A\right)$$-sharpness of $$f$$ at $$x$$ as:

$$
\phi_{x, f}(\epsilon, A) :=\frac{\left(\max _{y \in \mathcal{C}_{\epsilon}} f(x+A y)\right)-f(x)}{1+f(x)} \times 100
$$

Using the defined sharpness, the local minima found by large-batch method has larger sharpness than that found by small-batch empirically.

Although they are all unbiased gradient estimators, large-batch has small variance which makes it more likely to be stuck in a sharp minima. However, as small-batch introduces much more noise, it has the property of exploration and therefore can avoid the trap of sharp minima. Large-batch methods lack this explorative properties of small-batch methods and tend to zoom-in on the minima closest to the initial point.

**However, this definition of sharpness is not very rigorous in a deep neural network setting, as will be shown in [*Sharp minima can generalize for deep nets.*](./Sharpe_Minima_Works.html)**
