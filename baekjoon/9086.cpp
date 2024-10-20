#include <iostream>

int main() {
  int count;
  std::cin >> count;
  for (int i = 0; i < count; i++) {
    std::string word;
    std::cin >> word;
    int word_len = word.length();
    std::cout << word[0] << word[word_len - 1] << std::endl;
  }
  return 0;
}