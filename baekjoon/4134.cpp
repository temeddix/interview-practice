#include <cmath>
#include <iostream>

using u32 = unsigned long;

auto is_prime(u32 number) -> bool {
  if (number <= 1) {
    return false;
  } if (number <= 3) {
    return true;
  }

  if (number % 2 == 0 || number % 3 == 0) {
    return false;
  }

  u32 root = std::sqrt(number);
  for (int i = 5; i <= root; i += 6) {
    // Check 6k ± 1
    if (number % i == 0 || number % (i + 2) == 0) {
      return false;
    }
  }

  return true;
}

auto get_next_prime(u32 number) -> u32 {
  // Start with an odd number if even
  if (number <= 1) {
    return 2;
  } if (number <= 3) {
    return number;
  }

  if (number % 2 == 0) {
    number += 1;
  }

  while (true) {
    if (is_prime(number)) {
      return number;
    }
    // Skip even numbers
    number += 2;
  }
}

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int count = 0;
  std::cin >> count;

  for (int i = 0; i < count; i++) {
    u32 number = 0;
    std::cin >> number;
    std::cout << get_next_prime(number) << '\n';
  }
}