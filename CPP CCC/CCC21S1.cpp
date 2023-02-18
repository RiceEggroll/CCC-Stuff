//Crazy Fencing

#include <iostream>

using namespace std;
int main() {
    int n;
    double total;
    cin >> n;

    int height[n+1]; 
    int base[n];
 
    for (int i = 0; i < n+1; i++) {
        cin >> height[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> base[i];
    }


    for (int i = 0; i < n; i++) {
        total += base[i] * (height[i]+height[i+1]) / 2.0;
        if (i+1 > n) break;
    }
    cout << fixed << total;
}