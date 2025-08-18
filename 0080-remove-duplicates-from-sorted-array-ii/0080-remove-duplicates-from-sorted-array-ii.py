from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        dicty = Counter(nums)
        for key , val in dicty.items():
            while val > 2:
                nums.remove(key)
                val = val-1
               
        print(nums)