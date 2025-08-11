class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # # Insertion sort (failed due to large list)
        # for i in range(1,len(nums)):
        #     anchor = nums[i]
        #     j = i - 1
        #     while j>=0 and anchor > nums[j]:
        #         nums[j+1] = nums[j]
        #         j = j -1
        #     nums[j+1] = anchor
        
        # return nums[k-1]


        ## quick sort
        # def swap(nums, a, b):
        #     nums[a], nums[b] = nums[b], nums[a]

        # def partition(nums, start, end):
        #     pivot_idx = start
        #     pivot = nums[pivot_idx]
        #     left = start + 1
        #     right = end

        #     while left <= right:
        #         while left <= right and nums[left] >= pivot:
        #             left += 1
        #         while left <= right and nums[right] < pivot:
        #             right -= 1
        #         if left <= right:
        #             swap(nums, left, right)
        #             left += 1
        #             right -= 1

        #     swap(nums, pivot_idx, right)
        #     return right

        # def quick_sort(nums, start, end):
        #     if start < end:
        #         mid = partition(nums, start, end)
        #         quick_sort(nums, start, mid - 1)
        #         quick_sort(nums, mid + 1, end)

        # quick_sort(nums, 0, len(nums) - 1)
        # return nums[k - 1]


        return sorted(nums, reverse =True)[k-1]
