#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int main() {
    freopen("cowsignal.in","r", stdin);
    freopen("cowsignal.out", "w", stdout);

    int m, n, k;
    scanf("%d %d %d", &m, &n, &k);

    for (int i = 0; i<m; i+=1) {
        string line;
        cin >> line;
        for (int i = 0; i < k; i++) {
            for (char& ch : line) {
                for (int j = 0; j < k; j++) {
                    cout << ch;
                }
            }
            cout << "\n";
        }
    }

    return 0;
}