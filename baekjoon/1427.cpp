#include <algorithm>
#include <iostream>
#include <string>

auto main() -> int {
  int number = 0;
  std::cin >> number;

  std::string text = std::to_string(number);
  std::sort(text.begin(), text.end(), std::greater<char>());

  std::cout << text;
}