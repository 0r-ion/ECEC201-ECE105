/* Homework 6: Question 1
   Compile with: gcc -std=c89 -o Q1 Q1.c
   Then run your compiled program with: ./Q1
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * duplicate(char * tcpy)
{
  int len = strlen(tcpy) + 1;
  char * ret = malloc(len * sizeof(tcpy));
  int i;
  for(i = 0; i < len; i++)
  {
    ret[i] = tcpy[i];
  }
  return ret;
}

int main()
{
  char *dst;

  char *test = "Simplicity is the ultimate sophistication.";

  dst = duplicate(test);

  printf("%s", dst);

  free(dst);

  return 0;
}