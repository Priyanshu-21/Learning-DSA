# Implementation of Merge Sort Algorithm (this impl is not working properly)
import math, random, ast, time

def merge(array, low, mid, high):
    # Left array, Right array to have store the elements
    left = array[:mid]
    right = array[mid + 1:]
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