# Near-optimal Sample Complexity Bounds for Robust Learning of Gaussians Mixtures via Compression Schemes

- [Ashtiani, H., Ben-David, S., Harvey, N. J., Liaw, C., Mehrabian, A., & Plan, Y. (2018). Near-optimal sample complexity bounds for robust learning of Gaussians mixtures via compression schemes. URL https://arxiv. org/abs/1710, 5209.](https://www.cs.ubc.ca/~nickhar/Publications/MixtureOfGaussians/MixtureOfGaussians.pdf)

- [NIPS version](http://papers.nips.cc/paper/7601-nearly-tight-sample-complexity-bounds-for-learning-mixtures-of-gaussians-via-sample-compression-schemes.pdf)

## Summary

This paper prove that $$\widetilde{\Theta}\left(k d^{2} / \varepsilon^{2}\right)$$ samples are necessary and sufficient for learning a mixture of $$k$$ Gaussians in $$\mathbb{R}^d$$, up to error $$\varepsilon$$ in total variation distance. The near optimality is because $$\widetilde{O}(\cdot)$$ notation hides a polylog $$(k d / \varepsilon \delta)$$ factor. The upper bound is shown using a novel technique for distribution learning based on a notion of compression. Any class of distributions that allows such a compression scheme can also be learned with few samples. Furthermore, if a class of distributions has such a compression scheme, then so do the classes of products and mixtures of those distributions.

## Definition

**Definition.** *Let $$f_1$$ and $$f_2$$ be two probability distributions defined over $$\mathbb{R}^d$$, their* ***total variation distance*** *is defined by*

$$
\mathrm{TV}\left(f_{1}, f_{2}\right) :=\sup _{B \subseteq \mathbb{R}^{d}} \int_{B}\left(f_{1}(x)-f_{2}(x)\right) \mathrm{d} x=\frac{1}{2}\left\|f_{1}-f_{2}\right\|_{1}
$$

where $$\|f\|_{1} :=\int_{\mathbb{R}^{d}}|f(x)| \mathrm{d} x$$ is the $$L_{1}$$ norm of $$f$$.

**Definition.** *A distribution $$\hat{g}$$ is an $$\varepsilon$$-approximation for $$g$$ if $$\| \hat{g} - g \|_2 \leq \varepsilon$$. We also say $$\hat{g}$$ is $$\varepsilon$$-close to $$g$$. A distribution $$\hat{g}$$ is an $$(\varepsilon, C)$$-approximation for $$g$$ with respect to $$\mathcal{F}$$ if*

$$
\|\hat{g}-g\|_{1} \leq C \cdot \inf _{f \in \mathcal{F}}\|f-g\|_{1} + \varepsilon
$$

## Compression Scheme

Let $$\mathcal{F}$$ be a class of distributions over a domain $$Z$$.

**Definition.** *A distribution decoder for $$\mathcal{F}$$ is a deterministic function $$\mathcal{J} : \bigcup_{n=0}^{\infty} Z^{n} \times \bigcup_{n=0}^{\infty}\{0,1\}^{n} \rightarrow \mathcal{F}$$, which takes a finite sequence of elements of $$Z$$ and a finite sequence of bits, and outputs a member of $$\mathcal{F}$$*

**Definition.** *Let $$\tau, t, m :(0,1) \rightarrow \mathbb{Z}_{ \geq 0}$$ be functions, and let $$r \geq 0$$. We say $$\mathcal{F}$$ admits $$(\tau, t, m) r$$-robust compression if there exists a decoder $$\mathcal{J}$$ for $$\mathcal{F}$$ such that for any distribution $$g \in \mathcal{F},$$ and for any distribution q on $$Z$$ with $$\|g-q\|_{1} \leq r,$$ the following holds:*

*For any $$\varepsilon \in(0,1),$$ if a sample $$S$$ is drawn from $$q^{m(\varepsilon) \log 1 / \delta},$$ then with probability at least $$1 - \delta$$, there exists a sequence $$L$$ of at most $$\tau(\varepsilon)$$ elements of $$S$$, and a sequence $$B$$ of at most $$t(\varepsilon)$$ bits, such that $$\|\mathcal{J}(L, B)-g\|_{1} \leq \varepsilon$$*

Note that here $$q$$ can be seen as a corrupted version of real distribution $$g$$, and the data is drawn from this corrupted one. And here $$L$$ and $$B$$ are sequences therefore can contain repeated elements. Essentially, the definition asserts that with probability $$2/3$$, there is a (short) sequence of elements $$S$$ and some (small number of) additional bits, from which $$g$$ can be approximately reconstructed.

**Theorem.** *There exists a deterministic algorithm that, given candidate distributions $$f_{1}, \ldots, f_{M},$$ a parameter $$\varepsilon>0$$ and $$\log \left(3 M^{2} / \delta\right) / 2 \varepsilon^{2}$$ i.i.d. samples from an unknown distribution $$g,$$ outputs an index $$j \in[M]$$ such that*

$$
\left\|f_{j}-g\right\|_{1} \leq 3 \min _{i \in[M]}\left\|f_{i}-g\right\|_{1}+4 \varepsilon
$$

*with probability at least $$1-\delta/3$$.*

Notice that although one decoder cannot know the real set of $$L$$ and $$B$$, it does know the finite length of $$L$$ and $$B$$ as a function of $$\epsilon$$. Then, with the above theorem, one can approximate the optimal decoder from a finite set of candidate decoders.

**Theorem.** (compressibility implies learnability). *Suppose $$\mathcal{F}$$ admits $$(\tau, t, m) r$$-robust compression. Let $$\tau^{\prime}(\varepsilon) :=\tau(\varepsilon)+t(\varepsilon)$$. Then $$\mathcal{F}$$ can be max $$\{3,2 / r\}$$-learned in the agnostic setting using*

**Lemma.** *If $$\mathcal{F}$$ admits $$(\tau(\varepsilon), t(\varepsilon), m(\varepsilon)) r$$ r-robust compression, then $$\mathcal{F}^{d}$$ admits $$(d \tau(\varepsilon / d), d t(\varepsilon / d), m(\varepsilon / d) \log (3 d)) r$$-robust compression.*

$$
O\left(m\left(\frac{\varepsilon}{6}\right) \log \left(\frac{1}{\delta}\right)+\frac{\tau^{\prime}(\varepsilon / 6) \log \left(m\left(\frac{\varepsilon}{6}\right) \log (1 / \delta)\right)+\log (1 / \delta)}{\varepsilon^{2}}\right)=\widetilde{O}\left(m\left(\frac{\varepsilon}{6}\right)+\frac{\tau^{\prime}(\varepsilon / 6)}{\varepsilon^{2}}\right) \; \text{samples}.
$$

If $$\mathcal{F}$$ admits $$(\tau, t, m)$$ non-robust compression, then $$\mathcal{F}$$ can be learned in the realizable setting using the same number of samples.

**Lemma.** *If $$\mathcal{F}$$ admits $$a(\tau(\varepsilon), t(\varepsilon), m(\varepsilon))($$ non-robust) compression, then $$k$$-mix$$(\mathcal{F})$$ admits $$\left(k \tau(\varepsilon / 3), k t(\varepsilon / 3)+k \log _{2}(3 k / \varepsilon)\right), 48 m(\varepsilon / 3) k \log (6 k) / \varepsilon )$$ (non-robust) compression.*

## Sample Complexity Bounds of Gaussians Mixtures

**Lemma.** *For any positive integrand, the class of d-dimensional Gaussians admits an $$\left(O(d \log (2 d)), O\left(d^{2} \log (2 d) \log (d / \varepsilon)\right), O\left(d \log (2 d)\right) \right)$$ $$2/ 3$$-robust compression scheme.*

Then with our theorems and lemmas above, we can finally have the following main results.

**Theorem.** *The class of k-mixtures of d-dimensional Gaussians can be learned in the realizable setting, and can be 9-learned in the agnostic setting, using $$\widetilde{O}\left(k d^{2} / \varepsilon^{2}\right)$$ samples.*
