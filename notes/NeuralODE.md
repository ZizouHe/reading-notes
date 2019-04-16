## Neural Ordinary Differential Equations

- [Chen, T. Q., Rubanova, Y., Bettencourt, J., & Duvenaud, D. K. (2018). Neural ordinary differential equations. In Advances in Neural Information Processing Systems (pp. 6572-6583).](http://papers.nips.cc/paper/7892-neural-ordinary-differential-equations.pdf)

- [Author's code](https://github.com/rtqichen/torchdiffeq/)

### Summary

- **Memory efficiency**: Not storing any intermediate quantities of the forward pass allows us to train our models with constant memory cost as a function of depth, a major bottleneck of training deep models.

- **Adaptive computation**: Modern ODE solvers provide guarantees about the growth of approximation error, monitor the level of error, and adapt their evaluation strategy on the fly to achieve the requested level of accuracy. This allows the cost of evaluating a model to scale with problem complexity.

- **Parameter efficiency**: When the hidden unit dynamics are parameterized as a continuous function of time, the parameters of nearby “layers” are automatically tied together which reduces the number of parameters required on a supervised learning task.

- **Scalable and invertible normalizing flows**: the change of variables formula becomes easier to compute therefore it can avoid the single-unit bottleneck of normalizing flows, and can be trained directly by maximum likelihood.

### Feedforward structure

This paper introduce a new family of deep neural network models. Instead of a series of discrete hidden layer, as

$$
\mathbf { h } _ { t + 1 } = \mathbf { h } _ { t } + f \left( \mathbf { h } _ { t } , \theta _ { t } \right)
$$

the deep neural network can be parameterized by a continuous dynamics of hidden units using an ordinary differential equation scheme

$$
\frac { d \mathbf { h } ( t ) } { d t } = f ( \mathbf { h } ( t ) , t , \theta )
$$

Therefore, the traditional network can be seen as this function $$f ( \mathbf { h } ( t ) , t , \theta )$$. And the feedforward step can be solved by a black-box differential equation solver.

### Backpropogate scheme

The backpropogation step is as follows. Consider the loss function,

$$
L \left( \mathbf { h } \left( t _ { 1 } \right) \right) = L \left( \mathbf { h } \left( t _ { 0 } \right) + \int _ { t _ { 0 } } ^ { t _ { 1 } } f ( \mathbf { h } ( t ) , t , \theta ) d t \right) = L \left( \operatorname { ODESolve } \left( \mathbf { h } \left( t _ { 0 } \right) , f , t _ { 0 } , t _ { 1 } , \theta \right) \right)
$$

Using adjoint sensitivity method,

$$
\frac { d \mathbf { a } ( t ) } { d t } = - \mathbf { a } ( t ) ^ { \top } \frac { \partial f ( \mathbf { h } ( t ) , t , \theta ) } { \partial \mathbf { h } }, \;\; \text{where} \; \mathbf { a } ( t ) = \frac{\partial L}{\partial \mathbf { h } ( t )}
$$

this can be solved by a ODE solver once we know $$\mathbf{h}(t)$$ for any $$t_0 \leq t \leq t_1$$. This can be done by using a ODE solver of

$$
\frac { d \mathbf { h } ( t ) } { d t } = f ( \mathbf { h } ( t ) , t , \theta )
$$

with initial value $$\mathbf{h}(t_1)$$. With the knowledge of $$\frac{\partial L}{\partial \mathbf { h } ( t )}$$, the gradient can be obtained by

$$
\frac { d L } { d \theta } = - \int _ { t _ { 1 } } ^ { t _ { 0 } } \mathbf { a } ( t ) ^ { \top } \frac { \partial f ( \mathbf { h } ( t ) , t , \theta ) } { \partial \theta } d t
$$

still can be done by a ODE solver. All integrals for solving $$\mathbf{h}$$, $$\mathbf{a}$$ and $$\partial L / \partial \theta $$ can be computed in a single call to an ODE solver, which concatenates the original state, the adjoint, and the other partial derivatives into a single vector. Therefore, each step in the ODE solver, once we get $$\mathbf{h}(t)$$, we can therefore obtain $$\mathbf{a}(t)$$ and afterwards, the gradient.