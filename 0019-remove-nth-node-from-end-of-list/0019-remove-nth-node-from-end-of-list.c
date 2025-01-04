/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverse(struct ListNode* head)
{
    struct ListNode* current=head, *prev=NULL,*nextp=NULL;
    while(current!= NULL)
    {
       nextp = current->next;
       current->next=prev;
       prev=current;
       current=nextp;
    }
    return prev;
}


struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
   
    head = reverse(head);
    struct ListNode *ptr = head, *tptr = NULL;
    if (n == 1)
    {
        head = ptr->next;
        free(ptr);
    } 
    else 
    {
        for (int i = 1; i < n; i++) {
            tptr = ptr;
            ptr = ptr->next;
        }
        tptr->next = ptr->next;
        free(ptr);
    }

    head = reverse(head);
    return head;
    
    
}