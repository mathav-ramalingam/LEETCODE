class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        return nums2[0] - nums1[0]

