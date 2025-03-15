class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # my code
        # l = list(range(1,len(nums)+1))
        # res = []
        # for i in l:
        #     if i not in nums:
        #         res.append(i)

        # return res


        #cycle sort
        i = 0
        while i < len(nums):
            correct_pos = nums[i] - 1
            if nums[i] != nums[correct_pos]:
                nums[i] , nums[correct_pos] = nums[correct_pos] , nums[i]
            else:
                i=i+1

        res = []
        for i in range(len(nums)):
            if nums[i] == i+1:
                i=i+1
            else:
                res.append(i+1)


        return res


