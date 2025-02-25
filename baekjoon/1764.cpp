#include <iostream>
#include <set>
#include <unordered_set>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int not_heard_count = 0;
  int not_seen_count = 0;
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
    if (not_heard.count(name) != 0U) {
      overlaps.insert(name);
    }
  }

  std::cout << overlaps.size() << '\n';
  for (const std::string& overlap : overlaps) {
    std::cout << overlap << '\n';
  }
}