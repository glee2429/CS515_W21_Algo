## CS 515 Week 4: Dynamic Programming in Trees

### Problem Setting: Find the Maximum "Independent Set" of nodes in a tree
* Input: a tree
* Output: the size of the largest indepedent set, a set of vertices that contain NO adjacent pair of vertices.

```  
      x 
     /  \
    o    o
       / | \
      x  x  x
        / \
       o   o
      / \
     x   x
``` 
In this case, the size of the largest independent set is 6.

```
x--o--x--o--x--o--x
```
In this case, the size of the largest independent set is 4. 

```
     x
      \
       o
      / \
     o   x
    / \
   x   x
```
In this case, the size of the largest independent set is 4.


     
#### Useful Concepts/Notations in Tree Structure

```
T: a rooted tree

         o
      /  |  \
    { } { } { }
    
T[v]: a subtree of T rooted at v.

         r
         o
        /  \
       o    o v
          / | \
         {} {} {}
```
         
- Question to ask: am I going to take the last vertex or not? 
- Let's think about different cases.

#### Maximum Independent Set (MIS) in Tree Problem Definition

```
MIS[v]: the maximum independent set of T[r]
```

1. CASE I: The root is NOT in the maximum independent set. Therefore, we're not taking the root.

Since the root marked [X] is not considered, we can look at the children of the root eliminated.
```
         [X]
          o r
        /   \
     ------------
 C_1   o     o v   C_2
      /    / | \
     o    {} {} {}
         
MIS[r] = SUM of MIS of children of r.
```

2. CASE II: the root is in the MIS. 

Since the root marked [O] is considered, we can skip the children of the root and look at its *grandchildren*.
```
         [O]
          o r
        /   \
 [X]   o     o  [X] 
      /    / | \
G_1  o    {} {} {}
         G_2 G_3 G_4
         
MIS[r] = 1 + SUM of MIS of *grandchildren* of r.
```


#### Algorithm Design 

```
MIS(v):
if v is NULL:
      return 0
else 
      return max(
            SUM of MIS of children, 
            1+SUM of MIS of grandchildren
            )
```

However, is it the optimal solution? In fact, there are redundancies. To avoid this, we can use memoization. 

### Algorithm Optimization by Memoization 

#### How to: 
- Add one parameter, MIS, to each node of the tree, which is initially None. 
- Modify the algorithm design to fill out the memoization table.

```
MIS(v):
if v.mis is None:
      if v is NULL:
            return 0
      else 
            v.mis = max(
                  SUM of MIS of children, 
                  1+SUM of MIS of grandchildren
                  )
return v.mis
```
Example
```



```
#### Running time of Recursive Algorithm:

Generally, RT is the product of (# of different problems) and (Non-recursive work).
In the worst case, the total number of computation is counting the number of all children and grandchildren multiplied by recursive calls. Therefore, RT(n) = n O(n)=O(n^2).

#### Running time of Memoization Algorithm:

In this case, we will memoize each node and we can refer to them only once after the table is filled out. Therefore, the actual running time is O(n).


------------------------------------------------------------------
## Dynamic Program Takeaway 

Let's go back to the first DP problem. 

#### Example 1. Fibonacci

C(n) = C(n-1) + C(n-2)

To solve n, we need to solve (n-1) and (n-2). 
To solve (n-1), we need to solve (n-2) and (n-3). 

...

We can get to the base case. However, there is some *dependency* between chuncks.

### Dependency Graph 

To apply DP approach, the dependency graph should be *acyclical*.

#### Notations: 
- V: all subproblems 
- E: p -> q if to solve q, we need to solve p first. 

#### Example 2. Edit Distance 

To calculate the answer in the DP table, we need to calculate adjacent cells first. 

#### Example 3. MIS of Tree 

For each problem, the final answer depends on either children or grandchildren. 

Intuitively, dependency graph can be used to figure out an estimate of running time. 


### Directly Acyclic Graph 

G = (V,E) where G is directed, and G does not have a directed cycle. 

#### Caveat: 

- All dependencies that feeding to the next node should be *solved* already. 
- Therefore, the sequencing is important!!

#### Topologial Sort of Vertices of DAG 

- A left-to-right order of vertices so that each edge goes from left to right. 
- Once the nodes are sorted, then you can find the starting point where there's no dependency attached to it. 

##### Dynamic Programming and Tological Sort are interchangeable. 

#### Example: The Longest Path in a DAG 
- Input: a DAG, G=(V,E)
- Output: the length of the longest path in G.

##### Problem setting: 
```
Let v_1, v_2, ..., v_n be a topological sort of V. 

LP(i) = the longest path that end at the vertext i, v_i. 

Longest path of G = max(LP(i)) where i is between 1 and n. 
```
To find out the longest path to v_i, we need to look at the connected vertices right before vertext i. 
```
LP(i) = max(LP(j)+1) where j is connected to i and j < i.

The reason we do "+1" is that the vertext of interest is connected to the adjacent vertices we're calculating, so we need to add one to consider the edge connecting j and i.
```
Once we define the topological sort, we can go from left to right.

##### DAG Example

```
LP(i) = max(LP(j)+1) where j is connected to i and j < i.


o
LP(i) 
