class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(nums,index,curr):
            if index == len(nums):
                res.append(curr)
                return
            
            helper(nums,index+1,curr)

            helper(nums,index+1,curr + [nums[index]])
        

        helper(nums,0,[])
        return res