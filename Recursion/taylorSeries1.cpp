#include <iostream>

using namespace std;
double taylorSeries(double x, double n) {
    static double sum = 1;
    // Base - Condition
    if (n == 0) return 1;

    sum = sum * (x / n) + 1;
    taylorSeries(x, n - 1);
    return sum; 
}
double taylorIterative(double x, double n) {
    double sum = 1;
    while (n > 0) {
        sum = sum * (x / n) + 1;
        n--; 
    }
    return sum;
}
int main() {
    double x, n;
    double result, resultIterative;
    cout << "Enter the value of x: " << endl;
    cin >> x;
    cout << "Enter the value of n: " << endl;
    cin >> n;
    result = taylorSeries(x, n);
    cout << "The result of Taylor Series is: " << result << endl;

    resultIterative = taylorIterative(x, n);
    cout << "The result of Iterative Taylor Series is: " << result << endl;
    return 0;
}
/*
Formulate Taylor with less multiplication formula 
*/