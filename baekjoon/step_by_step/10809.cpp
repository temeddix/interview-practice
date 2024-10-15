#include <iostream>
#include <string>

int main() {
  std::string word_s;
  std::cin >> word_s;
  int word_len = word_s.length();
  for (int i = static_cast<int>('a'); i <= static_cast<int>('z'); i++) {
    char letter = static_cast<char>(i);
    int first_index = -1;
    for (int j = 0; j < word_len; j++) {
      if (word_s[j] == letter) {
        first_index = j;
        break;
      }
    }
    std::cout << first_index << ' ';
  }
  return 0;
}