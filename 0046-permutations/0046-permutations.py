# using built-in func

# from itertools import permutations

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         perm = [p for p in permutations(nums)]
#         return perm



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = []
        def helper(nums, start, end):
            if start == end:
                perm.append(nums[:])
                return
            
            for i in range(start,end+1):
                nums[start] , nums[i] = nums[i], nums[start]
                helper(nums,start+1,end)
                nums[start], nums[i] = nums[i], nums[start]

        helper(nums,0,len(nums)-1)
        return perm