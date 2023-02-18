#include <iostream>

using namespace std;
int main() {
    int aa;
    int bb;
    int c;

    while(true) {
        cin >> c;

        if (c == 0) {
            break;
        }

        int perimeter = 0;
        int minimum = 999999;
        
        for (int i = 0; i < c; i++) {
            int a = c/i;
            int b = c/a;
            perimeter = 2*a + 2*b;

            if (perimeter < minimum) {
                minimum = perimeter;
                aa = a;
                bb = b;
            }
        }
        cout << perimeter;
        cout << aa;
        cout << bb;
    }
}