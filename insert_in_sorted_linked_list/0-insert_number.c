#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        if (current->n > number)
        {
            new->next = current;
            *head = new;
            return (new);
        }

        while (current->next != NULL && current->next->n <= number)
            current = current->next;
        if (current->next != NULL)
        {
            new->next = current->next;
            current->next = new;
        }
        else
        {
            current->next = new;
        }
    }

    return (new);
}