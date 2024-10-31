#include <algorithm>
#include <iostream>
#include <vector>

struct Point {
  int x;
  int y;
};

bool compare_points(Point pt_a, Point pt_b) {
  if (pt_a.x != pt_b.x) {
    return pt_a.x < pt_b.x;
  } else {
    return pt_a.y < pt_b.y;
  }
}

int main() {
  int count;
  std::cin >> count;
  std::vector<Point> points;
  points.reserve(count);

  for (int i = 0; i < count; i++) {
    int x, y;
    std::cin >> x >> y;
    points.push_back({x, y});
  }

  std::sort(points.begin(), points.end(), compare_points);
  for (Point pt : points) {
    std::cout << pt.x << ' ' << pt.y << '\n';
  }

  return 0;
}