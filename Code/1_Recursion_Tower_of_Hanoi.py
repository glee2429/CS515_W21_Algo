# RECURSION
# 1. Program description: Python Program to solve the Tower of Hanoi puzzle:
# such that we can stack up 'n' disks from the first rod to the third rod while maintaining the original shape/order between the original disks
# (the largest disk at the bottom, the smallest disk on the top)


def moveTower(n, Origin, Destination, Temp):
    if n >= 1:
        print( "    "*(3-n), "moveTower:", n, Origin, Destination )
        moveTower(n-1, Origin, Temp, Destination) # Move the smallest (n-1) disks from Origin to the temporary storage
        moveDisk(Origin, Destination, n) # Move the largest disk to the destination
        moveTower(n-1, Temp, Destination, Origin) # Move the smallest (n-1) disks from Temp to Destination
    #print(Temp)

def moveDisk(Origin, Destination, n):
    print("    "*(4-n), "moving disk", "~"*(n), "from ", Origin, "to ", Destination)


moveTower(3,"A","B","C")

# 2. Time complexity:
