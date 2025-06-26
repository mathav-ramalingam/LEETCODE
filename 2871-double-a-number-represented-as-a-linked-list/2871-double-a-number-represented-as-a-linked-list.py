# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack  = []
        curr = head
  
        while curr:
            stack.append(curr.val)
            curr = curr.next

        carry = 0
        res_stack = []

        while stack:
            val = stack.pop()
            total = val * 2 + carry
            carry = total // 10
            res_stack.append(total % 10)
        
        if carry:
            res_stack.append(carry)

        dummy = ListNode(0)
        curr = dummy

        for val in reversed(res_stack):
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next