class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_ele = nums[0]
        index =0
        for i in range(1,len(nums)):
            if nums[i] > max_ele:
                max_ele = nums[i]
                index = i

        return index