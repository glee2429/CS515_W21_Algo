## Dynamic Programming (1/19/2021)

#### Motivating Example: 
In how many ways one can tile a 1xn grid with 1x1 and 1x2 blocks? 

Let's say F(n) is the number of tiles in 1xn grid. 

F(n): 
if n = 1, return 1
if n = 2, return 2
return F(n-1) + F(n-2)

##### Memoization: 
Since we backtrack the previously solved redundant problem, we can memoize values for future use. 

-----------------------------------
Ex) Show that the running time of F(n) is larger than 2^(n/2).

Mem F(n):
  if f(n) is None: 
    if n = 1: f(n) = 1
    if n = 2: f(n) = 2
    else
      f(n) = MemF(n-1) + MemF(n-2)
    return f(n)

f(n) will contain the number of ways to tile 1xn grid.

f(1) = 1
f(2) = 2
for i = 3 to n: 
  f(i) = f(i-1) + f(i-2) 
  
Total running time: O(n)

----------------------------------
Ex2) Modify the iterative algorithm above to work in O(1) space. 

- Weighted Indepedent Set: 
Input: A[1...n] of real numbers 
Output: pick a subset of A with no consecutive elements with max total 
e.g., {(11), 5, 7, (22), 0, (10), 8}
Total: 43

Approach: WIS(n): the solution for A[1...n]
* if WIS(n) contains A[n]
-> WIS(n) does NOT contain A[n-1]
-> WIS(n) = A[n] + WIS(n-2)

* if WIS(n) does NOT contain A[n]
-> WIS(n) = WIS(n-1)

WIS(n):
  if W(n) is NOT none: 
    if n = 1: w(1) = A[1]
    if n = 2: w(2) = max(A[1], A[2])
    w(n) = max( WIS(n-1), WIS(n-2)+A[n])
    return w(n)

----------------------------------------
Ex3) Longest Increasing Subsequence

* Input: A[1,...n] is composed of real numbers 
* Output: length of the longest increasing subsequence 

e.g., **0**, 20, 10, **1, 3, 5**, 2, **7, 78**

e.g., 7 **6 8** 5 **9** 4 **10** 3 **11** 2 1 **12**

LIS(A[1...n]): longest increasing subsequence of A[1...n]

Case 1: A[n] is NOT in LIS 

LIS(A[1...n]) = LIS(A[1...n-1])

Case 2: A[n] is in LIS: 

LIS(A[1...n]) = longest increasing subseq of A[1...n-1] with all element is equal to or smaller than A[n].

## Dynamic Programming Continued (1/21/2021) 

### Q1. Edit distance
- Intput: A[1...n], B[1...n]
- Output: edit ditsance of A and B with minimum number of operations (e.g., Delete, Insert, Substitute) to transfer A to B. 
- Example: 
```
Given A: MONEY, B: FOOD.
To transform A to B, 
MONEY -> (substitue Y with D)  -> MONED 
      -> (delete E)            -> MON_D 
      -> (substitue N with O)  -> MOO_D 
      -> (substitute M with F) -> FOO_D
```

##### Algorithm Design 
ED[m,n]: the edit distance of A[1...m], B[1...n].

1. delete A[m]: ED[m,n] = ED[m-1,n]+1
2. Insert a character in the end ED[m,n] = ED[m,n-1]+1
3. Substitute A[m] with B[n] ED[m,n] = ED[m-1,n-1]+1
4. Match A[m] and B[n] if A[m]==B[n], ED[m,n] = ED[m-1,n-1]

Basically, look at the rightmost element in the array. 

```
if m = 0: ED[m,n] = n
if n = 0: ED[m,n] = m
if m, n > 0: ED[m,n] = min {ED[m-1,n]+1, ED[m,n-1]+1, ED[m-1,n-1]+1, ED[m-1,n-1] if A[m] == B[n]}
```

##### Dynamic Programming Approach Applied 
-> Memoization 
```
              A
     0 1 ...            m
    ----------------------
  0 |0 1                m|
  1 |                    |
B   |                    |
    |                    |
  n |n                   |
    ----------------------
    
for j = 1 to m: ED[0,j] = j
for i = 1 to n: ED[i,0] = i
for i = 1 to n 
    for j = 1 to m
      ED[i,j] = min {
                     ED[m-1,n]+1, 
                     ED[m,n-1]+1, 
                     ED[m-1,n-1]+1, 
                     ED[m-1,n-1] if A[m] == B[n] -- if it's same, then take the diagonal value.
                     }
 ```
 Let's apply this to our example. A: MONEY & B: FOOD 
 ```
     0 F O O D
    -----------
  0 |0 1 2 3 4|
  M |1 1 2 3 4|
  O |2 2 1 2 3| -- O & O are the same. 
  N |3 3 2 2 3|
  E |4 4 3 3 3| -- E & F are different.
  Y |5 5 4 4 4|
    -----------
```
##### Running time: O(nm)
##### Space requirement: O(nm)
There are two for loops and the inside of them is constant.

#### Extra point: modify the algorithm to work with O(min(n,m)) space. 

### Q2. Subset Sum 
- Input: A[1..n] all positive numbers, T is a positive number
- Output: True if there is a subset of A whose sum is T, False otherwise.
- Example: A[1, 5, 7, 22, 53, 58], T = 61, The algorithm returns True. 

#### Algorithm Design 
SS(n,T): True if and only if for a, subset of A[1...n] with toal of T. 
1. Case 1: suppose that the subset above does not contain A[n]. SS(n,T) = SS(n-1,T)
2. Case 2: suppose that the subset above does contain A[n]. SS(n,T) = SS(n-1, T-A[n]); 

Basically, SS(n,T) = SS(n-1,T) or SS(n-1,T-A[n]).
