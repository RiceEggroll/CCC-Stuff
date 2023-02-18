#include <iostream>
#include <vector>

using namespace std;
int main() {
    int row, col, choices, counter=0, r=0,c=0;
    string a, b;
    cin >> row >> col >> choices;
    vector<string> paint;

    for (int i = 0; i < choices; i++) {
        cin >> a >> b;
        bool dup = false;
        string temp = a+b;

        for (int j = 0; j < paint.size(); j++) {
            if (paint.at(j) == temp) {
                dup = true;
                paint.erase(paint.begin()+j);
            }
        }
        if (!dup) {
            paint.push_back(temp);
        }
    }

    for (int i = 0; i < paint.size(); i++) {
        if ((paint.at(i))[0] == 'R') {
            counter = counter + col - (c*2);
            r++;
        }
        if ((paint.at(i))[0] == 'C') {
            counter = counter + row - (r*2);
            c++;

        }
    }
    cout << counter;
}