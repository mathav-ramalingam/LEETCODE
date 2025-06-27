class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = set()
        check = []

        for i in nums:
            if i not in val:
                val.add(i)
            else:
                check.append(i)
        
        for v in val:
            if v not in check:
                return v