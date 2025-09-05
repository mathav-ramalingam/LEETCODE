# sliding window algo (two pointer with same side)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        mini = float('inf')
        subSum = 0

        while right < len(nums):
            subSum += nums[right]
            
            while subSum >= target:
                mini = min(mini , right - left + 1)
                subSum -= nums[left]
                left += 1

            right += 1
        

        return 0 if mini == float('inf') else mini