#include <iostream>

using namespace std;
int main() {
    int num, counter=0;
    cin >> num;
    string answers[num];
    string correct;

    for (int i = 0; i < num; i++) {
        cin >> answers[i];
    }
    for (int i = 0; i < num; i++) {
        cin >> correct;
        if (answers[i] == correct) {
            counter++;
        }
    }
    cout << counter;
}