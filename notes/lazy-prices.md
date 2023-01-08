# Lazy Prices

- [Cohen, Lauren, Christopher Malloy, and Quoc Nguyen. "Lazy prices." *The Journal of Finance* 75, no. 3 (2020): 1371-1415.](https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.12885)

## Summary

1. Changes to the language and construction of financial reports have strong implications for firms’ future returns and operations. The lack of announcement returns is not due to financial statements becoming less useful over time, but rather to investors missing these subtle but important signals from annual reports at the time of theirs release, perhaps due to the reports’ increased complexity and length

2. Split stocks into 5 quantiles (portfolios) using financial report similarity with prior ones, also construct portfolio which long the nonchanges and short the changes. 
3. Potential mechanism behind the results: negative semtiment, higher uncertainty, more litigiousness, CEO/CFO changes (all can be found using text analysis of the reports).
4. Most crucial section changes within the report: Risk Factors, Management’s Discussion and Analysis.
5. When investor attention to year-over-year corporate filings is greater, the return predictability results of the changes to the language and construction of financial reports are somewhat weaker.



## Details

1. Use 10-K and 10-Q reports documents, use four classical NLP methods to measure document similarity, i.e., cosine similarity, Jaccard similarity, minimum edit distance and simple similarity, use the classification of sentiment ([Loughran and McDonald’s (2011) Master Dictionary](https://link.zhihu.com/?target=https%3A//sraf.nd.edu/textual-analysis/resources/)).

2. Fama-Macbeth regression

   - [wiki](https://en.wikipedia.org/wiki/Fama%E2%80%93MacBeth_regression)
   - [股票多因子模型回归](https://zhuanlan.zhihu.com/p/40984029)

   