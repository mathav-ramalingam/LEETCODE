class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []

        def helper(nums, start, end):
            if start == end:
                if nums[:] not in perm:
                    perm.append(nums[:])
            
            for i in range(start,end+1):
                nums[start] , nums[i] = nums[i], nums[start]
                helper(nums, start+1, end)
                nums[start], nums[i] = nums[i] , nums[start]
        

        helper(nums,0,len(nums)-1)
        return perm