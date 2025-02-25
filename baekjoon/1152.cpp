#include <iostream>
#include <string>

int main() {
  std::string all_words;
  std::getline(std::cin, all_words);
  bool finding = true;
  int word_count = 0;
  for (auto letter : all_words) {
    if (letter == ' ') {
      finding = true;
    } else if (finding) {
      word_count += 1;
      finding = false;
    }
  }
  std::cout << word_count;
}