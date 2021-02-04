## Randomized Algorithms

#### Problem setting: BoH and Nuts
- Input: B is a bolt, N_1,...,N_n are n nuts 
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

