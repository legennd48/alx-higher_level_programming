#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to be inserted
 * Return: pointer to inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *temp = NULL;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
	new->n = number;
	temp = *head;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	while (temp->next != NULL && number > temp->next->n)
		temp = temp->next;
	new->next = temp->next;
	temp->next = new;
	return (new);
}
