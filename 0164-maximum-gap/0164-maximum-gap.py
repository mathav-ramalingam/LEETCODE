class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        max_gap = abs(nums[0] - nums[1])
        for i in range(1,len(nums)-1):
            if abs(nums[i] - nums[i+1]) >= max_gap:
                max_gap = abs(nums[i]- nums[i+1])
        
        return max_gap
             