#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
    if (list == NULL || list->next == NULL)
        return 0;

    listint_t *slow = list;
    listint_t *fast = list->next;

    while (fast != NULL && fast->next != NULL)
    {
        if (slow == fast)
            return 1;

        slow = slow->next;
        fast = fast->next->next;
    }

    return 0;
}
