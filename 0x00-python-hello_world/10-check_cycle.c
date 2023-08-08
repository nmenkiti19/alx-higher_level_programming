#include "lists.h"
/**
 * check_cycle - function to check if linkedlist contains a cycle
 * @list: linked list to check for cycle
 *
 * Return: if the list has a cycle return 1, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_list = list;
	listint_t *fast_list = list;

	if (!list)
		return (0);
	while (slow_list && fast_list && fast_list->next)
	{
		slow_list = slow_list->next;
		fast_list = fast_list->next->next;
		if (slow_list == fast_list)
			return (1);
	}
	return (0);
}
