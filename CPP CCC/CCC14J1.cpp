#include <iostream>

using namespace std;

int main() {
    int a, b, c;

    cin >> a >> b >> c;

    if (a+b+c > 180) {
        cout << "Error";
    }
    else if (a == b == c){
        cout << "Equilateral";
    }
    else if (a != b != c) {
        cout << "Scalene";
    }
    else {
        cout << "Isoceles";
    }
}