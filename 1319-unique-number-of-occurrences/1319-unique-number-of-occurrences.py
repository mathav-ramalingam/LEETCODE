class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # num = set()
        # for n in arr:
        #     if n in num:
        #         return True
        #     num.add(n)
        # return False


        freq = Counter(arr)              
        nums = set()
        for count in freq.values():
            if count in nums:
                return False             
            nums.add(count)
        return True     
        