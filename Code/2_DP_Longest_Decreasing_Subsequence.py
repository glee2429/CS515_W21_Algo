# DYNAMIC PROGRAMMING
# 1. Program description: compute the length of the longest decreasing subsequence in arr of size n
# Input: array
# Output: length of the longest decreasing subsequence

# arr = [0, 5, 7]
# arr2 = [3, 2, 7, 1, 0]

def LDS(arr):
    n = len(arr)

    # Declare the list (array) for LDS and
    # initialize LDS values for all indexes
    LDS = [1]*n

    # Compute optimized LDS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] < arr[j] and LDS[i] < LDS[j] + 1 :
                LDS[i] = LDS[j] + 1

    # Initialize maximum to 0 to get
    # the maximum of all LDS
    maximum = 0

    # Pick maximum of all LDS values
    for i in range(n):
        maximum = max(maximum , LDS[i])

    return maximum

# 2. Time complexity: There are two inner loops, O(n^2).
