class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)
        seen = set()
        ans = set()

        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1 ,l):
                    lastNum = target - nums[i] - nums[j] - nums[k]
                    if lastNum in seen:
                        arr = [nums[i], nums[j], nums[k], lastNum]
                        arr.sort()
                        ans.add(tuple(arr))
            seen.add(nums[i])

        return [list(x) for x in ans]