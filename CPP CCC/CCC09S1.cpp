#include <iostream>
#include <math.h>

using namespace std;
int main() {
    int low, high, i = 0, counter = 0;
    cin >> low >> high;

    while (pow(i,6) <= high) {
        if (pow(i,6) >= low) counter++;
        i++;
    }
    cout << counter;
}