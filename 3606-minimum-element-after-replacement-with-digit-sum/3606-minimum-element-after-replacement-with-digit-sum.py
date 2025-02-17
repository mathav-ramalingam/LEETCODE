class Solution:
    def minElement(self, nums: List[int]) -> int:

        for i in range(0,len(nums)):
            s = str(nums[i])
            sum = 0
            for u in s:
                sum = sum + int(u)
            nums[i] = sum


        return min(nums)