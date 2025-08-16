class Solution:
    def countPrimes(self, n: int) -> int:
        # res = 0

        # def is_prime(val):
        #     if val <= 1:
        #         return False
            
        #     for i in range(2,int(val**0.5)+1):
        #         if val % i == 0:
        #             return False

        #     return True
        
        # primes = [val for val in range(0,n) if is_prime(val)]

        # return len(primes)

        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p < n:
            if is_prime[p]:

                for mul in range(p*p,n,p):
                    is_prime[mul] = False
            p += 1
        
        return sum(is_prime)
