#include <iostream> 
#include <cmath>

using namespace std;

int main() {
	double tiles;
	cin >> tiles;
	int answer = floor(sqrt(tiles));
	cout << endl << "The largest square has side length " << answer << "." << endl;
}