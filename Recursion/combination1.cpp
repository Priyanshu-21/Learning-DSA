#include <iostream>
using namespace std;

int pascalCombination(int n, int r) {
    // Base Condtion: 
    if (n == 0 || n == r) return 1;

    return pascalCombination(n - 1, r - 1) + pascalCombination(n - 1, r); 
}
int main() {
    int n, r, result; 
    cout << "Enter the number of space available: "<< endl;
    cin >> n; 
    cout << "Enter the picked value from space (r <= n): "<< endl;
    cin >> r; 
    result = pascalCombination(n, r);
    cout << "The result of this combination is: "<< result << endl;
    return 0;
}
/*
Caculate Combination using Pascal's Triangle Method: Improved Time Complexity 
*/