#include <iostream>

using namespace std;
struct Array {
    int A[10];
    int size; 
    int length; 
}; 

int iterativeSearch(struct Array *arr, int low, int high, int value) {
    while (low < high) {
        int mid = (low + high) / 2;
        
        if (arr->A[mid] < value) {
            low = mid + 1; 
        } else if (arr->A[mid] > value) {
            high = mid - 1; 
        } else {
            return mid; 
        }
    }
    return -1; 
}

int main () {
    struct Array arr = {5, 6, 7, 10, 12, 14, 16, 18, 20, 45};
    arr.size = sizeof(arr.A) / sizeof(arr.A[0]);
    arr.length = 10; 
    // Binary Search (Iterative Approach)
    int index = iterativeSearch(&arr, 0, arr.length - 1, 20);
    cout << "Element found at index "<< index << " in the array list"<< endl;  
    return 0; 
}
/*
Array ADT: - Operation performed for searching algorithm 
*/