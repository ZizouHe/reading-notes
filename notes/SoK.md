# A Survey of Attacks on Ethereum Smart Contracts

- [Atzei, Nicola, Massimo Bartoletti, and Tiziana Cimoli. "A survey of attacks on ethereum smart contracts (sok)." In *International conference on principles of security and trust*, pp. 164-186. Springer, Berlin, Heidelberg, 2017.](https://link.springer.com/chapter/10.1007/978-3-662-54455-6_8)

- [以太坊合约的安全性弱点，你都绕开了吗？](https://zhuanlan.zhihu.com/p/55866676)

## Summary

Some of the primitives used in Solidity to invoke func- tions and to transfer ether may have the side effect of invoking the **fallback** function of the callee/recipient. We illustrate them below.

1. ```call``` invokes a function (of another contract, or of itself), and transfers ether to the callee. E.g., one can invoke the function ```ping``` of contract  ```c``` as follows:

   ```solidity
   c.call.value(amount)(bytes4(sha3("ping(uint256)")),n);
   ```

   where the called function is identified by the first 4 bytes of its hashed signature, ```amount``` determines how many wei have to be transferred to ```c```, and ```n``` is the actual parameter of ping. Remarkably, if a function with the given signature does not exist at address ```c```, then the **fallback** function of ```c``` is executed, instead.

2. ```send``` is used to transfer ether from the running contract to some recipient ```r```, as in ```r.send(amount)```. After the ether has been transferred, ```send``` executes the recipient’s **fallback**.

3. ```delegatecall``` is quite similar to ```call```, with the difference that the invocation of the called function is run in the caller environment. For instance, executing 

   ```solidity
   c.delegatecall(bytes4(sha3("ping(uint256)")),n)
   ```

   if ```ping``` contains the variable this, it refers to the caller’s address and not to ```c```, and in case of ether transfer to some recipient ```d``` — via ```d.send(amount)``` — the ether is taken from the caller balance.

4. besides the primitives above, one can also use a direct call as follows:

   ```solidity
   contract Alice { function ping(uint) returns (uint) }
   contract Bob   { function pong(Alice c){ c.ping(42); } }
   ```

   The first line declares the interface of ```Alice```’s contract, and the last two lines contain ```Bob```’s contract: therein, ```pong``` invokes ```Alice```’s ```ping``` via a direct call. Now, if the programmer mistypes the interface of contract ```Alice``` (e.g., by declaring the type of the parameter as ```int```, instead of ```uint```), and ```Alice``` has no function with that signature, then the call to ```ping``` actually results in a call to ```Alice```’s **fallback** function.



Here is a list of vulnerabilities

1. **Exception disorder**. In Solidity there are several situations where an excep- tion may be raised, e.g. if (i) the execution runs out of gas; (ii) the call stack reaches its limit; (iii) the command throw is executed. However, Solidity is not uniform in the way it handles exceptions: there are two different behaviours, which depend on how contracts call each others.
   - if every element of the chain is a direct call, then the execution stops, and every side effect (including transfers of ether) is reverted. Further, all the gas allocated by the originating transaction is consumed;
   - if at least one element of the chain is a ```call``` (the cases ```delegatecall``` and ```send``` are similar), then the exception is propagated along the chain, reverting all the side effects in the called contracts, until it reaches a ```call```. From that point the execution is resumed, with the ```call``` returning false10. Further, all the gas allocated by the call is ```call```.
2. **Gasless send**. When using the function ```send``` to transfer ether to a contract, it is possible to incur in an out-of-gas exception. This may be quite unex- pected by programmers, because transferring ether is not generally associated to executing code.
3. **Type casts**. The Solidity compiler can detects some type errors.
4. **Reentrancy**. The fallback mechanism may allow an attacker to re-enter the caller function. This may result in unexpected behaviours, and possibly also in loops of invoca- tions which eventually consume all the gas.
5. **Keeping secrets**. Declaring a field as private does not guarantee its secrecy. This is because, to set the value of a field, users must send a suitable transaction to miners, who will then publish it on the blockchain. Since the blockchain is public, everyone can inspect the contents of the transaction, and infer the new value of the field.
6. **Immutable bugs**. Once a contract is published on the blockchain, it can no longer be altered. 
7. **Stack size limit**. Each time a contract invokes another contract (or even itself via ```this.f()``) the call stack associated with the transaction grows by one frame. The call stack is bounded to 1024 frames: when this limit is reached, a further invocation throws an exception.