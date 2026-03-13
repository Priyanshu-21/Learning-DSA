#include <iostream>
using namespace std;

void printNumber(int n) {
    // Base Condition: 
    if (n <= 0) return;

    printNumber(n - 1);
    cout << n << " "; 
}
int main() {
    int n; 
    cout << "Enter the number: "<< endl;
    cin >> n; 
    printNumber(n);
    return n; 
}
/* 
(Head Recursion)
Print the number n from 1 -> N without using iterative statements
*/