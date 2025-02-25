#include <iostream>
#include <set>
#include <unordered_set>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int not_heard_count, not_seen_count;
  std::cin >> not_heard_count >> not_seen_count;

  std::unordered_set<std::string> not_heard;
  not_heard.reserve(500000);
  for (int i = 0; i < not_heard_count; i++) {
    std::string name;
    std::cin >> name;
    not_heard.insert(name);
  }

  std::set<std::string> overlaps;
  for (int i = 0; i < not_seen_count; i++) {
    std::string name;
    std::cin >> name;
    if (not_heard.count(name)) {
      overlaps.insert(name);
    }
  }

  std::cout << overlaps.size() << '\n';
  for (const std::string& overlap : overlaps) {
    std::cout << overlap << '\n';
  }
}