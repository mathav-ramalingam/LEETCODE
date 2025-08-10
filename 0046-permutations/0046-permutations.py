from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [p for p in permutations(nums)]
        return perm