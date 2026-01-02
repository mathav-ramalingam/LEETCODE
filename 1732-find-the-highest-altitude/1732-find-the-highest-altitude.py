class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = 0
        diff = 0
        for num in gain:
            diff = diff + num
            maxi = max(maxi,diff)
        

        return maxi