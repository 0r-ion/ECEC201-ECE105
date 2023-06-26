#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "list.h"

#define to_person(ptr) container_of(ptr, struct person, node)

struct person {
  char name[128];
  int age;
  int salary;
  int years;
  struct list node;
};

/* This function prints the provided struct person to the screen */
void print_person(struct person *p) {
  printf("Employee %s:\n", p->name);
  printf("   Age: %d\n", p->age);
  printf("Salary: $%0.2f\n", (float)p->salary / 100.0f);
  printf(" Years: %d\n", p->years);
}

/* This function must do the following:
 * 1. Open the provided filename
 * 2. Return The NULL Pointer if filename could not be opened
 * 3. Allocate a new list head on the heap
 * 4. Populate the list with data from the file
 * 5. Return the head of the populated list  */

struct list *load_database(const char *filename) {
  FILE *fp;
  fp = fopen("employees.csv", "r");
  if (fp == NULL) {
    printf("failed to open file\n");
    return NULL;
  }
  struct list *head;
  head = malloc(sizeof(*head));
  list_init(head);
  struct person *item;
  int ret;

  while (1) {
    item = malloc(sizeof(*item));
    ret = fscanf(fp, "%[^,], %d, %d, %d\n", item->name, &item->age, &item->salary, &item->years);
    if (ret == EOF) {
      break;
    }
    /*print_person(item);*/
    list_add_after(head, &item->node);
  }
  return head;
}

/* This function must do the following:
 * 1. Remove all items from the provided list
 * 2. Free each removed item from the heap */
void unload_database(struct list *head) {
  struct list *cur, *sav;
  struct person *item;

  list_safe_for(head, cur,sav){
    list_remove(cur);
    item = to_person(cur);
    /*print_person(item);*/
    free(item);
  }
}

/* This function must do the following:
 * 1. Search the provided list for the item having the provided name
 * 2. Return the item if found
 * 3. Return The NULL Pointer if not found */
struct person *find_person(struct list *head, const char *name) {
  struct list *cur;
  char * p_name;
  struct person *item;
  list_for(head, cur){
    item = to_person(cur);
    if (0 == strcmp(name, item->name)){
      return item;
    }
    cur = cur->next;
  }
  return NULL;
}


int main(int argc, char **argv) {
  struct list *head;
  struct person *item;

  if (argc != 2) {
    fprintf(stderr, "Usage: %s employee_name\n", argv[0]);
    return EXIT_FAILURE;
  }

  head = load_database("employees.csv");

  if (!head) {
    fprintf(stderr, "Failed to open database.\n");
    return EXIT_FAILURE;
  }

  item = find_person(head, argv[1]);
  if (item)
    print_person(item);
  else
    printf("Employee NOT FOUND!\n");

  unload_database(head);
  free(head);

  return 0;
}