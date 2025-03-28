#include <iostream>
#include <optional>
#include <queue>

using namespace std;

struct Node {
  int incomings;
  vector<int> nexts;
};

auto sort_nodes(vector<Node>& nodes) -> optional<vector<int>> {
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

  if (static_cast<int>(sorted_nodes.size()) != node_count) {
    return nullopt;
  }

  return sorted_nodes;
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

  int test_count = 0;
  cin >> test_count;

  for (int k = 0; k < test_count; k++) {
    int node_count = 0;
    cin >> node_count;

    vector<int> last_ranks(node_count);
    for (int i = 0; i < node_count; i++) {
      int node = 0;
      cin >> node;
      node -= 1;
      last_ranks[node] = i;
    }

    vector<vector<bool>> swapped(node_count,
                                 std::vector<bool>(node_count, false));
    int swapped_pairs = 0;
    cin >> swapped_pairs;
    for (int i = 0; i < swapped_pairs; i++) {
      int node_a = 0;
      int node_b = 0;
      cin >> node_a >> node_b;
      node_a -= 1;
      node_b -= 1;
      swapped[node_a][node_b] = true;
      swapped[node_b][node_a] = true;
    }

    vector<Node> nodes = build_nodes(node_count, last_ranks, swapped);

    optional<vector<int>> option = sort_nodes(nodes);
    if (option) {
      for (int node : *option) {
        cout << (node + 1) << ' ';
      }
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << '\n';
  }
}