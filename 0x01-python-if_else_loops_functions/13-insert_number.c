#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *tracer = *head;

	if (!new || !head)
		return (0);
	new->n = number;

	if (!tracer)
	{
		*head = new;
		new->next = 0;
		return (new);
	}

	while (tracer)
	{
		if (tracer->next)
		{

			if (number < tracer->n)
			{
				new->next = tracer;
				*head = new;
				return (new);
			}

			if (number >= tracer->n && number < tracer->next->n)
			{
				new->next = tracer->next;
				tracer->next = new;
				return (new);
			}
		}
		else
		{
			tracer->next = new;
			new->next = 0;
		}
		tracer = tracer->next;
	}
	return (new);
}
