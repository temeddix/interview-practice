#include <cmath>
#include <iostream>

auto is_prime(int number) -> bool {
  if (number <= 1) {
    return false;
  } if (number <= 3) {
    return true;
  }

  if (number % 2 == 0 || number % 3 == 0) {
    return false;
  }

  int root = std::sqrt(number);
  for (int i = 5; i <= root; i += 6) {
    // Check 6k-1 and 6k+1
    if (number % i == 0 || number % (i + 2) == 0) {
      return false;
    }
  }

  return true;
}

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int start = 0;
  int end = 0;
  std::cin >> start >> end;

  for (int i = start; i <= end; i++) {
    if (is_prime(i)) {
      std::cout << i << '\n';
    };
  }
}