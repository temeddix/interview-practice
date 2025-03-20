#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

auto split_string(string& text, char delimiter) -> vector<string> {
  istringstream stream(text);
  vector<string> tokens;
  string token;
  while (getline(stream, token, delimiter)) {
    tokens.push_back(token);
  }
  return tokens;
}

auto join_strings(vector<string>& texts, char delimiter) -> string {
  ostringstream stream;
  for (size_t i = 0; i < texts.size(); i++) {
    if (i > 0) {
      stream << delimiter;
    }
    stream << texts[i];
  }
  return stream.str();
}

auto flip_words(string& text) -> string {
  vector<string> words = split_string(text, ' ');
  for (string& word : words) {
    reverse(word.begin(), word.end());
  }
  return join_strings(words, ' ');
}

auto main() -> int {
  int cases = 0;
  cin >> cases;
  cin.ignore();
  for (int i = 0; i < cases; i++) {
    string text;
    getline(cin, text);
    cout << flip_words(text) << '\n';
  }
}