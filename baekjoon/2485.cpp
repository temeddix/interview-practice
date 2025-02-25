#include <iostream>

auto get_gcd(int a, int b) -> int {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

auto get_lcm(int a, int b) -> int { return a * b / get_gcd(a, b); }

auto main() -> int {
  int count = 0;
  std::cin >> count;

  int last_position = 0;
  std::cin >> last_position;
  int first_position = last_position;
  int distance = 0;
  int distance_gcd = 0;

  int position = 0;
  std::cin >> position;
  distance = position - last_position;
  last_position = position;
  distance_gcd = distance;

  for (int i = 0; i < count - 2; i++) {
    int position = 0;
    std::cin >> position;
    int distance = position - last_position;
    last_position = position;
    distance_gcd = get_gcd(distance_gcd, distance);
  }

  int total_distance = last_position - first_position;
  int extra_trees = (total_distance / distance_gcd) + 1 - count;
  std::cout << extra_trees << '\n';
}