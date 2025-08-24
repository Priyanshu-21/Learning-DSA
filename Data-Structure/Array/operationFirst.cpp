#include <iostream> 

using namespace std;
struct Array {
    int A[8];
    int size; 
    int length; 
};
void getIndex(struct Array *arr, int index) {
    if (index >= 0 && index < arr->length) {
        cout << "Array at index " << index << " is " << arr->A[index] << endl; 
        return; 
    }
}
void setIndex(struct Array *arr, int index, int key) {
    if (index >= 0 && index < arr->length) {
        arr->A[index] = key; 
        cout << "change array at index " << index << endl; 
        return; 
    }
}
int main() {
    struct Array arr = {15, 18, 12, 10, 15, 11, 2, 8};
    arr.size = sizeof(arr.A) / sizeof(arr.A[0]);
    arr.length = 8; 
    int index = 4, key = 25;  
    getIndex(&arr, index);
    setIndex(&arr, index, key); 
    getIndex(&arr, index); 
    return 0; 
}