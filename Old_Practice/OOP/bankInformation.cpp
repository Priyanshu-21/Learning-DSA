#include <iostream>
#include <stdio.h>
#include <cstdio>

using namespace std;
class BankAccount {
    int bankNumber;
    char holderName[20];   
public:
    float balance = 0.0;

public:
    BankAccount() {

    }
    BankAccount(int num, char name[], float balance) {
        bankNumber = num;
        balance = balance; 

        cout << "Congrats ! Your account is created"<< endl;
    }
    void deposite(float ammount) {
        balance = balance + ammount;
    }
    void withDrawal(float ammount) {
        balance = balance - ammount;
    }

    void getStatement() {
        cout << "Your account number "<< bankNumber << " has " << balance << endl;
    }
};

int main() {
    int number = 0;
    char name[20];
    float balance = 0.0;
    cout << "Enter the bank number: " << endl;
    cin >> number;
    cout << "Enter your name: " << endl;
    scanf("%c", name);
    BankAccount b(number, name, balance);
    b.deposite(10000.00);
    b.getStatement();
    b.withDrawal(1000.00);
    b.getStatement();
    char name1[11] = "Ajay Kumar";
    BankAccount c = {123, name1, 0.0};
    c.withDrawal(b.balance);
    b.getStatement();
    return 0;
}

