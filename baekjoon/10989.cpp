#include <array>
#include <iostream>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int count = 0;
  std::cin >> count;

  std::array<int, 10000> occurrences{};
  occurrences.fill(0);
  for (int i = 0; i < count; i++) {
    int number = 0;
    std::cin >> number;
    occurrences[number - 1] += 1;
  }

  for (int i = 0; i < 10000; i++) {
    int occurence = occurrences[i];
    for (int j = 0; j < occurence; j++) {
      std::cout << i + 1 << '\n';
    }
  }
}