/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {

    while(head != NULL && head->val == val)
    {
        struct ListNode* temp = head;
        head= head->next;
        free(temp);
    }


    struct ListNode* current=head;
    struct ListNode* prev;

    while(current != NULL)
    {
        if(current->val == val)
        {
            struct ListNode* temp = current;
            prev->next = current->next;
            current= current->next;
            free(temp);
        }
        else
        {
            prev = current;
            current = current->next;
        }
    }

    return head;    
}