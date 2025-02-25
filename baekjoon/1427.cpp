#include <algorithm>
#include <iostream>
#include <string>

int main() {
  int number;
  std::cin >> number;

  std::string text = std::to_string(number);
  std::sort(text.begin(), text.end(), std::greater<char>());

  std::cout << text;
}