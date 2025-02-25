#include <algorithm>
#include <iostream>
#include <vector>

struct Point {
  int x;
  int y;
};

auto compare_points(Point pt_a, Point pt_b) -> bool {
  if (pt_a.y != pt_b.y) {
    return pt_a.y < pt_b.y;
  }     return pt_a.x < pt_b.x;
 
}

auto main() -> int {
  std::ios::sync_with_stdio(0);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int count = 0;
  std::cin >> count;
  std::vector<Point> points;
  points.reserve(count);

  for (int i = 0; i < count; i++) {
    int x = 0;
    int y = 0;
    std::cin >> x >> y;
    points.push_back({x, y});
  }

  std::sort(points.begin(), points.end(), compare_points);
  for (Point pt : points) {
    std::cout << pt.x << ' ' << pt.y << '\n';
  }
}