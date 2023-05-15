/* Homework 6: Question 2
   Compile with: gcc -std=c89 -o Q2 Q2.c
   Then run your compiled program with: ./Q2
*/
#include <stdio.h>
#include <stdlib.h>

#define ELEMENTS 8

int * create_array(int n, int initial_value)
{
  int * ret = malloc(n*sizeof(int));
  if ( ret == NULL){
    return NULL;
  }
  int i;
  for(i = 0; i < n; i++)
  {
    ret[i] = initial_value;
  }
  return ret;
}

int main()
{
  int i;
  int *foo;

  foo = create_array(ELEMENTS, 79);

  if (foo)
    for (i=0; i<ELEMENTS; i++)    
      printf("%d: %d\n", i, foo[i]);

  free(foo);

  return 0;
}