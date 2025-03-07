class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # my solution 
        # res = set()
        # for n in nums:
        #     if n not in res:
        #         res.add(n)
        #     else:
        #         return True
        # return False        

        # optimized solution
        if len(set(nums)) < len(nums):
            return True
        return False