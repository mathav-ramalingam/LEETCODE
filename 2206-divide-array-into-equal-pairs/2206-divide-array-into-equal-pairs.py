class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for val,count in freq.items():
            if count % 2 != 0:
                return False

        return True