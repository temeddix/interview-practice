#include <array>
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

struct Cell {
  bool is_golem;
  bool is_center;
  Move center_move;  // 골렘일 때만 유효
  Move exit_move;    // `is_center`일 때만 유효
};

struct BlockMap {
  int row_count;
  int col_count;
  vector<vector<Cell>> cells;
  Spot last_elf;
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
    if (block_map.cells[side_spot.row][side_spot.col].is_golem) {
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
    int r = golem.spot.row, c = golem.spot.col;
    block_map.cells[r][c].is_golem = true;
    block_map.cells[r][c].is_center = true;
    block_map.cells[r][c].exit_move = MOVES[golem.exit];
    for (Move move : MOVES) {
      Spot side_spot = {golem.spot.row + move.row, golem.spot.col + move.col};
      int side_r = side_spot.row, side_c = side_spot.col;
      block_map.cells[side_r][side_c].is_golem = true;
      block_map.cells[side_r][side_c].center_move = {-move.row, -move.col};
    }
    block_map.last_elf = {r, c};
    return true;
  }
}

// 마지막으로 들어온 정령이 가장 남쪽으로 내려갈 수 있는 행을 구한다.
auto move_elf_down(BlockMap& block_map) -> int {
  // 현재 상황을 파악한다.
  vector<vector<Cell>>& cells = block_map.cells;
  int row_count = block_map.row_count;
  int col_count = block_map.col_count;

  // 방금 들어온 엘프는 마지막 골렘을 타고 있다.
  // 여기서부터 출발하여 DFS 방식으로 최대한 밑으로 내려가 본다.
  Spot start_spot = block_map.last_elf;
  int max_row = start_spot.row + 1;
  vector<vector<bool>> visited(row_count, vector<bool>(col_count, false));
  vector<Spot> dfs_stack = {start_spot};
  while (!dfs_stack.empty()) {
    Spot curr_center = dfs_stack.back();
    int r = curr_center.row, c = curr_center.col;
    dfs_stack.pop_back();
    if (visited[r][c]) {
      continue;
    }
    visited[r][c] = true;
    max_row = max(max_row, r + 1);
    Move exit_move = cells[r][c].exit_move;
    Spot exit_spot = {r + exit_move.row, c + exit_move.col};
    for (Move diff : MOVES) {
      int next_r = exit_spot.row + diff.row;
      int next_c = exit_spot.col + diff.col;
      if (next_r == r && next_c == c) {
        continue;
      }
      if (!(next_r >= 0 && next_r < row_count)) {
        continue;
      }
      if (!(next_c >= 0 && next_c < col_count)) {
        continue;
      }
      if (!cells[next_r][next_c].is_golem) {
        continue;
      }
      Move center_move = cells[next_r][next_c].center_move;
      Spot next_center = {next_r + center_move.row, next_c + center_move.col};
      dfs_stack.push_back(next_center);
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
      block_map.cells[r][c].is_golem = false;
      block_map.cells[r][c].is_center = false;
      block_map.cells[r][c].exit_move = {-1, -1};
      block_map.cells[r][c].center_move = {-1, -1};
      block_map.last_elf = {-1, -1};
    }
  }
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
  vector<vector<Cell>> cells(
      row_count, vector<Cell>(col_count, {false, false, {-1, -1}, {-1, -1}}));
  BlockMap block_map = {row_count, col_count, cells, {-1, -1}};

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