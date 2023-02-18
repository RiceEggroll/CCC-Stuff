#include <iostream>

using namespace std;
int main(){
    int counter;
    for (int i = 0; i < 6; i++){
        string outcome;
        cin >> outcome;
        if (outcome == "W"){
            counter++;
        }
    }
    if (counter == 5 || counter == 6){
        cout << 1;
    }
    if (counter == 3 || counter == 4){
        cout << 2;
    }
    if (counter == 1 || counter == 2){
        cout << 3;
    }
    if (counter < 1){
        cout << -1;
    }
} 