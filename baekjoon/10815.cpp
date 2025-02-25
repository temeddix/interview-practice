#include <iostream>
#include <unordered_set>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  std::unordered_set<int> cards;
  int card_count = 0;
  std::cin >> card_count;

  for (int i = 0; i < card_count; i++) {
    int card = 0;
    std::cin >> card;
    cards.insert(card);
  }

  int number_count = 0;
  std::cin >> number_count;
  for (int i = 0; i < number_count; i++) {
    int number = 0;
    std::cin >> number;
    if (cards.count(number) != 0U) {
      std::cout << 1 << ' ';
    } else {
      std::cout << 0 << ' ';
    }
  }
}