# Introduction to Binary Search Algorithm
import math

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while(low <= high):
        mid = math.floor((low + high) / 2) # Convert float value to integer value 
        guess = list[mid]
        if (guess == item):
            return mid
        elif (guess < item):
            low = mid + 1
        elif (guess > item):
            high = mid - 1
        else:
            return None


list = [12, 14, 16, 17, 18, 20, 22, 30]

result = binary_search(list, 21)
print(result)