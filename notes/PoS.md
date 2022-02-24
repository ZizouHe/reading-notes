# Blockchain Without Waste: Proof-of-Stake

- [Saleh, Fahad. "Blockchain without waste: Proof-of-stake." *The Review of financial studies* 34, no. 3 (2021): 1156-1190.](https://academic.oup.com/rfs/article-abstract/34/3/1156/5868423)



## Summary

1. Nothing-at-stake is one of the downsides of Proof-of-Stake. The problem is that the lack of an explicit cost (compared to Proof-of-Work in Bitcoin) coupled with the explicit benefit of the block reward implies that a validator will always update the ledger whenever given the opportunity even if the update necessarily perpetuates disagreement.

2. This paper examines the nothing-at-stake problem using a formal economic analysis. The key results can be summarized as follows:

   - Adding a block to the shorter branch on the blockchain has two effects for the player appending the block. 
     - The first effect is that the player receives a block reward in terms of coins on that branch; this first effect creates an incentive for the player to append the block. 
     - The second effect is that the value of all coins falls; this second effect competes with the first effect and discourages the player from adding a block to the shorter branch. 

   - A myopic player with no coins always appends to the blockchain when given the option if the block reward takes a strictly positive value. Alternatively, a player with a large stake opts not to append to the blockchain when doing so defers consensus due to the prohibitive cost incurred via her stake being devalued. **An equilibrium in which all players follow the Longest Chain Rule exists if each player holds a sufficient stake. In this case, the long chain rule strategy also constitutes a subgame perfect equilibrium.** (second effect dominates)
   - **If there is no block rewards, then there exists an equilibrium in which each player follows the longest chain rule.** In other words, a Proof-of-Stake blockchain obtains consensus without further conditions if the blockchain possesses no block reward. (first effect is eliminated)
   - The Proof-of-Stake does not lead to wealth concentration. In expectation, one's wealth share remains the same.