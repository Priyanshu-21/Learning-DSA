#include <iostream>
#include <cstring>
using namespace std;

int calculateFibonacci(int n) {
    // Memoization: Base Condition 
    static int *isVisited = new int[n]; 
    memset(isVisited, -1, sizeof(isVisited));
    if (n == 0 || n == 1) {
        isVisited[n] = n;
        return n;
    } 
    if (isVisited[n] != -1) return isVisited[n];

    isVisited[n - 2] = calculateFibonacci(n - 2);
    isVisited[n - 1] = calculateFibonacci(n - 1);
    
    return isVisited[n - 2] + isVisited[n - 1];
    
}
int main() {
    int n, result; 
    cout << "Enter the number of term to calculate sum of Fibonacci Series: "<< endl;
    cin >> n; 
    result = calculateFibonacci(n);
    cout << "The sum of series is: "<< result << endl;
    return 0;
}
/*
Fibonacci Series using Memoization Method
Note: - Memoization method is not working propertly. 
*/