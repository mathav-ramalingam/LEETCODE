class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) -1

        while start <= end:
            if nums[start] % 2==0:
                nums[start] = 0
            else:
                nums[start] = 1
            
            if nums[end] % 2 == 0:
                nums[end] = 0
            else:
                nums[end] = 1
            
            start += 1
            end -= 1
        
        nums.sort()
        return nums