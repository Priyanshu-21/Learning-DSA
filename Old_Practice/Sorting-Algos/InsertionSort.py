# Implementation of Insertion Sorting Algorithm 
import ast, time, random

def insertionSort(array, n):
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while (j >= 0 and array[j] > key):
            array[j + 1] = array[j]
            array[j] = key
            j = j - 1
    return array

array = []
for i in range(1, 100000):
    array.append(random.randint(1, 100))

with open("./Sorting-Algos/input.txt", "w") as file:
    file.write(str(array))

with open("./Sorting-Algos/input.txt", "r") as file: 
    array = ast.literal_eval(file.readline())
    
n = len(array)
startTime = time.perf_counter()
result = insertionSort(array, n)
endTime = time.perf_counter()

# Save Sorted Array in output file
with open("./Sorting-Algos/InsertionSort_output.txt", "w") as file:
    file.write(str(result))

#print("Sorted array: \n", result)
print("Array Sorted in: ", endTime - startTime)