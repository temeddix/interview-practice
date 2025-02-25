#include <cmath>
#include <iostream>
#include <string>

int main() {
  int n;
  std::cin >> n;

  int creator = 0;
  // Sum of each digit never exceeds 54,
  // because `n` is smaller or equal to 1 million.
  for (int i = n - 54; i < n; i++) {
    int digit_sum = 0;
    std::string string_i = std::to_string(i);
    for (char digit : string_i) {
      digit_sum += digit - '0';
    }
    if (i + digit_sum == n) {
      creator = i;
      break;
    }
  }

  std::cout << creator << std::endl;
}