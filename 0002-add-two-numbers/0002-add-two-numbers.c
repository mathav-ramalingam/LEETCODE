/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

    struct ListNode *head = NULL, *new_node, *current;
    int carry=0;
    while(l1 != NULL || l2 != NULL || carry)
    {
        int sum = carry;
     
        if(l1 != NULL)
        {
            sum = sum + l1->val;
            l1 = l1->next;
        }

        if(l2 != NULL)
        {
            sum = sum + l2->val;
            l2 = l2->next;
        }

        carry = sum /10;
        new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val = sum %10;
        new_node->next = NULL;
        if(head == NULL)
        {
            head = new_node;
            current =new_node;
        }
        else
        {
            current->next = new_node;
            current = new_node;
        }
    
    }

    return head;
}