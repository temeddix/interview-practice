#include <cmath>
#include <iostream>
#include <vector>

auto is_prime(int number) -> bool {
  if (number <= 1) {
    return false;
  }
  if (number <= 3) {
    return true;
  }

  if (number % 2 == 0 || number % 3 == 0) {
    return false;
  }

  for (int i = 5; i * i <= number; i += 6) {
    if (number % i == 0 || number % (i + 2) == 0) {
      return false;
    }
  }

  return true;
}

auto main() -> int {
  std::vector<bool> are_prime;
  are_prime.reserve(1000000);
  for (int i = 0; i < 1000000; i++) {
    are_prime.push_back(is_prime(i));
  }

  int count = 0;
  std::cin >> count;
  for (int i = 0; i < count; i++) {
    int number = 0;
    std::cin >> number;
    int partition_count = 0;
    for (int j = 2; j <= number / 2; j++) {
      int other = number - j;
      if (are_prime[j] && are_prime[other]) {
        partition_count += 1;
      }
    }
    std::cout << partition_count << '\n';
  }
}