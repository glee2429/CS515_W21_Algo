# RECURSION 
# 1. Program description: sort a given array by splitting into three chunks
# Input: unsorted array
# Output: sorted array

def stoogesort(L, i=0, j=None):
	if j is None:
		j = len(L) - 1
	if L[j] < L[i]:
		L[i], L[j] = L[j], L[i]
	if j - i > 1:
		t = (j - i + 1) // 3
		stoogesort(L, i  , j-t)
		stoogesort(L, i+t, j  )
		stoogesort(L, i  , j-t)
	return L

# Driver program to test the above function
data = [1, 4, 5, 3, -6, 3, 7, 10, -2, -5, 7, 5, 9, -3, 7]
print(stoogesort(data))


# 2. Time complexity:
