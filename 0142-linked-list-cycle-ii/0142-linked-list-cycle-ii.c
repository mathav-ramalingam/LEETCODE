/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    if(head == NULL || head->next == NULL)
    {
        return NULL;
    }

    struct ListNode* fast=head;
    struct ListNode* slow=head;

    while(fast!=NULL  && fast->next !=NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast)
        {
            slow = head;
            while(slow != fast)
            {
                slow = slow->next;
                fast = fast->next;
            }
            return slow;
        }
    }

    return NULL;
    
}