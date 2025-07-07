class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque()
        self.maxSize = k

    def enQueue(self, value: int) -> bool:
        if self.maxSize > 0:
            self.queue.append(value)
            self.maxSize -= 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.popleft()
            self.maxSize += 1
            return True
        return False

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.maxSize == 0:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()