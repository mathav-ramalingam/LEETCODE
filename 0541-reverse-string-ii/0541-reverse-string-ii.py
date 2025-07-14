class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = len(s)
        s = list(s)

        for i in range(0,l,2*k):
            s[i:i+k] = reversed(s[i:i+k])
        
        return "".join(s)