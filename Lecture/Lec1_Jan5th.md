### 01/05/2021
## Lecture 1 - Logistics & Course Overview

### Key Concepts

1. Recursion
- Divide & Conquer
- Dynamic Programming
2. Greedy Algorithms
3. Randomized Algorithms & Data Structures
- Basic Randomization
- Quick sort
- Hashing
4. Network Flows
5. Linear Programming Algorithms
6. Approximation Algorithms  

### Recursion

#### Motivation: can we reuse a small solution to solve a bigger problem?
#### Prompt: To solve problem x on input of size n
1. If n is 'small,' solve it directly.
2. Otherwise, reduce the problem to smaller size problems of the git same type.
3. Example: find the maximum element in an array of the size n.
```Python
max(A[1..n]) # Assume n >= 1
 if n = 1:
    return A[1]
 else
    maxOfTwo(
      max(A[1,...,n-1]),
      A[n]
      )
```
4. Runtime of 'max' for n numbers: T(n) -- we care about the worst possible scenario. 
``` codeblock
T(1) = O(1)
T(n) = T(n-1) + O(1) -- recursive description of running time
     = (T(n-2) + O(1)) + O(1)
     ...
     = O(1) + O(1) + ... + O(1) -- O(1) n times
```
5. Proof of Correctness by Induction *Step by Step*
- [BC] First, start with "the base cases" and show they are correct to show the smallest unit of your solution is valid.
- [IH] Then, define "Inductive Hypothesis" to show that the algorithm is correct for n is smaller than k (n<k). 
- [IS] Finally, assuming the step 1 & 2, apply the "Inductive Steps" to show the algorithm is correct for k. 


### In-class Exercise 

#### Question: In how many different ways I can cover a (1xn) array with 1x1 and 1x2?
Suggested approach: 
1. When n = 1: there is 1 way (1)
2. When n = 2: there are 2 ways (1+1, 2)
3. When n = 3: there are 3 ways (1+2, 2+1, 1+1+1)
...
4. When n = k: Tile(k) = Tile(k-1) + Tile(k-2)

``` codeblock
Count(n): 
    if n is small 
    ...
    else
        return Count(n-1) + Count(n-2)
 ```
