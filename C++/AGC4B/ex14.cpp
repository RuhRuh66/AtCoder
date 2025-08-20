#include <bits/stdc++.h>
using namespace std;

int main(){
    int A, B, C;
    cin >> A >> B >> C;

    int MA = max(max(A, B), C);
    int MI = min(min(A, B), C);

    cout << MA-MI << endl;

}