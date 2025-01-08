/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {

    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val = 0;  
    dummy->next = head;

    struct ListNode* prev = dummy;
    
    for (int i = 0; i < left - 1; i++) {
        prev = prev->next;
    }
    
    struct ListNode* curr = prev->next; 


    for (int i = 0; i < right - left; i++) 
    {
        struct ListNode* forw = curr->next; 
        curr->next = forw->next;
        forw->next = prev->next;
        prev->next = forw;
    }
    
    struct ListNode* newHead = dummy->next;
    free(dummy); 
    return newHead;
}