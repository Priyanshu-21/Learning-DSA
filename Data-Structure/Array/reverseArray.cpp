#include <iostream> 
using namespace std; 

struct Array {
    int A[8]; 
    int size; 
    int length; 
}; 

// 1. Using Auxillary extra space
void reverseArray(struct Array *arr, int length) {
    int B[length]; 
    // Copy elements in decreasing index values to array B
    for (int i = length - 1, j = 0; i >= 0; i--, j++) {
        B[j] = arr->A[i]; 
    }
    // Copy the elements of B (which are reverse of A) to A 
    for (int i = 0; i < length; i++) {
        arr->A[i] = B[i]; 
    }
}
void swapElement(int &a, int &b) {
    int temp = b; 
    b = a; 
    a = temp; 
}

// 2. Two pointer swap approach 
void reverseAgain(struct Array *arr, int length) {
    int i = 0, j = length - 1; 
    while (i <= j) {
        swapElement(arr->A[i], arr->A[j]);
        i++; 
        j--;  
    }
}
void printElement(struct Array *arr) {
    for (int i = 0; i < arr->length; i++) {
        cout << arr->A[i] << " "; 
    }
    printf("\n"); 
}
int main () {
    struct Array arr = {15, 18, 12, 10, 1, 16, 11, 2, 8}; 
    arr.size = sizeof(arr.A) / sizeof(arr.A[0]); 
    arr.length = 9; 
    reverseArray(&arr, arr.length); 
    printElement(&arr); 
    reverseAgain(&arr, arr.length); // Reversing with two pointer approach 
    printElement(&arr);
    return 0; 
}
/*
Reverse Array: - 
1. Using Auxillary extra space --> TC : - f(n) = 2n + 1 ==> Order: O(n)
2. Two pointer swap approach  ---> TC : - f(n) = 2n ==> Order: O(n)
*/