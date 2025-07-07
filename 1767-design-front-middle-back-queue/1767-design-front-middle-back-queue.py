class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = deque()

    def pushFront(self, val: int) -> None:
        self.queue.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        if self.queue:
            idx = math.floor(len(self.queue) / 2)
            self.queue.insert(idx,val)
        else:
            self.queue.append(val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if self.queue:
            return self.queue.popleft()
        return -1

    def popMiddle(self) -> int:
        if self.queue:
            idx = math.floor((len(self.queue)-1)/2)
            x = self.queue[idx]
            del self.queue[idx]
            return x
        return -1

    def popBack(self) -> int:
        if self.queue:
            return self.queue.pop()
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()