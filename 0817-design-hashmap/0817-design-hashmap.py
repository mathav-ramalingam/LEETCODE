class MyHashMap:

    def __init__(self):
        self.dicty =  {}

    def put(self, key: int, value: int) -> None:
        self.dicty[key] = value

    def get(self, key: int) -> int:
        return self.dicty[key] if key in self.dicty else -1

    def remove(self, key: int) -> None:
        if key in self.dicty:
            del self.dicty[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)