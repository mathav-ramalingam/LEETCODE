class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        rev_num =0
        temp = x

        while temp != 0:
            digit = temp % 10 
            rev_num = rev_num * 10 + digit 
            temp = temp // 10

        return rev_num == x