#include <algorithm>
#include <array>
#include <iostream>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

namespace {

// 가장 작은 웜홀이 가지는 블록 번호.
constexpr int BASE_WORM = 6;

// 맵 위에서의 위치.
struct Spot {
  int row;
  int col;
};

// 움직임 벡터.
struct Move {
  int row;
  int col;
};

// 각각의 움직임 벡터가 가지는 번호이며, 시계 방향임.
constexpr array<Move, 4> MOVES = {{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}};

// 움직임 벡터의 종류 개수.
constexpr int MOVE_TYPES = 4;

// 맵을 구성하는 각 칸.
struct Cell {
  // 입력으로 주어진 칸의 모양.
  int shape;
  // 현재 게임이 이 지점에서 출발했는지의 여부.
  bool is_start;
};

// 전체 맵의 정보.
struct BlockMap {
  // 맵의 크기.
  int map_size;
  // 맵을 구성하는 칸들.
  vector<vector<Cell>> cells;
  // 웜홀들을 의미하며 인덱스 0은 6번에, 인덱스 4는 10번에 대응됨.
  array<pair<Spot, Spot>, 5> worms;
};

// 해당 좌표가 맵 내에 있는지 확인한다.
auto is_inside_map(Spot spot, int map_size) -> bool {
  if (!(spot.row >= 0 && spot.row < map_size)) {
    return false;
  }
  if (!(spot.col >= 0 && spot.col < map_size)) {
    return false;
  }
  return true;
}

// 반사되는 방식.
constexpr array<array<int, 4>, 6> HITS = {{
    {0, 1, 2, 3},  // 모양 0: 변경 없음
    {2, 3, 1, 0},  // 모양 1
    {1, 3, 0, 2},  // 모양 2
    {3, 2, 0, 1},  // 모양 3
    {2, 0, 3, 1},  // 모양 4
    {2, 3, 0, 1}   // 모양 5: 반대 방향
}};

// 공을 반사시킨다.
auto hit_ball(int move_idx, int shape) -> int {
  if (shape >= 0 && shape <= 5) {
    return HITS[shape][move_idx];
  }
  return move_idx;
}

// 해당 핀볼 맵과 시작 조건에서 나오는 점수를 구한다.
auto simulate(BlockMap& block_map, int start_r, int start_c, int m) -> int {
  // 초기 상태를 준비한다.
  int r = start_r, c = start_c;
  int score = 0;
  bool first = true;
  bool finished = false;

  // 공을 반복적으로 옮기며 게임을 진행한다.
  while (true) {
    // 블랙홀에 도달했거나, 시작 지점으로 돌아왔다면 게임을 멈춘다.
    if (finished || (!first && start_r == r && start_c == c)) break;
    first = false;

    // 공을 옮긴다.
    r += MOVES[m].row;
    c += MOVES[m].col;

    // 공이 정반사된다면 점수를 계산할 수 있다.
    if (!is_inside_map({r, c}, block_map.map_size)) {
      score = (score * 2) + 1;
      finished = true;
      continue;
    }

    // 모양에 따라 공의 방향을 바꾸고 점수를 추가한다.
    int shape = block_map.cells[r][c].shape;
    switch (shape) {
      case -1:
        finished = true;
        break;
      case 0:
        break;
      case 1:
      case 2:
      case 3:
      case 4:
        m = hit_ball(m, shape);
        score += 1;
        break;
      case 5:
        score = (score * 2) + 1;
        finished = true;
        break;
      default:
        int num = shape - 6;
        array<pair<Spot, Spot>, 5> worms = block_map.worms;
        if (worms[num].first.row == r && worms[num].first.col == c) {
          r = worms[num].second.row;
          c = worms[num].second.col;
        } else {
          r = worms[num].first.row;
          c = worms[num].first.col;
        }
        break;
    }
  }

  // 점수를 반환한다.
  return score;
}

// 해당 핀볼 맵에서 나올 수 있는 최대 점수를 구한다.
auto find_max_score(BlockMap& block_map) -> int {
  // 기본 정보를 꺼낸다.
  vector<vector<Cell>>& cells = block_map.cells;
  int map_size = block_map.map_size;

  // 모든 지점과 방향을 출발 상태로 삼아 점수를 기록한다.
  int max_score = 0;
  for (int r = 0; r < map_size; r++) {
    for (int c = 0; c < map_size; c++) {
      if (cells[r][c].shape != 0) {
        continue;
      }
      for (int m = 0; m < MOVE_TYPES; m++) {
        int score = simulate(block_map, r, c, m);
        max_score = max(max_score, score);
        cells[r][c].is_start = false;
      }
    }
  }

  return max_score;
}

// 각 테스트 케이스를 수행한다.
auto test(int test_number) -> void {
  // 맵의 크기 입력을 받는다.
  int map_size;
  cin >> map_size;

  // 맵의 세부적인 정보를 입력받는다.
  vector<vector<Cell>> cells(map_size, vector<Cell>(map_size));
  unordered_set<int> found_worms;
  array<pair<Spot, Spot>, 5> worms;
  for (int r = 0; r < map_size; r++) {
    for (int c = 0; c < map_size; c++) {
      int shape;
      cin >> shape;
      cells[r][c].shape = shape;
      if (shape >= BASE_WORM) {
        int worm_index = shape - BASE_WORM;
        if (found_worms.find(shape) == found_worms.end()) {
          worms[worm_index].first = {r, c};
          found_worms.insert(shape);
        } else {
          worms[worm_index].second = {r, c};
        }
      }
    }
  }

  // 맵을 구성한다.
  BlockMap block_map = {map_size, move(cells), worms};

  // 최대 점수를 구하고 결과를 출력한다.
  int max_score = find_max_score(block_map);
  cout << "#" << (test_number + 1) << ' ' << max_score << '\n';
}

}  // namespace

// 프로그램의 시작점.
auto main() -> int {
  // 입출력 속도를 높인다.
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  // 테스트를 반복한다.
  int test_count;
  cin >> test_count;
  for (int i = 0; i < test_count; i++) {
    test(i);
  }
}