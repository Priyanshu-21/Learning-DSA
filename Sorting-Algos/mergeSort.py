# Implementation of Merge Sort Algorithm (this impl is not working properly)
import math, random, ast, time

def merge(array, low, mid, high):
    # Left array, Right array to have store the elements
    left = array[:mid]
    right = array[mid:]

    i = j = k = 0
    while (i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    
    while (i < len(left)):
        array[k] = left[i]
        i = i + 1
        k = k + 1
    
    while (j < len(right)):
        array[k] = right[j]
        j = j + 1
        k = k + 1

def mergeSort(array, low, high):
    # Base Condition 
    if (low >= high):
        return
    
    # Recursive Condition 
    mid = math.floor((high + low) / 2)

    # Divide array into left and right half 
    mergeSort(array, low, mid)
    mergeSort(array, mid + 1, high)

    # Conquer: Arrange the array in ascending order 
    merge(array, low, mid, high)

array = [100, 73, 95, 71, 9, 3, 94, 16, 17, 33, 74, 8, 81, 64, 90, 58, 89, 42, 18, 99, 15, 66, 56, 71, 17, 1, 83, 83, 50, 46, 100, 35, 26, 68, 82, 39, 89, 78, 77, 54, 58, 57, 50, 4, 58, 26, 49, 43, 65, 30, 90, 96, 63, 20, 83, 57, 33, 6, 50, 9, 58, 97, 36, 16, 14, 85, 35, 69, 39, 15, 64, 9, 89, 18, 99, 69, 36, 70, 30, 80, 99, 69, 58, 50, 54, 1, 46, 2, 31, 20, 83, 11, 10, 77, 13, 83, 79, 78, 59, 23]

n = len(array)
mergeSort(array, 0, n)
print(array)

'''
array = []
for i in range(0, 100):
    array.append(random.randint(1, 100))

# Get the input text file (unsorted array)
with open("./Sorting-Algos/mergeSort_input.txt", "w") as file: 
    file.write(str(array))

# Sort this unsorted input text file 
with open("./Sorting-Algos/mergeSort_input.txt", "r") as file: 
    array = ast.literal_eval(file.readline())

startTime = time.perf_counter()
n = len(array)
mergeSort(array, 0, n)
endTime = time.perf_counter()
print("Time taken by algorithm to sort elements: ", endTime - startTime)
# Save result in output file 
with open("./Sorting-Algos/mergeSort_output.txt", "w") as file: 
    file.write(str(array))
'''
