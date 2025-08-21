class RandomizedCollection:

    def __init__(self):
        self.queue = []

    def insert(self, val: int) -> bool:
        if val in self.queue:
            self.queue.append(val)
            return False
        else:
            self.queue.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.queue:
            self.queue.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if len(self.queue) > 0:
            return random.choice(self.queue)
        else:
            return -1


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()