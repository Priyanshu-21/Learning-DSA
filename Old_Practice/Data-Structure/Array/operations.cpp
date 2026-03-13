#include <iostream>

using namespace std;
struct Array {
    int A[11];
    int size;
    int length;
};
void display(struct Array *arr) {
    if (arr->length < arr->size) {
        for (int i = 0; i < arr->length; i++) {
            cout << arr->A[i] << " "; 
        }
    }
}
void append(struct Array *arr, int value) {
    if (arr->length < arr->size) {
        arr->A[arr->length] = value;
        arr->length++; 
    }
    else {
        cout << "Insufficient Array Space" << endl;
    }
}
void insert(struct Array *arr, int index, int value) {
    if (arr->length < arr->size) {
        for (int i = arr->length; i >= index; i--) {
            arr->A[i + 1] = arr->A[i];
        }
        arr->A[index] = value; 
        arr->length++; 
    }
}
void Delete(struct Array *arr, int index) {
    if (index > 0 && index < arr->size) {
        for (int i = index; i < arr->length - 1; i++) {
            arr->A[i] = arr->A[i + 1];
        }
        arr->length--; 
    }
}
int main() {
    struct Array arr = {5, 8, 6, 9, 10, 21, 45};
    arr.size = sizeof(arr.A) / sizeof(arr.A[0]);
    arr.length = 7; 
    display(&arr);
    cout << endl; 
    append(&arr, 23);
    display(&arr);
    cout << endl;
    insert(&arr, 3, 8);
    display(&arr);
    cout << endl;
    Delete(&arr, 2);
    display(&arr);  
    return 0; 
}
/*
Introduction to array ADT and Operations on array data structure
Operations: - Display, Append, Insert, Delete
*/