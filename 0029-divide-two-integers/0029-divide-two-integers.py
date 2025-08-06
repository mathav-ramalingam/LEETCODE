class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = math.trunc(dividend / divisor)
        if a > (2**31) - 1 :
            return (a -1)
        else:
            return a