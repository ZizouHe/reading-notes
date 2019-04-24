# A Linear-Time Kernel Goodness-of-Fit Test

- [Jitkrittum, W., Xu, W., Szabó, Z., Fukumizu, K., & Gretton, A. (2017). A linear-time kernel goodness-of-fit test. In Advances in Neural Information Processing Systems (pp. 262-271).](http://papers.nips.cc/paper/6630-a-linear-time-kernel-goodness-of-fit-test.pdf)

- [Wittawat Jitkrittum's Github Python Package](https://github.com/wittawatj/kernel-gof)

- [Previous work on kernel Stein Discrepancy test](./KSD_test.html)

## Summary

The main drawback of the KSD test ([Liu, et al. 2016](https://arxiv.org/pdf/1602.03253.pdf)) is its high computational cost of O(n2). The Linear-Time Kernel test is one order of magnitude faster. Unfortunately, the decrease in the test power outweighs the computational gain. This paper seek a variant of the KSD statistic that can be computed in linear time, and whose test power is comparable to the KSD test.
