#include <bits/stdc++.h>
using namespace std;

int sum(vector<int> scores){
    int ans = 0;
    for (int i = 0; i < scores.size(); i++){
        ans += scores.at(i);
    }
    return ans;
}

void output(int sum_a, int sum_b, int sum_c){
    cout << sum_a * sum_b * sum_c << endl;
}

vector<int> input(int N){
    vector<int> vec(N);
    for (int i=0; i < N; i++){
        cin >> vec.at(i);
    }
    return vec;
}

int main(){
    int N;
    cin >> N;

    vector<int> A(N), B(N), C(N);

    A = input(N);
    B = input(N);
    C = input(N);

    int sum_A = sum(A);
    int sum_B = sum(B);
    int sum_C = sum(C);

    output(sum_A, sum_B, sum_C);
    

}