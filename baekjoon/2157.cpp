#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

constexpr int INVALID = -1'000'000'007;

struct Flight {
  int origin_city;
  int score;
};

struct City {
  vector<Flight> incomings;  // Cities that one can fly from
  vector<int> scores;        // Maximum score per number of visited cities
};

void fill_scores(vector<City>& cities, int stop_count) {
  for (City& city : cities) {
    for (Flight flight : city.incomings) {
      for (int visited = 1; visited <= stop_count; visited++) {
        int origin_score = cities[flight.origin_city].scores[visited - 1];
        if (origin_score == INVALID) {
          continue;
        }
        int new_score = origin_score + flight.score;
        city.scores[visited] = max(city.scores[visited], new_score);
      }
    }
  }
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int city_count = 0;
  int stop_count = 0;
  int flight_count = 0;
  cin >> city_count >> stop_count >> flight_count;

  vector<City> cities(
      city_count, City{vector<Flight>(), vector<int>(stop_count + 1, INVALID)});
  cities[0].scores[1] = 0;

  for (int i = 0; i < flight_count; i++) {
    int city_a = 0;
    int city_b = 0;
    int score = 0;
    cin >> city_a >> city_b >> score;
    city_a -= 1;
    city_b -= 1;
    if (city_a > city_b) {
      continue;
    }
    cities[city_b].incomings.push_back({city_a, score});
  }

  fill_scores(cities, stop_count);
  vector<int>& final_scores = cities.back().scores;
  cout << *max_element(final_scores.begin(), final_scores.end()) << '\n';
}