#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

constexpr int INVALID = 1'000'000'007;

struct Open {
  int idx_a;
  int idx_b;
};

auto get_min_record(vector<vector<int>>& dp_array, int cells) -> int {
  int min_movements = INVALID;
  for (int i = 0; i < cells; i++) {
    for (int j = 0; j < cells; j++) {
      min_movements = min(min_movements, dp_array[i][j]);
    }
  }
  return min_movements;
}

auto move_doors(int cells, vector<int>& accesses, Open open) -> int {
  vector<vector<int>> dp_prev(cells, vector(cells, INVALID));
  dp_prev[open.idx_a][open.idx_b] = 0;
  dp_prev[open.idx_b][open.idx_a] = 0;
  vector<vector<int>> dp_curr(cells, vector(cells, INVALID));

  for (int access : accesses) {
    // Fill in the current status.
    for (int i = 0; i < cells; i++) {
      for (int j = 0; j < cells; j++) {
        int dist = 0;

        // `i` and `j` represent previously open cells.
        if (i == j) {
          continue;
        }

        // When closing the cell at `i`
        if (access != j) {
          dist = abs(access - i);
          int written = dp_curr[access][j];
          dp_curr[access][j] = min(written, dp_prev[i][j] + dist);
          dp_curr[j][access] = min(written, dp_prev[i][j] + dist);
        }

        // When closing the cell at `j`
        if (access != i) {
          dist = abs(access - j);
          int written = dp_curr[access][i];
          dp_curr[access][i] = min(written, dp_prev[i][j] + dist);
          dp_curr[i][access] = min(written, dp_prev[i][j] + dist);
        }
      }
    }

    // Prepare to go onto the next step.
    swap(dp_prev, dp_curr);
    for (int i = 0; i < cells; i++) {
      for (int j = 0; j < cells; j++) {
        dp_curr[i][j] = INVALID;
      }
    }
  }

  return get_min_record(dp_prev, cells);
}

auto main() -> int {
  int cells = 0;
  cin >> cells;

  Open open = {0, 0};
  cin >> open.idx_a >> open.idx_b;
  open.idx_a -= 1;
  open.idx_b -= 1;

  int turns = 0;
  cin >> turns;

  vector<int> accesses;
  accesses.reserve(turns);
  for (int i = 0; i < turns; i++) {
    int access = 0;
    cin >> access;
    access -= 1;
    accesses.push_back(access);
  }

  cout << move_doors(cells, accesses, open) << '\n';
}