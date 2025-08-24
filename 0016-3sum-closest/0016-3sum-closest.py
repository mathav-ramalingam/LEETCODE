class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        
        # 1) closest_sum = float('inf')    # Initialize with a large value
        # 2) closest_sum = nums[0] + nums[1] + nums[2]
        # for i in range(len(nums) -2):
        #     for j in range(i+1 , len(nums)-1):
        #         for k in range(j+1 , len(nums)):
        #             current_sum = nums[i] + nums[j] + nums[k]
        #             if abs(current_sum - target) < abs(closest_sum - target):
        #                 closest_sum = current_sum
        
        # return closest_sum

        nums = sorted(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        difference = 2**31 - 1

        for i in range(len(nums)-2):
            n = nums[i]
            left = i+1
            right = len(nums)-1

            while left < right:
                new_sum = n + nums[left] + nums[right]

                if abs(new_sum - target) < difference:
                    difference = abs(new_sum - target)
                    closest_sum = new_sum

                if new_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
