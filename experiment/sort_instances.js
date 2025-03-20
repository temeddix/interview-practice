class Person {
  /**
   * @param {string} name
   * @param {number} age
   */
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  /**
   * @param {Person} other
   * @returns {number}
   */
  compare(other) {
    if (this.age < other.age) return -1;
    if (this.age > other.age) return 1;
    return 0;
  }
}

/**
 * @param {Person[]} people
 * @returns {Person[]}
 */
function sortPeopleByAge(people) {
  return people.sort((a, b) => a.compare(b));
}

function solution() {
  const people = [
    new Person("Alice", 30),
    new Person("Bob", 25),
    new Person("Charlie", 35),
  ];

  const sortedPeople = sortPeopleByAge(people);
  console.log(sortedPeople);
}

solution();
