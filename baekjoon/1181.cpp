#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

auto compare_words(const std::string& word_a, const std::string& word_b)
    -> bool {
  int a_length = static_cast<int>(word_a.length());
  int b_length = static_cast<int>(word_b.length());
  if (a_length != b_length) {
    return a_length < b_length;
  }
  for (int i = 0; i < a_length; i++) {
    char letter_a = word_a[i];
    char letter_b = word_b[i];
    if (letter_a != letter_b) {
      return letter_a < letter_b;
    }
  }
  return false;
}

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int count = 0;
  std::cin >> count;
  std::vector<std::string> words;
  words.reserve(count);

  for (int i = 0; i < count; i++) {
    std::string word;
    std::cin >> word;
    words.push_back(word);
  }

  std::sort(words.begin(), words.end(), compare_words);
  std::string last_word;
  for (const std::string& word : words) {
    if (word == last_word) {
      continue;
    }
    std::cout << word << '\n';
    last_word = word;
  }
}