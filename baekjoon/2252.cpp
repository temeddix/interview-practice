#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Node {
  int incomings;
  vector<int> nexts;
};

auto sort_nodes(vector<Node>& nodes) -> vector<int> {
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

  return sorted_nodes;
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int node_count = 0;
  int edge_count = 0;
  cin >> node_count >> edge_count;

  vector<Node> nodes;
  nodes.reserve(node_count);
  for (int i = 0; i < node_count; i++) {
    nodes.push_back({0, {}});
  }

  for (int i = 0; i < edge_count; i++) {
    int node_a = 0;
    int node_b = 0;
    cin >> node_a >> node_b;
    node_a -= 1;
    node_b -= 1;
    nodes[node_a].nexts.push_back(node_b);
    nodes[node_b].incomings += 1;
  }

  vector<int> sorted_nodes = sort_nodes(nodes);
  for (int node : sorted_nodes) {
    cout << (node + 1) << ' ';
  }
}