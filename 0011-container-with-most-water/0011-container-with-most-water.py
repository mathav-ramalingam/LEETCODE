from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxi = 0
        while(left < right):
            area = (right - left) * min(height[left], height[right])
            maxi = max(maxi, area)
            if height[left] < height[right]:
                left= left+1
            else:
                right = right -1
        
        return maxi