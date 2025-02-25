#include <iostream>
#include <unordered_map>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int count = 0;
  std::cin >> count;
  std::unordered_map<int, int> occurences;
  for (int i = 0; i < count; i++) {
    int number = 0;
    std::cin >> number;
    if (occurences.count(number) == 0U) {
      occurences[number] = 0;
    }
    occurences[number] += 1;
  }

  int check = 0;
  std::cin >> check;
  for (int i = 0; i < check; i++) {
    int number = 0;
    std::cin >> number;
    std::cout << occurences[number] << ' ';
  }
}