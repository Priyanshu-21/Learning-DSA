def printNumber(n):
    # Base Condition 
    if (n <= 0):
        return

    printNumber(n - 1)
    print(n, " ")

def print_reverse(n):
    # Base condition 
    if (n <= 0):
        return

    print(n, "\t")
    print_reverse(n - 1)


n = 10
printNumber(n)
print("\n")
print_reverse(n)
'''
1. Print the number from 1 -> N without using loop (Head Recursion)
2. Print the number from N -> 1 without using loop (Tail Recurison)
'''