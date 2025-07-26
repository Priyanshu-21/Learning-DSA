#include <iostream>

using namespace std;

double taylorSeries(int x, int n) {
    // Base Condition 
    if (n == 0) return 1;
    else {
        static double pow = 1, fact = 1;
        static double sum = 1;
        taylorSeries(x, n - 1);
        // Returning Operations 
        pow = pow * x;
        fact = fact * n;
        sum = sum + (pow/fact);
        return sum;
    }
}
int main() {
    int x, n;
    double result;
    cout << "Please enter the x term: "<< endl;
    cin >> x;
    cout << "Enter the nthe term value: "<< endl;
    cin >> n;

    result = taylorSeries(x, n);
    cout << "Sum of the series is: "<< result; 
    return 0; 
}

/*
Introduction to Taylor Series using Naive approach (Recursive)
*/