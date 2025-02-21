#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int get_max_sum(vector<vector<int>>& tower) {
  int tower_size = tower.size();
  vector<int> prev_sum = {tower[0][0]};
  prev_sum.reserve(tower_size);
  vector<int> curr_sum;
  curr_sum.reserve(tower_size);

  for (int i = 1; i < tower_size; i++) {
    int row_size = i + 1;
    curr_sum.push_back(prev_sum[0] + tower[i][0]);
    for (int j = 1; j < row_size - 1; j++) {
      int number = tower[i][j];
      int this_max = max(prev_sum[j - 1], prev_sum[j]) + number;
      curr_sum.push_back(this_max);
    }
    curr_sum.push_back(prev_sum[i - 1] + tower[i][i]);
    swap(prev_sum, curr_sum);
    curr_sum.clear();
  }

  return *max_element(prev_sum.begin(), prev_sum.end());
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int tower_size;
  cin >> tower_size;

  vector<vector<int>> tower;
  tower.reserve(tower_size);

  for (int i = 0; i < tower_size; i++) {
    vector<int> row;
    row.reserve(i);
    int row_size = i + 1;
    for (int j = 0; j < row_size; j++) {
      int number;
      cin >> number;
      row.push_back(number);
    }
    tower.push_back(row);
  }

  int max_sum = get_max_sum(tower);
  cout << max_sum << endl;
}