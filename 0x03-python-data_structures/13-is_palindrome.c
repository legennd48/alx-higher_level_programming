#include "lists.h"


/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer to head-node of list
 * Return: 0 if its not or 1 if it is palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev_slow = NULL;
	listint_t *second_half, *mid_node = NULL;
	int is_palindrome = 1;

	if (head == NULL || *head == NULL)
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

	second_half = reverse_list(&slow);
	is_palindrome = compare_lists(*head, second_half);

	reverse_list(&second_half);

	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}

	return (is_palindrome);
}

/**
 * reverse_list - Reverse a singly linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (prev);
}

/**
 * compare_lists - Compare two singly linked lists
 * @list1: pointer to the head of the first list
 * @list2: pointer to the head of the second list
 * Return: 1 if lists are the same, 0 otherwise
 */

int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}
