# Python program to find
# length of longest
# decreasing subsequence
# in O(n Log n) time

# Binary search (note
# boundaries in the caller)
# A[] is FloorIndex
# in the caller
def FloorIndex(A, l, r, key):

    while (r - l > 1):
        m = l + (r - l)//2
        if (A[m] <= key):
            r = m
        else:
            l = m
    return r

def LDS(A, size):

    Subsequence = [0 for i in range(size + 1)]
    #len = 0

    Subsequence[0] = A[0]
    len = 1
    for i in range(1, size):

        if (A[i] > Subsequence[0]):

            # new biggest value
            Subsequence[0] = A[i]

        elif (A[i] < Subsequence[len-1]):

            # A[i] wants to extend
            # smallest subsequence
            Subsequence[len] = A[i]
            len+= 1

        else:
            # A[i] wants to be current
            # end candidate of an existing
            # subsequence. It will replace
            # floor value in Subsequence
            Subsequence[FloorIndex(Subsequence, -1, len-1, A[i])] = A[i]


    return len


# Driver program to
# test above function

A = [2, 5, 4, 3]
n = len(A)

print('Length of Longest Decreasing Subsequence is ', LDS(A, n))
