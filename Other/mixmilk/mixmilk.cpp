#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    freopen("mixmilk.in", "r", stdin);
    freopen("mixmilk.out", "w", stdout);

    int c1, m1, c2, m2, c3, m3;
    scanf("%d %d\n%d %d\n%d %d", &c1, &m1, &c2, &m2, &c3, &m3);
    int array[3] = {c1, c2, c3};

    for (int i = 0; i < 100; i+=1) {
        switch(i % 3) {
            case 0:
                m2 += m1;
                m1 = 0;
                if (m2 > c2) {
                    int more = m2-c2;
                    m2 = c2;
                    m1 += more;
                }
                break;
            case 1:
                m3 += m2;
                m2 = 0;
                if (m3 > c3) {
                    int more = m3-c3;
                    m3 = c3;
                    m2 += more;
                }
                break;
            case 2:
                m1 += m3;
                m3 = 0;
                if (m1 > c1) {
                    int more = m1-c1;
                    m1 = c1;
                    m3 = 0;
                    m3 += more;
                }
                break;
        }
    }

    cout << m1 << "\n" << m2 << "\n" << m3;
    return 0;
}