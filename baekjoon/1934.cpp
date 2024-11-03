#include <iostream>

void get_result() {
  int number_a, number_b;
  std::cin >> number_a >> number_b;

  if (number_b % number_a == 0) {
    std::cout << number_b << std::endl;
    return;
  } else if (number_a % number_b == 0) {
    std::cout << number_a << std::endl;
    return;
  }

  int sum_a = number_a;
  int sum_b = number_b;
  while (sum_a != sum_b) {
    if (sum_a < sum_b) {
      sum_a += number_a;
    } else {
      sum_b += number_b;
    }
  }

  std::cout << sum_b << std::endl;
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int repeat;
  std::cin >> repeat;
  for (int i = 0; i < repeat; i++) {
    get_result();
  }

  return 0;
}