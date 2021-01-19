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
