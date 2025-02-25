#include <algorithm>
#include <array>
#include <iostream>
#include <string>

int main() {
  std::string input_a, input_b;
  std::cin >> input_a >> input_b;

  std::string reversed_a = input_a;
  std::string reversed_b = input_b;
  std::reverse(reversed_a.begin(), reversed_a.end());
  std::reverse(reversed_b.begin(), reversed_b.end());

  int number_a = std::stoi(reversed_a);
  int number_b = std::stoi(reversed_b);

  std::cout << std::max(number_a, number_b) << std::endl;
}