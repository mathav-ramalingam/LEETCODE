from collections import defaultdict
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.dicty = defaultdict(list)
        for key , val in enumerate(nums):
            self.dicty[val].append(key)

    def pick(self, target: int) -> int:
        indices = self.dicty[target]
        return random.choice(indices)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)