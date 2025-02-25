#include <array>
#include <iostream>

auto main() -> int {
  int n = 0;
  int m = 0;
  std::cin >> n >> m;

  std::array<int, 100> cards{};
  for (int i = 0; i < n; i++) {
    std::cin >> cards[i];
  }

  int biggest_sum = 0;
  for (int i = 0; i < n - 2; i++) {
    for (int j = i + 1; j < n - 1; j++) {
      for (int k = j + 1; k < n; k++) {
        int sum = cards[i] + cards[j] + cards[k];
        if (biggest_sum < sum && sum <= m) {
          biggest_sum = sum;
        }
      }
    }
  }

  std::cout << biggest_sum << '\n';
}