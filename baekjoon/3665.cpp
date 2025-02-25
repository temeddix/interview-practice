#include <iostream>
#include <queue>

using namespace std;

const int INT_INIT = -1;

struct Node {
  int incomings;
  vector<int> nexts;
};

template <typename T>
struct Result {
  T data;
  int code;
};

auto sort_nodes(vector<Node>& nodes) -> Result<vector<int>> {
  int node_count = static_cast<int>(nodes.size());
  vector<int> sorted_nodes;
  sorted_nodes.reserve(node_count);

  queue<int> bfs_queue;
  for (int i = 0; i < node_count; i++) {
    if (nodes[i].incomings == 0) {
      bfs_queue.push(i);
    }
  }

  while (!bfs_queue.empty()) {
    int idx_a = bfs_queue.front();
    bfs_queue.pop();
    sorted_nodes.push_back(idx_a);
    for (int idx_b : nodes[idx_a].nexts) {
      Node& next_node = nodes[idx_b];
      next_node.incomings -= 1;
      if (next_node.incomings == 0) {
        bfs_queue.push(idx_b);
      }
    }
  }

  if (sorted_nodes.size() != node_count) {
    return {{}, 1};
  }

  return {sorted_nodes, 0};
}

auto build_nodes(int node_count, vector<int>& last_ranks,
                 vector<vector<bool>>& swapped) -> vector<Node> {
  vector<Node> nodes;

  nodes.reserve(node_count);
  for (int i = 0; i < node_count; i++) {
    nodes.push_back({0, {}});
  }
  for (int i = 0; i < node_count; i++) {
    for (int j = i + 1; j < node_count; j++) {
      bool is_i_higher = last_ranks[i] < last_ranks[j];
      if (swapped[i][j]) {
        is_i_higher = !is_i_higher;
      }
      if (is_i_higher) {
        nodes[i].nexts.push_back(j);
        nodes[j].incomings += 1;
      } else {
        nodes[j].nexts.push_back(i);
        nodes[i].incomings += 1;
      }
    }
  }

  return nodes;
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int test_count = INT_INIT;
  cin >> test_count;

  for (int k = 0; k < test_count; k++) {
    int node_count = INT_INIT;
    cin >> node_count;

    vector<int> last_ranks(node_count);
    for (int i = 0; i < node_count; i++) {
      int node = INT_INIT;
      cin >> node;
      node -= 1;
      last_ranks[node] = i;
    }

    vector<vector<bool>> swapped(node_count,
                                 std::vector<bool>(node_count, false));
    int swapped_pairs = INT_INIT;
    cin >> swapped_pairs;
    for (int i = 0; i < swapped_pairs; i++) {
      int node_a = INT_INIT;
      int node_b = INT_INIT;
      cin >> node_a >> node_b;
      node_a -= 1;
      node_b -= 1;
      swapped[node_a][node_b] = true;
      swapped[node_b][node_a] = true;
    }

    vector<Node> nodes = build_nodes(node_count, last_ranks, swapped);

    Result<vector<int>> result = sort_nodes(nodes);
    if (result.code == 1) {
      cout << "IMPOSSIBLE";
    } else {
      for (int node : result.data) {
        cout << (node + 1) << " ";
      }
    }
    cout << "\n";
  }
}