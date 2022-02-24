# Path-sgd: Path-normalized Optimization in Deep Neural Networks

- [Neyshabur, B., Salakhutdinov, R. R., & Srebro, N. (2015). Path-sgd: Path-normalized optimization in deep neural networks. In Advances in Neural Information Processing Systems (pp. 2422-2430).](http://papers.nips.cc/paper/5797-path-sgd-path-normalized-optimization-in-deep-neural-networks.pdf)

- [Neyshabur, B., Tomioka, R., Salakhutdinov, R., & Srebro, N. (2017). Geometry of optimization and implicit regularization in deep learning. arXiv preprint arXiv:1705.03071.](https://arxiv.org/pdf/1705.03071.pdf)

- [Python Implementation](https://github.com/bneyshabur/path-sgd)

## Summary

The authors introduce a new regularizer, $$l_p$$-path regularizer and its corresponding SGD method, path-SGD. They show that both $$l_p$$-path regularizer and path-SGD are rescaling-free, and this rescaling-free property matches with the same property of a feed-forward neural network. They also show that traditional SGD does not share this property and therefore cannot optimize with the information of the geometry of the parameter space of deep networks.
