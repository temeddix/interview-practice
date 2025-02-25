#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int pokemon_count = 0;
  int question_count = 0;
  std::cin >> pokemon_count >> question_count;

  std::vector<std::string> pokemons;
  std::unordered_map<std::string, int> indexes;
  pokemons.reserve(100000);
  for (int i = 0; i < pokemon_count; i++) {
    std::string pokemon;
    std::cin >> pokemon;
    pokemons.push_back(pokemon);
    indexes[pokemon] = i;
  }

  for (int i = 0; i < question_count; i++) {
    std::string question;
    std::cin >> question;
    char first_letter = question[0];
    if ('0' <= first_letter && first_letter <= '9') {
      int number = std::stoi(question) - 1;
      std::cout << pokemons[number] << '\n';
    } else {
      std::cout << indexes[question] + 1 << '\n';
    }
  }
}