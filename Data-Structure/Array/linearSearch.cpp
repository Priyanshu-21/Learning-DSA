#include <iostream>

using namespace std;

struct Array {
    int A[16];
    int size; 
    int length; 
};

int linearSearch(struct Array *arr, int key) {
    for (int i = 0; i < arr->length; i++) {
        if (key == arr->A[i]) return i; 
    }
    return -1; 
}

int main() {
    struct Array arr = {29, 21, 15, 16, 18, 1, 2, 22, 24, 28, 26, 27, 11, 14, 8, 13};
    arr.size = sizeof(arr.A) / sizeof(arr.A[0]);
    arr.length = 16; 
    int key = 7;
    int result = linearSearch(&arr, key);
    cout << "Array found at index " << result << endl;
    return 0; 
}