class Solution:
    def isPowerOfThree(self, n: int) -> bool:


        # my solution one test is failed  (
        #     n =1
        #     Output : false
        #     Expected : true
        # )

        # if n < 0:
        #     return False
        # power_val , i = 0 , 1
        # while(power_val < n):
        #     power_val = pow(3,i)
        #     if power_val == n:
        #         return True
        #     i= i+1
        # return False

        if n<=0:
            return False
        while n % 3 ==0:
            n = n // 3
        return n==1


        