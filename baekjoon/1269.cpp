#include <iostream>
#include <unordered_set>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int count_a, count_b;
  std::cin >> count_a >> count_b;

  std::unordered_set<int> set_a;
  set_a.reserve(count_a);
  int overlap_count;
  for (int i = 0; i < count_a; i++) {
    int number;
    std::cin >> number;
    set_a.insert(number);
  }
  for (int i = 0; i < count_b; i++) {
    int number;
    std::cin >> number;
    if (set_a.count(number)) {
      overlap_count += 1;
    }
  }

  int symmetrical_diff = count_a + count_b - overlap_count * 2;
  std::cout << symmetrical_diff << std::endl;

  return 0;
}