class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
    
    def sizeofLL(self):
        count = 0
        temp = self.head

        while temp:
            count = count+1
            temp = temp.next
        return count

    def get(self, index: int) -> int:
        if index < 0 or index >= self.sizeofLL():
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val if curr else -1


    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return

        node = Node(val,self.head)
        self.head = node 
        

    def addAtTail(self, val: int) -> None:

        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 and index > self.sizeofLL():
            return -1
        
        if index == 0:
            self.addAtHead(val)
            return
        
        prev = 0
        curr = self.head
        while curr:
            if prev == index-1:
                node = Node(val,curr.next)
                curr.next = node
                break
            curr = curr.next
            prev = prev +1
        

    def deleteAtIndex(self, index: int) -> None:
        size = self.sizeofLL()
        if index < 0 or index >= size:
            return

        if self.head is None:
            return  

        if index == 0:
            self.head = self.head.next  # Safe now
            return

        prev = 0
        temp = self.head
        while temp:
            if prev == index - 1 and temp.next:
                temp.next = temp.next.next
                break
            temp = temp.next
            prev += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)