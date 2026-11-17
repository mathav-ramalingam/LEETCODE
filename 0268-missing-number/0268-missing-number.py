class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums) 

        excepted_sum = n * (n+1) // 2
        actual_sum = sum(nums)

        return excepted_sum - actual_sum 