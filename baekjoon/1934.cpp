#include <iostream>

int get_gcd(int a, int b) {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

int get_lcm(int a, int b) { return (a * b) / get_gcd(a, b); }

void get_result() {
  int number_a, number_b;
  std::cin >> number_a >> number_b;

  int lcm = get_lcm(number_a, number_b);
  std::cout << lcm << std::endl;
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
}