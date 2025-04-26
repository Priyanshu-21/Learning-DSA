# Implementation of Insertion Sorting Algorithm 
def insertionSort(array, n):
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while (j > 0 and array[j] > key):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


array = [2, 4, 7, 15, 5, 8, 3, 1]
n = len(array)
result = insertionSort(array, n)
print("Sorted array: \n", result)

# Wrong implementation of Insertion Sort algorithm (Need to check on this)