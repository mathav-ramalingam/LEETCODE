/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(!head)
    {
        return head;
    }
    struct ListNode* prev=NULL , *current=head, *nextp= current->next;
    while(nextp)
    {
        if(current->val == nextp->val)
        {
            while(nextp && nextp->val == current->val )
            {
                nextp =  nextp->next;
            }
            if(!prev)
            {
                head=nextp;
            }
            else
            {
                prev->next = nextp;
            }
        }
        else
        {
            prev = current;
        }


        current = nextp;
        if(nextp)
        {
            nextp = current->next;
        }
    }

    return head;
}