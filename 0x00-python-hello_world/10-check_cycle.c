#include "lists.h"

/**
 * check_cycle - checks a singly linked list for a cycle
 * @list: head of linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1 = list;
	listint_t *temp2 = list;

	while (temp2 != NULL && temp2->next != NULL)
	{
		temp1 = temp1->next;
		temp2 = temp2->next->next;

		if (temp1 == temp2)
		{
			return (1);
		}
	}

	return (0);

	/* works but not efficient */
	/* while (list != NULL) */
	/* { */
	/* 	temp = list; */
	/* 	while (list != NULL) */
	/* 	{ */
	/* 		list = list->next; */
	/* 		if (temp == list) */
	/* 		{ */
	/* 			return (1); */
	/* 		} */
	/* 	} */
	/* } */
	/* return (0); */
}
