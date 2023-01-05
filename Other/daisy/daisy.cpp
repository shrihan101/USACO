#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
	freopeon("daisy.in", "r", stdin);
	
	int n;
	vector<int> nums;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		int temp = 0;
		cin >> temp;
		nums.push_back(temp);
	}

	
	return 0;
}
