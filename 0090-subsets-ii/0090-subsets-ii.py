class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []

        def helper(nums,index,curr):
            if index == len(nums):
                if curr not in res:
                    res.append(curr)
                return
            
            helper(nums,index+1,curr)

            helper(nums,index+1, curr + [nums[index]])



        helper(nums,0,[])
        return res