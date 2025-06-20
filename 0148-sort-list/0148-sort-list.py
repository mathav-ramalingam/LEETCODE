# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next
        
        l.sort()
        temp = head
        for num in l:
            temp.val = num
            temp= temp.next
        
        return head
        
