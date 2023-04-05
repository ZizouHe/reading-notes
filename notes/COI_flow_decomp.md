# Order Imbalance with Trade Flow Decomposition

- [Lu, Reinert, and Cucuringu, 2022. Trade Co-occurrence, Trade Flow Decomposition, and Conditional Order Imbalance in Equity Markets]()

## Introduction

- For any stock, the conditional order imbalance is defined as
  $$
  COI = \frac{N_{buy} - N_{sell}}{N_{buy} + N_{sell}}
  $$

- where $$N_{buy}$$ and $$N_{sell}$$ denote the total number of market buy orders and market respectively.

- We now decomposite trade into different types,

  - ***isolated***: Trades are labelled as isolated if they do not co-occur with any other trades.
  - ***non-isolated***: Otherwise, trades are labelled as non-isolated.
    - ***non-self-isolated***: the co-occurrence neighborhood contains only trades of the same stock;
    - ***non-cross-isolated***: the co-occurrence neighborhood contains only trades of different stocks;
    - ***non-both-isolated***: the co-occurrence neighborhood contains only trades of same and other stocks

- For each identified trade type, we can compute the order imbalance. The regression R square is higher if we use 3 types of non-isolated COI and the isolated COI. 