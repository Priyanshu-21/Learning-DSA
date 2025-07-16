#include <iostream>

using namespace std;

struct card {
    int color;
    int type; 
    int number;

};

int main() {
    struct card c1[52] = {{0, 0, 0}, {0, 0, 1}, {0, 0, 2}, {0, 0, 3}, {1, 3, 13}};


    cout << c1[4].color << c1[4].type << c1[4].number << endl;
    return 0;
}

/*
Characterstics of Card: 
    Color: - Red, Black
    Type: - Spade, Heart, Diamond, Clubes
    Number: - {A, 1, 2, 3, 4, 5 ... 10, J, K, Q} 
*/

/*
1. Introduction to Structure: Define, Declare, Initialize and accessing member 
2. Pointer to Structures 
*/