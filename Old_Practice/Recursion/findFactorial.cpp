#include <iostream> 
using namespace std;
int findFactorial(int n) {
    // Base Condition 
    if (n <= 1) return 1;

    return n * findFactorial(n - 1);
}
int main() {
    int n; 
    cout << "Enter a number: "<< endl;
    cin >> n;
    int result = findFactorial(n);
    cout << "Factorial of number: "<< n << " is " << result; 
    return 0;
}

/*
Find the factorial of a number using Head Recursion 
*/