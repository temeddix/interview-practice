#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Node {
  int incomings;
  vector<int> nexts;
};

vector<int> sort_nodes(vector<Node>& nodes) {
  int node_count = nodes.size();
  vector<int> sorted_nodes;
  sorted_nodes.reserve(node_count);

  queue<int> bfs_queue;
  for (int i = 0; i < node_count; i++) {
    if (nodes[i].incomings == 0) {
      bfs_queue.push(i);
    }
  }

  while (!bfs_queue.empty()) {
    int i = bfs_queue.front();
    bfs_queue.pop();
    sorted_nodes.push_back(i);
    for (int j : nodes[i].nexts) {
      Node& next_node = nodes[j];
      next_node.incomings -= 1;
      if (next_node.incomings == 0) {
        bfs_queue.push(j);
      }
    }
  }

  return sorted_nodes;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int node_count, edge_count;
  cin >> node_count >> edge_count;

  vector<Node> nodes;
  nodes.reserve(node_count);
  for (int i = 0; i < node_count; i++) {
    nodes.push_back({0, {}});
  }

  for (int i = 0; i < edge_count; i++) {
    int node_a, node_b;
    cin >> node_a >> node_b;
    node_a -= 1;
    node_b -= 1;
    nodes[node_a].nexts.push_back(node_b);
    nodes[node_b].incomings += 1;
  }

  vector<int> sorted_nodes = sort_nodes(nodes);
  for (int node : sorted_nodes) {
    cout << (node + 1) << " ";
  }
}