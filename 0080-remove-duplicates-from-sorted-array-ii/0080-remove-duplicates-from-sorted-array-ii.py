from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = nums

        dicty = Counter(nums)
        for key , val in dicty.items():
            while val > 2:
                res.remove(key)
                val = val-1
               
        print(res)