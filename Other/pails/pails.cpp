// 
#include <bits/stdc++.h>
using namespace std;

int main() {
  freopen("pails.in", "r", stdin);
  freopen("pails.out", "w", stdout);

  int x, y, m, most = 0;
  scanf("%d %d %d", &x, &y, &m);
  // cout << x << " " << y << " " << m;
  
  for (int i = 0; i * x < m+1; i++) {
    for (int j = 0; i * x + j * y < m+1; j++) {
      most = max(i*x+j*y, most);
    }
  }

  cout << most;

	return 0;
}
