#include <chrono>  // For std::chrono::seconds, milliseconds, etc.
#include <iostream>
#include <queue>

using namespace std;

struct Node {
  int incomings;
  vector<int> nexts;
};

template <typename T>
struct Result {
  T data;
  int code;
};

Result<vector<int>> sort_nodes(vector<Node>& nodes) {
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

  if (sorted_nodes.size() != node_count) {
    return {{}, 1};
  }

  return {sorted_nodes, 0};
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int test_count;
  cin >> test_count;

  for (int t = 0; t < test_count; t++) {
    int node_count;
    cin >> node_count;

    vector<int> last_ranks(node_count);
    for (int i = 0; i < node_count; i++) {
      int node;
      cin >> node;
      node -= 1;
      last_ranks[node] = i;
    }

    vector<vector<bool>> swapped(node_count,
                                 std::vector<bool>(node_count, false));
    int swapped_pairs;
    cin >> swapped_pairs;
    for (int i = 0; i < swapped_pairs; i++) {
      int node_a, node_b;
      cin >> node_a >> node_b;
      node_a -= 1;
      node_b -= 1;
      swapped[node_a][node_b] = true;
      swapped[node_b][node_a] = true;
    }

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

    Result<vector<int>> result = sort_nodes(nodes);
    if (result.code == 1) {
      cout << "IMPOSSIBLE";
    } else {
      for (int node : result.data) {
        cout << (node + 1) << " ";
      }
    }
    cout << endl;
  }
}