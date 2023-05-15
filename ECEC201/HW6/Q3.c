/* Homework 6: Question 3
   Compile with: gcc -std=c89 -o Q3 Q3.c
   Then run your compiled program with: ./Q3
*/
#include <stdlib.h>
#include <stdio.h>

struct list
{
  int val;
  struct list *next;
};

/* from Lecture 6 */
void list_add_head(struct list **head, struct list *item)
{
  item->next = *head;
  *head = item;
}

/* from Lecture 6 (just for your reference) */
struct list *list_pop_head(struct list **head)
{
  struct list *cur;

  cur = *head;
  if (cur)
  {
    *head = cur->next;
    cur->next = NULL;
  }

  return cur;
}

/* you write this one! */
int list_count(struct list *head)
{
  if (head == NULL)
  {
    return -1;
  }
  int i = 0;
  struct list *cur =  head;
  while (cur->next != NULL)
  {
    i++;
    cur = cur->next;
  }
  return i;
}

/* you write this one! */
struct list *list_pop_tail(struct list **head)
{
  if (head == NULL)
  {
    return NULL;
  }
  printf("popping\n");
  struct list *cur =  *head;
  if (cur == NULL)
  {
    return NULL;
  }
  struct list * twos;
  if (cur->next != NULL)
  {
    twos = cur->next;
    while (twos->next != NULL)
    {
      cur = cur->next;
      twos = cur->next;
    }
    cur->next = NULL;
    twos->next = NULL;
    return twos;
  }
  else if(cur->next == NULL)
  {
    * head = NULL;
    return cur;
  }
}

int main()
{
  int i;
  struct list *item;
  struct list *head = NULL;

  /* load up the list with ten items */
  for (i = 0; i < 10; i++)
  {
    item = malloc(sizeof(*item));
    item->val = i;
    list_add_head(&head, item);
    printf("Added %p (val: %d) to list.\n", item, item->val);
  }
  if(head == NULL)
  {
    printf("badnews\n");
  }
  printf("# of items: %d\n", list_count(head));

  /* remove each item and print its value */
  while (item = list_pop_tail(&head))
  {
    printf("Removed %p (val: %d)\n", item, item->val);
    free(item);
  }

  return 0;
}