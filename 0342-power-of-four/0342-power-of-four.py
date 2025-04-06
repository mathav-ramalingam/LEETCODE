class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(n):
            power_of_4 = 4**i

            if power_of_4 == n:
                return True 

            if power_of_4 > n:
                return False
        return False

            