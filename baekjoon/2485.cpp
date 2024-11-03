#include <iostream>

int get_gcd(int a, int b) {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

int get_lcm(int a, int b) { return a * b / get_gcd(a, b); }

int main() {
  int count;
  std::cin >> count;

  int last_position;
  std::cin >> last_position;
  int first_position = last_position;
  int distance;
  int distance_gcd;

  int position;
  std::cin >> position;
  distance = position - last_position;
  last_position = position;
  distance_gcd = distance;

  for (int i = 0; i < count - 2; i++) {
    int position;
    std::cin >> position;
    int distance = position - last_position;
    last_position = position;
    distance_gcd = get_gcd(distance_gcd, distance);
  }

  int total_distance = last_position - first_position;
  int extra_trees = total_distance / distance_gcd + 1 - count;
  std::cout << extra_trees << std::endl;
  return 0;
}