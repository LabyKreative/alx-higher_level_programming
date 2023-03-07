#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struck listint_s - a singly linked list has a cycle in it.
 * @n: integer
 * @next: pointer to the next node
 * 
 * Description: singly linked list noe structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
void free_listin(listint_t *head);
int check_cycle(listint_t *list)

#endif /* LISTS_H */
