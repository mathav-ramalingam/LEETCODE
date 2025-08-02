class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums,target):
            ans = [-1,-1]
            left_index = 0
            right_index = len(nums)-1


            while left_index <= right_index:
                mid_index = (left_index + right_index) // 2
                mid_val = nums[mid_index]

                if mid_val == target:
                    ans = [mid_index, mid_index]

                    l = mid_index -1
                    while l >= left_index and nums[l] == target:
                        ans[0] = l
                        l = l - 1
                    
                    r = mid_index + 1
                    while r <= right_index and nums[r] == target:
                        ans[1] = r
                        r = r + 1
                    break

                elif mid_val < target:
                    left_index = mid_index + 1
                else:
                    right_index = mid_index - 1
                
            return ans
        
        res = binary_search(nums,target)
        return res