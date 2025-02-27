#include <iostream>
#include <vector>

using namespace std;

const int INF = 1000000007;
const int INVALID_COST = 0;

auto get_min_cycle_cost(int node_count, vector<vector<int>>& costs) -> int {
  // Because the node count is not bigger than 16,
  // the inner vector in this DP array is never bigger than 65536.
  int all_visited = (1 << node_count) - 1;
  vector<vector<int>> dp_array(node_count, vector<int>(all_visited + 1, INF));
  dp_array[0][0] = 0;

  // Assume we start from the node number zero.
  for (int visited = 0; visited <= all_visited; visited++) {
    for (int current_node = 0; current_node < node_count; current_node++) {
      int current_cost = dp_array[current_node][visited];
      if (current_cost == INF) {
        // Not searched yet.
        continue;
      }
      for (int next_node = 0; next_node < node_count; next_node++) {
        int extra_cost = costs[current_node][next_node];
        if (extra_cost == INVALID_COST) {
          // There's no road, or it's the same city.
          continue;
        }
        if (static_cast<bool>(visited & (1 << next_node))) {
          // Has already visited the next node.
          continue;
        }
        int new_visited = visited | (1 << next_node);
        int written_cost = dp_array[next_node][new_visited];
        int new_cost = current_cost + extra_cost;
        if (new_cost < written_cost) {
          dp_array[next_node][new_visited] = new_cost;
        }
      }
    }
  }

  // Get the cost of destination zero with all visited status.
  return dp_array[0][all_visited];
}

auto main() -> int {
  int node_count = 0;
  cin >> node_count;

  vector<vector<int>> costs(node_count, vector<int>(node_count, INVALID_COST));
  for (int i = 0; i < node_count; i++) {
    for (int j = 0; j < node_count; j++) {
      int cost = 0;
      cin >> cost;
      costs[i][j] = cost;
    }
  }

  cout << get_min_cycle_cost(node_count, costs) << '\n';
}