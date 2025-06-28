class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # one test is failed in the code 
                # Input nums1 = [1], nums2 = [3] 
                # Use Testcase : Output [3] 
                #                Expected []

        # res = set()

        # n1 = len(nums1)
        # n2 = len(nums2)

        # client = nums1 if n1<n2 else nums2
        # server = nums1 if n1>n2 else nums2

        # for val in client:
        #     if val in server:
        #         res.add(val)

        # return list(res)
        
        nums1 = set(nums1)
        nums2 = set(nums2)

        return list(nums1 & nums2)

