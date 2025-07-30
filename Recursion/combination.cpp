#include <iostream> 
using namespace std;
int calculateFact(int n) {
    if (n <= 0) return 1;

    return n * calculateFact(n - 1);
}
double calculateCombination(double n, double r) {
    double result;
    result = calculateFact(n) / (calculateFact(r) * calculateFact(n - r));
    return result;
}
int main() {
    double n, r, result; 
    cout << "Enter the number of the space objects"<< endl;
    cin >> n;
    cout << "Enter the picked combination number from space objects (r <= n)"<< endl;
    cin >> r;
    result = calculateCombination(n, r);
    cout << "Number of possible ways to pick from n objects: "<< result << endl;
    return 0; 
}
/*
Caculation of Combinaton using Factorial's Recursion Method 
*/