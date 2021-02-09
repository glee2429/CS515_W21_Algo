# RECURSION
# 1. Program description: compute the length of the longest common subsequence of two arrays
# Input: Two arrays (+ their lengths)
# Output: Length of the longest common subsequence

def lcs(X, Y, m, n):

    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]: # Compare the last element of each array
       return 1 + lcs(X, Y, m-1, n-1); # Increment lsc by 1 and compare the previous elements
    else: # If the last elements are not identical, shave the last element off from X or Y and recurse
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X , Y, len(X), len(Y))

# 2. Time complexity 
