class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = 0
        num = abs(x)
        while num > 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num = num // 10
        
        reversed_num = reversed_num if x>0 else -reversed_num

        MAX_INT , MIN_INT = 2**31-1 , -2**31
        if reversed_num > MAX_INT or reversed_num < MIN_INT:
            return 0
        else:
            return reversed_num