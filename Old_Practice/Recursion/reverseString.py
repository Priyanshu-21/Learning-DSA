def reverse_string(s, i, n):
    # Base Condition
    if (n <= 0):
        return 
    reverse_string(s, i + 1, n - 1)
    print(s[i], " ")

n = "Priyanshu Mishra"
reverse_string(n, 0, 16)