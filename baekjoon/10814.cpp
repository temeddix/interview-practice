#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Person {
  int turn;
  int age;
  std::string name;
};

bool compare_people(Person& person_a, Person& person_b) {
  int age_a = person_a.age;
  int age_b = person_b.age;
  if (age_a != age_b) {
    return age_a < age_b;
  }
  return person_a.turn < person_b.turn;
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int count;
  std::cin >> count;
  std::vector<Person> people;
  people.reserve(count);

  for (int i = 0; i < count; i++) {
    int age;
    std::string name;
    std::cin >> age >> name;
    people.push_back(Person{
        i,
        age,
        name,
    });
  }

  std::sort(people.begin(), people.end(), compare_people);
  for (Person& person : people) {
    std::cout << person.age << ' ' << person.name << '\n';
  }

  return 0;
}