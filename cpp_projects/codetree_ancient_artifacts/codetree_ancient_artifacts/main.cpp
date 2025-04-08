#include <algorithm>
#include <array>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

namespace {

constexpr int MAP_SIZE = 5;    // 지도의 가로, 세로 크기.
constexpr int PIECE_SIZE = 3;  // 유물로 인정되는 조각 묶음의 크기.
constexpr int REACH = 1;       // 회전 반경.

// 격자 위 좌표.
struct Spot {
  int row;
  int col;
};

// 움직임 벡터.
struct Move {
  int row;
  int col;
};

// 다양한 회전 방식 중 각각에 대한 정보.
struct RotationPlan {
  int score;
  int angle;
  Spot center;
};

// 회전 방식을 선택하는 것의 우선순위를 정한다.
auto operator<(RotationPlan& obj_a, RotationPlan& obj_b) -> bool {
  if (obj_a.score != obj_b.score) {
    // 점수는 클수록 좋다.
    return obj_a.score < obj_b.score;
  } else if (obj_a.angle != obj_b.angle) {
    // 회전각은 작을수록 좋다.
    return obj_a.angle > obj_b.angle;
  } else {
    // 열은 작을수록, 행은 작을수록 좋다.
    if (obj_a.center.col != obj_b.center.col) {
      return obj_a.center.col > obj_b.center.col;
    } else {
      return obj_a.center.row > obj_b.center.row;
    }
  }
}

// 격자 내의 칸들을 주어진 중심점과 각도(90도 단위)로 돌린다.
auto rotate(vector<vector<int>>& original, const Spot center, int angle)
    -> vector<vector<int>> {
  // 원본을 복제하여 새로운 격자 정보를 생성한다.
  vector<vector<int>> rotated = original;

  // 중심 정보를 얻는다.
  int r = center.row;
  int c = center.col;

  // 회전시킨다.
  for (int r_from = -REACH; r_from <= REACH; r_from++) {
    for (int c_from = -REACH; c_from <= REACH; c_from++) {
      int r_to = 0, c_to = 0;
      if (angle == 1) {
        // 90도 돌리는 경우
        r_to = c_from;
        c_to = -r_from;
      } else if (angle == 2) {
        // 180도 돌리는 경우
        r_to = -r_from;
        c_to = -c_from;
      } else if (angle == 3) {
        // 270도 돌리는 경우
        r_to = -c_from;
        c_to = r_from;
      }
      // 새로운 격자에 다시 작성한다.
      int r_dest = r + r_to, c_dest = c + c_to;
      int r_orig = r + r_from, c_orig = c + c_from;
      rotated[r_dest][c_dest] = original[r_orig][c_orig];
    }
  }

  return rotated;
}

constexpr array<Move, 4> MOVES = {{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};

// 3개 이상 연결된 동종 조각들의 위치를 파악한다.
auto collect_usable(vector<vector<int>>& values) -> vector<Spot> {
  // 정보를 담을 준비를 한다.
  vector<Spot> spots;

  // 각 조각을 시작 지점으로 삼아 인접한 동종 조각들을 모아 본다.
  vector<vector<bool>> visited(MAP_SIZE, vector<bool>(MAP_SIZE, false));
  for (int r = 0; r < MAP_SIZE; r++) {
    for (int c = 0; c < MAP_SIZE; c++) {
      // 이 시작 지점이 이미 탐색하였다면 스킵한다.
      if (visited[r][c]) {
        continue;
      }
      // DFS 방식으로 인접한 동종 조각을 모은다.
      vector<Spot> collected;
      int value = values[r][c];
      vector<Spot> dfs_stack = {{r, c}};
      while (!dfs_stack.empty()) {
        Spot curr_spot = dfs_stack.back();
        dfs_stack.pop_back();
        int curr_r = curr_spot.row, curr_c = curr_spot.col;
        if (visited[curr_r][curr_c]) {
          continue;
        } else if (values[curr_r][curr_c] != value) {
          continue;
        }
        visited[curr_r][curr_c] = true;
        collected.push_back({curr_r, curr_c});
        for (Move move : MOVES) {
          int r_diff = move.row, c_diff = move.col;
          int next_r = curr_r + r_diff, next_c = curr_c + c_diff;
          if (!(next_r >= 0 && next_r < MAP_SIZE)) {
            continue;
          } else if (!(next_c >= 0 && next_c < MAP_SIZE)) {
            continue;
          }
          dfs_stack.push_back({next_r, next_c});
        }
      }
      // 충분히 많이 수집되었다면 유물로 취급한다.
      if (collected.size() >= PIECE_SIZE) {
        for (Spot spot : collected) {
          spots.push_back(spot);
        }
      }
    }
  }

  // 없앨 조각들의 정보를 반환한다.
  return spots;
}

// 열이 작고, 행이 큰 빈 칸부터 채운다.
void fill_empty(vector<vector<int>>& values, queue<int>& extras) {
  for (int c = 0; c < MAP_SIZE; c++) {
    for (int r = MAP_SIZE - 1; r >= 0; r--) {
      if (values[r][c] == 0) {
        values[r][c] = extras.front();
        extras.pop();
      }
    }
  }
}

auto perform_turn(vector<vector<int>>& values, queue<int>& extras) -> int {
  // 이 턴에서 모은 점수를 기억한다.
  int score = 0;

  // 모든 회전 방식을 시도하여 비교한다.
  vector<RotationPlan> rotation_plans;
  for (int r = REACH; r < MAP_SIZE - REACH; r++) {
    for (int c = REACH; c < MAP_SIZE - REACH; c++) {
      for (int angle = 1; angle <= 3; angle++) {
        Spot center = {r, c};
        vector<vector<int>> rotated = rotate(values, center, angle);
        vector<Spot> usable = collect_usable(rotated);
        int plan_score = static_cast<int>(usable.size());
        rotation_plans.push_back({plan_score, angle, center});
      }
    }
  }

  // 기준에 부합하는 최선의 회전 방식을 고른다.
  sort(rotation_plans.begin(), rotation_plans.end());
  RotationPlan rotation_plan = rotation_plans.back();

  // 최선의 회전 방식으로 실제로 조각들을 회전시킨다.
  values = rotate(values, rotation_plan.center, rotation_plan.angle);

  // 유물을 골라 내고, 채우는 작업을 반복한다.
  while (true) {
    vector<Spot> usable = collect_usable(values);
    int new_score = static_cast<int>(usable.size());
    if (new_score == 0) {
      break;
    }
    score += new_score;
    for (Spot spot : usable) {
      values[spot.row][spot.col] = 0;
    }
    fill_empty(values, extras);
  }

  // 점수를 반환한다.
  return score;
}

}  // namespace

auto main() -> int {
  // 입출력 속도를 개선한다.
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  // 입력을 받는다.
  int turn_count, extra_count;
  cin >> turn_count >> extra_count;
  vector<vector<int>> values(MAP_SIZE, vector<int>(MAP_SIZE, 0));
  for (int r = 0; r < MAP_SIZE; r++) {
    for (int c = 0; c < MAP_SIZE; c++) {
      cin >> values[r][c];
    }
  }
  queue<int> extras;
  for (int i = 0; i < extra_count; i++) {
    int number;
    cin >> number;
    extras.push(number);
  }

  // 반복적으로 턴을 수행한다.
  for (int i = 0; i < turn_count; i++) {
    int score = perform_turn(values, extras);
    if (score == 0) {
      break;
    }
    cout << score << ' ';
  }
}
