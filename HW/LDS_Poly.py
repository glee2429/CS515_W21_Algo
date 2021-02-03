    # Binary search to find the starting point

    def FloorIndex(A, l, r, key):
        while (r - l > 1):
            m = l + (r - l)//2
            if (A[m] <= key):
                r = m
            else:
                l = m
        return r

    # Build a temporary array to store the LDS and
    # compare it with each element in the original array
    def LDS(A, size):
        # Initialize the temp subsequence array
        Subsequence = [0 for i in range(size+1)]
        Subsequence[0] = A[0]
        len = 1
        for i in range(1, size):
            if (A[i] > Subsequence[0]):
                # Update the starting point as A[i] is the largest value.
                Subsequence[0] = A[i]

            elif (A[i] < Subsequence[len-1]):
                # Append A[i] to the subsequence
                # since it's smaller than the preceding value.
                Subsequence[len] = A[i]
                len+= 1

            else:
                # A[i] might be a new end candidate of the subsequence.
                # Find a subsequence where the end element is larger than A[i].
                # Then, replace the floor value in Subsequence.
                Subsequence[FloorIndex(tailTable, -1, len-1, A[i])] = A[i]

        return len
