#include <iostream>
#include <string>

bool recursion(const std::string& s, int l, int r, int& depth) {
  depth += 1;
  if (l >= r)
    return true;
  else if (s[l] != s[r])
    return false;
  else
    return recursion(s, l + 1, r - 1, depth);
}

bool is_palindrome(const std::string& s, int& depth) {
  return recursion(s, 0, s.length() - 1, depth);
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int word_count;
  std::cin >> word_count;

  for (int i = 0; i < word_count; i++) {
    std::string word;
    std::cin >> word;
    int depth = 0;
    bool palindrome = is_palindrome(word, depth);
    std::cout << palindrome << ' ' << depth << '\n';
  }

  return 0;
}