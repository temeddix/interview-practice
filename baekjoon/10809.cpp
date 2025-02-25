#include <iostream>
#include <string>

int main() {
  std::string word_s;
  std::cin >> word_s;
  for (int i = 'a'; i <= 'z'; i++) {
    char letter = i;
    int first_index = -1;
    int current_index = -1;
    for (auto each_letter : word_s) {
      current_index += 1;
      if (each_letter == letter) {
        first_index = current_index;
        break;
      }
    }
    std::cout << first_index << ' ';
  }
}