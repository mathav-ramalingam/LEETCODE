
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        freq = Counter(nums)
        for val,count in sorted(freq.items(), key = lambda x : (x[1], -x[0])):
            while count != 0:
                res.append(val)
                count -= 1
        
        return res