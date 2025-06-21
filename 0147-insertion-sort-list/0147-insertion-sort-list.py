# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # s = ''
        # curr = head

        # while curr:
        #     s = s + str(curr.val)
        #     curr = curr.next
        
        # l = []
        # for num in s:
        #     l.append(int(num))
        
        # l.sort()
        # print(l)

        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next
        
        l.sort()
        temp = head
        for num in l:
            temp.val = num
            temp = temp.next
        
        return head