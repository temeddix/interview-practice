#include <cmath>
#include <iostream>

typedef unsigned long int u32;

bool is_prime(u32 number) {
  if (number <= 1) {
    return false;
  } else if (number <= 3) {
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

u32 get_next_prime(u32 number) {
  // Start with an odd number if even
  if (number <= 1) {
    return 2;
  } else if (number <= 3) {
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

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int count;
  std::cin >> count;

  for (int i = 0; i < count; i++) {
    u32 number;
    std::cin >> number;
    std::cout << get_next_prime(number) << '\n';
  }

  return 0;
}