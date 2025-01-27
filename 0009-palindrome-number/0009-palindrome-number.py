class Solution:
    def isPalindrome(self, x: int) -> bool:
        # optimized solution
        str_x = str(x)
        rev_str = str_x[::-1]
        return str_x == rev_str


        # my solution________
        
        # if x<0:
        #     return False
        
        # rev_num =0
        # temp = x

        # while temp != 0:
        #     digit = temp % 10 
        #     rev_num = rev_num * 10 + digit 
        #     temp = temp // 10

        # return rev_num == x