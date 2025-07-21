#include <iostream>
using namespace std;

int findSum(int number[], int n) {
    // Base Condition: 
    if (n < 0) {
        return  0; 
    }
    return number[n] + findSum(number, n - 1);
}
int main() {
    int number[10] = {21, 37, 45, 92, 87, 24, 33, 44, 10, 11}; 
    int result = findSum(number, 9);
    cout << "Sum of Array Element is: "<< result << endl;
    return 0;
}
/* 
Solve sum of N element in array using recursion 
*/