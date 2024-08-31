# Machine Learning Interpretation

- [Molnar, Christoph. *Interpretable machine learning*. Chapter 9](https://christophm.github.io/interpretable-ml-book/local-methods.html)

## Local Surrogate

- [LIME](https://christophm.github.io/interpretable-ml-book/lime.html)
- [Ribeiro et al. (2016 KDD). "Why should I trust you?" Explaining the predictions of any classifier.](https://dl.acm.org/doi/abs/10.1145/2939672.2939778)
- Steps:
  - Select your instance of interest for which you want to have an explanation of its black box prediction, and K features that you want to explain.
  - Perturb your dataset and get the black box predictions for these new points. 
  - Weight the new samples according to their proximity to the instance of interest. (define neighborhood, e.g., use kernel smoothing)
  - Train a weighted, interpretable model on the dataset with the variations. 
  - Explain the prediction by interpreting the local model.
- Disadvantage:
  - The correct definition of the neighborhood is a very big, unsolved problem when using LIME with tabular data. 

## Shapley Values

- [Shapley Values](https://christophm.github.io/interpretable-ml-book/shapley.html)

The Shapley value of a feature value is its contribution to the payout, weighted and summed over all possible feature value combinations:
$$
\phi_j(v a l)=\sum_{S \subseteq\{1, \ldots, p\} \backslash\{j\}} \frac{|S| !(p-|S|-1) !}{p !}(\operatorname{val}(S \cup\{j\})-\operatorname{val}(S))
$$
where $$S$$ is a subset of the features used in the model, $$\mathrm{x}$$ is the vector of feature values of the instance to be explained and $$\mathrm{p}$$ the number of features. $$v a l_x(S)$$ is the prediction for feature values in set $$\mathrm{S}$$ that are marginalized over features that are not included in set $$\mathrm{S}$$
$$
v a l_x(S)=\int \hat{f}\left(x_1, \ldots, x_p\right) d \mathbb{P}_{x \notin S}-E_X(\hat{f}(X)), \; \; E_X(\hat{f}(X)) = \int_X \hat{f}\left(x_1, \ldots, x_p\right) d \mathbb{P}_{X}
$$
An intuitive way to understand the Shapley value is the following illustration: The feature values enter a room in random order. All feature values in the room participate in the game (= contribute to the prediction). The Shapley value of a feature value is the average change in the prediction that the coalition already in the room receives when the feature value joins them. (**the coefficient **$$\frac{|S| !(p-|S|-1) !}{p !}$$ **is the probability that features enters the room in this order**)

1. **Efficiency** The feature contributions must add up to the difference of prediction for x and the average.
   $$
   \sum_{j=1}^p \phi_j=\hat{f}(x)-E_X(\hat{f}(X))
   $$

2. **Additivity** For a game with combined payouts $$val+val^+$$ the respective Shapley values are as follows:
   $$
   \phi_j+\phi_j^{+}
   $$
   Suppose you trained a random forest, which means that the prediction is an average of many decision trees. **The Additivity property guarantees that for a feature value, you can calculate the Shapley value for each tree individually, average them, and get the Shapley value for the feature value for the random forest.**

## SHAP

- [SHAP](https://christophm.github.io/interpretable-ml-book/shap.html)
- [Lundberg and Lee (2017 NIPS) A unified approach to interpreting model predictions.](https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html)

SHAP (SHapley Additive exPlanations) is a unified measure of feature importance that provides a consistent way to interpret the output of any machine learning model. It is based on the concept of Shapley values, which originate from cooperative game theory. Shapley values are used to fairly distribute a payoff among players in a game, taking into account their individual contributions to the overall outcome.

The process to compute SHAP values is complex, as it involves several steps, including kernel functions, optimizations, and approximations. Here is a high-level overview:

1. For a given instance, use a reference dataset to create a set of perturbed instances. For example, if the instance is $$X^j = (X^j_1, \ldots, X^j_d) \in \R^d$$. Each perturbed instance is created by "masking" a subset of the features. Denote the mask vector as $$z^j \in [0,1]^d$$ where the $$z_i^j = 0$$ means a mask on the feature $$X_i^j$$ and $$z_i^j = 1$$ means keeping the original values of the feature $$X_i^j$$. There are several ways of conduct musking:

   - replacing them with their average values in the reference dataset (assume model linearity)

   - sample values from the reference dataset, Monte-Carlo approximation to the marginalization below (assume features are independent)
     $$
     \int f(X) \, \mathrm{d} \, X_S, \; \; \text{where S is the set of masked features}.
     $$

   - For tree-based model, can use conditional expectation, by averaging all the feasible paths of the tree given unmasked feature values, this is fast but not valid in theory. See [TreeSHAP](https://christophm.github.io/interpretable-ml-book/shap.html#treeshap)

2. For each perturbed instance, obtain the prediction from the original model. We now obtained a pertubed dataset $$\{(z^j, f(\widetilde(X)^j))\}$$.

3. Train a weighted linear regression model on the perturbed instances where the weight is given by SHAP kernel, and the loss function is
   $$
   \begin{aligned}
   \mathcal{L} &= \sum_{j=1}^N \left[f(\widetilde(X)^j - g(z^j)\right]^2 w(z^j), \\
   \text{where} \;\; g(z) &= \phi_0 + \sum_{i=1}^d \phi_i z_i, \; \; 
   \text{and } w(\cdot) \text{ is the SHAP kernel}
   \end{aligned}
   $$

4. The Shapley value for this instance for each feature is given by the coefficient in linear model $$\phi_1, \ldots, \phi_d$$.

## Permutation importance

Permutation importance is a model-agnostic method that measures the impact of a feature on the model's performance by randomly shuffling the values of that feature and observing the change in the model's performance metric (e.g., accuracy, F1-score, or mean squared error). The idea is that if a feature is important, then shuffling its values should lead to a significant decrease in the model's performance.

To calculate permutation importance, follow these steps:

- Train a model on the dataset and record its performance on a validation or test set.
- For each feature, shuffle its values, leaving the other features unchanged. Then, re-evaluate the model's performance on the modified dataset.
- Calculate the difference between the model's performance with the shuffled feature and its performance on the original dataset.
- The larger the difference, the more important the feature is. Repeat the process multiple times to obtain a more reliable estimate of feature importance.

## LightGBM Feature Importance

In LightGBM, feature importance is calculated using two common methods: Gain and Split.

1. Gain: Gain is the improvement in the model's performance (measured by a reduction in the loss function) that can be attributed to a particular feature when used in a tree. It is calculated by summing the gains across all the trees in the ensemble where the feature is used to split a node. Features with a higher total gain are considered more important.

   Mathematically, the gain is the difference between the loss before and after a split. It can be represented as:
   $$
   Gain = Loss(\text{parent)}) - [Loss(\text{left\_child)}) + Loss(\text{right\_child)}].
   $$
   

   To calculate feature importance based on gain, LightGBM sums the gain values of each feature across all trees in the model. Features with higher total gain values are considered more important.

2. Split: The split method simply counts the number of times a feature is used to split the data across all trees in the model. Features that are used more frequently for splitting are considered more important. This method does not consider the magnitude of improvement a feature brings to the model.
