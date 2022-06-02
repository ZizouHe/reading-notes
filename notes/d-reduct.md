# Nonlinear Dimension Reduction

## UMAP

- [McInnes, Leland, John Healy, and James Melville. "Umap: Uniform manifold approximation and projection for dimension reduction." *arXiv preprint arXiv:1802.03426* (2018).](https://arxiv.org/abs/1802.03426)
- [UMAP Python Library Document](https://umap-learn.readthedocs.io/en/latest/index.html)
- [Leland McInnes - UMAP Talk](https://www.youtube.com/watch?v=nq6iPZVUxZU&t=1397s)
- [How Exactly UMAP Works and why exactly it is better than t-SNE](https://towardsdatascience.com/how-exactly-umap-works-13e3040e1668)

## Details

- Assumption: Data is uniformly distributed on the manifold.
  - Define Riemannian metric on manifold to make the assumption true.
- Assumption: The manifold is locally connected.
- Graph with combined edge weights

- t-SNE preserves only local structure (KL divergence) while UMAP can preserve global structure (cross entropy)
- UMAP find approximate nearest neighbours very efficiently (even in high-d space)
  - Random-projection tree + nearest neighbour descent
  - SGD + negative sampling (avoid the curse of dimensionality and can do dimension reduction over 3-d, unlike t-SNE)
- Use Python + Numba (custom distance metrics as long as it can be compiled by JIT)
- Can make use of labels for supervised dimension reduction
- combine different distance (categorical data, discrete data, etc.)

## t-SNE

- [Van der Maaten, Laurens, and Geoffrey Hinton. "Visualizing data using t-SNE." *Journal of machine learning research* 9, no. 11 (2008).](https://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf?fbclid=IwA)

- [How Exactly UMAP Works and why exactly it is better than t-SNE](https://towardsdatascience.com/how-exactly-umap-works-13e3040e1668)