#include <stdlib.h>
#include <stdio.h>

struct queue
{
    int val;
    struct queue *next;
};

/* Write your enqueue() and dequeue() functions here */
void enqueue(struct queue** head, struct queue* toadd)
{
    if(*head == NULL)
    {
        printf("head was null\n");
        *head = toadd;
        return;
    }
    struct queue* cur = *head;
    while(cur->next != NULL)
    {
        cur = cur->next;
    }
    cur->next = toadd;
}

struct queue *(dequeue)(struct queue** head)
{
    struct queue *oldhead = *head;
    if (oldhead == NULL)
    {
        head = NULL;
        return NULL;
    }

    *head = oldhead->next;
    return (oldhead);
}

/*****************************************************/

int main(int argc, char **argv)
{
    int i, num_items;
    struct queue *Q = NULL;
    struct queue *item;

    if (argc != 2)
    {
        printf("Usage: %s queue_size\n", argv[0]);
        return 0;
    }

    /* atoi() converts a string to an integer */
    num_items = atoi(argv[1]);

    /* load the queue with items: 0, 1, 2, 3, ... */
    for (i = 0; i < num_items; i++)
    {
        item = malloc(sizeof(*item));

        if (!item)
        {
            printf("Failed to malloc() item! Exiting...\n");
            return EXIT_FAILURE;
        }

        item->val = i;
        enqueue(&Q, item);
    }

    /* unload the queue and print the value of each item */
    while (item = dequeue(&Q))
    {
        printf("%d\n", item->val);
        free(item);
    }

    return 0;
}