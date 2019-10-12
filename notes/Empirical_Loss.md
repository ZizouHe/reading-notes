# An Empirical Analysis of the Optimization of Deep Network Loss Surfaces

- [Im, D. J., Tao, M., & Branson, K. (2016). An empirical analysis of the optimization of deep network loss surfaces. arXiv preprint arXiv:1612.04010.](https://arxiv.org/pdf/1612.04010.pdf)

## Summary

This paper empirically analyzes the loss function properties of five popular SGD optimization methods: SGD, SGD with Momentum, RMSprop, Adadelta and Adam. It comes to the following conclusions:

1. Different optimization algorithms find different solutions within the projected space. This is true even when starting from the same initialization with the same mini-batch and dropout settings. Most surprisingly, this remained true when we switched from one optimization algorithm to another after the training error has nearly plateaued, suggesting that there are a plethora of saddle points even near the convergence points. 
2. Despite corresponding to different final points, the loss surfaces for the same algorithm from different initializations are remarkably consistent and characteristic of the optimization algorithm. The shapes of the loss functions near the final solution differ across algorithms, and we trace this back to different algorithms selecting weight vectors with a consistent norm. Switching from one optimization algorithm to another late in training results in a final point characteristic of the second optimization algorithm. 
3. Batch normalization is key to obtaining this consistency in the projected loss surface. Without it, we see much more variability across re-runs from different initializations. 

