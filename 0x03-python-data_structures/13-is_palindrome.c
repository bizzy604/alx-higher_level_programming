#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = *head;
    listint_t *second_half;
    listint_t *mid_node = NULL;
    int is_palindrome = 1; // Assume the list is a palindrome

    if (*head == NULL || (*head)->next == NULL)
        return is_palindrome; // Empty list or single node list is a palindrome

    // Find the middle node of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // Handling odd length lists
    if (fast != NULL)
    {
        mid_node = slow;
        slow = slow->next;
    }

    // Reverse the second half of the list
    second_half = reverse_list(&slow);
    prev_slow->next = NULL; // Terminate the first half of the list

    // Compare the first half with the reversed second half
    while (*head != NULL && second_half != NULL)
    {
        if ((*head)->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }
        *head = (*head)->next;
        second_half = second_half->next;
    }

    // Reconstruct the original list and free the reversed second half
    second_half = reverse_list(&slow);
    if (mid_node != NULL)
    {
        prev_slow->next = mid_node;
        mid_node->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return is_palindrome;
}
