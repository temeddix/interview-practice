#include <cstdio>

int main() {
  char word[1000];
  scanf("%s", word);
  int index;
  scanf("%d", &index);
  printf("%c", word[index - 1]);
  return 0;
}