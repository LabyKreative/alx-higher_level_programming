#include "lists.h"

/**
 * is_palindrome - a functoin that checks if a singly
 * linked list is a palindrome.
 * @head: head node
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
        listint_t *current = *head;
        int tmp[100], x = 0, y = 0;

        if (!*head || !head || !current->next)
                return (1);

        while (current)
        {
            tmp[x] = current->n;
            x++;
            current = current->next;
        }
        x--;
        while (y <= x)
        {
            if(tmp[y] != tmp[x])
                return (0);
            y++;
            x--;
        }
        return (1);
}
