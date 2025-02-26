#include <iostream>
#include <vector>

using namespace std;

struct Question {
  int start;
  int end;
};

struct Symmetry {
  int checked_size;  // Ceiling value of the one-way distance
  bool reached_limit;
};

auto give_answers(vector<int>& numbers, vector<Question>& questions)
    -> vector<bool> {
  vector<Symmetry> symmetries((numbers.size() * 2) - 1, {0, false});
  vector<bool> answers;
  answers.reserve(questions.size());

  for (Question question : questions) {
    // Check the recorded symmetry.
    int doubled_mid = question.start + question.end;
    int doubled_size = (question.end - question.start);
    Symmetry& symmetry = symmetries[doubled_mid];

    // Update the symmetry.
    if (!symmetry.reached_limit) {
      int size = symmetry.checked_size + 1;
      bool is_mid_integer = doubled_mid % 2 == 0;  // Mid can be `N.0` or `N.5`

      int end_index = (doubled_mid / 2) + size;
      int start_index = (doubled_mid / 2) - size + (is_mid_integer ? 0 : 1);
      while (end_index - start_index <= doubled_size) {
        if (numbers[start_index] != numbers[end_index]) {
          symmetry.reached_limit = true;
          break;
        }
        start_index -= 1;
        end_index += 1;
      }
      start_index += 1;
      end_index -= 1;
      symmetry.checked_size = (end_index - start_index + 1) / 2;
    }

    // Give an answer.
    answers.push_back(symmetry.checked_size >= (doubled_size + 1) / 2);
  }

  return answers;
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int number_count = 0;
  cin >> number_count;

  vector<int> numbers;
  numbers.reserve(number_count);
  for (int i = 0; i < number_count; i++) {
    int number = 0;
    cin >> number;
    numbers.push_back(number);
  }

  int question_count = 0;
  cin >> question_count;
  vector<Question> questions;
  questions.reserve(question_count);
  for (int i = 0; i < question_count; i++) {
    int start_raw = 0;
    int end_raw = 0;
    cin >> start_raw >> end_raw;
    questions.push_back({start_raw - 1, end_raw - 1});
  }

  vector<bool> answers = give_answers(numbers, questions);
  for (bool answer : answers) {
    cout << answer << '\n';
  }
}