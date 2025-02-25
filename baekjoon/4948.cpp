#include <cmath>
#include <iostream>
#include <vector>

bool is_prime(int number) {
  if (number <= 1) {
    return false;
  } else if (number <= 3) {
    return true;
  }

  if (number % 2 == 0 || number % 3 == 0) {
    return false;
  }

  int root = std::sqrt(number);
  for (int i = 5; i <= root; i += 6) {
    if (number % i == 0 || number % (i + 2) == 0) {
      return false;
    }
  }

  return true;
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  std::vector<bool> are_prime;
  are_prime.reserve(250000);
  for (int i = 0; i < 250000; i++) {
    are_prime.push_back(is_prime(i));
  }

  while (true) {
    int number;
    std::cin >> number;
    if (number == 0) {
      break;
    }
    int prime_count = 0;
    int find_until = number * 2;
    for (int i = number + 1; i <= find_until; i++) {
      if (are_prime[i]) {
        prime_count += 1;
      }
    }
    std::cout << prime_count << '\n';
  }
}