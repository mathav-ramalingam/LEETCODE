# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None : return head 

        curr = head

        odd = ListNode(0)
        odd_ptr = odd

        even = ListNode(0)
        even_ptr = even

        idx = 1
        while curr:
            if idx %2 == 0:
                even_ptr.next = curr
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = curr
                odd_ptr = odd_ptr.next
            curr = curr.next
            idx = idx+1
        
        even_ptr.next = None
        odd_ptr.next = even.next

        return odd.next