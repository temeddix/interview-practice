#include <iostream>
#include <string>
#include <unordered_set>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  std::string text;
  std::cin >> text;
  int text_length = text.length();

  int max_combination = text_length * (text_length + 1) / 2;
  std::unordered_set<std::string> slices;
  slices.reserve(max_combination);

  for (int i = 0; i < text_length; i++) {
    int max_extra = text_length - i;
    for (int j = 0; j < max_extra; j++) {
      std::string slice = text.substr(i, j + 1);
      slices.insert(slice);
    }
  }

  std::cout << slices.size() << std::endl;
  return 0;
}