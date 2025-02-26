#include <iostream>
#include <vector>

using namespace std;

struct Question {
  int start;
  int end;
};

auto give_answers(vector<int>& numbers, vector<Question>& questions)
    -> vector<bool> {
  vector<int> checked_sizes((numbers.size() * 2) - 1, 0);

  vector<bool> answers;
  answers.reserve(questions.size());

  for (Question question : questions) {
    // Check the recorded symmetry.
    int doubled_mid = question.start + question.end;
    int doubled_size = (question.end - question.start);

    // Update the symmetry.
    bool is_mid_integer = doubled_mid % 2 == 0;  // Mid can be `N.0` or `N.5`

    int size = checked_sizes[doubled_mid] + 1;
    int end = (doubled_mid / 2) + size;
    int start = (doubled_mid / 2) - size + (is_mid_integer ? 0 : 1);
    while (end - start <= doubled_size) {
      if (numbers[start] != numbers[end]) {
        break;
      }
      start -= 1;
      end += 1;
    }
    start += 1;
    end -= 1;

    // Remember.
    int checked_size = (end - start + 1) / 2;
    checked_sizes[doubled_mid] = checked_size;

    // Give an answer.
    answers.push_back(checked_size >= (doubled_size + 1) / 2);
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