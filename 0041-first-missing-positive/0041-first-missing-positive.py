class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # my code (time exceed)

        # l = len(nums)

        # test = set(range(1,l+1))
        
        # for n in test:
        #     if n not in nums:
        #         return n

        # return l+1

        i = 0
        n = len(nums)
        while i < n:
            correct_pos = nums[i] - 1
            if 0 <= correct_pos < n and  nums[i] != nums[correct_pos]:
                nums[i] , nums[correct_pos] = nums[correct_pos] , nums[i]
            else:
                i = i+1

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        
        return n + 1
            
        