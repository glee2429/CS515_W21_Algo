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
# Randomly permutate N_1,..., N_n s.t. your permutation comes from uniform distribution over all permutation
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
```
X: N_1,...,N_n, B
After permutations, the matching nut is at location i with probability 1/n for any 1<=i<=n. 
T(X) = {k with probability 1/n for k < n} or {n-1 with probability 1/n}

Pr[T(X)=k] = {1/n when k < n-1} or {2/n when k <= n - 1}
# Why is it 2/n? 
# When k=n-1, the remaining nut is going to be the match at k=n and when k=n it is the matching nut.

E[T(X)] = Summation of (k * Pr[T(X) = k]) where k = 1 to n-2
        = (1/n) * Summation of (k*1/n) + 2(n-1)/n where k = 1 to n-2
        = (1/n) * (n-1)(n-2)/2 + 2(n-1)/n
        = (n+1)/2 - (1/n)
```
T_WorstExpCase(n) = max{E(T(x))} where x of size n. 

T(x) is the same for all x of size n. 

T_WEC(n) = max{E(T[x])} = (n+1)/2 - (1/n)


### Randomized vs. Deterministic 
The running time differs between randomized vs. deterministic approach. 
#### Goal of the lecture: 
- Understand why calculating expectation is useful. 
