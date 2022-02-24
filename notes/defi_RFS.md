# Decentralized Mining in Centralized Pools

- [Cong, Lin William, Zhiguo He, and Jiasun Li. "Decentralized mining in centralized pools." *The Review of Financial Studies* 34, no. 3 (2021): 1191-1235.](https://academic.oup.com/rfs/article-abstract/34/3/1191/5815571)



## Summary

1. Two features of cryptocurrency mining that are key:
   - It is easy for profit-driven miners to participate in multiple mining pools
   - the dynamic adjustment of mining difficulty required for ensuring a stable block production rate leads to an arms race, creating a negative externality in which each individual’s acquisition of hash rates directly hurts others’ payoffs
2. The certainty equivalent of joining a mining pool more than doubles that of solo mining
3. The total revenue in crypto-mining stays the same whether two miners join force or not
4. **Without friction (without passive hash rate)**, every active miner owns an equal share of each mining pool, **irrelevant to the exact pool size**. Pool managers charge zero fees due to Bertrand competition, otherwise one pool manager can cut her fee to steal the entire market.
   - As a result, the folk wisdom in the blockchain community that pools become concentrated for better risk sharing is misguided, as long as miners can freely allocate their hash rates.
5. **With friction**, a larger incumbent pool optimally charges a higher fee, which slows its percentage growth relative to smaller pools. **Therefore, pool sizes mean-revert endogenously.**
   - A larger pool has a larger impact on global hash rates and consequently charges a higher fee and accommodates proportionally less active hash rates, reminiscent of traditional oligopolistic models where larger producers charge higher prices and produce less. Consequently, in the long run we expect a relatively decentralized market structure in the global mining industry may sustain and no single pool would grow too dominant.
6. The global hash rates is much higher for multiple mining pools, compared to solo mining mode. As expected, the homogeneous two-pool equilibrium generates lower global hash rates compared to the full risk-sharing equilibrium. Intuitively, pool managers with some market power take into account the arms race effect and hence discourage active miners’ hash rate acquisition by raising their fees. Even when we give the best chance of this market-power force to produce a countervailing effect by considering the lowest possible of number of pools (here, M = 2), quantitatively there is no big difference from the full risk-sharing case. The takeaway is that no matter whether we consider the friction of passive mining, **the emergence of mining pools as a form of financial innovation escalates the mining arms race and contributes to its explosive growth in energy consumption in recent years.**



### Model

Technology rules that for all practical purposes the probability of finding a solution is not affected by the number of trials attempted. This well-known **memoryless property** implies that the event of finding a solution is captured by a **Poisson process** with the arrival rate proportional to a miner’s share of hash rates globally. Given a unit hash cost $c$ and a dollar award $$R$$ for each block, the payoff to a miner who has a hash rate of $$\lambda_A$$ operating over a period $$T$$ is
$$
X_{solo} - c \lambda_A T, \text{ where } X_{solo} = B_{solo} R, \; \; B_{solo} \sim \mathrm{Poisson} \left(\frac{1}{D} \frac{\lambda_A}{\Lambda} T\right).
$$
Here, $$B_{solo}$$ is the number of blocks the miner finds within $$T$$—a Poisson distributed random variable capturing the risk that a miner faces in this mining game; $$\Lambda$$ denotes global hash rate (i.e., the sum of hash rates employed by all miners, whether individual or pool); $$D = 60×10$$ is a constant so that on average one block is created every $$10$$ minutes.



The payoff to a participating miner with hash rate $$\lambda_A$$ who joins a pool with existing hash rate $$\Lambda_B$$ is
$$
X_{pool} - c \lambda_A T, \text{ where } X_{pool} = \frac{\lambda_A}{\lambda_A + \Lambda_B} B_{pool} R, \; \; B_{pool} \sim \mathrm{Poisson} \left(\frac{1}{D} \frac{\lambda_A + \Lambda_B}{\Lambda} T\right).
$$
$$X_{pool}$$ second-order stochastically dominates $$X_{solo}$$, so any risk-averse miner strictly prefers $$X_{pool}$$ over $$X_{solo}$$.

Throughout the paper we use preference with constant absolute risk aversion (CARA), i.e., exponential utility with risk-aversion parameter $$\rho$$:
$$
u(x) := \frac{1}{\rho} (1 - e^{-\rho x}).
$$
