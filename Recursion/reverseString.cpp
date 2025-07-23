#include <iostream> 
using namespace std;

void reverseString(string s, int i, int n) {
    // Base Condition 
    if (n < 0) return; 

    reverseString(s, i + 1, n - 1);
    cout << s[i] << " ";
}
int main() {
    string s = "Priyanshu Mishra";
    
    reverseString(s, 0, s.size());
    return 0;
}
/*
Understand how to reverse a string recursively 
*/