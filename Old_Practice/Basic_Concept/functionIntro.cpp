#include <iostream>

using namespace std; 
void swapbyValue(int x, int y) {
    int temp;
    temp = x;
    x = y;
    y = temp;
}
void swapbyAddress(int *x, int *y) {
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
void swapbyReference(int &x, int &y) {
    int temp;
    temp = x;
    x = y;
    y = temp;
}
int main() {
    int a = 10; int b = 20;

    swapbyValue(a, b);
    cout << "Value swapped (Pass by value):"<< a << " " << b << endl; 
    
    swapbyAddress(&a, &b); 
    cout << "Value swapped (Pass by Address):"<< a << " " << b << endl;
    
    swapbyReference(a, b);
    cout << "Value swapped (Pass by Reference):"<< a << " " << b << endl; 
    
    return 0;
}

/*
1. Defination of function (Protocol), Calling 
2. Argument passing in function {Call by Value, call by reference & call by address }
*/