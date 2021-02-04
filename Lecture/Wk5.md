## Randomized Algorithms

#### Problem setting: BoH and Nuts
- Input: B is a bolt, N_1,...,N_n are n nuts (unsorted).
- Operations: test B & N_i -- there are three cases {B > N_i} or {B < N_i} or {B = N_i}
- Assumption: there is exactly one nut that matches B. 
- Output: the nut that matches B. 

#### Algorithm 
```
for i = 1 to n-1:
  if B = N_i:
      return N_i
return N_n
```

#### Running time 
Let X be any input, T(X) be a running time of Alg assuming for X.
However, we don't have any information about the distribution of input. Therefore, just get the worst case scenario. 
- Worst case: T_wc(n) = max [T(x)] for size n
- T_wc(n) = n-1 (in the worst case scenario, we need to compare the bolt with (n-1) nuts.)


#### Randomized Algorithm 
```
# Randomly permutate N_1,..., N_n such taht your permutation comes from uniform distribution over all permutation
for i = 1 to n-1:
  if B = N_i:
    return N_i
return N_n
```

#### Running time 
Let X be any input, T(X) be a running time of the algorithm, which will depends on the distribution of X. 
- T(x): a random variable -- since even if you fix the input, you'll be shuffling the input. 
- A possible approach to figure out RT is to use *expected* values or *maximum* value. 
- E(T(X)) or max(T(X)) -- this expectation is happening *inside* the randomize choice of algorithm. 
- T_worstExpCase(n) = max{E(T(x))} where x of size n -- the worst is going over every input. 

### Randomized vs. Deterministic 
The running time differs between randomized vs. deterministic approach. 
#### Goal of the lecture: 
- Understand why calculating expectation is useful. 
