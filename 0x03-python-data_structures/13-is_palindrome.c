#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer to head-node of list
 * Return: 0 if it's not or 1 if it is a palindrome
 */
int is_palindrome(head)
listint_t **head;
{
	listint_t *slow = *head, *fast = *head, *prev_slow = NULL;
	int is_palindrome = 1;
	listint_t *first_half = *head, *second_half = slow,  *mid_node = NULL;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}
	/* Compare the first and second halves of the list while traversing. */
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	/* Restore the second half to its original order. */
	prev_slow->next = mid_node;
	return (is_palindrome);
}
