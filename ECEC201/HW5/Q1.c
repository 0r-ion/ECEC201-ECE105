/* Homework 5: Question 1
   Compile with: gcc -std=c89 -o Q1 Q1.c
   Then run your compiled program with: ./Q1
*/

#include <stdio.h>


int g(int val)
{
  return val * val;
}


/* Your sum function goes here */
int sum(int (*func)(int value), int i, int j){
    int icpy;
    int running_total;

    for( icpy=i; icpy <= j; icpy++ ){
        running_total += func(icpy);
    }

    return running_total;
}


int main()
{
  printf("Result: %d\n", sum(g, 10, 20));

  return 0;
}
