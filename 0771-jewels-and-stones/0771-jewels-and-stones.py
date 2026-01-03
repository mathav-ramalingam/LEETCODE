class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n_j = 0
        jewels = set(jewels)
        for s in stones:
            if s in jewels:
                n_j +=1
        return n_j 