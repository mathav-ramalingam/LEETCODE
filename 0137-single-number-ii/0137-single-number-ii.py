from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # # my idealogy

        # val = set()
        # check = []

        # for i in nums:
        #     if i not in val:
        #         val.add(i)
        #     else:
        #         check.append(i)
        
        # for v in val:
        #     if v not in check:
        #         return v

        # using counter class
        freq = Counter(nums)

        for key , count in freq.items():
            if count == 1:
                return key
