class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # my logic

        # res = []
        # nums.sort()
        # for i in range(0,len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         res.append(nums[i])

        # return res

        seen = set()
        res = []

        for n in nums:
            if n in seen:
                res.append(n)
            else:
                seen.add(n)

        return res


