/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {

    if (!head || !head->next || k == 0) {
        return head; // Handle edge cases
    }

    int length =1;
    struct ListNode *temp=head;
    while(temp->next)
    {
        temp=temp->next;
        length++;
    }

    // to calculate the no of rotations need,if k too high
    k = k % length;  
    if(k == 0)
    {
        return head;
    }


    for(int i=0;i<k;i++)
    {
        temp=head;
        struct ListNode* ptr= NULL;
        while(temp->next != NULL)
        {
            ptr = temp;
            temp= temp->next;
        }

        ptr->next = NULL;
        temp->next =head;
        head= temp;
    }
    return head;
    
}