#include <cmath>
#include <iostream>

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
    // Check 6k-1 and 6k+1
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

  int start, end;
  std::cin >> start >> end;

  for (int i = start; i <= end; i++) {
    if (is_prime(i)) {
      std::cout << i << '\n';
    };
  }
}