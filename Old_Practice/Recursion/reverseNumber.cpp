#include <iostream>
using namespace std;

void reversePrint(int n) {
    // Base Condition
    if (n <= 0) return;

    cout << n << " ";
    reversePrint(n - 1);
}
int main() {
    int n; 
    cout << "Enter the number: ";
    cin >> n;
    reversePrint(n);
    return 0;
}
/*
Print number from N -> 1 in reverse order without using iterative statements
*/