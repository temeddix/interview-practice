#include <algorithm>
#include <iostream>
#include <vector>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int count = 0;
  std::cin >> count;
  std::vector<int> coords;
  coords.reserve(count);

  for (int i = 0; i < count; i++) {
    int coord = 0;
    std::cin >> coord;
    coords.push_back(coord);
  }

  std::vector<int> sorted = coords;
  std::sort(sorted.begin(), sorted.end());
  auto iter = std::unique(sorted.begin(), sorted.end());
  sorted.erase(iter, sorted.end());

  for (int coord : coords) {
    auto iter = std::lower_bound(sorted.begin(), sorted.end(), coord);
    int compressed = std::distance(sorted.begin(), iter);
    std::cout << compressed << ' ';
  }
}