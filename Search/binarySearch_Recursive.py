import math
class Binary:
    def __init__(self):
        self.n = len(array)

    def binarySearch(self, array: list[int], target: int) -> int:
        n = len(array)
        mid = math.floor(n / 2)
        if (array[mid] == target):
            return mid
        elif (array[mid] < target):
            # Search in right side of list 
            return self.binarySearch(array[mid + 1:n], target)
        else:
            return self.binarySearch(array[:mid], target)

if __name__ == "__main__":
    array = [1, 3, 5, 7, 8, 10]
    bb = Binary()
    result = bb.binarySearch(array, 5)
    print(result)