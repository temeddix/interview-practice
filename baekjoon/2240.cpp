#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int INVALID = -1;

int calculate_max_yield(vector<bool>& fall_sides, int move_limit) {
  vector<int> prev_yield(move_limit + 1, INVALID);
  prev_yield[0] = 0;
  vector<int> curr_yield;
  curr_yield.reserve(move_limit + 1);

  for (bool fall_side : fall_sides) {
    curr_yield.push_back(prev_yield[0] + !fall_side);

    for (int i = 1; i <= move_limit; i++) {
      bool stand_side = i % 2;
      bool gets_plum = stand_side == fall_side;
      int moving_prev = prev_yield[i - 1];
      int staying_prev = prev_yield[i];
      if (moving_prev == INVALID) {
        curr_yield.push_back(INVALID);
      } else if (staying_prev == INVALID) {
        curr_yield.push_back(moving_prev + gets_plum);
      } else {
        int new_value = max(moving_prev, staying_prev) + gets_plum;
        curr_yield.push_back(new_value);
      }
    }

    swap(prev_yield, curr_yield);
    curr_yield.clear();
  }

  return *max_element(prev_yield.begin(), prev_yield.end());
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int seconds, move_limit;
  cin >> seconds >> move_limit;

  vector<bool> fall_sides;
  fall_sides.reserve(seconds);
  for (int i = 0; i < seconds; i++) {
    int fall_side;
    cin >> fall_side;
    fall_sides.push_back(fall_side == 1 ? false : true);
  }

  int max_yield = calculate_max_yield(fall_sides, move_limit);
  cout << max_yield;
}