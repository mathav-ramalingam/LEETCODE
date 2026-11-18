class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        
        size = len(nums)
        stack = deque()
        result = [-1] * size

        for i in range(2*size-1, -1, -1):
            idx = i % size

            while stack and stack[-1] <= nums[idx]:
                stack.pop()
            
            if stack:
                result[idx] = stack[-1]

            stack.append(nums[idx])
        
        return result