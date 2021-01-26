## CS 515 Algorithms  
### Week 4: Dynamic Programming in Trees

#### Problem Setting: Find the Maximum "Independent Set" of nodes in a tree
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

#### Algorithm Optimization by Memoization 

##### How to: 
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
##### Running time: 

Generally, RT is the product of (# of different problems) and (Non-recursive work).
In the worst case, the total number of computation is counting the number of all children and grandchildren multiplied by recursive calls. Therefore, RT(n) = n O(n)=O(n^2).


