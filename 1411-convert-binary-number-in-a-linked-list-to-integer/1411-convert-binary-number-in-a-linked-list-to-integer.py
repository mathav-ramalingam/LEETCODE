# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        llstr = ""
        
        curr = head
        while curr:
            llstr = llstr + (str(curr.val))
            curr = curr.next
        
        base_10_number = int(llstr, 2)
        
        return base_10_number