#include <algorithm>
#include <iostream>
#include <optional>
#include <vector>

using namespace std;

const int INF = 1000000007;

auto use_min_coins(vector<int>& coins, int goal_value) -> optional<int> {
  vector<int> record;
  record.reserve(goal_value + 1);
  record.push_back(0);

  for (int i = 1; i <= goal_value; i++) {
    int min_count = INF;
    for (int coin : coins) {
      int prev_value = i - coin;
      if (0 <= prev_value) {
        min_count = min(min_count, record[prev_value] + 1);
      }
    }
    record.push_back(min_count);
  }

  int min_coins = record.back();
  return (min_coins == INF) ? nullopt : optional(min_coins);
}

auto main() -> int {
  int coin_count = 0;
  int goal_value = 0;
  cin >> coin_count >> goal_value;

  vector<int> coins;
  coins.reserve(coin_count);
  for (int i = 0; i < coin_count; i++) {
    int coin = 0;
    cin >> coin;
    coins.push_back(coin);
  }

  optional<int> min_coins = use_min_coins(coins, goal_value);
  cout << (min_coins ? *min_coins : -1) << '\n';
}