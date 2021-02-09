# DYNAMIC PROGRAMMING
# 1. Program description: compute the 'n'th Fibonacci number
# Input: n
# Output: 'n'th iteration, f_small, f_big(Fibonacci Number), TempArray

def fibonacci(n):
    f_small = 0 # Initialized - Base case 1
    f_big = 1   # Initialized - Base case 2

    # Case I. When n is negative, return error message
    if n < 0:
        print("Incorrect input")

    # Case II. When n is 0, return 0
    elif n == 0:
        return f_small

    # Case III. When n is 1, return 1
    elif n == 1:
        return f_big
    else:
        for i in range(1, n):
            f_temp = f_small + f_big # Temp storage to add f_small and f_big
            f_small = f_big          # Increase the fib_small by replacing it with fib_big
            f_big = f_temp           # Get the sum of fib_small and fib_big, stored in f_temp
            print(i,'th iteration: ' ,f_small, f_big, f_temp)
        return f_big

# Driver Program
print(fibonacci(9))
