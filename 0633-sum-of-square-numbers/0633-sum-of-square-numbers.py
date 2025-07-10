class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False
        
        left , right = 0 , int(math.sqrt(c))
        
        while left <= right:
            s = left**2 + right**2
            if s == c:
                return True
            elif s < c:
                left += 1
            else:
                right -= 1

        return False 