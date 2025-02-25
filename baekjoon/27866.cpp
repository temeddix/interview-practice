#include <array>
#include <iostream>

int main() {
  std::array<char, 1000> word;
  std::cin >> word.data();
  int index;
  std::cin >> index;
  std::cout << word[index - 1] << std::endl;
}