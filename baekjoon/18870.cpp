#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int count;
  std::cin >> count;
  std::vector<int> coords;
  coords.reserve(count);

  for (int i = 0; i < count; i++) {
    int coord;
    std::cin >> coord;
    coords.push_back(coord);
  }

  std::vector<int> sorted = coords;
  std::sort(sorted.begin(), sorted.end());
  std::vector<int>::iterator iter = std::unique(sorted.begin(), sorted.end());
  sorted.erase(iter, sorted.end());

  for (int coord : coords) {
    std::vector<int>::iterator iter =
        std::lower_bound(sorted.begin(), sorted.end(), coord);
    int compressed = std::distance(sorted.begin(), iter);
    std::cout << compressed << ' ';
  }

  return 0;
}