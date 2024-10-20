#include <array>
#include <iostream>

int main() {
  std::array<char, 101> word;
  std::cin >> word.data();

  int croatia_letters = 0;
  for (int i = 0; word[i] != '\0'; i++) {
    char current = word[i];
    char next_1 = word[i + 1];
    char next_2 = word[i + 2];
    if (current == 'c' && next_1 == '=') {
      i += 1;
    } else if (current == 'c' && next_1 == '-') {
      i += 1;
    } else if (current == 'd' && next_1 == 'z' && next_2 == '=') {
      i += 2;
    } else if (current == 'd' && next_1 == '-') {
      i += 1;
    } else if (current == 'l' && next_1 == 'j') {
      i += 1;
    } else if (current == 'n' && next_1 == 'j') {
      i += 1;
    } else if (current == 's' && next_1 == '=') {
      i += 1;
    } else if (current == 'z' && next_1 == '=') {
      i += 1;
    }
    croatia_letters += 1;
  }

  std::cout << croatia_letters << std::endl;

  return 0;
}