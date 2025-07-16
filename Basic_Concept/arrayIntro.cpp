#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
    int number[5] = {10, 23, 21, 24};
    int *p; 
    p = number; // Pointer p takes an address of first value of aaray number

    // Dynamic Allocated Memory Array & Pointer 
    int *dy_Array = (int *)malloc(5 * sizeof(int));
    dy_Array[0] = 10; dy_Array[1] = 12; dy_Array[2] = 14;

    cout<< number[3] << endl;
    cout<< number[4] << endl; // Garbage value of Initilized array --> 0

    cout<< *(p+ 1)<< endl;

    cout<< sizeof(dy_Array)<< endl;
    cout<< dy_Array[0] << " " << dy_Array[2]<< endl;
    return 0;
}

/*
1. Initializaiton of Array, Declaration (static Memory) --> Stack Memory
2. Initialization in Dynamic Memory (Heap Memory) --> Runtime Memory 
3. Pointer to Array. 
*/