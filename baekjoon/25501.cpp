#include <iostream>
#include <string>

auto recursion(const std::string& s, int l, int r, int& depth) -> bool {
  depth += 1;
  if (l >= r) {
    return true;
  } if (s[l] != s[r]) {
    return false;
  }     return recursion(s, l + 1, r - 1, depth);
}

auto is_palindrome(const std::string& s, int& depth) -> bool {
  return recursion(s, 0, s.length() - 1, depth);
}

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int word_count = 0;
  std::cin >> word_count;

  for (int i = 0; i < word_count; i++) {
    std::string word;
    std::cin >> word;
    int depth = 0;
    bool palindrome = is_palindrome(word, depth);
    std::cout << palindrome << ' ' << depth << '\n';
  }
}