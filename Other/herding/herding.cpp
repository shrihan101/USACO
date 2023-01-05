#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("herding.in", "r", stdin);
	freopen("herding.out", "w", stdout);

	int a, b, c;
	int minSwaps = 2;
	int maxSwaps = 0;
	scanf("%d %d %d", &a, &b, &c);

	if (a > b) {
		swap(b, a);
	}
	if (b > c) {
		swap(c, b);
	}
	if (a > b) {
		swap(a, b);
	}

	if (a + 1 == b && b + 1 == c && a + 2 == c) {
		cout << 0 << endl;
	} else if (b == a + 2 || c == b + 2) {
		cout << 1 << endl;
	} else {
		cout << 2 << endl;
	}

	maxSwaps = max(b-a, c-b) - 1;

	cout << maxSwaps;
	return 0;
}