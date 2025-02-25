#include <iostream>
#include <unordered_set>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int count_a = 0;
  int count_b = 0;
  std::cin >> count_a >> count_b;

  std::unordered_set<int> set_a;
  set_a.reserve(count_a);
  int overlap_count = 0;
  for (int i = 0; i < count_a; i++) {
    int number = 0;
    std::cin >> number;
    set_a.insert(number);
  }
  for (int i = 0; i < count_b; i++) {
    int number = 0;
    std::cin >> number;
    if (set_a.count(number) != 0U) {
      overlap_count += 1;
    }
  }

  int symmetrical_diff = count_a + count_b - (overlap_count * 2);
  std::cout << symmetrical_diff << '\n';
}