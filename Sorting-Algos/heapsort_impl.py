import time, random, ast

# Implementation of Heap Sort Algorithm
def max_heap(Arr: list[int], i: int, n: int) -> None:

    maximum = i
    left = 2 * i 
    right = 2 * i + 1

    # comparing which node is larger from parent, left & right child 
    if (left <= n and Arr[left - 1] > Arr[maximum - 1]):
        maximum = left
    
    if (right <= n and Arr[right - 1] > Arr[maximum - 1]):
        maximum = right

    if (i != maximum):
        # Swap elements and maitain max-heap property 
        (Arr[i - 1], Arr[maximum - 1]) = (Arr[maximum - 1], Arr[i - 1])
        max_heap(Arr, maximum, n)


def build_maxheap(Arr: list[int]) -> None: 
    
    n = len(Arr)
    for i in range (n // 2, 0, -1):
        max_heap(Arr, i, n)


# Logic to implement HeapSort Algorithm 
def heap_sort(Arr: list[int], n: int) -> None:

    build_maxheap(Arr)
    for i in range (n - 1, 0, -1):
        # Swap root element with last element
        (Arr[i], Arr[0]) = (Arr[0], Arr[i])
        max_heap(Arr, 1, i)

Arr = []
for i in range(1, 100000):
    Arr.append(random.randint(1, 500))

with open("./input.txt", "w") as file:
    file.write(str(Arr))

with open("./input.txt", "r") as file: 
    Arr = ast.literal_eval(file.readline())

# Let's take how much time does it take to compute sorting of algorithm 
start_time = time.perf_counter()
heap_sort(Arr, len(Arr))
end_time = time.perf_counter()

# time taken to compute approach 
print("Time taken to complete sorting: ", end_time - start_time)

# Save result in result.txt
with open("./heapsort_result.txt", "w") as file:
    file.write(str(Arr))

