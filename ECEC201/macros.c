#include <stddef.h>
#include <stdio.h>
#include <string.h>

/*
  Hash tables (python dictionaries)
  python example > bob = staff["bob"]
  c ex{
    struct employee *bob;

    bob = dict_peek(&staff, "bob");
    |^^---------------------------|
    |address of data stored        |
    |------------------------------|
  }

*/
struct list {
  struct list *next;
  struct list *prev;
};

struct dict {
  struct list **bins;
  unsigned int nbins;
  void (*deleter)(void *user_data);
};
