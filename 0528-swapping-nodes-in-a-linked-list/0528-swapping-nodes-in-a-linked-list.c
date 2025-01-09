/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapNodes(struct ListNode* head, int k) {
    struct ListNode* sp = head;
    struct ListNode* fp = head;
    for(int i=0;i<k-1;i++){
        fp=fp->next;
    }
    struct ListNode* n1 = fp;
    while(fp->next!=NULL){
        fp = fp->next;
        sp = sp->next;
    }
    struct ListNode* n2 = sp;
    int temp = n1->val;
    n1->val = n2->val;
    n2->val = temp;
    return head;
}