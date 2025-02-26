#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

auto get_max_price_sum(int card_count, vector<int>& card_prices) -> int {
  vector<int> max_price_sums(card_count + 1, 0);

  for (int i = 1; i <= card_count; i++) {
    int new_sum = 0;
    for (int new_cards = 1; new_cards <= i; new_cards++) {
      int cost = card_prices[new_cards - 1];
      int prev_cards = i - new_cards;
      int prev_sum = max_price_sums[prev_cards];
      new_sum = max(new_sum, prev_sum + cost);
    }
    max_price_sums[i] = new_sum;
  }

  return max_price_sums[card_count];
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int card_count = 0;
  cin >> card_count;

  vector<int> card_prices;
  card_prices.reserve(card_count);
  for (int i = 0; i < card_count; i++) {
    int card_price = 0;
    cin >> card_price;
    card_prices.push_back(card_price);
  }

  int max_price_sum = get_max_price_sum(card_count, card_prices);
  cout << max_price_sum << '\n';
}