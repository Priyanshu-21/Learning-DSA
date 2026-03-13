#include <iostream>
#include <math.h>

using namespace std;

struct Array {
    int A[16];
    int size; 
    int length;
};
int binarySearch(struct Array *arr, int key, int low, int high) {
    
    while (low <= high) {
        int mid = floor((low + high) / 2);
        
        if (key == arr->A[mid]) return mid;

        else if (key < arr->A[mid]) {
            // Left Side of Array 
            high = mid - 1;
        } else if (key > arr->A[mid]) {
            // Right Side of Array 
            low = mid + 1;
        }
    }
    return -1; 
}

int recursiveBS(struct Array *arr, int key, int low, int high) {
    // Base Condition
    if (low > high) {
        return -1;
    } 
    else {
        int mid = floor((low + high) / 2);
        
        if(key == arr->A[mid]) return mid;
        else if (key < arr->A[mid]) {
            return recursiveBS(arr, key, low, mid - 1);
        } else {
            return recursiveBS(arr, key, mid + 1, high);
        }
    } 
    return 0;
}
int main() {
    struct Array arr = {2, 5, 7, 9, 11, 13, 15, 17, 20, 23, 26, 30, 34, 38, 46, 54};
    arr.size = sizeof(arr.A) / sizeof(arr.A[0]);
    arr.length = 16; 
    int key = 26; 
    int low = 0, high = arr.length - 1; 
    int result = binarySearch(&arr, key, low, high);
    cout << "Element found at index: "<< result << endl;
    // Recursive function: 
    key = 15; 
    int resultRec = recursiveBS(&arr, key, low, high);
    cout << "Element found at index: "<< resultRec << endl; 
    return 0;
}