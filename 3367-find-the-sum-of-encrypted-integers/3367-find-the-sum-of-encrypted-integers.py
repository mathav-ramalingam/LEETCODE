class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        sum=0
        for n in map(str,nums):
            max_digit = max(n)  
            encrypted_value = int(max_digit * len(n))
            sum = sum + encrypted_value
        
        return sum
        

            # single line code 
        # return sum(int(max(list(str(n)))*len(str(n))) for n in nums)
