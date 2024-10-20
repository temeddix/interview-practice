#include <iostream>
#include <string>

int main() {
  std::string word;
  std::cin >> word;

  int length = word.length();
  int search_count = length / 2;

  bool is_palindrome = true;
  for (int i = 0; i < search_count; i++) {
    char left = word[i];
    char right = word[length - 1 - i];
    if (left != right) {
      is_palindrome = false;
      break;
    }
  }

  std::cout << static_cast<int>(is_palindrome) << std::endl;

  return 0;
}