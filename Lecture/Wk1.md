# CS 515 W21 Algorithms + Data Structures 
## Lecture 1 - Logistics & Course Overview (01/05/2021)

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


### In-class Exercise 1

#### Question: In how many different ways to fill a (1xn) array with 1x1 and 1x2 tiles?
Suggested approach: 
1. When n = 1: there is 1 way (1)
2. When n = 2: there are 2 ways (1+1, 2)
3. When n = 3: there are 3 ways (1+2, 2+1, 1+1+1)
4. When n = k: Tile(k) = Tile(k-1) + Tile(k-2)

``` codeblock
Count(n): 
    if n is small 
    ...
    else
        return Count(n-1) + Count(n-2)
 ```
Running time: Let's say T(n) is the runtime of Count(n). 
```
T(1) = O(1)
T(2) = O(1)
T(n) = T(n-1) + T(n-2) + O(1)
```
Upper bound: 
```
T(n) <= T(n-1) + T(n-2)
     <= 2T(n-1) 
     <= 2(2T(n-2)) --- you reduce each step by one and multiply by 2
     <= 2^n
T(n) >= 2T(n-2) + O(1)
     >= 2T(n-2) 
     >= 2^(n/2)
   
This algorithm grows exponentially and is very slow.
```
### In-class Exercise 2

#### Question: In how many different ways to cover a (2^n)x(2^n) grid with one missing square at the corner?
Break down into four pieces of (2^n-1)x(2^n-1). One of the piece containing a tile is identical to the one-step smaller problem (sub-problem) with a (2^n-1)x(2^n-1) grid. Then with the remaining three chuncks, you can fill them out and collect the three empty tiles to create a block. 

``` 
Algorithm:
# Base case:
  if n = 0 do nothing 
# Otherwise: 
  - Divide the grid into four (2^n-1)x(2^n-1) grids
  - Place a ㄴ to intersect those remaining smaller grids. 
  - Recursively tile the rest. 
 ```

## Lecture 2 - Recursion Continued (01/07/2021) 

### Tower of Hanoi w/ Three Poles
#### Rules
1. Move one disk at a time.
2. Never place a disk on a smaller disk.

#### Hint
- Ignore the largest disk.

Hanoi Tower Algorithm
```
Hanoi (n, src, dst, tmp)
 if n > 0:
    Hanoi(n-1, src, tmp, dst) --> Recursive call #1
    move n to dst
    Hanoi(n-1, tmp, dst, src) --> Recursive call #2
```

The number of moves to solve the puzzle

This is basically a preliminary attempt to solve running time.
```
T(n) = # of moves for n disks. -- Due to recursion in the algorithm, it will involve T(n-1).

T(0) = 0 
T(n) = T(n-1) + 1 T(n-1) 
     = 2T(n-1) + 1       --> Two recursive calls #1 & #2
```

##### Recursion Tree to Find Rnning Time Analysis
```
                            Total # of Work in Each Level
        n                       1
       /  \
     n-1  n-1                   2
    / \    / \
  n-2 n-2 n-2 n-2               4
  / \ / \ / \ / \
       
        ...                     Until the last level reaches 1.
  
Each branch has "1" as the amount of work required. 
If you add all of the total amount of work required in each level, the running time will be {1+2+2^2+...2^(n-1)} = 2^n-1
```
