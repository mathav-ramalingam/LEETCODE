class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        res = 0
        sign = 1
        i = 0
        
        if s[i] == "-" or s[i] == "+":
            if s[i] == "-":
                sign = -1
            i = i + 1
        
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i = i + 1
        
        res = res * sign

    
        MAX_INT, MIN_INT = 2**31 - 1, -2**31
        if res > MAX_INT:
            return MAX_INT
        if res < MIN_INT:
            return MIN_INT
        
        return res

        
            