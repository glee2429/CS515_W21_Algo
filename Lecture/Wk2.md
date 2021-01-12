# CS 515 Algorithms + Data Structructures
## Week 2 - Recursion / Divide & Conquer (1/12/2021)
### Question: Multiplication algorithm 
#### Condition: 
- Input: x[1,...,n], y[1,...,n]
- Output: z = x*y
- x[i], y[i] is a subset of {0, 1, 2, 3, ..., 9}
#### Complexity: O(n^2)  to solve multiplication 
#### Hint: turn the multiplication problem into array 
Let's say 
- x is an array of two chunks with each piece of size a, b where the largest m digits, m=n/2
- x = a * 10^m + b
- y is an array of two chunks with each piece of size c, d where the largest m digits, m=n/2
- y = c * 10^m + d
Then, 
- xy = (a*10^m+b)(c*10^m+d) = 10^2m*ac + 10^mad + 10^mbc + bd = 10^2m*ac + 10^m*ad+bc) + bd
- Let's say e = ac, g = ad, h = bc, f = bd
Finally, plug this into the algorithm
```
Mult(x[1,...,n],y[1,...,n]):
    if n = 1:
       return x[1] * y[1]
    else
      m = n/2
      a = x[1...m], b = x[m+1,...,n], c = y[1,..m], d = y[m+1,..n]
      e = Mult(a,c)
      f = Mult(b,d)
      g = Mult(a,d)
      h = Mult(b,c)
      
      return 10^2m*e + 10^m*(g+h) + f...
```
#### Assumption: n is a power of 2. 
```
The number of opeartion needed: T(n) = 4T(n/2) + O(n)
