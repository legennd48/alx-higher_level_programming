#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer to head-node of list
 * Return: 0 if it's not or 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	unsigned int list_size = 0, index = 0;
	int *buff = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	while (current != NULL)
	{
		current = current->next;
		list_size += 1;
	}
	if (list_size == 1)
		return (1);
	buff = malloc(sizeof(int) * list_size);
	if (buff == NULL)
		return (0);
	current = *head;
	while (current != NULL && index < list_size)
	{
		buff[index++] = current->n;
		current = current->next;
	}
	for (index = 0; index <= (list_size / 2); index++)
	{
		if (buff[index] != buff[list_size - index - 1])
		{
			free(buff);
			return (0);
		}
	}

	free(buff);
	return (1);
}
