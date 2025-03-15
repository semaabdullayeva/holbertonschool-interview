#include "lists.h"

/**
 * check_cycle - check whether linked list has a cycle or not
 * @head: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *head)
{
    listint_t *tortoise = head;
    listint_t *hare = head;
    if (head == NULL)
    {
        return 0;
    }
    while (head->next != NULL)
    {
        tortoise = tortoise->next;
        hare = hare->next;
        head = head->next;
        if (head->next != NULL)
        {
            hare = hare->next;
            head = head->next;
        }
        else
        {
            return 0;
        }

        if (hare == tortoise)
        {
            return 1;
        }
    }
    return 0;
}