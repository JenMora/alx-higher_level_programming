#include "lists.h"

/**
*check_cycle - A C function that checks if a linked list contains a cycle
*@list: The linked list to be checked
*Return: 1 if the list has a cycle, otherwise 0
*/
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

if (!list)
return (0);

while (slow && fast && fast->next)
{
fast = fast->next->next;
slow = slow->next;
if (slow == fast)
return (1);
}
return (0);
}


