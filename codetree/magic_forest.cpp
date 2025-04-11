#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

struct Move {
  int row;
  int col;
};

struct Spot {
  int row;
  int col;
};

struct Enter {
  int col;
  int exit;
};

struct Golem {
  Spot spot;
  int exit;
};

struct BlockMap {
  int row_count;
  int col_count;
  vector<vector<bool>> filled;
  vector<Golem> golems;
};

constexpr int MOVE_TYPES = 4;
constexpr array<Move, 4> MOVES = {{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}};

// 골렘이 해당 상태로 배치 가능한지 확인한다.
auto is_placeable(BlockMap& block_map, Golem next_golem) -> bool {
  // 맵 밖으로 나갔다면 배치 불가능하다.
  int row_count = block_map.row_count;
  int col_count = block_map.col_count;
  Spot golem_spot = next_golem.spot;
  if (!(golem_spot.row < row_count - 1 && golem_spot.col >= 1 &&
        golem_spot.col < col_count - 1)) {
    return false;
  }

  // 다른 골렘과 겹치면 배치 불가능하다.
  for (Move move : MOVES) {
    Spot side_spot = {golem_spot.row + move.row, golem_spot.col + move.col};
    if (side_spot.row < 0) {
      continue;
    }
    if (block_map.filled[side_spot.row][side_spot.col]) {
      return false;
    }
  }

  return true;
}

// 골렘을 가장 낮은 곳에 배치한다.
auto place_golem(BlockMap& block_map, Enter enter) -> bool {
  // 골렘 상태를 준비한다.
  Golem golem = {{-2, enter.col}, enter.exit};

  // 막힐 때까지 아래로 내려 보고,
  // 왼쪽으로 돌려 내려 보고, 오른쪽으로 돌려 내려 본다.
  while (true) {
    Golem next_golem;

    // 골렘을 한 칸 내린다.
    next_golem = golem;
    next_golem.spot.row += 1;
    if (is_placeable(block_map, next_golem)) {
      golem = next_golem;
      continue;
    }

    // 골렘을 왼쪽으로 돌려 내린다.
    next_golem = golem;
    next_golem.spot.col -= 1;
    if (is_placeable(block_map, next_golem)) {
      next_golem.spot.row += 1;
      if (is_placeable(block_map, next_golem)) {
        next_golem.exit += 3;
        next_golem.exit %= MOVE_TYPES;
        golem = next_golem;
        continue;
      }
    }

    // 골렘을 오른쪽으로 돌려 내린다.
    next_golem = golem;
    next_golem.spot.col += 1;
    if (is_placeable(block_map, next_golem)) {
      next_golem.spot.row += 1;
      if (is_placeable(block_map, next_golem)) {
        next_golem.exit += 1;
        next_golem.exit %= MOVE_TYPES;
        golem = next_golem;
        continue;
      }
    }

    // 골렘이 최대한 내려갔다면 멈춘다.
    break;
  }

  // 골렘이 위쪽으로 벗어나지 않았다면 성공을, 아니라면 실패를 반환한다.
  if (golem.spot.row < 1) {
    // 잘 배치되지 않았다면 맵을 업데이트하지 않고 실패를 반환한다.
    return false;
  } else {
    // 잘 배치되었다면 맵을 업데이트하고 성공을 반환한다.
    block_map.filled[golem.spot.row][golem.spot.col] = true;
    for (Move move : MOVES) {
      Spot side_spot = {golem.spot.row + move.row, golem.spot.col + move.col};
      block_map.filled[side_spot.row][side_spot.col] = true;
    }
    block_map.golems.push_back(golem);
    return true;
  }
}

// 마지막으로 들어온 정령이 가장 남쪽으로 내려갈 수 있는 행을 구한다.
auto move_elf_down(BlockMap& block_map) -> int {
  // 골렘이 몇 마리인지 파악한다.
  vector<Golem>& golems = block_map.golems;
  int golem_count = static_cast<int>(golems.size());

  // 특정 골렘에서 갈 수 있는 다음 골렘들의 정보를 그래프 형태로 파악한다.
  vector<vector<int>> nexts(golem_count, vector<int>());
  for (int from_idx = 0; from_idx < golem_count; from_idx++) {
    Spot from_spot = golems[from_idx].spot;
    Move exit_move = MOVES[golems[from_idx].exit];
    Spot exit_spot = {from_spot.row + exit_move.row,
                      from_spot.col + exit_move.col};
    for (int to_idx = 0; to_idx < golem_count; to_idx++) {
      // 같은 골렘으로 갈 수는 없다.
      if (from_idx == to_idx) {
        continue;
      }
      // 이 골렘의 출구가 다른 골렘의 몸체와 맞닿아 있지 않으면 이동할 수 없다.
      Spot to_spot = golems[to_idx].spot;
      int perp_dist =
          abs(exit_spot.row - to_spot.row) + abs(exit_spot.col - to_spot.col);
      if (perp_dist != 2) {
        continue;
      }
      // 이동이 가능하다면 기록한다.
      nexts[from_idx].push_back(to_idx);
    }
  }

  // 방금 들어온 엘프는 마지막 골렘을 타고 있다.
  // 여기서부터 출발하여 DFS 방식으로 최대한 밑으로 내려가 본다.
  int start_golem = golem_count - 1;
  int max_row = golems[start_golem].spot.row + 1;
  vector<bool> visited(golem_count, false);
  vector<int> dfs_stack = {start_golem};
  while (!dfs_stack.empty()) {
    int curr_idx = dfs_stack.back();
    dfs_stack.pop_back();
    if (visited[curr_idx]) {
      continue;
    }
    visited[curr_idx] = true;
    max_row = max(max_row, golems[curr_idx].spot.row + 1);
    for (int next_idx : nexts[curr_idx]) {
      dfs_stack.push_back(next_idx);
    }
  }

  // 도달 가능한 가장 아래쪽 행 번호를 반환한다.
  return max_row;
}

void clear_map(BlockMap& block_map) {
  int row_count = block_map.row_count;
  int col_count = block_map.col_count;
  for (int r = 0; r < row_count; r++) {
    for (int c = 0; c < col_count; c++) {
      block_map.filled[r][c] = false;
    }
  }
  block_map.golems.clear();
}

// 프로그램을 실행한다.
auto main() -> int {
  // 입출력 속도를 높인다.
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  // 입력을 받는다.
  int row_count, col_count, elf_count;
  cin >> row_count >> col_count >> elf_count;
  vector<Enter> enters;
  for (int i = 0; i < elf_count; i++) {
    int col, exit;
    cin >> col >> exit;
    col -= 1;
    enters.push_back({col, exit});
  }

  // 맵을 준비한다.
  vector<vector<bool>> filled(row_count, vector<bool>(col_count, false));
  BlockMap block_map = {row_count, col_count, filled, vector<Golem>()};

  // 시뮬레이션을 한다.
  int dest_sum = 0;  // 정령들이 도달하는 행 번호들의 합
  for (Enter enter : enters) {
    bool is_placed = place_golem(block_map, enter);
    if (!is_placed) {
      // 맵이 꽉 차서 골렘 배치에 실패했다면 정령을 내리지 않고 맵을 비운다.
      clear_map(block_map);
      continue;
    }

    // 정령을 최대한 밑으로 내려보내고 행을 기록한다.
    int dest_col = move_elf_down(block_map);
    dest_sum += dest_col + 1;
  }

  // 결과를 출력한다.
  cout << dest_sum << '\n';
}