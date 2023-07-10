#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list that checks whether a
 * linked list has a cycle in it
 * @i: The integer value stored in the node
 * @next: points to the next node
 * 
 */
typedef struct listint_s
{
    int i;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int i);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif/*LISTS_H*/
