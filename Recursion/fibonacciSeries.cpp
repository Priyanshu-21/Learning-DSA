#include <iostream>

using namespace std;

int fibonacciSeries(int n) {
    // Base Condition 
    if (n == 0 || n == 1) return n;

    return fibonacciSeries(n - 2) + fibonacciSeries(n - 1);
}
int main() {
    int n, result; 
    cout << "Enter the number of terms for the fibonacci sequence"<< endl;
    cin >> n;

    result = fibonacciSeries(n);

    cout << "Fibonacci result for value "<< n << " is "<< result << endl; 
    return 0;
}
/*
Understanding Fibonacci Series using Recurrence Relation (Navie Approach)
*/