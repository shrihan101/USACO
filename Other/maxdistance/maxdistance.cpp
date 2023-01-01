#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

struct Point {
    public:
        double x;
        double y;
        double distance(Point other) {
            double a = abs(x-other.x);
            double b = abs(y-other.y);

            double c = sqrt(pow(a, 2) + pow(b, 2));
            return c;
        }
};

int main() {
    freopen("maxdistance.in", "r", stdin);
    freopen("maxdistance.out", "w", stdout);

    int n; cin >> n;
    scanf("%d", &n);
    const int temp = n;

    vector<Point> points;
    for (int i = 1; i <= 2; i++) {
        for (int j = 0; j < n; j++) {
            int cord1; cin >> cord1;
            scanf("%d", &cord1);
            if (i == 1) {
                Point temp;
                temp.x = cord1;
                points.push_back(temp);
            } else {
                points[j].y = cord1;
            }
        }
    }

    int max = 0;
    for (int i = 0; i < points.size(); i++) {
        for (int j = 0; j < points.size(); j++) {
            double distance = points[i].distance(points[j]);
            if (distance > max) {
                max = int(distance);
            }
        }
    }

    cout << fixed << int(pow(max, 2));

    return 0;
}