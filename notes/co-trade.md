# Co-trade Network

- [Lu, Reinert, and Cucuringu, 2022. Co-trading networks for modeling dynamic interdependency structures and estimating high-dimensional covariances in US equity markets]()

- [基于『成交数据』的股票联动研究](https://mp.weixin.qq.com/s/2H_EPZJovqE8TXz-mMtZ7g)

## Introduction

- Calculate pairwise co-occurrence score, calculated as follows,
  $$
  c_{t, i, j}^{\delta, d^i, d^j}:=\frac{L_{t, i \rightarrow j}^{d^i \rightarrow d^j}+L_{t, j \rightarrow i}^{d^j \rightarrow d^i}}{\sqrt{\left|S_t^{i, d^i}\right| \sqrt{\left|S_t^{j, d^j}\right|}}}
  $$
  where $$L_{t, i \rightarrow j}^{d^i \rightarrow d^j}+L_{t, j \rightarrow i}^{d^j \rightarrow d^i}$$ is the total co-trade between stock i,j. 

- Could conduct clustering based on co-occurrence matrix (similarity matrix).

- **Some thoughts:**

  - could find a way to regress co-occurrence matrix on industry matrix, i.e.,

    ![](/Users/Zizou/Zizou/Paper/reading-notes/notes/pic/QAP.png)Or we can obtain the eigenvectors and take the orthogonal part of the top-K eigenvectors of industry matrix.


  $$
  C = \sum_{k=1}^d \lambda_k \hat{v}_k \hat{v}_k^\top, \; \; v_k = \beta \cdot U_K + \hat{v}_k
  $$

  - remove noise impact, by set a threshold on the co-occurrence score, or take top-K eigenvalue, eigenvectors from co-occurrence matrix.