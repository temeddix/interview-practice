#include <iostream>

auto get_gcd(int a, int b) -> int {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

auto get_lcm(int a, int b) -> int { return (a * b) / get_gcd(a, b); }

void get_result() {
  int number_a = 0;
  int number_b = 0;
  std::cin >> number_a >> number_b;

  int lcm = get_lcm(number_a, number_b);
  std::cout << lcm << '\n';
}

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int repeat = 0;
  std::cin >> repeat;
  for (int i = 0; i < repeat; i++) {
    get_result();
  }
}