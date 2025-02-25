#include <iostream>
#include <unordered_set>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  std::unordered_set<int> cards;
  int card_count;
  std::cin >> card_count;

  for (int i = 0; i < card_count; i++) {
    int card;
    std::cin >> card;
    cards.insert(card);
  }

  int number_count;
  std::cin >> number_count;
  for (int i = 0; i < number_count; i++) {
    int number;
    std::cin >> number;
    if (cards.count(number)) {
      std::cout << 1 << ' ';
    } else {
      std::cout << 0 << ' ';
    }
  }
}