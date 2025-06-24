# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None 
        
        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next
        
        del_index = floor(count / 2)

        curr = head
        c = 0

        while curr:
            if c == del_index - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            c += 1

        return head

