#include <iostream>
#include <queue>

using namespace std;

struct Edge {
  int next;
  int weight;
};

struct Node {
  vector<Edge> edges;
};

struct Cursor {
  int cost;
  int destination;
};

const int INF = 1000000007;

auto operator<(const Cursor& obj_a, const Cursor& obj_b) -> bool {
  if (obj_a.cost != obj_b.cost) {
    return obj_a.cost < obj_b.cost;
  }
  return obj_a.destination < obj_b.destination;
}

auto operator>(const Cursor& obj_a, const Cursor& obj_b) -> bool {
  if (obj_a.cost != obj_b.cost) {
    return obj_a.cost > obj_b.cost;
  }
  return obj_a.destination > obj_b.destination;
}

auto get_costs(vector<Node>& nodes, int start_node) -> vector<int> {
  int node_count = static_cast<int>(nodes.size());
  vector<int> costs(node_count, INF);
  priority_queue<Cursor, vector<Cursor>, greater<>> p_queue;

  costs[start_node] = 0;
  p_queue.push({0, start_node});

  while (!p_queue.empty()) {
    Cursor cursor = p_queue.top();
    p_queue.pop();
    for (Edge edge : nodes[cursor.destination].edges) {
      int written_cost = costs[edge.next];
      int new_cost = cursor.cost + edge.weight;
      if (new_cost < written_cost) {
        costs[edge.next] = new_cost;
        p_queue.push({new_cost, edge.next});
      }
    }
  }

  return costs;
}

auto main() -> int {
  int node_count = 0;
  int edge_count = 0;
  cin >> node_count >> edge_count;
  int start_node = 0;
  cin >> start_node;
  start_node -= 1;

  vector<Node> nodes(node_count, Node());
  for (int i = 0; i < edge_count; i++) {
    int from_node_raw = 0;
    int to_node_raw = 0;
    int weight = 0;
    cin >> from_node_raw >> to_node_raw >> weight;
    nodes[from_node_raw - 1].edges.push_back({to_node_raw - 1, weight});
  }

  vector<int> costs = get_costs(nodes, start_node);
  for (int cost : costs) {
    if (cost < INF) {
      cout << cost << '\n';
    } else {
      cout << "INF\n";
    }
  }
}