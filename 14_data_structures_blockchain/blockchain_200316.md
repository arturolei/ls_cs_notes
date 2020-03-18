# Blockchain
- Blockchain as secure ledger formed on trust (think about the credit system)
- How to we keep track of and guarantee the state of the world and keep track of the transactions? 
  - History is a big concern, we need to keep track of all transactions 
- Blockchain is a distributed ledger or de-centralized ledger

# What are we going to build
We are going to try and build a chain like so, with blocks:

```
chain = [
 {index, timestamp, transactions: [], proof}, 
 {index, timestamp, transactions: [], prevHash(2nd block), proof},
 {index, timestamp, transactions: [], prevHas(3rd block), proof}

]
```

## What does it mean to hash a block? 
- A hash function usually takes in a non-numerical value like a string and outputs an integer/something numerical, e.g. hexadecimal
- What can we hash? 
    - We can hash sentences with spaces, e.g. the quick brown fox jumps over the lazy dog--> bc139de
    - So how do we stringify our block, a data structure? 
- We can serialize the data/stringify our data (e.g. what happens with JSON)
- What if we hash (using sha256) a block like `hashlib.sha256({index, timestamp, transactions: [], prevHas(3rd block), proof})`

## Why do we need Proof of Work? 
- We have a prevHash which prevents you from messing with past transactions (you'll mess up the chain)
    - You can all still make changes or malicious alterations but you need to re-hash everything from when you maliciously altered things
    - Thus we cannot rely solely on Hash of previous block's data
- We need a rule "where the longest chain wins"---> We need to slow down via a verification process 
- We need to add a "proof" mechanism, it
- hash( {proof} {prevHash}) --> Hash with a pattern (This requires a lot of work to do)

