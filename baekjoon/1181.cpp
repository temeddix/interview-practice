#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

bool compare_words(const std::string& word_a, const std::string& word_b) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int a_length = word_a.length();
  int b_length = word_b.length();
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

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int count;
  std::cin >> count;
  std::vector<std::string> words;
  words.reserve(count);

  for (int i = 0; i < count; i++) {
    std::string word;
    std::cin >> word;
    words.push_back(word);
  }

  std::sort(words.begin(), words.end(), compare_words);
  std::string last_word = "";
  for (const std::string& word : words) {
    if (word == last_word) {
      continue;
    }
    std::cout << word << '\n';
    last_word = word;
  }

  return 0;
}